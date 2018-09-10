# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Synthetic_Natural_Gas = Worksheet('Synthetic_Natural_Gas', 10, 10)



@register(Synthetic_Natural_Gas)
class A1():
    # 'Synthetic_Natural_Gas'!A1
    value = "conversion rate"

@register(Synthetic_Natural_Gas)
class D1():
    # 'Synthetic_Natural_Gas'!D1
    value = 1986

@register(Synthetic_Natural_Gas)
class E1():
    # 'Synthetic_Natural_Gas'!E1
    value = 1987

@register(Synthetic_Natural_Gas)
class F1():
    # 'Synthetic_Natural_Gas'!F1
    value = 1988

@register(Synthetic_Natural_Gas)
class G1():
    # 'Synthetic_Natural_Gas'!G1
    value = 1989

@register(Synthetic_Natural_Gas)
class H1():
    # 'Synthetic_Natural_Gas'!H1
    value = 1990

@register(Synthetic_Natural_Gas)
class I1():
    # 'Synthetic_Natural_Gas'!I1
    value = 1991

@register(Synthetic_Natural_Gas)
class J1():
    # 'Synthetic_Natural_Gas'!J1
    value = 1992

@register(Synthetic_Natural_Gas)
class K1():
    # 'Synthetic_Natural_Gas'!K1
    value = 1993

@register(Synthetic_Natural_Gas)
class L1():
    # 'Synthetic_Natural_Gas'!L1
    value = 1994

@register(Synthetic_Natural_Gas)
class M1():
    # 'Synthetic_Natural_Gas'!M1
    value = 1995

@register(Synthetic_Natural_Gas)
class N1():
    # 'Synthetic_Natural_Gas'!N1
    value = 1996

@register(Synthetic_Natural_Gas)
class O1():
    # 'Synthetic_Natural_Gas'!O1
    value = 1997

@register(Synthetic_Natural_Gas)
class P1():
    # 'Synthetic_Natural_Gas'!P1
    value = 1998

@register(Synthetic_Natural_Gas)
class Q1():
    # 'Synthetic_Natural_Gas'!Q1
    value = 1999

@register(Synthetic_Natural_Gas)
class R1():
    # 'Synthetic_Natural_Gas'!R1
    value = 2000

@register(Synthetic_Natural_Gas)
class S1():
    # 'Synthetic_Natural_Gas'!S1
    value = 2001

@register(Synthetic_Natural_Gas)
class T1():
    # 'Synthetic_Natural_Gas'!T1
    value = 2002

@register(Synthetic_Natural_Gas)
class U1():
    # 'Synthetic_Natural_Gas'!U1
    value = 2003

@register(Synthetic_Natural_Gas)
class V1():
    # 'Synthetic_Natural_Gas'!V1
    value = 2004

@register(Synthetic_Natural_Gas)
class W1():
    # 'Synthetic_Natural_Gas'!W1
    value = 2005

@register(Synthetic_Natural_Gas)
class X1():
    # 'Synthetic_Natural_Gas'!X1
    value = 2006

@register(Synthetic_Natural_Gas)
class Y1():
    # 'Synthetic_Natural_Gas'!Y1
    value = 2007

@register(Synthetic_Natural_Gas)
class Z1():
    # 'Synthetic_Natural_Gas'!Z1
    value = 2008

@register(Synthetic_Natural_Gas)
class AA1():
    # 'Synthetic_Natural_Gas'!AA1
    value = 2009

@register(Synthetic_Natural_Gas)
class AB1():
    # 'Synthetic_Natural_Gas'!AB1
    value = 2010

@register(Synthetic_Natural_Gas)
class AC1():
    # 'Synthetic_Natural_Gas'!AC1
    value = 2011

@register(Synthetic_Natural_Gas)
class B2():
    # 'Synthetic_Natural_Gas'!B2
    value = "mmbtu/barrel"

@register(Synthetic_Natural_Gas)
class C2():
    # 'Synthetic_Natural_Gas'!C2
    value = "http://www.eia.gov/forecasts/aeo/pdf/appg.pdf "

