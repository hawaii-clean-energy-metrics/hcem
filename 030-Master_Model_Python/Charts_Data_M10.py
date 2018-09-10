# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_Data_M10 = Worksheet('Charts_Data_M10', 10, 10)



@register(Charts_Data_M10)
class A1():
    # 'Charts_Data_M10'!A1
    value = "Metric 10:"

@register(Charts_Data_M10)
class F1():
    # 'Charts_Data_M10'!F1
    value = "Notes"

@register(Charts_Data_M10)
class G1():
    # 'Charts_Data_M10'!G1
    value = 1999

@register(Charts_Data_M10)
class H1():
    # 'Charts_Data_M10'!H1
    value = 2000

@register(Charts_Data_M10)
class I1():
    # 'Charts_Data_M10'!I1
    value = 2001

@register(Charts_Data_M10)
class J1():
    # 'Charts_Data_M10'!J1
    value = 2002

@register(Charts_Data_M10)
class K1():
    # 'Charts_Data_M10'!K1
    value = 2003

@register(Charts_Data_M10)
class L1():
    # 'Charts_Data_M10'!L1
    value = 2004

@register(Charts_Data_M10)
class M1():
    # 'Charts_Data_M10'!M1
    value = 2005

@register(Charts_Data_M10)
class N1():
    # 'Charts_Data_M10'!N1
    value = 2006

@register(Charts_Data_M10)
class O1():
    # 'Charts_Data_M10'!O1
    value = 2007

@register(Charts_Data_M10)
class P1():
    # 'Charts_Data_M10'!P1
    value = 2008

@register(Charts_Data_M10)
class Q1():
    # 'Charts_Data_M10'!Q1
    value = 2009

@register(Charts_Data_M10)
class R1():
    # 'Charts_Data_M10'!R1
    value = 2010

@register(Charts_Data_M10)
class S1():
    # 'Charts_Data_M10'!S1
    value = 2011

@register(Charts_Data_M10)
class T1():
    # 'Charts_Data_M10'!T1
    value = 2012

@register(Charts_Data_M10)
class U1():
    # 'Charts_Data_M10'!U1
    value = 2013

@register(Charts_Data_M10)
class V1():
    # 'Charts_Data_M10'!V1
    value = 2014

@register(Charts_Data_M10)
class W1():
    # 'Charts_Data_M10'!W1
    value = 2015

@register(Charts_Data_M10)
class X1():
    # 'Charts_Data_M10'!X1
    value = 2016

@register(Charts_Data_M10)
class Y1():
    # 'Charts_Data_M10'!Y1
    value = 2017

@register(Charts_Data_M10)
class Z1():
    # 'Charts_Data_M10'!Z1
    value = 2018

@register(Charts_Data_M10)
class AA1():
    # 'Charts_Data_M10'!AA1
    value = 2019

@register(Charts_Data_M10)
class AB1():
    # 'Charts_Data_M10'!AB1
    value = 2020

@register(Charts_Data_M10)
class AC1():
    # 'Charts_Data_M10'!AC1
    value = 2021

@register(Charts_Data_M10)
class AD1():
    # 'Charts_Data_M10'!AD1
    value = 2022

@register(Charts_Data_M10)
class AE1():
    # 'Charts_Data_M10'!AE1
    value = 2023

@register(Charts_Data_M10)
class AF1():
    # 'Charts_Data_M10'!AF1
    value = 2024

@register(Charts_Data_M10)
class AG1():
    # 'Charts_Data_M10'!AG1
    value = 2025

@register(Charts_Data_M10)
class AH1():
    # 'Charts_Data_M10'!AH1
    value = 2026

@register(Charts_Data_M10)
class AI1():
    # 'Charts_Data_M10'!AI1
    value = 2027

@register(Charts_Data_M10)
class AJ1():
    # 'Charts_Data_M10'!AJ1
    value = 2028

@register(Charts_Data_M10)
class AK1():
    # 'Charts_Data_M10'!AK1
    value = 2029

@register(Charts_Data_M10)
class AL1():
    # 'Charts_Data_M10'!AL1
    value = 2030

@register(Charts_Data_M10)
class A2():
    # 'Charts_Data_M10'!A2
    value = "RPS Chart Title"

@register(Charts_Data_M10)
class B2():
    # 'Charts_Data_M10'!B2
    value = "Renewable Electricity Generated in 2015"
    formula = '''="Renewable Electricity Generated in "&'Charts Data M10'!C9'''
    @eval_fn
    def B2():
        c9_1 = Charts_Data_M10.C9()
        var_1 = concat("Renewable Electricity Generated in ", c9_1)
        return var_1

@register(Charts_Data_M10)
class F2():
    # 'Charts_Data_M10'!F2
    value = "Notes"

@register(Charts_Data_M10)
class B3():
    # 'Charts_Data_M10'!B3
    value = "Renewable Generation as Percent of Total Sales in 2015"
    formula = '''="Renewable Generation as Percent of Total Sales in "&'Charts Data M10'!C9'''
    @eval_fn
    def B3():
        c9_1 = Charts_Data_M10.C9()
        var_1 = concat("Renewable Generation as Percent of Total Sales in ", c9_1)
        return var_1

@register(Charts_Data_M10)
class F3():
    # 'Charts_Data_M10'!F3
    value = "Notes"

@register(Charts_Data_M10)
class A4():
    # 'Charts_Data_M10'!A4
    value = "Line Graph Input 1"

@register(Charts_Data_M10)
class D4():
    # 'Charts_Data_M10'!D4
    value = "Total"

@register(Charts_Data_M10)
class F4():
    # 'Charts_Data_M10'!F4
    value = "Notes"

@register(Charts_Data_M10)
class G4():
    # 'Charts_Data_M10'!G4
    value = 0.140685946105
    formula = "=IF(ISERROR('Dashboard M10 RPS'!G138),NA(),'Dashboard M10 RPS'!G138)"
    @eval_fn
    def G4():
        g138_1 = Dashboard_M10_RPS.G138()
        var_1 = ISERROR(g138_1)
        var_2 = NA()
        g138_2 = Dashboard_M10_RPS.G138()
        var_3 = IF(var_1, var_2, g138_2)
        return var_3

@register(Charts_Data_M10)
class H4():
    # 'Charts_Data_M10'!H4
    value = 0.175069685961
    formula = "=IF(ISERROR('Dashboard M10 RPS'!H138),NA(),'Dashboard M10 RPS'!H138)"
    @eval_fn
    def H4():
        h138_1 = Dashboard_M10_RPS.H138()
        var_1 = ISERROR(h138_1)
        var_2 = NA()
        h138_2 = Dashboard_M10_RPS.H138()
        var_3 = IF(var_1, var_2, h138_2)
        return var_3

@register(Charts_Data_M10)
class I4():
    # 'Charts_Data_M10'!I4
    value = 0.156667174115
    formula = "=IF(ISERROR('Dashboard M10 RPS'!I138),NA(),'Dashboard M10 RPS'!I138)"
    @eval_fn
    def I4():
        i138_1 = Dashboard_M10_RPS.I138()
        var_1 = ISERROR(i138_1)
        var_2 = NA()
        i138_2 = Dashboard_M10_RPS.I138()
        var_3 = IF(var_1, var_2, i138_2)
        return var_3

@register(Charts_Data_M10)
class J4():
    # 'Charts_Data_M10'!J4
    value = 0.129793727507
    formula = "=IF(ISERROR('Dashboard M10 RPS'!J138),NA(),'Dashboard M10 RPS'!J138)"
    @eval_fn
    def J4():
        j138_1 = Dashboard_M10_RPS.J138()
        var_1 = ISERROR(j138_1)
        var_2 = NA()
        j138_2 = Dashboard_M10_RPS.J138()
        var_3 = IF(var_1, var_2, j138_2)
        return var_3

@register(Charts_Data_M10)
class K4():
    # 'Charts_Data_M10'!K4
    value = 0.165501115749
    formula = "=IF(ISERROR('Dashboard M10 RPS'!K138),NA(),'Dashboard M10 RPS'!K138)"
    @eval_fn
    def K4():
        k138_1 = Dashboard_M10_RPS.K138()
        var_1 = ISERROR(k138_1)
        var_2 = NA()
        k138_2 = Dashboard_M10_RPS.K138()
        var_3 = IF(var_1, var_2, k138_2)
        return var_3

@register(Charts_Data_M10)
class L4():
    # 'Charts_Data_M10'!L4
    value = 0.175089079901
    formula = "=IF(ISERROR('Dashboard M10 RPS'!L138),NA(),'Dashboard M10 RPS'!L138)"
    @eval_fn
    def L4():
        l138_1 = Dashboard_M10_RPS.L138()
        var_1 = ISERROR(l138_1)
        var_2 = NA()
        l138_2 = Dashboard_M10_RPS.L138()
        var_3 = IF(var_1, var_2, l138_2)
        return var_3

@register(Charts_Data_M10)
class M4():
    # 'Charts_Data_M10'!M4
    value = 0.169517031403
    formula = "=IF(ISERROR('Dashboard M10 RPS'!M138),NA(),'Dashboard M10 RPS'!M138)"
    @eval_fn
    def M4():
        m138_1 = Dashboard_M10_RPS.M138()
        var_1 = ISERROR(m138_1)
        var_2 = NA()
        m138_2 = Dashboard_M10_RPS.M138()
        var_3 = IF(var_1, var_2, m138_2)
        return var_3

@register(Charts_Data_M10)
class N4():
    # 'Charts_Data_M10'!N4
    value = 0.204137387828
    formula = "=IF(ISERROR('Dashboard M10 RPS'!N138),NA(),'Dashboard M10 RPS'!N138)"
    @eval_fn
    def N4():
        n138_1 = Dashboard_M10_RPS.N138()
        var_1 = ISERROR(n138_1)
        var_2 = NA()
        n138_2 = Dashboard_M10_RPS.N138()
        var_3 = IF(var_1, var_2, n138_2)
        return var_3

@register(Charts_Data_M10)
class O4():
    # 'Charts_Data_M10'!O4
    value = 0.222782315884
    formula = "=IF(ISERROR('Dashboard M10 RPS'!O138),NA(),'Dashboard M10 RPS'!O138)"
    @eval_fn
    def O4():
        o138_1 = Dashboard_M10_RPS.O138()
        var_1 = ISERROR(o138_1)
        var_2 = NA()
        o138_2 = Dashboard_M10_RPS.O138()
        var_3 = IF(var_1, var_2, o138_2)
        return var_3

@register(Charts_Data_M10)
class P4():
    # 'Charts_Data_M10'!P4
    value = 0.234702545853
    formula = "=IF(ISERROR('Dashboard M10 RPS'!P138),NA(),'Dashboard M10 RPS'!P138)"
    @eval_fn
    def P4():
        p138_1 = Dashboard_M10_RPS.P138()
        var_1 = ISERROR(p138_1)
        var_2 = NA()
        p138_2 = Dashboard_M10_RPS.P138()
        var_3 = IF(var_1, var_2, p138_2)
        return var_3

@register(Charts_Data_M10)
class Q4():
    # 'Charts_Data_M10'!Q4
    value = 0.237635646443
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Q138),NA(),'Dashboard M10 RPS'!Q138)"
    @eval_fn
    def Q4():
        q138_1 = Dashboard_M10_RPS.Q138()
        var_1 = ISERROR(q138_1)
        var_2 = NA()
        q138_2 = Dashboard_M10_RPS.Q138()
        var_3 = IF(var_1, var_2, q138_2)
        return var_3

@register(Charts_Data_M10)
class R4():
    # 'Charts_Data_M10'!R4
    value = 0.237004899189
    formula = "=IF(ISERROR('Dashboard M10 RPS'!R138),NA(),'Dashboard M10 RPS'!R138)"
    @eval_fn
    def R4():
        r138_1 = Dashboard_M10_RPS.R138()
        var_1 = ISERROR(r138_1)
        var_2 = NA()
        r138_2 = Dashboard_M10_RPS.R138()
        var_3 = IF(var_1, var_2, r138_2)
        return var_3

@register(Charts_Data_M10)
class S4():
    # 'Charts_Data_M10'!S4
    value = 0.297679064526
    formula = "=IF(ISERROR('Dashboard M10 RPS'!S138),NA(),'Dashboard M10 RPS'!S138)"
    @eval_fn
    def S4():
        s138_1 = Dashboard_M10_RPS.S138()
        var_1 = ISERROR(s138_1)
        var_2 = NA()
        s138_2 = Dashboard_M10_RPS.S138()
        var_3 = IF(var_1, var_2, s138_2)
        return var_3

@register(Charts_Data_M10)
class T4():
    # 'Charts_Data_M10'!T4
    value = 0.345024369608
    formula = "=IF(ISERROR('Dashboard M10 RPS'!T138),NA(),'Dashboard M10 RPS'!T138)"
    @eval_fn
    def T4():
        t138_1 = Dashboard_M10_RPS.T138()
        var_1 = ISERROR(t138_1)
        var_2 = NA()
        t138_2 = Dashboard_M10_RPS.T138()
        var_3 = IF(var_1, var_2, t138_2)
        return var_3

@register(Charts_Data_M10)
class U4():
    # 'Charts_Data_M10'!U4
    value = 0.452207177191
    formula = "=IF(ISERROR('Dashboard M10 RPS'!U138),NA(),'Dashboard M10 RPS'!U138)"
    @eval_fn
    def U4():
        u138_1 = Dashboard_M10_RPS.U138()
        var_1 = ISERROR(u138_1)
        var_2 = NA()
        u138_2 = Dashboard_M10_RPS.U138()
        var_3 = IF(var_1, var_2, u138_2)
        return var_3

@register(Charts_Data_M10)
class V4():
    # 'Charts_Data_M10'!V4
    value = 0.532673712018
    formula = "=IF(ISERROR('Dashboard M10 RPS'!V138),NA(),'Dashboard M10 RPS'!V138)"
    @eval_fn
    def V4():
        v138_1 = Dashboard_M10_RPS.V138()
        var_1 = ISERROR(v138_1)
        var_2 = NA()
        v138_2 = Dashboard_M10_RPS.V138()
        var_3 = IF(var_1, var_2, v138_2)
        return var_3

@register(Charts_Data_M10)
class W4():
    # 'Charts_Data_M10'!W4
    value = 0.585495074013
    formula = "=IF(ISERROR('Dashboard M10 RPS'!W138),NA(),'Dashboard M10 RPS'!W138)"
    @eval_fn
    def W4():
        w138_1 = Dashboard_M10_RPS.W138()
        var_1 = ISERROR(w138_1)
        var_2 = NA()
        w138_2 = Dashboard_M10_RPS.W138()
        var_3 = IF(var_1, var_2, w138_2)
        return var_3

@register(Charts_Data_M10)
class X4():
    # 'Charts_Data_M10'!X4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!X138),NA(),'Dashboard M10 RPS'!X138)"
    @eval_fn
    def X4():
        x138_1 = Dashboard_M10_RPS.X138()
        var_1 = ISERROR(x138_1)
        var_2 = NA()
        x138_2 = Dashboard_M10_RPS.X138()
        var_3 = IF(var_1, var_2, x138_2)
        return var_3

@register(Charts_Data_M10)
class Y4():
    # 'Charts_Data_M10'!Y4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Y138),NA(),'Dashboard M10 RPS'!Y138)"
    @eval_fn
    def Y4():
        y138_1 = Dashboard_M10_RPS.Y138()
        var_1 = ISERROR(y138_1)
        var_2 = NA()
        y138_2 = Dashboard_M10_RPS.Y138()
        var_3 = IF(var_1, var_2, y138_2)
        return var_3

@register(Charts_Data_M10)
class Z4():
    # 'Charts_Data_M10'!Z4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Z138),NA(),'Dashboard M10 RPS'!Z138)"
    @eval_fn
    def Z4():
        z138_1 = Dashboard_M10_RPS.Z138()
        var_1 = ISERROR(z138_1)
        var_2 = NA()
        z138_2 = Dashboard_M10_RPS.Z138()
        var_3 = IF(var_1, var_2, z138_2)
        return var_3

@register(Charts_Data_M10)
class AA4():
    # 'Charts_Data_M10'!AA4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AA138),NA(),'Dashboard M10 RPS'!AA138)"
    @eval_fn
    def AA4():
        aa138_1 = Dashboard_M10_RPS.AA138()
        var_1 = ISERROR(aa138_1)
        var_2 = NA()
        aa138_2 = Dashboard_M10_RPS.AA138()
        var_3 = IF(var_1, var_2, aa138_2)
        return var_3

@register(Charts_Data_M10)
class AB4():
    # 'Charts_Data_M10'!AB4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AB138),NA(),'Dashboard M10 RPS'!AB138)"
    @eval_fn
    def AB4():
        ab138_1 = Dashboard_M10_RPS.AB138()
        var_1 = ISERROR(ab138_1)
        var_2 = NA()
        ab138_2 = Dashboard_M10_RPS.AB138()
        var_3 = IF(var_1, var_2, ab138_2)
        return var_3

@register(Charts_Data_M10)
class AC4():
    # 'Charts_Data_M10'!AC4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AC138),NA(),'Dashboard M10 RPS'!AC138)"
    @eval_fn
    def AC4():
        ac138_1 = Dashboard_M10_RPS.AC138()
        var_1 = ISERROR(ac138_1)
        var_2 = NA()
        ac138_2 = Dashboard_M10_RPS.AC138()
        var_3 = IF(var_1, var_2, ac138_2)
        return var_3

@register(Charts_Data_M10)
class AD4():
    # 'Charts_Data_M10'!AD4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AD138),NA(),'Dashboard M10 RPS'!AD138)"
    @eval_fn
    def AD4():
        ad138_1 = Dashboard_M10_RPS.AD138()
        var_1 = ISERROR(ad138_1)
        var_2 = NA()
        ad138_2 = Dashboard_M10_RPS.AD138()
        var_3 = IF(var_1, var_2, ad138_2)
        return var_3

@register(Charts_Data_M10)
class AE4():
    # 'Charts_Data_M10'!AE4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AE138),NA(),'Dashboard M10 RPS'!AE138)"
    @eval_fn
    def AE4():
        ae138_1 = Dashboard_M10_RPS.AE138()
        var_1 = ISERROR(ae138_1)
        var_2 = NA()
        ae138_2 = Dashboard_M10_RPS.AE138()
        var_3 = IF(var_1, var_2, ae138_2)
        return var_3

@register(Charts_Data_M10)
class AF4():
    # 'Charts_Data_M10'!AF4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AF138),NA(),'Dashboard M10 RPS'!AF138)"
    @eval_fn
    def AF4():
        af138_1 = Dashboard_M10_RPS.AF138()
        var_1 = ISERROR(af138_1)
        var_2 = NA()
        af138_2 = Dashboard_M10_RPS.AF138()
        var_3 = IF(var_1, var_2, af138_2)
        return var_3

@register(Charts_Data_M10)
class AG4():
    # 'Charts_Data_M10'!AG4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AG138),NA(),'Dashboard M10 RPS'!AG138)"
    @eval_fn
    def AG4():
        ag138_1 = Dashboard_M10_RPS.AG138()
        var_1 = ISERROR(ag138_1)
        var_2 = NA()
        ag138_2 = Dashboard_M10_RPS.AG138()
        var_3 = IF(var_1, var_2, ag138_2)
        return var_3

@register(Charts_Data_M10)
class AH4():
    # 'Charts_Data_M10'!AH4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AH138),NA(),'Dashboard M10 RPS'!AH138)"
    @eval_fn
    def AH4():
        ah138_1 = Dashboard_M10_RPS.AH138()
        var_1 = ISERROR(ah138_1)
        var_2 = NA()
        ah138_2 = Dashboard_M10_RPS.AH138()
        var_3 = IF(var_1, var_2, ah138_2)
        return var_3

@register(Charts_Data_M10)
class AI4():
    # 'Charts_Data_M10'!AI4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AI138),NA(),'Dashboard M10 RPS'!AI138)"
    @eval_fn
    def AI4():
        ai138_1 = Dashboard_M10_RPS.AI138()
        var_1 = ISERROR(ai138_1)
        var_2 = NA()
        ai138_2 = Dashboard_M10_RPS.AI138()
        var_3 = IF(var_1, var_2, ai138_2)
        return var_3

@register(Charts_Data_M10)
class AJ4():
    # 'Charts_Data_M10'!AJ4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AJ138),NA(),'Dashboard M10 RPS'!AJ138)"
    @eval_fn
    def AJ4():
        aj138_1 = Dashboard_M10_RPS.AJ138()
        var_1 = ISERROR(aj138_1)
        var_2 = NA()
        aj138_2 = Dashboard_M10_RPS.AJ138()
        var_3 = IF(var_1, var_2, aj138_2)
        return var_3

@register(Charts_Data_M10)
class AK4():
    # 'Charts_Data_M10'!AK4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AK138),NA(),'Dashboard M10 RPS'!AK138)"
    @eval_fn
    def AK4():
        ak138_1 = Dashboard_M10_RPS.AK138()
        var_1 = ISERROR(ak138_1)
        var_2 = NA()
        ak138_2 = Dashboard_M10_RPS.AK138()
        var_3 = IF(var_1, var_2, ak138_2)
        return var_3

@register(Charts_Data_M10)
class AL4():
    # 'Charts_Data_M10'!AL4
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AL138),NA(),'Dashboard M10 RPS'!AL138)"
    @eval_fn
    def AL4():
        al138_1 = Dashboard_M10_RPS.AL138()
        var_1 = ISERROR(al138_1)
        var_2 = NA()
        al138_2 = Dashboard_M10_RPS.AL138()
        var_3 = IF(var_1, var_2, al138_2)
        return var_3

@register(Charts_Data_M10)
class D5():
    # 'Charts_Data_M10'!D5
    value = "HECO"

@register(Charts_Data_M10)
class F5():
    # 'Charts_Data_M10'!F5
    value = "Notes"

@register(Charts_Data_M10)
class G5():
    # 'Charts_Data_M10'!G5
    value = 0.0908535230051
    formula = "=IF(ISERROR('Dashboard M10 RPS'!G133),NA(),'Dashboard M10 RPS'!G133)"
    @eval_fn
    def G5():
        g133_1 = Dashboard_M10_RPS.G133()
        var_1 = ISERROR(g133_1)
        var_2 = NA()
        g133_2 = Dashboard_M10_RPS.G133()
        var_3 = IF(var_1, var_2, g133_2)
        return var_3

@register(Charts_Data_M10)
class H5():
    # 'Charts_Data_M10'!H5
    value = 0.112659456461
    formula = "=IF(ISERROR('Dashboard M10 RPS'!H133),NA(),'Dashboard M10 RPS'!H133)"
    @eval_fn
    def H5():
        h133_1 = Dashboard_M10_RPS.H133()
        var_1 = ISERROR(h133_1)
        var_2 = NA()
        h133_2 = Dashboard_M10_RPS.H133()
        var_3 = IF(var_1, var_2, h133_2)
        return var_3

@register(Charts_Data_M10)
class I5():
    # 'Charts_Data_M10'!I5
    value = 0.104095094132
    formula = "=IF(ISERROR('Dashboard M10 RPS'!I133),NA(),'Dashboard M10 RPS'!I133)"
    @eval_fn
    def I5():
        i133_1 = Dashboard_M10_RPS.I133()
        var_1 = ISERROR(i133_1)
        var_2 = NA()
        i133_2 = Dashboard_M10_RPS.I133()
        var_3 = IF(var_1, var_2, i133_2)
        return var_3

@register(Charts_Data_M10)
class J5():
    # 'Charts_Data_M10'!J5
    value = 0.110622462788
    formula = "=IF(ISERROR('Dashboard M10 RPS'!J133),NA(),'Dashboard M10 RPS'!J133)"
    @eval_fn
    def J5():
        j133_1 = Dashboard_M10_RPS.J133()
        var_1 = ISERROR(j133_1)
        var_2 = NA()
        j133_2 = Dashboard_M10_RPS.J133()
        var_3 = IF(var_1, var_2, j133_2)
        return var_3

@register(Charts_Data_M10)
class K5():
    # 'Charts_Data_M10'!K5
    value = 0.122374368519
    formula = "=IF(ISERROR('Dashboard M10 RPS'!K133),NA(),'Dashboard M10 RPS'!K133)"
    @eval_fn
    def K5():
        k133_1 = Dashboard_M10_RPS.K133()
        var_1 = ISERROR(k133_1)
        var_2 = NA()
        k133_2 = Dashboard_M10_RPS.K133()
        var_3 = IF(var_1, var_2, k133_2)
        return var_3

@register(Charts_Data_M10)
class L5():
    # 'Charts_Data_M10'!L5
    value = 0.119423251002
    formula = "=IF(ISERROR('Dashboard M10 RPS'!L133),NA(),'Dashboard M10 RPS'!L133)"
    @eval_fn
    def L5():
        l133_1 = Dashboard_M10_RPS.L133()
        var_1 = ISERROR(l133_1)
        var_2 = NA()
        l133_2 = Dashboard_M10_RPS.L133()
        var_3 = IF(var_1, var_2, l133_2)
        return var_3

@register(Charts_Data_M10)
class M5():
    # 'Charts_Data_M10'!M5
    value = 0.10795233778
    formula = "=IF(ISERROR('Dashboard M10 RPS'!M133),NA(),'Dashboard M10 RPS'!M133)"
    @eval_fn
    def M5():
        m133_1 = Dashboard_M10_RPS.M133()
        var_1 = ISERROR(m133_1)
        var_2 = NA()
        m133_2 = Dashboard_M10_RPS.M133()
        var_3 = IF(var_1, var_2, m133_2)
        return var_3

@register(Charts_Data_M10)
class N5():
    # 'Charts_Data_M10'!N5
    value = 0.128392416569
    formula = "=IF(ISERROR('Dashboard M10 RPS'!N133),NA(),'Dashboard M10 RPS'!N133)"
    @eval_fn
    def N5():
        n133_1 = Dashboard_M10_RPS.N133()
        var_1 = ISERROR(n133_1)
        var_2 = NA()
        n133_2 = Dashboard_M10_RPS.N133()
        var_3 = IF(var_1, var_2, n133_2)
        return var_3

@register(Charts_Data_M10)
class O5():
    # 'Charts_Data_M10'!O5
    value = 0.10674267101
    formula = "=IF(ISERROR('Dashboard M10 RPS'!O133),NA(),'Dashboard M10 RPS'!O133)"
    @eval_fn
    def O5():
        o133_1 = Dashboard_M10_RPS.O133()
        var_1 = ISERROR(o133_1)
        var_2 = NA()
        o133_2 = Dashboard_M10_RPS.O133()
        var_3 = IF(var_1, var_2, o133_2)
        return var_3

@register(Charts_Data_M10)
class P5():
    # 'Charts_Data_M10'!P5
    value = 0.120108465342
    formula = "=IF(ISERROR('Dashboard M10 RPS'!P133),NA(),'Dashboard M10 RPS'!P133)"
    @eval_fn
    def P5():
        p133_1 = Dashboard_M10_RPS.P133()
        var_1 = ISERROR(p133_1)
        var_2 = NA()
        p133_2 = Dashboard_M10_RPS.P133()
        var_3 = IF(var_1, var_2, p133_2)
        return var_3

@register(Charts_Data_M10)
class Q5():
    # 'Charts_Data_M10'!Q5
    value = 0.128531378426
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Q133),NA(),'Dashboard M10 RPS'!Q133)"
    @eval_fn
    def Q5():
        q133_1 = Dashboard_M10_RPS.Q133()
        var_1 = ISERROR(q133_1)
        var_2 = NA()
        q133_2 = Dashboard_M10_RPS.Q133()
        var_3 = IF(var_1, var_2, q133_2)
        return var_3

@register(Charts_Data_M10)
class R5():
    # 'Charts_Data_M10'!R5
    value = 0.118454771727
    formula = "=IF(ISERROR('Dashboard M10 RPS'!R133),NA(),'Dashboard M10 RPS'!R133)"
    @eval_fn
    def R5():
        r133_1 = Dashboard_M10_RPS.R133()
        var_1 = ISERROR(r133_1)
        var_2 = NA()
        r133_2 = Dashboard_M10_RPS.R133()
        var_3 = IF(var_1, var_2, r133_2)
        return var_3

@register(Charts_Data_M10)
class S5():
    # 'Charts_Data_M10'!S5
    value = 0.167358872051
    formula = "=IF(ISERROR('Dashboard M10 RPS'!S133),NA(),'Dashboard M10 RPS'!S133)"
    @eval_fn
    def S5():
        s133_1 = Dashboard_M10_RPS.S133()
        var_1 = ISERROR(s133_1)
        var_2 = NA()
        s133_2 = Dashboard_M10_RPS.S133()
        var_3 = IF(var_1, var_2, s133_2)
        return var_3

@register(Charts_Data_M10)
class T5():
    # 'Charts_Data_M10'!T5
    value = 0.19024272663
    formula = "=IF(ISERROR('Dashboard M10 RPS'!T133),NA(),'Dashboard M10 RPS'!T133)"
    @eval_fn
    def T5():
        t133_1 = Dashboard_M10_RPS.T133()
        var_1 = ISERROR(t133_1)
        var_2 = NA()
        t133_2 = Dashboard_M10_RPS.T133()
        var_3 = IF(var_1, var_2, t133_2)
        return var_3

@register(Charts_Data_M10)
class U5():
    # 'Charts_Data_M10'!U5
    value = 0.29197521162
    formula = "=IF(ISERROR('Dashboard M10 RPS'!U133),NA(),'Dashboard M10 RPS'!U133)"
    @eval_fn
    def U5():
        u133_1 = Dashboard_M10_RPS.U133()
        var_1 = ISERROR(u133_1)
        var_2 = NA()
        u133_2 = Dashboard_M10_RPS.U133()
        var_3 = IF(var_1, var_2, u133_2)
        return var_3

@register(Charts_Data_M10)
class V5():
    # 'Charts_Data_M10'!V5
    value = 0.379357429186
    formula = "=IF(ISERROR('Dashboard M10 RPS'!V133),NA(),'Dashboard M10 RPS'!V133)"
    @eval_fn
    def V5():
        v133_1 = Dashboard_M10_RPS.V133()
        var_1 = ISERROR(v133_1)
        var_2 = NA()
        v133_2 = Dashboard_M10_RPS.V133()
        var_3 = IF(var_1, var_2, v133_2)
        return var_3

@register(Charts_Data_M10)
class W5():
    # 'Charts_Data_M10'!W5
    value = 0.429232584201
    formula = "=IF(ISERROR('Dashboard M10 RPS'!W133),NA(),'Dashboard M10 RPS'!W133)"
    @eval_fn
    def W5():
        w133_1 = Dashboard_M10_RPS.W133()
        var_1 = ISERROR(w133_1)
        var_2 = NA()
        w133_2 = Dashboard_M10_RPS.W133()
        var_3 = IF(var_1, var_2, w133_2)
        return var_3

@register(Charts_Data_M10)
class X5():
    # 'Charts_Data_M10'!X5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!X133),NA(),'Dashboard M10 RPS'!X133)"
    @eval_fn
    def X5():
        x133_1 = Dashboard_M10_RPS.X133()
        var_1 = ISERROR(x133_1)
        var_2 = NA()
        x133_2 = Dashboard_M10_RPS.X133()
        var_3 = IF(var_1, var_2, x133_2)
        return var_3

@register(Charts_Data_M10)
class Y5():
    # 'Charts_Data_M10'!Y5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Y133),NA(),'Dashboard M10 RPS'!Y133)"
    @eval_fn
    def Y5():
        y133_1 = Dashboard_M10_RPS.Y133()
        var_1 = ISERROR(y133_1)
        var_2 = NA()
        y133_2 = Dashboard_M10_RPS.Y133()
        var_3 = IF(var_1, var_2, y133_2)
        return var_3

@register(Charts_Data_M10)
class Z5():
    # 'Charts_Data_M10'!Z5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Z133),NA(),'Dashboard M10 RPS'!Z133)"
    @eval_fn
    def Z5():
        z133_1 = Dashboard_M10_RPS.Z133()
        var_1 = ISERROR(z133_1)
        var_2 = NA()
        z133_2 = Dashboard_M10_RPS.Z133()
        var_3 = IF(var_1, var_2, z133_2)
        return var_3

@register(Charts_Data_M10)
class AA5():
    # 'Charts_Data_M10'!AA5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AA133),NA(),'Dashboard M10 RPS'!AA133)"
    @eval_fn
    def AA5():
        aa133_1 = Dashboard_M10_RPS.AA133()
        var_1 = ISERROR(aa133_1)
        var_2 = NA()
        aa133_2 = Dashboard_M10_RPS.AA133()
        var_3 = IF(var_1, var_2, aa133_2)
        return var_3

@register(Charts_Data_M10)
class AB5():
    # 'Charts_Data_M10'!AB5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AB133),NA(),'Dashboard M10 RPS'!AB133)"
    @eval_fn
    def AB5():
        ab133_1 = Dashboard_M10_RPS.AB133()
        var_1 = ISERROR(ab133_1)
        var_2 = NA()
        ab133_2 = Dashboard_M10_RPS.AB133()
        var_3 = IF(var_1, var_2, ab133_2)
        return var_3

@register(Charts_Data_M10)
class AC5():
    # 'Charts_Data_M10'!AC5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AC133),NA(),'Dashboard M10 RPS'!AC133)"
    @eval_fn
    def AC5():
        ac133_1 = Dashboard_M10_RPS.AC133()
        var_1 = ISERROR(ac133_1)
        var_2 = NA()
        ac133_2 = Dashboard_M10_RPS.AC133()
        var_3 = IF(var_1, var_2, ac133_2)
        return var_3

@register(Charts_Data_M10)
class AD5():
    # 'Charts_Data_M10'!AD5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AD133),NA(),'Dashboard M10 RPS'!AD133)"
    @eval_fn
    def AD5():
        ad133_1 = Dashboard_M10_RPS.AD133()
        var_1 = ISERROR(ad133_1)
        var_2 = NA()
        ad133_2 = Dashboard_M10_RPS.AD133()
        var_3 = IF(var_1, var_2, ad133_2)
        return var_3

@register(Charts_Data_M10)
class AE5():
    # 'Charts_Data_M10'!AE5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AE133),NA(),'Dashboard M10 RPS'!AE133)"
    @eval_fn
    def AE5():
        ae133_1 = Dashboard_M10_RPS.AE133()
        var_1 = ISERROR(ae133_1)
        var_2 = NA()
        ae133_2 = Dashboard_M10_RPS.AE133()
        var_3 = IF(var_1, var_2, ae133_2)
        return var_3

@register(Charts_Data_M10)
class AF5():
    # 'Charts_Data_M10'!AF5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AF133),NA(),'Dashboard M10 RPS'!AF133)"
    @eval_fn
    def AF5():
        af133_1 = Dashboard_M10_RPS.AF133()
        var_1 = ISERROR(af133_1)
        var_2 = NA()
        af133_2 = Dashboard_M10_RPS.AF133()
        var_3 = IF(var_1, var_2, af133_2)
        return var_3

@register(Charts_Data_M10)
class AG5():
    # 'Charts_Data_M10'!AG5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AG133),NA(),'Dashboard M10 RPS'!AG133)"
    @eval_fn
    def AG5():
        ag133_1 = Dashboard_M10_RPS.AG133()
        var_1 = ISERROR(ag133_1)
        var_2 = NA()
        ag133_2 = Dashboard_M10_RPS.AG133()
        var_3 = IF(var_1, var_2, ag133_2)
        return var_3

@register(Charts_Data_M10)
class AH5():
    # 'Charts_Data_M10'!AH5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AH133),NA(),'Dashboard M10 RPS'!AH133)"
    @eval_fn
    def AH5():
        ah133_1 = Dashboard_M10_RPS.AH133()
        var_1 = ISERROR(ah133_1)
        var_2 = NA()
        ah133_2 = Dashboard_M10_RPS.AH133()
        var_3 = IF(var_1, var_2, ah133_2)
        return var_3

@register(Charts_Data_M10)
class AI5():
    # 'Charts_Data_M10'!AI5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AI133),NA(),'Dashboard M10 RPS'!AI133)"
    @eval_fn
    def AI5():
        ai133_1 = Dashboard_M10_RPS.AI133()
        var_1 = ISERROR(ai133_1)
        var_2 = NA()
        ai133_2 = Dashboard_M10_RPS.AI133()
        var_3 = IF(var_1, var_2, ai133_2)
        return var_3

@register(Charts_Data_M10)
class AJ5():
    # 'Charts_Data_M10'!AJ5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AJ133),NA(),'Dashboard M10 RPS'!AJ133)"
    @eval_fn
    def AJ5():
        aj133_1 = Dashboard_M10_RPS.AJ133()
        var_1 = ISERROR(aj133_1)
        var_2 = NA()
        aj133_2 = Dashboard_M10_RPS.AJ133()
        var_3 = IF(var_1, var_2, aj133_2)
        return var_3

@register(Charts_Data_M10)
class AK5():
    # 'Charts_Data_M10'!AK5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AK133),NA(),'Dashboard M10 RPS'!AK133)"
    @eval_fn
    def AK5():
        ak133_1 = Dashboard_M10_RPS.AK133()
        var_1 = ISERROR(ak133_1)
        var_2 = NA()
        ak133_2 = Dashboard_M10_RPS.AK133()
        var_3 = IF(var_1, var_2, ak133_2)
        return var_3

@register(Charts_Data_M10)
class AL5():
    # 'Charts_Data_M10'!AL5
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AL133),NA(),'Dashboard M10 RPS'!AL133)"
    @eval_fn
    def AL5():
        al133_1 = Dashboard_M10_RPS.AL133()
        var_1 = ISERROR(al133_1)
        var_2 = NA()
        al133_2 = Dashboard_M10_RPS.AL133()
        var_3 = IF(var_1, var_2, al133_2)
        return var_3

@register(Charts_Data_M10)
class D6():
    # 'Charts_Data_M10'!D6
    value = "HELCO"

@register(Charts_Data_M10)
class F6():
    # 'Charts_Data_M10'!F6
    value = "Notes"