@register(Synthetic_Natural_Gas)
class D2():
    # 'Synthetic_Natural_Gas'!D2
    value = 5.82980739678
    formula = "='EIA Consumption'!AE218/'EIA Consumption'!AE219"
    @eval_fn
    def D2():
        ae218_1 = EIA_Consumption.AE218()
        ae219_1 = EIA_Consumption.AE219()
        var_1 = divide(ae218_1, ae219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class E2():
    # 'Synthetic_Natural_Gas'!E2
    value = 5.81114016604
    formula = "='EIA Consumption'!AF218/'EIA Consumption'!AF219"
    @eval_fn
    def E2():
        af218_1 = EIA_Consumption.AF218()
        af219_1 = EIA_Consumption.AF219()
        var_1 = divide(af218_1, af219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class F2():
    # 'Synthetic_Natural_Gas'!F2
    value = 5.83904840748
    formula = "='EIA Consumption'!AG218/'EIA Consumption'!AG219"
    @eval_fn
    def F2():
        ag218_1 = EIA_Consumption.AG218()
        ag219_1 = EIA_Consumption.AG219()
        var_1 = divide(ag218_1, ag219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class G2():
    # 'Synthetic_Natural_Gas'!G2
    value = 5.83282313988
    formula = "='EIA Consumption'!AH218/'EIA Consumption'!AH219"
    @eval_fn
    def G2():
        ah218_1 = EIA_Consumption.AH218()
        ah219_1 = EIA_Consumption.AH219()
        var_1 = divide(ah218_1, ah219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class H2():
    # 'Synthetic_Natural_Gas'!H2
    value = 5.85350394882
    formula = "='EIA Consumption'!AI218/'EIA Consumption'!AI219"
    @eval_fn
    def H2():
        ai218_1 = EIA_Consumption.AI218()
        ai219_1 = EIA_Consumption.AI219()
        var_1 = divide(ai218_1, ai219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class I2():
    # 'Synthetic_Natural_Gas'!I2
    value = 5.82575724463
    formula = "='EIA Consumption'!AJ218/'EIA Consumption'!AJ219"
    @eval_fn
    def I2():
        aj218_1 = EIA_Consumption.AJ218()
        aj219_1 = EIA_Consumption.AJ219()
        var_1 = divide(aj218_1, aj219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class J2():
    # 'Synthetic_Natural_Gas'!J2
    value = 5.84057442932
    formula = "='EIA Consumption'!AK218/'EIA Consumption'!AK219"
    @eval_fn
    def J2():
        ak218_1 = EIA_Consumption.AK218()
        ak219_1 = EIA_Consumption.AK219()
        var_1 = divide(ak218_1, ak219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class K2():
    # 'Synthetic_Natural_Gas'!K2
    value = 5.79012852725
    formula = "='EIA Consumption'!AL218/'EIA Consumption'!AL219"
    @eval_fn
    def K2():
        al218_1 = EIA_Consumption.AL218()
        al219_1 = EIA_Consumption.AL219()
        var_1 = divide(al218_1, al219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class L2():
    # 'Synthetic_Natural_Gas'!L2
    value = 5.75846843432
    formula = "='EIA Consumption'!AM218/'EIA Consumption'!AM219"
    @eval_fn
    def L2():
        am218_1 = EIA_Consumption.AM218()
        am219_1 = EIA_Consumption.AM219()
        var_1 = divide(am218_1, am219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class M2():
    # 'Synthetic_Natural_Gas'!M2
    value = 5.75968249624
    formula = "='EIA Consumption'!AN218/'EIA Consumption'!AN219"
    @eval_fn
    def M2():
        an218_1 = EIA_Consumption.AN218()
        an219_1 = EIA_Consumption.AN219()
        var_1 = divide(an218_1, an219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class N2():
    # 'Synthetic_Natural_Gas'!N2
    value = 5.73632629531
    formula = "='EIA Consumption'!AO218/'EIA Consumption'!AO219"
    @eval_fn
    def N2():
        ao218_1 = EIA_Consumption.AO218()
        ao219_1 = EIA_Consumption.AO219()
        var_1 = divide(ao218_1, ao219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class O2():
    # 'Synthetic_Natural_Gas'!O2
    value = 5.78889753697
    formula = "='EIA Consumption'!AP218/'EIA Consumption'!AP219"
    @eval_fn
    def O2():
        ap218_1 = EIA_Consumption.AP218()
        ap219_1 = EIA_Consumption.AP219()
        var_1 = divide(ap218_1, ap219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class P2():
    # 'Synthetic_Natural_Gas'!P2
    value = 5.76976267503
    formula = "='EIA Consumption'!AQ218/'EIA Consumption'!AQ219"
    @eval_fn
    def P2():
        aq218_1 = EIA_Consumption.AQ218()
        aq219_1 = EIA_Consumption.AQ219()
        var_1 = divide(aq218_1, aq219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Q2():
    # 'Synthetic_Natural_Gas'!Q2
    value = 5.79910241541
    formula = "='EIA Consumption'!AR218/'EIA Consumption'!AR219"
    @eval_fn
    def Q2():
        ar218_1 = EIA_Consumption.AR218()
        ar219_1 = EIA_Consumption.AR219()
        var_1 = divide(ar218_1, ar219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class R2():
    # 'Synthetic_Natural_Gas'!R2
    value = 5.79704860683
    formula = "='EIA Consumption'!AS218/'EIA Consumption'!AS219"
    @eval_fn
    def R2():
        as218_1 = EIA_Consumption.AS218()
        as219_1 = EIA_Consumption.AS219()
        var_1 = divide(as218_1, as219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class S2():
    # 'Synthetic_Natural_Gas'!S2
    value = 5.78475855252
    formula = "='EIA Consumption'!AT218/'EIA Consumption'!AT219"
    @eval_fn
    def S2():
        at218_1 = EIA_Consumption.AT218()
        at219_1 = EIA_Consumption.AT219()
        var_1 = divide(at218_1, at219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class T2():
    # 'Synthetic_Natural_Gas'!T2
    value = 5.75381935138
    formula = "='EIA Consumption'!AU218/'EIA Consumption'!AU219"
    @eval_fn
    def T2():
        au218_1 = EIA_Consumption.AU218()
        au219_1 = EIA_Consumption.AU219()
        var_1 = divide(au218_1, au219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class U2():
    # 'Synthetic_Natural_Gas'!U2
    value = 5.75271547769
    formula = "='EIA Consumption'!AV218/'EIA Consumption'!AV219"
    @eval_fn
    def U2():
        av218_1 = EIA_Consumption.AV218()
        av219_1 = EIA_Consumption.AV219()
        var_1 = divide(av218_1, av219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class V2():
    # 'Synthetic_Natural_Gas'!V2
    value = 5.76463399731
    formula = "='EIA Consumption'!AW218/'EIA Consumption'!AW219"
    @eval_fn
    def V2():
        aw218_1 = EIA_Consumption.AW218()
        aw219_1 = EIA_Consumption.AW219()
        var_1 = divide(aw218_1, aw219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class W2():
    # 'Synthetic_Natural_Gas'!W2
    value = 5.75955292878
    formula = "='EIA Consumption'!AX218/'EIA Consumption'!AX219"
    @eval_fn
    def W2():
        ax218_1 = EIA_Consumption.AX218()
        ax219_1 = EIA_Consumption.AX219()
        var_1 = divide(ax218_1, ax219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class X2():
    # 'Synthetic_Natural_Gas'!X2
    value = 5.76506865255
    formula = "='EIA Consumption'!AY218/'EIA Consumption'!AY219"
    @eval_fn
    def X2():
        ay218_1 = EIA_Consumption.AY218()
        ay219_1 = EIA_Consumption.AY219()
        var_1 = divide(ay218_1, ay219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Y2():
    # 'Synthetic_Natural_Gas'!Y2
    value = 5.79236367073
    formula = "='EIA Consumption'!AZ218/'EIA Consumption'!AZ219"
    @eval_fn
    def Y2():
        az218_1 = EIA_Consumption.AZ218()
        az219_1 = EIA_Consumption.AZ219()
        var_1 = divide(az218_1, az219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Z2():
    # 'Synthetic_Natural_Gas'!Z2
    value = 5.74665660306
    formula = "='EIA Consumption'!BA218/'EIA Consumption'!BA219"
    @eval_fn
    def Z2():
        ba218_1 = EIA_Consumption.BA218()
        ba219_1 = EIA_Consumption.BA219()
        var_1 = divide(ba218_1, ba219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AA2():
    # 'Synthetic_Natural_Gas'!AA2
    value = 5.74375
    formula = "='EIA Consumption'!BB218/'EIA Consumption'!BB219"
    @eval_fn
    def AA2():
        bb218_1 = EIA_Consumption.BB218()
        bb219_1 = EIA_Consumption.BB219()
        var_1 = divide(bb218_1, bb219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AB2():
    # 'Synthetic_Natural_Gas'!AB2
    value = 5.74805188634
    formula = "='EIA Consumption'!BC218/'EIA Consumption'!BC219"
    @eval_fn
    def AB2():
        bc218_1 = EIA_Consumption.BC218()
        bc219_1 = EIA_Consumption.BC219()
        var_1 = divide(bc218_1, bc219_1)
        return var_1

@register(Synthetic_Natural_Gas)
class B4():
    # 'Synthetic_Natural_Gas'!B4
    value = "unit"

@register(Synthetic_Natural_Gas)
class C4():
    # 'Synthetic_Natural_Gas'!C4
    value = "source"

@register(Synthetic_Natural_Gas)
class D4():
    # 'Synthetic_Natural_Gas'!D4
    value = 1960

@register(Synthetic_Natural_Gas)
class E4():
    # 'Synthetic_Natural_Gas'!E4
    value = 1961

@register(Synthetic_Natural_Gas)
class F4():
    # 'Synthetic_Natural_Gas'!F4
    value = 1962

@register(Synthetic_Natural_Gas)
class G4():
    # 'Synthetic_Natural_Gas'!G4
    value = 1963

@register(Synthetic_Natural_Gas)
class H4():
    # 'Synthetic_Natural_Gas'!H4
    value = 1964

@register(Synthetic_Natural_Gas)
class I4():
    # 'Synthetic_Natural_Gas'!I4
    value = 1965

@register(Synthetic_Natural_Gas)
class J4():
    # 'Synthetic_Natural_Gas'!J4
    value = 1966

@register(Synthetic_Natural_Gas)
class K4():
    # 'Synthetic_Natural_Gas'!K4
    value = 1967

@register(Synthetic_Natural_Gas)
class L4():
    # 'Synthetic_Natural_Gas'!L4
    value = 1968

@register(Synthetic_Natural_Gas)
class M4():
    # 'Synthetic_Natural_Gas'!M4
    value = 1969

@register(Synthetic_Natural_Gas)
class N4():
    # 'Synthetic_Natural_Gas'!N4
    value = 1970

@register(Synthetic_Natural_Gas)
class O4():
    # 'Synthetic_Natural_Gas'!O4
    value = 1971

@register(Synthetic_Natural_Gas)
class P4():
    # 'Synthetic_Natural_Gas'!P4
    value = 1972

@register(Synthetic_Natural_Gas)
class Q4():
    # 'Synthetic_Natural_Gas'!Q4
    value = 1973

@register(Synthetic_Natural_Gas)
class R4():
    # 'Synthetic_Natural_Gas'!R4
    value = 1974

@register(Synthetic_Natural_Gas)
class S4():
    # 'Synthetic_Natural_Gas'!S4
    value = 1975

@register(Synthetic_Natural_Gas)
class T4():
    # 'Synthetic_Natural_Gas'!T4
    value = 1976

@register(Synthetic_Natural_Gas)
class U4():
    # 'Synthetic_Natural_Gas'!U4
    value = 1977

@register(Synthetic_Natural_Gas)
class V4():
    # 'Synthetic_Natural_Gas'!V4
    value = 1978

@register(Synthetic_Natural_Gas)
class W4():
    # 'Synthetic_Natural_Gas'!W4
    value = 1979

@register(Synthetic_Natural_Gas)
class X4():
    # 'Synthetic_Natural_Gas'!X4
    value = 1980

@register(Synthetic_Natural_Gas)
class Y4():
    # 'Synthetic_Natural_Gas'!Y4
    value = 1981

@register(Synthetic_Natural_Gas)
class Z4():
    # 'Synthetic_Natural_Gas'!Z4
    value = 1982

@register(Synthetic_Natural_Gas)
class AA4():
    # 'Synthetic_Natural_Gas'!AA4
    value = 1983

@register(Synthetic_Natural_Gas)
class AB4():
    # 'Synthetic_Natural_Gas'!AB4
    value = 1984

@register(Synthetic_Natural_Gas)
class AC4():
    # 'Synthetic_Natural_Gas'!AC4
    value = 1985

@register(Synthetic_Natural_Gas)
class AD4():
    # 'Synthetic_Natural_Gas'!AD4
    value = 1986

@register(Synthetic_Natural_Gas)
class AE4():
    # 'Synthetic_Natural_Gas'!AE4
    value = 1987

@register(Synthetic_Natural_Gas)
class AF4():
    # 'Synthetic_Natural_Gas'!AF4
    value = 1988

@register(Synthetic_Natural_Gas)
class AG4():
    # 'Synthetic_Natural_Gas'!AG4
    value = 1989

@register(Synthetic_Natural_Gas)
class AH4():
    # 'Synthetic_Natural_Gas'!AH4
    value = 1990

@register(Synthetic_Natural_Gas)
class AI4():
    # 'Synthetic_Natural_Gas'!AI4
    value = 1991

@register(Synthetic_Natural_Gas)
class AJ4():
    # 'Synthetic_Natural_Gas'!AJ4
    value = 1992

@register(Synthetic_Natural_Gas)
class AK4():
    # 'Synthetic_Natural_Gas'!AK4
    value = 1993

@register(Synthetic_Natural_Gas)
class AL4():
    # 'Synthetic_Natural_Gas'!AL4
    value = 1994

@register(Synthetic_Natural_Gas)
class AM4():
    # 'Synthetic_Natural_Gas'!AM4
    value = 1995

@register(Synthetic_Natural_Gas)
class AN4():
    # 'Synthetic_Natural_Gas'!AN4
    value = 1996

@register(Synthetic_Natural_Gas)
class AO4():
    # 'Synthetic_Natural_Gas'!AO4
    value = 1997

@register(Synthetic_Natural_Gas)
class AP4():
    # 'Synthetic_Natural_Gas'!AP4
    value = 1998

@register(Synthetic_Natural_Gas)
class AQ4():
    # 'Synthetic_Natural_Gas'!AQ4
    value = 1999

@register(Synthetic_Natural_Gas)
class AR4():
    # 'Synthetic_Natural_Gas'!AR4
    value = 2000

@register(Synthetic_Natural_Gas)
class AS4():
    # 'Synthetic_Natural_Gas'!AS4
    value = 2001

@register(Synthetic_Natural_Gas)
class AT4():
    # 'Synthetic_Natural_Gas'!AT4
    value = 2002

@register(Synthetic_Natural_Gas)
class AU4():
    # 'Synthetic_Natural_Gas'!AU4
    value = 2003

@register(Synthetic_Natural_Gas)
class AV4():
    # 'Synthetic_Natural_Gas'!AV4
    value = 2004

@register(Synthetic_Natural_Gas)
class AW4():
    # 'Synthetic_Natural_Gas'!AW4
    value = 2005

@register(Synthetic_Natural_Gas)
class AX4():
    # 'Synthetic_Natural_Gas'!AX4
    value = 2006

@register(Synthetic_Natural_Gas)
class AY4():
    # 'Synthetic_Natural_Gas'!AY4
    value = 2007

@register(Synthetic_Natural_Gas)
class AZ4():
    # 'Synthetic_Natural_Gas'!AZ4
    value = 2008

@register(Synthetic_Natural_Gas)
class BA4():
    # 'Synthetic_Natural_Gas'!BA4
    value = 2009

@register(Synthetic_Natural_Gas)
class BB4():
    # 'Synthetic_Natural_Gas'!BB4
    value = 2010

@register(Synthetic_Natural_Gas)
class BC4():
    # 'Synthetic_Natural_Gas'!BC4
    value = 2011

@register(Synthetic_Natural_Gas)
class BD4():
    # 'Synthetic_Natural_Gas'!BD4
    value = 2012

@register(Synthetic_Natural_Gas)
class BE4():
    # 'Synthetic_Natural_Gas'!BE4
    value = 2013

@register(Synthetic_Natural_Gas)
class BF4():
    # 'Synthetic_Natural_Gas'!BF4
    value = 2014

@register(Synthetic_Natural_Gas)
class BG4():
    # 'Synthetic_Natural_Gas'!BG4
    value = 2015

@register(Synthetic_Natural_Gas)
class BH4():
    # 'Synthetic_Natural_Gas'!BH4
    value = 2016

@register(Synthetic_Natural_Gas)
class BI4():
    # 'Synthetic_Natural_Gas'!BI4
    value = 2017

@register(Synthetic_Natural_Gas)
class BJ4():
    # 'Synthetic_Natural_Gas'!BJ4
    value = 2018

@register(Synthetic_Natural_Gas)
class BK4():
    # 'Synthetic_Natural_Gas'!BK4
    value = 2019

@register(Synthetic_Natural_Gas)
class BL4():
    # 'Synthetic_Natural_Gas'!BL4
    value = 2020

@register(Synthetic_Natural_Gas)
class A5():
    # 'Synthetic_Natural_Gas'!A5
    value = "Total Synthetic Natural Gas Consumption (MMBtu)"

@register(Synthetic_Natural_Gas)
class A6():
    # 'Synthetic_Natural_Gas'!A6
    value = "Total Synthetic Natural Gas Consumption (MMBtu)"

@register(Synthetic_Natural_Gas)
class B6():
    # 'Synthetic_Natural_Gas'!B6
    value = "MMBtu"

@register(Synthetic_Natural_Gas)
class D6():
    # 'Synthetic_Natural_Gas'!D6
    value = 0
    formula = "='EIA Consumption'!E186*1000"
    @eval_fn
    def D6():
        e186_1 = EIA_Consumption.E186()
        var_1 = mult(e186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class E6():
    # 'Synthetic_Natural_Gas'!E6
    value = 0
    formula = "='EIA Consumption'!F186*1000"
    @eval_fn
    def E6():
        f186_1 = EIA_Consumption.F186()
        var_1 = mult(f186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class F6():
    # 'Synthetic_Natural_Gas'!F6
    value = 0
    formula = "='EIA Consumption'!G186*1000"
    @eval_fn
    def F6():
        g186_1 = EIA_Consumption.G186()
        var_1 = mult(g186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class G6():
    # 'Synthetic_Natural_Gas'!G6
    value = 0
    formula = "='EIA Consumption'!H186*1000"
    @eval_fn
    def G6():
        h186_1 = EIA_Consumption.H186()
        var_1 = mult(h186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class H6():
    # 'Synthetic_Natural_Gas'!H6
    value = 0
    formula = "='EIA Consumption'!I186*1000"
    @eval_fn
    def H6():
        i186_1 = EIA_Consumption.I186()
        var_1 = mult(i186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class I6():
    # 'Synthetic_Natural_Gas'!I6
    value = 0
    formula = "='EIA Consumption'!J186*1000"
    @eval_fn
    def I6():
        j186_1 = EIA_Consumption.J186()
        var_1 = mult(j186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class J6():
    # 'Synthetic_Natural_Gas'!J6
    value = 0
    formula = "='EIA Consumption'!K186*1000"
    @eval_fn
    def J6():
        k186_1 = EIA_Consumption.K186()
        var_1 = mult(k186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class K6():
    # 'Synthetic_Natural_Gas'!K6
    value = 0
    formula = "='EIA Consumption'!L186*1000"
    @eval_fn
    def K6():
        l186_1 = EIA_Consumption.L186()
        var_1 = mult(l186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class L6():
    # 'Synthetic_Natural_Gas'!L6
    value = 0
    formula = "='EIA Consumption'!M186*1000"
    @eval_fn
    def L6():
        m186_1 = EIA_Consumption.M186()
        var_1 = mult(m186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class M6():
    # 'Synthetic_Natural_Gas'!M6
    value = 0
    formula = "='EIA Consumption'!N186*1000"
    @eval_fn
    def M6():
        n186_1 = EIA_Consumption.N186()
        var_1 = mult(n186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class N6():
    # 'Synthetic_Natural_Gas'!N6
    value = 0
    formula = "='EIA Consumption'!O186*1000"
    @eval_fn
    def N6():
        o186_1 = EIA_Consumption.O186()
        var_1 = mult(o186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class O6():
    # 'Synthetic_Natural_Gas'!O6
    value = 0
    formula = "='EIA Consumption'!P186*1000"
    @eval_fn
    def O6():
        p186_1 = EIA_Consumption.P186()
        var_1 = mult(p186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class P6():
    # 'Synthetic_Natural_Gas'!P6
    value = 0
    formula = "='EIA Consumption'!Q186*1000"
    @eval_fn
    def P6():
        q186_1 = EIA_Consumption.Q186()
        var_1 = mult(q186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class Q6():
    # 'Synthetic_Natural_Gas'!Q6
    value = 0
    formula = "='EIA Consumption'!R186*1000"
    @eval_fn
    def Q6():
        r186_1 = EIA_Consumption.R186()
        var_1 = mult(r186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class R6():
    # 'Synthetic_Natural_Gas'!R6
    value = 0
    formula = "='EIA Consumption'!S186*1000"
    @eval_fn
    def R6():
        s186_1 = EIA_Consumption.S186()
        var_1 = mult(s186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class S6():
    # 'Synthetic_Natural_Gas'!S6
    value = 0
    formula = "='EIA Consumption'!T186*1000"
    @eval_fn
    def S6():
        t186_1 = EIA_Consumption.T186()
        var_1 = mult(t186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class T6():
    # 'Synthetic_Natural_Gas'!T6
    value = 0
    formula = "='EIA Consumption'!U186*1000"
    @eval_fn
    def T6():
        u186_1 = EIA_Consumption.U186()
        var_1 = mult(u186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class U6():
    # 'Synthetic_Natural_Gas'!U6
    value = 0
    formula = "='EIA Consumption'!V186*1000"
    @eval_fn
    def U6():
        v186_1 = EIA_Consumption.V186()
        var_1 = mult(v186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class V6():
    # 'Synthetic_Natural_Gas'!V6
    value = 0
    formula = "='EIA Consumption'!W186*1000"
    @eval_fn
    def V6():
        w186_1 = EIA_Consumption.W186()
        var_1 = mult(w186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class W6():
    # 'Synthetic_Natural_Gas'!W6
    value = 0
    formula = "='EIA Consumption'!X186*1000"
    @eval_fn
    def W6():
        x186_1 = EIA_Consumption.X186()
        var_1 = mult(x186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class X6():
    # 'Synthetic_Natural_Gas'!X6
    value = 3015000
    formula = "='EIA Consumption'!Y186*1000"
    @eval_fn
    def X6():
        y186_1 = EIA_Consumption.Y186()
        var_1 = mult(y186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class Y6():
    # 'Synthetic_Natural_Gas'!Y6
    value = 2780000
    formula = "='EIA Consumption'!Z186*1000"
    @eval_fn
    def Y6():
        z186_1 = EIA_Consumption.Z186()
        var_1 = mult(z186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class Z6():
    # 'Synthetic_Natural_Gas'!Z6
    value = 2773000
    formula = "='EIA Consumption'!AA186*1000"
    @eval_fn
    def Z6():
        aa186_1 = EIA_Consumption.AA186()
        var_1 = mult(aa186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AA6():
    # 'Synthetic_Natural_Gas'!AA6
    value = 2730000
    formula = "='EIA Consumption'!AB186*1000"
    @eval_fn
    def AA6():
        ab186_1 = EIA_Consumption.AB186()
        var_1 = mult(ab186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AB6():
    # 'Synthetic_Natural_Gas'!AB6
    value = 2438000
    formula = "='EIA Consumption'!AC186*1000"
    @eval_fn
    def AB6():
        ac186_1 = EIA_Consumption.AC186()
        var_1 = mult(ac186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AC6():
    # 'Synthetic_Natural_Gas'!AC6
    value = 2687000
    formula = "='EIA Consumption'!AD186*1000"
    @eval_fn
    def AC6():
        ad186_1 = EIA_Consumption.AD186()
        var_1 = mult(ad186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AD6():
    # 'Synthetic_Natural_Gas'!AD6
    value = 2674000
    formula = "='EIA Consumption'!AE186*1000"
    @eval_fn
    def AD6():
        ae186_1 = EIA_Consumption.AE186()
        var_1 = mult(ae186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AE6():
    # 'Synthetic_Natural_Gas'!AE6
    value = 2787000
    formula = "='EIA Consumption'!AF186*1000"
    @eval_fn
    def AE6():
        af186_1 = EIA_Consumption.AF186()
        var_1 = mult(af186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AF6():
    # 'Synthetic_Natural_Gas'!AF6
    value = 2816000
    formula = "='EIA Consumption'!AG186*1000"
    @eval_fn
    def AF6():
        ag186_1 = EIA_Consumption.AG186()
        var_1 = mult(ag186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AG6():
    # 'Synthetic_Natural_Gas'!AG6
    value = 2909000
    formula = "='EIA Consumption'!AH186*1000"
    @eval_fn
    def AG6():
        ah186_1 = EIA_Consumption.AH186()
        var_1 = mult(ah186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AH6():
    # 'Synthetic_Natural_Gas'!AH6
    value = 2983000
    formula = "='EIA Consumption'!AI186*1000"
    @eval_fn
    def AH6():
        ai186_1 = EIA_Consumption.AI186()
        var_1 = mult(ai186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AI6():
    # 'Synthetic_Natural_Gas'!AI6
    value = 2909000
    formula = "='EIA Consumption'!AJ186*1000"
    @eval_fn
    def AI6():
        aj186_1 = EIA_Consumption.AJ186()
        var_1 = mult(aj186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AJ6():
    # 'Synthetic_Natural_Gas'!AJ6
    value = 2892000
    formula = "='EIA Consumption'!AK186*1000"
    @eval_fn
    def AJ6():
        ak186_1 = EIA_Consumption.AK186()
        var_1 = mult(ak186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AK6():
    # 'Synthetic_Natural_Gas'!AK6
    value = 2847000
    formula = "='EIA Consumption'!AL186*1000"
    @eval_fn
    def AK6():
        al186_1 = EIA_Consumption.AL186()
        var_1 = mult(al186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AL6():
    # 'Synthetic_Natural_Gas'!AL6
    value = 2920000
    formula = "='EIA Consumption'!AM186*1000"
    @eval_fn
    def AL6():
        am186_1 = EIA_Consumption.AM186()
        var_1 = mult(am186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AM6():
    # 'Synthetic_Natural_Gas'!AM6
    value = 2906000
    formula = "='EIA Consumption'!AN186*1000"
    @eval_fn
    def AM6():
        an186_1 = EIA_Consumption.AN186()
        var_1 = mult(an186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AN6():
    # 'Synthetic_Natural_Gas'!AN6
    value = 2825000
    formula = "='EIA Consumption'!AO186*1000"
    @eval_fn
    def AN6():
        ao186_1 = EIA_Consumption.AO186()
        var_1 = mult(ao186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AO6():
    # 'Synthetic_Natural_Gas'!AO6
    value = 2689000
    formula = "='EIA Consumption'!AP186*1000"
    @eval_fn
    def AO6():
        ap186_1 = EIA_Consumption.AP186()
        var_1 = mult(ap186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AP6():
    # 'Synthetic_Natural_Gas'!AP6
    value = 2803000
    formula = "='EIA Consumption'!AQ186*1000"
    @eval_fn
    def AP6():
        aq186_1 = EIA_Consumption.AQ186()
        var_1 = mult(aq186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AQ6():
    # 'Synthetic_Natural_Gas'!AQ6
    value = 2886000
    formula = "='EIA Consumption'!AR186*1000"
    @eval_fn
    def AQ6():
        ar186_1 = EIA_Consumption.AR186()
        var_1 = mult(ar186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AR6():
    # 'Synthetic_Natural_Gas'!AR6
    value = 2975000
    formula = "='EIA Consumption'!AS186*1000"
    @eval_fn
    def AR6():
        as186_1 = EIA_Consumption.AS186()
        var_1 = mult(as186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AS6():
    # 'Synthetic_Natural_Gas'!AS6
    value = 2920000
    formula = "='EIA Consumption'!AT186*1000"
    @eval_fn
    def AS6():
        at186_1 = EIA_Consumption.AT186()
        var_1 = mult(at186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AT6():
    # 'Synthetic_Natural_Gas'!AT6
    value = 2898000
    formula = "='EIA Consumption'!AU186*1000"
    @eval_fn
    def AT6():
        au186_1 = EIA_Consumption.AU186()
        var_1 = mult(au186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AU6():
    # 'Synthetic_Natural_Gas'!AU6
    value = 2861000
    formula = "='EIA Consumption'!AV186*1000"
    @eval_fn
    def AU6():
        av186_1 = EIA_Consumption.AV186()
        var_1 = mult(av186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AV6():
    # 'Synthetic_Natural_Gas'!AV6
    value = 2907000
    formula = "='EIA Consumption'!AW186*1000"
    @eval_fn
    def AV6():
        aw186_1 = EIA_Consumption.AW186()
        var_1 = mult(aw186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AW6():
    # 'Synthetic_Natural_Gas'!AW6
    value = 2898000
    formula = "='EIA Consumption'!AX186*1000"
    @eval_fn
    def AW6():
        ax186_1 = EIA_Consumption.AX186()
        var_1 = mult(ax186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AX6():
    # 'Synthetic_Natural_Gas'!AX6
    value = 2914000
    formula = "='EIA Consumption'!AY186*1000"
    @eval_fn
    def AX6():
        ay186_1 = EIA_Consumption.AY186()
        var_1 = mult(ay186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AY6():
    # 'Synthetic_Natural_Gas'!AY6
    value = 2956000
    formula = "='EIA Consumption'!AZ186*1000"
    @eval_fn
    def AY6():
        az186_1 = EIA_Consumption.AZ186()
        var_1 = mult(az186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class AZ6():
    # 'Synthetic_Natural_Gas'!AZ6
    value = 2817000
    formula = "='EIA Consumption'!BA186*1000"
    @eval_fn
    def AZ6():
        ba186_1 = EIA_Consumption.BA186()
        var_1 = mult(ba186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BA6():
    # 'Synthetic_Natural_Gas'!BA6
    value = 2712000
    formula = "='EIA Consumption'!BB186*1000"
    @eval_fn
    def BA6():
        bb186_1 = EIA_Consumption.BB186()
        var_1 = mult(bb186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BB6():
    # 'Synthetic_Natural_Gas'!BB6
    value = 2732000
    formula = "='EIA Consumption'!BC186*1000"
    @eval_fn
    def BB6():
        bc186_1 = EIA_Consumption.BC186()
        var_1 = mult(bc186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BC6():
    # 'Synthetic_Natural_Gas'!BC6
    value = 2744000
    formula = "='EIA Consumption'!BD186*1000"
    @eval_fn
    def BC6():
        bd186_1 = EIA_Consumption.BD186()
        var_1 = mult(bd186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BD6():
    # 'Synthetic_Natural_Gas'!BD6
    value = 2813000
    formula = "='EIA Consumption'!BE186*1000"
    @eval_fn
    def BD6():
        be186_1 = EIA_Consumption.BE186()
        var_1 = mult(be186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BE6():
    # 'Synthetic_Natural_Gas'!BE6
    value = 2861000
    formula = "='EIA Consumption'!BF186*1000"
    @eval_fn
    def BE6():
        bf186_1 = EIA_Consumption.BF186()
        var_1 = mult(bf186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BF6():
    # 'Synthetic_Natural_Gas'!BF6
    value = "#N/A"
    formula = "='EIA Consumption'!BG186*1000"
    @eval_fn
    def BF6():
        bg186_1 = EIA_Consumption.BG186()
        var_1 = mult(bg186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BG6():
    # 'Synthetic_Natural_Gas'!BG6
    value = "#N/A"
    formula = "='EIA Consumption'!BH186*1000"
    @eval_fn
    def BG6():
        bh186_1 = EIA_Consumption.BH186()
        var_1 = mult(bh186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BH6():
    # 'Synthetic_Natural_Gas'!BH6
    value = "#N/A"
    formula = "='EIA Consumption'!BI186*1000"
    @eval_fn
    def BH6():
        bi186_1 = EIA_Consumption.BI186()
        var_1 = mult(bi186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BI6():
    # 'Synthetic_Natural_Gas'!BI6
    value = "#N/A"
    formula = "='EIA Consumption'!BJ186*1000"
    @eval_fn
    def BI6():
        bj186_1 = EIA_Consumption.BJ186()
        var_1 = mult(bj186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BJ6():
    # 'Synthetic_Natural_Gas'!BJ6
    value = "#N/A"
    formula = "='EIA Consumption'!BK186*1000"
    @eval_fn
    def BJ6():
        bk186_1 = EIA_Consumption.BK186()
        var_1 = mult(bk186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BK6():
    # 'Synthetic_Natural_Gas'!BK6
    value = "#N/A"
    formula = "='EIA Consumption'!BL186*1000"
    @eval_fn
    def BK6():
        bl186_1 = EIA_Consumption.BL186()
        var_1 = mult(bl186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class BL6():
    # 'Synthetic_Natural_Gas'!BL6
    value = "#N/A"
    formula = "='EIA Consumption'!BM186*1000"
    @eval_fn
    def BL6():
        bm186_1 = EIA_Consumption.BM186()
        var_1 = mult(bm186_1, 1000)
        return var_1

@register(Synthetic_Natural_Gas)
class A8():
    # 'Synthetic_Natural_Gas'!A8
    value = "Standard coefficient Emissions (kgCO2)"

@register(Synthetic_Natural_Gas)
class C8():
    # 'Synthetic_Natural_Gas'!C8
    value = " (Gate-to-Tank) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A9():
    # 'Synthetic_Natural_Gas'!A9
    value = "US"

@register(Synthetic_Natural_Gas)
class B9():
    # 'Synthetic_Natural_Gas'!B9
    value = "kgCO2/MMBTU"

@register(Synthetic_Natural_Gas)
class D9():
    # 'Synthetic_Natural_Gas'!D9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def D9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class E9():
    # 'Synthetic_Natural_Gas'!E9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def E9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class F9():
    # 'Synthetic_Natural_Gas'!F9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def F9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class G9():
    # 'Synthetic_Natural_Gas'!G9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def G9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class H9():
    # 'Synthetic_Natural_Gas'!H9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def H9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class I9():
    # 'Synthetic_Natural_Gas'!I9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def I9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class J9():
    # 'Synthetic_Natural_Gas'!J9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def J9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class K9():
    # 'Synthetic_Natural_Gas'!K9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def K9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class L9():
    # 'Synthetic_Natural_Gas'!L9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def L9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class M9():
    # 'Synthetic_Natural_Gas'!M9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def M9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class N9():
    # 'Synthetic_Natural_Gas'!N9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def N9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class O9():
    # 'Synthetic_Natural_Gas'!O9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def O9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class P9():
    # 'Synthetic_Natural_Gas'!P9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def P9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class Q9():
    # 'Synthetic_Natural_Gas'!Q9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def Q9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class R9():
    # 'Synthetic_Natural_Gas'!R9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def R9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class S9():
    # 'Synthetic_Natural_Gas'!S9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def S9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class T9():
    # 'Synthetic_Natural_Gas'!T9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def T9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class U9():
    # 'Synthetic_Natural_Gas'!U9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def U9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class V9():
    # 'Synthetic_Natural_Gas'!V9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def V9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class W9():
    # 'Synthetic_Natural_Gas'!W9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def W9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class X9():
    # 'Synthetic_Natural_Gas'!X9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def X9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class Y9():
    # 'Synthetic_Natural_Gas'!Y9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def Y9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class Z9():
    # 'Synthetic_Natural_Gas'!Z9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def Z9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AA9():
    # 'Synthetic_Natural_Gas'!AA9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AA9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AB9():
    # 'Synthetic_Natural_Gas'!AB9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AB9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AC9():
    # 'Synthetic_Natural_Gas'!AC9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AC9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AD9():
    # 'Synthetic_Natural_Gas'!AD9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AD9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AE9():
    # 'Synthetic_Natural_Gas'!AE9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AE9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AF9():
    # 'Synthetic_Natural_Gas'!AF9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AF9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AG9():
    # 'Synthetic_Natural_Gas'!AG9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AG9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AH9():
    # 'Synthetic_Natural_Gas'!AH9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AH9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AI9():
    # 'Synthetic_Natural_Gas'!AI9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AI9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AJ9():
    # 'Synthetic_Natural_Gas'!AJ9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AJ9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AK9():
    # 'Synthetic_Natural_Gas'!AK9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AK9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AL9():
    # 'Synthetic_Natural_Gas'!AL9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AL9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AM9():
    # 'Synthetic_Natural_Gas'!AM9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AM9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AN9():
    # 'Synthetic_Natural_Gas'!AN9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AN9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AO9():
    # 'Synthetic_Natural_Gas'!AO9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AO9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AP9():
    # 'Synthetic_Natural_Gas'!AP9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AP9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AQ9():
    # 'Synthetic_Natural_Gas'!AQ9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AQ9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AR9():
    # 'Synthetic_Natural_Gas'!AR9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AR9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AS9():
    # 'Synthetic_Natural_Gas'!AS9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AS9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AT9():
    # 'Synthetic_Natural_Gas'!AT9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AT9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AU9():
    # 'Synthetic_Natural_Gas'!AU9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AU9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AV9():
    # 'Synthetic_Natural_Gas'!AV9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AV9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AW9():
    # 'Synthetic_Natural_Gas'!AW9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AW9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AX9():
    # 'Synthetic_Natural_Gas'!AX9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AX9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AY9():
    # 'Synthetic_Natural_Gas'!AY9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AY9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class AZ9():
    # 'Synthetic_Natural_Gas'!AZ9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def AZ9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BA9():
    # 'Synthetic_Natural_Gas'!BA9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BA9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BB9():
    # 'Synthetic_Natural_Gas'!BB9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BB9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BC9():
    # 'Synthetic_Natural_Gas'!BC9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BC9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BD9():
    # 'Synthetic_Natural_Gas'!BD9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BD9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BE9():
    # 'Synthetic_Natural_Gas'!BE9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BE9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BF9():
    # 'Synthetic_Natural_Gas'!BF9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BF9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BG9():
    # 'Synthetic_Natural_Gas'!BG9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BG9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BH9():
    # 'Synthetic_Natural_Gas'!BH9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BH9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BI9():
    # 'Synthetic_Natural_Gas'!BI9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BI9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BJ9():
    # 'Synthetic_Natural_Gas'!BJ9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BJ9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BK9():
    # 'Synthetic_Natural_Gas'!BK9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BK9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class BL9():
    # 'Synthetic_Natural_Gas'!BL9
    value = 53.06
    formula = "='Carbon Coefficients'!$D$7"
    @eval_fn
    def BL9():
        d7_1 = Carbon_Coefficients.D7()
        return d7_1

@register(Synthetic_Natural_Gas)
class A11():
    # 'Synthetic_Natural_Gas'!A11
    value = "Upstream coefficient emissions"

@register(Synthetic_Natural_Gas)
class C11():
    # 'Synthetic_Natural_Gas'!C11
    value = "(Well-to-Gate) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A12():
    # 'Synthetic_Natural_Gas'!A12
    value = "US"

@register(Synthetic_Natural_Gas)
class B12():
    # 'Synthetic_Natural_Gas'!B12
    value = "kgCO2/MMBTU"

@register(Synthetic_Natural_Gas)
class D12():
    # 'Synthetic_Natural_Gas'!D12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def D12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class E12():
    # 'Synthetic_Natural_Gas'!E12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def E12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class F12():
    # 'Synthetic_Natural_Gas'!F12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def F12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class G12():
    # 'Synthetic_Natural_Gas'!G12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def G12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class H12():
    # 'Synthetic_Natural_Gas'!H12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def H12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class I12():
    # 'Synthetic_Natural_Gas'!I12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def I12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class J12():
    # 'Synthetic_Natural_Gas'!J12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def J12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class K12():
    # 'Synthetic_Natural_Gas'!K12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def K12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class L12():
    # 'Synthetic_Natural_Gas'!L12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def L12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class M12():
    # 'Synthetic_Natural_Gas'!M12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def M12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class N12():
    # 'Synthetic_Natural_Gas'!N12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def N12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class O12():
    # 'Synthetic_Natural_Gas'!O12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def O12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class P12():
    # 'Synthetic_Natural_Gas'!P12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def P12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class Q12():
    # 'Synthetic_Natural_Gas'!Q12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def Q12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class R12():
    # 'Synthetic_Natural_Gas'!R12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def R12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class S12():
    # 'Synthetic_Natural_Gas'!S12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def S12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class T12():
    # 'Synthetic_Natural_Gas'!T12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def T12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class U12():
    # 'Synthetic_Natural_Gas'!U12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def U12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class V12():
    # 'Synthetic_Natural_Gas'!V12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def V12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class W12():
    # 'Synthetic_Natural_Gas'!W12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def W12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class X12():
    # 'Synthetic_Natural_Gas'!X12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def X12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class Y12():
    # 'Synthetic_Natural_Gas'!Y12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def Y12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class Z12():
    # 'Synthetic_Natural_Gas'!Z12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def Z12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AA12():
    # 'Synthetic_Natural_Gas'!AA12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AA12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AB12():
    # 'Synthetic_Natural_Gas'!AB12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AB12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AC12():
    # 'Synthetic_Natural_Gas'!AC12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AC12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AD12():
    # 'Synthetic_Natural_Gas'!AD12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AD12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AE12():
    # 'Synthetic_Natural_Gas'!AE12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AE12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AF12():
    # 'Synthetic_Natural_Gas'!AF12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AF12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AG12():
    # 'Synthetic_Natural_Gas'!AG12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AG12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AH12():
    # 'Synthetic_Natural_Gas'!AH12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AH12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AI12():
    # 'Synthetic_Natural_Gas'!AI12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AI12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AJ12():
    # 'Synthetic_Natural_Gas'!AJ12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AJ12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AK12():
    # 'Synthetic_Natural_Gas'!AK12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AK12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AL12():
    # 'Synthetic_Natural_Gas'!AL12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AL12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AM12():
    # 'Synthetic_Natural_Gas'!AM12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AM12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AN12():
    # 'Synthetic_Natural_Gas'!AN12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AN12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AO12():
    # 'Synthetic_Natural_Gas'!AO12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AO12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AP12():
    # 'Synthetic_Natural_Gas'!AP12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AP12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AQ12():
    # 'Synthetic_Natural_Gas'!AQ12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AQ12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AR12():
    # 'Synthetic_Natural_Gas'!AR12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AR12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AS12():
    # 'Synthetic_Natural_Gas'!AS12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AS12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AT12():
    # 'Synthetic_Natural_Gas'!AT12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AT12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AU12():
    # 'Synthetic_Natural_Gas'!AU12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AU12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AV12():
    # 'Synthetic_Natural_Gas'!AV12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AV12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AW12():
    # 'Synthetic_Natural_Gas'!AW12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AW12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AX12():
    # 'Synthetic_Natural_Gas'!AX12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AX12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AY12():
    # 'Synthetic_Natural_Gas'!AY12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AY12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class AZ12():
    # 'Synthetic_Natural_Gas'!AZ12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def AZ12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BA12():
    # 'Synthetic_Natural_Gas'!BA12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BA12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BB12():
    # 'Synthetic_Natural_Gas'!BB12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BB12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BC12():
    # 'Synthetic_Natural_Gas'!BC12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BC12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BD12():
    # 'Synthetic_Natural_Gas'!BD12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BD12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BE12():
    # 'Synthetic_Natural_Gas'!BE12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BE12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BF12():
    # 'Synthetic_Natural_Gas'!BF12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BF12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BG12():
    # 'Synthetic_Natural_Gas'!BG12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BG12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BH12():
    # 'Synthetic_Natural_Gas'!BH12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BH12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BI12():
    # 'Synthetic_Natural_Gas'!BI12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BI12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BJ12():
    # 'Synthetic_Natural_Gas'!BJ12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BJ12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BK12():
    # 'Synthetic_Natural_Gas'!BK12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BK12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class BL12():
    # 'Synthetic_Natural_Gas'!BL12
    value = 39.9
    formula = "='Carbon Coefficients'!$D$8"
    @eval_fn
    def BL12():
        d8_1 = Carbon_Coefficients.D8()
        return d8_1

@register(Synthetic_Natural_Gas)
class A14():
    # 'Synthetic_Natural_Gas'!A14
    value = "Combined Coeffiecient "

@register(Synthetic_Natural_Gas)
class C14():
    # 'Synthetic_Natural_Gas'!C14
    value = "Total WTT (Well-to-Tank) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A15():
    # 'Synthetic_Natural_Gas'!A15
    value = "US"

@register(Synthetic_Natural_Gas)
class B15():
    # 'Synthetic_Natural_Gas'!B15
    value = "kgCO2/MMBTU"

@register(Synthetic_Natural_Gas)
class D15():
    # 'Synthetic_Natural_Gas'!D15
    value = 92.96
    formula = "=D12+D9"
    @eval_fn
    def D15():
        d12_1 = Synthetic_Natural_Gas.D12()
        d9_1 = Synthetic_Natural_Gas.D9()
        var_1 = add(d12_1, d9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class E15():
    # 'Synthetic_Natural_Gas'!E15
    value = 92.96
    formula = "=E12+E9"
    @eval_fn
    def E15():
        e12_1 = Synthetic_Natural_Gas.E12()
        e9_1 = Synthetic_Natural_Gas.E9()
        var_1 = add(e12_1, e9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class F15():
    # 'Synthetic_Natural_Gas'!F15
    value = 92.96
    formula = "=F12+F9"
    @eval_fn
    def F15():
        f12_1 = Synthetic_Natural_Gas.F12()
        f9_1 = Synthetic_Natural_Gas.F9()
        var_1 = add(f12_1, f9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class G15():
    # 'Synthetic_Natural_Gas'!G15
    value = 92.96
    formula = "=G12+G9"
    @eval_fn
    def G15():
        g12_1 = Synthetic_Natural_Gas.G12()
        g9_1 = Synthetic_Natural_Gas.G9()
        var_1 = add(g12_1, g9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class H15():
    # 'Synthetic_Natural_Gas'!H15
    value = 92.96
    formula = "=H12+H9"
    @eval_fn
    def H15():
        h12_1 = Synthetic_Natural_Gas.H12()
        h9_1 = Synthetic_Natural_Gas.H9()
        var_1 = add(h12_1, h9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class I15():
    # 'Synthetic_Natural_Gas'!I15
    value = 92.96
    formula = "=I12+I9"
    @eval_fn
    def I15():
        i12_1 = Synthetic_Natural_Gas.I12()
        i9_1 = Synthetic_Natural_Gas.I9()
        var_1 = add(i12_1, i9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class J15():
    # 'Synthetic_Natural_Gas'!J15
    value = 92.96
    formula = "=J12+J9"
    @eval_fn
    def J15():
        j12_1 = Synthetic_Natural_Gas.J12()
        j9_1 = Synthetic_Natural_Gas.J9()
        var_1 = add(j12_1, j9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class K15():
    # 'Synthetic_Natural_Gas'!K15
    value = 92.96
    formula = "=K12+K9"
    @eval_fn
    def K15():
        k12_1 = Synthetic_Natural_Gas.K12()
        k9_1 = Synthetic_Natural_Gas.K9()
        var_1 = add(k12_1, k9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class L15():
    # 'Synthetic_Natural_Gas'!L15
    value = 92.96
    formula = "=L12+L9"
    @eval_fn
    def L15():
        l12_1 = Synthetic_Natural_Gas.L12()
        l9_1 = Synthetic_Natural_Gas.L9()
        var_1 = add(l12_1, l9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class M15():
    # 'Synthetic_Natural_Gas'!M15
    value = 92.96
    formula = "=M12+M9"
    @eval_fn
    def M15():
        m12_1 = Synthetic_Natural_Gas.M12()
        m9_1 = Synthetic_Natural_Gas.M9()
        var_1 = add(m12_1, m9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class N15():
    # 'Synthetic_Natural_Gas'!N15
    value = 92.96
    formula = "=N12+N9"
    @eval_fn
    def N15():
        n12_1 = Synthetic_Natural_Gas.N12()
        n9_1 = Synthetic_Natural_Gas.N9()
        var_1 = add(n12_1, n9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class O15():
    # 'Synthetic_Natural_Gas'!O15
    value = 92.96
    formula = "=O12+O9"
    @eval_fn
    def O15():
        o12_1 = Synthetic_Natural_Gas.O12()
        o9_1 = Synthetic_Natural_Gas.O9()
        var_1 = add(o12_1, o9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class P15():
    # 'Synthetic_Natural_Gas'!P15
    value = 92.96
    formula = "=P12+P9"
    @eval_fn
    def P15():
        p12_1 = Synthetic_Natural_Gas.P12()
        p9_1 = Synthetic_Natural_Gas.P9()
        var_1 = add(p12_1, p9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Q15():
    # 'Synthetic_Natural_Gas'!Q15
    value = 92.96
    formula = "=Q12+Q9"
    @eval_fn
    def Q15():
        q12_1 = Synthetic_Natural_Gas.Q12()
        q9_1 = Synthetic_Natural_Gas.Q9()
        var_1 = add(q12_1, q9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class R15():
    # 'Synthetic_Natural_Gas'!R15
    value = 92.96
    formula = "=R12+R9"
    @eval_fn
    def R15():
        r12_1 = Synthetic_Natural_Gas.R12()
        r9_1 = Synthetic_Natural_Gas.R9()
        var_1 = add(r12_1, r9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class S15():
    # 'Synthetic_Natural_Gas'!S15
    value = 92.96
    formula = "=S12+S9"
    @eval_fn
    def S15():
        s12_1 = Synthetic_Natural_Gas.S12()
        s9_1 = Synthetic_Natural_Gas.S9()
        var_1 = add(s12_1, s9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class T15():
    # 'Synthetic_Natural_Gas'!T15
    value = 92.96
    formula = "=T12+T9"
    @eval_fn
    def T15():
        t12_1 = Synthetic_Natural_Gas.T12()
        t9_1 = Synthetic_Natural_Gas.T9()
        var_1 = add(t12_1, t9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class U15():
    # 'Synthetic_Natural_Gas'!U15
    value = 92.96
    formula = "=U12+U9"
    @eval_fn
    def U15():
        u12_1 = Synthetic_Natural_Gas.U12()
        u9_1 = Synthetic_Natural_Gas.U9()
        var_1 = add(u12_1, u9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class V15():
    # 'Synthetic_Natural_Gas'!V15
    value = 92.96
    formula = "=V12+V9"
    @eval_fn
    def V15():
        v12_1 = Synthetic_Natural_Gas.V12()
        v9_1 = Synthetic_Natural_Gas.V9()
        var_1 = add(v12_1, v9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class W15():
    # 'Synthetic_Natural_Gas'!W15
    value = 92.96
    formula = "=W12+W9"
    @eval_fn
    def W15():
        w12_1 = Synthetic_Natural_Gas.W12()
        w9_1 = Synthetic_Natural_Gas.W9()
        var_1 = add(w12_1, w9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class X15():
    # 'Synthetic_Natural_Gas'!X15
    value = 92.96
    formula = "=X12+X9"
    @eval_fn
    def X15():
        x12_1 = Synthetic_Natural_Gas.X12()
        x9_1 = Synthetic_Natural_Gas.X9()
        var_1 = add(x12_1, x9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Y15():
    # 'Synthetic_Natural_Gas'!Y15
    value = 92.96
    formula = "=Y12+Y9"
    @eval_fn
    def Y15():
        y12_1 = Synthetic_Natural_Gas.Y12()
        y9_1 = Synthetic_Natural_Gas.Y9()
        var_1 = add(y12_1, y9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Z15():
    # 'Synthetic_Natural_Gas'!Z15
    value = 92.96
    formula = "=Z12+Z9"
    @eval_fn
    def Z15():
        z12_1 = Synthetic_Natural_Gas.Z12()
        z9_1 = Synthetic_Natural_Gas.Z9()
        var_1 = add(z12_1, z9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AA15():
    # 'Synthetic_Natural_Gas'!AA15
    value = 92.96
    formula = "=AA12+AA9"
    @eval_fn
    def AA15():
        aa12_1 = Synthetic_Natural_Gas.AA12()
        aa9_1 = Synthetic_Natural_Gas.AA9()
        var_1 = add(aa12_1, aa9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AB15():
    # 'Synthetic_Natural_Gas'!AB15
    value = 92.96
    formula = "=AB12+AB9"
    @eval_fn
    def AB15():
        ab12_1 = Synthetic_Natural_Gas.AB12()
        ab9_1 = Synthetic_Natural_Gas.AB9()
        var_1 = add(ab12_1, ab9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AC15():
    # 'Synthetic_Natural_Gas'!AC15
    value = 92.96
    formula = "=AC12+AC9"
    @eval_fn
    def AC15():
        ac12_1 = Synthetic_Natural_Gas.AC12()
        ac9_1 = Synthetic_Natural_Gas.AC9()
        var_1 = add(ac12_1, ac9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AD15():
    # 'Synthetic_Natural_Gas'!AD15
    value = 92.96
    formula = "=AD12+AD9"
    @eval_fn
    def AD15():
        ad12_1 = Synthetic_Natural_Gas.AD12()
        ad9_1 = Synthetic_Natural_Gas.AD9()
        var_1 = add(ad12_1, ad9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AE15():
    # 'Synthetic_Natural_Gas'!AE15
    value = 92.96
    formula = "=AE12+AE9"
    @eval_fn
    def AE15():
        ae12_1 = Synthetic_Natural_Gas.AE12()
        ae9_1 = Synthetic_Natural_Gas.AE9()
        var_1 = add(ae12_1, ae9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AF15():
    # 'Synthetic_Natural_Gas'!AF15
    value = 92.96
    formula = "=AF12+AF9"
    @eval_fn
    def AF15():
        af12_1 = Synthetic_Natural_Gas.AF12()
        af9_1 = Synthetic_Natural_Gas.AF9()
        var_1 = add(af12_1, af9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AG15():
    # 'Synthetic_Natural_Gas'!AG15
    value = 92.96
    formula = "=AG12+AG9"
    @eval_fn
    def AG15():
        ag12_1 = Synthetic_Natural_Gas.AG12()
        ag9_1 = Synthetic_Natural_Gas.AG9()
        var_1 = add(ag12_1, ag9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AH15():
    # 'Synthetic_Natural_Gas'!AH15
    value = 92.96
    formula = "=AH12+AH9"
    @eval_fn
    def AH15():
        ah12_1 = Synthetic_Natural_Gas.AH12()
        ah9_1 = Synthetic_Natural_Gas.AH9()
        var_1 = add(ah12_1, ah9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AI15():
    # 'Synthetic_Natural_Gas'!AI15
    value = 92.96
    formula = "=AI12+AI9"
    @eval_fn
    def AI15():
        ai12_1 = Synthetic_Natural_Gas.AI12()
        ai9_1 = Synthetic_Natural_Gas.AI9()
        var_1 = add(ai12_1, ai9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AJ15():
    # 'Synthetic_Natural_Gas'!AJ15
    value = 92.96
    formula = "=AJ12+AJ9"
    @eval_fn
    def AJ15():
        aj12_1 = Synthetic_Natural_Gas.AJ12()
        aj9_1 = Synthetic_Natural_Gas.AJ9()
        var_1 = add(aj12_1, aj9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AK15():
    # 'Synthetic_Natural_Gas'!AK15
    value = 92.96
    formula = "=AK12+AK9"
    @eval_fn
    def AK15():
        ak12_1 = Synthetic_Natural_Gas.AK12()
        ak9_1 = Synthetic_Natural_Gas.AK9()
        var_1 = add(ak12_1, ak9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AL15():
    # 'Synthetic_Natural_Gas'!AL15
    value = 92.96
    formula = "=AL12+AL9"
    @eval_fn
    def AL15():
        al12_1 = Synthetic_Natural_Gas.AL12()
        al9_1 = Synthetic_Natural_Gas.AL9()
        var_1 = add(al12_1, al9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AM15():
    # 'Synthetic_Natural_Gas'!AM15
    value = 92.96
    formula = "=AM12+AM9"
    @eval_fn
    def AM15():
        am12_1 = Synthetic_Natural_Gas.AM12()
        am9_1 = Synthetic_Natural_Gas.AM9()
        var_1 = add(am12_1, am9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AN15():
    # 'Synthetic_Natural_Gas'!AN15
    value = 92.96
    formula = "=AN12+AN9"
    @eval_fn
    def AN15():
        an12_1 = Synthetic_Natural_Gas.AN12()
        an9_1 = Synthetic_Natural_Gas.AN9()
        var_1 = add(an12_1, an9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AO15():
    # 'Synthetic_Natural_Gas'!AO15
    value = 92.96
    formula = "=AO12+AO9"
    @eval_fn
    def AO15():
        ao12_1 = Synthetic_Natural_Gas.AO12()
        ao9_1 = Synthetic_Natural_Gas.AO9()
        var_1 = add(ao12_1, ao9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AP15():
    # 'Synthetic_Natural_Gas'!AP15
    value = 92.96
    formula = "=AP12+AP9"
    @eval_fn
    def AP15():
        ap12_1 = Synthetic_Natural_Gas.AP12()
        ap9_1 = Synthetic_Natural_Gas.AP9()
        var_1 = add(ap12_1, ap9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AQ15():
    # 'Synthetic_Natural_Gas'!AQ15
    value = 92.96
    formula = "=AQ12+AQ9"
    @eval_fn
    def AQ15():
        aq12_1 = Synthetic_Natural_Gas.AQ12()
        aq9_1 = Synthetic_Natural_Gas.AQ9()
        var_1 = add(aq12_1, aq9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AR15():
    # 'Synthetic_Natural_Gas'!AR15
    value = 92.96
    formula = "=AR12+AR9"
    @eval_fn
    def AR15():
        ar12_1 = Synthetic_Natural_Gas.AR12()
        ar9_1 = Synthetic_Natural_Gas.AR9()
        var_1 = add(ar12_1, ar9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AS15():
    # 'Synthetic_Natural_Gas'!AS15
    value = 92.96
    formula = "=AS12+AS9"
    @eval_fn
    def AS15():
        as12_1 = Synthetic_Natural_Gas.AS12()
        as9_1 = Synthetic_Natural_Gas.AS9()
        var_1 = add(as12_1, as9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AT15():
    # 'Synthetic_Natural_Gas'!AT15
    value = 92.96
    formula = "=AT12+AT9"
    @eval_fn
    def AT15():
        at12_1 = Synthetic_Natural_Gas.AT12()
        at9_1 = Synthetic_Natural_Gas.AT9()
        var_1 = add(at12_1, at9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AU15():
    # 'Synthetic_Natural_Gas'!AU15
    value = 92.96
    formula = "=AU12+AU9"
    @eval_fn
    def AU15():
        au12_1 = Synthetic_Natural_Gas.AU12()
        au9_1 = Synthetic_Natural_Gas.AU9()
        var_1 = add(au12_1, au9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AV15():
    # 'Synthetic_Natural_Gas'!AV15
    value = 92.96
    formula = "=AV12+AV9"
    @eval_fn
    def AV15():
        av12_1 = Synthetic_Natural_Gas.AV12()
        av9_1 = Synthetic_Natural_Gas.AV9()
        var_1 = add(av12_1, av9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AW15():
    # 'Synthetic_Natural_Gas'!AW15
    value = 92.96
    formula = "=AW12+AW9"
    @eval_fn
    def AW15():
        aw12_1 = Synthetic_Natural_Gas.AW12()
        aw9_1 = Synthetic_Natural_Gas.AW9()
        var_1 = add(aw12_1, aw9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AX15():
    # 'Synthetic_Natural_Gas'!AX15
    value = 92.96
    formula = "=AX12+AX9"
    @eval_fn
    def AX15():
        ax12_1 = Synthetic_Natural_Gas.AX12()
        ax9_1 = Synthetic_Natural_Gas.AX9()
        var_1 = add(ax12_1, ax9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AY15():
    # 'Synthetic_Natural_Gas'!AY15
    value = 92.96
    formula = "=AY12+AY9"
    @eval_fn
    def AY15():
        ay12_1 = Synthetic_Natural_Gas.AY12()
        ay9_1 = Synthetic_Natural_Gas.AY9()
        var_1 = add(ay12_1, ay9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AZ15():
    # 'Synthetic_Natural_Gas'!AZ15
    value = 92.96
    formula = "=AZ12+AZ9"
    @eval_fn
    def AZ15():
        az12_1 = Synthetic_Natural_Gas.AZ12()
        az9_1 = Synthetic_Natural_Gas.AZ9()
        var_1 = add(az12_1, az9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BA15():
    # 'Synthetic_Natural_Gas'!BA15
    value = 92.96
    formula = "=BA12+BA9"
    @eval_fn
    def BA15():
        ba12_1 = Synthetic_Natural_Gas.BA12()
        ba9_1 = Synthetic_Natural_Gas.BA9()
        var_1 = add(ba12_1, ba9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BB15():
    # 'Synthetic_Natural_Gas'!BB15
    value = 92.96
    formula = "=BB12+BB9"
    @eval_fn
    def BB15():
        bb12_1 = Synthetic_Natural_Gas.BB12()
        bb9_1 = Synthetic_Natural_Gas.BB9()
        var_1 = add(bb12_1, bb9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BC15():
    # 'Synthetic_Natural_Gas'!BC15
    value = 92.96
    formula = "=BC12+BC9"
    @eval_fn
    def BC15():
        bc12_1 = Synthetic_Natural_Gas.BC12()
        bc9_1 = Synthetic_Natural_Gas.BC9()
        var_1 = add(bc12_1, bc9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BD15():
    # 'Synthetic_Natural_Gas'!BD15
    value = 92.96
    formula = "=BD12+BD9"
    @eval_fn
    def BD15():
        bd12_1 = Synthetic_Natural_Gas.BD12()
        bd9_1 = Synthetic_Natural_Gas.BD9()
        var_1 = add(bd12_1, bd9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BE15():
    # 'Synthetic_Natural_Gas'!BE15
    value = 92.96
    formula = "=BE12+BE9"
    @eval_fn
    def BE15():
        be12_1 = Synthetic_Natural_Gas.BE12()
        be9_1 = Synthetic_Natural_Gas.BE9()
        var_1 = add(be12_1, be9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BF15():
    # 'Synthetic_Natural_Gas'!BF15
    value = 92.96
    formula = "=BF12+BF9"
    @eval_fn
    def BF15():
        bf12_1 = Synthetic_Natural_Gas.BF12()
        bf9_1 = Synthetic_Natural_Gas.BF9()
        var_1 = add(bf12_1, bf9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BG15():
    # 'Synthetic_Natural_Gas'!BG15
    value = 92.96
    formula = "=BG12+BG9"
    @eval_fn
    def BG15():
        bg12_1 = Synthetic_Natural_Gas.BG12()
        bg9_1 = Synthetic_Natural_Gas.BG9()
        var_1 = add(bg12_1, bg9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BH15():
    # 'Synthetic_Natural_Gas'!BH15
    value = 92.96
    formula = "=BH12+BH9"
    @eval_fn
    def BH15():
        bh12_1 = Synthetic_Natural_Gas.BH12()
        bh9_1 = Synthetic_Natural_Gas.BH9()
        var_1 = add(bh12_1, bh9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BI15():
    # 'Synthetic_Natural_Gas'!BI15
    value = 92.96
    formula = "=BI12+BI9"
    @eval_fn
    def BI15():
        bi12_1 = Synthetic_Natural_Gas.BI12()
        bi9_1 = Synthetic_Natural_Gas.BI9()
        var_1 = add(bi12_1, bi9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BJ15():
    # 'Synthetic_Natural_Gas'!BJ15
    value = 92.96
    formula = "=BJ12+BJ9"
    @eval_fn
    def BJ15():
        bj12_1 = Synthetic_Natural_Gas.BJ12()
        bj9_1 = Synthetic_Natural_Gas.BJ9()
        var_1 = add(bj12_1, bj9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BK15():
    # 'Synthetic_Natural_Gas'!BK15
    value = 92.96
    formula = "=BK12+BK9"
    @eval_fn
    def BK15():
        bk12_1 = Synthetic_Natural_Gas.BK12()
        bk9_1 = Synthetic_Natural_Gas.BK9()
        var_1 = add(bk12_1, bk9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BL15():
    # 'Synthetic_Natural_Gas'!BL15
    value = 92.96
    formula = "=BL12+BL9"
    @eval_fn
    def BL15():
        bl12_1 = Synthetic_Natural_Gas.BL12()
        bl9_1 = Synthetic_Natural_Gas.BL9()
        var_1 = add(bl12_1, bl9_1)
        return var_1

@register(Synthetic_Natural_Gas)
class A17():
    # 'Synthetic_Natural_Gas'!A17
    value = "Total Emissions"

@register(Synthetic_Natural_Gas)
class C17():
    # 'Synthetic_Natural_Gas'!C17
    value = "Total WTT (Well-to-Tank) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A18():
    # 'Synthetic_Natural_Gas'!A18
    value = "US"

@register(Synthetic_Natural_Gas)
class B18():
    # 'Synthetic_Natural_Gas'!B18
    value = "kgCO2"

@register(Synthetic_Natural_Gas)
class D18():
    # 'Synthetic_Natural_Gas'!D18
    value = 0
    formula = "=D15*D6"
    @eval_fn
    def D18():
        d15_1 = Synthetic_Natural_Gas.D15()
        d6_1 = Synthetic_Natural_Gas.D6()
        var_1 = mult(d15_1, d6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class E18():
    # 'Synthetic_Natural_Gas'!E18
    value = 0
    formula = "=E15*E6"
    @eval_fn
    def E18():
        e15_1 = Synthetic_Natural_Gas.E15()
        e6_1 = Synthetic_Natural_Gas.E6()
        var_1 = mult(e15_1, e6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class F18():
    # 'Synthetic_Natural_Gas'!F18
    value = 0
    formula = "=F15*F6"
    @eval_fn
    def F18():
        f15_1 = Synthetic_Natural_Gas.F15()
        f6_1 = Synthetic_Natural_Gas.F6()
        var_1 = mult(f15_1, f6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class G18():
    # 'Synthetic_Natural_Gas'!G18
    value = 0
    formula = "=G15*G6"
    @eval_fn
    def G18():
        g15_1 = Synthetic_Natural_Gas.G15()
        g6_1 = Synthetic_Natural_Gas.G6()
        var_1 = mult(g15_1, g6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class H18():
    # 'Synthetic_Natural_Gas'!H18
    value = 0
    formula = "=H15*H6"
    @eval_fn
    def H18():
        h15_1 = Synthetic_Natural_Gas.H15()
        h6_1 = Synthetic_Natural_Gas.H6()
        var_1 = mult(h15_1, h6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class I18():
    # 'Synthetic_Natural_Gas'!I18
    value = 0
    formula = "=I15*I6"
    @eval_fn
    def I18():
        i15_1 = Synthetic_Natural_Gas.I15()
        i6_1 = Synthetic_Natural_Gas.I6()
        var_1 = mult(i15_1, i6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class J18():
    # 'Synthetic_Natural_Gas'!J18
    value = 0
    formula = "=J15*J6"
    @eval_fn
    def J18():
        j15_1 = Synthetic_Natural_Gas.J15()
        j6_1 = Synthetic_Natural_Gas.J6()
        var_1 = mult(j15_1, j6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class K18():
    # 'Synthetic_Natural_Gas'!K18
    value = 0
    formula = "=K15*K6"
    @eval_fn
    def K18():
        k15_1 = Synthetic_Natural_Gas.K15()
        k6_1 = Synthetic_Natural_Gas.K6()
        var_1 = mult(k15_1, k6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class L18():
    # 'Synthetic_Natural_Gas'!L18
    value = 0
    formula = "=L15*L6"
    @eval_fn
    def L18():
        l15_1 = Synthetic_Natural_Gas.L15()
        l6_1 = Synthetic_Natural_Gas.L6()
        var_1 = mult(l15_1, l6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class M18():
    # 'Synthetic_Natural_Gas'!M18
    value = 0
    formula = "=M15*M6"
    @eval_fn
    def M18():
        m15_1 = Synthetic_Natural_Gas.M15()
        m6_1 = Synthetic_Natural_Gas.M6()
        var_1 = mult(m15_1, m6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class N18():
    # 'Synthetic_Natural_Gas'!N18
    value = 0
    formula = "=N15*N6"
    @eval_fn
    def N18():
        n15_1 = Synthetic_Natural_Gas.N15()
        n6_1 = Synthetic_Natural_Gas.N6()
        var_1 = mult(n15_1, n6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class O18():
    # 'Synthetic_Natural_Gas'!O18
    value = 0
    formula = "=O15*O6"
    @eval_fn
    def O18():
        o15_1 = Synthetic_Natural_Gas.O15()
        o6_1 = Synthetic_Natural_Gas.O6()
        var_1 = mult(o15_1, o6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class P18():
    # 'Synthetic_Natural_Gas'!P18
    value = 0
    formula = "=P15*P6"
    @eval_fn
    def P18():
        p15_1 = Synthetic_Natural_Gas.P15()
        p6_1 = Synthetic_Natural_Gas.P6()
        var_1 = mult(p15_1, p6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Q18():
    # 'Synthetic_Natural_Gas'!Q18
    value = 0
    formula = "=Q15*Q6"
    @eval_fn
    def Q18():
        q15_1 = Synthetic_Natural_Gas.Q15()
        q6_1 = Synthetic_Natural_Gas.Q6()
        var_1 = mult(q15_1, q6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class R18():
    # 'Synthetic_Natural_Gas'!R18
    value = 0
    formula = "=R15*R6"
    @eval_fn
    def R18():
        r15_1 = Synthetic_Natural_Gas.R15()
        r6_1 = Synthetic_Natural_Gas.R6()
        var_1 = mult(r15_1, r6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class S18():
    # 'Synthetic_Natural_Gas'!S18
    value = 0
    formula = "=S15*S6"
    @eval_fn
    def S18():
        s15_1 = Synthetic_Natural_Gas.S15()
        s6_1 = Synthetic_Natural_Gas.S6()
        var_1 = mult(s15_1, s6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class T18():
    # 'Synthetic_Natural_Gas'!T18
    value = 0
    formula = "=T15*T6"
    @eval_fn
    def T18():
        t15_1 = Synthetic_Natural_Gas.T15()
        t6_1 = Synthetic_Natural_Gas.T6()
        var_1 = mult(t15_1, t6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class U18():
    # 'Synthetic_Natural_Gas'!U18
    value = 0
    formula = "=U15*U6"
    @eval_fn
    def U18():
        u15_1 = Synthetic_Natural_Gas.U15()
        u6_1 = Synthetic_Natural_Gas.U6()
        var_1 = mult(u15_1, u6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class V18():
    # 'Synthetic_Natural_Gas'!V18
    value = 0
    formula = "=V15*V6"
    @eval_fn
    def V18():
        v15_1 = Synthetic_Natural_Gas.V15()
        v6_1 = Synthetic_Natural_Gas.V6()
        var_1 = mult(v15_1, v6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class W18():
    # 'Synthetic_Natural_Gas'!W18
    value = 0
    formula = "=W15*W6"
    @eval_fn
    def W18():
        w15_1 = Synthetic_Natural_Gas.W15()
        w6_1 = Synthetic_Natural_Gas.W6()
        var_1 = mult(w15_1, w6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class X18():
    # 'Synthetic_Natural_Gas'!X18
    value = 280274400
    formula = "=X15*X6"
    @eval_fn
    def X18():
        x15_1 = Synthetic_Natural_Gas.X15()
        x6_1 = Synthetic_Natural_Gas.X6()
        var_1 = mult(x15_1, x6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Y18():
    # 'Synthetic_Natural_Gas'!Y18
    value = 258428800
    formula = "=Y15*Y6"
    @eval_fn
    def Y18():
        y15_1 = Synthetic_Natural_Gas.Y15()
        y6_1 = Synthetic_Natural_Gas.Y6()
        var_1 = mult(y15_1, y6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Z18():
    # 'Synthetic_Natural_Gas'!Z18
    value = 257778080
    formula = "=Z15*Z6"
    @eval_fn
    def Z18():
        z15_1 = Synthetic_Natural_Gas.Z15()
        z6_1 = Synthetic_Natural_Gas.Z6()
        var_1 = mult(z15_1, z6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AA18():
    # 'Synthetic_Natural_Gas'!AA18
    value = 253780800
    formula = "=AA15*AA6"
    @eval_fn
    def AA18():
        aa15_1 = Synthetic_Natural_Gas.AA15()
        aa6_1 = Synthetic_Natural_Gas.AA6()
        var_1 = mult(aa15_1, aa6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AB18():
    # 'Synthetic_Natural_Gas'!AB18
    value = 226636480
    formula = "=AB15*AB6"
    @eval_fn
    def AB18():
        ab15_1 = Synthetic_Natural_Gas.AB15()
        ab6_1 = Synthetic_Natural_Gas.AB6()
        var_1 = mult(ab15_1, ab6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AC18():
    # 'Synthetic_Natural_Gas'!AC18
    value = 249783520
    formula = "=AC15*AC6"
    @eval_fn
    def AC18():
        ac15_1 = Synthetic_Natural_Gas.AC15()
        ac6_1 = Synthetic_Natural_Gas.AC6()
        var_1 = mult(ac15_1, ac6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AD18():
    # 'Synthetic_Natural_Gas'!AD18
    value = 248575040
    formula = "=AD15*AD6"
    @eval_fn
    def AD18():
        ad15_1 = Synthetic_Natural_Gas.AD15()
        ad6_1 = Synthetic_Natural_Gas.AD6()
        var_1 = mult(ad15_1, ad6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AE18():
    # 'Synthetic_Natural_Gas'!AE18
    value = 259079520
    formula = "=AE15*AE6"
    @eval_fn
    def AE18():
        ae15_1 = Synthetic_Natural_Gas.AE15()
        ae6_1 = Synthetic_Natural_Gas.AE6()
        var_1 = mult(ae15_1, ae6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AF18():
    # 'Synthetic_Natural_Gas'!AF18
    value = 261775360
    formula = "=AF15*AF6"
    @eval_fn
    def AF18():
        af15_1 = Synthetic_Natural_Gas.AF15()
        af6_1 = Synthetic_Natural_Gas.AF6()
        var_1 = mult(af15_1, af6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AG18():
    # 'Synthetic_Natural_Gas'!AG18
    value = 270420640
    formula = "=AG15*AG6"
    @eval_fn
    def AG18():
        ag15_1 = Synthetic_Natural_Gas.AG15()
        ag6_1 = Synthetic_Natural_Gas.AG6()
        var_1 = mult(ag15_1, ag6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AH18():
    # 'Synthetic_Natural_Gas'!AH18
    value = 277299680
    formula = "=AH15*AH6"
    @eval_fn
    def AH18():
        ah15_1 = Synthetic_Natural_Gas.AH15()
        ah6_1 = Synthetic_Natural_Gas.AH6()
        var_1 = mult(ah15_1, ah6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AI18():
    # 'Synthetic_Natural_Gas'!AI18
    value = 270420640
    formula = "=AI15*AI6"
    @eval_fn
    def AI18():
        ai15_1 = Synthetic_Natural_Gas.AI15()
        ai6_1 = Synthetic_Natural_Gas.AI6()
        var_1 = mult(ai15_1, ai6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AJ18():
    # 'Synthetic_Natural_Gas'!AJ18
    value = 268840320
    formula = "=AJ15*AJ6"
    @eval_fn
    def AJ18():
        aj15_1 = Synthetic_Natural_Gas.AJ15()
        aj6_1 = Synthetic_Natural_Gas.AJ6()
        var_1 = mult(aj15_1, aj6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AK18():
    # 'Synthetic_Natural_Gas'!AK18
    value = 264657120
    formula = "=AK15*AK6"
    @eval_fn
    def AK18():
        ak15_1 = Synthetic_Natural_Gas.AK15()
        ak6_1 = Synthetic_Natural_Gas.AK6()
        var_1 = mult(ak15_1, ak6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AL18():
    # 'Synthetic_Natural_Gas'!AL18
    value = 271443200
    formula = "=AL15*AL6"
    @eval_fn
    def AL18():
        al15_1 = Synthetic_Natural_Gas.AL15()
        al6_1 = Synthetic_Natural_Gas.AL6()
        var_1 = mult(al15_1, al6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AM18():
    # 'Synthetic_Natural_Gas'!AM18
    value = 270141760
    formula = "=AM15*AM6"
    @eval_fn
    def AM18():
        am15_1 = Synthetic_Natural_Gas.AM15()
        am6_1 = Synthetic_Natural_Gas.AM6()
        var_1 = mult(am15_1, am6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AN18():
    # 'Synthetic_Natural_Gas'!AN18
    value = 262612000
    formula = "=AN15*AN6"
    @eval_fn
    def AN18():
        an15_1 = Synthetic_Natural_Gas.AN15()
        an6_1 = Synthetic_Natural_Gas.AN6()
        var_1 = mult(an15_1, an6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AO18():
    # 'Synthetic_Natural_Gas'!AO18
    value = 249969440
    formula = "=AO15*AO6"
    @eval_fn
    def AO18():
        ao15_1 = Synthetic_Natural_Gas.AO15()
        ao6_1 = Synthetic_Natural_Gas.AO6()
        var_1 = mult(ao15_1, ao6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AP18():
    # 'Synthetic_Natural_Gas'!AP18
    value = 260566880
    formula = "=AP15*AP6"
    @eval_fn
    def AP18():
        ap15_1 = Synthetic_Natural_Gas.AP15()
        ap6_1 = Synthetic_Natural_Gas.AP6()
        var_1 = mult(ap15_1, ap6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AQ18():
    # 'Synthetic_Natural_Gas'!AQ18
    value = 268282560
    formula = "=AQ15*AQ6"
    @eval_fn
    def AQ18():
        aq15_1 = Synthetic_Natural_Gas.AQ15()
        aq6_1 = Synthetic_Natural_Gas.AQ6()
        var_1 = mult(aq15_1, aq6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AR18():
    # 'Synthetic_Natural_Gas'!AR18
    value = 276556000
    formula = "=AR15*AR6"
    @eval_fn
    def AR18():
        ar15_1 = Synthetic_Natural_Gas.AR15()
        ar6_1 = Synthetic_Natural_Gas.AR6()
        var_1 = mult(ar15_1, ar6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AS18():
    # 'Synthetic_Natural_Gas'!AS18
    value = 271443200
    formula = "=AS15*AS6"
    @eval_fn
    def AS18():
        as15_1 = Synthetic_Natural_Gas.AS15()
        as6_1 = Synthetic_Natural_Gas.AS6()
        var_1 = mult(as15_1, as6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AT18():
    # 'Synthetic_Natural_Gas'!AT18
    value = 269398080
    formula = "=AT15*AT6"
    @eval_fn
    def AT18():
        at15_1 = Synthetic_Natural_Gas.AT15()
        at6_1 = Synthetic_Natural_Gas.AT6()
        var_1 = mult(at15_1, at6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AU18():
    # 'Synthetic_Natural_Gas'!AU18
    value = 265958560
    formula = "=AU15*AU6"
    @eval_fn
    def AU18():
        au15_1 = Synthetic_Natural_Gas.AU15()
        au6_1 = Synthetic_Natural_Gas.AU6()
        var_1 = mult(au15_1, au6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AV18():
    # 'Synthetic_Natural_Gas'!AV18
    value = 270234720
    formula = "=AV15*AV6"
    @eval_fn
    def AV18():
        av15_1 = Synthetic_Natural_Gas.AV15()
        av6_1 = Synthetic_Natural_Gas.AV6()
        var_1 = mult(av15_1, av6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AW18():
    # 'Synthetic_Natural_Gas'!AW18
    value = 269398080
    formula = "=AW15*AW6"
    @eval_fn
    def AW18():
        aw15_1 = Synthetic_Natural_Gas.AW15()
        aw6_1 = Synthetic_Natural_Gas.AW6()
        var_1 = mult(aw15_1, aw6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AX18():
    # 'Synthetic_Natural_Gas'!AX18
    value = 270885440
    formula = "=AX15*AX6"
    @eval_fn
    def AX18():
        ax15_1 = Synthetic_Natural_Gas.AX15()
        ax6_1 = Synthetic_Natural_Gas.AX6()
        var_1 = mult(ax15_1, ax6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AY18():
    # 'Synthetic_Natural_Gas'!AY18
    value = 274789760
    formula = "=AY15*AY6"
    @eval_fn
    def AY18():
        ay15_1 = Synthetic_Natural_Gas.AY15()
        ay6_1 = Synthetic_Natural_Gas.AY6()
        var_1 = mult(ay15_1, ay6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AZ18():
    # 'Synthetic_Natural_Gas'!AZ18
    value = 261868320
    formula = "=AZ15*AZ6"
    @eval_fn
    def AZ18():
        az15_1 = Synthetic_Natural_Gas.AZ15()
        az6_1 = Synthetic_Natural_Gas.AZ6()
        var_1 = mult(az15_1, az6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BA18():
    # 'Synthetic_Natural_Gas'!BA18
    value = 252107520
    formula = "=BA15*BA6"
    @eval_fn
    def BA18():
        ba15_1 = Synthetic_Natural_Gas.BA15()
        ba6_1 = Synthetic_Natural_Gas.BA6()
        var_1 = mult(ba15_1, ba6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BB18():
    # 'Synthetic_Natural_Gas'!BB18
    value = 253966720
    formula = "=BB15*BB6"
    @eval_fn
    def BB18():
        bb15_1 = Synthetic_Natural_Gas.BB15()
        bb6_1 = Synthetic_Natural_Gas.BB6()
        var_1 = mult(bb15_1, bb6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BC18():
    # 'Synthetic_Natural_Gas'!BC18
    value = 255082240
    formula = "=BC15*BC6"
    @eval_fn
    def BC18():
        bc15_1 = Synthetic_Natural_Gas.BC15()
        bc6_1 = Synthetic_Natural_Gas.BC6()
        var_1 = mult(bc15_1, bc6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BD18():
    # 'Synthetic_Natural_Gas'!BD18
    value = 261496480
    formula = "=BD15*BD6"
    @eval_fn
    def BD18():
        bd15_1 = Synthetic_Natural_Gas.BD15()
        bd6_1 = Synthetic_Natural_Gas.BD6()
        var_1 = mult(bd15_1, bd6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BE18():
    # 'Synthetic_Natural_Gas'!BE18
    value = 265958560
    formula = "=BE15*BE6"
    @eval_fn
    def BE18():
        be15_1 = Synthetic_Natural_Gas.BE15()
        be6_1 = Synthetic_Natural_Gas.BE6()
        var_1 = mult(be15_1, be6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BF18():
    # 'Synthetic_Natural_Gas'!BF18
    value = "#N/A"
    formula = "=BF15*BF6"
    @eval_fn
    def BF18():
        bf15_1 = Synthetic_Natural_Gas.BF15()
        bf6_1 = Synthetic_Natural_Gas.BF6()
        var_1 = mult(bf15_1, bf6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BG18():
    # 'Synthetic_Natural_Gas'!BG18
    value = "#N/A"
    formula = "=BG15*BG6"
    @eval_fn
    def BG18():
        bg15_1 = Synthetic_Natural_Gas.BG15()
        bg6_1 = Synthetic_Natural_Gas.BG6()
        var_1 = mult(bg15_1, bg6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BH18():
    # 'Synthetic_Natural_Gas'!BH18
    value = "#N/A"
    formula = "=BH15*BH6"
    @eval_fn
    def BH18():
        bh15_1 = Synthetic_Natural_Gas.BH15()
        bh6_1 = Synthetic_Natural_Gas.BH6()
        var_1 = mult(bh15_1, bh6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BI18():
    # 'Synthetic_Natural_Gas'!BI18
    value = "#N/A"
    formula = "=BI15*BI6"
    @eval_fn
    def BI18():
        bi15_1 = Synthetic_Natural_Gas.BI15()
        bi6_1 = Synthetic_Natural_Gas.BI6()
        var_1 = mult(bi15_1, bi6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BJ18():
    # 'Synthetic_Natural_Gas'!BJ18
    value = "#N/A"
    formula = "=BJ15*BJ6"
    @eval_fn
    def BJ18():
        bj15_1 = Synthetic_Natural_Gas.BJ15()
        bj6_1 = Synthetic_Natural_Gas.BJ6()
        var_1 = mult(bj15_1, bj6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BK18():
    # 'Synthetic_Natural_Gas'!BK18
    value = "#N/A"
    formula = "=BK15*BK6"
    @eval_fn
    def BK18():
        bk15_1 = Synthetic_Natural_Gas.BK15()
        bk6_1 = Synthetic_Natural_Gas.BK6()
        var_1 = mult(bk15_1, bk6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BL18():
    # 'Synthetic_Natural_Gas'!BL18
    value = "#N/A"
    formula = "=BL15*BL6"
    @eval_fn
    def BL18():
        bl15_1 = Synthetic_Natural_Gas.BL15()
        bl6_1 = Synthetic_Natural_Gas.BL6()
        var_1 = mult(bl15_1, bl6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class A20():
    # 'Synthetic_Natural_Gas'!A20
    value = "Weights (Upstream Emissions to Total Emissions"

@register(Synthetic_Natural_Gas)
class C20():
    # 'Synthetic_Natural_Gas'!C20
    value = "Percentage"

@register(Synthetic_Natural_Gas)
class A21():
    # 'Synthetic_Natural_Gas'!A21
    value = "US"

@register(Synthetic_Natural_Gas)
class B21():
    # 'Synthetic_Natural_Gas'!B21
    value = "kgCO2"

@register(Synthetic_Natural_Gas)
class D21():
    # 'Synthetic_Natural_Gas'!D21
    value = 0
    formula = "=IF(D18=0,0,(D6*D12)/D18)"
    @eval_fn
    def D21():
        d18_1 = Synthetic_Natural_Gas.D18()
        var_1 = equal(d18_1, 0)
        d6_1 = Synthetic_Natural_Gas.D6()
        d12_1 = Synthetic_Natural_Gas.D12()
        var_2 = mult(d6_1, d12_1)
        d18_2 = Synthetic_Natural_Gas.D18()
        var_3 = divide(var_2, d18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class E21():
    # 'Synthetic_Natural_Gas'!E21
    value = 0
    formula = "=IF(E18=0,0,(E6*E12)/E18)"
    @eval_fn
    def E21():
        e18_1 = Synthetic_Natural_Gas.E18()
        var_1 = equal(e18_1, 0)
        e6_1 = Synthetic_Natural_Gas.E6()
        e12_1 = Synthetic_Natural_Gas.E12()
        var_2 = mult(e6_1, e12_1)
        e18_2 = Synthetic_Natural_Gas.E18()
        var_3 = divide(var_2, e18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class F21():
    # 'Synthetic_Natural_Gas'!F21
    value = 0
    formula = "=IF(F18=0,0,(F6*F12)/F18)"
    @eval_fn
    def F21():
        f18_1 = Synthetic_Natural_Gas.F18()
        var_1 = equal(f18_1, 0)
        f6_1 = Synthetic_Natural_Gas.F6()
        f12_1 = Synthetic_Natural_Gas.F12()
        var_2 = mult(f6_1, f12_1)
        f18_2 = Synthetic_Natural_Gas.F18()
        var_3 = divide(var_2, f18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class G21():
    # 'Synthetic_Natural_Gas'!G21
    value = 0
    formula = "=IF(G18=0,0,(G6*G12)/G18)"
    @eval_fn
    def G21():
        g18_1 = Synthetic_Natural_Gas.G18()
        var_1 = equal(g18_1, 0)
        g6_1 = Synthetic_Natural_Gas.G6()
        g12_1 = Synthetic_Natural_Gas.G12()
        var_2 = mult(g6_1, g12_1)
        g18_2 = Synthetic_Natural_Gas.G18()
        var_3 = divide(var_2, g18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class H21():
    # 'Synthetic_Natural_Gas'!H21
    value = 0
    formula = "=IF(H18=0,0,(H6*H12)/H18)"
    @eval_fn
    def H21():
        h18_1 = Synthetic_Natural_Gas.H18()
        var_1 = equal(h18_1, 0)
        h6_1 = Synthetic_Natural_Gas.H6()
        h12_1 = Synthetic_Natural_Gas.H12()
        var_2 = mult(h6_1, h12_1)
        h18_2 = Synthetic_Natural_Gas.H18()
        var_3 = divide(var_2, h18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class I21():
    # 'Synthetic_Natural_Gas'!I21
    value = 0
    formula = "=IF(I18=0,0,(I6*I12)/I18)"
    @eval_fn
    def I21():
        i18_1 = Synthetic_Natural_Gas.I18()
        var_1 = equal(i18_1, 0)
        i6_1 = Synthetic_Natural_Gas.I6()
        i12_1 = Synthetic_Natural_Gas.I12()
        var_2 = mult(i6_1, i12_1)
        i18_2 = Synthetic_Natural_Gas.I18()
        var_3 = divide(var_2, i18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class J21():
    # 'Synthetic_Natural_Gas'!J21
    value = 0
    formula = "=IF(J18=0,0,(J6*J12)/J18)"
    @eval_fn
    def J21():
        j18_1 = Synthetic_Natural_Gas.J18()
        var_1 = equal(j18_1, 0)
        j6_1 = Synthetic_Natural_Gas.J6()
        j12_1 = Synthetic_Natural_Gas.J12()
        var_2 = mult(j6_1, j12_1)
        j18_2 = Synthetic_Natural_Gas.J18()
        var_3 = divide(var_2, j18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class K21():
    # 'Synthetic_Natural_Gas'!K21
    value = 0
    formula = "=IF(K18=0,0,(K6*K12)/K18)"
    @eval_fn
    def K21():
        k18_1 = Synthetic_Natural_Gas.K18()
        var_1 = equal(k18_1, 0)
        k6_1 = Synthetic_Natural_Gas.K6()
        k12_1 = Synthetic_Natural_Gas.K12()
        var_2 = mult(k6_1, k12_1)
        k18_2 = Synthetic_Natural_Gas.K18()
        var_3 = divide(var_2, k18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class L21():
    # 'Synthetic_Natural_Gas'!L21
    value = 0
    formula = "=IF(L18=0,0,(L6*L12)/L18)"
    @eval_fn
    def L21():
        l18_1 = Synthetic_Natural_Gas.L18()
        var_1 = equal(l18_1, 0)
        l6_1 = Synthetic_Natural_Gas.L6()
        l12_1 = Synthetic_Natural_Gas.L12()
        var_2 = mult(l6_1, l12_1)
        l18_2 = Synthetic_Natural_Gas.L18()
        var_3 = divide(var_2, l18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class M21():
    # 'Synthetic_Natural_Gas'!M21
    value = 0
    formula = "=IF(M18=0,0,(M6*M12)/M18)"
    @eval_fn
    def M21():
        m18_1 = Synthetic_Natural_Gas.M18()
        var_1 = equal(m18_1, 0)
        m6_1 = Synthetic_Natural_Gas.M6()
        m12_1 = Synthetic_Natural_Gas.M12()
        var_2 = mult(m6_1, m12_1)
        m18_2 = Synthetic_Natural_Gas.M18()
        var_3 = divide(var_2, m18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class N21():
    # 'Synthetic_Natural_Gas'!N21
    value = 0
    formula = "=IF(N18=0,0,(N6*N12)/N18)"
    @eval_fn
    def N21():
        n18_1 = Synthetic_Natural_Gas.N18()
        var_1 = equal(n18_1, 0)
        n6_1 = Synthetic_Natural_Gas.N6()
        n12_1 = Synthetic_Natural_Gas.N12()
        var_2 = mult(n6_1, n12_1)
        n18_2 = Synthetic_Natural_Gas.N18()
        var_3 = divide(var_2, n18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class O21():
    # 'Synthetic_Natural_Gas'!O21
    value = 0
    formula = "=IF(O18=0,0,(O6*O12)/O18)"
    @eval_fn
    def O21():
        o18_1 = Synthetic_Natural_Gas.O18()
        var_1 = equal(o18_1, 0)
        o6_1 = Synthetic_Natural_Gas.O6()
        o12_1 = Synthetic_Natural_Gas.O12()
        var_2 = mult(o6_1, o12_1)
        o18_2 = Synthetic_Natural_Gas.O18()
        var_3 = divide(var_2, o18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class P21():
    # 'Synthetic_Natural_Gas'!P21
    value = 0
    formula = "=IF(P18=0,0,(P6*P12)/P18)"
    @eval_fn
    def P21():
        p18_1 = Synthetic_Natural_Gas.P18()
        var_1 = equal(p18_1, 0)
        p6_1 = Synthetic_Natural_Gas.P6()
        p12_1 = Synthetic_Natural_Gas.P12()
        var_2 = mult(p6_1, p12_1)
        p18_2 = Synthetic_Natural_Gas.P18()
        var_3 = divide(var_2, p18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class Q21():
    # 'Synthetic_Natural_Gas'!Q21
    value = 0
    formula = "=IF(Q18=0,0,(Q6*Q12)/Q18)"
    @eval_fn
    def Q21():
        q18_1 = Synthetic_Natural_Gas.Q18()
        var_1 = equal(q18_1, 0)
        q6_1 = Synthetic_Natural_Gas.Q6()
        q12_1 = Synthetic_Natural_Gas.Q12()
        var_2 = mult(q6_1, q12_1)
        q18_2 = Synthetic_Natural_Gas.Q18()
        var_3 = divide(var_2, q18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class R21():
    # 'Synthetic_Natural_Gas'!R21
    value = 0
    formula = "=IF(R18=0,0,(R6*R12)/R18)"
    @eval_fn
    def R21():
        r18_1 = Synthetic_Natural_Gas.R18()
        var_1 = equal(r18_1, 0)
        r6_1 = Synthetic_Natural_Gas.R6()
        r12_1 = Synthetic_Natural_Gas.R12()
        var_2 = mult(r6_1, r12_1)
        r18_2 = Synthetic_Natural_Gas.R18()
        var_3 = divide(var_2, r18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class S21():
    # 'Synthetic_Natural_Gas'!S21
    value = 0
    formula = "=IF(S18=0,0,(S6*S12)/S18)"
    @eval_fn
    def S21():
        s18_1 = Synthetic_Natural_Gas.S18()
        var_1 = equal(s18_1, 0)
        s6_1 = Synthetic_Natural_Gas.S6()
        s12_1 = Synthetic_Natural_Gas.S12()
        var_2 = mult(s6_1, s12_1)
        s18_2 = Synthetic_Natural_Gas.S18()
        var_3 = divide(var_2, s18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class T21():
    # 'Synthetic_Natural_Gas'!T21
    value = 0
    formula = "=IF(T18=0,0,(T6*T12)/T18)"
    @eval_fn
    def T21():
        t18_1 = Synthetic_Natural_Gas.T18()
        var_1 = equal(t18_1, 0)
        t6_1 = Synthetic_Natural_Gas.T6()
        t12_1 = Synthetic_Natural_Gas.T12()
        var_2 = mult(t6_1, t12_1)
        t18_2 = Synthetic_Natural_Gas.T18()
        var_3 = divide(var_2, t18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class U21():
    # 'Synthetic_Natural_Gas'!U21
    value = 0
    formula = "=IF(U18=0,0,(U6*U12)/U18)"
    @eval_fn
    def U21():
        u18_1 = Synthetic_Natural_Gas.U18()
        var_1 = equal(u18_1, 0)
        u6_1 = Synthetic_Natural_Gas.U6()
        u12_1 = Synthetic_Natural_Gas.U12()
        var_2 = mult(u6_1, u12_1)
        u18_2 = Synthetic_Natural_Gas.U18()
        var_3 = divide(var_2, u18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class V21():
    # 'Synthetic_Natural_Gas'!V21
    value = 0
    formula = "=IF(V18=0,0,(V6*V12)/V18)"
    @eval_fn
    def V21():
        v18_1 = Synthetic_Natural_Gas.V18()
        var_1 = equal(v18_1, 0)
        v6_1 = Synthetic_Natural_Gas.V6()
        v12_1 = Synthetic_Natural_Gas.V12()
        var_2 = mult(v6_1, v12_1)
        v18_2 = Synthetic_Natural_Gas.V18()
        var_3 = divide(var_2, v18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class W21():
    # 'Synthetic_Natural_Gas'!W21
    value = 0
    formula = "=IF(W18=0,0,(W6*W12)/W18)"
    @eval_fn
    def W21():
        w18_1 = Synthetic_Natural_Gas.W18()
        var_1 = equal(w18_1, 0)
        w6_1 = Synthetic_Natural_Gas.W6()
        w12_1 = Synthetic_Natural_Gas.W12()
        var_2 = mult(w6_1, w12_1)
        w18_2 = Synthetic_Natural_Gas.W18()
        var_3 = divide(var_2, w18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class X21():
    # 'Synthetic_Natural_Gas'!X21
    value = 0.42921686747
    formula = "=IF(X18=0,0,(X6*X12)/X18)"
    @eval_fn
    def X21():
        x18_1 = Synthetic_Natural_Gas.X18()
        var_1 = equal(x18_1, 0)
        x6_1 = Synthetic_Natural_Gas.X6()
        x12_1 = Synthetic_Natural_Gas.X12()
        var_2 = mult(x6_1, x12_1)
        x18_2 = Synthetic_Natural_Gas.X18()
        var_3 = divide(var_2, x18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class Y21():
    # 'Synthetic_Natural_Gas'!Y21
    value = 0.42921686747
    formula = "=IF(Y18=0,0,(Y6*Y12)/Y18)"
    @eval_fn
    def Y21():
        y18_1 = Synthetic_Natural_Gas.Y18()
        var_1 = equal(y18_1, 0)
        y6_1 = Synthetic_Natural_Gas.Y6()
        y12_1 = Synthetic_Natural_Gas.Y12()
        var_2 = mult(y6_1, y12_1)
        y18_2 = Synthetic_Natural_Gas.Y18()
        var_3 = divide(var_2, y18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class Z21():
    # 'Synthetic_Natural_Gas'!Z21
    value = 0.42921686747
    formula = "=IF(Z18=0,0,(Z6*Z12)/Z18)"
    @eval_fn
    def Z21():
        z18_1 = Synthetic_Natural_Gas.Z18()
        var_1 = equal(z18_1, 0)
        z6_1 = Synthetic_Natural_Gas.Z6()
        z12_1 = Synthetic_Natural_Gas.Z12()
        var_2 = mult(z6_1, z12_1)
        z18_2 = Synthetic_Natural_Gas.Z18()
        var_3 = divide(var_2, z18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AA21():
    # 'Synthetic_Natural_Gas'!AA21
    value = 0.42921686747
    formula = "=IF(AA18=0,0,(AA6*AA12)/AA18)"
    @eval_fn
    def AA21():
        aa18_1 = Synthetic_Natural_Gas.AA18()
        var_1 = equal(aa18_1, 0)
        aa6_1 = Synthetic_Natural_Gas.AA6()
        aa12_1 = Synthetic_Natural_Gas.AA12()
        var_2 = mult(aa6_1, aa12_1)
        aa18_2 = Synthetic_Natural_Gas.AA18()
        var_3 = divide(var_2, aa18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AB21():
    # 'Synthetic_Natural_Gas'!AB21
    value = 0.42921686747
    formula = "=IF(AB18=0,0,(AB6*AB12)/AB18)"
    @eval_fn
    def AB21():
        ab18_1 = Synthetic_Natural_Gas.AB18()
        var_1 = equal(ab18_1, 0)
        ab6_1 = Synthetic_Natural_Gas.AB6()
        ab12_1 = Synthetic_Natural_Gas.AB12()
        var_2 = mult(ab6_1, ab12_1)
        ab18_2 = Synthetic_Natural_Gas.AB18()
        var_3 = divide(var_2, ab18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AC21():
    # 'Synthetic_Natural_Gas'!AC21
    value = 0.42921686747
    formula = "=IF(AC18=0,0,(AC6*AC12)/AC18)"
    @eval_fn
    def AC21():
        ac18_1 = Synthetic_Natural_Gas.AC18()
        var_1 = equal(ac18_1, 0)
        ac6_1 = Synthetic_Natural_Gas.AC6()
        ac12_1 = Synthetic_Natural_Gas.AC12()
        var_2 = mult(ac6_1, ac12_1)
        ac18_2 = Synthetic_Natural_Gas.AC18()
        var_3 = divide(var_2, ac18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AD21():
    # 'Synthetic_Natural_Gas'!AD21
    value = 0.42921686747
    formula = "=IF(AD18=0,0,(AD6*AD12)/AD18)"
    @eval_fn
    def AD21():
        ad18_1 = Synthetic_Natural_Gas.AD18()
        var_1 = equal(ad18_1, 0)
        ad6_1 = Synthetic_Natural_Gas.AD6()
        ad12_1 = Synthetic_Natural_Gas.AD12()
        var_2 = mult(ad6_1, ad12_1)
        ad18_2 = Synthetic_Natural_Gas.AD18()
        var_3 = divide(var_2, ad18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AE21():
    # 'Synthetic_Natural_Gas'!AE21
    value = 0.42921686747
    formula = "=IF(AE18=0,0,(AE6*AE12)/AE18)"
    @eval_fn
    def AE21():
        ae18_1 = Synthetic_Natural_Gas.AE18()
        var_1 = equal(ae18_1, 0)
        ae6_1 = Synthetic_Natural_Gas.AE6()
        ae12_1 = Synthetic_Natural_Gas.AE12()
        var_2 = mult(ae6_1, ae12_1)
        ae18_2 = Synthetic_Natural_Gas.AE18()
        var_3 = divide(var_2, ae18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AF21():
    # 'Synthetic_Natural_Gas'!AF21
    value = 0.42921686747
    formula = "=IF(AF18=0,0,(AF6*AF12)/AF18)"
    @eval_fn
    def AF21():
        af18_1 = Synthetic_Natural_Gas.AF18()
        var_1 = equal(af18_1, 0)
        af6_1 = Synthetic_Natural_Gas.AF6()
        af12_1 = Synthetic_Natural_Gas.AF12()
        var_2 = mult(af6_1, af12_1)
        af18_2 = Synthetic_Natural_Gas.AF18()
        var_3 = divide(var_2, af18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AG21():
    # 'Synthetic_Natural_Gas'!AG21
    value = 0.42921686747
    formula = "=IF(AG18=0,0,(AG6*AG12)/AG18)"
    @eval_fn
    def AG21():
        ag18_1 = Synthetic_Natural_Gas.AG18()
        var_1 = equal(ag18_1, 0)
        ag6_1 = Synthetic_Natural_Gas.AG6()
        ag12_1 = Synthetic_Natural_Gas.AG12()
        var_2 = mult(ag6_1, ag12_1)
        ag18_2 = Synthetic_Natural_Gas.AG18()
        var_3 = divide(var_2, ag18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AH21():
    # 'Synthetic_Natural_Gas'!AH21
    value = 0.42921686747
    formula = "=IF(AH18=0,0,(AH6*AH12)/AH18)"
    @eval_fn
    def AH21():
        ah18_1 = Synthetic_Natural_Gas.AH18()
        var_1 = equal(ah18_1, 0)
        ah6_1 = Synthetic_Natural_Gas.AH6()
        ah12_1 = Synthetic_Natural_Gas.AH12()
        var_2 = mult(ah6_1, ah12_1)
        ah18_2 = Synthetic_Natural_Gas.AH18()
        var_3 = divide(var_2, ah18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AI21():
    # 'Synthetic_Natural_Gas'!AI21
    value = 0.42921686747
    formula = "=IF(AI18=0,0,(AI6*AI12)/AI18)"
    @eval_fn
    def AI21():
        ai18_1 = Synthetic_Natural_Gas.AI18()
        var_1 = equal(ai18_1, 0)
        ai6_1 = Synthetic_Natural_Gas.AI6()
        ai12_1 = Synthetic_Natural_Gas.AI12()
        var_2 = mult(ai6_1, ai12_1)
        ai18_2 = Synthetic_Natural_Gas.AI18()
        var_3 = divide(var_2, ai18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AJ21():
    # 'Synthetic_Natural_Gas'!AJ21
    value = 0.42921686747
    formula = "=IF(AJ18=0,0,(AJ6*AJ12)/AJ18)"
    @eval_fn
    def AJ21():
        aj18_1 = Synthetic_Natural_Gas.AJ18()
        var_1 = equal(aj18_1, 0)
        aj6_1 = Synthetic_Natural_Gas.AJ6()
        aj12_1 = Synthetic_Natural_Gas.AJ12()
        var_2 = mult(aj6_1, aj12_1)
        aj18_2 = Synthetic_Natural_Gas.AJ18()
        var_3 = divide(var_2, aj18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AK21():
    # 'Synthetic_Natural_Gas'!AK21
    value = 0.42921686747
    formula = "=IF(AK18=0,0,(AK6*AK12)/AK18)"
    @eval_fn
    def AK21():
        ak18_1 = Synthetic_Natural_Gas.AK18()
        var_1 = equal(ak18_1, 0)
        ak6_1 = Synthetic_Natural_Gas.AK6()
        ak12_1 = Synthetic_Natural_Gas.AK12()
        var_2 = mult(ak6_1, ak12_1)
        ak18_2 = Synthetic_Natural_Gas.AK18()
        var_3 = divide(var_2, ak18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AL21():
    # 'Synthetic_Natural_Gas'!AL21
    value = 0.42921686747
    formula = "=IF(AL18=0,0,(AL6*AL12)/AL18)"
    @eval_fn
    def AL21():
        al18_1 = Synthetic_Natural_Gas.AL18()
        var_1 = equal(al18_1, 0)
        al6_1 = Synthetic_Natural_Gas.AL6()
        al12_1 = Synthetic_Natural_Gas.AL12()
        var_2 = mult(al6_1, al12_1)
        al18_2 = Synthetic_Natural_Gas.AL18()
        var_3 = divide(var_2, al18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AM21():
    # 'Synthetic_Natural_Gas'!AM21
    value = 0.42921686747
    formula = "=IF(AM18=0,0,(AM6*AM12)/AM18)"
    @eval_fn
    def AM21():
        am18_1 = Synthetic_Natural_Gas.AM18()
        var_1 = equal(am18_1, 0)
        am6_1 = Synthetic_Natural_Gas.AM6()
        am12_1 = Synthetic_Natural_Gas.AM12()
        var_2 = mult(am6_1, am12_1)
        am18_2 = Synthetic_Natural_Gas.AM18()
        var_3 = divide(var_2, am18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AN21():
    # 'Synthetic_Natural_Gas'!AN21
    value = 0.42921686747
    formula = "=IF(AN18=0,0,(AN6*AN12)/AN18)"
    @eval_fn
    def AN21():
        an18_1 = Synthetic_Natural_Gas.AN18()
        var_1 = equal(an18_1, 0)
        an6_1 = Synthetic_Natural_Gas.AN6()
        an12_1 = Synthetic_Natural_Gas.AN12()
        var_2 = mult(an6_1, an12_1)
        an18_2 = Synthetic_Natural_Gas.AN18()
        var_3 = divide(var_2, an18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AO21():
    # 'Synthetic_Natural_Gas'!AO21
    value = 0.42921686747
    formula = "=IF(AO18=0,0,(AO6*AO12)/AO18)"
    @eval_fn
    def AO21():
        ao18_1 = Synthetic_Natural_Gas.AO18()
        var_1 = equal(ao18_1, 0)
        ao6_1 = Synthetic_Natural_Gas.AO6()
        ao12_1 = Synthetic_Natural_Gas.AO12()
        var_2 = mult(ao6_1, ao12_1)
        ao18_2 = Synthetic_Natural_Gas.AO18()
        var_3 = divide(var_2, ao18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AP21():
    # 'Synthetic_Natural_Gas'!AP21
    value = 0.42921686747
    formula = "=IF(AP18=0,0,(AP6*AP12)/AP18)"
    @eval_fn
    def AP21():
        ap18_1 = Synthetic_Natural_Gas.AP18()
        var_1 = equal(ap18_1, 0)
        ap6_1 = Synthetic_Natural_Gas.AP6()
        ap12_1 = Synthetic_Natural_Gas.AP12()
        var_2 = mult(ap6_1, ap12_1)
        ap18_2 = Synthetic_Natural_Gas.AP18()
        var_3 = divide(var_2, ap18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AQ21():
    # 'Synthetic_Natural_Gas'!AQ21
    value = 0.42921686747
    formula = "=IF(AQ18=0,0,(AQ6*AQ12)/AQ18)"
    @eval_fn
    def AQ21():
        aq18_1 = Synthetic_Natural_Gas.AQ18()
        var_1 = equal(aq18_1, 0)
        aq6_1 = Synthetic_Natural_Gas.AQ6()
        aq12_1 = Synthetic_Natural_Gas.AQ12()
        var_2 = mult(aq6_1, aq12_1)
        aq18_2 = Synthetic_Natural_Gas.AQ18()
        var_3 = divide(var_2, aq18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AR21():
    # 'Synthetic_Natural_Gas'!AR21
    value = 0.42921686747
    formula = "=IF(AR18=0,0,(AR6*AR12)/AR18)"
    @eval_fn
    def AR21():
        ar18_1 = Synthetic_Natural_Gas.AR18()
        var_1 = equal(ar18_1, 0)
        ar6_1 = Synthetic_Natural_Gas.AR6()
        ar12_1 = Synthetic_Natural_Gas.AR12()
        var_2 = mult(ar6_1, ar12_1)
        ar18_2 = Synthetic_Natural_Gas.AR18()
        var_3 = divide(var_2, ar18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AS21():
    # 'Synthetic_Natural_Gas'!AS21
    value = 0.42921686747
    formula = "=IF(AS18=0,0,(AS6*AS12)/AS18)"
    @eval_fn
    def AS21():
        as18_1 = Synthetic_Natural_Gas.AS18()
        var_1 = equal(as18_1, 0)
        as6_1 = Synthetic_Natural_Gas.AS6()
        as12_1 = Synthetic_Natural_Gas.AS12()
        var_2 = mult(as6_1, as12_1)
        as18_2 = Synthetic_Natural_Gas.AS18()
        var_3 = divide(var_2, as18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AT21():
    # 'Synthetic_Natural_Gas'!AT21
    value = 0.42921686747
    formula = "=IF(AT18=0,0,(AT6*AT12)/AT18)"
    @eval_fn
    def AT21():
        at18_1 = Synthetic_Natural_Gas.AT18()
        var_1 = equal(at18_1, 0)
        at6_1 = Synthetic_Natural_Gas.AT6()
        at12_1 = Synthetic_Natural_Gas.AT12()
        var_2 = mult(at6_1, at12_1)
        at18_2 = Synthetic_Natural_Gas.AT18()
        var_3 = divide(var_2, at18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AU21():
    # 'Synthetic_Natural_Gas'!AU21
    value = 0.42921686747
    formula = "=IF(AU18=0,0,(AU6*AU12)/AU18)"
    @eval_fn
    def AU21():
        au18_1 = Synthetic_Natural_Gas.AU18()
        var_1 = equal(au18_1, 0)
        au6_1 = Synthetic_Natural_Gas.AU6()
        au12_1 = Synthetic_Natural_Gas.AU12()
        var_2 = mult(au6_1, au12_1)
        au18_2 = Synthetic_Natural_Gas.AU18()
        var_3 = divide(var_2, au18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AV21():
    # 'Synthetic_Natural_Gas'!AV21
    value = 0.42921686747
    formula = "=IF(AV18=0,0,(AV6*AV12)/AV18)"
    @eval_fn
    def AV21():
        av18_1 = Synthetic_Natural_Gas.AV18()
        var_1 = equal(av18_1, 0)
        av6_1 = Synthetic_Natural_Gas.AV6()
        av12_1 = Synthetic_Natural_Gas.AV12()
        var_2 = mult(av6_1, av12_1)
        av18_2 = Synthetic_Natural_Gas.AV18()
        var_3 = divide(var_2, av18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AW21():
    # 'Synthetic_Natural_Gas'!AW21
    value = 0.42921686747
    formula = "=IF(AW18=0,0,(AW6*AW12)/AW18)"
    @eval_fn
    def AW21():
        aw18_1 = Synthetic_Natural_Gas.AW18()
        var_1 = equal(aw18_1, 0)
        aw6_1 = Synthetic_Natural_Gas.AW6()
        aw12_1 = Synthetic_Natural_Gas.AW12()
        var_2 = mult(aw6_1, aw12_1)
        aw18_2 = Synthetic_Natural_Gas.AW18()
        var_3 = divide(var_2, aw18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AX21():
    # 'Synthetic_Natural_Gas'!AX21
    value = 0.42921686747
    formula = "=IF(AX18=0,0,(AX6*AX12)/AX18)"
    @eval_fn
    def AX21():
        ax18_1 = Synthetic_Natural_Gas.AX18()
        var_1 = equal(ax18_1, 0)
        ax6_1 = Synthetic_Natural_Gas.AX6()
        ax12_1 = Synthetic_Natural_Gas.AX12()
        var_2 = mult(ax6_1, ax12_1)
        ax18_2 = Synthetic_Natural_Gas.AX18()
        var_3 = divide(var_2, ax18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AY21():
    # 'Synthetic_Natural_Gas'!AY21
    value = 0.42921686747
    formula = "=IF(AY18=0,0,(AY6*AY12)/AY18)"
    @eval_fn
    def AY21():
        ay18_1 = Synthetic_Natural_Gas.AY18()
        var_1 = equal(ay18_1, 0)
        ay6_1 = Synthetic_Natural_Gas.AY6()
        ay12_1 = Synthetic_Natural_Gas.AY12()
        var_2 = mult(ay6_1, ay12_1)
        ay18_2 = Synthetic_Natural_Gas.AY18()
        var_3 = divide(var_2, ay18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class AZ21():
    # 'Synthetic_Natural_Gas'!AZ21
    value = 0.42921686747
    formula = "=IF(AZ18=0,0,(AZ6*AZ12)/AZ18)"
    @eval_fn
    def AZ21():
        az18_1 = Synthetic_Natural_Gas.AZ18()
        var_1 = equal(az18_1, 0)
        az6_1 = Synthetic_Natural_Gas.AZ6()
        az12_1 = Synthetic_Natural_Gas.AZ12()
        var_2 = mult(az6_1, az12_1)
        az18_2 = Synthetic_Natural_Gas.AZ18()
        var_3 = divide(var_2, az18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BA21():
    # 'Synthetic_Natural_Gas'!BA21
    value = 0.42921686747
    formula = "=IF(BA18=0,0,(BA6*BA12)/BA18)"
    @eval_fn
    def BA21():
        ba18_1 = Synthetic_Natural_Gas.BA18()
        var_1 = equal(ba18_1, 0)
        ba6_1 = Synthetic_Natural_Gas.BA6()
        ba12_1 = Synthetic_Natural_Gas.BA12()
        var_2 = mult(ba6_1, ba12_1)
        ba18_2 = Synthetic_Natural_Gas.BA18()
        var_3 = divide(var_2, ba18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BB21():
    # 'Synthetic_Natural_Gas'!BB21
    value = 0.42921686747
    formula = "=IF(BB18=0,0,(BB6*BB12)/BB18)"
    @eval_fn
    def BB21():
        bb18_1 = Synthetic_Natural_Gas.BB18()
        var_1 = equal(bb18_1, 0)
        bb6_1 = Synthetic_Natural_Gas.BB6()
        bb12_1 = Synthetic_Natural_Gas.BB12()
        var_2 = mult(bb6_1, bb12_1)
        bb18_2 = Synthetic_Natural_Gas.BB18()
        var_3 = divide(var_2, bb18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BC21():
    # 'Synthetic_Natural_Gas'!BC21
    value = 0.42921686747
    formula = "=IF(BC18=0,0,(BC6*BC12)/BC18)"
    @eval_fn
    def BC21():
        bc18_1 = Synthetic_Natural_Gas.BC18()
        var_1 = equal(bc18_1, 0)
        bc6_1 = Synthetic_Natural_Gas.BC6()
        bc12_1 = Synthetic_Natural_Gas.BC12()
        var_2 = mult(bc6_1, bc12_1)
        bc18_2 = Synthetic_Natural_Gas.BC18()
        var_3 = divide(var_2, bc18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BD21():
    # 'Synthetic_Natural_Gas'!BD21
    value = 0.42921686747
    formula = "=IF(BD18=0,0,(BD6*BD12)/BD18)"
    @eval_fn
    def BD21():
        bd18_1 = Synthetic_Natural_Gas.BD18()
        var_1 = equal(bd18_1, 0)
        bd6_1 = Synthetic_Natural_Gas.BD6()
        bd12_1 = Synthetic_Natural_Gas.BD12()
        var_2 = mult(bd6_1, bd12_1)
        bd18_2 = Synthetic_Natural_Gas.BD18()
        var_3 = divide(var_2, bd18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BE21():
    # 'Synthetic_Natural_Gas'!BE21
    value = 0.42921686747
    formula = "=IF(BE18=0,0,(BE6*BE12)/BE18)"
    @eval_fn
    def BE21():
        be18_1 = Synthetic_Natural_Gas.BE18()
        var_1 = equal(be18_1, 0)
        be6_1 = Synthetic_Natural_Gas.BE6()
        be12_1 = Synthetic_Natural_Gas.BE12()
        var_2 = mult(be6_1, be12_1)
        be18_2 = Synthetic_Natural_Gas.BE18()
        var_3 = divide(var_2, be18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BF21():
    # 'Synthetic_Natural_Gas'!BF21
    value = "#N/A"
    formula = "=IF(BF18=0,0,(BF6*BF12)/BF18)"
    @eval_fn
    def BF21():
        bf18_1 = Synthetic_Natural_Gas.BF18()
        var_1 = equal(bf18_1, 0)
        bf6_1 = Synthetic_Natural_Gas.BF6()
        bf12_1 = Synthetic_Natural_Gas.BF12()
        var_2 = mult(bf6_1, bf12_1)
        bf18_2 = Synthetic_Natural_Gas.BF18()
        var_3 = divide(var_2, bf18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BG21():
    # 'Synthetic_Natural_Gas'!BG21
    value = "#N/A"
    formula = "=IF(BG18=0,0,(BG6*BG12)/BG18)"
    @eval_fn
    def BG21():
        bg18_1 = Synthetic_Natural_Gas.BG18()
        var_1 = equal(bg18_1, 0)
        bg6_1 = Synthetic_Natural_Gas.BG6()
        bg12_1 = Synthetic_Natural_Gas.BG12()
        var_2 = mult(bg6_1, bg12_1)
        bg18_2 = Synthetic_Natural_Gas.BG18()
        var_3 = divide(var_2, bg18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BH21():
    # 'Synthetic_Natural_Gas'!BH21
    value = "#N/A"
    formula = "=IF(BH18=0,0,(BH6*BH12)/BH18)"
    @eval_fn
    def BH21():
        bh18_1 = Synthetic_Natural_Gas.BH18()
        var_1 = equal(bh18_1, 0)
        bh6_1 = Synthetic_Natural_Gas.BH6()
        bh12_1 = Synthetic_Natural_Gas.BH12()
        var_2 = mult(bh6_1, bh12_1)
        bh18_2 = Synthetic_Natural_Gas.BH18()
        var_3 = divide(var_2, bh18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BI21():
    # 'Synthetic_Natural_Gas'!BI21
    value = "#N/A"
    formula = "=IF(BI18=0,0,(BI6*BI12)/BI18)"
    @eval_fn
    def BI21():
        bi18_1 = Synthetic_Natural_Gas.BI18()
        var_1 = equal(bi18_1, 0)
        bi6_1 = Synthetic_Natural_Gas.BI6()
        bi12_1 = Synthetic_Natural_Gas.BI12()
        var_2 = mult(bi6_1, bi12_1)
        bi18_2 = Synthetic_Natural_Gas.BI18()
        var_3 = divide(var_2, bi18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BJ21():
    # 'Synthetic_Natural_Gas'!BJ21
    value = "#N/A"
    formula = "=IF(BJ18=0,0,(BJ6*BJ12)/BJ18)"
    @eval_fn
    def BJ21():
        bj18_1 = Synthetic_Natural_Gas.BJ18()
        var_1 = equal(bj18_1, 0)
        bj6_1 = Synthetic_Natural_Gas.BJ6()
        bj12_1 = Synthetic_Natural_Gas.BJ12()
        var_2 = mult(bj6_1, bj12_1)
        bj18_2 = Synthetic_Natural_Gas.BJ18()
        var_3 = divide(var_2, bj18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BK21():
    # 'Synthetic_Natural_Gas'!BK21
    value = "#N/A"
    formula = "=IF(BK18=0,0,(BK6*BK12)/BK18)"
    @eval_fn
    def BK21():
        bk18_1 = Synthetic_Natural_Gas.BK18()
        var_1 = equal(bk18_1, 0)
        bk6_1 = Synthetic_Natural_Gas.BK6()
        bk12_1 = Synthetic_Natural_Gas.BK12()
        var_2 = mult(bk6_1, bk12_1)
        bk18_2 = Synthetic_Natural_Gas.BK18()
        var_3 = divide(var_2, bk18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class BL21():
    # 'Synthetic_Natural_Gas'!BL21
    value = "#N/A"
    formula = "=IF(BL18=0,0,(BL6*BL12)/BL18)"
    @eval_fn
    def BL21():
        bl18_1 = Synthetic_Natural_Gas.BL18()
        var_1 = equal(bl18_1, 0)
        bl6_1 = Synthetic_Natural_Gas.BL6()
        bl12_1 = Synthetic_Natural_Gas.BL12()
        var_2 = mult(bl6_1, bl12_1)
        bl18_2 = Synthetic_Natural_Gas.BL18()
        var_3 = divide(var_2, bl18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Synthetic_Natural_Gas)
class A23():
    # 'Synthetic_Natural_Gas'!A23
    value = "Upstream BTU (BTU attributable to raw materials acquisition and raw materials transport"

@register(Synthetic_Natural_Gas)
class C23():
    # 'Synthetic_Natural_Gas'!C23
    value = "Total WTW (Well-to-Tank) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A24():
    # 'Synthetic_Natural_Gas'!A24
    value = "US"

@register(Synthetic_Natural_Gas)
class B24():
    # 'Synthetic_Natural_Gas'!B24
    value = "Mmbtu"

@register(Synthetic_Natural_Gas)
class D24():
    # 'Synthetic_Natural_Gas'!D24
    value = 0
    formula = "=D21*D6"
    @eval_fn
    def D24():
        d21_1 = Synthetic_Natural_Gas.D21()
        d6_1 = Synthetic_Natural_Gas.D6()
        var_1 = mult(d21_1, d6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class E24():
    # 'Synthetic_Natural_Gas'!E24
    value = 0
    formula = "=E21*E6"
    @eval_fn
    def E24():
        e21_1 = Synthetic_Natural_Gas.E21()
        e6_1 = Synthetic_Natural_Gas.E6()
        var_1 = mult(e21_1, e6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class F24():
    # 'Synthetic_Natural_Gas'!F24
    value = 0
    formula = "=F21*F6"
    @eval_fn
    def F24():
        f21_1 = Synthetic_Natural_Gas.F21()
        f6_1 = Synthetic_Natural_Gas.F6()
        var_1 = mult(f21_1, f6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class G24():
    # 'Synthetic_Natural_Gas'!G24
    value = 0
    formula = "=G21*G6"
    @eval_fn
    def G24():
        g21_1 = Synthetic_Natural_Gas.G21()
        g6_1 = Synthetic_Natural_Gas.G6()
        var_1 = mult(g21_1, g6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class H24():
    # 'Synthetic_Natural_Gas'!H24
    value = 0
    formula = "=H21*H6"
    @eval_fn
    def H24():
        h21_1 = Synthetic_Natural_Gas.H21()
        h6_1 = Synthetic_Natural_Gas.H6()
        var_1 = mult(h21_1, h6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class I24():
    # 'Synthetic_Natural_Gas'!I24
    value = 0
    formula = "=I21*I6"
    @eval_fn
    def I24():
        i21_1 = Synthetic_Natural_Gas.I21()
        i6_1 = Synthetic_Natural_Gas.I6()
        var_1 = mult(i21_1, i6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class J24():
    # 'Synthetic_Natural_Gas'!J24
    value = 0
    formula = "=J21*J6"
    @eval_fn
    def J24():
        j21_1 = Synthetic_Natural_Gas.J21()
        j6_1 = Synthetic_Natural_Gas.J6()
        var_1 = mult(j21_1, j6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class K24():
    # 'Synthetic_Natural_Gas'!K24
    value = 0
    formula = "=K21*K6"
    @eval_fn
    def K24():
        k21_1 = Synthetic_Natural_Gas.K21()
        k6_1 = Synthetic_Natural_Gas.K6()
        var_1 = mult(k21_1, k6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class L24():
    # 'Synthetic_Natural_Gas'!L24
    value = 0
    formula = "=L21*L6"
    @eval_fn
    def L24():
        l21_1 = Synthetic_Natural_Gas.L21()
        l6_1 = Synthetic_Natural_Gas.L6()
        var_1 = mult(l21_1, l6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class M24():
    # 'Synthetic_Natural_Gas'!M24
    value = 0
    formula = "=M21*M6"
    @eval_fn
    def M24():
        m21_1 = Synthetic_Natural_Gas.M21()
        m6_1 = Synthetic_Natural_Gas.M6()
        var_1 = mult(m21_1, m6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class N24():
    # 'Synthetic_Natural_Gas'!N24
    value = 0
    formula = "=N21*N6"
    @eval_fn
    def N24():
        n21_1 = Synthetic_Natural_Gas.N21()
        n6_1 = Synthetic_Natural_Gas.N6()
        var_1 = mult(n21_1, n6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class O24():
    # 'Synthetic_Natural_Gas'!O24
    value = 0
    formula = "=O21*O6"
    @eval_fn
    def O24():
        o21_1 = Synthetic_Natural_Gas.O21()
        o6_1 = Synthetic_Natural_Gas.O6()
        var_1 = mult(o21_1, o6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class P24():
    # 'Synthetic_Natural_Gas'!P24
    value = 0
    formula = "=P21*P6"
    @eval_fn
    def P24():
        p21_1 = Synthetic_Natural_Gas.P21()
        p6_1 = Synthetic_Natural_Gas.P6()
        var_1 = mult(p21_1, p6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Q24():
    # 'Synthetic_Natural_Gas'!Q24
    value = 0
    formula = "=Q21*Q6"
    @eval_fn
    def Q24():
        q21_1 = Synthetic_Natural_Gas.Q21()
        q6_1 = Synthetic_Natural_Gas.Q6()
        var_1 = mult(q21_1, q6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class R24():
    # 'Synthetic_Natural_Gas'!R24
    value = 0
    formula = "=R21*R6"
    @eval_fn
    def R24():
        r21_1 = Synthetic_Natural_Gas.R21()
        r6_1 = Synthetic_Natural_Gas.R6()
        var_1 = mult(r21_1, r6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class S24():
    # 'Synthetic_Natural_Gas'!S24
    value = 0
    formula = "=S21*S6"
    @eval_fn
    def S24():
        s21_1 = Synthetic_Natural_Gas.S21()
        s6_1 = Synthetic_Natural_Gas.S6()
        var_1 = mult(s21_1, s6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class T24():
    # 'Synthetic_Natural_Gas'!T24
    value = 0
    formula = "=T21*T6"
    @eval_fn
    def T24():
        t21_1 = Synthetic_Natural_Gas.T21()
        t6_1 = Synthetic_Natural_Gas.T6()
        var_1 = mult(t21_1, t6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class U24():
    # 'Synthetic_Natural_Gas'!U24
    value = 0
    formula = "=U21*U6"
    @eval_fn
    def U24():
        u21_1 = Synthetic_Natural_Gas.U21()
        u6_1 = Synthetic_Natural_Gas.U6()
        var_1 = mult(u21_1, u6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class V24():
    # 'Synthetic_Natural_Gas'!V24
    value = 0
    formula = "=V21*V6"
    @eval_fn
    def V24():
        v21_1 = Synthetic_Natural_Gas.V21()
        v6_1 = Synthetic_Natural_Gas.V6()
        var_1 = mult(v21_1, v6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class W24():
    # 'Synthetic_Natural_Gas'!W24
    value = 0
    formula = "=W21*W6"
    @eval_fn
    def W24():
        w21_1 = Synthetic_Natural_Gas.W21()
        w6_1 = Synthetic_Natural_Gas.W6()
        var_1 = mult(w21_1, w6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class X24():
    # 'Synthetic_Natural_Gas'!X24
    value = 1294088.85542
    formula = "=X21*X6"
    @eval_fn
    def X24():
        x21_1 = Synthetic_Natural_Gas.X21()
        x6_1 = Synthetic_Natural_Gas.X6()
        var_1 = mult(x21_1, x6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Y24():
    # 'Synthetic_Natural_Gas'!Y24
    value = 1193222.89157
    formula = "=Y21*Y6"
    @eval_fn
    def Y24():
        y21_1 = Synthetic_Natural_Gas.Y21()
        y6_1 = Synthetic_Natural_Gas.Y6()
        var_1 = mult(y21_1, y6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class Z24():
    # 'Synthetic_Natural_Gas'!Z24
    value = 1190218.37349
    formula = "=Z21*Z6"
    @eval_fn
    def Z24():
        z21_1 = Synthetic_Natural_Gas.Z21()
        z6_1 = Synthetic_Natural_Gas.Z6()
        var_1 = mult(z21_1, z6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AA24():
    # 'Synthetic_Natural_Gas'!AA24
    value = 1171762.04819
    formula = "=AA21*AA6"
    @eval_fn
    def AA24():
        aa21_1 = Synthetic_Natural_Gas.AA21()
        aa6_1 = Synthetic_Natural_Gas.AA6()
        var_1 = mult(aa21_1, aa6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AB24():
    # 'Synthetic_Natural_Gas'!AB24
    value = 1046430.72289
    formula = "=AB21*AB6"
    @eval_fn
    def AB24():
        ab21_1 = Synthetic_Natural_Gas.AB21()
        ab6_1 = Synthetic_Natural_Gas.AB6()
        var_1 = mult(ab21_1, ab6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AC24():
    # 'Synthetic_Natural_Gas'!AC24
    value = 1153305.72289
    formula = "=AC21*AC6"
    @eval_fn
    def AC24():
        ac21_1 = Synthetic_Natural_Gas.AC21()
        ac6_1 = Synthetic_Natural_Gas.AC6()
        var_1 = mult(ac21_1, ac6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AD24():
    # 'Synthetic_Natural_Gas'!AD24
    value = 1147725.90361
    formula = "=AD21*AD6"
    @eval_fn
    def AD24():
        ad21_1 = Synthetic_Natural_Gas.AD21()
        ad6_1 = Synthetic_Natural_Gas.AD6()
        var_1 = mult(ad21_1, ad6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AE24():
    # 'Synthetic_Natural_Gas'!AE24
    value = 1196227.40964
    formula = "=AE21*AE6"
    @eval_fn
    def AE24():
        ae21_1 = Synthetic_Natural_Gas.AE21()
        ae6_1 = Synthetic_Natural_Gas.AE6()
        var_1 = mult(ae21_1, ae6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AF24():
    # 'Synthetic_Natural_Gas'!AF24
    value = 1208674.6988
    formula = "=AF21*AF6"
    @eval_fn
    def AF24():
        af21_1 = Synthetic_Natural_Gas.AF21()
        af6_1 = Synthetic_Natural_Gas.AF6()
        var_1 = mult(af21_1, af6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AG24():
    # 'Synthetic_Natural_Gas'!AG24
    value = 1248591.86747
    formula = "=AG21*AG6"
    @eval_fn
    def AG24():
        ag21_1 = Synthetic_Natural_Gas.AG21()
        ag6_1 = Synthetic_Natural_Gas.AG6()
        var_1 = mult(ag21_1, ag6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AH24():
    # 'Synthetic_Natural_Gas'!AH24
    value = 1280353.91566
    formula = "=AH21*AH6"
    @eval_fn
    def AH24():
        ah21_1 = Synthetic_Natural_Gas.AH21()
        ah6_1 = Synthetic_Natural_Gas.AH6()
        var_1 = mult(ah21_1, ah6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AI24():
    # 'Synthetic_Natural_Gas'!AI24
    value = 1248591.86747
    formula = "=AI21*AI6"
    @eval_fn
    def AI24():
        ai21_1 = Synthetic_Natural_Gas.AI21()
        ai6_1 = Synthetic_Natural_Gas.AI6()
        var_1 = mult(ai21_1, ai6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AJ24():
    # 'Synthetic_Natural_Gas'!AJ24
    value = 1241295.18072
    formula = "=AJ21*AJ6"
    @eval_fn
    def AJ24():
        aj21_1 = Synthetic_Natural_Gas.AJ21()
        aj6_1 = Synthetic_Natural_Gas.AJ6()
        var_1 = mult(aj21_1, aj6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AK24():
    # 'Synthetic_Natural_Gas'!AK24
    value = 1221980.42169
    formula = "=AK21*AK6"
    @eval_fn
    def AK24():
        ak21_1 = Synthetic_Natural_Gas.AK21()
        ak6_1 = Synthetic_Natural_Gas.AK6()
        var_1 = mult(ak21_1, ak6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AL24():
    # 'Synthetic_Natural_Gas'!AL24
    value = 1253313.25301
    formula = "=AL21*AL6"
    @eval_fn
    def AL24():
        al21_1 = Synthetic_Natural_Gas.AL21()
        al6_1 = Synthetic_Natural_Gas.AL6()
        var_1 = mult(al21_1, al6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AM24():
    # 'Synthetic_Natural_Gas'!AM24
    value = 1247304.21687
    formula = "=AM21*AM6"
    @eval_fn
    def AM24():
        am21_1 = Synthetic_Natural_Gas.AM21()
        am6_1 = Synthetic_Natural_Gas.AM6()
        var_1 = mult(am21_1, am6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AN24():
    # 'Synthetic_Natural_Gas'!AN24
    value = 1212537.6506
    formula = "=AN21*AN6"
    @eval_fn
    def AN24():
        an21_1 = Synthetic_Natural_Gas.AN21()
        an6_1 = Synthetic_Natural_Gas.AN6()
        var_1 = mult(an21_1, an6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AO24():
    # 'Synthetic_Natural_Gas'!AO24
    value = 1154164.15663
    formula = "=AO21*AO6"
    @eval_fn
    def AO24():
        ao21_1 = Synthetic_Natural_Gas.AO21()
        ao6_1 = Synthetic_Natural_Gas.AO6()
        var_1 = mult(ao21_1, ao6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AP24():
    # 'Synthetic_Natural_Gas'!AP24
    value = 1203094.87952
    formula = "=AP21*AP6"
    @eval_fn
    def AP24():
        ap21_1 = Synthetic_Natural_Gas.AP21()
        ap6_1 = Synthetic_Natural_Gas.AP6()
        var_1 = mult(ap21_1, ap6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AQ24():
    # 'Synthetic_Natural_Gas'!AQ24
    value = 1238719.87952
    formula = "=AQ21*AQ6"
    @eval_fn
    def AQ24():
        aq21_1 = Synthetic_Natural_Gas.AQ21()
        aq6_1 = Synthetic_Natural_Gas.AQ6()
        var_1 = mult(aq21_1, aq6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AR24():
    # 'Synthetic_Natural_Gas'!AR24
    value = 1276920.18072
    formula = "=AR21*AR6"
    @eval_fn
    def AR24():
        ar21_1 = Synthetic_Natural_Gas.AR21()
        ar6_1 = Synthetic_Natural_Gas.AR6()
        var_1 = mult(ar21_1, ar6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AS24():
    # 'Synthetic_Natural_Gas'!AS24
    value = 1253313.25301
    formula = "=AS21*AS6"
    @eval_fn
    def AS24():
        as21_1 = Synthetic_Natural_Gas.AS21()
        as6_1 = Synthetic_Natural_Gas.AS6()
        var_1 = mult(as21_1, as6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AT24():
    # 'Synthetic_Natural_Gas'!AT24
    value = 1243870.48193
    formula = "=AT21*AT6"
    @eval_fn
    def AT24():
        at21_1 = Synthetic_Natural_Gas.AT21()
        at6_1 = Synthetic_Natural_Gas.AT6()
        var_1 = mult(at21_1, at6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AU24():
    # 'Synthetic_Natural_Gas'!AU24
    value = 1227989.45783
    formula = "=AU21*AU6"
    @eval_fn
    def AU24():
        au21_1 = Synthetic_Natural_Gas.AU21()
        au6_1 = Synthetic_Natural_Gas.AU6()
        var_1 = mult(au21_1, au6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AV24():
    # 'Synthetic_Natural_Gas'!AV24
    value = 1247733.43373
    formula = "=AV21*AV6"
    @eval_fn
    def AV24():
        av21_1 = Synthetic_Natural_Gas.AV21()
        av6_1 = Synthetic_Natural_Gas.AV6()
        var_1 = mult(av21_1, av6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AW24():
    # 'Synthetic_Natural_Gas'!AW24
    value = 1243870.48193
    formula = "=AW21*AW6"
    @eval_fn
    def AW24():
        aw21_1 = Synthetic_Natural_Gas.AW21()
        aw6_1 = Synthetic_Natural_Gas.AW6()
        var_1 = mult(aw21_1, aw6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AX24():
    # 'Synthetic_Natural_Gas'!AX24
    value = 1250737.95181
    formula = "=AX21*AX6"
    @eval_fn
    def AX24():
        ax21_1 = Synthetic_Natural_Gas.AX21()
        ax6_1 = Synthetic_Natural_Gas.AX6()
        var_1 = mult(ax21_1, ax6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AY24():
    # 'Synthetic_Natural_Gas'!AY24
    value = 1268765.06024
    formula = "=AY21*AY6"
    @eval_fn
    def AY24():
        ay21_1 = Synthetic_Natural_Gas.AY21()
        ay6_1 = Synthetic_Natural_Gas.AY6()
        var_1 = mult(ay21_1, ay6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class AZ24():
    # 'Synthetic_Natural_Gas'!AZ24
    value = 1209103.91566
    formula = "=AZ21*AZ6"
    @eval_fn
    def AZ24():
        az21_1 = Synthetic_Natural_Gas.AZ21()
        az6_1 = Synthetic_Natural_Gas.AZ6()
        var_1 = mult(az21_1, az6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BA24():
    # 'Synthetic_Natural_Gas'!BA24
    value = 1164036.14458
    formula = "=BA21*BA6"
    @eval_fn
    def BA24():
        ba21_1 = Synthetic_Natural_Gas.BA21()
        ba6_1 = Synthetic_Natural_Gas.BA6()
        var_1 = mult(ba21_1, ba6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BB24():
    # 'Synthetic_Natural_Gas'!BB24
    value = 1172620.48193
    formula = "=BB21*BB6"
    @eval_fn
    def BB24():
        bb21_1 = Synthetic_Natural_Gas.BB21()
        bb6_1 = Synthetic_Natural_Gas.BB6()
        var_1 = mult(bb21_1, bb6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BC24():
    # 'Synthetic_Natural_Gas'!BC24
    value = 1177771.08434
    formula = "=BC21*BC6"
    @eval_fn
    def BC24():
        bc21_1 = Synthetic_Natural_Gas.BC21()
        bc6_1 = Synthetic_Natural_Gas.BC6()
        var_1 = mult(bc21_1, bc6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BD24():
    # 'Synthetic_Natural_Gas'!BD24
    value = 1207387.04819
    formula = "=BD21*BD6"
    @eval_fn
    def BD24():
        bd21_1 = Synthetic_Natural_Gas.BD21()
        bd6_1 = Synthetic_Natural_Gas.BD6()
        var_1 = mult(bd21_1, bd6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BE24():
    # 'Synthetic_Natural_Gas'!BE24
    value = 1227989.45783
    formula = "=BE21*BE6"
    @eval_fn
    def BE24():
        be21_1 = Synthetic_Natural_Gas.BE21()
        be6_1 = Synthetic_Natural_Gas.BE6()
        var_1 = mult(be21_1, be6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BF24():
    # 'Synthetic_Natural_Gas'!BF24
    value = "#N/A"
    formula = "=BF21*BF6"
    @eval_fn
    def BF24():
        bf21_1 = Synthetic_Natural_Gas.BF21()
        bf6_1 = Synthetic_Natural_Gas.BF6()
        var_1 = mult(bf21_1, bf6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BG24():
    # 'Synthetic_Natural_Gas'!BG24
    value = "#N/A"
    formula = "=BG21*BG6"
    @eval_fn
    def BG24():
        bg21_1 = Synthetic_Natural_Gas.BG21()
        bg6_1 = Synthetic_Natural_Gas.BG6()
        var_1 = mult(bg21_1, bg6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BH24():
    # 'Synthetic_Natural_Gas'!BH24
    value = "#N/A"
    formula = "=BH21*BH6"
    @eval_fn
    def BH24():
        bh21_1 = Synthetic_Natural_Gas.BH21()
        bh6_1 = Synthetic_Natural_Gas.BH6()
        var_1 = mult(bh21_1, bh6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BI24():
    # 'Synthetic_Natural_Gas'!BI24
    value = "#N/A"
    formula = "=BI21*BI6"
    @eval_fn
    def BI24():
        bi21_1 = Synthetic_Natural_Gas.BI21()
        bi6_1 = Synthetic_Natural_Gas.BI6()
        var_1 = mult(bi21_1, bi6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BJ24():
    # 'Synthetic_Natural_Gas'!BJ24
    value = "#N/A"
    formula = "=BJ21*BJ6"
    @eval_fn
    def BJ24():
        bj21_1 = Synthetic_Natural_Gas.BJ21()
        bj6_1 = Synthetic_Natural_Gas.BJ6()
        var_1 = mult(bj21_1, bj6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BK24():
    # 'Synthetic_Natural_Gas'!BK24
    value = "#N/A"
    formula = "=BK21*BK6"
    @eval_fn
    def BK24():
        bk21_1 = Synthetic_Natural_Gas.BK21()
        bk6_1 = Synthetic_Natural_Gas.BK6()
        var_1 = mult(bk21_1, bk6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class BL24():
    # 'Synthetic_Natural_Gas'!BL24
    value = "#N/A"
    formula = "=BL21*BL6"
    @eval_fn
    def BL24():
        bl21_1 = Synthetic_Natural_Gas.BL21()
        bl6_1 = Synthetic_Natural_Gas.BL6()
        var_1 = mult(bl21_1, bl6_1)
        return var_1

@register(Synthetic_Natural_Gas)
class A26():
    # 'Synthetic_Natural_Gas'!A26
    value = "Upstream BTU (BTU attributable to raw materials acquisition and raw materials transport"

@register(Synthetic_Natural_Gas)
class C26():
    # 'Synthetic_Natural_Gas'!C26
    value = "Total WTW (Well-to-Tank) (kgCO2/MMBtu)"

@register(Synthetic_Natural_Gas)
class A27():
    # 'Synthetic_Natural_Gas'!A27
    value = "US"

@register(Synthetic_Natural_Gas)
class B27():
    # 'Synthetic_Natural_Gas'!B27
    value = "Mmbtu"

@register(Synthetic_Natural_Gas)
class D27():
    # 'Synthetic_Natural_Gas'!D27
    value = 0
    formula = "=IF(D24=0,0,D24/D6)"
    @eval_fn
    def D27():
        d24_1 = Synthetic_Natural_Gas.D24()
        var_1 = equal(d24_1, 0)
        d24_2 = Synthetic_Natural_Gas.D24()
        d6_1 = Synthetic_Natural_Gas.D6()
        var_2 = divide(d24_2, d6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class E27():
    # 'Synthetic_Natural_Gas'!E27
    value = 0
    formula = "=IF(E24=0,0,E24/E6)"
    @eval_fn
    def E27():
        e24_1 = Synthetic_Natural_Gas.E24()
        var_1 = equal(e24_1, 0)
        e24_2 = Synthetic_Natural_Gas.E24()
        e6_1 = Synthetic_Natural_Gas.E6()
        var_2 = divide(e24_2, e6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class F27():
    # 'Synthetic_Natural_Gas'!F27
    value = 0
    formula = "=IF(F24=0,0,F24/F6)"
    @eval_fn
    def F27():
        f24_1 = Synthetic_Natural_Gas.F24()
        var_1 = equal(f24_1, 0)
        f24_2 = Synthetic_Natural_Gas.F24()
        f6_1 = Synthetic_Natural_Gas.F6()
        var_2 = divide(f24_2, f6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class G27():
    # 'Synthetic_Natural_Gas'!G27
    value = 0
    formula = "=IF(G24=0,0,G24/G6)"
    @eval_fn
    def G27():
        g24_1 = Synthetic_Natural_Gas.G24()
        var_1 = equal(g24_1, 0)
        g24_2 = Synthetic_Natural_Gas.G24()
        g6_1 = Synthetic_Natural_Gas.G6()
        var_2 = divide(g24_2, g6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class H27():
    # 'Synthetic_Natural_Gas'!H27
    value = 0
    formula = "=IF(H24=0,0,H24/H6)"
    @eval_fn
    def H27():
        h24_1 = Synthetic_Natural_Gas.H24()
        var_1 = equal(h24_1, 0)
        h24_2 = Synthetic_Natural_Gas.H24()
        h6_1 = Synthetic_Natural_Gas.H6()
        var_2 = divide(h24_2, h6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class I27():
    # 'Synthetic_Natural_Gas'!I27
    value = 0
    formula = "=IF(I24=0,0,I24/I6)"
    @eval_fn
    def I27():
        i24_1 = Synthetic_Natural_Gas.I24()
        var_1 = equal(i24_1, 0)
        i24_2 = Synthetic_Natural_Gas.I24()
        i6_1 = Synthetic_Natural_Gas.I6()
        var_2 = divide(i24_2, i6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class J27():
    # 'Synthetic_Natural_Gas'!J27
    value = 0
    formula = "=IF(J24=0,0,J24/J6)"
    @eval_fn
    def J27():
        j24_1 = Synthetic_Natural_Gas.J24()
        var_1 = equal(j24_1, 0)
        j24_2 = Synthetic_Natural_Gas.J24()
        j6_1 = Synthetic_Natural_Gas.J6()
        var_2 = divide(j24_2, j6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class K27():
    # 'Synthetic_Natural_Gas'!K27
    value = 0
    formula = "=IF(K24=0,0,K24/K6)"
    @eval_fn
    def K27():
        k24_1 = Synthetic_Natural_Gas.K24()
        var_1 = equal(k24_1, 0)
        k24_2 = Synthetic_Natural_Gas.K24()
        k6_1 = Synthetic_Natural_Gas.K6()
        var_2 = divide(k24_2, k6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class L27():
    # 'Synthetic_Natural_Gas'!L27
    value = 0
    formula = "=IF(L24=0,0,L24/L6)"
    @eval_fn
    def L27():
        l24_1 = Synthetic_Natural_Gas.L24()
        var_1 = equal(l24_1, 0)
        l24_2 = Synthetic_Natural_Gas.L24()
        l6_1 = Synthetic_Natural_Gas.L6()
        var_2 = divide(l24_2, l6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class M27():
    # 'Synthetic_Natural_Gas'!M27
    value = 0
    formula = "=IF(M24=0,0,M24/M6)"
    @eval_fn
    def M27():
        m24_1 = Synthetic_Natural_Gas.M24()
        var_1 = equal(m24_1, 0)
        m24_2 = Synthetic_Natural_Gas.M24()
        m6_1 = Synthetic_Natural_Gas.M6()
        var_2 = divide(m24_2, m6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class N27():
    # 'Synthetic_Natural_Gas'!N27
    value = 0
    formula = "=IF(N24=0,0,N24/N6)"
    @eval_fn
    def N27():
        n24_1 = Synthetic_Natural_Gas.N24()
        var_1 = equal(n24_1, 0)
        n24_2 = Synthetic_Natural_Gas.N24()
        n6_1 = Synthetic_Natural_Gas.N6()
        var_2 = divide(n24_2, n6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class O27():
    # 'Synthetic_Natural_Gas'!O27
    value = 0
    formula = "=IF(O24=0,0,O24/O6)"
    @eval_fn
    def O27():
        o24_1 = Synthetic_Natural_Gas.O24()
        var_1 = equal(o24_1, 0)
        o24_2 = Synthetic_Natural_Gas.O24()
        o6_1 = Synthetic_Natural_Gas.O6()
        var_2 = divide(o24_2, o6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class P27():
    # 'Synthetic_Natural_Gas'!P27
    value = 0
    formula = "=IF(P24=0,0,P24/P6)"
    @eval_fn
    def P27():
        p24_1 = Synthetic_Natural_Gas.P24()
        var_1 = equal(p24_1, 0)
        p24_2 = Synthetic_Natural_Gas.P24()
        p6_1 = Synthetic_Natural_Gas.P6()
        var_2 = divide(p24_2, p6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class Q27():
    # 'Synthetic_Natural_Gas'!Q27
    value = 0
    formula = "=IF(Q24=0,0,Q24/Q6)"
    @eval_fn
    def Q27():
        q24_1 = Synthetic_Natural_Gas.Q24()
        var_1 = equal(q24_1, 0)
        q24_2 = Synthetic_Natural_Gas.Q24()
        q6_1 = Synthetic_Natural_Gas.Q6()
        var_2 = divide(q24_2, q6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class R27():
    # 'Synthetic_Natural_Gas'!R27
    value = 0
    formula = "=IF(R24=0,0,R24/R6)"
    @eval_fn
    def R27():
        r24_1 = Synthetic_Natural_Gas.R24()
        var_1 = equal(r24_1, 0)
        r24_2 = Synthetic_Natural_Gas.R24()
        r6_1 = Synthetic_Natural_Gas.R6()
        var_2 = divide(r24_2, r6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class S27():
    # 'Synthetic_Natural_Gas'!S27
    value = 0
    formula = "=IF(S24=0,0,S24/S6)"
    @eval_fn
    def S27():
        s24_1 = Synthetic_Natural_Gas.S24()
        var_1 = equal(s24_1, 0)
        s24_2 = Synthetic_Natural_Gas.S24()
        s6_1 = Synthetic_Natural_Gas.S6()
        var_2 = divide(s24_2, s6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class T27():
    # 'Synthetic_Natural_Gas'!T27
    value = 0
    formula = "=IF(T24=0,0,T24/T6)"
    @eval_fn
    def T27():
        t24_1 = Synthetic_Natural_Gas.T24()
        var_1 = equal(t24_1, 0)
        t24_2 = Synthetic_Natural_Gas.T24()
        t6_1 = Synthetic_Natural_Gas.T6()
        var_2 = divide(t24_2, t6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class U27():
    # 'Synthetic_Natural_Gas'!U27
    value = 0
    formula = "=IF(U24=0,0,U24/U6)"
    @eval_fn
    def U27():
        u24_1 = Synthetic_Natural_Gas.U24()
        var_1 = equal(u24_1, 0)
        u24_2 = Synthetic_Natural_Gas.U24()
        u6_1 = Synthetic_Natural_Gas.U6()
        var_2 = divide(u24_2, u6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class V27():
    # 'Synthetic_Natural_Gas'!V27
    value = 0
    formula = "=IF(V24=0,0,V24/V6)"
    @eval_fn
    def V27():
        v24_1 = Synthetic_Natural_Gas.V24()
        var_1 = equal(v24_1, 0)
        v24_2 = Synthetic_Natural_Gas.V24()
        v6_1 = Synthetic_Natural_Gas.V6()
        var_2 = divide(v24_2, v6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class W27():
    # 'Synthetic_Natural_Gas'!W27
    value = 0
    formula = "=IF(W24=0,0,W24/W6)"
    @eval_fn
    def W27():
        w24_1 = Synthetic_Natural_Gas.W24()
        var_1 = equal(w24_1, 0)
        w24_2 = Synthetic_Natural_Gas.W24()
        w6_1 = Synthetic_Natural_Gas.W6()
        var_2 = divide(w24_2, w6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class X27():
    # 'Synthetic_Natural_Gas'!X27
    value = 0.42921686747
    formula = "=IF(X24=0,0,X24/X6)"
    @eval_fn
    def X27():
        x24_1 = Synthetic_Natural_Gas.X24()
        var_1 = equal(x24_1, 0)
        x24_2 = Synthetic_Natural_Gas.X24()
        x6_1 = Synthetic_Natural_Gas.X6()
        var_2 = divide(x24_2, x6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class Y27():
    # 'Synthetic_Natural_Gas'!Y27
    value = 0.42921686747
    formula = "=IF(Y24=0,0,Y24/Y6)"
    @eval_fn
    def Y27():
        y24_1 = Synthetic_Natural_Gas.Y24()
        var_1 = equal(y24_1, 0)
        y24_2 = Synthetic_Natural_Gas.Y24()
        y6_1 = Synthetic_Natural_Gas.Y6()
        var_2 = divide(y24_2, y6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class Z27():
    # 'Synthetic_Natural_Gas'!Z27
    value = 0.42921686747
    formula = "=IF(Z24=0,0,Z24/Z6)"
    @eval_fn
    def Z27():
        z24_1 = Synthetic_Natural_Gas.Z24()
        var_1 = equal(z24_1, 0)
        z24_2 = Synthetic_Natural_Gas.Z24()
        z6_1 = Synthetic_Natural_Gas.Z6()
        var_2 = divide(z24_2, z6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AA27():
    # 'Synthetic_Natural_Gas'!AA27
    value = 0.42921686747
    formula = "=IF(AA24=0,0,AA24/AA6)"
    @eval_fn
    def AA27():
        aa24_1 = Synthetic_Natural_Gas.AA24()
        var_1 = equal(aa24_1, 0)
        aa24_2 = Synthetic_Natural_Gas.AA24()
        aa6_1 = Synthetic_Natural_Gas.AA6()
        var_2 = divide(aa24_2, aa6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AB27():
    # 'Synthetic_Natural_Gas'!AB27
    value = 0.42921686747
    formula = "=IF(AB24=0,0,AB24/AB6)"
    @eval_fn
    def AB27():
        ab24_1 = Synthetic_Natural_Gas.AB24()
        var_1 = equal(ab24_1, 0)
        ab24_2 = Synthetic_Natural_Gas.AB24()
        ab6_1 = Synthetic_Natural_Gas.AB6()
        var_2 = divide(ab24_2, ab6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AC27():
    # 'Synthetic_Natural_Gas'!AC27
    value = 0.42921686747
    formula = "=IF(AC24=0,0,AC24/AC6)"
    @eval_fn
    def AC27():
        ac24_1 = Synthetic_Natural_Gas.AC24()
        var_1 = equal(ac24_1, 0)
        ac24_2 = Synthetic_Natural_Gas.AC24()
        ac6_1 = Synthetic_Natural_Gas.AC6()
        var_2 = divide(ac24_2, ac6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AD27():
    # 'Synthetic_Natural_Gas'!AD27
    value = 0.42921686747
    formula = "=IF(AD24=0,0,AD24/AD6)"
    @eval_fn
    def AD27():
        ad24_1 = Synthetic_Natural_Gas.AD24()
        var_1 = equal(ad24_1, 0)
        ad24_2 = Synthetic_Natural_Gas.AD24()
        ad6_1 = Synthetic_Natural_Gas.AD6()
        var_2 = divide(ad24_2, ad6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AE27():
    # 'Synthetic_Natural_Gas'!AE27
    value = 0.42921686747
    formula = "=IF(AE24=0,0,AE24/AE6)"
    @eval_fn
    def AE27():
        ae24_1 = Synthetic_Natural_Gas.AE24()
        var_1 = equal(ae24_1, 0)
        ae24_2 = Synthetic_Natural_Gas.AE24()
        ae6_1 = Synthetic_Natural_Gas.AE6()
        var_2 = divide(ae24_2, ae6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AF27():
    # 'Synthetic_Natural_Gas'!AF27
    value = 0.42921686747
    formula = "=IF(AF24=0,0,AF24/AF6)"
    @eval_fn
    def AF27():
        af24_1 = Synthetic_Natural_Gas.AF24()
        var_1 = equal(af24_1, 0)
        af24_2 = Synthetic_Natural_Gas.AF24()
        af6_1 = Synthetic_Natural_Gas.AF6()
        var_2 = divide(af24_2, af6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AG27():
    # 'Synthetic_Natural_Gas'!AG27
    value = 0.42921686747
    formula = "=IF(AG24=0,0,AG24/AG6)"
    @eval_fn
    def AG27():
        ag24_1 = Synthetic_Natural_Gas.AG24()
        var_1 = equal(ag24_1, 0)
        ag24_2 = Synthetic_Natural_Gas.AG24()
        ag6_1 = Synthetic_Natural_Gas.AG6()
        var_2 = divide(ag24_2, ag6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AH27():
    # 'Synthetic_Natural_Gas'!AH27
    value = 0.42921686747
    formula = "=IF(AH24=0,0,AH24/AH6)"
    @eval_fn
    def AH27():
        ah24_1 = Synthetic_Natural_Gas.AH24()
        var_1 = equal(ah24_1, 0)
        ah24_2 = Synthetic_Natural_Gas.AH24()
        ah6_1 = Synthetic_Natural_Gas.AH6()
        var_2 = divide(ah24_2, ah6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AI27():
    # 'Synthetic_Natural_Gas'!AI27
    value = 0.42921686747
    formula = "=IF(AI24=0,0,AI24/AI6)"
    @eval_fn
    def AI27():
        ai24_1 = Synthetic_Natural_Gas.AI24()
        var_1 = equal(ai24_1, 0)
        ai24_2 = Synthetic_Natural_Gas.AI24()
        ai6_1 = Synthetic_Natural_Gas.AI6()
        var_2 = divide(ai24_2, ai6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AJ27():
    # 'Synthetic_Natural_Gas'!AJ27
    value = 0.42921686747
    formula = "=IF(AJ24=0,0,AJ24/AJ6)"
    @eval_fn
    def AJ27():
        aj24_1 = Synthetic_Natural_Gas.AJ24()
        var_1 = equal(aj24_1, 0)
        aj24_2 = Synthetic_Natural_Gas.AJ24()
        aj6_1 = Synthetic_Natural_Gas.AJ6()
        var_2 = divide(aj24_2, aj6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AK27():
    # 'Synthetic_Natural_Gas'!AK27
    value = 0.42921686747
    formula = "=IF(AK24=0,0,AK24/AK6)"
    @eval_fn
    def AK27():
        ak24_1 = Synthetic_Natural_Gas.AK24()
        var_1 = equal(ak24_1, 0)
        ak24_2 = Synthetic_Natural_Gas.AK24()
        ak6_1 = Synthetic_Natural_Gas.AK6()
        var_2 = divide(ak24_2, ak6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AL27():
    # 'Synthetic_Natural_Gas'!AL27
    value = 0.42921686747
    formula = "=IF(AL24=0,0,AL24/AL6)"
    @eval_fn
    def AL27():
        al24_1 = Synthetic_Natural_Gas.AL24()
        var_1 = equal(al24_1, 0)
        al24_2 = Synthetic_Natural_Gas.AL24()
        al6_1 = Synthetic_Natural_Gas.AL6()
        var_2 = divide(al24_2, al6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AM27():
    # 'Synthetic_Natural_Gas'!AM27
    value = 0.42921686747
    formula = "=IF(AM24=0,0,AM24/AM6)"
    @eval_fn
    def AM27():
        am24_1 = Synthetic_Natural_Gas.AM24()
        var_1 = equal(am24_1, 0)
        am24_2 = Synthetic_Natural_Gas.AM24()
        am6_1 = Synthetic_Natural_Gas.AM6()
        var_2 = divide(am24_2, am6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AN27():
    # 'Synthetic_Natural_Gas'!AN27
    value = 0.42921686747
    formula = "=IF(AN24=0,0,AN24/AN6)"
    @eval_fn
    def AN27():
        an24_1 = Synthetic_Natural_Gas.AN24()
        var_1 = equal(an24_1, 0)
        an24_2 = Synthetic_Natural_Gas.AN24()
        an6_1 = Synthetic_Natural_Gas.AN6()
        var_2 = divide(an24_2, an6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AO27():
    # 'Synthetic_Natural_Gas'!AO27
    value = 0.42921686747
    formula = "=IF(AO24=0,0,AO24/AO6)"
    @eval_fn
    def AO27():
        ao24_1 = Synthetic_Natural_Gas.AO24()
        var_1 = equal(ao24_1, 0)
        ao24_2 = Synthetic_Natural_Gas.AO24()
        ao6_1 = Synthetic_Natural_Gas.AO6()
        var_2 = divide(ao24_2, ao6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AP27():
    # 'Synthetic_Natural_Gas'!AP27
    value = 0.42921686747
    formula = "=IF(AP24=0,0,AP24/AP6)"
    @eval_fn
    def AP27():
        ap24_1 = Synthetic_Natural_Gas.AP24()
        var_1 = equal(ap24_1, 0)
        ap24_2 = Synthetic_Natural_Gas.AP24()
        ap6_1 = Synthetic_Natural_Gas.AP6()
        var_2 = divide(ap24_2, ap6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AQ27():
    # 'Synthetic_Natural_Gas'!AQ27
    value = 0.42921686747
    formula = "=IF(AQ24=0,0,AQ24/AQ6)"
    @eval_fn
    def AQ27():
        aq24_1 = Synthetic_Natural_Gas.AQ24()
        var_1 = equal(aq24_1, 0)
        aq24_2 = Synthetic_Natural_Gas.AQ24()
        aq6_1 = Synthetic_Natural_Gas.AQ6()
        var_2 = divide(aq24_2, aq6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AR27():
    # 'Synthetic_Natural_Gas'!AR27
    value = 0.42921686747
    formula = "=IF(AR24=0,0,AR24/AR6)"
    @eval_fn
    def AR27():
        ar24_1 = Synthetic_Natural_Gas.AR24()
        var_1 = equal(ar24_1, 0)
        ar24_2 = Synthetic_Natural_Gas.AR24()
        ar6_1 = Synthetic_Natural_Gas.AR6()
        var_2 = divide(ar24_2, ar6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AS27():
    # 'Synthetic_Natural_Gas'!AS27
    value = 0.42921686747
    formula = "=IF(AS24=0,0,AS24/AS6)"
    @eval_fn
    def AS27():
        as24_1 = Synthetic_Natural_Gas.AS24()
        var_1 = equal(as24_1, 0)
        as24_2 = Synthetic_Natural_Gas.AS24()
        as6_1 = Synthetic_Natural_Gas.AS6()
        var_2 = divide(as24_2, as6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AT27():
    # 'Synthetic_Natural_Gas'!AT27
    value = 0.42921686747
    formula = "=IF(AT24=0,0,AT24/AT6)"
    @eval_fn
    def AT27():
        at24_1 = Synthetic_Natural_Gas.AT24()
        var_1 = equal(at24_1, 0)
        at24_2 = Synthetic_Natural_Gas.AT24()
        at6_1 = Synthetic_Natural_Gas.AT6()
        var_2 = divide(at24_2, at6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AU27():
    # 'Synthetic_Natural_Gas'!AU27
    value = 0.42921686747
    formula = "=IF(AU24=0,0,AU24/AU6)"
    @eval_fn
    def AU27():
        au24_1 = Synthetic_Natural_Gas.AU24()
        var_1 = equal(au24_1, 0)
        au24_2 = Synthetic_Natural_Gas.AU24()
        au6_1 = Synthetic_Natural_Gas.AU6()
        var_2 = divide(au24_2, au6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AV27():
    # 'Synthetic_Natural_Gas'!AV27
    value = 0.42921686747
    formula = "=IF(AV24=0,0,AV24/AV6)"
    @eval_fn
    def AV27():
        av24_1 = Synthetic_Natural_Gas.AV24()
        var_1 = equal(av24_1, 0)
        av24_2 = Synthetic_Natural_Gas.AV24()
        av6_1 = Synthetic_Natural_Gas.AV6()
        var_2 = divide(av24_2, av6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AW27():
    # 'Synthetic_Natural_Gas'!AW27
    value = 0.42921686747
    formula = "=IF(AW24=0,0,AW24/AW6)"
    @eval_fn
    def AW27():
        aw24_1 = Synthetic_Natural_Gas.AW24()
        var_1 = equal(aw24_1, 0)
        aw24_2 = Synthetic_Natural_Gas.AW24()
        aw6_1 = Synthetic_Natural_Gas.AW6()
        var_2 = divide(aw24_2, aw6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AX27():
    # 'Synthetic_Natural_Gas'!AX27
    value = 0.42921686747
    formula = "=IF(AX24=0,0,AX24/AX6)"
    @eval_fn
    def AX27():
        ax24_1 = Synthetic_Natural_Gas.AX24()
        var_1 = equal(ax24_1, 0)
        ax24_2 = Synthetic_Natural_Gas.AX24()
        ax6_1 = Synthetic_Natural_Gas.AX6()
        var_2 = divide(ax24_2, ax6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AY27():
    # 'Synthetic_Natural_Gas'!AY27
    value = 0.42921686747
    formula = "=IF(AY24=0,0,AY24/AY6)"
    @eval_fn
    def AY27():
        ay24_1 = Synthetic_Natural_Gas.AY24()
        var_1 = equal(ay24_1, 0)
        ay24_2 = Synthetic_Natural_Gas.AY24()
        ay6_1 = Synthetic_Natural_Gas.AY6()
        var_2 = divide(ay24_2, ay6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class AZ27():
    # 'Synthetic_Natural_Gas'!AZ27
    value = 0.42921686747
    formula = "=IF(AZ24=0,0,AZ24/AZ6)"
    @eval_fn
    def AZ27():
        az24_1 = Synthetic_Natural_Gas.AZ24()
        var_1 = equal(az24_1, 0)
        az24_2 = Synthetic_Natural_Gas.AZ24()
        az6_1 = Synthetic_Natural_Gas.AZ6()
        var_2 = divide(az24_2, az6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BA27():
    # 'Synthetic_Natural_Gas'!BA27
    value = 0.42921686747
    formula = "=IF(BA24=0,0,BA24/BA6)"
    @eval_fn
    def BA27():
        ba24_1 = Synthetic_Natural_Gas.BA24()
        var_1 = equal(ba24_1, 0)
        ba24_2 = Synthetic_Natural_Gas.BA24()
        ba6_1 = Synthetic_Natural_Gas.BA6()
        var_2 = divide(ba24_2, ba6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BB27():
    # 'Synthetic_Natural_Gas'!BB27
    value = 0.42921686747
    formula = "=IF(BB24=0,0,BB24/BB6)"
    @eval_fn
    def BB27():
        bb24_1 = Synthetic_Natural_Gas.BB24()
        var_1 = equal(bb24_1, 0)
        bb24_2 = Synthetic_Natural_Gas.BB24()
        bb6_1 = Synthetic_Natural_Gas.BB6()
        var_2 = divide(bb24_2, bb6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BC27():
    # 'Synthetic_Natural_Gas'!BC27
    value = 0.42921686747
    formula = "=IF(BC24=0,0,BC24/BC6)"
    @eval_fn
    def BC27():
        bc24_1 = Synthetic_Natural_Gas.BC24()
        var_1 = equal(bc24_1, 0)
        bc24_2 = Synthetic_Natural_Gas.BC24()
        bc6_1 = Synthetic_Natural_Gas.BC6()
        var_2 = divide(bc24_2, bc6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BD27():
    # 'Synthetic_Natural_Gas'!BD27
    value = 0.42921686747
    formula = "=IF(BD24=0,0,BD24/BD6)"
    @eval_fn
    def BD27():
        bd24_1 = Synthetic_Natural_Gas.BD24()
        var_1 = equal(bd24_1, 0)
        bd24_2 = Synthetic_Natural_Gas.BD24()
        bd6_1 = Synthetic_Natural_Gas.BD6()
        var_2 = divide(bd24_2, bd6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BE27():
    # 'Synthetic_Natural_Gas'!BE27
    value = 0.42921686747
    formula = "=IF(BE24=0,0,BE24/BE6)"
    @eval_fn
    def BE27():
        be24_1 = Synthetic_Natural_Gas.BE24()
        var_1 = equal(be24_1, 0)
        be24_2 = Synthetic_Natural_Gas.BE24()
        be6_1 = Synthetic_Natural_Gas.BE6()
        var_2 = divide(be24_2, be6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BF27():
    # 'Synthetic_Natural_Gas'!BF27
    value = "#N/A"
    formula = "=IF(BF24=0,0,BF24/BF6)"
    @eval_fn
    def BF27():
        bf24_1 = Synthetic_Natural_Gas.BF24()
        var_1 = equal(bf24_1, 0)
        bf24_2 = Synthetic_Natural_Gas.BF24()
        bf6_1 = Synthetic_Natural_Gas.BF6()
        var_2 = divide(bf24_2, bf6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BG27():
    # 'Synthetic_Natural_Gas'!BG27
    value = "#N/A"
    formula = "=IF(BG24=0,0,BG24/BG6)"
    @eval_fn
    def BG27():
        bg24_1 = Synthetic_Natural_Gas.BG24()
        var_1 = equal(bg24_1, 0)
        bg24_2 = Synthetic_Natural_Gas.BG24()
        bg6_1 = Synthetic_Natural_Gas.BG6()
        var_2 = divide(bg24_2, bg6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BH27():
    # 'Synthetic_Natural_Gas'!BH27
    value = "#N/A"
    formula = "=IF(BH24=0,0,BH24/BH6)"
    @eval_fn
    def BH27():
        bh24_1 = Synthetic_Natural_Gas.BH24()
        var_1 = equal(bh24_1, 0)
        bh24_2 = Synthetic_Natural_Gas.BH24()
        bh6_1 = Synthetic_Natural_Gas.BH6()
        var_2 = divide(bh24_2, bh6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BI27():
    # 'Synthetic_Natural_Gas'!BI27
    value = "#N/A"
    formula = "=IF(BI24=0,0,BI24/BI6)"
    @eval_fn
    def BI27():
        bi24_1 = Synthetic_Natural_Gas.BI24()
        var_1 = equal(bi24_1, 0)
        bi24_2 = Synthetic_Natural_Gas.BI24()
        bi6_1 = Synthetic_Natural_Gas.BI6()
        var_2 = divide(bi24_2, bi6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BJ27():
    # 'Synthetic_Natural_Gas'!BJ27
    value = "#N/A"
    formula = "=IF(BJ24=0,0,BJ24/BJ6)"
    @eval_fn
    def BJ27():
        bj24_1 = Synthetic_Natural_Gas.BJ24()
        var_1 = equal(bj24_1, 0)
        bj24_2 = Synthetic_Natural_Gas.BJ24()
        bj6_1 = Synthetic_Natural_Gas.BJ6()
        var_2 = divide(bj24_2, bj6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BK27():
    # 'Synthetic_Natural_Gas'!BK27
    value = "#N/A"
    formula = "=IF(BK24=0,0,BK24/BK6)"
    @eval_fn
    def BK27():
        bk24_1 = Synthetic_Natural_Gas.BK24()
        var_1 = equal(bk24_1, 0)
        bk24_2 = Synthetic_Natural_Gas.BK24()
        bk6_1 = Synthetic_Natural_Gas.BK6()
        var_2 = divide(bk24_2, bk6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Synthetic_Natural_Gas)
class BL27():
    # 'Synthetic_Natural_Gas'!BL27
    value = "#N/A"
    formula = "=IF(BL24=0,0,BL24/BL6)"
    @eval_fn
    def BL27():
        bl24_1 = Synthetic_Natural_Gas.BL24()
        var_1 = equal(bl24_1, 0)
        bl24_2 = Synthetic_Natural_Gas.BL24()
        bl6_1 = Synthetic_Natural_Gas.BL6()
        var_2 = divide(bl24_2, bl6_1)
        var_3 = IF(var_1, 0, var_2)
        return var_3