@register(Charts_Data_M10)
class G6():
    # 'Charts_Data_M10'!G6
    value = 0.704989154013
    formula = "=IF(ISERROR('Dashboard M10 RPS'!G134),NA(),'Dashboard M10 RPS'!G134)"
    @eval_fn
    def G6():
        g134_1 = Dashboard_M10_RPS.G134()
        var_1 = ISERROR(g134_1)
        var_2 = NA()
        g134_2 = Dashboard_M10_RPS.G134()
        var_3 = IF(var_1, var_2, g134_2)
        return var_3

@register(Charts_Data_M10)
class H6():
    # 'Charts_Data_M10'!H6
    value = 0.81498951782
    formula = "=IF(ISERROR('Dashboard M10 RPS'!H134),NA(),'Dashboard M10 RPS'!H134)"
    @eval_fn
    def H6():
        h134_1 = Dashboard_M10_RPS.H134()
        var_1 = ISERROR(h134_1)
        var_2 = NA()
        h134_2 = Dashboard_M10_RPS.H134()
        var_3 = IF(var_1, var_2, h134_2)
        return var_3

@register(Charts_Data_M10)
class I6():
    # 'Charts_Data_M10'!I6
    value = 0.714285714286
    formula = "=IF(ISERROR('Dashboard M10 RPS'!I134),NA(),'Dashboard M10 RPS'!I134)"
    @eval_fn
    def I6():
        i134_1 = Dashboard_M10_RPS.I134()
        var_1 = ISERROR(i134_1)
        var_2 = NA()
        i134_2 = Dashboard_M10_RPS.I134()
        var_3 = IF(var_1, var_2, i134_2)
        return var_3

@register(Charts_Data_M10)
class J6():
    # 'Charts_Data_M10'!J6
    value = 0.309045226131
    formula = "=IF(ISERROR('Dashboard M10 RPS'!J134),NA(),'Dashboard M10 RPS'!J134)"
    @eval_fn
    def J6():
        j134_1 = Dashboard_M10_RPS.J134()
        var_1 = ISERROR(j134_1)
        var_2 = NA()
        j134_2 = Dashboard_M10_RPS.J134()
        var_3 = IF(var_1, var_2, j134_2)
        return var_3

@register(Charts_Data_M10)
class K6():
    # 'Charts_Data_M10'!K6
    value = 0.517208413002
    formula = "=IF(ISERROR('Dashboard M10 RPS'!K134),NA(),'Dashboard M10 RPS'!K134)"
    @eval_fn
    def K6():
        k134_1 = Dashboard_M10_RPS.K134()
        var_1 = ISERROR(k134_1)
        var_2 = NA()
        k134_2 = Dashboard_M10_RPS.K134()
        var_3 = IF(var_1, var_2, k134_2)
        return var_3

@register(Charts_Data_M10)
class L6():
    # 'Charts_Data_M10'!L6
    value = 0.592105263158
    formula = "=IF(ISERROR('Dashboard M10 RPS'!L134),NA(),'Dashboard M10 RPS'!L134)"
    @eval_fn
    def L6():
        l134_1 = Dashboard_M10_RPS.L134()
        var_1 = ISERROR(l134_1)
        var_2 = NA()
        l134_2 = Dashboard_M10_RPS.L134()
        var_3 = IF(var_1, var_2, l134_2)
        return var_3

@register(Charts_Data_M10)
class M6():
    # 'Charts_Data_M10'!M6
    value = 0.603401969561
    formula = "=IF(ISERROR('Dashboard M10 RPS'!M134),NA(),'Dashboard M10 RPS'!M134)"
    @eval_fn
    def M6():
        m134_1 = Dashboard_M10_RPS.M134()
        var_1 = ISERROR(m134_1)
        var_2 = NA()
        m134_2 = Dashboard_M10_RPS.M134()
        var_3 = IF(var_1, var_2, m134_2)
        return var_3

@register(Charts_Data_M10)
class N6():
    # 'Charts_Data_M10'!N6
    value = 0.642297650131
    formula = "=IF(ISERROR('Dashboard M10 RPS'!N134),NA(),'Dashboard M10 RPS'!N134)"
    @eval_fn
    def N6():
        n134_1 = Dashboard_M10_RPS.N134()
        var_1 = ISERROR(n134_1)
        var_2 = NA()
        n134_2 = Dashboard_M10_RPS.N134()
        var_3 = IF(var_1, var_2, n134_2)
        return var_3

@register(Charts_Data_M10)
class O6():
    # 'Charts_Data_M10'!O6
    value = 0.845012897678
    formula = "=IF(ISERROR('Dashboard M10 RPS'!O134),NA(),'Dashboard M10 RPS'!O134)"
    @eval_fn
    def O6():
        o134_1 = Dashboard_M10_RPS.O134()
        var_1 = ISERROR(o134_1)
        var_2 = NA()
        o134_2 = Dashboard_M10_RPS.O134()
        var_3 = IF(var_1, var_2, o134_2)
        return var_3

@register(Charts_Data_M10)
class P6():
    # 'Charts_Data_M10'!P6
    value = 0.884038982323
    formula = "=IF(ISERROR('Dashboard M10 RPS'!P134),NA(),'Dashboard M10 RPS'!P134)"
    @eval_fn
    def P6():
        p134_1 = Dashboard_M10_RPS.P134()
        var_1 = ISERROR(p134_1)
        var_2 = NA()
        p134_2 = Dashboard_M10_RPS.P134()
        var_3 = IF(var_1, var_2, p134_2)
        return var_3

@register(Charts_Data_M10)
class Q6():
    # 'Charts_Data_M10'!Q6
    value = 0.843236915351
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Q134),NA(),'Dashboard M10 RPS'!Q134)"
    @eval_fn
    def Q6():
        q134_1 = Dashboard_M10_RPS.Q134()
        var_1 = ISERROR(q134_1)
        var_2 = NA()
        q134_2 = Dashboard_M10_RPS.Q134()
        var_3 = IF(var_1, var_2, q134_2)
        return var_3

@register(Charts_Data_M10)
class R6():
    # 'Charts_Data_M10'!R6
    value = 0.864182457291
    formula = "=IF(ISERROR('Dashboard M10 RPS'!R134),NA(),'Dashboard M10 RPS'!R134)"
    @eval_fn
    def R6():
        r134_1 = Dashboard_M10_RPS.R134()
        var_1 = ISERROR(r134_1)
        var_2 = NA()
        r134_2 = Dashboard_M10_RPS.R134()
        var_3 = IF(var_1, var_2, r134_2)
        return var_3

@register(Charts_Data_M10)
class S6():
    # 'Charts_Data_M10'!S6
    value = 1.02700367534
    formula = "=IF(ISERROR('Dashboard M10 RPS'!S134),NA(),'Dashboard M10 RPS'!S134)"
    @eval_fn
    def S6():
        s134_1 = Dashboard_M10_RPS.S134()
        var_1 = ISERROR(s134_1)
        var_2 = NA()
        s134_2 = Dashboard_M10_RPS.S134()
        var_3 = IF(var_1, var_2, s134_2)
        return var_3

@register(Charts_Data_M10)
class T6():
    # 'Charts_Data_M10'!T6
    value = 1.16816151556
    formula = "=IF(ISERROR('Dashboard M10 RPS'!T134),NA(),'Dashboard M10 RPS'!T134)"
    @eval_fn
    def T6():
        t134_1 = Dashboard_M10_RPS.T134()
        var_1 = ISERROR(t134_1)
        var_2 = NA()
        t134_2 = Dashboard_M10_RPS.T134()
        var_3 = IF(var_1, var_2, t134_2)
        return var_3

@register(Charts_Data_M10)
class U6():
    # 'Charts_Data_M10'!U6
    value = 1.20196328608
    formula = "=IF(ISERROR('Dashboard M10 RPS'!U134),NA(),'Dashboard M10 RPS'!U134)"
    @eval_fn
    def U6():
        u134_1 = Dashboard_M10_RPS.U134()
        var_1 = ISERROR(u134_1)
        var_2 = NA()
        u134_2 = Dashboard_M10_RPS.U134()
        var_3 = IF(var_1, var_2, u134_2)
        return var_3

@register(Charts_Data_M10)
class V6():
    # 'Charts_Data_M10'!V6
    value = 1.18383542537
    formula = "=IF(ISERROR('Dashboard M10 RPS'!V134),NA(),'Dashboard M10 RPS'!V134)"
    @eval_fn
    def V6():
        v134_1 = Dashboard_M10_RPS.V134()
        var_1 = ISERROR(v134_1)
        var_2 = NA()
        v134_2 = Dashboard_M10_RPS.V134()
        var_3 = IF(var_1, var_2, v134_2)
        return var_3

@register(Charts_Data_M10)
class W6():
    # 'Charts_Data_M10'!W6
    value = 1.21693816123
    formula = "=IF(ISERROR('Dashboard M10 RPS'!W134),NA(),'Dashboard M10 RPS'!W134)"
    @eval_fn
    def W6():
        w134_1 = Dashboard_M10_RPS.W134()
        var_1 = ISERROR(w134_1)
        var_2 = NA()
        w134_2 = Dashboard_M10_RPS.W134()
        var_3 = IF(var_1, var_2, w134_2)
        return var_3

@register(Charts_Data_M10)
class X6():
    # 'Charts_Data_M10'!X6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!X134),NA(),'Dashboard M10 RPS'!X134)"
    @eval_fn
    def X6():
        x134_1 = Dashboard_M10_RPS.X134()
        var_1 = ISERROR(x134_1)
        var_2 = NA()
        x134_2 = Dashboard_M10_RPS.X134()
        var_3 = IF(var_1, var_2, x134_2)
        return var_3

@register(Charts_Data_M10)
class Y6():
    # 'Charts_Data_M10'!Y6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Y134),NA(),'Dashboard M10 RPS'!Y134)"
    @eval_fn
    def Y6():
        y134_1 = Dashboard_M10_RPS.Y134()
        var_1 = ISERROR(y134_1)
        var_2 = NA()
        y134_2 = Dashboard_M10_RPS.Y134()
        var_3 = IF(var_1, var_2, y134_2)
        return var_3

@register(Charts_Data_M10)
class Z6():
    # 'Charts_Data_M10'!Z6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Z134),NA(),'Dashboard M10 RPS'!Z134)"
    @eval_fn
    def Z6():
        z134_1 = Dashboard_M10_RPS.Z134()
        var_1 = ISERROR(z134_1)
        var_2 = NA()
        z134_2 = Dashboard_M10_RPS.Z134()
        var_3 = IF(var_1, var_2, z134_2)
        return var_3

@register(Charts_Data_M10)
class AA6():
    # 'Charts_Data_M10'!AA6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AA134),NA(),'Dashboard M10 RPS'!AA134)"
    @eval_fn
    def AA6():
        aa134_1 = Dashboard_M10_RPS.AA134()
        var_1 = ISERROR(aa134_1)
        var_2 = NA()
        aa134_2 = Dashboard_M10_RPS.AA134()
        var_3 = IF(var_1, var_2, aa134_2)
        return var_3

@register(Charts_Data_M10)
class AB6():
    # 'Charts_Data_M10'!AB6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AB134),NA(),'Dashboard M10 RPS'!AB134)"
    @eval_fn
    def AB6():
        ab134_1 = Dashboard_M10_RPS.AB134()
        var_1 = ISERROR(ab134_1)
        var_2 = NA()
        ab134_2 = Dashboard_M10_RPS.AB134()
        var_3 = IF(var_1, var_2, ab134_2)
        return var_3

@register(Charts_Data_M10)
class AC6():
    # 'Charts_Data_M10'!AC6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AC134),NA(),'Dashboard M10 RPS'!AC134)"
    @eval_fn
    def AC6():
        ac134_1 = Dashboard_M10_RPS.AC134()
        var_1 = ISERROR(ac134_1)
        var_2 = NA()
        ac134_2 = Dashboard_M10_RPS.AC134()
        var_3 = IF(var_1, var_2, ac134_2)
        return var_3

@register(Charts_Data_M10)
class AD6():
    # 'Charts_Data_M10'!AD6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AD134),NA(),'Dashboard M10 RPS'!AD134)"
    @eval_fn
    def AD6():
        ad134_1 = Dashboard_M10_RPS.AD134()
        var_1 = ISERROR(ad134_1)
        var_2 = NA()
        ad134_2 = Dashboard_M10_RPS.AD134()
        var_3 = IF(var_1, var_2, ad134_2)
        return var_3

@register(Charts_Data_M10)
class AE6():
    # 'Charts_Data_M10'!AE6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AE134),NA(),'Dashboard M10 RPS'!AE134)"
    @eval_fn
    def AE6():
        ae134_1 = Dashboard_M10_RPS.AE134()
        var_1 = ISERROR(ae134_1)
        var_2 = NA()
        ae134_2 = Dashboard_M10_RPS.AE134()
        var_3 = IF(var_1, var_2, ae134_2)
        return var_3

@register(Charts_Data_M10)
class AF6():
    # 'Charts_Data_M10'!AF6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AF134),NA(),'Dashboard M10 RPS'!AF134)"
    @eval_fn
    def AF6():
        af134_1 = Dashboard_M10_RPS.AF134()
        var_1 = ISERROR(af134_1)
        var_2 = NA()
        af134_2 = Dashboard_M10_RPS.AF134()
        var_3 = IF(var_1, var_2, af134_2)
        return var_3

@register(Charts_Data_M10)
class AG6():
    # 'Charts_Data_M10'!AG6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AG134),NA(),'Dashboard M10 RPS'!AG134)"
    @eval_fn
    def AG6():
        ag134_1 = Dashboard_M10_RPS.AG134()
        var_1 = ISERROR(ag134_1)
        var_2 = NA()
        ag134_2 = Dashboard_M10_RPS.AG134()
        var_3 = IF(var_1, var_2, ag134_2)
        return var_3

@register(Charts_Data_M10)
class AH6():
    # 'Charts_Data_M10'!AH6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AH134),NA(),'Dashboard M10 RPS'!AH134)"
    @eval_fn
    def AH6():
        ah134_1 = Dashboard_M10_RPS.AH134()
        var_1 = ISERROR(ah134_1)
        var_2 = NA()
        ah134_2 = Dashboard_M10_RPS.AH134()
        var_3 = IF(var_1, var_2, ah134_2)
        return var_3

@register(Charts_Data_M10)
class AI6():
    # 'Charts_Data_M10'!AI6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AI134),NA(),'Dashboard M10 RPS'!AI134)"
    @eval_fn
    def AI6():
        ai134_1 = Dashboard_M10_RPS.AI134()
        var_1 = ISERROR(ai134_1)
        var_2 = NA()
        ai134_2 = Dashboard_M10_RPS.AI134()
        var_3 = IF(var_1, var_2, ai134_2)
        return var_3

@register(Charts_Data_M10)
class AJ6():
    # 'Charts_Data_M10'!AJ6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AJ134),NA(),'Dashboard M10 RPS'!AJ134)"
    @eval_fn
    def AJ6():
        aj134_1 = Dashboard_M10_RPS.AJ134()
        var_1 = ISERROR(aj134_1)
        var_2 = NA()
        aj134_2 = Dashboard_M10_RPS.AJ134()
        var_3 = IF(var_1, var_2, aj134_2)
        return var_3

@register(Charts_Data_M10)
class AK6():
    # 'Charts_Data_M10'!AK6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AK134),NA(),'Dashboard M10 RPS'!AK134)"
    @eval_fn
    def AK6():
        ak134_1 = Dashboard_M10_RPS.AK134()
        var_1 = ISERROR(ak134_1)
        var_2 = NA()
        ak134_2 = Dashboard_M10_RPS.AK134()
        var_3 = IF(var_1, var_2, ak134_2)
        return var_3

@register(Charts_Data_M10)
class AL6():
    # 'Charts_Data_M10'!AL6
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AL134),NA(),'Dashboard M10 RPS'!AL134)"
    @eval_fn
    def AL6():
        al134_1 = Dashboard_M10_RPS.AL134()
        var_1 = ISERROR(al134_1)
        var_2 = NA()
        al134_2 = Dashboard_M10_RPS.AL134()
        var_3 = IF(var_1, var_2, al134_2)
        return var_3

@register(Charts_Data_M10)
class D7():
    # 'Charts_Data_M10'!D7
    value = "MECO"

@register(Charts_Data_M10)
class F7():
    # 'Charts_Data_M10'!F7
    value = "Notes"

@register(Charts_Data_M10)
class G7():
    # 'Charts_Data_M10'!G7
    value = 0.129107981221
    formula = "=IF(ISERROR('Dashboard M10 RPS'!G135),NA(),'Dashboard M10 RPS'!G135)"
    @eval_fn
    def G7():
        g135_1 = Dashboard_M10_RPS.G135()
        var_1 = ISERROR(g135_1)
        var_2 = NA()
        g135_2 = Dashboard_M10_RPS.G135()
        var_3 = IF(var_1, var_2, g135_2)
        return var_3

@register(Charts_Data_M10)
class H7():
    # 'Charts_Data_M10'!H7
    value = 0.101717902351
    formula = "=IF(ISERROR('Dashboard M10 RPS'!H135),NA(),'Dashboard M10 RPS'!H135)"
    @eval_fn
    def H7():
        h135_1 = Dashboard_M10_RPS.H135()
        var_1 = ISERROR(h135_1)
        var_2 = NA()
        h135_2 = Dashboard_M10_RPS.H135()
        var_3 = IF(var_1, var_2, h135_2)
        return var_3

@register(Charts_Data_M10)
class I7():
    # 'Charts_Data_M10'!I7
    value = 0.0837742504409
    formula = "=IF(ISERROR('Dashboard M10 RPS'!I135),NA(),'Dashboard M10 RPS'!I135)"
    @eval_fn
    def I7():
        i135_1 = Dashboard_M10_RPS.I135()
        var_1 = ISERROR(i135_1)
        var_2 = NA()
        i135_2 = Dashboard_M10_RPS.I135()
        var_3 = IF(var_1, var_2, i135_2)
        return var_3

@register(Charts_Data_M10)
class J7():
    # 'Charts_Data_M10'!J7
    value = 0.148835202761
    formula = "=IF(ISERROR('Dashboard M10 RPS'!J135),NA(),'Dashboard M10 RPS'!J135)"
    @eval_fn
    def J7():
        j135_1 = Dashboard_M10_RPS.J135()
        var_1 = ISERROR(j135_1)
        var_2 = NA()
        j135_2 = Dashboard_M10_RPS.J135()
        var_3 = IF(var_1, var_2, j135_2)
        return var_3

@register(Charts_Data_M10)
class K7():
    # 'Charts_Data_M10'!K7
    value = 0.136702568351
    formula = "=IF(ISERROR('Dashboard M10 RPS'!K135),NA(),'Dashboard M10 RPS'!K135)"
    @eval_fn
    def K7():
        k135_1 = Dashboard_M10_RPS.K135()
        var_1 = ISERROR(k135_1)
        var_2 = NA()
        k135_2 = Dashboard_M10_RPS.K135()
        var_3 = IF(var_1, var_2, k135_2)
        return var_3

@register(Charts_Data_M10)
class L7():
    # 'Charts_Data_M10'!L7
    value = 0.14875701684
    formula = "=IF(ISERROR('Dashboard M10 RPS'!L135),NA(),'Dashboard M10 RPS'!L135)"
    @eval_fn
    def L7():
        l135_1 = Dashboard_M10_RPS.L135()
        var_1 = ISERROR(l135_1)
        var_2 = NA()
        l135_2 = Dashboard_M10_RPS.L135()
        var_3 = IF(var_1, var_2, l135_2)
        return var_3

@register(Charts_Data_M10)
class M7():
    # 'Charts_Data_M10'!M7
    value = 0.150559105431
    formula = "=IF(ISERROR('Dashboard M10 RPS'!M135),NA(),'Dashboard M10 RPS'!M135)"
    @eval_fn
    def M7():
        m135_1 = Dashboard_M10_RPS.M135()
        var_1 = ISERROR(m135_1)
        var_2 = NA()
        m135_2 = Dashboard_M10_RPS.M135()
        var_3 = IF(var_1, var_2, m135_2)
        return var_3

@register(Charts_Data_M10)
class N7():
    # 'Charts_Data_M10'!N7
    value = 0.270339652449
    formula = "=IF(ISERROR('Dashboard M10 RPS'!N135),NA(),'Dashboard M10 RPS'!N135)"
    @eval_fn
    def N7():
        n135_1 = Dashboard_M10_RPS.N135()
        var_1 = ISERROR(n135_1)
        var_2 = NA()
        n135_2 = Dashboard_M10_RPS.N135()
        var_3 = IF(var_1, var_2, n135_2)
        return var_3

@register(Charts_Data_M10)
class O7():
    # 'Charts_Data_M10'!O7
    value = 0.3861328125
    formula = "=IF(ISERROR('Dashboard M10 RPS'!O135),NA(),'Dashboard M10 RPS'!O135)"
    @eval_fn
    def O7():
        o135_1 = Dashboard_M10_RPS.O135()
        var_1 = ISERROR(o135_1)
        var_2 = NA()
        o135_2 = Dashboard_M10_RPS.O135()
        var_3 = IF(var_1, var_2, o135_2)
        return var_3

@register(Charts_Data_M10)
class P7():
    # 'Charts_Data_M10'!P7
    value = 0.346846988609
    formula = "=IF(ISERROR('Dashboard M10 RPS'!P135),NA(),'Dashboard M10 RPS'!P135)"
    @eval_fn
    def P7():
        p135_1 = Dashboard_M10_RPS.P135()
        var_1 = ISERROR(p135_1)
        var_2 = NA()
        p135_2 = Dashboard_M10_RPS.P135()
        var_3 = IF(var_1, var_2, p135_2)
        return var_3

@register(Charts_Data_M10)
class Q7():
    # 'Charts_Data_M10'!Q7
    value = 0.347737415946
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Q135),NA(),'Dashboard M10 RPS'!Q135)"
    @eval_fn
    def Q7():
        q135_1 = Dashboard_M10_RPS.Q135()
        var_1 = ISERROR(q135_1)
        var_2 = NA()
        q135_2 = Dashboard_M10_RPS.Q135()
        var_3 = IF(var_1, var_2, q135_2)
        return var_3

@register(Charts_Data_M10)
class R7():
    # 'Charts_Data_M10'!R7
    value = 0.383027613404
    formula = "=IF(ISERROR('Dashboard M10 RPS'!R135),NA(),'Dashboard M10 RPS'!R135)"
    @eval_fn
    def R7():
        r135_1 = Dashboard_M10_RPS.R135()
        var_1 = ISERROR(r135_1)
        var_2 = NA()
        r135_2 = Dashboard_M10_RPS.R135()
        var_3 = IF(var_1, var_2, r135_2)
        return var_3

@register(Charts_Data_M10)
class S7():
    # 'Charts_Data_M10'!S7
    value = 0.428165849016
    formula = "=IF(ISERROR('Dashboard M10 RPS'!S135),NA(),'Dashboard M10 RPS'!S135)"
    @eval_fn
    def S7():
        s135_1 = Dashboard_M10_RPS.S135()
        var_1 = ISERROR(s135_1)
        var_2 = NA()
        s135_2 = Dashboard_M10_RPS.S135()
        var_3 = IF(var_1, var_2, s135_2)
        return var_3

@register(Charts_Data_M10)
class T7():
    # 'Charts_Data_M10'!T7
    value = 0.520423520656
    formula = "=IF(ISERROR('Dashboard M10 RPS'!T135),NA(),'Dashboard M10 RPS'!T135)"
    @eval_fn
    def T7():
        t135_1 = Dashboard_M10_RPS.T135()
        var_1 = ISERROR(t135_1)
        var_2 = NA()
        t135_2 = Dashboard_M10_RPS.T135()
        var_3 = IF(var_1, var_2, t135_2)
        return var_3

@register(Charts_Data_M10)
class U7():
    # 'Charts_Data_M10'!U7
    value = 0.727101182247
    formula = "=IF(ISERROR('Dashboard M10 RPS'!U135),NA(),'Dashboard M10 RPS'!U135)"
    @eval_fn
    def U7():
        u135_1 = Dashboard_M10_RPS.U135()
        var_1 = ISERROR(u135_1)
        var_2 = NA()
        u135_2 = Dashboard_M10_RPS.U135()
        var_3 = IF(var_1, var_2, u135_2)
        return var_3

@register(Charts_Data_M10)
class V7():
    # 'Charts_Data_M10'!V7
    value = 0.842164610231
    formula = "=IF(ISERROR('Dashboard M10 RPS'!V135),NA(),'Dashboard M10 RPS'!V135)"
    @eval_fn
    def V7():
        v135_1 = Dashboard_M10_RPS.V135()
        var_1 = ISERROR(v135_1)
        var_2 = NA()
        v135_2 = Dashboard_M10_RPS.V135()
        var_3 = IF(var_1, var_2, v135_2)
        return var_3

@register(Charts_Data_M10)
class W7():
    # 'Charts_Data_M10'!W7
    value = 0.885243884215
    formula = "=IF(ISERROR('Dashboard M10 RPS'!W135),NA(),'Dashboard M10 RPS'!W135)"
    @eval_fn
    def W7():
        w135_1 = Dashboard_M10_RPS.W135()
        var_1 = ISERROR(w135_1)
        var_2 = NA()
        w135_2 = Dashboard_M10_RPS.W135()
        var_3 = IF(var_1, var_2, w135_2)
        return var_3

@register(Charts_Data_M10)
class X7():
    # 'Charts_Data_M10'!X7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!X135),NA(),'Dashboard M10 RPS'!X135)"
    @eval_fn
    def X7():
        x135_1 = Dashboard_M10_RPS.X135()
        var_1 = ISERROR(x135_1)
        var_2 = NA()
        x135_2 = Dashboard_M10_RPS.X135()
        var_3 = IF(var_1, var_2, x135_2)
        return var_3

@register(Charts_Data_M10)
class Y7():
    # 'Charts_Data_M10'!Y7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Y135),NA(),'Dashboard M10 RPS'!Y135)"
    @eval_fn
    def Y7():
        y135_1 = Dashboard_M10_RPS.Y135()
        var_1 = ISERROR(y135_1)
        var_2 = NA()
        y135_2 = Dashboard_M10_RPS.Y135()
        var_3 = IF(var_1, var_2, y135_2)
        return var_3

@register(Charts_Data_M10)
class Z7():
    # 'Charts_Data_M10'!Z7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Z135),NA(),'Dashboard M10 RPS'!Z135)"
    @eval_fn
    def Z7():
        z135_1 = Dashboard_M10_RPS.Z135()
        var_1 = ISERROR(z135_1)
        var_2 = NA()
        z135_2 = Dashboard_M10_RPS.Z135()
        var_3 = IF(var_1, var_2, z135_2)
        return var_3

@register(Charts_Data_M10)
class AA7():
    # 'Charts_Data_M10'!AA7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AA135),NA(),'Dashboard M10 RPS'!AA135)"
    @eval_fn
    def AA7():
        aa135_1 = Dashboard_M10_RPS.AA135()
        var_1 = ISERROR(aa135_1)
        var_2 = NA()
        aa135_2 = Dashboard_M10_RPS.AA135()
        var_3 = IF(var_1, var_2, aa135_2)
        return var_3

@register(Charts_Data_M10)
class AB7():
    # 'Charts_Data_M10'!AB7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AB135),NA(),'Dashboard M10 RPS'!AB135)"
    @eval_fn
    def AB7():
        ab135_1 = Dashboard_M10_RPS.AB135()
        var_1 = ISERROR(ab135_1)
        var_2 = NA()
        ab135_2 = Dashboard_M10_RPS.AB135()
        var_3 = IF(var_1, var_2, ab135_2)
        return var_3

@register(Charts_Data_M10)
class AC7():
    # 'Charts_Data_M10'!AC7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AC135),NA(),'Dashboard M10 RPS'!AC135)"
    @eval_fn
    def AC7():
        ac135_1 = Dashboard_M10_RPS.AC135()
        var_1 = ISERROR(ac135_1)
        var_2 = NA()
        ac135_2 = Dashboard_M10_RPS.AC135()
        var_3 = IF(var_1, var_2, ac135_2)
        return var_3

@register(Charts_Data_M10)
class AD7():
    # 'Charts_Data_M10'!AD7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AD135),NA(),'Dashboard M10 RPS'!AD135)"
    @eval_fn
    def AD7():
        ad135_1 = Dashboard_M10_RPS.AD135()
        var_1 = ISERROR(ad135_1)
        var_2 = NA()
        ad135_2 = Dashboard_M10_RPS.AD135()
        var_3 = IF(var_1, var_2, ad135_2)
        return var_3

@register(Charts_Data_M10)
class AE7():
    # 'Charts_Data_M10'!AE7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AE135),NA(),'Dashboard M10 RPS'!AE135)"
    @eval_fn
    def AE7():
        ae135_1 = Dashboard_M10_RPS.AE135()
        var_1 = ISERROR(ae135_1)
        var_2 = NA()
        ae135_2 = Dashboard_M10_RPS.AE135()
        var_3 = IF(var_1, var_2, ae135_2)
        return var_3

@register(Charts_Data_M10)
class AF7():
    # 'Charts_Data_M10'!AF7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AF135),NA(),'Dashboard M10 RPS'!AF135)"
    @eval_fn
    def AF7():
        af135_1 = Dashboard_M10_RPS.AF135()
        var_1 = ISERROR(af135_1)
        var_2 = NA()
        af135_2 = Dashboard_M10_RPS.AF135()
        var_3 = IF(var_1, var_2, af135_2)
        return var_3

@register(Charts_Data_M10)
class AG7():
    # 'Charts_Data_M10'!AG7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AG135),NA(),'Dashboard M10 RPS'!AG135)"
    @eval_fn
    def AG7():
        ag135_1 = Dashboard_M10_RPS.AG135()
        var_1 = ISERROR(ag135_1)
        var_2 = NA()
        ag135_2 = Dashboard_M10_RPS.AG135()
        var_3 = IF(var_1, var_2, ag135_2)
        return var_3

@register(Charts_Data_M10)
class AH7():
    # 'Charts_Data_M10'!AH7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AH135),NA(),'Dashboard M10 RPS'!AH135)"
    @eval_fn
    def AH7():
        ah135_1 = Dashboard_M10_RPS.AH135()
        var_1 = ISERROR(ah135_1)
        var_2 = NA()
        ah135_2 = Dashboard_M10_RPS.AH135()
        var_3 = IF(var_1, var_2, ah135_2)
        return var_3

@register(Charts_Data_M10)
class AI7():
    # 'Charts_Data_M10'!AI7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AI135),NA(),'Dashboard M10 RPS'!AI135)"
    @eval_fn
    def AI7():
        ai135_1 = Dashboard_M10_RPS.AI135()
        var_1 = ISERROR(ai135_1)
        var_2 = NA()
        ai135_2 = Dashboard_M10_RPS.AI135()
        var_3 = IF(var_1, var_2, ai135_2)
        return var_3

@register(Charts_Data_M10)
class AJ7():
    # 'Charts_Data_M10'!AJ7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AJ135),NA(),'Dashboard M10 RPS'!AJ135)"
    @eval_fn
    def AJ7():
        aj135_1 = Dashboard_M10_RPS.AJ135()
        var_1 = ISERROR(aj135_1)
        var_2 = NA()
        aj135_2 = Dashboard_M10_RPS.AJ135()
        var_3 = IF(var_1, var_2, aj135_2)
        return var_3

@register(Charts_Data_M10)
class AK7():
    # 'Charts_Data_M10'!AK7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AK135),NA(),'Dashboard M10 RPS'!AK135)"
    @eval_fn
    def AK7():
        ak135_1 = Dashboard_M10_RPS.AK135()
        var_1 = ISERROR(ak135_1)
        var_2 = NA()
        ak135_2 = Dashboard_M10_RPS.AK135()
        var_3 = IF(var_1, var_2, ak135_2)
        return var_3

@register(Charts_Data_M10)
class AL7():
    # 'Charts_Data_M10'!AL7
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AL135),NA(),'Dashboard M10 RPS'!AL135)"
    @eval_fn
    def AL7():
        al135_1 = Dashboard_M10_RPS.AL135()
        var_1 = ISERROR(al135_1)
        var_2 = NA()
        al135_2 = Dashboard_M10_RPS.AL135()
        var_3 = IF(var_1, var_2, al135_2)
        return var_3

@register(Charts_Data_M10)
class D8():
    # 'Charts_Data_M10'!D8
    value = "KIUC"

@register(Charts_Data_M10)
class F8():
    # 'Charts_Data_M10'!F8
    value = "Notes"

@register(Charts_Data_M10)
class G8():
    # 'Charts_Data_M10'!G8
    value = 0
    formula = "=IF(ISERROR('Dashboard M10 RPS'!G137),NA(),'Dashboard M10 RPS'!G137)"
    @eval_fn
    def G8():
        g137_1 = Dashboard_M10_RPS.G137()
        var_1 = ISERROR(g137_1)
        var_2 = NA()
        g137_2 = Dashboard_M10_RPS.G137()
        var_3 = IF(var_1, var_2, g137_2)
        return var_3

@register(Charts_Data_M10)
class H8():
    # 'Charts_Data_M10'!H8
    value = 0
    formula = "=IF(ISERROR('Dashboard M10 RPS'!H137),NA(),'Dashboard M10 RPS'!H137)"
    @eval_fn
    def H8():
        h137_1 = Dashboard_M10_RPS.H137()
        var_1 = ISERROR(h137_1)
        var_2 = NA()
        h137_2 = Dashboard_M10_RPS.H137()
        var_3 = IF(var_1, var_2, h137_2)
        return var_3

@register(Charts_Data_M10)
class I8():
    # 'Charts_Data_M10'!I8
    value = 0
    formula = "=IF(ISERROR('Dashboard M10 RPS'!I137),NA(),'Dashboard M10 RPS'!I137)"
    @eval_fn
    def I8():
        i137_1 = Dashboard_M10_RPS.I137()
        var_1 = ISERROR(i137_1)
        var_2 = NA()
        i137_2 = Dashboard_M10_RPS.I137()
        var_3 = IF(var_1, var_2, i137_2)
        return var_3

@register(Charts_Data_M10)
class J8():
    # 'Charts_Data_M10'!J8
    value = 0
    formula = "=IF(ISERROR('Dashboard M10 RPS'!J137),NA(),'Dashboard M10 RPS'!J137)"
    @eval_fn
    def J8():
        j137_1 = Dashboard_M10_RPS.J137()
        var_1 = ISERROR(j137_1)
        var_2 = NA()
        j137_2 = Dashboard_M10_RPS.J137()
        var_3 = IF(var_1, var_2, j137_2)
        return var_3

@register(Charts_Data_M10)
class K8():
    # 'Charts_Data_M10'!K8
    value = 0.145612259782
    formula = "=IF(ISERROR('Dashboard M10 RPS'!K137),NA(),'Dashboard M10 RPS'!K137)"
    @eval_fn
    def K8():
        k137_1 = Dashboard_M10_RPS.K137()
        var_1 = ISERROR(k137_1)
        var_2 = NA()
        k137_2 = Dashboard_M10_RPS.K137()
        var_3 = IF(var_1, var_2, k137_2)
        return var_3

@register(Charts_Data_M10)
class L8():
    # 'Charts_Data_M10'!L8
    value = 0.199732690326
    formula = "=IF(ISERROR('Dashboard M10 RPS'!L137),NA(),'Dashboard M10 RPS'!L137)"
    @eval_fn
    def L8():
        l137_1 = Dashboard_M10_RPS.L137()
        var_1 = ISERROR(l137_1)
        var_2 = NA()
        l137_2 = Dashboard_M10_RPS.L137()
        var_3 = IF(var_1, var_2, l137_2)
        return var_3

@register(Charts_Data_M10)
class M8():
    # 'Charts_Data_M10'!M8
    value = 0.199745833311
    formula = "=IF(ISERROR('Dashboard M10 RPS'!M137),NA(),'Dashboard M10 RPS'!M137)"
    @eval_fn
    def M8():
        m137_1 = Dashboard_M10_RPS.M137()
        var_1 = ISERROR(m137_1)
        var_2 = NA()
        m137_2 = Dashboard_M10_RPS.M137()
        var_3 = IF(var_1, var_2, m137_2)
        return var_3

@register(Charts_Data_M10)
class N8():
    # 'Charts_Data_M10'!N8
    value = 0.195941117045
    formula = "=IF(ISERROR('Dashboard M10 RPS'!N137),NA(),'Dashboard M10 RPS'!N137)"
    @eval_fn
    def N8():
        n137_1 = Dashboard_M10_RPS.N137()
        var_1 = ISERROR(n137_1)
        var_2 = NA()
        n137_2 = Dashboard_M10_RPS.N137()
        var_3 = IF(var_1, var_2, n137_2)
        return var_3

@register(Charts_Data_M10)
class O8():
    # 'Charts_Data_M10'!O8
    value = 0.137948410347
    formula = "=IF(ISERROR('Dashboard M10 RPS'!O137),NA(),'Dashboard M10 RPS'!O137)"
    @eval_fn
    def O8():
        o137_1 = Dashboard_M10_RPS.O137()
        var_1 = ISERROR(o137_1)
        var_2 = NA()
        o137_2 = Dashboard_M10_RPS.O137()
        var_3 = IF(var_1, var_2, o137_2)
        return var_3

@register(Charts_Data_M10)
class P8():
    # 'Charts_Data_M10'!P8
    value = 0.205314919027
    formula = "=IF(ISERROR('Dashboard M10 RPS'!P137),NA(),'Dashboard M10 RPS'!P137)"
    @eval_fn
    def P8():
        p137_1 = Dashboard_M10_RPS.P137()
        var_1 = ISERROR(p137_1)
        var_2 = NA()
        p137_2 = Dashboard_M10_RPS.P137()
        var_3 = IF(var_1, var_2, p137_2)
        return var_3

@register(Charts_Data_M10)
class Q8():
    # 'Charts_Data_M10'!Q8
    value = 0.227758304326
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Q137),NA(),'Dashboard M10 RPS'!Q137)"
    @eval_fn
    def Q8():
        q137_1 = Dashboard_M10_RPS.Q137()
        var_1 = ISERROR(q137_1)
        var_2 = NA()
        q137_2 = Dashboard_M10_RPS.Q137()
        var_3 = IF(var_1, var_2, q137_2)
        return var_3

@register(Charts_Data_M10)
class R8():
    # 'Charts_Data_M10'!R8
    value = 0.221020509585
    formula = "=IF(ISERROR('Dashboard M10 RPS'!R137),NA(),'Dashboard M10 RPS'!R137)"
    @eval_fn
    def R8():
        r137_1 = Dashboard_M10_RPS.R137()
        var_1 = ISERROR(r137_1)
        var_2 = NA()
        r137_2 = Dashboard_M10_RPS.R137()
        var_3 = IF(var_1, var_2, r137_2)
        return var_3

@register(Charts_Data_M10)
class S8():
    # 'Charts_Data_M10'!S8
    value = 0.264811181181
    formula = "=IF(ISERROR('Dashboard M10 RPS'!S137),NA(),'Dashboard M10 RPS'!S137)"
    @eval_fn
    def S8():
        s137_1 = Dashboard_M10_RPS.S137()
        var_1 = ISERROR(s137_1)
        var_2 = NA()
        s137_2 = Dashboard_M10_RPS.S137()
        var_3 = IF(var_1, var_2, s137_2)
        return var_3

@register(Charts_Data_M10)
class T8():
    # 'Charts_Data_M10'!T8
    value = 0.31203186936
    formula = "=IF(ISERROR('Dashboard M10 RPS'!T137),NA(),'Dashboard M10 RPS'!T137)"
    @eval_fn
    def T8():
        t137_1 = Dashboard_M10_RPS.T137()
        var_1 = ISERROR(t137_1)
        var_2 = NA()
        t137_2 = Dashboard_M10_RPS.T137()
        var_3 = IF(var_1, var_2, t137_2)
        return var_3

@register(Charts_Data_M10)
class U8():
    # 'Charts_Data_M10'!U8
    value = 0.40625204676
    formula = "=IF(ISERROR('Dashboard M10 RPS'!U137),NA(),'Dashboard M10 RPS'!U137)"
    @eval_fn
    def U8():
        u137_1 = Dashboard_M10_RPS.U137()
        var_1 = ISERROR(u137_1)
        var_2 = NA()
        u137_2 = Dashboard_M10_RPS.U137()
        var_3 = IF(var_1, var_2, u137_2)
        return var_3

@register(Charts_Data_M10)
class V8():
    # 'Charts_Data_M10'!V8
    value = 0.526871863584
    formula = "=IF(ISERROR('Dashboard M10 RPS'!V137),NA(),'Dashboard M10 RPS'!V137)"
    @eval_fn
    def V8():
        v137_1 = Dashboard_M10_RPS.V137()
        var_1 = ISERROR(v137_1)
        var_2 = NA()
        v137_2 = Dashboard_M10_RPS.V137()
        var_3 = IF(var_1, var_2, v137_2)
        return var_3

@register(Charts_Data_M10)
class W8():
    # 'Charts_Data_M10'!W8
    value = 0.682828100482
    formula = "=IF(ISERROR('Dashboard M10 RPS'!W137),NA(),'Dashboard M10 RPS'!W137)"
    @eval_fn
    def W8():
        w137_1 = Dashboard_M10_RPS.W137()
        var_1 = ISERROR(w137_1)
        var_2 = NA()
        w137_2 = Dashboard_M10_RPS.W137()
        var_3 = IF(var_1, var_2, w137_2)
        return var_3

@register(Charts_Data_M10)
class X8():
    # 'Charts_Data_M10'!X8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!X137),NA(),'Dashboard M10 RPS'!X137)"
    @eval_fn
    def X8():
        x137_1 = Dashboard_M10_RPS.X137()
        var_1 = ISERROR(x137_1)
        var_2 = NA()
        x137_2 = Dashboard_M10_RPS.X137()
        var_3 = IF(var_1, var_2, x137_2)
        return var_3

@register(Charts_Data_M10)
class Y8():
    # 'Charts_Data_M10'!Y8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Y137),NA(),'Dashboard M10 RPS'!Y137)"
    @eval_fn
    def Y8():
        y137_1 = Dashboard_M10_RPS.Y137()
        var_1 = ISERROR(y137_1)
        var_2 = NA()
        y137_2 = Dashboard_M10_RPS.Y137()
        var_3 = IF(var_1, var_2, y137_2)
        return var_3

@register(Charts_Data_M10)
class Z8():
    # 'Charts_Data_M10'!Z8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!Z137),NA(),'Dashboard M10 RPS'!Z137)"
    @eval_fn
    def Z8():
        z137_1 = Dashboard_M10_RPS.Z137()
        var_1 = ISERROR(z137_1)
        var_2 = NA()
        z137_2 = Dashboard_M10_RPS.Z137()
        var_3 = IF(var_1, var_2, z137_2)
        return var_3

@register(Charts_Data_M10)
class AA8():
    # 'Charts_Data_M10'!AA8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AA137),NA(),'Dashboard M10 RPS'!AA137)"
    @eval_fn
    def AA8():
        aa137_1 = Dashboard_M10_RPS.AA137()
        var_1 = ISERROR(aa137_1)
        var_2 = NA()
        aa137_2 = Dashboard_M10_RPS.AA137()
        var_3 = IF(var_1, var_2, aa137_2)
        return var_3

@register(Charts_Data_M10)
class AB8():
    # 'Charts_Data_M10'!AB8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AB137),NA(),'Dashboard M10 RPS'!AB137)"
    @eval_fn
    def AB8():
        ab137_1 = Dashboard_M10_RPS.AB137()
        var_1 = ISERROR(ab137_1)
        var_2 = NA()
        ab137_2 = Dashboard_M10_RPS.AB137()
        var_3 = IF(var_1, var_2, ab137_2)
        return var_3

@register(Charts_Data_M10)
class AC8():
    # 'Charts_Data_M10'!AC8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AC137),NA(),'Dashboard M10 RPS'!AC137)"
    @eval_fn
    def AC8():
        ac137_1 = Dashboard_M10_RPS.AC137()
        var_1 = ISERROR(ac137_1)
        var_2 = NA()
        ac137_2 = Dashboard_M10_RPS.AC137()
        var_3 = IF(var_1, var_2, ac137_2)
        return var_3

@register(Charts_Data_M10)
class AD8():
    # 'Charts_Data_M10'!AD8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AD137),NA(),'Dashboard M10 RPS'!AD137)"
    @eval_fn
    def AD8():
        ad137_1 = Dashboard_M10_RPS.AD137()
        var_1 = ISERROR(ad137_1)
        var_2 = NA()
        ad137_2 = Dashboard_M10_RPS.AD137()
        var_3 = IF(var_1, var_2, ad137_2)
        return var_3

@register(Charts_Data_M10)
class AE8():
    # 'Charts_Data_M10'!AE8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AE137),NA(),'Dashboard M10 RPS'!AE137)"
    @eval_fn
    def AE8():
        ae137_1 = Dashboard_M10_RPS.AE137()
        var_1 = ISERROR(ae137_1)
        var_2 = NA()
        ae137_2 = Dashboard_M10_RPS.AE137()
        var_3 = IF(var_1, var_2, ae137_2)
        return var_3

@register(Charts_Data_M10)
class AF8():
    # 'Charts_Data_M10'!AF8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AF137),NA(),'Dashboard M10 RPS'!AF137)"
    @eval_fn
    def AF8():
        af137_1 = Dashboard_M10_RPS.AF137()
        var_1 = ISERROR(af137_1)
        var_2 = NA()
        af137_2 = Dashboard_M10_RPS.AF137()
        var_3 = IF(var_1, var_2, af137_2)
        return var_3

@register(Charts_Data_M10)
class AG8():
    # 'Charts_Data_M10'!AG8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AG137),NA(),'Dashboard M10 RPS'!AG137)"
    @eval_fn
    def AG8():
        ag137_1 = Dashboard_M10_RPS.AG137()
        var_1 = ISERROR(ag137_1)
        var_2 = NA()
        ag137_2 = Dashboard_M10_RPS.AG137()
        var_3 = IF(var_1, var_2, ag137_2)
        return var_3

@register(Charts_Data_M10)
class AH8():
    # 'Charts_Data_M10'!AH8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AH137),NA(),'Dashboard M10 RPS'!AH137)"
    @eval_fn
    def AH8():
        ah137_1 = Dashboard_M10_RPS.AH137()
        var_1 = ISERROR(ah137_1)
        var_2 = NA()
        ah137_2 = Dashboard_M10_RPS.AH137()
        var_3 = IF(var_1, var_2, ah137_2)
        return var_3

@register(Charts_Data_M10)
class AI8():
    # 'Charts_Data_M10'!AI8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AI137),NA(),'Dashboard M10 RPS'!AI137)"
    @eval_fn
    def AI8():
        ai137_1 = Dashboard_M10_RPS.AI137()
        var_1 = ISERROR(ai137_1)
        var_2 = NA()
        ai137_2 = Dashboard_M10_RPS.AI137()
        var_3 = IF(var_1, var_2, ai137_2)
        return var_3

@register(Charts_Data_M10)
class AJ8():
    # 'Charts_Data_M10'!AJ8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AJ137),NA(),'Dashboard M10 RPS'!AJ137)"
    @eval_fn
    def AJ8():
        aj137_1 = Dashboard_M10_RPS.AJ137()
        var_1 = ISERROR(aj137_1)
        var_2 = NA()
        aj137_2 = Dashboard_M10_RPS.AJ137()
        var_3 = IF(var_1, var_2, aj137_2)
        return var_3

@register(Charts_Data_M10)
class AK8():
    # 'Charts_Data_M10'!AK8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AK137),NA(),'Dashboard M10 RPS'!AK137)"
    @eval_fn
    def AK8():
        ak137_1 = Dashboard_M10_RPS.AK137()
        var_1 = ISERROR(ak137_1)
        var_2 = NA()
        ak137_2 = Dashboard_M10_RPS.AK137()
        var_3 = IF(var_1, var_2, ak137_2)
        return var_3

@register(Charts_Data_M10)
class AL8():
    # 'Charts_Data_M10'!AL8
    value = "#N/A"
    formula = "=IF(ISERROR('Dashboard M10 RPS'!AL137),NA(),'Dashboard M10 RPS'!AL137)"
    @eval_fn
    def AL8():
        al137_1 = Dashboard_M10_RPS.AL137()
        var_1 = ISERROR(al137_1)
        var_2 = NA()
        al137_2 = Dashboard_M10_RPS.AL137()
        var_3 = IF(var_1, var_2, al137_2)
        return var_3

@register(Charts_Data_M10)
class B9():
    # 'Charts_Data_M10'!B9
    value = "year"

@register(Charts_Data_M10)
class C9():
    # 'Charts_Data_M10'!C9
    value = 2015
    formula = "=VLOOKUP('Charts M10 RPS'!C23,'Charts Interactive LookupTables'!J:M,4,FALSE)"
    @eval_fn
    def C9():
        c23_1 = Charts_M10_RPS.C23()
        range_1 = Charts_Interactive_LookupTables(10, 0, 13, 0)
        var_1 = VLOOKUP(c23_1, range_1, 4, "FALSE")
        return var_1

@register(Charts_Data_M10)
class F9():
    # 'Charts_Data_M10'!F9
    value = "Notes"

@register(Charts_Data_M10)
class G9():
    # 'Charts_Data_M10'!G9
    value = "Renewable Electricity"

@register(Charts_Data_M10)
class H9():
    # 'Charts_Data_M10'!H9
    value = "Total Electricity Sales"

@register(Charts_Data_M10)
class I9():
    # 'Charts_Data_M10'!I9
    value = "Total Conventional"

@register(Charts_Data_M10)
class B10():
    # 'Charts_Data_M10'!B10
    value = "Total Renewable"

@register(Charts_Data_M10)
class C10():
    # 'Charts_Data_M10'!C10
    value = "HECORenewable Electricity"
    formula = "='Dashboard M10 RPS'!A22"
    @eval_fn
    def C10():
        a22_1 = Dashboard_M10_RPS.A22()
        return a22_1

@register(Charts_Data_M10)
class D10():
    # 'Charts_Data_M10'!D10
    value = "HECO"

@register(Charts_Data_M10)
class F10():
    # 'Charts_Data_M10'!F10
    value = "Notes"

@register(Charts_Data_M10)
class G10():
    # 'Charts_Data_M10'!G10
    value = 1159629
    formula = "=INDEX('Dashboard M10 RPS'!$A$14:$AL$58,MATCH($C10,'Dashboard M10 RPS'!$A$14:$A$58,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def G10():
        range_1 = Dashboard_M10_RPS(1, 14, 38, 58)
        c10_1 = Charts_Data_M10.C10()
        range_2 = Dashboard_M10_RPS(1, 14, 1, 58)
        var_1 = MATCH(c10_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H10():
    # 'Charts_Data_M10'!H10
    value = 6754083
    formula = "=INDEX('Dashboard M10 RPS'!$A$7:$AL$11,MATCH(CONCATENATE(D10,$B$10),'Dashboard M10 RPS'!$A$7:$A$11,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def H10():
        range_1 = Dashboard_M10_RPS(1, 7, 38, 11)
        d10_1 = Charts_Data_M10.D10()
        b10_1 = Charts_Data_M10.B10()
        var_1 = CONCATENATE(d10_1, b10_1)
        range_2 = Dashboard_M10_RPS(1, 7, 1, 11)
        var_2 = MATCH(var_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_3 = MATCH(c9_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M10)
class I10():
    # 'Charts_Data_M10'!I10
    value = 5594454
    formula = "=H10-G10"
    @eval_fn
    def I10():
        h10_1 = Charts_Data_M10.H10()
        g10_1 = Charts_Data_M10.G10()
        var_1 = sub(h10_1, g10_1)
        return var_1

@register(Charts_Data_M10)
class J10():
    # 'Charts_Data_M10'!J10
    value = 0.171693033681
    formula = "=G10/H10"
    @eval_fn
    def J10():
        g10_1 = Charts_Data_M10.G10()
        h10_1 = Charts_Data_M10.H10()
        var_1 = divide(g10_1, h10_1)
        return var_1

@register(Charts_Data_M10)
class C11():
    # 'Charts_Data_M10'!C11
    value = "HELCORenewable Electricity"
    formula = "='Dashboard M10 RPS'!A31"
    @eval_fn
    def C11():
        a31_1 = Dashboard_M10_RPS.A31()
        return a31_1

@register(Charts_Data_M10)
class D11():
    # 'Charts_Data_M10'!D11
    value = "HELCO"

@register(Charts_Data_M10)
class F11():
    # 'Charts_Data_M10'!F11
    value = "Notes"

@register(Charts_Data_M10)
class G11():
    # 'Charts_Data_M10'!G11
    value = 518311
    formula = "=INDEX('Dashboard M10 RPS'!$A$14:$AL$58,MATCH($C11,'Dashboard M10 RPS'!$A$14:$A$58,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def G11():
        range_1 = Dashboard_M10_RPS(1, 14, 38, 58)
        c11_1 = Charts_Data_M10.C11()
        range_2 = Dashboard_M10_RPS(1, 14, 1, 58)
        var_1 = MATCH(c11_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H11():
    # 'Charts_Data_M10'!H11
    value = 1064785
    formula = "=INDEX('Dashboard M10 RPS'!$A$7:$AL$11,MATCH(CONCATENATE(D11,$B$10),'Dashboard M10 RPS'!$A$7:$A$11,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def H11():
        range_1 = Dashboard_M10_RPS(1, 7, 38, 11)
        d11_1 = Charts_Data_M10.D11()
        b10_1 = Charts_Data_M10.B10()
        var_1 = CONCATENATE(d11_1, b10_1)
        range_2 = Dashboard_M10_RPS(1, 7, 1, 11)
        var_2 = MATCH(var_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_3 = MATCH(c9_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M10)
class I11():
    # 'Charts_Data_M10'!I11
    value = 546474
    formula = "=H11-G11"
    @eval_fn
    def I11():
        h11_1 = Charts_Data_M10.H11()
        g11_1 = Charts_Data_M10.G11()
        var_1 = sub(h11_1, g11_1)
        return var_1

@register(Charts_Data_M10)
class J11():
    # 'Charts_Data_M10'!J11
    value = 0.48677526449
    formula = "=G11/H11"
    @eval_fn
    def J11():
        g11_1 = Charts_Data_M10.G11()
        h11_1 = Charts_Data_M10.H11()
        var_1 = divide(g11_1, h11_1)
        return var_1

@register(Charts_Data_M10)
class C12():
    # 'Charts_Data_M10'!C12
    value = "MECORenewable Electricity"
    formula = "='Dashboard M10 RPS'!A40"
    @eval_fn
    def C12():
        a40_1 = Dashboard_M10_RPS.A40()
        return a40_1

@register(Charts_Data_M10)
class D12():
    # 'Charts_Data_M10'!D12
    value = "MECO"

@register(Charts_Data_M10)
class F12():
    # 'Charts_Data_M10'!F12
    value = "Notes"

@register(Charts_Data_M10)
class G12():
    # 'Charts_Data_M10'!G12
    value = 402832
    formula = "=INDEX('Dashboard M10 RPS'!$A$14:$AL$58,MATCH($C12,'Dashboard M10 RPS'!$A$14:$A$58,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def G12():
        range_1 = Dashboard_M10_RPS(1, 14, 38, 58)
        c12_1 = Charts_Data_M10.C12()
        range_2 = Dashboard_M10_RPS(1, 14, 1, 58)
        var_1 = MATCH(c12_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H12():
    # 'Charts_Data_M10'!H12
    value = 1137630
    formula = "=INDEX('Dashboard M10 RPS'!$A$7:$AL$11,MATCH(CONCATENATE(D12,$B$10),'Dashboard M10 RPS'!$A$7:$A$11,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def H12():
        range_1 = Dashboard_M10_RPS(1, 7, 38, 11)
        d12_1 = Charts_Data_M10.D12()
        b10_1 = Charts_Data_M10.B10()
        var_1 = CONCATENATE(d12_1, b10_1)
        range_2 = Dashboard_M10_RPS(1, 7, 1, 11)
        var_2 = MATCH(var_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_3 = MATCH(c9_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M10)
class I12():
    # 'Charts_Data_M10'!I12
    value = 734798
    formula = "=H12-G12"
    @eval_fn
    def I12():
        h12_1 = Charts_Data_M10.H12()
        g12_1 = Charts_Data_M10.G12()
        var_1 = sub(h12_1, g12_1)
        return var_1

@register(Charts_Data_M10)
class J12():
    # 'Charts_Data_M10'!J12
    value = 0.354097553686
    formula = "=G12/H12"
    @eval_fn
    def J12():
        g12_1 = Charts_Data_M10.G12()
        h12_1 = Charts_Data_M10.H12()
        var_1 = divide(g12_1, h12_1)
        return var_1

@register(Charts_Data_M10)
class C13():
    # 'Charts_Data_M10'!C13
    value = "KIUCRenewable Electricity"
    formula = "='Dashboard M10 RPS'!A49"
    @eval_fn
    def C13():
        a49_1 = Dashboard_M10_RPS.A49()
        return a49_1

@register(Charts_Data_M10)
class D13():
    # 'Charts_Data_M10'!D13
    value = "KIUC"

@register(Charts_Data_M10)
class F13():
    # 'Charts_Data_M10'!F13
    value = "Notes"

@register(Charts_Data_M10)
class G13():
    # 'Charts_Data_M10'!G13
    value = 118014
    formula = "=INDEX('Dashboard M10 RPS'!$A$14:$AL$58,MATCH($C13,'Dashboard M10 RPS'!$A$14:$A$58,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def G13():
        range_1 = Dashboard_M10_RPS(1, 14, 38, 58)
        c13_1 = Charts_Data_M10.C13()
        range_2 = Dashboard_M10_RPS(1, 14, 1, 58)
        var_1 = MATCH(c13_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H13():
    # 'Charts_Data_M10'!H13
    value = 432078
    formula = "=INDEX('Dashboard M10 RPS'!$A$7:$AL$11,MATCH(CONCATENATE(D13,$B$10),'Dashboard M10 RPS'!$A$7:$A$11,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def H13():
        range_1 = Dashboard_M10_RPS(1, 7, 38, 11)
        d13_1 = Charts_Data_M10.D13()
        b10_1 = Charts_Data_M10.B10()
        var_1 = CONCATENATE(d13_1, b10_1)
        range_2 = Dashboard_M10_RPS(1, 7, 1, 11)
        var_2 = MATCH(var_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_3 = MATCH(c9_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M10)
class I13():
    # 'Charts_Data_M10'!I13
    value = 314064
    formula = "=H13-G13"
    @eval_fn
    def I13():
        h13_1 = Charts_Data_M10.H13()
        g13_1 = Charts_Data_M10.G13()
        var_1 = sub(h13_1, g13_1)
        return var_1

@register(Charts_Data_M10)
class J13():
    # 'Charts_Data_M10'!J13
    value = 0.273131240193
    formula = "=G13/H13"
    @eval_fn
    def J13():
        g13_1 = Charts_Data_M10.G13()
        h13_1 = Charts_Data_M10.H13()
        var_1 = divide(g13_1, h13_1)
        return var_1

@register(Charts_Data_M10)
class C14():
    # 'Charts_Data_M10'!C14
    value = "TotalRenewable Electricity"
    formula = "='Dashboard M10 RPS'!A58"
    @eval_fn
    def C14():
        a58_1 = Dashboard_M10_RPS.A58()
        return a58_1

@register(Charts_Data_M10)
class D14():
    # 'Charts_Data_M10'!D14
    value = "Total"

@register(Charts_Data_M10)
class F14():
    # 'Charts_Data_M10'!F14
    value = "Notes"

@register(Charts_Data_M10)
class G14():
    # 'Charts_Data_M10'!G14
    value = 2198786
    formula = "=INDEX('Dashboard M10 RPS'!$A$14:$AL$58,MATCH($C14,'Dashboard M10 RPS'!$A$14:$A$58,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def G14():
        range_1 = Dashboard_M10_RPS(1, 14, 38, 58)
        c14_1 = Charts_Data_M10.C14()
        range_2 = Dashboard_M10_RPS(1, 14, 1, 58)
        var_1 = MATCH(c14_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_2 = MATCH(c9_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H14():
    # 'Charts_Data_M10'!H14
    value = 9388576
    formula = "=INDEX('Dashboard M10 RPS'!$A$7:$AL$11,MATCH(CONCATENATE(D14,$B$10),'Dashboard M10 RPS'!$A$7:$A$11,0),MATCH($C$9,'Dashboard M10 RPS'!$A$5:$AL$5,0))"
    @eval_fn
    def H14():
        range_1 = Dashboard_M10_RPS(1, 7, 38, 11)
        d14_1 = Charts_Data_M10.D14()
        b10_1 = Charts_Data_M10.B10()
        var_1 = CONCATENATE(d14_1, b10_1)
        range_2 = Dashboard_M10_RPS(1, 7, 1, 11)
        var_2 = MATCH(var_1, range_2, 0)
        c9_1 = Charts_Data_M10.C9()
        range_3 = Dashboard_M10_RPS(1, 5, 38, 5)
        var_3 = MATCH(c9_1, range_3, 0)
        var_4 = INDEX(range_1, var_2, var_3)
        return var_4

@register(Charts_Data_M10)
class I14():
    # 'Charts_Data_M10'!I14
    value = 7189790
    formula = "=H14-G14"
    @eval_fn
    def I14():
        h14_1 = Charts_Data_M10.H14()
        g14_1 = Charts_Data_M10.G14()
        var_1 = sub(h14_1, g14_1)
        return var_1

@register(Charts_Data_M10)
class J14():
    # 'Charts_Data_M10'!J14
    value = 0.234198029605
    formula = "=G14/H14"
    @eval_fn
    def J14():
        g14_1 = Charts_Data_M10.G14()
        h14_1 = Charts_Data_M10.H14()
        var_1 = divide(g14_1, h14_1)
        return var_1

@register(Charts_Data_M10)
class A15():
    # 'Charts_Data_M10'!A15
    value = "Line Graph Input Final"

@register(Charts_Data_M10)
class C15():
    # 'Charts_Data_M10'!C15
    value = "Total"
    formula = "=VLOOKUP('Charts M10 RPS'!B2,'Charts Interactive LookupTables'!J:K,2,FALSE)"
    @eval_fn
    def C15():
        b2_1 = Charts_M10_RPS.B2()
        range_1 = Charts_Interactive_LookupTables(10, 0, 11, 0)
        var_1 = VLOOKUP(b2_1, range_1, 2, "FALSE")
        return var_1

@register(Charts_Data_M10)
class D15():
    # 'Charts_Data_M10'!D15
    value = "HECO"
    formula = '''=IF(OR($C$15="Total",$C$15="HECO"),"HECO",NA())'''
    @eval_fn
    def D15():
        c15_1 = Charts_Data_M10.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M10.C15()
        var_2 = equal(c15_2, "HECO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "HECO", var_4)
        return var_5

@register(Charts_Data_M10)
class F15():
    # 'Charts_Data_M10'!F15
    value = "Notes"

@register(Charts_Data_M10)
class G15():
    # 'Charts_Data_M10'!G15
    value = 0.0908535230051
    formula = "=IF(ISERROR($D15),NA(),G5)"
    @eval_fn
    def G15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        g5_1 = Charts_Data_M10.G5()
        var_3 = IF(var_1, var_2, g5_1)
        return var_3

@register(Charts_Data_M10)
class H15():
    # 'Charts_Data_M10'!H15
    value = 0.112659456461
    formula = "=IF(ISERROR($D15),NA(),H5)"
    @eval_fn
    def H15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        h5_1 = Charts_Data_M10.H5()
        var_3 = IF(var_1, var_2, h5_1)
        return var_3

@register(Charts_Data_M10)
class I15():
    # 'Charts_Data_M10'!I15
    value = 0.104095094132
    formula = "=IF(ISERROR($D15),NA(),I5)"
    @eval_fn
    def I15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        i5_1 = Charts_Data_M10.I5()
        var_3 = IF(var_1, var_2, i5_1)
        return var_3

@register(Charts_Data_M10)
class J15():
    # 'Charts_Data_M10'!J15
    value = 0.110622462788
    formula = "=IF(ISERROR($D15),NA(),J5)"
    @eval_fn
    def J15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        j5_1 = Charts_Data_M10.J5()
        var_3 = IF(var_1, var_2, j5_1)
        return var_3

@register(Charts_Data_M10)
class K15():
    # 'Charts_Data_M10'!K15
    value = 0.122374368519
    formula = "=IF(ISERROR($D15),NA(),K5)"
    @eval_fn
    def K15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        k5_1 = Charts_Data_M10.K5()
        var_3 = IF(var_1, var_2, k5_1)
        return var_3

@register(Charts_Data_M10)
class L15():
    # 'Charts_Data_M10'!L15
    value = 0.119423251002
    formula = "=IF(ISERROR($D15),NA(),L5)"
    @eval_fn
    def L15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        l5_1 = Charts_Data_M10.L5()
        var_3 = IF(var_1, var_2, l5_1)
        return var_3

@register(Charts_Data_M10)
class M15():
    # 'Charts_Data_M10'!M15
    value = 0.10795233778
    formula = "=IF(ISERROR($D15),NA(),M5)"
    @eval_fn
    def M15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        m5_1 = Charts_Data_M10.M5()
        var_3 = IF(var_1, var_2, m5_1)
        return var_3

@register(Charts_Data_M10)
class N15():
    # 'Charts_Data_M10'!N15
    value = 0.128392416569
    formula = "=IF(ISERROR($D15),NA(),N5)"
    @eval_fn
    def N15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        n5_1 = Charts_Data_M10.N5()
        var_3 = IF(var_1, var_2, n5_1)
        return var_3

@register(Charts_Data_M10)
class O15():
    # 'Charts_Data_M10'!O15
    value = 0.10674267101
    formula = "=IF(ISERROR($D15),NA(),O5)"
    @eval_fn
    def O15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        o5_1 = Charts_Data_M10.O5()
        var_3 = IF(var_1, var_2, o5_1)
        return var_3

@register(Charts_Data_M10)
class P15():
    # 'Charts_Data_M10'!P15
    value = 0.120108465342
    formula = "=IF(ISERROR($D15),NA(),P5)"
    @eval_fn
    def P15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        p5_1 = Charts_Data_M10.P5()
        var_3 = IF(var_1, var_2, p5_1)
        return var_3

@register(Charts_Data_M10)
class Q15():
    # 'Charts_Data_M10'!Q15
    value = 0.128531378426
    formula = "=IF(ISERROR($D15),NA(),Q5)"
    @eval_fn
    def Q15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        q5_1 = Charts_Data_M10.Q5()
        var_3 = IF(var_1, var_2, q5_1)
        return var_3

@register(Charts_Data_M10)
class R15():
    # 'Charts_Data_M10'!R15
    value = 0.118454771727
    formula = "=IF(ISERROR($D15),NA(),R5)"
    @eval_fn
    def R15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        r5_1 = Charts_Data_M10.R5()
        var_3 = IF(var_1, var_2, r5_1)
        return var_3

@register(Charts_Data_M10)
class S15():
    # 'Charts_Data_M10'!S15
    value = 0.167358872051
    formula = "=IF(ISERROR($D15),NA(),S5)"
    @eval_fn
    def S15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        s5_1 = Charts_Data_M10.S5()
        var_3 = IF(var_1, var_2, s5_1)
        return var_3

@register(Charts_Data_M10)
class T15():
    # 'Charts_Data_M10'!T15
    value = 0.19024272663
    formula = "=IF(ISERROR($D15),NA(),T5)"
    @eval_fn
    def T15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        t5_1 = Charts_Data_M10.T5()
        var_3 = IF(var_1, var_2, t5_1)
        return var_3

@register(Charts_Data_M10)
class U15():
    # 'Charts_Data_M10'!U15
    value = 0.29197521162
    formula = "=IF(ISERROR($D15),NA(),U5)"
    @eval_fn
    def U15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        u5_1 = Charts_Data_M10.U5()
        var_3 = IF(var_1, var_2, u5_1)
        return var_3

@register(Charts_Data_M10)
class V15():
    # 'Charts_Data_M10'!V15
    value = 0.379357429186
    formula = "=IF(ISERROR($D15),NA(),V5)"
    @eval_fn
    def V15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        v5_1 = Charts_Data_M10.V5()
        var_3 = IF(var_1, var_2, v5_1)
        return var_3

@register(Charts_Data_M10)
class W15():
    # 'Charts_Data_M10'!W15
    value = 0.429232584201
    formula = "=IF(ISERROR($D15),NA(),W5)"
    @eval_fn
    def W15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        w5_1 = Charts_Data_M10.W5()
        var_3 = IF(var_1, var_2, w5_1)
        return var_3

@register(Charts_Data_M10)
class X15():
    # 'Charts_Data_M10'!X15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),X5)"
    @eval_fn
    def X15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        x5_1 = Charts_Data_M10.X5()
        var_3 = IF(var_1, var_2, x5_1)
        return var_3

@register(Charts_Data_M10)
class Y15():
    # 'Charts_Data_M10'!Y15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),Y5)"
    @eval_fn
    def Y15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        y5_1 = Charts_Data_M10.Y5()
        var_3 = IF(var_1, var_2, y5_1)
        return var_3

@register(Charts_Data_M10)
class Z15():
    # 'Charts_Data_M10'!Z15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),Z5)"
    @eval_fn
    def Z15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        z5_1 = Charts_Data_M10.Z5()
        var_3 = IF(var_1, var_2, z5_1)
        return var_3

@register(Charts_Data_M10)
class AA15():
    # 'Charts_Data_M10'!AA15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AA5)"
    @eval_fn
    def AA15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        aa5_1 = Charts_Data_M10.AA5()
        var_3 = IF(var_1, var_2, aa5_1)
        return var_3

@register(Charts_Data_M10)
class AB15():
    # 'Charts_Data_M10'!AB15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AB5)"
    @eval_fn
    def AB15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ab5_1 = Charts_Data_M10.AB5()
        var_3 = IF(var_1, var_2, ab5_1)
        return var_3

@register(Charts_Data_M10)
class AC15():
    # 'Charts_Data_M10'!AC15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AC5)"
    @eval_fn
    def AC15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ac5_1 = Charts_Data_M10.AC5()
        var_3 = IF(var_1, var_2, ac5_1)
        return var_3

@register(Charts_Data_M10)
class AD15():
    # 'Charts_Data_M10'!AD15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AD5)"
    @eval_fn
    def AD15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ad5_1 = Charts_Data_M10.AD5()
        var_3 = IF(var_1, var_2, ad5_1)
        return var_3

@register(Charts_Data_M10)
class AE15():
    # 'Charts_Data_M10'!AE15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AE5)"
    @eval_fn
    def AE15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ae5_1 = Charts_Data_M10.AE5()
        var_3 = IF(var_1, var_2, ae5_1)
        return var_3

@register(Charts_Data_M10)
class AF15():
    # 'Charts_Data_M10'!AF15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AF5)"
    @eval_fn
    def AF15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        af5_1 = Charts_Data_M10.AF5()
        var_3 = IF(var_1, var_2, af5_1)
        return var_3

@register(Charts_Data_M10)
class AG15():
    # 'Charts_Data_M10'!AG15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AG5)"
    @eval_fn
    def AG15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ag5_1 = Charts_Data_M10.AG5()
        var_3 = IF(var_1, var_2, ag5_1)
        return var_3

@register(Charts_Data_M10)
class AH15():
    # 'Charts_Data_M10'!AH15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AH5)"
    @eval_fn
    def AH15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ah5_1 = Charts_Data_M10.AH5()
        var_3 = IF(var_1, var_2, ah5_1)
        return var_3

@register(Charts_Data_M10)
class AI15():
    # 'Charts_Data_M10'!AI15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AI5)"
    @eval_fn
    def AI15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ai5_1 = Charts_Data_M10.AI5()
        var_3 = IF(var_1, var_2, ai5_1)
        return var_3

@register(Charts_Data_M10)
class AJ15():
    # 'Charts_Data_M10'!AJ15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AJ5)"
    @eval_fn
    def AJ15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        aj5_1 = Charts_Data_M10.AJ5()
        var_3 = IF(var_1, var_2, aj5_1)
        return var_3

@register(Charts_Data_M10)
class AK15():
    # 'Charts_Data_M10'!AK15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AK5)"
    @eval_fn
    def AK15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        ak5_1 = Charts_Data_M10.AK5()
        var_3 = IF(var_1, var_2, ak5_1)
        return var_3

@register(Charts_Data_M10)
class AL15():
    # 'Charts_Data_M10'!AL15
    value = "#N/A"
    formula = "=IF(ISERROR($D15),NA(),AL5)"
    @eval_fn
    def AL15():
        d15_1 = Charts_Data_M10.D15()
        var_1 = ISERROR(d15_1)
        var_2 = NA()
        al5_1 = Charts_Data_M10.AL5()
        var_3 = IF(var_1, var_2, al5_1)
        return var_3

@register(Charts_Data_M10)
class D16():
    # 'Charts_Data_M10'!D16
    value = "HELCO"
    formula = '''=IF(OR($C$15="Total",$C$15="HELCO"),"HELCO",NA())'''
    @eval_fn
    def D16():
        c15_1 = Charts_Data_M10.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M10.C15()
        var_2 = equal(c15_2, "HELCO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "HELCO", var_4)
        return var_5

@register(Charts_Data_M10)
class F16():
    # 'Charts_Data_M10'!F16
    value = "Notes"

@register(Charts_Data_M10)
class G16():
    # 'Charts_Data_M10'!G16
    value = 0.704989154013
    formula = "=IF(ISERROR($D16),NA(),G6)"
    @eval_fn
    def G16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        g6_1 = Charts_Data_M10.G6()
        var_3 = IF(var_1, var_2, g6_1)
        return var_3

@register(Charts_Data_M10)
class H16():
    # 'Charts_Data_M10'!H16
    value = 0.81498951782
    formula = "=IF(ISERROR($D16),NA(),H6)"
    @eval_fn
    def H16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        h6_1 = Charts_Data_M10.H6()
        var_3 = IF(var_1, var_2, h6_1)
        return var_3

@register(Charts_Data_M10)
class I16():
    # 'Charts_Data_M10'!I16
    value = 0.714285714286
    formula = "=IF(ISERROR($D16),NA(),I6)"
    @eval_fn
    def I16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        i6_1 = Charts_Data_M10.I6()
        var_3 = IF(var_1, var_2, i6_1)
        return var_3

@register(Charts_Data_M10)
class J16():
    # 'Charts_Data_M10'!J16
    value = 0.309045226131
    formula = "=IF(ISERROR($D16),NA(),J6)"
    @eval_fn
    def J16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        j6_1 = Charts_Data_M10.J6()
        var_3 = IF(var_1, var_2, j6_1)
        return var_3

@register(Charts_Data_M10)
class K16():
    # 'Charts_Data_M10'!K16
    value = 0.517208413002
    formula = "=IF(ISERROR($D16),NA(),K6)"
    @eval_fn
    def K16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        k6_1 = Charts_Data_M10.K6()
        var_3 = IF(var_1, var_2, k6_1)
        return var_3

@register(Charts_Data_M10)
class L16():
    # 'Charts_Data_M10'!L16
    value = 0.592105263158
    formula = "=IF(ISERROR($D16),NA(),L6)"
    @eval_fn
    def L16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        l6_1 = Charts_Data_M10.L6()
        var_3 = IF(var_1, var_2, l6_1)
        return var_3

@register(Charts_Data_M10)
class M16():
    # 'Charts_Data_M10'!M16
    value = 0.603401969561
    formula = "=IF(ISERROR($D16),NA(),M6)"
    @eval_fn
    def M16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        m6_1 = Charts_Data_M10.M6()
        var_3 = IF(var_1, var_2, m6_1)
        return var_3

@register(Charts_Data_M10)
class N16():
    # 'Charts_Data_M10'!N16
    value = 0.642297650131
    formula = "=IF(ISERROR($D16),NA(),N6)"
    @eval_fn
    def N16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        n6_1 = Charts_Data_M10.N6()
        var_3 = IF(var_1, var_2, n6_1)
        return var_3

@register(Charts_Data_M10)
class O16():
    # 'Charts_Data_M10'!O16
    value = 0.845012897678
    formula = "=IF(ISERROR($D16),NA(),O6)"
    @eval_fn
    def O16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        o6_1 = Charts_Data_M10.O6()
        var_3 = IF(var_1, var_2, o6_1)
        return var_3

@register(Charts_Data_M10)
class P16():
    # 'Charts_Data_M10'!P16
    value = 0.884038982323
    formula = "=IF(ISERROR($D16),NA(),P6)"
    @eval_fn
    def P16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        p6_1 = Charts_Data_M10.P6()
        var_3 = IF(var_1, var_2, p6_1)
        return var_3

@register(Charts_Data_M10)
class Q16():
    # 'Charts_Data_M10'!Q16
    value = 0.843236915351
    formula = "=IF(ISERROR($D16),NA(),Q6)"
    @eval_fn
    def Q16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        q6_1 = Charts_Data_M10.Q6()
        var_3 = IF(var_1, var_2, q6_1)
        return var_3

@register(Charts_Data_M10)
class R16():
    # 'Charts_Data_M10'!R16
    value = 0.864182457291
    formula = "=IF(ISERROR($D16),NA(),R6)"
    @eval_fn
    def R16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        r6_1 = Charts_Data_M10.R6()
        var_3 = IF(var_1, var_2, r6_1)
        return var_3

@register(Charts_Data_M10)
class S16():
    # 'Charts_Data_M10'!S16
    value = 1.02700367534
    formula = "=IF(ISERROR($D16),NA(),S6)"
    @eval_fn
    def S16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        s6_1 = Charts_Data_M10.S6()
        var_3 = IF(var_1, var_2, s6_1)
        return var_3

@register(Charts_Data_M10)
class T16():
    # 'Charts_Data_M10'!T16
    value = 1.16816151556
    formula = "=IF(ISERROR($D16),NA(),T6)"
    @eval_fn
    def T16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        t6_1 = Charts_Data_M10.T6()
        var_3 = IF(var_1, var_2, t6_1)
        return var_3

@register(Charts_Data_M10)
class U16():
    # 'Charts_Data_M10'!U16
    value = 1.20196328608
    formula = "=IF(ISERROR($D16),NA(),U6)"
    @eval_fn
    def U16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        u6_1 = Charts_Data_M10.U6()
        var_3 = IF(var_1, var_2, u6_1)
        return var_3

@register(Charts_Data_M10)
class V16():
    # 'Charts_Data_M10'!V16
    value = 1.18383542537
    formula = "=IF(ISERROR($D16),NA(),V6)"
    @eval_fn
    def V16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        v6_1 = Charts_Data_M10.V6()
        var_3 = IF(var_1, var_2, v6_1)
        return var_3

@register(Charts_Data_M10)
class W16():
    # 'Charts_Data_M10'!W16
    value = 1.21693816123
    formula = "=IF(ISERROR($D16),NA(),W6)"
    @eval_fn
    def W16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        w6_1 = Charts_Data_M10.W6()
        var_3 = IF(var_1, var_2, w6_1)
        return var_3

@register(Charts_Data_M10)
class X16():
    # 'Charts_Data_M10'!X16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),X6)"
    @eval_fn
    def X16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        x6_1 = Charts_Data_M10.X6()
        var_3 = IF(var_1, var_2, x6_1)
        return var_3

@register(Charts_Data_M10)
class Y16():
    # 'Charts_Data_M10'!Y16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),Y6)"
    @eval_fn
    def Y16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        y6_1 = Charts_Data_M10.Y6()
        var_3 = IF(var_1, var_2, y6_1)
        return var_3

@register(Charts_Data_M10)
class Z16():
    # 'Charts_Data_M10'!Z16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),Z6)"
    @eval_fn
    def Z16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        z6_1 = Charts_Data_M10.Z6()
        var_3 = IF(var_1, var_2, z6_1)
        return var_3

@register(Charts_Data_M10)
class AA16():
    # 'Charts_Data_M10'!AA16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AA6)"
    @eval_fn
    def AA16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        aa6_1 = Charts_Data_M10.AA6()
        var_3 = IF(var_1, var_2, aa6_1)
        return var_3

@register(Charts_Data_M10)
class AB16():
    # 'Charts_Data_M10'!AB16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AB6)"
    @eval_fn
    def AB16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ab6_1 = Charts_Data_M10.AB6()
        var_3 = IF(var_1, var_2, ab6_1)
        return var_3

@register(Charts_Data_M10)
class AC16():
    # 'Charts_Data_M10'!AC16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AC6)"
    @eval_fn
    def AC16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ac6_1 = Charts_Data_M10.AC6()
        var_3 = IF(var_1, var_2, ac6_1)
        return var_3

@register(Charts_Data_M10)
class AD16():
    # 'Charts_Data_M10'!AD16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AD6)"
    @eval_fn
    def AD16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ad6_1 = Charts_Data_M10.AD6()
        var_3 = IF(var_1, var_2, ad6_1)
        return var_3

@register(Charts_Data_M10)
class AE16():
    # 'Charts_Data_M10'!AE16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AE6)"
    @eval_fn
    def AE16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ae6_1 = Charts_Data_M10.AE6()
        var_3 = IF(var_1, var_2, ae6_1)
        return var_3

@register(Charts_Data_M10)
class AF16():
    # 'Charts_Data_M10'!AF16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AF6)"
    @eval_fn
    def AF16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        af6_1 = Charts_Data_M10.AF6()
        var_3 = IF(var_1, var_2, af6_1)
        return var_3

@register(Charts_Data_M10)
class AG16():
    # 'Charts_Data_M10'!AG16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AG6)"
    @eval_fn
    def AG16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ag6_1 = Charts_Data_M10.AG6()
        var_3 = IF(var_1, var_2, ag6_1)
        return var_3

@register(Charts_Data_M10)
class AH16():
    # 'Charts_Data_M10'!AH16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AH6)"
    @eval_fn
    def AH16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ah6_1 = Charts_Data_M10.AH6()
        var_3 = IF(var_1, var_2, ah6_1)
        return var_3

@register(Charts_Data_M10)
class AI16():
    # 'Charts_Data_M10'!AI16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AI6)"
    @eval_fn
    def AI16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ai6_1 = Charts_Data_M10.AI6()
        var_3 = IF(var_1, var_2, ai6_1)
        return var_3

@register(Charts_Data_M10)
class AJ16():
    # 'Charts_Data_M10'!AJ16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AJ6)"
    @eval_fn
    def AJ16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        aj6_1 = Charts_Data_M10.AJ6()
        var_3 = IF(var_1, var_2, aj6_1)
        return var_3

@register(Charts_Data_M10)
class AK16():
    # 'Charts_Data_M10'!AK16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AK6)"
    @eval_fn
    def AK16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        ak6_1 = Charts_Data_M10.AK6()
        var_3 = IF(var_1, var_2, ak6_1)
        return var_3

@register(Charts_Data_M10)
class AL16():
    # 'Charts_Data_M10'!AL16
    value = "#N/A"
    formula = "=IF(ISERROR($D16),NA(),AL6)"
    @eval_fn
    def AL16():
        d16_1 = Charts_Data_M10.D16()
        var_1 = ISERROR(d16_1)
        var_2 = NA()
        al6_1 = Charts_Data_M10.AL6()
        var_3 = IF(var_1, var_2, al6_1)
        return var_3

@register(Charts_Data_M10)
class D17():
    # 'Charts_Data_M10'!D17
    value = "MECO"
    formula = '''=IF(OR($C$15="Total",$C$15="MECO"),"MECO",NA())'''
    @eval_fn
    def D17():
        c15_1 = Charts_Data_M10.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M10.C15()
        var_2 = equal(c15_2, "MECO")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "MECO", var_4)
        return var_5

@register(Charts_Data_M10)
class F17():
    # 'Charts_Data_M10'!F17
    value = "Notes"

@register(Charts_Data_M10)
class G17():
    # 'Charts_Data_M10'!G17
    value = 0.129107981221
    formula = "=IF(ISERROR($D17),NA(),G7)"
    @eval_fn
    def G17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        g7_1 = Charts_Data_M10.G7()
        var_3 = IF(var_1, var_2, g7_1)
        return var_3

@register(Charts_Data_M10)
class H17():
    # 'Charts_Data_M10'!H17
    value = 0.101717902351
    formula = "=IF(ISERROR($D17),NA(),H7)"
    @eval_fn
    def H17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        h7_1 = Charts_Data_M10.H7()
        var_3 = IF(var_1, var_2, h7_1)
        return var_3

@register(Charts_Data_M10)
class I17():
    # 'Charts_Data_M10'!I17
    value = 0.0837742504409
    formula = "=IF(ISERROR($D17),NA(),I7)"
    @eval_fn
    def I17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        i7_1 = Charts_Data_M10.I7()
        var_3 = IF(var_1, var_2, i7_1)
        return var_3

@register(Charts_Data_M10)
class J17():
    # 'Charts_Data_M10'!J17
    value = 0.148835202761
    formula = "=IF(ISERROR($D17),NA(),J7)"
    @eval_fn
    def J17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        j7_1 = Charts_Data_M10.J7()
        var_3 = IF(var_1, var_2, j7_1)
        return var_3

@register(Charts_Data_M10)
class K17():
    # 'Charts_Data_M10'!K17
    value = 0.136702568351
    formula = "=IF(ISERROR($D17),NA(),K7)"
    @eval_fn
    def K17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        k7_1 = Charts_Data_M10.K7()
        var_3 = IF(var_1, var_2, k7_1)
        return var_3

@register(Charts_Data_M10)
class L17():
    # 'Charts_Data_M10'!L17
    value = 0.14875701684
    formula = "=IF(ISERROR($D17),NA(),L7)"
    @eval_fn
    def L17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        l7_1 = Charts_Data_M10.L7()
        var_3 = IF(var_1, var_2, l7_1)
        return var_3

@register(Charts_Data_M10)
class M17():
    # 'Charts_Data_M10'!M17
    value = 0.150559105431
    formula = "=IF(ISERROR($D17),NA(),M7)"
    @eval_fn
    def M17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        m7_1 = Charts_Data_M10.M7()
        var_3 = IF(var_1, var_2, m7_1)
        return var_3

@register(Charts_Data_M10)
class N17():
    # 'Charts_Data_M10'!N17
    value = 0.270339652449
    formula = "=IF(ISERROR($D17),NA(),N7)"
    @eval_fn
    def N17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        n7_1 = Charts_Data_M10.N7()
        var_3 = IF(var_1, var_2, n7_1)
        return var_3

@register(Charts_Data_M10)
class O17():
    # 'Charts_Data_M10'!O17
    value = 0.3861328125
    formula = "=IF(ISERROR($D17),NA(),O7)"
    @eval_fn
    def O17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        o7_1 = Charts_Data_M10.O7()
        var_3 = IF(var_1, var_2, o7_1)
        return var_3

@register(Charts_Data_M10)
class P17():
    # 'Charts_Data_M10'!P17
    value = 0.346846988609
    formula = "=IF(ISERROR($D17),NA(),P7)"
    @eval_fn
    def P17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        p7_1 = Charts_Data_M10.P7()
        var_3 = IF(var_1, var_2, p7_1)
        return var_3

@register(Charts_Data_M10)
class Q17():
    # 'Charts_Data_M10'!Q17
    value = 0.347737415946
    formula = "=IF(ISERROR($D17),NA(),Q7)"
    @eval_fn
    def Q17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        q7_1 = Charts_Data_M10.Q7()
        var_3 = IF(var_1, var_2, q7_1)
        return var_3

@register(Charts_Data_M10)
class R17():
    # 'Charts_Data_M10'!R17
    value = 0.383027613404
    formula = "=IF(ISERROR($D17),NA(),R7)"
    @eval_fn
    def R17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        r7_1 = Charts_Data_M10.R7()
        var_3 = IF(var_1, var_2, r7_1)
        return var_3

@register(Charts_Data_M10)
class S17():
    # 'Charts_Data_M10'!S17
    value = 0.428165849016
    formula = "=IF(ISERROR($D17),NA(),S7)"
    @eval_fn
    def S17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        s7_1 = Charts_Data_M10.S7()
        var_3 = IF(var_1, var_2, s7_1)
        return var_3

@register(Charts_Data_M10)
class T17():
    # 'Charts_Data_M10'!T17
    value = 0.520423520656
    formula = "=IF(ISERROR($D17),NA(),T7)"
    @eval_fn
    def T17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        t7_1 = Charts_Data_M10.T7()
        var_3 = IF(var_1, var_2, t7_1)
        return var_3

@register(Charts_Data_M10)
class U17():
    # 'Charts_Data_M10'!U17
    value = 0.727101182247
    formula = "=IF(ISERROR($D17),NA(),U7)"
    @eval_fn
    def U17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        u7_1 = Charts_Data_M10.U7()
        var_3 = IF(var_1, var_2, u7_1)
        return var_3

@register(Charts_Data_M10)
class V17():
    # 'Charts_Data_M10'!V17
    value = 0.842164610231
    formula = "=IF(ISERROR($D17),NA(),V7)"
    @eval_fn
    def V17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        v7_1 = Charts_Data_M10.V7()
        var_3 = IF(var_1, var_2, v7_1)
        return var_3

@register(Charts_Data_M10)
class W17():
    # 'Charts_Data_M10'!W17
    value = 0.885243884215
    formula = "=IF(ISERROR($D17),NA(),W7)"
    @eval_fn
    def W17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        w7_1 = Charts_Data_M10.W7()
        var_3 = IF(var_1, var_2, w7_1)
        return var_3

@register(Charts_Data_M10)
class X17():
    # 'Charts_Data_M10'!X17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),X7)"
    @eval_fn
    def X17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        x7_1 = Charts_Data_M10.X7()
        var_3 = IF(var_1, var_2, x7_1)
        return var_3

@register(Charts_Data_M10)
class Y17():
    # 'Charts_Data_M10'!Y17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),Y7)"
    @eval_fn
    def Y17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        y7_1 = Charts_Data_M10.Y7()
        var_3 = IF(var_1, var_2, y7_1)
        return var_3

@register(Charts_Data_M10)
class Z17():
    # 'Charts_Data_M10'!Z17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),Z7)"
    @eval_fn
    def Z17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        z7_1 = Charts_Data_M10.Z7()
        var_3 = IF(var_1, var_2, z7_1)
        return var_3

@register(Charts_Data_M10)
class AA17():
    # 'Charts_Data_M10'!AA17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AA7)"
    @eval_fn
    def AA17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        aa7_1 = Charts_Data_M10.AA7()
        var_3 = IF(var_1, var_2, aa7_1)
        return var_3

@register(Charts_Data_M10)
class AB17():
    # 'Charts_Data_M10'!AB17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AB7)"
    @eval_fn
    def AB17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ab7_1 = Charts_Data_M10.AB7()
        var_3 = IF(var_1, var_2, ab7_1)
        return var_3

@register(Charts_Data_M10)
class AC17():
    # 'Charts_Data_M10'!AC17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AC7)"
    @eval_fn
    def AC17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ac7_1 = Charts_Data_M10.AC7()
        var_3 = IF(var_1, var_2, ac7_1)
        return var_3

@register(Charts_Data_M10)
class AD17():
    # 'Charts_Data_M10'!AD17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AD7)"
    @eval_fn
    def AD17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ad7_1 = Charts_Data_M10.AD7()
        var_3 = IF(var_1, var_2, ad7_1)
        return var_3

@register(Charts_Data_M10)
class AE17():
    # 'Charts_Data_M10'!AE17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AE7)"
    @eval_fn
    def AE17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ae7_1 = Charts_Data_M10.AE7()
        var_3 = IF(var_1, var_2, ae7_1)
        return var_3

@register(Charts_Data_M10)
class AF17():
    # 'Charts_Data_M10'!AF17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AF7)"
    @eval_fn
    def AF17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        af7_1 = Charts_Data_M10.AF7()
        var_3 = IF(var_1, var_2, af7_1)
        return var_3

@register(Charts_Data_M10)
class AG17():
    # 'Charts_Data_M10'!AG17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AG7)"
    @eval_fn
    def AG17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ag7_1 = Charts_Data_M10.AG7()
        var_3 = IF(var_1, var_2, ag7_1)
        return var_3

@register(Charts_Data_M10)
class AH17():
    # 'Charts_Data_M10'!AH17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AH7)"
    @eval_fn
    def AH17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ah7_1 = Charts_Data_M10.AH7()
        var_3 = IF(var_1, var_2, ah7_1)
        return var_3

@register(Charts_Data_M10)
class AI17():
    # 'Charts_Data_M10'!AI17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AI7)"
    @eval_fn
    def AI17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ai7_1 = Charts_Data_M10.AI7()
        var_3 = IF(var_1, var_2, ai7_1)
        return var_3

@register(Charts_Data_M10)
class AJ17():
    # 'Charts_Data_M10'!AJ17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AJ7)"
    @eval_fn
    def AJ17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        aj7_1 = Charts_Data_M10.AJ7()
        var_3 = IF(var_1, var_2, aj7_1)
        return var_3

@register(Charts_Data_M10)
class AK17():
    # 'Charts_Data_M10'!AK17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AK7)"
    @eval_fn
    def AK17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        ak7_1 = Charts_Data_M10.AK7()
        var_3 = IF(var_1, var_2, ak7_1)
        return var_3

@register(Charts_Data_M10)
class AL17():
    # 'Charts_Data_M10'!AL17
    value = "#N/A"
    formula = "=IF(ISERROR($D17),NA(),AL7)"
    @eval_fn
    def AL17():
        d17_1 = Charts_Data_M10.D17()
        var_1 = ISERROR(d17_1)
        var_2 = NA()
        al7_1 = Charts_Data_M10.AL7()
        var_3 = IF(var_1, var_2, al7_1)
        return var_3

@register(Charts_Data_M10)
class D18():
    # 'Charts_Data_M10'!D18
    value = "KIUC"
    formula = '''=IF(OR($C$15="Total",$C$15="KIUC"),"KIUC",NA())'''
    @eval_fn
    def D18():
        c15_1 = Charts_Data_M10.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M10.C15()
        var_2 = equal(c15_2, "KIUC")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "KIUC", var_4)
        return var_5

@register(Charts_Data_M10)
class F18():
    # 'Charts_Data_M10'!F18
    value = "Notes"

@register(Charts_Data_M10)
class G18():
    # 'Charts_Data_M10'!G18
    value = 0
    formula = "=IF(ISERROR($D18),NA(),G8)"
    @eval_fn
    def G18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        g8_1 = Charts_Data_M10.G8()
        var_3 = IF(var_1, var_2, g8_1)
        return var_3

@register(Charts_Data_M10)
class H18():
    # 'Charts_Data_M10'!H18
    value = 0
    formula = "=IF(ISERROR($D18),NA(),H8)"
    @eval_fn
    def H18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        h8_1 = Charts_Data_M10.H8()
        var_3 = IF(var_1, var_2, h8_1)
        return var_3

@register(Charts_Data_M10)
class I18():
    # 'Charts_Data_M10'!I18
    value = 0
    formula = "=IF(ISERROR($D18),NA(),I8)"
    @eval_fn
    def I18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        i8_1 = Charts_Data_M10.I8()
        var_3 = IF(var_1, var_2, i8_1)
        return var_3

@register(Charts_Data_M10)
class J18():
    # 'Charts_Data_M10'!J18
    value = 0
    formula = "=IF(ISERROR($D18),NA(),J8)"
    @eval_fn
    def J18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        j8_1 = Charts_Data_M10.J8()
        var_3 = IF(var_1, var_2, j8_1)
        return var_3

@register(Charts_Data_M10)
class K18():
    # 'Charts_Data_M10'!K18
    value = 0.145612259782
    formula = "=IF(ISERROR($D18),NA(),K8)"
    @eval_fn
    def K18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        k8_1 = Charts_Data_M10.K8()
        var_3 = IF(var_1, var_2, k8_1)
        return var_3

@register(Charts_Data_M10)
class L18():
    # 'Charts_Data_M10'!L18
    value = 0.199732690326
    formula = "=IF(ISERROR($D18),NA(),L8)"
    @eval_fn
    def L18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        l8_1 = Charts_Data_M10.L8()
        var_3 = IF(var_1, var_2, l8_1)
        return var_3

@register(Charts_Data_M10)
class M18():
    # 'Charts_Data_M10'!M18
    value = 0.199745833311
    formula = "=IF(ISERROR($D18),NA(),M8)"
    @eval_fn
    def M18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        m8_1 = Charts_Data_M10.M8()
        var_3 = IF(var_1, var_2, m8_1)
        return var_3

@register(Charts_Data_M10)
class N18():
    # 'Charts_Data_M10'!N18
    value = 0.195941117045
    formula = "=IF(ISERROR($D18),NA(),N8)"
    @eval_fn
    def N18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        n8_1 = Charts_Data_M10.N8()
        var_3 = IF(var_1, var_2, n8_1)
        return var_3

@register(Charts_Data_M10)
class O18():
    # 'Charts_Data_M10'!O18
    value = 0.137948410347
    formula = "=IF(ISERROR($D18),NA(),O8)"
    @eval_fn
    def O18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        o8_1 = Charts_Data_M10.O8()
        var_3 = IF(var_1, var_2, o8_1)
        return var_3

@register(Charts_Data_M10)
class P18():
    # 'Charts_Data_M10'!P18
    value = 0.205314919027
    formula = "=IF(ISERROR($D18),NA(),P8)"
    @eval_fn
    def P18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        p8_1 = Charts_Data_M10.P8()
        var_3 = IF(var_1, var_2, p8_1)
        return var_3

@register(Charts_Data_M10)
class Q18():
    # 'Charts_Data_M10'!Q18
    value = 0.227758304326
    formula = "=IF(ISERROR($D18),NA(),Q8)"
    @eval_fn
    def Q18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        q8_1 = Charts_Data_M10.Q8()
        var_3 = IF(var_1, var_2, q8_1)
        return var_3

@register(Charts_Data_M10)
class R18():
    # 'Charts_Data_M10'!R18
    value = 0.221020509585
    formula = "=IF(ISERROR($D18),NA(),R8)"
    @eval_fn
    def R18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        r8_1 = Charts_Data_M10.R8()
        var_3 = IF(var_1, var_2, r8_1)
        return var_3

@register(Charts_Data_M10)
class S18():
    # 'Charts_Data_M10'!S18
    value = 0.264811181181
    formula = "=IF(ISERROR($D18),NA(),S8)"
    @eval_fn
    def S18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        s8_1 = Charts_Data_M10.S8()
        var_3 = IF(var_1, var_2, s8_1)
        return var_3

@register(Charts_Data_M10)
class T18():
    # 'Charts_Data_M10'!T18
    value = 0.31203186936
    formula = "=IF(ISERROR($D18),NA(),T8)"
    @eval_fn
    def T18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        t8_1 = Charts_Data_M10.T8()
        var_3 = IF(var_1, var_2, t8_1)
        return var_3

@register(Charts_Data_M10)
class U18():
    # 'Charts_Data_M10'!U18
    value = 0.40625204676
    formula = "=IF(ISERROR($D18),NA(),U8)"
    @eval_fn
    def U18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        u8_1 = Charts_Data_M10.U8()
        var_3 = IF(var_1, var_2, u8_1)
        return var_3

@register(Charts_Data_M10)
class V18():
    # 'Charts_Data_M10'!V18
    value = 0.526871863584
    formula = "=IF(ISERROR($D18),NA(),V8)"
    @eval_fn
    def V18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        v8_1 = Charts_Data_M10.V8()
        var_3 = IF(var_1, var_2, v8_1)
        return var_3

@register(Charts_Data_M10)
class W18():
    # 'Charts_Data_M10'!W18
    value = 0.682828100482
    formula = "=IF(ISERROR($D18),NA(),W8)"
    @eval_fn
    def W18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        w8_1 = Charts_Data_M10.W8()
        var_3 = IF(var_1, var_2, w8_1)
        return var_3

@register(Charts_Data_M10)
class X18():
    # 'Charts_Data_M10'!X18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),X8)"
    @eval_fn
    def X18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        x8_1 = Charts_Data_M10.X8()
        var_3 = IF(var_1, var_2, x8_1)
        return var_3

@register(Charts_Data_M10)
class Y18():
    # 'Charts_Data_M10'!Y18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),Y8)"
    @eval_fn
    def Y18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        y8_1 = Charts_Data_M10.Y8()
        var_3 = IF(var_1, var_2, y8_1)
        return var_3

@register(Charts_Data_M10)
class Z18():
    # 'Charts_Data_M10'!Z18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),Z8)"
    @eval_fn
    def Z18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        z8_1 = Charts_Data_M10.Z8()
        var_3 = IF(var_1, var_2, z8_1)
        return var_3

@register(Charts_Data_M10)
class AA18():
    # 'Charts_Data_M10'!AA18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AA8)"
    @eval_fn
    def AA18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        aa8_1 = Charts_Data_M10.AA8()
        var_3 = IF(var_1, var_2, aa8_1)
        return var_3

@register(Charts_Data_M10)
class AB18():
    # 'Charts_Data_M10'!AB18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AB8)"
    @eval_fn
    def AB18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ab8_1 = Charts_Data_M10.AB8()
        var_3 = IF(var_1, var_2, ab8_1)
        return var_3

@register(Charts_Data_M10)
class AC18():
    # 'Charts_Data_M10'!AC18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AC8)"
    @eval_fn
    def AC18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ac8_1 = Charts_Data_M10.AC8()
        var_3 = IF(var_1, var_2, ac8_1)
        return var_3

@register(Charts_Data_M10)
class AD18():
    # 'Charts_Data_M10'!AD18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AD8)"
    @eval_fn
    def AD18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ad8_1 = Charts_Data_M10.AD8()
        var_3 = IF(var_1, var_2, ad8_1)
        return var_3

@register(Charts_Data_M10)
class AE18():
    # 'Charts_Data_M10'!AE18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AE8)"
    @eval_fn
    def AE18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ae8_1 = Charts_Data_M10.AE8()
        var_3 = IF(var_1, var_2, ae8_1)
        return var_3

@register(Charts_Data_M10)
class AF18():
    # 'Charts_Data_M10'!AF18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AF8)"
    @eval_fn
    def AF18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        af8_1 = Charts_Data_M10.AF8()
        var_3 = IF(var_1, var_2, af8_1)
        return var_3

@register(Charts_Data_M10)
class AG18():
    # 'Charts_Data_M10'!AG18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AG8)"
    @eval_fn
    def AG18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ag8_1 = Charts_Data_M10.AG8()
        var_3 = IF(var_1, var_2, ag8_1)
        return var_3

@register(Charts_Data_M10)
class AH18():
    # 'Charts_Data_M10'!AH18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AH8)"
    @eval_fn
    def AH18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ah8_1 = Charts_Data_M10.AH8()
        var_3 = IF(var_1, var_2, ah8_1)
        return var_3

@register(Charts_Data_M10)
class AI18():
    # 'Charts_Data_M10'!AI18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AI8)"
    @eval_fn
    def AI18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ai8_1 = Charts_Data_M10.AI8()
        var_3 = IF(var_1, var_2, ai8_1)
        return var_3

@register(Charts_Data_M10)
class AJ18():
    # 'Charts_Data_M10'!AJ18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AJ8)"
    @eval_fn
    def AJ18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        aj8_1 = Charts_Data_M10.AJ8()
        var_3 = IF(var_1, var_2, aj8_1)
        return var_3

@register(Charts_Data_M10)
class AK18():
    # 'Charts_Data_M10'!AK18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AK8)"
    @eval_fn
    def AK18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        ak8_1 = Charts_Data_M10.AK8()
        var_3 = IF(var_1, var_2, ak8_1)
        return var_3

@register(Charts_Data_M10)
class AL18():
    # 'Charts_Data_M10'!AL18
    value = "#N/A"
    formula = "=IF(ISERROR($D18),NA(),AL8)"
    @eval_fn
    def AL18():
        d18_1 = Charts_Data_M10.D18()
        var_1 = ISERROR(d18_1)
        var_2 = NA()
        al8_1 = Charts_Data_M10.AL8()
        var_3 = IF(var_1, var_2, al8_1)
        return var_3

@register(Charts_Data_M10)
class D19():
    # 'Charts_Data_M10'!D19
    value = "Total"
    formula = '''=IF(OR($C$15="Total",$C$15="Total"),"Total",NA())'''
    @eval_fn
    def D19():
        c15_1 = Charts_Data_M10.C15()
        var_1 = equal(c15_1, "Total")
        c15_2 = Charts_Data_M10.C15()
        var_2 = equal(c15_2, "Total")
        var_3 = OR(var_1, var_2)
        var_4 = NA()
        var_5 = IF(var_3, "Total", var_4)
        return var_5

@register(Charts_Data_M10)
class F19():
    # 'Charts_Data_M10'!F19
    value = "Notes"

@register(Charts_Data_M10)
class G19():
    # 'Charts_Data_M10'!G19
    value = 0.140685946105
    formula = "=IF(ISTEXT($D19),G4,NA())"
    @eval_fn
    def G19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        g4_1 = Charts_Data_M10.G4()
        var_2 = NA()
        var_3 = IF(var_1, g4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class H19():
    # 'Charts_Data_M10'!H19
    value = 0.175069685961
    formula = "=IF(ISTEXT($D19),H4,NA())"
    @eval_fn
    def H19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        h4_1 = Charts_Data_M10.H4()
        var_2 = NA()
        var_3 = IF(var_1, h4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class I19():
    # 'Charts_Data_M10'!I19
    value = 0.156667174115
    formula = "=IF(ISTEXT($D19),I4,NA())"
    @eval_fn
    def I19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        i4_1 = Charts_Data_M10.I4()
        var_2 = NA()
        var_3 = IF(var_1, i4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class J19():
    # 'Charts_Data_M10'!J19
    value = 0.129793727507
    formula = "=IF(ISTEXT($D19),J4,NA())"
    @eval_fn
    def J19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        j4_1 = Charts_Data_M10.J4()
        var_2 = NA()
        var_3 = IF(var_1, j4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class K19():
    # 'Charts_Data_M10'!K19
    value = 0.165501115749
    formula = "=IF(ISTEXT($D19),K4,NA())"
    @eval_fn
    def K19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        k4_1 = Charts_Data_M10.K4()
        var_2 = NA()
        var_3 = IF(var_1, k4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class L19():
    # 'Charts_Data_M10'!L19
    value = 0.175089079901
    formula = "=IF(ISTEXT($D19),L4,NA())"
    @eval_fn
    def L19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        l4_1 = Charts_Data_M10.L4()
        var_2 = NA()
        var_3 = IF(var_1, l4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class M19():
    # 'Charts_Data_M10'!M19
    value = 0.169517031403
    formula = "=IF(ISTEXT($D19),M4,NA())"
    @eval_fn
    def M19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        m4_1 = Charts_Data_M10.M4()
        var_2 = NA()
        var_3 = IF(var_1, m4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class N19():
    # 'Charts_Data_M10'!N19
    value = 0.204137387828
    formula = "=IF(ISTEXT($D19),N4,NA())"
    @eval_fn
    def N19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        n4_1 = Charts_Data_M10.N4()
        var_2 = NA()
        var_3 = IF(var_1, n4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class O19():
    # 'Charts_Data_M10'!O19
    value = 0.222782315884
    formula = "=IF(ISTEXT($D19),O4,NA())"
    @eval_fn
    def O19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        o4_1 = Charts_Data_M10.O4()
        var_2 = NA()
        var_3 = IF(var_1, o4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class P19():
    # 'Charts_Data_M10'!P19
    value = 0.234702545853
    formula = "=IF(ISTEXT($D19),P4,NA())"
    @eval_fn
    def P19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        p4_1 = Charts_Data_M10.P4()
        var_2 = NA()
        var_3 = IF(var_1, p4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class Q19():
    # 'Charts_Data_M10'!Q19
    value = 0.237635646443
    formula = "=IF(ISTEXT($D19),Q4,NA())"
    @eval_fn
    def Q19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        q4_1 = Charts_Data_M10.Q4()
        var_2 = NA()
        var_3 = IF(var_1, q4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class R19():
    # 'Charts_Data_M10'!R19
    value = 0.237004899189
    formula = "=IF(ISTEXT($D19),R4,NA())"
    @eval_fn
    def R19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        r4_1 = Charts_Data_M10.R4()
        var_2 = NA()
        var_3 = IF(var_1, r4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class S19():
    # 'Charts_Data_M10'!S19
    value = 0.297679064526
    formula = "=IF(ISTEXT($D19),S4,NA())"
    @eval_fn
    def S19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        s4_1 = Charts_Data_M10.S4()
        var_2 = NA()
        var_3 = IF(var_1, s4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class T19():
    # 'Charts_Data_M10'!T19
    value = 0.345024369608
    formula = "=IF(ISTEXT($D19),T4,NA())"
    @eval_fn
    def T19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        t4_1 = Charts_Data_M10.T4()
        var_2 = NA()
        var_3 = IF(var_1, t4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class U19():
    # 'Charts_Data_M10'!U19
    value = 0.452207177191
    formula = "=IF(ISTEXT($D19),U4,NA())"
    @eval_fn
    def U19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        u4_1 = Charts_Data_M10.U4()
        var_2 = NA()
        var_3 = IF(var_1, u4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class V19():
    # 'Charts_Data_M10'!V19
    value = 0.532673712018
    formula = "=IF(ISTEXT($D19),V4,NA())"
    @eval_fn
    def V19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        v4_1 = Charts_Data_M10.V4()
        var_2 = NA()
        var_3 = IF(var_1, v4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class W19():
    # 'Charts_Data_M10'!W19
    value = 0.585495074013
    formula = "=IF(ISTEXT($D19),W4,NA())"
    @eval_fn
    def W19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        w4_1 = Charts_Data_M10.W4()
        var_2 = NA()
        var_3 = IF(var_1, w4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class X19():
    # 'Charts_Data_M10'!X19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),X4,NA())"
    @eval_fn
    def X19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        x4_1 = Charts_Data_M10.X4()
        var_2 = NA()
        var_3 = IF(var_1, x4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class Y19():
    # 'Charts_Data_M10'!Y19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),Y4,NA())"
    @eval_fn
    def Y19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        y4_1 = Charts_Data_M10.Y4()
        var_2 = NA()
        var_3 = IF(var_1, y4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class Z19():
    # 'Charts_Data_M10'!Z19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),Z4,NA())"
    @eval_fn
    def Z19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        z4_1 = Charts_Data_M10.Z4()
        var_2 = NA()
        var_3 = IF(var_1, z4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AA19():
    # 'Charts_Data_M10'!AA19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AA4,NA())"
    @eval_fn
    def AA19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        aa4_1 = Charts_Data_M10.AA4()
        var_2 = NA()
        var_3 = IF(var_1, aa4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AB19():
    # 'Charts_Data_M10'!AB19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AB4,NA())"
    @eval_fn
    def AB19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ab4_1 = Charts_Data_M10.AB4()
        var_2 = NA()
        var_3 = IF(var_1, ab4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AC19():
    # 'Charts_Data_M10'!AC19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AC4,NA())"
    @eval_fn
    def AC19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ac4_1 = Charts_Data_M10.AC4()
        var_2 = NA()
        var_3 = IF(var_1, ac4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AD19():
    # 'Charts_Data_M10'!AD19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AD4,NA())"
    @eval_fn
    def AD19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ad4_1 = Charts_Data_M10.AD4()
        var_2 = NA()
        var_3 = IF(var_1, ad4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AE19():
    # 'Charts_Data_M10'!AE19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AE4,NA())"
    @eval_fn
    def AE19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ae4_1 = Charts_Data_M10.AE4()
        var_2 = NA()
        var_3 = IF(var_1, ae4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AF19():
    # 'Charts_Data_M10'!AF19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AF4,NA())"
    @eval_fn
    def AF19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        af4_1 = Charts_Data_M10.AF4()
        var_2 = NA()
        var_3 = IF(var_1, af4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AG19():
    # 'Charts_Data_M10'!AG19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AG4,NA())"
    @eval_fn
    def AG19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ag4_1 = Charts_Data_M10.AG4()
        var_2 = NA()
        var_3 = IF(var_1, ag4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AH19():
    # 'Charts_Data_M10'!AH19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AH4,NA())"
    @eval_fn
    def AH19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ah4_1 = Charts_Data_M10.AH4()
        var_2 = NA()
        var_3 = IF(var_1, ah4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AI19():
    # 'Charts_Data_M10'!AI19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AI4,NA())"
    @eval_fn
    def AI19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ai4_1 = Charts_Data_M10.AI4()
        var_2 = NA()
        var_3 = IF(var_1, ai4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AJ19():
    # 'Charts_Data_M10'!AJ19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AJ4,NA())"
    @eval_fn
    def AJ19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        aj4_1 = Charts_Data_M10.AJ4()
        var_2 = NA()
        var_3 = IF(var_1, aj4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AK19():
    # 'Charts_Data_M10'!AK19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AK4,NA())"
    @eval_fn
    def AK19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        ak4_1 = Charts_Data_M10.AK4()
        var_2 = NA()
        var_3 = IF(var_1, ak4_1, var_2)
        return var_3

@register(Charts_Data_M10)
class AL19():
    # 'Charts_Data_M10'!AL19
    value = "#N/A"
    formula = "=IF(ISTEXT($D19),AL4,NA())"
    @eval_fn
    def AL19():
        d19_1 = Charts_Data_M10.D19()
        var_1 = ISTEXT(d19_1)
        al4_1 = Charts_Data_M10.AL4()
        var_2 = NA()
        var_3 = IF(var_1, al4_1, var_2)
        return var_3