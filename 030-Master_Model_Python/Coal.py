# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Coal = Worksheet('Coal', 10, 10)



@register(Coal)
class B4():
    # 'Coal'!B4
    value = "unit"

@register(Coal)
class C4():
    # 'Coal'!C4
    value = "source"

@register(Coal)
class E4():
    # 'Coal'!E4
    value = 1961

@register(Coal)
class F4():
    # 'Coal'!F4
    value = 1962

@register(Coal)
class G4():
    # 'Coal'!G4
    value = 1963

@register(Coal)
class H4():
    # 'Coal'!H4
    value = 1964

@register(Coal)
class I4():
    # 'Coal'!I4
    value = 1965

@register(Coal)
class J4():
    # 'Coal'!J4
    value = 1966

@register(Coal)
class K4():
    # 'Coal'!K4
    value = 1967

@register(Coal)
class L4():
    # 'Coal'!L4
    value = 1968

@register(Coal)
class M4():
    # 'Coal'!M4
    value = 1969

@register(Coal)
class N4():
    # 'Coal'!N4
    value = 1970

@register(Coal)
class O4():
    # 'Coal'!O4
    value = 1971

@register(Coal)
class P4():
    # 'Coal'!P4
    value = 1972

@register(Coal)
class Q4():
    # 'Coal'!Q4
    value = 1973

@register(Coal)
class R4():
    # 'Coal'!R4
    value = 1974

@register(Coal)
class S4():
    # 'Coal'!S4
    value = 1975

@register(Coal)
class T4():
    # 'Coal'!T4
    value = 1976

@register(Coal)
class U4():
    # 'Coal'!U4
    value = 1977

@register(Coal)
class V4():
    # 'Coal'!V4
    value = 1978

@register(Coal)
class W4():
    # 'Coal'!W4
    value = 1979

@register(Coal)
class X4():
    # 'Coal'!X4
    value = 1980

@register(Coal)
class Y4():
    # 'Coal'!Y4
    value = 1981

@register(Coal)
class Z4():
    # 'Coal'!Z4
    value = 1982

@register(Coal)
class AA4():
    # 'Coal'!AA4
    value = 1983

@register(Coal)
class AB4():
    # 'Coal'!AB4
    value = 1984

@register(Coal)
class AC4():
    # 'Coal'!AC4
    value = 1985

@register(Coal)
class AD4():
    # 'Coal'!AD4
    value = 1986

@register(Coal)
class AE4():
    # 'Coal'!AE4
    value = 1987

@register(Coal)
class AF4():
    # 'Coal'!AF4
    value = 1988

@register(Coal)
class AG4():
    # 'Coal'!AG4
    value = 1989

@register(Coal)
class AH4():
    # 'Coal'!AH4
    value = 1990

@register(Coal)
class AI4():
    # 'Coal'!AI4
    value = 1991

@register(Coal)
class AJ4():
    # 'Coal'!AJ4
    value = 1992

@register(Coal)
class AK4():
    # 'Coal'!AK4
    value = 1993

@register(Coal)
class AL4():
    # 'Coal'!AL4
    value = 1994

@register(Coal)
class AM4():
    # 'Coal'!AM4
    value = 1995

@register(Coal)
class AN4():
    # 'Coal'!AN4
    value = 1996

@register(Coal)
class AO4():
    # 'Coal'!AO4
    value = 1997

@register(Coal)
class AP4():
    # 'Coal'!AP4
    value = 1998

@register(Coal)
class AQ4():
    # 'Coal'!AQ4
    value = 1999

@register(Coal)
class AR4():
    # 'Coal'!AR4
    value = 2000

@register(Coal)
class AS4():
    # 'Coal'!AS4
    value = 2001

@register(Coal)
class AT4():
    # 'Coal'!AT4
    value = 2002

@register(Coal)
class AU4():
    # 'Coal'!AU4
    value = 2003

@register(Coal)
class AV4():
    # 'Coal'!AV4
    value = 2004

@register(Coal)
class AW4():
    # 'Coal'!AW4
    value = 2005

@register(Coal)
class AX4():
    # 'Coal'!AX4
    value = 2006

@register(Coal)
class AY4():
    # 'Coal'!AY4
    value = 2007

@register(Coal)
class AZ4():
    # 'Coal'!AZ4
    value = 2008

@register(Coal)
class BA4():
    # 'Coal'!BA4
    value = 2009

@register(Coal)
class BB4():
    # 'Coal'!BB4
    value = 2010

@register(Coal)
class BC4():
    # 'Coal'!BC4
    value = 2011

@register(Coal)
class BD4():
    # 'Coal'!BD4
    value = 2012

@register(Coal)
class BE4():
    # 'Coal'!BE4
    value = 2013

@register(Coal)
class BF4():
    # 'Coal'!BF4
    value = 2014

@register(Coal)
class BG4():
    # 'Coal'!BG4
    value = 2015

@register(Coal)
class BH4():
    # 'Coal'!BH4
    value = 2016

@register(Coal)
class BI4():
    # 'Coal'!BI4
    value = 2017

@register(Coal)
class BJ4():
    # 'Coal'!BJ4
    value = 2018

@register(Coal)
class BK4():
    # 'Coal'!BK4
    value = 2019

@register(Coal)
class BL4():
    # 'Coal'!BL4
    value = 2020

@register(Coal)
class A5():
    # 'Coal'!A5
    value = "Total Coal Consumption (MMBtu)"

@register(Coal)
class A6():
    # 'Coal'!A6
    value = "Total Coal Consumption (MMBtu)"

@register(Coal)
class B6():
    # 'Coal'!B6
    value = "MMBtu"

@register(Coal)
class E6():
    # 'Coal'!E6
    value = 0
    formula = "='EIA Consumption'!F32*1000"
    @eval_fn
    def E6():
        f32_1 = EIA_Consumption.F32()
        var_1 = mult(f32_1, 1000)
        return var_1

@register(Coal)
class F6():
    # 'Coal'!F6
    value = 0
    formula = "='EIA Consumption'!G32*1000"
    @eval_fn
    def F6():
        g32_1 = EIA_Consumption.G32()
        var_1 = mult(g32_1, 1000)
        return var_1

@register(Coal)
class G6():
    # 'Coal'!G6
    value = 0
    formula = "='EIA Consumption'!H32*1000"
    @eval_fn
    def G6():
        h32_1 = EIA_Consumption.H32()
        var_1 = mult(h32_1, 1000)
        return var_1

@register(Coal)
class H6():
    # 'Coal'!H6
    value = 0
    formula = "='EIA Consumption'!I32*1000"
    @eval_fn
    def H6():
        i32_1 = EIA_Consumption.I32()
        var_1 = mult(i32_1, 1000)
        return var_1

@register(Coal)
class I6():
    # 'Coal'!I6
    value = 0
    formula = "='EIA Consumption'!J32*1000"
    @eval_fn
    def I6():
        j32_1 = EIA_Consumption.J32()
        var_1 = mult(j32_1, 1000)
        return var_1

@register(Coal)
class J6():
    # 'Coal'!J6
    value = 0
    formula = "='EIA Consumption'!K32*1000"
    @eval_fn
    def J6():
        k32_1 = EIA_Consumption.K32()
        var_1 = mult(k32_1, 1000)
        return var_1

@register(Coal)
class K6():
    # 'Coal'!K6
    value = 0
    formula = "='EIA Consumption'!L32*1000"
    @eval_fn
    def K6():
        l32_1 = EIA_Consumption.L32()
        var_1 = mult(l32_1, 1000)
        return var_1

@register(Coal)
class L6():
    # 'Coal'!L6
    value = 0
    formula = "='EIA Consumption'!M32*1000"
    @eval_fn
    def L6():
        m32_1 = EIA_Consumption.M32()
        var_1 = mult(m32_1, 1000)
        return var_1

@register(Coal)
class M6():
    # 'Coal'!M6
    value = 0
    formula = "='EIA Consumption'!N32*1000"
    @eval_fn
    def M6():
        n32_1 = EIA_Consumption.N32()
        var_1 = mult(n32_1, 1000)
        return var_1

@register(Coal)
class N6():
    # 'Coal'!N6
    value = 0
    formula = "='EIA Consumption'!O32*1000"
    @eval_fn
    def N6():
        o32_1 = EIA_Consumption.O32()
        var_1 = mult(o32_1, 1000)
        return var_1

@register(Coal)
class O6():
    # 'Coal'!O6
    value = 0
    formula = "='EIA Consumption'!P32*1000"
    @eval_fn
    def O6():
        p32_1 = EIA_Consumption.P32()
        var_1 = mult(p32_1, 1000)
        return var_1

@register(Coal)
class P6():
    # 'Coal'!P6
    value = 0
    formula = "='EIA Consumption'!Q32*1000"
    @eval_fn
    def P6():
        q32_1 = EIA_Consumption.Q32()
        var_1 = mult(q32_1, 1000)
        return var_1

@register(Coal)
class Q6():
    # 'Coal'!Q6
    value = 0
    formula = "='EIA Consumption'!R32*1000"
    @eval_fn
    def Q6():
        r32_1 = EIA_Consumption.R32()
        var_1 = mult(r32_1, 1000)
        return var_1

@register(Coal)
class R6():
    # 'Coal'!R6
    value = 0
    formula = "='EIA Consumption'!S32*1000"
    @eval_fn
    def R6():
        s32_1 = EIA_Consumption.S32()
        var_1 = mult(s32_1, 1000)
        return var_1

@register(Coal)
class S6():
    # 'Coal'!S6
    value = 0
    formula = "='EIA Consumption'!T32*1000"
    @eval_fn
    def S6():
        t32_1 = EIA_Consumption.T32()
        var_1 = mult(t32_1, 1000)
        return var_1

@register(Coal)
class T6():
    # 'Coal'!T6
    value = 0
    formula = "='EIA Consumption'!U32*1000"
    @eval_fn
    def T6():
        u32_1 = EIA_Consumption.U32()
        var_1 = mult(u32_1, 1000)
        return var_1

@register(Coal)
class U6():
    # 'Coal'!U6
    value = 0
    formula = "='EIA Consumption'!V32*1000"
    @eval_fn
    def U6():
        v32_1 = EIA_Consumption.V32()
        var_1 = mult(v32_1, 1000)
        return var_1

@register(Coal)
class V6():
    # 'Coal'!V6
    value = 0
    formula = "='EIA Consumption'!W32*1000"
    @eval_fn
    def V6():
        w32_1 = EIA_Consumption.W32()
        var_1 = mult(w32_1, 1000)
        return var_1

@register(Coal)
class W6():
    # 'Coal'!W6
    value = 0
    formula = "='EIA Consumption'!X32*1000"
    @eval_fn
    def W6():
        x32_1 = EIA_Consumption.X32()
        var_1 = mult(x32_1, 1000)
        return var_1

@register(Coal)
class X6():
    # 'Coal'!X6
    value = 0
    formula = "='EIA Consumption'!Y32*1000"
    @eval_fn
    def X6():
        y32_1 = EIA_Consumption.Y32()
        var_1 = mult(y32_1, 1000)
        return var_1

@register(Coal)
class Y6():
    # 'Coal'!Y6
    value = 0
    formula = "='EIA Consumption'!Z32*1000"
    @eval_fn
    def Y6():
        z32_1 = EIA_Consumption.Z32()
        var_1 = mult(z32_1, 1000)
        return var_1

@register(Coal)
class Z6():
    # 'Coal'!Z6
    value = 1149000
    formula = "='EIA Consumption'!AA32*1000"
    @eval_fn
    def Z6():
        aa32_1 = EIA_Consumption.AA32()
        var_1 = mult(aa32_1, 1000)
        return var_1

@register(Coal)
class AA6():
    # 'Coal'!AA6
    value = 1040000
    formula = "='EIA Consumption'!AB32*1000"
    @eval_fn
    def AA6():
        ab32_1 = EIA_Consumption.AB32()
        var_1 = mult(ab32_1, 1000)
        return var_1

@register(Coal)
class AB6():
    # 'Coal'!AB6
    value = 941000
    formula = "='EIA Consumption'!AC32*1000"
    @eval_fn
    def AB6():
        ac32_1 = EIA_Consumption.AC32()
        var_1 = mult(ac32_1, 1000)
        return var_1

@register(Coal)
class AC6():
    # 'Coal'!AC6
    value = 1124000
    formula = "='EIA Consumption'!AD32*1000"
    @eval_fn
    def AC6():
        ad32_1 = EIA_Consumption.AD32()
        var_1 = mult(ad32_1, 1000)
        return var_1

@register(Coal)
class AD6():
    # 'Coal'!AD6
    value = 395000
    formula = "='EIA Consumption'!AE32*1000"
    @eval_fn
    def AD6():
        ae32_1 = EIA_Consumption.AE32()
        var_1 = mult(ae32_1, 1000)
        return var_1

@register(Coal)
class AE6():
    # 'Coal'!AE6
    value = 1573000
    formula = "='EIA Consumption'!AF32*1000"
    @eval_fn
    def AE6():
        af32_1 = EIA_Consumption.AF32()
        var_1 = mult(af32_1, 1000)
        return var_1

@register(Coal)
class AF6():
    # 'Coal'!AF6
    value = 1242000
    formula = "='EIA Consumption'!AG32*1000"
    @eval_fn
    def AF6():
        ag32_1 = EIA_Consumption.AG32()
        var_1 = mult(ag32_1, 1000)
        return var_1

@register(Coal)
class AG6():
    # 'Coal'!AG6
    value = 795000
    formula = "='EIA Consumption'!AH32*1000"
    @eval_fn
    def AG6():
        ah32_1 = EIA_Consumption.AH32()
        var_1 = mult(ah32_1, 1000)
        return var_1

@register(Coal)
class AH6():
    # 'Coal'!AH6
    value = 721000
    formula = "='EIA Consumption'!AI32*1000"
    @eval_fn
    def AH6():
        ai32_1 = EIA_Consumption.AI32()
        var_1 = mult(ai32_1, 1000)
        return var_1

@register(Coal)
class AI6():
    # 'Coal'!AI6
    value = 1063000
    formula = "='EIA Consumption'!AJ32*1000"
    @eval_fn
    def AI6():
        aj32_1 = EIA_Consumption.AJ32()
        var_1 = mult(aj32_1, 1000)
        return var_1

@register(Coal)
class AJ6():
    # 'Coal'!AJ6
    value = 6750000
    formula = "='EIA Consumption'!AK32*1000"
    @eval_fn
    def AJ6():
        ak32_1 = EIA_Consumption.AK32()
        var_1 = mult(ak32_1, 1000)
        return var_1

@register(Coal)
class AK6():
    # 'Coal'!AK6
    value = 15575000
    formula = "='EIA Consumption'!AL32*1000"
    @eval_fn
    def AK6():
        al32_1 = EIA_Consumption.AL32()
        var_1 = mult(al32_1, 1000)
        return var_1

@register(Coal)
class AL6():
    # 'Coal'!AL6
    value = 15740000
    formula = "='EIA Consumption'!AM32*1000"
    @eval_fn
    def AL6():
        am32_1 = EIA_Consumption.AM32()
        var_1 = mult(am32_1, 1000)
        return var_1

@register(Coal)
class AM6():
    # 'Coal'!AM6
    value = 19914000
    formula = "='EIA Consumption'!AN32*1000"
    @eval_fn
    def AM6():
        an32_1 = EIA_Consumption.AN32()
        var_1 = mult(an32_1, 1000)
        return var_1

@register(Coal)
class AN6():
    # 'Coal'!AN6
    value = 20371000
    formula = "='EIA Consumption'!AO32*1000"
    @eval_fn
    def AN6():
        ao32_1 = EIA_Consumption.AO32()
        var_1 = mult(ao32_1, 1000)
        return var_1

@register(Coal)
class AO6():
    # 'Coal'!AO6
    value = 20513000
    formula = "='EIA Consumption'!AP32*1000"
    @eval_fn
    def AO6():
        ap32_1 = EIA_Consumption.AP32()
        var_1 = mult(ap32_1, 1000)
        return var_1

@register(Coal)
class AP6():
    # 'Coal'!AP6
    value = 18223000
    formula = "='EIA Consumption'!AQ32*1000"
    @eval_fn
    def AP6():
        aq32_1 = EIA_Consumption.AQ32()
        var_1 = mult(aq32_1, 1000)
        return var_1

@register(Coal)
class AQ6():
    # 'Coal'!AQ6
    value = 17691000
    formula = "='EIA Consumption'!AR32*1000"
    @eval_fn
    def AQ6():
        ar32_1 = EIA_Consumption.AR32()
        var_1 = mult(ar32_1, 1000)
        return var_1

@register(Coal)
class AR6():
    # 'Coal'!AR6
    value = 17653000
    formula = "='EIA Consumption'!AS32*1000"
    @eval_fn
    def AR6():
        as32_1 = EIA_Consumption.AS32()
        var_1 = mult(as32_1, 1000)
        return var_1

@register(Coal)
class AS6():
    # 'Coal'!AS6
    value = 17774000
    formula = "='EIA Consumption'!AT32*1000"
    @eval_fn
    def AS6():
        at32_1 = EIA_Consumption.AT32()
        var_1 = mult(at32_1, 1000)
        return var_1

@register(Coal)
class AT6():
    # 'Coal'!AT6
    value = 16618000
    formula = "='EIA Consumption'!AU32*1000"
    @eval_fn
    def AT6():
        au32_1 = EIA_Consumption.AU32()
        var_1 = mult(au32_1, 1000)
        return var_1

@register(Coal)
class AU6():
    # 'Coal'!AU6
    value = 19256000
    formula = "='EIA Consumption'!AV32*1000"
    @eval_fn
    def AU6():
        av32_1 = EIA_Consumption.AV32()
        var_1 = mult(av32_1, 1000)
        return var_1

@register(Coal)
class AV6():
    # 'Coal'!AV6
    value = 19254000
    formula = "='EIA Consumption'!AW32*1000"
    @eval_fn
    def AV6():
        aw32_1 = EIA_Consumption.AW32()
        var_1 = mult(aw32_1, 1000)
        return var_1

@register(Coal)
class AW6():
    # 'Coal'!AW6
    value = 17956000
    formula = "='EIA Consumption'!AX32*1000"
    @eval_fn
    def AW6():
        ax32_1 = EIA_Consumption.AX32()
        var_1 = mult(ax32_1, 1000)
        return var_1

@register(Coal)
class AX6():
    # 'Coal'!AX6
    value = 17527000
    formula = "='EIA Consumption'!AY32*1000"
    @eval_fn
    def AX6():
        ay32_1 = EIA_Consumption.AY32()
        var_1 = mult(ay32_1, 1000)
        return var_1

@register(Coal)
class AY6():
    # 'Coal'!AY6
    value = 19007000
    formula = "='EIA Consumption'!AZ32*1000"
    @eval_fn
    def AY6():
        az32_1 = EIA_Consumption.AZ32()
        var_1 = mult(az32_1, 1000)
        return var_1

@register(Coal)
class AZ6():
    # 'Coal'!AZ6
    value = 20158000
    formula = "='EIA Consumption'!BA32*1000"
    @eval_fn
    def AZ6():
        ba32_1 = EIA_Consumption.BA32()
        var_1 = mult(ba32_1, 1000)
        return var_1

@register(Coal)
class BA6():
    # 'Coal'!BA6
    value = 18958000
    formula = "='EIA Consumption'!BB32*1000"
    @eval_fn
    def BA6():
        bb32_1 = EIA_Consumption.BB32()
        var_1 = mult(bb32_1, 1000)
        return var_1

@register(Coal)
class BB6():
    # 'Coal'!BB6
    value = 17117000
    formula = "='EIA Consumption'!BC32*1000"
    @eval_fn
    def BB6():
        bc32_1 = EIA_Consumption.BC32()
        var_1 = mult(bc32_1, 1000)
        return var_1

@register(Coal)
class BC6():
    # 'Coal'!BC6
    value = 16080000
    formula = "='EIA Consumption'!BD32*1000"
    @eval_fn
    def BC6():
        bd32_1 = EIA_Consumption.BD32()
        var_1 = mult(bd32_1, 1000)
        return var_1

@register(Coal)
class BD6():
    # 'Coal'!BD6
    value = 16572000
    formula = "='EIA Consumption'!BE32*1000"
    @eval_fn
    def BD6():
        be32_1 = EIA_Consumption.BE32()
        var_1 = mult(be32_1, 1000)
        return var_1

@register(Coal)
class BE6():
    # 'Coal'!BE6
    value = 15306000
    formula = "='EIA Consumption'!BF32*1000"
    @eval_fn
    def BE6():
        bf32_1 = EIA_Consumption.BF32()
        var_1 = mult(bf32_1, 1000)
        return var_1

@register(Coal)
class BF6():
    # 'Coal'!BF6
    value = "#N/A"
    formula = "='EIA Consumption'!BG32*1000"
    @eval_fn
    def BF6():
        bg32_1 = EIA_Consumption.BG32()
        var_1 = mult(bg32_1, 1000)
        return var_1

@register(Coal)
class BG6():
    # 'Coal'!BG6
    value = "#N/A"
    formula = "='EIA Consumption'!BH32*1000"
    @eval_fn
    def BG6():
        bh32_1 = EIA_Consumption.BH32()
        var_1 = mult(bh32_1, 1000)
        return var_1

@register(Coal)
class BH6():
    # 'Coal'!BH6
    value = "#N/A"
    formula = "='EIA Consumption'!BI32*1000"
    @eval_fn
    def BH6():
        bi32_1 = EIA_Consumption.BI32()
        var_1 = mult(bi32_1, 1000)
        return var_1

@register(Coal)
class BI6():
    # 'Coal'!BI6
    value = "#N/A"
    formula = "='EIA Consumption'!BJ32*1000"
    @eval_fn
    def BI6():
        bj32_1 = EIA_Consumption.BJ32()
        var_1 = mult(bj32_1, 1000)
        return var_1

@register(Coal)
class BJ6():
    # 'Coal'!BJ6
    value = "#N/A"
    formula = "='EIA Consumption'!BK32*1000"
    @eval_fn
    def BJ6():
        bk32_1 = EIA_Consumption.BK32()
        var_1 = mult(bk32_1, 1000)
        return var_1

@register(Coal)
class BK6():
    # 'Coal'!BK6
    value = "#N/A"
    formula = "='EIA Consumption'!BL32*1000"
    @eval_fn
    def BK6():
        bl32_1 = EIA_Consumption.BL32()
        var_1 = mult(bl32_1, 1000)
        return var_1

@register(Coal)
class BL6():
    # 'Coal'!BL6
    value = "#N/A"
    formula = "='EIA Consumption'!BM32*1000"
    @eval_fn
    def BL6():
        bm32_1 = EIA_Consumption.BM32()
        var_1 = mult(bm32_1, 1000)
        return var_1

@register(Coal)
class A8():
    # 'Coal'!A8
    value = "Standard coefficient Emissions (kgCO2)"

@register(Coal)
class C8():
    # 'Coal'!C8
    value = " (Gate-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A9():
    # 'Coal'!A9
    value = "US"

@register(Coal)
class B9():
    # 'Coal'!B9
    value = "kgCO2/MMBTU"

@register(Coal)
class E9():
    # 'Coal'!E9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def E9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class F9():
    # 'Coal'!F9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def F9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class G9():
    # 'Coal'!G9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def G9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class H9():
    # 'Coal'!H9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def H9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class I9():
    # 'Coal'!I9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def I9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class J9():
    # 'Coal'!J9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def J9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class K9():
    # 'Coal'!K9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def K9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class L9():
    # 'Coal'!L9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def L9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class M9():
    # 'Coal'!M9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def M9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class N9():
    # 'Coal'!N9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def N9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class O9():
    # 'Coal'!O9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def O9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class P9():
    # 'Coal'!P9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def P9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class Q9():
    # 'Coal'!Q9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def Q9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class R9():
    # 'Coal'!R9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def R9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class S9():
    # 'Coal'!S9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def S9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class T9():
    # 'Coal'!T9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def T9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class U9():
    # 'Coal'!U9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def U9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class V9():
    # 'Coal'!V9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def V9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class W9():
    # 'Coal'!W9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def W9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class X9():
    # 'Coal'!X9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def X9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class Y9():
    # 'Coal'!Y9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def Y9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class Z9():
    # 'Coal'!Z9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def Z9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AA9():
    # 'Coal'!AA9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AA9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AB9():
    # 'Coal'!AB9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AB9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AC9():
    # 'Coal'!AC9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AC9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AD9():
    # 'Coal'!AD9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AD9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AE9():
    # 'Coal'!AE9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AE9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AF9():
    # 'Coal'!AF9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AF9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AG9():
    # 'Coal'!AG9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AG9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AH9():
    # 'Coal'!AH9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AH9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AI9():
    # 'Coal'!AI9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AI9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AJ9():
    # 'Coal'!AJ9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AJ9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AK9():
    # 'Coal'!AK9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AK9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AL9():
    # 'Coal'!AL9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AL9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AM9():
    # 'Coal'!AM9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AM9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AN9():
    # 'Coal'!AN9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AN9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AO9():
    # 'Coal'!AO9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AO9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AP9():
    # 'Coal'!AP9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AP9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AQ9():
    # 'Coal'!AQ9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AQ9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AR9():
    # 'Coal'!AR9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AR9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AS9():
    # 'Coal'!AS9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AS9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AT9():
    # 'Coal'!AT9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AT9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AU9():
    # 'Coal'!AU9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AU9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AV9():
    # 'Coal'!AV9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AV9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AW9():
    # 'Coal'!AW9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AW9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AX9():
    # 'Coal'!AX9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AX9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AY9():
    # 'Coal'!AY9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AY9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class AZ9():
    # 'Coal'!AZ9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def AZ9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BA9():
    # 'Coal'!BA9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BA9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BB9():
    # 'Coal'!BB9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BB9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BC9():
    # 'Coal'!BC9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BC9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BD9():
    # 'Coal'!BD9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BD9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BE9():
    # 'Coal'!BE9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BE9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BF9():
    # 'Coal'!BF9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BF9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BG9():
    # 'Coal'!BG9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BG9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BH9():
    # 'Coal'!BH9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BH9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BI9():
    # 'Coal'!BI9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BI9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BJ9():
    # 'Coal'!BJ9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BJ9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BK9():
    # 'Coal'!BK9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BK9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class BL9():
    # 'Coal'!BL9
    value = 94.5266666667
    formula = "='Carbon Coefficients'!$D$20"
    @eval_fn
    def BL9():
        d20_1 = Carbon_Coefficients.D20()
        return d20_1

@register(Coal)
class A11():
    # 'Coal'!A11
    value = "Upstream coefficient emissions"

@register(Coal)
class C11():
    # 'Coal'!C11
    value = "(Well-to-Gate) (kgCO2/MMBtu)"

@register(Coal)
class A12():
    # 'Coal'!A12
    value = "US"

@register(Coal)
class B12():
    # 'Coal'!B12
    value = "kgCO2/MMBTU"

@register(Coal)
class E12():
    # 'Coal'!E12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def E12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class F12():
    # 'Coal'!F12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def F12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class G12():
    # 'Coal'!G12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def G12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class H12():
    # 'Coal'!H12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def H12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class I12():
    # 'Coal'!I12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def I12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class J12():
    # 'Coal'!J12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def J12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class K12():
    # 'Coal'!K12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def K12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class L12():
    # 'Coal'!L12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def L12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class M12():
    # 'Coal'!M12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def M12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class N12():
    # 'Coal'!N12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def N12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class O12():
    # 'Coal'!O12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def O12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class P12():
    # 'Coal'!P12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def P12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class Q12():
    # 'Coal'!Q12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def Q12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class R12():
    # 'Coal'!R12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def R12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class S12():
    # 'Coal'!S12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def S12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class T12():
    # 'Coal'!T12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def T12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class U12():
    # 'Coal'!U12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def U12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class V12():
    # 'Coal'!V12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def V12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class W12():
    # 'Coal'!W12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def W12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class X12():
    # 'Coal'!X12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def X12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class Y12():
    # 'Coal'!Y12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def Y12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class Z12():
    # 'Coal'!Z12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def Z12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AA12():
    # 'Coal'!AA12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AA12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AB12():
    # 'Coal'!AB12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AB12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AC12():
    # 'Coal'!AC12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AC12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AD12():
    # 'Coal'!AD12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AD12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AE12():
    # 'Coal'!AE12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AE12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AF12():
    # 'Coal'!AF12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AF12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AG12():
    # 'Coal'!AG12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AG12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AH12():
    # 'Coal'!AH12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AH12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AI12():
    # 'Coal'!AI12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AI12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AJ12():
    # 'Coal'!AJ12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AJ12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AK12():
    # 'Coal'!AK12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AK12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AL12():
    # 'Coal'!AL12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AL12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AM12():
    # 'Coal'!AM12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AM12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AN12():
    # 'Coal'!AN12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AN12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AO12():
    # 'Coal'!AO12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AO12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AP12():
    # 'Coal'!AP12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AP12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AQ12():
    # 'Coal'!AQ12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AQ12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AR12():
    # 'Coal'!AR12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AR12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AS12():
    # 'Coal'!AS12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AS12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AT12():
    # 'Coal'!AT12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AT12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AU12():
    # 'Coal'!AU12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AU12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AV12():
    # 'Coal'!AV12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AV12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AW12():
    # 'Coal'!AW12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AW12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AX12():
    # 'Coal'!AX12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AX12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AY12():
    # 'Coal'!AY12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AY12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class AZ12():
    # 'Coal'!AZ12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def AZ12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BA12():
    # 'Coal'!BA12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BA12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BB12():
    # 'Coal'!BB12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BB12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BC12():
    # 'Coal'!BC12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BC12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BD12():
    # 'Coal'!BD12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BD12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BE12():
    # 'Coal'!BE12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BE12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BF12():
    # 'Coal'!BF12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BF12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BG12():
    # 'Coal'!BG12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BG12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BH12():
    # 'Coal'!BH12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BH12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BI12():
    # 'Coal'!BI12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BI12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BJ12():
    # 'Coal'!BJ12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BJ12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BK12():
    # 'Coal'!BK12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BK12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class BL12():
    # 'Coal'!BL12
    value = 9.2
    formula = "='Carbon Coefficients'!$D$21"
    @eval_fn
    def BL12():
        d21_1 = Carbon_Coefficients.D21()
        return d21_1

@register(Coal)
class A14():
    # 'Coal'!A14
    value = "Combined Coeffiecient "

@register(Coal)
class C14():
    # 'Coal'!C14
    value = "Total WTW (Well-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A15():
    # 'Coal'!A15
    value = "US"

@register(Coal)
class B15():
    # 'Coal'!B15
    value = "kgCO2/MMBTU"

@register(Coal)
class E15():
    # 'Coal'!E15
    value = 103.726666667
    formula = "=E12+E9"
    @eval_fn
    def E15():
        e12_1 = Coal.E12()
        e9_1 = Coal.E9()
        var_1 = add(e12_1, e9_1)
        return var_1

@register(Coal)
class F15():
    # 'Coal'!F15
    value = 103.726666667
    formula = "=F12+F9"
    @eval_fn
    def F15():
        f12_1 = Coal.F12()
        f9_1 = Coal.F9()
        var_1 = add(f12_1, f9_1)
        return var_1

@register(Coal)
class G15():
    # 'Coal'!G15
    value = 103.726666667
    formula = "=G12+G9"
    @eval_fn
    def G15():
        g12_1 = Coal.G12()
        g9_1 = Coal.G9()
        var_1 = add(g12_1, g9_1)
        return var_1

@register(Coal)
class H15():
    # 'Coal'!H15
    value = 103.726666667
    formula = "=H12+H9"
    @eval_fn
    def H15():
        h12_1 = Coal.H12()
        h9_1 = Coal.H9()
        var_1 = add(h12_1, h9_1)
        return var_1

@register(Coal)
class I15():
    # 'Coal'!I15
    value = 103.726666667
    formula = "=I12+I9"
    @eval_fn
    def I15():
        i12_1 = Coal.I12()
        i9_1 = Coal.I9()
        var_1 = add(i12_1, i9_1)
        return var_1

@register(Coal)
class J15():
    # 'Coal'!J15
    value = 103.726666667
    formula = "=J12+J9"
    @eval_fn
    def J15():
        j12_1 = Coal.J12()
        j9_1 = Coal.J9()
        var_1 = add(j12_1, j9_1)
        return var_1

@register(Coal)
class K15():
    # 'Coal'!K15
    value = 103.726666667
    formula = "=K12+K9"
    @eval_fn
    def K15():
        k12_1 = Coal.K12()
        k9_1 = Coal.K9()
        var_1 = add(k12_1, k9_1)
        return var_1

@register(Coal)
class L15():
    # 'Coal'!L15
    value = 103.726666667
    formula = "=L12+L9"
    @eval_fn
    def L15():
        l12_1 = Coal.L12()
        l9_1 = Coal.L9()
        var_1 = add(l12_1, l9_1)
        return var_1

@register(Coal)
class M15():
    # 'Coal'!M15
    value = 103.726666667
    formula = "=M12+M9"
    @eval_fn
    def M15():
        m12_1 = Coal.M12()
        m9_1 = Coal.M9()
        var_1 = add(m12_1, m9_1)
        return var_1

@register(Coal)
class N15():
    # 'Coal'!N15
    value = 103.726666667
    formula = "=N12+N9"
    @eval_fn
    def N15():
        n12_1 = Coal.N12()
        n9_1 = Coal.N9()
        var_1 = add(n12_1, n9_1)
        return var_1

@register(Coal)
class O15():
    # 'Coal'!O15
    value = 103.726666667
    formula = "=O12+O9"
    @eval_fn
    def O15():
        o12_1 = Coal.O12()
        o9_1 = Coal.O9()
        var_1 = add(o12_1, o9_1)
        return var_1

@register(Coal)
class P15():
    # 'Coal'!P15
    value = 103.726666667
    formula = "=P12+P9"
    @eval_fn
    def P15():
        p12_1 = Coal.P12()
        p9_1 = Coal.P9()
        var_1 = add(p12_1, p9_1)
        return var_1

@register(Coal)
class Q15():
    # 'Coal'!Q15
    value = 103.726666667
    formula = "=Q12+Q9"
    @eval_fn
    def Q15():
        q12_1 = Coal.Q12()
        q9_1 = Coal.Q9()
        var_1 = add(q12_1, q9_1)
        return var_1

@register(Coal)
class R15():
    # 'Coal'!R15
    value = 103.726666667
    formula = "=R12+R9"
    @eval_fn
    def R15():
        r12_1 = Coal.R12()
        r9_1 = Coal.R9()
        var_1 = add(r12_1, r9_1)
        return var_1

@register(Coal)
class S15():
    # 'Coal'!S15
    value = 103.726666667
    formula = "=S12+S9"
    @eval_fn
    def S15():
        s12_1 = Coal.S12()
        s9_1 = Coal.S9()
        var_1 = add(s12_1, s9_1)
        return var_1

@register(Coal)
class T15():
    # 'Coal'!T15
    value = 103.726666667
    formula = "=T12+T9"
    @eval_fn
    def T15():
        t12_1 = Coal.T12()
        t9_1 = Coal.T9()
        var_1 = add(t12_1, t9_1)
        return var_1

@register(Coal)
class U15():
    # 'Coal'!U15
    value = 103.726666667
    formula = "=U12+U9"
    @eval_fn
    def U15():
        u12_1 = Coal.U12()
        u9_1 = Coal.U9()
        var_1 = add(u12_1, u9_1)
        return var_1

@register(Coal)
class V15():
    # 'Coal'!V15
    value = 103.726666667
    formula = "=V12+V9"
    @eval_fn
    def V15():
        v12_1 = Coal.V12()
        v9_1 = Coal.V9()
        var_1 = add(v12_1, v9_1)
        return var_1

@register(Coal)
class W15():
    # 'Coal'!W15
    value = 103.726666667
    formula = "=W12+W9"
    @eval_fn
    def W15():
        w12_1 = Coal.W12()
        w9_1 = Coal.W9()
        var_1 = add(w12_1, w9_1)
        return var_1

@register(Coal)
class X15():
    # 'Coal'!X15
    value = 103.726666667
    formula = "=X12+X9"
    @eval_fn
    def X15():
        x12_1 = Coal.X12()
        x9_1 = Coal.X9()
        var_1 = add(x12_1, x9_1)
        return var_1

@register(Coal)
class Y15():
    # 'Coal'!Y15
    value = 103.726666667
    formula = "=Y12+Y9"
    @eval_fn
    def Y15():
        y12_1 = Coal.Y12()
        y9_1 = Coal.Y9()
        var_1 = add(y12_1, y9_1)
        return var_1

@register(Coal)
class Z15():
    # 'Coal'!Z15
    value = 103.726666667
    formula = "=Z12+Z9"
    @eval_fn
    def Z15():
        z12_1 = Coal.Z12()
        z9_1 = Coal.Z9()
        var_1 = add(z12_1, z9_1)
        return var_1

@register(Coal)
class AA15():
    # 'Coal'!AA15
    value = 103.726666667
    formula = "=AA12+AA9"
    @eval_fn
    def AA15():
        aa12_1 = Coal.AA12()
        aa9_1 = Coal.AA9()
        var_1 = add(aa12_1, aa9_1)
        return var_1

@register(Coal)
class AB15():
    # 'Coal'!AB15
    value = 103.726666667
    formula = "=AB12+AB9"
    @eval_fn
    def AB15():
        ab12_1 = Coal.AB12()
        ab9_1 = Coal.AB9()
        var_1 = add(ab12_1, ab9_1)
        return var_1

@register(Coal)
class AC15():
    # 'Coal'!AC15
    value = 103.726666667
    formula = "=AC12+AC9"
    @eval_fn
    def AC15():
        ac12_1 = Coal.AC12()
        ac9_1 = Coal.AC9()
        var_1 = add(ac12_1, ac9_1)
        return var_1

@register(Coal)
class AD15():
    # 'Coal'!AD15
    value = 103.726666667
    formula = "=AD12+AD9"
    @eval_fn
    def AD15():
        ad12_1 = Coal.AD12()
        ad9_1 = Coal.AD9()
        var_1 = add(ad12_1, ad9_1)
        return var_1

@register(Coal)
class AE15():
    # 'Coal'!AE15
    value = 103.726666667
    formula = "=AE12+AE9"
    @eval_fn
    def AE15():
        ae12_1 = Coal.AE12()
        ae9_1 = Coal.AE9()
        var_1 = add(ae12_1, ae9_1)
        return var_1

@register(Coal)
class AF15():
    # 'Coal'!AF15
    value = 103.726666667
    formula = "=AF12+AF9"
    @eval_fn
    def AF15():
        af12_1 = Coal.AF12()
        af9_1 = Coal.AF9()
        var_1 = add(af12_1, af9_1)
        return var_1

@register(Coal)
class AG15():
    # 'Coal'!AG15
    value = 103.726666667
    formula = "=AG12+AG9"
    @eval_fn
    def AG15():
        ag12_1 = Coal.AG12()
        ag9_1 = Coal.AG9()
        var_1 = add(ag12_1, ag9_1)
        return var_1

@register(Coal)
class AH15():
    # 'Coal'!AH15
    value = 103.726666667
    formula = "=AH12+AH9"
    @eval_fn
    def AH15():
        ah12_1 = Coal.AH12()
        ah9_1 = Coal.AH9()
        var_1 = add(ah12_1, ah9_1)
        return var_1

@register(Coal)
class AI15():
    # 'Coal'!AI15
    value = 103.726666667
    formula = "=AI12+AI9"
    @eval_fn
    def AI15():
        ai12_1 = Coal.AI12()
        ai9_1 = Coal.AI9()
        var_1 = add(ai12_1, ai9_1)
        return var_1

@register(Coal)
class AJ15():
    # 'Coal'!AJ15
    value = 103.726666667
    formula = "=AJ12+AJ9"
    @eval_fn
    def AJ15():
        aj12_1 = Coal.AJ12()
        aj9_1 = Coal.AJ9()
        var_1 = add(aj12_1, aj9_1)
        return var_1

@register(Coal)
class AK15():
    # 'Coal'!AK15
    value = 103.726666667
    formula = "=AK12+AK9"
    @eval_fn
    def AK15():
        ak12_1 = Coal.AK12()
        ak9_1 = Coal.AK9()
        var_1 = add(ak12_1, ak9_1)
        return var_1

@register(Coal)
class AL15():
    # 'Coal'!AL15
    value = 103.726666667
    formula = "=AL12+AL9"
    @eval_fn
    def AL15():
        al12_1 = Coal.AL12()
        al9_1 = Coal.AL9()
        var_1 = add(al12_1, al9_1)
        return var_1

@register(Coal)
class AM15():
    # 'Coal'!AM15
    value = 103.726666667
    formula = "=AM12+AM9"
    @eval_fn
    def AM15():
        am12_1 = Coal.AM12()
        am9_1 = Coal.AM9()
        var_1 = add(am12_1, am9_1)
        return var_1

@register(Coal)
class AN15():
    # 'Coal'!AN15
    value = 103.726666667
    formula = "=AN12+AN9"
    @eval_fn
    def AN15():
        an12_1 = Coal.AN12()
        an9_1 = Coal.AN9()
        var_1 = add(an12_1, an9_1)
        return var_1

@register(Coal)
class AO15():
    # 'Coal'!AO15
    value = 103.726666667
    formula = "=AO12+AO9"
    @eval_fn
    def AO15():
        ao12_1 = Coal.AO12()
        ao9_1 = Coal.AO9()
        var_1 = add(ao12_1, ao9_1)
        return var_1

@register(Coal)
class AP15():
    # 'Coal'!AP15
    value = 103.726666667
    formula = "=AP12+AP9"
    @eval_fn
    def AP15():
        ap12_1 = Coal.AP12()
        ap9_1 = Coal.AP9()
        var_1 = add(ap12_1, ap9_1)
        return var_1

@register(Coal)
class AQ15():
    # 'Coal'!AQ15
    value = 103.726666667
    formula = "=AQ12+AQ9"
    @eval_fn
    def AQ15():
        aq12_1 = Coal.AQ12()
        aq9_1 = Coal.AQ9()
        var_1 = add(aq12_1, aq9_1)
        return var_1

@register(Coal)
class AR15():
    # 'Coal'!AR15
    value = 103.726666667
    formula = "=AR12+AR9"
    @eval_fn
    def AR15():
        ar12_1 = Coal.AR12()
        ar9_1 = Coal.AR9()
        var_1 = add(ar12_1, ar9_1)
        return var_1

@register(Coal)
class AS15():
    # 'Coal'!AS15
    value = 103.726666667
    formula = "=AS12+AS9"
    @eval_fn
    def AS15():
        as12_1 = Coal.AS12()
        as9_1 = Coal.AS9()
        var_1 = add(as12_1, as9_1)
        return var_1

@register(Coal)
class AT15():
    # 'Coal'!AT15
    value = 103.726666667
    formula = "=AT12+AT9"
    @eval_fn
    def AT15():
        at12_1 = Coal.AT12()
        at9_1 = Coal.AT9()
        var_1 = add(at12_1, at9_1)
        return var_1

@register(Coal)
class AU15():
    # 'Coal'!AU15
    value = 103.726666667
    formula = "=AU12+AU9"
    @eval_fn
    def AU15():
        au12_1 = Coal.AU12()
        au9_1 = Coal.AU9()
        var_1 = add(au12_1, au9_1)
        return var_1

@register(Coal)
class AV15():
    # 'Coal'!AV15
    value = 103.726666667
    formula = "=AV12+AV9"
    @eval_fn
    def AV15():
        av12_1 = Coal.AV12()
        av9_1 = Coal.AV9()
        var_1 = add(av12_1, av9_1)
        return var_1

@register(Coal)
class AW15():
    # 'Coal'!AW15
    value = 103.726666667
    formula = "=AW12+AW9"
    @eval_fn
    def AW15():
        aw12_1 = Coal.AW12()
        aw9_1 = Coal.AW9()
        var_1 = add(aw12_1, aw9_1)
        return var_1

@register(Coal)
class AX15():
    # 'Coal'!AX15
    value = 103.726666667
    formula = "=AX12+AX9"
    @eval_fn
    def AX15():
        ax12_1 = Coal.AX12()
        ax9_1 = Coal.AX9()
        var_1 = add(ax12_1, ax9_1)
        return var_1

@register(Coal)
class AY15():
    # 'Coal'!AY15
    value = 103.726666667
    formula = "=AY12+AY9"
    @eval_fn
    def AY15():
        ay12_1 = Coal.AY12()
        ay9_1 = Coal.AY9()
        var_1 = add(ay12_1, ay9_1)
        return var_1

@register(Coal)
class AZ15():
    # 'Coal'!AZ15
    value = 103.726666667
    formula = "=AZ12+AZ9"
    @eval_fn
    def AZ15():
        az12_1 = Coal.AZ12()
        az9_1 = Coal.AZ9()
        var_1 = add(az12_1, az9_1)
        return var_1

@register(Coal)
class BA15():
    # 'Coal'!BA15
    value = 103.726666667
    formula = "=BA12+BA9"
    @eval_fn
    def BA15():
        ba12_1 = Coal.BA12()
        ba9_1 = Coal.BA9()
        var_1 = add(ba12_1, ba9_1)
        return var_1

@register(Coal)
class BB15():
    # 'Coal'!BB15
    value = 103.726666667
    formula = "=BB12+BB9"
    @eval_fn
    def BB15():
        bb12_1 = Coal.BB12()
        bb9_1 = Coal.BB9()
        var_1 = add(bb12_1, bb9_1)
        return var_1

@register(Coal)
class BC15():
    # 'Coal'!BC15
    value = 103.726666667
    formula = "=BC12+BC9"
    @eval_fn
    def BC15():
        bc12_1 = Coal.BC12()
        bc9_1 = Coal.BC9()
        var_1 = add(bc12_1, bc9_1)
        return var_1

@register(Coal)
class BD15():
    # 'Coal'!BD15
    value = 103.726666667
    formula = "=BD12+BD9"
    @eval_fn
    def BD15():
        bd12_1 = Coal.BD12()
        bd9_1 = Coal.BD9()
        var_1 = add(bd12_1, bd9_1)
        return var_1

@register(Coal)
class BE15():
    # 'Coal'!BE15
    value = 103.726666667
    formula = "=BE12+BE9"
    @eval_fn
    def BE15():
        be12_1 = Coal.BE12()
        be9_1 = Coal.BE9()
        var_1 = add(be12_1, be9_1)
        return var_1

@register(Coal)
class BF15():
    # 'Coal'!BF15
    value = 103.726666667
    formula = "=BF12+BF9"
    @eval_fn
    def BF15():
        bf12_1 = Coal.BF12()
        bf9_1 = Coal.BF9()
        var_1 = add(bf12_1, bf9_1)
        return var_1

@register(Coal)
class BG15():
    # 'Coal'!BG15
    value = 103.726666667
    formula = "=BG12+BG9"
    @eval_fn
    def BG15():
        bg12_1 = Coal.BG12()
        bg9_1 = Coal.BG9()
        var_1 = add(bg12_1, bg9_1)
        return var_1

@register(Coal)
class BH15():
    # 'Coal'!BH15
    value = 103.726666667
    formula = "=BH12+BH9"
    @eval_fn
    def BH15():
        bh12_1 = Coal.BH12()
        bh9_1 = Coal.BH9()
        var_1 = add(bh12_1, bh9_1)
        return var_1

@register(Coal)
class BI15():
    # 'Coal'!BI15
    value = 103.726666667
    formula = "=BI12+BI9"
    @eval_fn
    def BI15():
        bi12_1 = Coal.BI12()
        bi9_1 = Coal.BI9()
        var_1 = add(bi12_1, bi9_1)
        return var_1

@register(Coal)
class BJ15():
    # 'Coal'!BJ15
    value = 103.726666667
    formula = "=BJ12+BJ9"
    @eval_fn
    def BJ15():
        bj12_1 = Coal.BJ12()
        bj9_1 = Coal.BJ9()
        var_1 = add(bj12_1, bj9_1)
        return var_1

@register(Coal)
class BK15():
    # 'Coal'!BK15
    value = 103.726666667
    formula = "=BK12+BK9"
    @eval_fn
    def BK15():
        bk12_1 = Coal.BK12()
        bk9_1 = Coal.BK9()
        var_1 = add(bk12_1, bk9_1)
        return var_1

@register(Coal)
class BL15():
    # 'Coal'!BL15
    value = 103.726666667
    formula = "=BL12+BL9"
    @eval_fn
    def BL15():
        bl12_1 = Coal.BL12()
        bl9_1 = Coal.BL9()
        var_1 = add(bl12_1, bl9_1)
        return var_1

@register(Coal)
class A17():
    # 'Coal'!A17
    value = "Life Cycle Emissions"

@register(Coal)
class C17():
    # 'Coal'!C17
    value = "Total WTT (Well-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A18():
    # 'Coal'!A18
    value = "US"

@register(Coal)
class B18():
    # 'Coal'!B18
    value = "kgCO2"

@register(Coal)
class C18():
    # 'Coal'!C18
    value = 103.726666667
    formula = "='Carbon Coefficients'!D22"
    @eval_fn
    def C18():
        d22_1 = Carbon_Coefficients.D22()
        return d22_1

@register(Coal)
class E18():
    # 'Coal'!E18
    value = 0
    formula = "=E6*$C$18"
    @eval_fn
    def E18():
        e6_1 = Coal.E6()
        c18_1 = Coal.C18()
        var_1 = mult(e6_1, c18_1)
        return var_1

@register(Coal)
class F18():
    # 'Coal'!F18
    value = 0
    formula = "=F6*$C$18"
    @eval_fn
    def F18():
        f6_1 = Coal.F6()
        c18_1 = Coal.C18()
        var_1 = mult(f6_1, c18_1)
        return var_1

@register(Coal)
class G18():
    # 'Coal'!G18
    value = 0
    formula = "=G6*$C$18"
    @eval_fn
    def G18():
        g6_1 = Coal.G6()
        c18_1 = Coal.C18()
        var_1 = mult(g6_1, c18_1)
        return var_1

@register(Coal)
class H18():
    # 'Coal'!H18
    value = 0
    formula = "=H6*$C$18"
    @eval_fn
    def H18():
        h6_1 = Coal.H6()
        c18_1 = Coal.C18()
        var_1 = mult(h6_1, c18_1)
        return var_1

@register(Coal)
class I18():
    # 'Coal'!I18
    value = 0
    formula = "=I6*$C$18"
    @eval_fn
    def I18():
        i6_1 = Coal.I6()
        c18_1 = Coal.C18()
        var_1 = mult(i6_1, c18_1)
        return var_1

@register(Coal)
class J18():
    # 'Coal'!J18
    value = 0
    formula = "=J6*$C$18"
    @eval_fn
    def J18():
        j6_1 = Coal.J6()
        c18_1 = Coal.C18()
        var_1 = mult(j6_1, c18_1)
        return var_1

@register(Coal)
class K18():
    # 'Coal'!K18
    value = 0
    formula = "=K6*$C$18"
    @eval_fn
    def K18():
        k6_1 = Coal.K6()
        c18_1 = Coal.C18()
        var_1 = mult(k6_1, c18_1)
        return var_1

@register(Coal)
class L18():
    # 'Coal'!L18
    value = 0
    formula = "=L6*$C$18"
    @eval_fn
    def L18():
        l6_1 = Coal.L6()
        c18_1 = Coal.C18()
        var_1 = mult(l6_1, c18_1)
        return var_1

@register(Coal)
class M18():
    # 'Coal'!M18
    value = 0
    formula = "=M6*$C$18"
    @eval_fn
    def M18():
        m6_1 = Coal.M6()
        c18_1 = Coal.C18()
        var_1 = mult(m6_1, c18_1)
        return var_1

@register(Coal)
class N18():
    # 'Coal'!N18
    value = 0
    formula = "=N6*$C$18"
    @eval_fn
    def N18():
        n6_1 = Coal.N6()
        c18_1 = Coal.C18()
        var_1 = mult(n6_1, c18_1)
        return var_1

@register(Coal)
class O18():
    # 'Coal'!O18
    value = 0
    formula = "=O6*$C$18"
    @eval_fn
    def O18():
        o6_1 = Coal.O6()
        c18_1 = Coal.C18()
        var_1 = mult(o6_1, c18_1)
        return var_1

@register(Coal)
class P18():
    # 'Coal'!P18
    value = 0
    formula = "=P6*$C$18"
    @eval_fn
    def P18():
        p6_1 = Coal.P6()
        c18_1 = Coal.C18()
        var_1 = mult(p6_1, c18_1)
        return var_1

@register(Coal)
class Q18():
    # 'Coal'!Q18
    value = 0
    formula = "=Q6*$C$18"
    @eval_fn
    def Q18():
        q6_1 = Coal.Q6()
        c18_1 = Coal.C18()
        var_1 = mult(q6_1, c18_1)
        return var_1

@register(Coal)
class R18():
    # 'Coal'!R18
    value = 0
    formula = "=R6*$C$18"
    @eval_fn
    def R18():
        r6_1 = Coal.R6()
        c18_1 = Coal.C18()
        var_1 = mult(r6_1, c18_1)
        return var_1

@register(Coal)
class S18():
    # 'Coal'!S18
    value = 0
    formula = "=S6*$C$18"
    @eval_fn
    def S18():
        s6_1 = Coal.S6()
        c18_1 = Coal.C18()
        var_1 = mult(s6_1, c18_1)
        return var_1

@register(Coal)
class T18():
    # 'Coal'!T18
    value = 0
    formula = "=T6*$C$18"
    @eval_fn
    def T18():
        t6_1 = Coal.T6()
        c18_1 = Coal.C18()
        var_1 = mult(t6_1, c18_1)
        return var_1

@register(Coal)
class U18():
    # 'Coal'!U18
    value = 0
    formula = "=U6*$C$18"
    @eval_fn
    def U18():
        u6_1 = Coal.U6()
        c18_1 = Coal.C18()
        var_1 = mult(u6_1, c18_1)
        return var_1

@register(Coal)
class V18():
    # 'Coal'!V18
    value = 0
    formula = "=V6*$C$18"
    @eval_fn
    def V18():
        v6_1 = Coal.V6()
        c18_1 = Coal.C18()
        var_1 = mult(v6_1, c18_1)
        return var_1

@register(Coal)
class W18():
    # 'Coal'!W18
    value = 0
    formula = "=W6*$C$18"
    @eval_fn
    def W18():
        w6_1 = Coal.W6()
        c18_1 = Coal.C18()
        var_1 = mult(w6_1, c18_1)
        return var_1

@register(Coal)
class X18():
    # 'Coal'!X18
    value = 0
    formula = "=X6*$C$18"
    @eval_fn
    def X18():
        x6_1 = Coal.X6()
        c18_1 = Coal.C18()
        var_1 = mult(x6_1, c18_1)
        return var_1

@register(Coal)
class Y18():
    # 'Coal'!Y18
    value = 0
    formula = "=Y6*$C$18"
    @eval_fn
    def Y18():
        y6_1 = Coal.Y6()
        c18_1 = Coal.C18()
        var_1 = mult(y6_1, c18_1)
        return var_1

@register(Coal)
class Z18():
    # 'Coal'!Z18
    value = 119181940
    formula = "=Z6*$C$18"
    @eval_fn
    def Z18():
        z6_1 = Coal.Z6()
        c18_1 = Coal.C18()
        var_1 = mult(z6_1, c18_1)
        return var_1

@register(Coal)
class AA18():
    # 'Coal'!AA18
    value = 107875733.333
    formula = "=AA6*$C$18"
    @eval_fn
    def AA18():
        aa6_1 = Coal.AA6()
        c18_1 = Coal.C18()
        var_1 = mult(aa6_1, c18_1)
        return var_1

@register(Coal)
class AB18():
    # 'Coal'!AB18
    value = 97606793.3333
    formula = "=AB6*$C$18"
    @eval_fn
    def AB18():
        ab6_1 = Coal.AB6()
        c18_1 = Coal.C18()
        var_1 = mult(ab6_1, c18_1)
        return var_1

@register(Coal)
class AC18():
    # 'Coal'!AC18
    value = 116588773.333
    formula = "=AC6*$C$18"
    @eval_fn
    def AC18():
        ac6_1 = Coal.AC6()
        c18_1 = Coal.C18()
        var_1 = mult(ac6_1, c18_1)
        return var_1

@register(Coal)
class AD18():
    # 'Coal'!AD18
    value = 40972033.3333
    formula = "=AD6*$C$18"
    @eval_fn
    def AD18():
        ad6_1 = Coal.AD6()
        c18_1 = Coal.C18()
        var_1 = mult(ad6_1, c18_1)
        return var_1

@register(Coal)
class AE18():
    # 'Coal'!AE18
    value = 163162046.667
    formula = "=AE6*$C$18"
    @eval_fn
    def AE18():
        ae6_1 = Coal.AE6()
        c18_1 = Coal.C18()
        var_1 = mult(ae6_1, c18_1)
        return var_1

@register(Coal)
class AF18():
    # 'Coal'!AF18
    value = 128828520
    formula = "=AF6*$C$18"
    @eval_fn
    def AF18():
        af6_1 = Coal.AF6()
        c18_1 = Coal.C18()
        var_1 = mult(af6_1, c18_1)
        return var_1

@register(Coal)
class AG18():
    # 'Coal'!AG18
    value = 82462700
    formula = "=AG6*$C$18"
    @eval_fn
    def AG18():
        ag6_1 = Coal.AG6()
        c18_1 = Coal.C18()
        var_1 = mult(ag6_1, c18_1)
        return var_1

@register(Coal)
class AH18():
    # 'Coal'!AH18
    value = 74786926.6667
    formula = "=AH6*$C$18"
    @eval_fn
    def AH18():
        ah6_1 = Coal.AH6()
        c18_1 = Coal.C18()
        var_1 = mult(ah6_1, c18_1)
        return var_1

@register(Coal)
class AI18():
    # 'Coal'!AI18
    value = 110261446.667
    formula = "=AI6*$C$18"
    @eval_fn
    def AI18():
        ai6_1 = Coal.AI6()
        c18_1 = Coal.C18()
        var_1 = mult(ai6_1, c18_1)
        return var_1

@register(Coal)
class AJ18():
    # 'Coal'!AJ18
    value = 700155000
    formula = "=AJ6*$C$18"
    @eval_fn
    def AJ18():
        aj6_1 = Coal.AJ6()
        c18_1 = Coal.C18()
        var_1 = mult(aj6_1, c18_1)
        return var_1

@register(Coal)
class AK18():
    # 'Coal'!AK18
    value = 1615542833.33
    formula = "=AK6*$C$18"
    @eval_fn
    def AK18():
        ak6_1 = Coal.AK6()
        c18_1 = Coal.C18()
        var_1 = mult(ak6_1, c18_1)
        return var_1

@register(Coal)
class AL18():
    # 'Coal'!AL18
    value = 1632657733.33
    formula = "=AL6*$C$18"
    @eval_fn
    def AL18():
        al6_1 = Coal.AL6()
        c18_1 = Coal.C18()
        var_1 = mult(al6_1, c18_1)
        return var_1

@register(Coal)
class AM18():
    # 'Coal'!AM18
    value = 2065612840
    formula = "=AM6*$C$18"
    @eval_fn
    def AM18():
        am6_1 = Coal.AM6()
        c18_1 = Coal.C18()
        var_1 = mult(am6_1, c18_1)
        return var_1

@register(Coal)
class AN18():
    # 'Coal'!AN18
    value = 2113015926.67
    formula = "=AN6*$C$18"
    @eval_fn
    def AN18():
        an6_1 = Coal.AN6()
        c18_1 = Coal.C18()
        var_1 = mult(an6_1, c18_1)
        return var_1

@register(Coal)
class AO18():
    # 'Coal'!AO18
    value = 2127745113.33
    formula = "=AO6*$C$18"
    @eval_fn
    def AO18():
        ao6_1 = Coal.AO6()
        c18_1 = Coal.C18()
        var_1 = mult(ao6_1, c18_1)
        return var_1

@register(Coal)
class AP18():
    # 'Coal'!AP18
    value = 1890211046.67
    formula = "=AP6*$C$18"
    @eval_fn
    def AP18():
        ap6_1 = Coal.AP6()
        c18_1 = Coal.C18()
        var_1 = mult(ap6_1, c18_1)
        return var_1

@register(Coal)
class AQ18():
    # 'Coal'!AQ18
    value = 1835028460
    formula = "=AQ6*$C$18"
    @eval_fn
    def AQ18():
        aq6_1 = Coal.AQ6()
        c18_1 = Coal.C18()
        var_1 = mult(aq6_1, c18_1)
        return var_1

@register(Coal)
class AR18():
    # 'Coal'!AR18
    value = 1831086846.67
    formula = "=AR6*$C$18"
    @eval_fn
    def AR18():
        ar6_1 = Coal.AR6()
        c18_1 = Coal.C18()
        var_1 = mult(ar6_1, c18_1)
        return var_1

@register(Coal)
class AS18():
    # 'Coal'!AS18
    value = 1843637773.33
    formula = "=AS6*$C$18"
    @eval_fn
    def AS18():
        as6_1 = Coal.AS6()
        c18_1 = Coal.C18()
        var_1 = mult(as6_1, c18_1)
        return var_1

@register(Coal)
class AT18():
    # 'Coal'!AT18
    value = 1723729746.67
    formula = "=AT6*$C$18"
    @eval_fn
    def AT18():
        at6_1 = Coal.AT6()
        c18_1 = Coal.C18()
        var_1 = mult(at6_1, c18_1)
        return var_1

@register(Coal)
class AU18():
    # 'Coal'!AU18
    value = 1997360693.33
    formula = "=AU6*$C$18"
    @eval_fn
    def AU18():
        au6_1 = Coal.AU6()
        c18_1 = Coal.C18()
        var_1 = mult(au6_1, c18_1)
        return var_1

@register(Coal)
class AV18():
    # 'Coal'!AV18
    value = 1997153240
    formula = "=AV6*$C$18"
    @eval_fn
    def AV18():
        av6_1 = Coal.AV6()
        c18_1 = Coal.C18()
        var_1 = mult(av6_1, c18_1)
        return var_1

@register(Coal)
class AW18():
    # 'Coal'!AW18
    value = 1862516026.67
    formula = "=AW6*$C$18"
    @eval_fn
    def AW18():
        aw6_1 = Coal.AW6()
        c18_1 = Coal.C18()
        var_1 = mult(aw6_1, c18_1)
        return var_1

@register(Coal)
class AX18():
    # 'Coal'!AX18
    value = 1818017286.67
    formula = "=AX6*$C$18"
    @eval_fn
    def AX18():
        ax6_1 = Coal.AX6()
        c18_1 = Coal.C18()
        var_1 = mult(ax6_1, c18_1)
        return var_1

@register(Coal)
class AY18():
    # 'Coal'!AY18
    value = 1971532753.33
    formula = "=AY6*$C$18"
    @eval_fn
    def AY18():
        ay6_1 = Coal.AY6()
        c18_1 = Coal.C18()
        var_1 = mult(ay6_1, c18_1)
        return var_1

@register(Coal)
class AZ18():
    # 'Coal'!AZ18
    value = 2090922146.67
    formula = "=AZ6*$C$18"
    @eval_fn
    def AZ18():
        az6_1 = Coal.AZ6()
        c18_1 = Coal.C18()
        var_1 = mult(az6_1, c18_1)
        return var_1

@register(Coal)
class BA18():
    # 'Coal'!BA18
    value = 1966450146.67
    formula = "=BA6*$C$18"
    @eval_fn
    def BA18():
        ba6_1 = Coal.BA6()
        c18_1 = Coal.C18()
        var_1 = mult(ba6_1, c18_1)
        return var_1

@register(Coal)
class BB18():
    # 'Coal'!BB18
    value = 1775489353.33
    formula = "=BB6*$C$18"
    @eval_fn
    def BB18():
        bb6_1 = Coal.BB6()
        c18_1 = Coal.C18()
        var_1 = mult(bb6_1, c18_1)
        return var_1

@register(Coal)
class BC18():
    # 'Coal'!BC18
    value = 1667924800
    formula = "=BC6*$C$18"
    @eval_fn
    def BC18():
        bc6_1 = Coal.BC6()
        c18_1 = Coal.C18()
        var_1 = mult(bc6_1, c18_1)
        return var_1

@register(Coal)
class BD18():
    # 'Coal'!BD18
    value = 1718958320
    formula = "=BD6*$C$18"
    @eval_fn
    def BD18():
        bd6_1 = Coal.BD6()
        c18_1 = Coal.C18()
        var_1 = mult(bd6_1, c18_1)
        return var_1

@register(Coal)
class BE18():
    # 'Coal'!BE18
    value = 1587640360
    formula = "=BE6*$C$18"
    @eval_fn
    def BE18():
        be6_1 = Coal.BE6()
        c18_1 = Coal.C18()
        var_1 = mult(be6_1, c18_1)
        return var_1

@register(Coal)
class BF18():
    # 'Coal'!BF18
    value = "#N/A"
    formula = "=BF6*$C$18"
    @eval_fn
    def BF18():
        bf6_1 = Coal.BF6()
        c18_1 = Coal.C18()
        var_1 = mult(bf6_1, c18_1)
        return var_1

@register(Coal)
class BG18():
    # 'Coal'!BG18
    value = "#N/A"
    formula = "=BG6*$C$18"
    @eval_fn
    def BG18():
        bg6_1 = Coal.BG6()
        c18_1 = Coal.C18()
        var_1 = mult(bg6_1, c18_1)
        return var_1

@register(Coal)
class BH18():
    # 'Coal'!BH18
    value = "#N/A"
    formula = "=BH6*$C$18"
    @eval_fn
    def BH18():
        bh6_1 = Coal.BH6()
        c18_1 = Coal.C18()
        var_1 = mult(bh6_1, c18_1)
        return var_1

@register(Coal)
class BI18():
    # 'Coal'!BI18
    value = "#N/A"
    formula = "=BI6*$C$18"
    @eval_fn
    def BI18():
        bi6_1 = Coal.BI6()
        c18_1 = Coal.C18()
        var_1 = mult(bi6_1, c18_1)
        return var_1

@register(Coal)
class BJ18():
    # 'Coal'!BJ18
    value = "#N/A"
    formula = "=BJ6*$C$18"
    @eval_fn
    def BJ18():
        bj6_1 = Coal.BJ6()
        c18_1 = Coal.C18()
        var_1 = mult(bj6_1, c18_1)
        return var_1

@register(Coal)
class BK18():
    # 'Coal'!BK18
    value = "#N/A"
    formula = "=BK6*$C$18"
    @eval_fn
    def BK18():
        bk6_1 = Coal.BK6()
        c18_1 = Coal.C18()
        var_1 = mult(bk6_1, c18_1)
        return var_1

@register(Coal)
class BL18():
    # 'Coal'!BL18
    value = "#N/A"
    formula = "=BL6*$C$18"
    @eval_fn
    def BL18():
        bl6_1 = Coal.BL6()
        c18_1 = Coal.C18()
        var_1 = mult(bl6_1, c18_1)
        return var_1

@register(Coal)
class A20():
    # 'Coal'!A20
    value = "Life Cycle Emissions (Coal Eq)"

@register(Coal)
class C20():
    # 'Coal'!C20
    value = "Total WTT (Well-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A21():
    # 'Coal'!A21
    value = "US"

@register(Coal)
class B21():
    # 'Coal'!B21
    value = "MMBTU"

@register(Coal)
class C21():
    # 'Coal'!C21
    value = 15.31
    formula = "='Carbon Coefficients'!D6"
    @eval_fn
    def C21():
        d6_1 = Carbon_Coefficients.D6()
        return d6_1

@register(Coal)
class E21():
    # 'Coal'!E21
    value = 0
    formula = "=E18/$C$21"
    @eval_fn
    def E21():
        e18_1 = Coal.E18()
        c21_1 = Coal.C21()
        var_1 = divide(e18_1, c21_1)
        return var_1

@register(Coal)
class F21():
    # 'Coal'!F21
    value = 0
    formula = "=F18/$C$21"
    @eval_fn
    def F21():
        f18_1 = Coal.F18()
        c21_1 = Coal.C21()
        var_1 = divide(f18_1, c21_1)
        return var_1

@register(Coal)
class G21():
    # 'Coal'!G21
    value = 0
    formula = "=G18/$C$21"
    @eval_fn
    def G21():
        g18_1 = Coal.G18()
        c21_1 = Coal.C21()
        var_1 = divide(g18_1, c21_1)
        return var_1

@register(Coal)
class H21():
    # 'Coal'!H21
    value = 0
    formula = "=H18/$C$21"
    @eval_fn
    def H21():
        h18_1 = Coal.H18()
        c21_1 = Coal.C21()
        var_1 = divide(h18_1, c21_1)
        return var_1

@register(Coal)
class I21():
    # 'Coal'!I21
    value = 0
    formula = "=I18/$C$21"
    @eval_fn
    def I21():
        i18_1 = Coal.I18()
        c21_1 = Coal.C21()
        var_1 = divide(i18_1, c21_1)
        return var_1

@register(Coal)
class J21():
    # 'Coal'!J21
    value = 0
    formula = "=J18/$C$21"
    @eval_fn
    def J21():
        j18_1 = Coal.J18()
        c21_1 = Coal.C21()
        var_1 = divide(j18_1, c21_1)
        return var_1

@register(Coal)
class K21():
    # 'Coal'!K21
    value = 0
    formula = "=K18/$C$21"
    @eval_fn
    def K21():
        k18_1 = Coal.K18()
        c21_1 = Coal.C21()
        var_1 = divide(k18_1, c21_1)
        return var_1

@register(Coal)
class L21():
    # 'Coal'!L21
    value = 0
    formula = "=L18/$C$21"
    @eval_fn
    def L21():
        l18_1 = Coal.L18()
        c21_1 = Coal.C21()
        var_1 = divide(l18_1, c21_1)
        return var_1

@register(Coal)
class M21():
    # 'Coal'!M21
    value = 0
    formula = "=M18/$C$21"
    @eval_fn
    def M21():
        m18_1 = Coal.M18()
        c21_1 = Coal.C21()
        var_1 = divide(m18_1, c21_1)
        return var_1

@register(Coal)
class N21():
    # 'Coal'!N21
    value = 0
    formula = "=N18/$C$21"
    @eval_fn
    def N21():
        n18_1 = Coal.N18()
        c21_1 = Coal.C21()
        var_1 = divide(n18_1, c21_1)
        return var_1

@register(Coal)
class O21():
    # 'Coal'!O21
    value = 0
    formula = "=O18/$C$21"
    @eval_fn
    def O21():
        o18_1 = Coal.O18()
        c21_1 = Coal.C21()
        var_1 = divide(o18_1, c21_1)
        return var_1

@register(Coal)
class P21():
    # 'Coal'!P21
    value = 0
    formula = "=P18/$C$21"
    @eval_fn
    def P21():
        p18_1 = Coal.P18()
        c21_1 = Coal.C21()
        var_1 = divide(p18_1, c21_1)
        return var_1

@register(Coal)
class Q21():
    # 'Coal'!Q21
    value = 0
    formula = "=Q18/$C$21"
    @eval_fn
    def Q21():
        q18_1 = Coal.Q18()
        c21_1 = Coal.C21()
        var_1 = divide(q18_1, c21_1)
        return var_1

@register(Coal)
class R21():
    # 'Coal'!R21
    value = 0
    formula = "=R18/$C$21"
    @eval_fn
    def R21():
        r18_1 = Coal.R18()
        c21_1 = Coal.C21()
        var_1 = divide(r18_1, c21_1)
        return var_1

@register(Coal)
class S21():
    # 'Coal'!S21
    value = 0
    formula = "=S18/$C$21"
    @eval_fn
    def S21():
        s18_1 = Coal.S18()
        c21_1 = Coal.C21()
        var_1 = divide(s18_1, c21_1)
        return var_1

@register(Coal)
class T21():
    # 'Coal'!T21
    value = 0
    formula = "=T18/$C$21"
    @eval_fn
    def T21():
        t18_1 = Coal.T18()
        c21_1 = Coal.C21()
        var_1 = divide(t18_1, c21_1)
        return var_1

@register(Coal)
class U21():
    # 'Coal'!U21
    value = 0
    formula = "=U18/$C$21"
    @eval_fn
    def U21():
        u18_1 = Coal.U18()
        c21_1 = Coal.C21()
        var_1 = divide(u18_1, c21_1)
        return var_1

@register(Coal)
class V21():
    # 'Coal'!V21
    value = 0
    formula = "=V18/$C$21"
    @eval_fn
    def V21():
        v18_1 = Coal.V18()
        c21_1 = Coal.C21()
        var_1 = divide(v18_1, c21_1)
        return var_1

@register(Coal)
class W21():
    # 'Coal'!W21
    value = 0
    formula = "=W18/$C$21"
    @eval_fn
    def W21():
        w18_1 = Coal.W18()
        c21_1 = Coal.C21()
        var_1 = divide(w18_1, c21_1)
        return var_1

@register(Coal)
class X21():
    # 'Coal'!X21
    value = 0
    formula = "=X18/$C$21"
    @eval_fn
    def X21():
        x18_1 = Coal.X18()
        c21_1 = Coal.C21()
        var_1 = divide(x18_1, c21_1)
        return var_1

@register(Coal)
class Y21():
    # 'Coal'!Y21
    value = 0
    formula = "=Y18/$C$21"
    @eval_fn
    def Y21():
        y18_1 = Coal.Y18()
        c21_1 = Coal.C21()
        var_1 = divide(y18_1, c21_1)
        return var_1

@register(Coal)
class Z21():
    # 'Coal'!Z21
    value = 7784581.3194
    formula = "=Z18/$C$21"
    @eval_fn
    def Z21():
        z18_1 = Coal.Z18()
        c21_1 = Coal.C21()
        var_1 = divide(z18_1, c21_1)
        return var_1

@register(Coal)
class AA21():
    # 'Coal'!AA21
    value = 7046096.2334
    formula = "=AA18/$C$21"
    @eval_fn
    def AA21():
        aa18_1 = Coal.AA18()
        c21_1 = Coal.C21()
        var_1 = divide(aa18_1, c21_1)
        return var_1

@register(Coal)
class AB21():
    # 'Coal'!AB21
    value = 6375362.07272
    formula = "=AB18/$C$21"
    @eval_fn
    def AB21():
        ab18_1 = Coal.AB18()
        c21_1 = Coal.C21()
        var_1 = divide(ab18_1, c21_1)
        return var_1

@register(Coal)
class AC21():
    # 'Coal'!AC21
    value = 7615204.0061
    formula = "=AC18/$C$21"
    @eval_fn
    def AC21():
        ac18_1 = Coal.AC18()
        c21_1 = Coal.C21()
        var_1 = divide(ac18_1, c21_1)
        return var_1

@register(Coal)
class AD21():
    # 'Coal'!AD21
    value = 2676161.55019
    formula = "=AD18/$C$21"
    @eval_fn
    def AD21():
        ad18_1 = Coal.AD18()
        c21_1 = Coal.C21()
        var_1 = divide(ad18_1, c21_1)
        return var_1

@register(Coal)
class AE21():
    # 'Coal'!AE21
    value = 10657220.553
    formula = "=AE18/$C$21"
    @eval_fn
    def AE21():
        ae18_1 = Coal.AE18()
        c21_1 = Coal.C21()
        var_1 = divide(ae18_1, c21_1)
        return var_1

@register(Coal)
class AF21():
    # 'Coal'!AF21
    value = 8414664.92489
    formula = "=AF18/$C$21"
    @eval_fn
    def AF21():
        af18_1 = Coal.AF18()
        c21_1 = Coal.C21()
        var_1 = divide(af18_1, c21_1)
        return var_1

@register(Coal)
class AG21():
    # 'Coal'!AG21
    value = 5386198.56303
    formula = "=AG18/$C$21"
    @eval_fn
    def AG21():
        ag18_1 = Coal.AG18()
        c21_1 = Coal.C21()
        var_1 = divide(ag18_1, c21_1)
        return var_1

@register(Coal)
class AH21():
    # 'Coal'!AH21
    value = 4884841.71565
    formula = "=AH18/$C$21"
    @eval_fn
    def AH21():
        ah18_1 = Coal.AH18()
        c21_1 = Coal.C21()
        var_1 = divide(ah18_1, c21_1)
        return var_1

@register(Coal)
class AI21():
    # 'Coal'!AI21
    value = 7201923.36164
    formula = "=AI18/$C$21"
    @eval_fn
    def AI21():
        ai18_1 = Coal.AI18()
        c21_1 = Coal.C21()
        var_1 = divide(ai18_1, c21_1)
        return var_1

@register(Coal)
class AJ21():
    # 'Coal'!AJ21
    value = 45731874.5918
    formula = "=AJ18/$C$21"
    @eval_fn
    def AJ21():
        aj18_1 = Coal.AJ18()
        c21_1 = Coal.C21()
        var_1 = divide(aj18_1, c21_1)
        return var_1

@register(Coal)
class AK21():
    # 'Coal'!AK21
    value = 105522066.188
    formula = "=AK18/$C$21"
    @eval_fn
    def AK21():
        ak18_1 = Coal.AK18()
        c21_1 = Coal.C21()
        var_1 = divide(ak18_1, c21_1)
        return var_1

@register(Coal)
class AL21():
    # 'Coal'!AL21
    value = 106639956.455
    formula = "=AL18/$C$21"
    @eval_fn
    def AL21():
        al18_1 = Coal.AL18()
        c21_1 = Coal.C21()
        var_1 = divide(al18_1, c21_1)
        return var_1

@register(Coal)
class AM21():
    # 'Coal'!AM21
    value = 134919192.685
    formula = "=AM18/$C$21"
    @eval_fn
    def AM21():
        am18_1 = Coal.AM18()
        c21_1 = Coal.C21()
        var_1 = divide(am18_1, c21_1)
        return var_1

@register(Coal)
class AN21():
    # 'Coal'!AN21
    value = 138015409.972
    formula = "=AN18/$C$21"
    @eval_fn
    def AN21():
        an18_1 = Coal.AN18()
        c21_1 = Coal.C21()
        var_1 = divide(an18_1, c21_1)
        return var_1

@register(Coal)
class AO21():
    # 'Coal'!AO21
    value = 138977473.111
    formula = "=AO18/$C$21"
    @eval_fn
    def AO21():
        ao18_1 = Coal.AO18()
        c21_1 = Coal.C21()
        var_1 = divide(ao18_1, c21_1)
        return var_1

@register(Coal)
class AP21():
    # 'Coal'!AP21
    value = 123462511.213
    formula = "=AP18/$C$21"
    @eval_fn
    def AP21():
        ap18_1 = Coal.AP18()
        c21_1 = Coal.C21()
        var_1 = divide(ap18_1, c21_1)
        return var_1

@register(Coal)
class AQ21():
    # 'Coal'!AQ21
    value = 119858161.986
    formula = "=AQ18/$C$21"
    @eval_fn
    def AQ21():
        aq18_1 = Coal.AQ18()
        c21_1 = Coal.C21()
        var_1 = divide(aq18_1, c21_1)
        return var_1

@register(Coal)
class AR21():
    # 'Coal'!AR21
    value = 119600708.469
    formula = "=AR18/$C$21"
    @eval_fn
    def AR21():
        ar18_1 = Coal.AR18()
        c21_1 = Coal.C21()
        var_1 = divide(ar18_1, c21_1)
        return var_1

@register(Coal)
class AS21():
    # 'Coal'!AS21
    value = 120420494.666
    formula = "=AS18/$C$21"
    @eval_fn
    def AS21():
        as18_1 = Coal.AS18()
        c21_1 = Coal.C21()
        var_1 = divide(as18_1, c21_1)
        return var_1

@register(Coal)
class AT21():
    # 'Coal'!AT21
    value = 112588487.699
    formula = "=AT18/$C$21"
    @eval_fn
    def AT21():
        at18_1 = Coal.AT18()
        c21_1 = Coal.C21()
        var_1 = divide(at18_1, c21_1)
        return var_1

@register(Coal)
class AU21():
    # 'Coal'!AU21
    value = 130461181.798
    formula = "=AU18/$C$21"
    @eval_fn
    def AU21():
        au18_1 = Coal.AU18()
        c21_1 = Coal.C21()
        var_1 = divide(au18_1, c21_1)
        return var_1

@register(Coal)
class AV21():
    # 'Coal'!AV21
    value = 130447631.613
    formula = "=AV18/$C$21"
    @eval_fn
    def AV21():
        av18_1 = Coal.AV18()
        c21_1 = Coal.C21()
        var_1 = divide(av18_1, c21_1)
        return var_1

@register(Coal)
class AW21():
    # 'Coal'!AW21
    value = 121653561.507
    formula = "=AW18/$C$21"
    @eval_fn
    def AW21():
        aw18_1 = Coal.AW18()
        c21_1 = Coal.C21()
        var_1 = divide(aw18_1, c21_1)
        return var_1

@register(Coal)
class AX21():
    # 'Coal'!AX21
    value = 118747046.81
    formula = "=AX18/$C$21"
    @eval_fn
    def AX21():
        ax18_1 = Coal.AX18()
        c21_1 = Coal.C21()
        var_1 = divide(ax18_1, c21_1)
        return var_1

@register(Coal)
class AY21():
    # 'Coal'!AY21
    value = 128774183.758
    formula = "=AY18/$C$21"
    @eval_fn
    def AY21():
        ay18_1 = Coal.AY18()
        c21_1 = Coal.C21()
        var_1 = divide(ay18_1, c21_1)
        return var_1

@register(Coal)
class AZ21():
    # 'Coal'!AZ21
    value = 136572315.262
    formula = "=AZ18/$C$21"
    @eval_fn
    def AZ21():
        az18_1 = Coal.AZ18()
        c21_1 = Coal.C21()
        var_1 = divide(az18_1, c21_1)
        return var_1

@register(Coal)
class BA21():
    # 'Coal'!BA21
    value = 128442204.224
    formula = "=BA18/$C$21"
    @eval_fn
    def BA21():
        ba18_1 = Coal.BA18()
        c21_1 = Coal.C21()
        var_1 = divide(ba18_1, c21_1)
        return var_1

@register(Coal)
class BB21():
    # 'Coal'!BB21
    value = 115969258.872
    formula = "=BB18/$C$21"
    @eval_fn
    def BB21():
        bb18_1 = Coal.BB18()
        c21_1 = Coal.C21()
        var_1 = divide(bb18_1, c21_1)
        return var_1

@register(Coal)
class BC21():
    # 'Coal'!BC21
    value = 108943487.916
    formula = "=BC18/$C$21"
    @eval_fn
    def BC21():
        bc18_1 = Coal.BC18()
        c21_1 = Coal.C21()
        var_1 = divide(bc18_1, c21_1)
        return var_1

@register(Coal)
class BD21():
    # 'Coal'!BD21
    value = 112276833.442
    formula = "=BD18/$C$21"
    @eval_fn
    def BD21():
        bd18_1 = Coal.BD18()
        c21_1 = Coal.C21()
        var_1 = divide(bd18_1, c21_1)
        return var_1

@register(Coal)
class BE21():
    # 'Coal'!BE21
    value = 103699566.297
    formula = "=BE18/$C$21"
    @eval_fn
    def BE21():
        be18_1 = Coal.BE18()
        c21_1 = Coal.C21()
        var_1 = divide(be18_1, c21_1)
        return var_1

@register(Coal)
class BF21():
    # 'Coal'!BF21
    value = "#N/A"
    formula = "=BF18/$C$21"
    @eval_fn
    def BF21():
        bf18_1 = Coal.BF18()
        c21_1 = Coal.C21()
        var_1 = divide(bf18_1, c21_1)
        return var_1

@register(Coal)
class BG21():
    # 'Coal'!BG21
    value = "#N/A"
    formula = "=BG18/$C$21"
    @eval_fn
    def BG21():
        bg18_1 = Coal.BG18()
        c21_1 = Coal.C21()
        var_1 = divide(bg18_1, c21_1)
        return var_1

@register(Coal)
class BH21():
    # 'Coal'!BH21
    value = "#N/A"
    formula = "=BH18/$C$21"
    @eval_fn
    def BH21():
        bh18_1 = Coal.BH18()
        c21_1 = Coal.C21()
        var_1 = divide(bh18_1, c21_1)
        return var_1

@register(Coal)
class BI21():
    # 'Coal'!BI21
    value = "#N/A"
    formula = "=BI18/$C$21"
    @eval_fn
    def BI21():
        bi18_1 = Coal.BI18()
        c21_1 = Coal.C21()
        var_1 = divide(bi18_1, c21_1)
        return var_1

@register(Coal)
class BJ21():
    # 'Coal'!BJ21
    value = "#N/A"
    formula = "=BJ18/$C$21"
    @eval_fn
    def BJ21():
        bj18_1 = Coal.BJ18()
        c21_1 = Coal.C21()
        var_1 = divide(bj18_1, c21_1)
        return var_1

@register(Coal)
class BK21():
    # 'Coal'!BK21
    value = "#N/A"
    formula = "=BK18/$C$21"
    @eval_fn
    def BK21():
        bk18_1 = Coal.BK18()
        c21_1 = Coal.C21()
        var_1 = divide(bk18_1, c21_1)
        return var_1

@register(Coal)
class BL21():
    # 'Coal'!BL21
    value = "#N/A"
    formula = "=BL18/$C$21"
    @eval_fn
    def BL21():
        bl18_1 = Coal.BL18()
        c21_1 = Coal.C21()
        var_1 = divide(bl18_1, c21_1)
        return var_1

@register(Coal)
class A23():
    # 'Coal'!A23
    value = "Weights (Upstream Emissions to Total Emissions"

@register(Coal)
class C23():
    # 'Coal'!C23
    value = "Percentage"

@register(Coal)
class A24():
    # 'Coal'!A24
    value = "US"

@register(Coal)
class B24():
    # 'Coal'!B24
    value = "kgCO2"

@register(Coal)
class E24():
    # 'Coal'!E24
    value = 0
    formula = "=IF(E18=0,0,(E6*E12)/E18)"
    @eval_fn
    def E24():
        e18_1 = Coal.E18()
        var_1 = equal(e18_1, 0)
        e6_1 = Coal.E6()
        e12_1 = Coal.E12()
        var_2 = mult(e6_1, e12_1)
        e18_2 = Coal.E18()
        var_3 = divide(var_2, e18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class F24():
    # 'Coal'!F24
    value = 0
    formula = "=IF(F18=0,0,(F6*F12)/F18)"
    @eval_fn
    def F24():
        f18_1 = Coal.F18()
        var_1 = equal(f18_1, 0)
        f6_1 = Coal.F6()
        f12_1 = Coal.F12()
        var_2 = mult(f6_1, f12_1)
        f18_2 = Coal.F18()
        var_3 = divide(var_2, f18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class G24():
    # 'Coal'!G24
    value = 0
    formula = "=IF(G18=0,0,(G6*G12)/G18)"
    @eval_fn
    def G24():
        g18_1 = Coal.G18()
        var_1 = equal(g18_1, 0)
        g6_1 = Coal.G6()
        g12_1 = Coal.G12()
        var_2 = mult(g6_1, g12_1)
        g18_2 = Coal.G18()
        var_3 = divide(var_2, g18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class H24():
    # 'Coal'!H24
    value = 0
    formula = "=IF(H18=0,0,(H6*H12)/H18)"
    @eval_fn
    def H24():
        h18_1 = Coal.H18()
        var_1 = equal(h18_1, 0)
        h6_1 = Coal.H6()
        h12_1 = Coal.H12()
        var_2 = mult(h6_1, h12_1)
        h18_2 = Coal.H18()
        var_3 = divide(var_2, h18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class I24():
    # 'Coal'!I24
    value = 0
    formula = "=IF(I18=0,0,(I6*I12)/I18)"
    @eval_fn
    def I24():
        i18_1 = Coal.I18()
        var_1 = equal(i18_1, 0)
        i6_1 = Coal.I6()
        i12_1 = Coal.I12()
        var_2 = mult(i6_1, i12_1)
        i18_2 = Coal.I18()
        var_3 = divide(var_2, i18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class J24():
    # 'Coal'!J24
    value = 0
    formula = "=IF(J18=0,0,(J6*J12)/J18)"
    @eval_fn
    def J24():
        j18_1 = Coal.J18()
        var_1 = equal(j18_1, 0)
        j6_1 = Coal.J6()
        j12_1 = Coal.J12()
        var_2 = mult(j6_1, j12_1)
        j18_2 = Coal.J18()
        var_3 = divide(var_2, j18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class K24():
    # 'Coal'!K24
    value = 0
    formula = "=IF(K18=0,0,(K6*K12)/K18)"
    @eval_fn
    def K24():
        k18_1 = Coal.K18()
        var_1 = equal(k18_1, 0)
        k6_1 = Coal.K6()
        k12_1 = Coal.K12()
        var_2 = mult(k6_1, k12_1)
        k18_2 = Coal.K18()
        var_3 = divide(var_2, k18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class L24():
    # 'Coal'!L24
    value = 0
    formula = "=IF(L18=0,0,(L6*L12)/L18)"
    @eval_fn
    def L24():
        l18_1 = Coal.L18()
        var_1 = equal(l18_1, 0)
        l6_1 = Coal.L6()
        l12_1 = Coal.L12()
        var_2 = mult(l6_1, l12_1)
        l18_2 = Coal.L18()
        var_3 = divide(var_2, l18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class M24():
    # 'Coal'!M24
    value = 0
    formula = "=IF(M18=0,0,(M6*M12)/M18)"
    @eval_fn
    def M24():
        m18_1 = Coal.M18()
        var_1 = equal(m18_1, 0)
        m6_1 = Coal.M6()
        m12_1 = Coal.M12()
        var_2 = mult(m6_1, m12_1)
        m18_2 = Coal.M18()
        var_3 = divide(var_2, m18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class N24():
    # 'Coal'!N24
    value = 0
    formula = "=IF(N18=0,0,(N6*N12)/N18)"
    @eval_fn
    def N24():
        n18_1 = Coal.N18()
        var_1 = equal(n18_1, 0)
        n6_1 = Coal.N6()
        n12_1 = Coal.N12()
        var_2 = mult(n6_1, n12_1)
        n18_2 = Coal.N18()
        var_3 = divide(var_2, n18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class O24():
    # 'Coal'!O24
    value = 0
    formula = "=IF(O18=0,0,(O6*O12)/O18)"
    @eval_fn
    def O24():
        o18_1 = Coal.O18()
        var_1 = equal(o18_1, 0)
        o6_1 = Coal.O6()
        o12_1 = Coal.O12()
        var_2 = mult(o6_1, o12_1)
        o18_2 = Coal.O18()
        var_3 = divide(var_2, o18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class P24():
    # 'Coal'!P24
    value = 0
    formula = "=IF(P18=0,0,(P6*P12)/P18)"
    @eval_fn
    def P24():
        p18_1 = Coal.P18()
        var_1 = equal(p18_1, 0)
        p6_1 = Coal.P6()
        p12_1 = Coal.P12()
        var_2 = mult(p6_1, p12_1)
        p18_2 = Coal.P18()
        var_3 = divide(var_2, p18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class Q24():
    # 'Coal'!Q24
    value = 0
    formula = "=IF(Q18=0,0,(Q6*Q12)/Q18)"
    @eval_fn
    def Q24():
        q18_1 = Coal.Q18()
        var_1 = equal(q18_1, 0)
        q6_1 = Coal.Q6()
        q12_1 = Coal.Q12()
        var_2 = mult(q6_1, q12_1)
        q18_2 = Coal.Q18()
        var_3 = divide(var_2, q18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class R24():
    # 'Coal'!R24
    value = 0
    formula = "=IF(R18=0,0,(R6*R12)/R18)"
    @eval_fn
    def R24():
        r18_1 = Coal.R18()
        var_1 = equal(r18_1, 0)
        r6_1 = Coal.R6()
        r12_1 = Coal.R12()
        var_2 = mult(r6_1, r12_1)
        r18_2 = Coal.R18()
        var_3 = divide(var_2, r18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class S24():
    # 'Coal'!S24
    value = 0
    formula = "=IF(S18=0,0,(S6*S12)/S18)"
    @eval_fn
    def S24():
        s18_1 = Coal.S18()
        var_1 = equal(s18_1, 0)
        s6_1 = Coal.S6()
        s12_1 = Coal.S12()
        var_2 = mult(s6_1, s12_1)
        s18_2 = Coal.S18()
        var_3 = divide(var_2, s18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class T24():
    # 'Coal'!T24
    value = 0
    formula = "=IF(T18=0,0,(T6*T12)/T18)"
    @eval_fn
    def T24():
        t18_1 = Coal.T18()
        var_1 = equal(t18_1, 0)
        t6_1 = Coal.T6()
        t12_1 = Coal.T12()
        var_2 = mult(t6_1, t12_1)
        t18_2 = Coal.T18()
        var_3 = divide(var_2, t18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class U24():
    # 'Coal'!U24
    value = 0
    formula = "=IF(U18=0,0,(U6*U12)/U18)"
    @eval_fn
    def U24():
        u18_1 = Coal.U18()
        var_1 = equal(u18_1, 0)
        u6_1 = Coal.U6()
        u12_1 = Coal.U12()
        var_2 = mult(u6_1, u12_1)
        u18_2 = Coal.U18()
        var_3 = divide(var_2, u18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class V24():
    # 'Coal'!V24
    value = 0
    formula = "=IF(V18=0,0,(V6*V12)/V18)"
    @eval_fn
    def V24():
        v18_1 = Coal.V18()
        var_1 = equal(v18_1, 0)
        v6_1 = Coal.V6()
        v12_1 = Coal.V12()
        var_2 = mult(v6_1, v12_1)
        v18_2 = Coal.V18()
        var_3 = divide(var_2, v18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class W24():
    # 'Coal'!W24
    value = 0
    formula = "=IF(W18=0,0,(W6*W12)/W18)"
    @eval_fn
    def W24():
        w18_1 = Coal.W18()
        var_1 = equal(w18_1, 0)
        w6_1 = Coal.W6()
        w12_1 = Coal.W12()
        var_2 = mult(w6_1, w12_1)
        w18_2 = Coal.W18()
        var_3 = divide(var_2, w18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class X24():
    # 'Coal'!X24
    value = 0
    formula = "=IF(X18=0,0,(X6*X12)/X18)"
    @eval_fn
    def X24():
        x18_1 = Coal.X18()
        var_1 = equal(x18_1, 0)
        x6_1 = Coal.X6()
        x12_1 = Coal.X12()
        var_2 = mult(x6_1, x12_1)
        x18_2 = Coal.X18()
        var_3 = divide(var_2, x18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class Y24():
    # 'Coal'!Y24
    value = 0
    formula = "=IF(Y18=0,0,(Y6*Y12)/Y18)"
    @eval_fn
    def Y24():
        y18_1 = Coal.Y18()
        var_1 = equal(y18_1, 0)
        y6_1 = Coal.Y6()
        y12_1 = Coal.Y12()
        var_2 = mult(y6_1, y12_1)
        y18_2 = Coal.Y18()
        var_3 = divide(var_2, y18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class Z24():
    # 'Coal'!Z24
    value = 0.0886946461855
    formula = "=IF(Z18=0,0,(Z6*Z12)/Z18)"
    @eval_fn
    def Z24():
        z18_1 = Coal.Z18()
        var_1 = equal(z18_1, 0)
        z6_1 = Coal.Z6()
        z12_1 = Coal.Z12()
        var_2 = mult(z6_1, z12_1)
        z18_2 = Coal.Z18()
        var_3 = divide(var_2, z18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AA24():
    # 'Coal'!AA24
    value = 0.0886946461855
    formula = "=IF(AA18=0,0,(AA6*AA12)/AA18)"
    @eval_fn
    def AA24():
        aa18_1 = Coal.AA18()
        var_1 = equal(aa18_1, 0)
        aa6_1 = Coal.AA6()
        aa12_1 = Coal.AA12()
        var_2 = mult(aa6_1, aa12_1)
        aa18_2 = Coal.AA18()
        var_3 = divide(var_2, aa18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AB24():
    # 'Coal'!AB24
    value = 0.0886946461855
    formula = "=IF(AB18=0,0,(AB6*AB12)/AB18)"
    @eval_fn
    def AB24():
        ab18_1 = Coal.AB18()
        var_1 = equal(ab18_1, 0)
        ab6_1 = Coal.AB6()
        ab12_1 = Coal.AB12()
        var_2 = mult(ab6_1, ab12_1)
        ab18_2 = Coal.AB18()
        var_3 = divide(var_2, ab18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AC24():
    # 'Coal'!AC24
    value = 0.0886946461855
    formula = "=IF(AC18=0,0,(AC6*AC12)/AC18)"
    @eval_fn
    def AC24():
        ac18_1 = Coal.AC18()
        var_1 = equal(ac18_1, 0)
        ac6_1 = Coal.AC6()
        ac12_1 = Coal.AC12()
        var_2 = mult(ac6_1, ac12_1)
        ac18_2 = Coal.AC18()
        var_3 = divide(var_2, ac18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AD24():
    # 'Coal'!AD24
    value = 0.0886946461855
    formula = "=IF(AD18=0,0,(AD6*AD12)/AD18)"
    @eval_fn
    def AD24():
        ad18_1 = Coal.AD18()
        var_1 = equal(ad18_1, 0)
        ad6_1 = Coal.AD6()
        ad12_1 = Coal.AD12()
        var_2 = mult(ad6_1, ad12_1)
        ad18_2 = Coal.AD18()
        var_3 = divide(var_2, ad18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AE24():
    # 'Coal'!AE24
    value = 0.0886946461855
    formula = "=IF(AE18=0,0,(AE6*AE12)/AE18)"
    @eval_fn
    def AE24():
        ae18_1 = Coal.AE18()
        var_1 = equal(ae18_1, 0)
        ae6_1 = Coal.AE6()
        ae12_1 = Coal.AE12()
        var_2 = mult(ae6_1, ae12_1)
        ae18_2 = Coal.AE18()
        var_3 = divide(var_2, ae18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AF24():
    # 'Coal'!AF24
    value = 0.0886946461855
    formula = "=IF(AF18=0,0,(AF6*AF12)/AF18)"
    @eval_fn
    def AF24():
        af18_1 = Coal.AF18()
        var_1 = equal(af18_1, 0)
        af6_1 = Coal.AF6()
        af12_1 = Coal.AF12()
        var_2 = mult(af6_1, af12_1)
        af18_2 = Coal.AF18()
        var_3 = divide(var_2, af18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AG24():
    # 'Coal'!AG24
    value = 0.0886946461855
    formula = "=IF(AG18=0,0,(AG6*AG12)/AG18)"
    @eval_fn
    def AG24():
        ag18_1 = Coal.AG18()
        var_1 = equal(ag18_1, 0)
        ag6_1 = Coal.AG6()
        ag12_1 = Coal.AG12()
        var_2 = mult(ag6_1, ag12_1)
        ag18_2 = Coal.AG18()
        var_3 = divide(var_2, ag18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AH24():
    # 'Coal'!AH24
    value = 0.0886946461855
    formula = "=IF(AH18=0,0,(AH6*AH12)/AH18)"
    @eval_fn
    def AH24():
        ah18_1 = Coal.AH18()
        var_1 = equal(ah18_1, 0)
        ah6_1 = Coal.AH6()
        ah12_1 = Coal.AH12()
        var_2 = mult(ah6_1, ah12_1)
        ah18_2 = Coal.AH18()
        var_3 = divide(var_2, ah18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AI24():
    # 'Coal'!AI24
    value = 0.0886946461855
    formula = "=IF(AI18=0,0,(AI6*AI12)/AI18)"
    @eval_fn
    def AI24():
        ai18_1 = Coal.AI18()
        var_1 = equal(ai18_1, 0)
        ai6_1 = Coal.AI6()
        ai12_1 = Coal.AI12()
        var_2 = mult(ai6_1, ai12_1)
        ai18_2 = Coal.AI18()
        var_3 = divide(var_2, ai18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AJ24():
    # 'Coal'!AJ24
    value = 0.0886946461855
    formula = "=IF(AJ18=0,0,(AJ6*AJ12)/AJ18)"
    @eval_fn
    def AJ24():
        aj18_1 = Coal.AJ18()
        var_1 = equal(aj18_1, 0)
        aj6_1 = Coal.AJ6()
        aj12_1 = Coal.AJ12()
        var_2 = mult(aj6_1, aj12_1)
        aj18_2 = Coal.AJ18()
        var_3 = divide(var_2, aj18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AK24():
    # 'Coal'!AK24
    value = 0.0886946461855
    formula = "=IF(AK18=0,0,(AK6*AK12)/AK18)"
    @eval_fn
    def AK24():
        ak18_1 = Coal.AK18()
        var_1 = equal(ak18_1, 0)
        ak6_1 = Coal.AK6()
        ak12_1 = Coal.AK12()
        var_2 = mult(ak6_1, ak12_1)
        ak18_2 = Coal.AK18()
        var_3 = divide(var_2, ak18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AL24():
    # 'Coal'!AL24
    value = 0.0886946461855
    formula = "=IF(AL18=0,0,(AL6*AL12)/AL18)"
    @eval_fn
    def AL24():
        al18_1 = Coal.AL18()
        var_1 = equal(al18_1, 0)
        al6_1 = Coal.AL6()
        al12_1 = Coal.AL12()
        var_2 = mult(al6_1, al12_1)
        al18_2 = Coal.AL18()
        var_3 = divide(var_2, al18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AM24():
    # 'Coal'!AM24
    value = 0.0886946461855
    formula = "=IF(AM18=0,0,(AM6*AM12)/AM18)"
    @eval_fn
    def AM24():
        am18_1 = Coal.AM18()
        var_1 = equal(am18_1, 0)
        am6_1 = Coal.AM6()
        am12_1 = Coal.AM12()
        var_2 = mult(am6_1, am12_1)
        am18_2 = Coal.AM18()
        var_3 = divide(var_2, am18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AN24():
    # 'Coal'!AN24
    value = 0.0886946461855
    formula = "=IF(AN18=0,0,(AN6*AN12)/AN18)"
    @eval_fn
    def AN24():
        an18_1 = Coal.AN18()
        var_1 = equal(an18_1, 0)
        an6_1 = Coal.AN6()
        an12_1 = Coal.AN12()
        var_2 = mult(an6_1, an12_1)
        an18_2 = Coal.AN18()
        var_3 = divide(var_2, an18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AO24():
    # 'Coal'!AO24
    value = 0.0886946461855
    formula = "=IF(AO18=0,0,(AO6*AO12)/AO18)"
    @eval_fn
    def AO24():
        ao18_1 = Coal.AO18()
        var_1 = equal(ao18_1, 0)
        ao6_1 = Coal.AO6()
        ao12_1 = Coal.AO12()
        var_2 = mult(ao6_1, ao12_1)
        ao18_2 = Coal.AO18()
        var_3 = divide(var_2, ao18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AP24():
    # 'Coal'!AP24
    value = 0.0886946461855
    formula = "=IF(AP18=0,0,(AP6*AP12)/AP18)"
    @eval_fn
    def AP24():
        ap18_1 = Coal.AP18()
        var_1 = equal(ap18_1, 0)
        ap6_1 = Coal.AP6()
        ap12_1 = Coal.AP12()
        var_2 = mult(ap6_1, ap12_1)
        ap18_2 = Coal.AP18()
        var_3 = divide(var_2, ap18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AQ24():
    # 'Coal'!AQ24
    value = 0.0886946461855
    formula = "=IF(AQ18=0,0,(AQ6*AQ12)/AQ18)"
    @eval_fn
    def AQ24():
        aq18_1 = Coal.AQ18()
        var_1 = equal(aq18_1, 0)
        aq6_1 = Coal.AQ6()
        aq12_1 = Coal.AQ12()
        var_2 = mult(aq6_1, aq12_1)
        aq18_2 = Coal.AQ18()
        var_3 = divide(var_2, aq18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AR24():
    # 'Coal'!AR24
    value = 0.0886946461855
    formula = "=IF(AR18=0,0,(AR6*AR12)/AR18)"
    @eval_fn
    def AR24():
        ar18_1 = Coal.AR18()
        var_1 = equal(ar18_1, 0)
        ar6_1 = Coal.AR6()
        ar12_1 = Coal.AR12()
        var_2 = mult(ar6_1, ar12_1)
        ar18_2 = Coal.AR18()
        var_3 = divide(var_2, ar18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AS24():
    # 'Coal'!AS24
    value = 0.0886946461855
    formula = "=IF(AS18=0,0,(AS6*AS12)/AS18)"
    @eval_fn
    def AS24():
        as18_1 = Coal.AS18()
        var_1 = equal(as18_1, 0)
        as6_1 = Coal.AS6()
        as12_1 = Coal.AS12()
        var_2 = mult(as6_1, as12_1)
        as18_2 = Coal.AS18()
        var_3 = divide(var_2, as18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AT24():
    # 'Coal'!AT24
    value = 0.0886946461855
    formula = "=IF(AT18=0,0,(AT6*AT12)/AT18)"
    @eval_fn
    def AT24():
        at18_1 = Coal.AT18()
        var_1 = equal(at18_1, 0)
        at6_1 = Coal.AT6()
        at12_1 = Coal.AT12()
        var_2 = mult(at6_1, at12_1)
        at18_2 = Coal.AT18()
        var_3 = divide(var_2, at18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AU24():
    # 'Coal'!AU24
    value = 0.0886946461855
    formula = "=IF(AU18=0,0,(AU6*AU12)/AU18)"
    @eval_fn
    def AU24():
        au18_1 = Coal.AU18()
        var_1 = equal(au18_1, 0)
        au6_1 = Coal.AU6()
        au12_1 = Coal.AU12()
        var_2 = mult(au6_1, au12_1)
        au18_2 = Coal.AU18()
        var_3 = divide(var_2, au18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AV24():
    # 'Coal'!AV24
    value = 0.0886946461855
    formula = "=IF(AV18=0,0,(AV6*AV12)/AV18)"
    @eval_fn
    def AV24():
        av18_1 = Coal.AV18()
        var_1 = equal(av18_1, 0)
        av6_1 = Coal.AV6()
        av12_1 = Coal.AV12()
        var_2 = mult(av6_1, av12_1)
        av18_2 = Coal.AV18()
        var_3 = divide(var_2, av18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AW24():
    # 'Coal'!AW24
    value = 0.0886946461855
    formula = "=IF(AW18=0,0,(AW6*AW12)/AW18)"
    @eval_fn
    def AW24():
        aw18_1 = Coal.AW18()
        var_1 = equal(aw18_1, 0)
        aw6_1 = Coal.AW6()
        aw12_1 = Coal.AW12()
        var_2 = mult(aw6_1, aw12_1)
        aw18_2 = Coal.AW18()
        var_3 = divide(var_2, aw18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AX24():
    # 'Coal'!AX24
    value = 0.0886946461855
    formula = "=IF(AX18=0,0,(AX6*AX12)/AX18)"
    @eval_fn
    def AX24():
        ax18_1 = Coal.AX18()
        var_1 = equal(ax18_1, 0)
        ax6_1 = Coal.AX6()
        ax12_1 = Coal.AX12()
        var_2 = mult(ax6_1, ax12_1)
        ax18_2 = Coal.AX18()
        var_3 = divide(var_2, ax18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AY24():
    # 'Coal'!AY24
    value = 0.0886946461855
    formula = "=IF(AY18=0,0,(AY6*AY12)/AY18)"
    @eval_fn
    def AY24():
        ay18_1 = Coal.AY18()
        var_1 = equal(ay18_1, 0)
        ay6_1 = Coal.AY6()
        ay12_1 = Coal.AY12()
        var_2 = mult(ay6_1, ay12_1)
        ay18_2 = Coal.AY18()
        var_3 = divide(var_2, ay18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class AZ24():
    # 'Coal'!AZ24
    value = 0.0886946461855
    formula = "=IF(AZ18=0,0,(AZ6*AZ12)/AZ18)"
    @eval_fn
    def AZ24():
        az18_1 = Coal.AZ18()
        var_1 = equal(az18_1, 0)
        az6_1 = Coal.AZ6()
        az12_1 = Coal.AZ12()
        var_2 = mult(az6_1, az12_1)
        az18_2 = Coal.AZ18()
        var_3 = divide(var_2, az18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BA24():
    # 'Coal'!BA24
    value = 0.0886946461855
    formula = "=IF(BA18=0,0,(BA6*BA12)/BA18)"
    @eval_fn
    def BA24():
        ba18_1 = Coal.BA18()
        var_1 = equal(ba18_1, 0)
        ba6_1 = Coal.BA6()
        ba12_1 = Coal.BA12()
        var_2 = mult(ba6_1, ba12_1)
        ba18_2 = Coal.BA18()
        var_3 = divide(var_2, ba18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BB24():
    # 'Coal'!BB24
    value = 0.0886946461855
    formula = "=IF(BB18=0,0,(BB6*BB12)/BB18)"
    @eval_fn
    def BB24():
        bb18_1 = Coal.BB18()
        var_1 = equal(bb18_1, 0)
        bb6_1 = Coal.BB6()
        bb12_1 = Coal.BB12()
        var_2 = mult(bb6_1, bb12_1)
        bb18_2 = Coal.BB18()
        var_3 = divide(var_2, bb18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BC24():
    # 'Coal'!BC24
    value = 0.0886946461855
    formula = "=IF(BC18=0,0,(BC6*BC12)/BC18)"
    @eval_fn
    def BC24():
        bc18_1 = Coal.BC18()
        var_1 = equal(bc18_1, 0)
        bc6_1 = Coal.BC6()
        bc12_1 = Coal.BC12()
        var_2 = mult(bc6_1, bc12_1)
        bc18_2 = Coal.BC18()
        var_3 = divide(var_2, bc18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BD24():
    # 'Coal'!BD24
    value = 0.0886946461855
    formula = "=IF(BD18=0,0,(BD6*BD12)/BD18)"
    @eval_fn
    def BD24():
        bd18_1 = Coal.BD18()
        var_1 = equal(bd18_1, 0)
        bd6_1 = Coal.BD6()
        bd12_1 = Coal.BD12()
        var_2 = mult(bd6_1, bd12_1)
        bd18_2 = Coal.BD18()
        var_3 = divide(var_2, bd18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BE24():
    # 'Coal'!BE24
    value = 0.0886946461855
    formula = "=IF(BE18=0,0,(BE6*BE12)/BE18)"
    @eval_fn
    def BE24():
        be18_1 = Coal.BE18()
        var_1 = equal(be18_1, 0)
        be6_1 = Coal.BE6()
        be12_1 = Coal.BE12()
        var_2 = mult(be6_1, be12_1)
        be18_2 = Coal.BE18()
        var_3 = divide(var_2, be18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BF24():
    # 'Coal'!BF24
    value = "#N/A"
    formula = "=IF(BF18=0,0,(BF6*BF12)/BF18)"
    @eval_fn
    def BF24():
        bf18_1 = Coal.BF18()
        var_1 = equal(bf18_1, 0)
        bf6_1 = Coal.BF6()
        bf12_1 = Coal.BF12()
        var_2 = mult(bf6_1, bf12_1)
        bf18_2 = Coal.BF18()
        var_3 = divide(var_2, bf18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BG24():
    # 'Coal'!BG24
    value = "#N/A"
    formula = "=IF(BG18=0,0,(BG6*BG12)/BG18)"
    @eval_fn
    def BG24():
        bg18_1 = Coal.BG18()
        var_1 = equal(bg18_1, 0)
        bg6_1 = Coal.BG6()
        bg12_1 = Coal.BG12()
        var_2 = mult(bg6_1, bg12_1)
        bg18_2 = Coal.BG18()
        var_3 = divide(var_2, bg18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BH24():
    # 'Coal'!BH24
    value = "#N/A"
    formula = "=IF(BH18=0,0,(BH6*BH12)/BH18)"
    @eval_fn
    def BH24():
        bh18_1 = Coal.BH18()
        var_1 = equal(bh18_1, 0)
        bh6_1 = Coal.BH6()
        bh12_1 = Coal.BH12()
        var_2 = mult(bh6_1, bh12_1)
        bh18_2 = Coal.BH18()
        var_3 = divide(var_2, bh18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BI24():
    # 'Coal'!BI24
    value = "#N/A"
    formula = "=IF(BI18=0,0,(BI6*BI12)/BI18)"
    @eval_fn
    def BI24():
        bi18_1 = Coal.BI18()
        var_1 = equal(bi18_1, 0)
        bi6_1 = Coal.BI6()
        bi12_1 = Coal.BI12()
        var_2 = mult(bi6_1, bi12_1)
        bi18_2 = Coal.BI18()
        var_3 = divide(var_2, bi18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BJ24():
    # 'Coal'!BJ24
    value = "#N/A"
    formula = "=IF(BJ18=0,0,(BJ6*BJ12)/BJ18)"
    @eval_fn
    def BJ24():
        bj18_1 = Coal.BJ18()
        var_1 = equal(bj18_1, 0)
        bj6_1 = Coal.BJ6()
        bj12_1 = Coal.BJ12()
        var_2 = mult(bj6_1, bj12_1)
        bj18_2 = Coal.BJ18()
        var_3 = divide(var_2, bj18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BK24():
    # 'Coal'!BK24
    value = "#N/A"
    formula = "=IF(BK18=0,0,(BK6*BK12)/BK18)"
    @eval_fn
    def BK24():
        bk18_1 = Coal.BK18()
        var_1 = equal(bk18_1, 0)
        bk6_1 = Coal.BK6()
        bk12_1 = Coal.BK12()
        var_2 = mult(bk6_1, bk12_1)
        bk18_2 = Coal.BK18()
        var_3 = divide(var_2, bk18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class BL24():
    # 'Coal'!BL24
    value = "#N/A"
    formula = "=IF(BL18=0,0,(BL6*BL12)/BL18)"
    @eval_fn
    def BL24():
        bl18_1 = Coal.BL18()
        var_1 = equal(bl18_1, 0)
        bl6_1 = Coal.BL6()
        bl12_1 = Coal.BL12()
        var_2 = mult(bl6_1, bl12_1)
        bl18_2 = Coal.BL18()
        var_3 = divide(var_2, bl18_2)
        var_4 = IF(var_1, 0, var_3)
        return var_4

@register(Coal)
class A26():
    # 'Coal'!A26
    value = "Upstream BTU (BTU attributable to raw materials acquisition and raw materials transport"

@register(Coal)
class C26():
    # 'Coal'!C26
    value = "Total WTW (Well-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A27():
    # 'Coal'!A27
    value = "US"

@register(Coal)
class B27():
    # 'Coal'!B27
    value = "Mmbtu"

@register(Coal)
class E27():
    # 'Coal'!E27
    value = 0
    formula = "=E24*E6"
    @eval_fn
    def E27():
        e24_1 = Coal.E24()
        e6_1 = Coal.E6()
        var_1 = mult(e24_1, e6_1)
        return var_1

@register(Coal)
class F27():
    # 'Coal'!F27
    value = 0
    formula = "=F24*F6"
    @eval_fn
    def F27():
        f24_1 = Coal.F24()
        f6_1 = Coal.F6()
        var_1 = mult(f24_1, f6_1)
        return var_1

@register(Coal)
class G27():
    # 'Coal'!G27
    value = 0
    formula = "=G24*G6"
    @eval_fn
    def G27():
        g24_1 = Coal.G24()
        g6_1 = Coal.G6()
        var_1 = mult(g24_1, g6_1)
        return var_1

@register(Coal)
class H27():
    # 'Coal'!H27
    value = 0
    formula = "=H24*H6"
    @eval_fn
    def H27():
        h24_1 = Coal.H24()
        h6_1 = Coal.H6()
        var_1 = mult(h24_1, h6_1)
        return var_1

@register(Coal)
class I27():
    # 'Coal'!I27
    value = 0
    formula = "=I24*I6"
    @eval_fn
    def I27():
        i24_1 = Coal.I24()
        i6_1 = Coal.I6()
        var_1 = mult(i24_1, i6_1)
        return var_1

@register(Coal)
class J27():
    # 'Coal'!J27
    value = 0
    formula = "=J24*J6"
    @eval_fn
    def J27():
        j24_1 = Coal.J24()
        j6_1 = Coal.J6()
        var_1 = mult(j24_1, j6_1)
        return var_1

@register(Coal)
class K27():
    # 'Coal'!K27
    value = 0
    formula = "=K24*K6"
    @eval_fn
    def K27():
        k24_1 = Coal.K24()
        k6_1 = Coal.K6()
        var_1 = mult(k24_1, k6_1)
        return var_1

@register(Coal)
class L27():
    # 'Coal'!L27
    value = 0
    formula = "=L24*L6"
    @eval_fn
    def L27():
        l24_1 = Coal.L24()
        l6_1 = Coal.L6()
        var_1 = mult(l24_1, l6_1)
        return var_1

@register(Coal)
class M27():
    # 'Coal'!M27
    value = 0
    formula = "=M24*M6"
    @eval_fn
    def M27():
        m24_1 = Coal.M24()
        m6_1 = Coal.M6()
        var_1 = mult(m24_1, m6_1)
        return var_1

@register(Coal)
class N27():
    # 'Coal'!N27
    value = 0
    formula = "=N24*N6"
    @eval_fn
    def N27():
        n24_1 = Coal.N24()
        n6_1 = Coal.N6()
        var_1 = mult(n24_1, n6_1)
        return var_1

@register(Coal)
class O27():
    # 'Coal'!O27
    value = 0
    formula = "=O24*O6"
    @eval_fn
    def O27():
        o24_1 = Coal.O24()
        o6_1 = Coal.O6()
        var_1 = mult(o24_1, o6_1)
        return var_1

@register(Coal)
class P27():
    # 'Coal'!P27
    value = 0
    formula = "=P24*P6"
    @eval_fn
    def P27():
        p24_1 = Coal.P24()
        p6_1 = Coal.P6()
        var_1 = mult(p24_1, p6_1)
        return var_1

@register(Coal)
class Q27():
    # 'Coal'!Q27
    value = 0
    formula = "=Q24*Q6"
    @eval_fn
    def Q27():
        q24_1 = Coal.Q24()
        q6_1 = Coal.Q6()
        var_1 = mult(q24_1, q6_1)
        return var_1

@register(Coal)
class R27():
    # 'Coal'!R27
    value = 0
    formula = "=R24*R6"
    @eval_fn
    def R27():
        r24_1 = Coal.R24()
        r6_1 = Coal.R6()
        var_1 = mult(r24_1, r6_1)
        return var_1

@register(Coal)
class S27():
    # 'Coal'!S27
    value = 0
    formula = "=S24*S6"
    @eval_fn
    def S27():
        s24_1 = Coal.S24()
        s6_1 = Coal.S6()
        var_1 = mult(s24_1, s6_1)
        return var_1

@register(Coal)
class T27():
    # 'Coal'!T27
    value = 0
    formula = "=T24*T6"
    @eval_fn
    def T27():
        t24_1 = Coal.T24()
        t6_1 = Coal.T6()
        var_1 = mult(t24_1, t6_1)
        return var_1

@register(Coal)
class U27():
    # 'Coal'!U27
    value = 0
    formula = "=U24*U6"
    @eval_fn
    def U27():
        u24_1 = Coal.U24()
        u6_1 = Coal.U6()
        var_1 = mult(u24_1, u6_1)
        return var_1

@register(Coal)
class V27():
    # 'Coal'!V27
    value = 0
    formula = "=V24*V6"
    @eval_fn
    def V27():
        v24_1 = Coal.V24()
        v6_1 = Coal.V6()
        var_1 = mult(v24_1, v6_1)
        return var_1

@register(Coal)
class W27():
    # 'Coal'!W27
    value = 0
    formula = "=W24*W6"
    @eval_fn
    def W27():
        w24_1 = Coal.W24()
        w6_1 = Coal.W6()
        var_1 = mult(w24_1, w6_1)
        return var_1

@register(Coal)
class X27():
    # 'Coal'!X27
    value = 0
    formula = "=X24*X6"
    @eval_fn
    def X27():
        x24_1 = Coal.X24()
        x6_1 = Coal.X6()
        var_1 = mult(x24_1, x6_1)
        return var_1

@register(Coal)
class Y27():
    # 'Coal'!Y27
    value = 0
    formula = "=Y24*Y6"
    @eval_fn
    def Y27():
        y24_1 = Coal.Y24()
        y6_1 = Coal.Y6()
        var_1 = mult(y24_1, y6_1)
        return var_1

@register(Coal)
class Z27():
    # 'Coal'!Z27
    value = 101910.148467
    formula = "=Z24*Z6"
    @eval_fn
    def Z27():
        z24_1 = Coal.Z24()
        z6_1 = Coal.Z6()
        var_1 = mult(z24_1, z6_1)
        return var_1

@register(Coal)
class AA27():
    # 'Coal'!AA27
    value = 92242.4320329
    formula = "=AA24*AA6"
    @eval_fn
    def AA27():
        aa24_1 = Coal.AA24()
        aa6_1 = Coal.AA6()
        var_1 = mult(aa24_1, aa6_1)
        return var_1

@register(Coal)
class AB27():
    # 'Coal'!AB27
    value = 83461.6620605
    formula = "=AB24*AB6"
    @eval_fn
    def AB27():
        ab24_1 = Coal.AB24()
        ab6_1 = Coal.AB6()
        var_1 = mult(ab24_1, ab6_1)
        return var_1

@register(Coal)
class AC27():
    # 'Coal'!AC27
    value = 99692.7823125
    formula = "=AC24*AC6"
    @eval_fn
    def AC27():
        ac24_1 = Coal.AC24()
        ac6_1 = Coal.AC6()
        var_1 = mult(ac24_1, ac6_1)
        return var_1

@register(Coal)
class AD27():
    # 'Coal'!AD27
    value = 35034.3852433
    formula = "=AD24*AD6"
    @eval_fn
    def AD27():
        ad24_1 = Coal.AD24()
        ad6_1 = Coal.AD6()
        var_1 = mult(ad24_1, ad6_1)
        return var_1

@register(Coal)
class AE27():
    # 'Coal'!AE27
    value = 139516.67845
    formula = "=AE24*AE6"
    @eval_fn
    def AE27():
        ae24_1 = Coal.AE24()
        ae6_1 = Coal.AE6()
        var_1 = mult(ae24_1, ae6_1)
        return var_1

@register(Coal)
class AF27():
    # 'Coal'!AF27
    value = 110158.750562
    formula = "=AF24*AF6"
    @eval_fn
    def AF27():
        af24_1 = Coal.AF24()
        af6_1 = Coal.AF6()
        var_1 = mult(af24_1, af6_1)
        return var_1

@register(Coal)
class AG27():
    # 'Coal'!AG27
    value = 70512.2437175
    formula = "=AG24*AG6"
    @eval_fn
    def AG27():
        ag24_1 = Coal.AG24()
        ag6_1 = Coal.AG6()
        var_1 = mult(ag24_1, ag6_1)
        return var_1

@register(Coal)
class AH27():
    # 'Coal'!AH27
    value = 63948.8398997
    formula = "=AH24*AH6"
    @eval_fn
    def AH27():
        ah24_1 = Coal.AH24()
        ah6_1 = Coal.AH6()
        var_1 = mult(ah24_1, ah6_1)
        return var_1

@register(Coal)
class AI27():
    # 'Coal'!AI27
    value = 94282.4088952
    formula = "=AI24*AI6"
    @eval_fn
    def AI27():
        ai24_1 = Coal.AI24()
        ai6_1 = Coal.AI6()
        var_1 = mult(ai24_1, ai6_1)
        return var_1

@register(Coal)
class AJ27():
    # 'Coal'!AJ27
    value = 598688.861752
    formula = "=AJ24*AJ6"
    @eval_fn
    def AJ27():
        aj24_1 = Coal.AJ24()
        aj6_1 = Coal.AJ6()
        var_1 = mult(aj24_1, aj6_1)
        return var_1

@register(Coal)
class AK27():
    # 'Coal'!AK27
    value = 1381419.11434
    formula = "=AK24*AK6"
    @eval_fn
    def AK27():
        ak24_1 = Coal.AK24()
        ak6_1 = Coal.AK6()
        var_1 = mult(ak24_1, ak6_1)
        return var_1

@register(Coal)
class AL27():
    # 'Coal'!AL27
    value = 1396053.73096
    formula = "=AL24*AL6"
    @eval_fn
    def AL27():
        al24_1 = Coal.AL24()
        al6_1 = Coal.AL6()
        var_1 = mult(al24_1, al6_1)
        return var_1

@register(Coal)
class AM27():
    # 'Coal'!AM27
    value = 1766265.18414
    formula = "=AM24*AM6"
    @eval_fn
    def AM27():
        am24_1 = Coal.AM24()
        am6_1 = Coal.AM6()
        var_1 = mult(am24_1, am6_1)
        return var_1

@register(Coal)
class AN27():
    # 'Coal'!AN27
    value = 1806798.63744
    formula = "=AN24*AN6"
    @eval_fn
    def AN27():
        an24_1 = Coal.AN24()
        an6_1 = Coal.AN6()
        var_1 = mult(an24_1, an6_1)
        return var_1

@register(Coal)
class AO27():
    # 'Coal'!AO27
    value = 1819393.2772
    formula = "=AO24*AO6"
    @eval_fn
    def AO27():
        ao24_1 = Coal.AO24()
        ao6_1 = Coal.AO6()
        var_1 = mult(ao24_1, ao6_1)
        return var_1

@register(Coal)
class AP27():
    # 'Coal'!AP27
    value = 1616282.53744
    formula = "=AP24*AP6"
    @eval_fn
    def AP27():
        ap24_1 = Coal.AP24()
        ap6_1 = Coal.AP6()
        var_1 = mult(ap24_1, ap6_1)
        return var_1

@register(Coal)
class AQ27():
    # 'Coal'!AQ27
    value = 1569096.98567
    formula = "=AQ24*AQ6"
    @eval_fn
    def AQ27():
        aq24_1 = Coal.AQ24()
        aq6_1 = Coal.AQ6()
        var_1 = mult(aq24_1, aq6_1)
        return var_1

@register(Coal)
class AR27():
    # 'Coal'!AR27
    value = 1565726.58911
    formula = "=AR24*AR6"
    @eval_fn
    def AR27():
        ar24_1 = Coal.AR24()
        ar6_1 = Coal.AR6()
        var_1 = mult(ar24_1, ar6_1)
        return var_1

@register(Coal)
class AS27():
    # 'Coal'!AS27
    value = 1576458.6413
    formula = "=AS24*AS6"
    @eval_fn
    def AS27():
        as24_1 = Coal.AS24()
        as6_1 = Coal.AS6()
        var_1 = mult(as24_1, as6_1)
        return var_1

@register(Coal)
class AT27():
    # 'Coal'!AT27
    value = 1473927.63031
    formula = "=AT24*AT6"
    @eval_fn
    def AT27():
        at24_1 = Coal.AT24()
        at6_1 = Coal.AT6()
        var_1 = mult(at24_1, at6_1)
        return var_1

@register(Coal)
class AU27():
    # 'Coal'!AU27
    value = 1707904.10695
    formula = "=AU24*AU6"
    @eval_fn
    def AU27():
        au24_1 = Coal.AU24()
        au6_1 = Coal.AU6()
        var_1 = mult(au24_1, au6_1)
        return var_1

@register(Coal)
class AV27():
    # 'Coal'!AV27
    value = 1707726.71766
    formula = "=AV24*AV6"
    @eval_fn
    def AV27():
        av24_1 = Coal.AV24()
        av6_1 = Coal.AV6()
        var_1 = mult(av24_1, av6_1)
        return var_1

@register(Coal)
class AW27():
    # 'Coal'!AW27
    value = 1592601.06691
    formula = "=AW24*AW6"
    @eval_fn
    def AW27():
        aw24_1 = Coal.AW24()
        aw6_1 = Coal.AW6()
        var_1 = mult(aw24_1, aw6_1)
        return var_1

@register(Coal)
class AX27():
    # 'Coal'!AX27
    value = 1554551.06369
    formula = "=AX24*AX6"
    @eval_fn
    def AX27():
        ax24_1 = Coal.AX24()
        ax6_1 = Coal.AX6()
        var_1 = mult(ax24_1, ax6_1)
        return var_1

@register(Coal)
class AY27():
    # 'Coal'!AY27
    value = 1685819.14005
    formula = "=AY24*AY6"
    @eval_fn
    def AY27():
        ay24_1 = Coal.AY24()
        ay6_1 = Coal.AY6()
        var_1 = mult(ay24_1, ay6_1)
        return var_1

@register(Coal)
class AZ27():
    # 'Coal'!AZ27
    value = 1787906.67781
    formula = "=AZ24*AZ6"
    @eval_fn
    def AZ27():
        az24_1 = Coal.AZ24()
        az6_1 = Coal.AZ6()
        var_1 = mult(az24_1, az6_1)
        return var_1

@register(Coal)
class BA27():
    # 'Coal'!BA27
    value = 1681473.10238
    formula = "=BA24*BA6"
    @eval_fn
    def BA27():
        ba24_1 = Coal.BA24()
        ba6_1 = Coal.BA6()
        var_1 = mult(ba24_1, ba6_1)
        return var_1

@register(Coal)
class BB27():
    # 'Coal'!BB27
    value = 1518186.25876
    formula = "=BB24*BB6"
    @eval_fn
    def BB27():
        bb24_1 = Coal.BB24()
        bb6_1 = Coal.BB6()
        var_1 = mult(bb24_1, bb6_1)
        return var_1

@register(Coal)
class BC27():
    # 'Coal'!BC27
    value = 1426209.91066
    formula = "=BC24*BC6"
    @eval_fn
    def BC27():
        bc24_1 = Coal.BC24()
        bc6_1 = Coal.BC6()
        var_1 = mult(bc24_1, bc6_1)
        return var_1

@register(Coal)
class BD27():
    # 'Coal'!BD27
    value = 1469847.67659
    formula = "=BD24*BD6"
    @eval_fn
    def BD27():
        bd24_1 = Coal.BD24()
        bd6_1 = Coal.BD6()
        var_1 = mult(bd24_1, bd6_1)
        return var_1

@register(Coal)
class BE27():
    # 'Coal'!BE27
    value = 1357560.25452
    formula = "=BE24*BE6"
    @eval_fn
    def BE27():
        be24_1 = Coal.BE24()
        be6_1 = Coal.BE6()
        var_1 = mult(be24_1, be6_1)
        return var_1

@register(Coal)
class BF27():
    # 'Coal'!BF27
    value = "#N/A"
    formula = "=BF24*BF6"
    @eval_fn
    def BF27():
        bf24_1 = Coal.BF24()
        bf6_1 = Coal.BF6()
        var_1 = mult(bf24_1, bf6_1)
        return var_1

@register(Coal)
class BG27():
    # 'Coal'!BG27
    value = "#N/A"
    formula = "=BG24*BG6"
    @eval_fn
    def BG27():
        bg24_1 = Coal.BG24()
        bg6_1 = Coal.BG6()
        var_1 = mult(bg24_1, bg6_1)
        return var_1

@register(Coal)
class BH27():
    # 'Coal'!BH27
    value = "#N/A"
    formula = "=BH24*BH6"
    @eval_fn
    def BH27():
        bh24_1 = Coal.BH24()
        bh6_1 = Coal.BH6()
        var_1 = mult(bh24_1, bh6_1)
        return var_1

@register(Coal)
class BI27():
    # 'Coal'!BI27
    value = "#N/A"
    formula = "=BI24*BI6"
    @eval_fn
    def BI27():
        bi24_1 = Coal.BI24()
        bi6_1 = Coal.BI6()
        var_1 = mult(bi24_1, bi6_1)
        return var_1

@register(Coal)
class BJ27():
    # 'Coal'!BJ27
    value = "#N/A"
    formula = "=BJ24*BJ6"
    @eval_fn
    def BJ27():
        bj24_1 = Coal.BJ24()
        bj6_1 = Coal.BJ6()
        var_1 = mult(bj24_1, bj6_1)
        return var_1

@register(Coal)
class BK27():
    # 'Coal'!BK27
    value = "#N/A"
    formula = "=BK24*BK6"
    @eval_fn
    def BK27():
        bk24_1 = Coal.BK24()
        bk6_1 = Coal.BK6()
        var_1 = mult(bk24_1, bk6_1)
        return var_1

@register(Coal)
class BL27():
    # 'Coal'!BL27
    value = "#N/A"
    formula = "=BL24*BL6"
    @eval_fn
    def BL27():
        bl24_1 = Coal.BL24()
        bl6_1 = Coal.BL6()
        var_1 = mult(bl24_1, bl6_1)
        return var_1

@register(Coal)
class A29():
    # 'Coal'!A29
    value = "Upstream BTU (BTU attributable to raw materials acquisition and raw materials transport"

@register(Coal)
class C29():
    # 'Coal'!C29
    value = "Total WTW (Well-to-Tank) (kgCO2/MMBtu)"

@register(Coal)
class A30():
    # 'Coal'!A30
    value = "US"

@register(Coal)
class B30():
    # 'Coal'!B30
    value = "Mmbtu"

@register(Coal)
class E30():
    # 'Coal'!E30
    value = 0
    formula = "=IF(E6=0,0,E27/E6)"
    @eval_fn
    def E30():
        e6_1 = Coal.E6()
        var_1 = equal(e6_1, 0)
        e27_1 = Coal.E27()
        e6_2 = Coal.E6()
        var_2 = divide(e27_1, e6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class F30():
    # 'Coal'!F30
    value = 0
    formula = "=IF(F6=0,0,F27/F6)"
    @eval_fn
    def F30():
        f6_1 = Coal.F6()
        var_1 = equal(f6_1, 0)
        f27_1 = Coal.F27()
        f6_2 = Coal.F6()
        var_2 = divide(f27_1, f6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class G30():
    # 'Coal'!G30
    value = 0
    formula = "=IF(G6=0,0,G27/G6)"
    @eval_fn
    def G30():
        g6_1 = Coal.G6()
        var_1 = equal(g6_1, 0)
        g27_1 = Coal.G27()
        g6_2 = Coal.G6()
        var_2 = divide(g27_1, g6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class H30():
    # 'Coal'!H30
    value = 0
    formula = "=IF(H6=0,0,H27/H6)"
    @eval_fn
    def H30():
        h6_1 = Coal.H6()
        var_1 = equal(h6_1, 0)
        h27_1 = Coal.H27()
        h6_2 = Coal.H6()
        var_2 = divide(h27_1, h6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class I30():
    # 'Coal'!I30
    value = 0
    formula = "=IF(I6=0,0,I27/I6)"
    @eval_fn
    def I30():
        i6_1 = Coal.I6()
        var_1 = equal(i6_1, 0)
        i27_1 = Coal.I27()
        i6_2 = Coal.I6()
        var_2 = divide(i27_1, i6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class J30():
    # 'Coal'!J30
    value = 0
    formula = "=IF(J6=0,0,J27/J6)"
    @eval_fn
    def J30():
        j6_1 = Coal.J6()
        var_1 = equal(j6_1, 0)
        j27_1 = Coal.J27()
        j6_2 = Coal.J6()
        var_2 = divide(j27_1, j6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class K30():
    # 'Coal'!K30
    value = 0
    formula = "=IF(K6=0,0,K27/K6)"
    @eval_fn
    def K30():
        k6_1 = Coal.K6()
        var_1 = equal(k6_1, 0)
        k27_1 = Coal.K27()
        k6_2 = Coal.K6()
        var_2 = divide(k27_1, k6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class L30():
    # 'Coal'!L30
    value = 0
    formula = "=IF(L6=0,0,L27/L6)"
    @eval_fn
    def L30():
        l6_1 = Coal.L6()
        var_1 = equal(l6_1, 0)
        l27_1 = Coal.L27()
        l6_2 = Coal.L6()
        var_2 = divide(l27_1, l6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class M30():
    # 'Coal'!M30
    value = 0
    formula = "=IF(M6=0,0,M27/M6)"
    @eval_fn
    def M30():
        m6_1 = Coal.M6()
        var_1 = equal(m6_1, 0)
        m27_1 = Coal.M27()
        m6_2 = Coal.M6()
        var_2 = divide(m27_1, m6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class N30():
    # 'Coal'!N30
    value = 0
    formula = "=IF(N6=0,0,N27/N6)"
    @eval_fn
    def N30():
        n6_1 = Coal.N6()
        var_1 = equal(n6_1, 0)
        n27_1 = Coal.N27()
        n6_2 = Coal.N6()
        var_2 = divide(n27_1, n6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class O30():
    # 'Coal'!O30
    value = 0
    formula = "=IF(O6=0,0,O27/O6)"
    @eval_fn
    def O30():
        o6_1 = Coal.O6()
        var_1 = equal(o6_1, 0)
        o27_1 = Coal.O27()
        o6_2 = Coal.O6()
        var_2 = divide(o27_1, o6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class P30():
    # 'Coal'!P30
    value = 0
    formula = "=IF(P6=0,0,P27/P6)"
    @eval_fn
    def P30():
        p6_1 = Coal.P6()
        var_1 = equal(p6_1, 0)
        p27_1 = Coal.P27()
        p6_2 = Coal.P6()
        var_2 = divide(p27_1, p6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class Q30():
    # 'Coal'!Q30
    value = 0
    formula = "=IF(Q6=0,0,Q27/Q6)"
    @eval_fn
    def Q30():
        q6_1 = Coal.Q6()
        var_1 = equal(q6_1, 0)
        q27_1 = Coal.Q27()
        q6_2 = Coal.Q6()
        var_2 = divide(q27_1, q6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class R30():
    # 'Coal'!R30
    value = 0
    formula = "=IF(R6=0,0,R27/R6)"
    @eval_fn
    def R30():
        r6_1 = Coal.R6()
        var_1 = equal(r6_1, 0)
        r27_1 = Coal.R27()
        r6_2 = Coal.R6()
        var_2 = divide(r27_1, r6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class S30():
    # 'Coal'!S30
    value = 0
    formula = "=IF(S6=0,0,S27/S6)"
    @eval_fn
    def S30():
        s6_1 = Coal.S6()
        var_1 = equal(s6_1, 0)
        s27_1 = Coal.S27()
        s6_2 = Coal.S6()
        var_2 = divide(s27_1, s6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class T30():
    # 'Coal'!T30
    value = 0
    formula = "=IF(T6=0,0,T27/T6)"
    @eval_fn
    def T30():
        t6_1 = Coal.T6()
        var_1 = equal(t6_1, 0)
        t27_1 = Coal.T27()
        t6_2 = Coal.T6()
        var_2 = divide(t27_1, t6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class U30():
    # 'Coal'!U30
    value = 0
    formula = "=IF(U6=0,0,U27/U6)"
    @eval_fn
    def U30():
        u6_1 = Coal.U6()
        var_1 = equal(u6_1, 0)
        u27_1 = Coal.U27()
        u6_2 = Coal.U6()
        var_2 = divide(u27_1, u6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class V30():
    # 'Coal'!V30
    value = 0
    formula = "=IF(V6=0,0,V27/V6)"
    @eval_fn
    def V30():
        v6_1 = Coal.V6()
        var_1 = equal(v6_1, 0)
        v27_1 = Coal.V27()
        v6_2 = Coal.V6()
        var_2 = divide(v27_1, v6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class W30():
    # 'Coal'!W30
    value = 0
    formula = "=IF(W6=0,0,W27/W6)"
    @eval_fn
    def W30():
        w6_1 = Coal.W6()
        var_1 = equal(w6_1, 0)
        w27_1 = Coal.W27()
        w6_2 = Coal.W6()
        var_2 = divide(w27_1, w6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class X30():
    # 'Coal'!X30
    value = 0
    formula = "=IF(X6=0,0,X27/X6)"
    @eval_fn
    def X30():
        x6_1 = Coal.X6()
        var_1 = equal(x6_1, 0)
        x27_1 = Coal.X27()
        x6_2 = Coal.X6()
        var_2 = divide(x27_1, x6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class Y30():
    # 'Coal'!Y30
    value = 0
    formula = "=IF(Y6=0,0,Y27/Y6)"
    @eval_fn
    def Y30():
        y6_1 = Coal.Y6()
        var_1 = equal(y6_1, 0)
        y27_1 = Coal.Y27()
        y6_2 = Coal.Y6()
        var_2 = divide(y27_1, y6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class Z30():
    # 'Coal'!Z30
    value = 0.0886946461855
    formula = "=IF(Z6=0,0,Z27/Z6)"
    @eval_fn
    def Z30():
        z6_1 = Coal.Z6()
        var_1 = equal(z6_1, 0)
        z27_1 = Coal.Z27()
        z6_2 = Coal.Z6()
        var_2 = divide(z27_1, z6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AA30():
    # 'Coal'!AA30
    value = 0.0886946461855
    formula = "=IF(AA6=0,0,AA27/AA6)"
    @eval_fn
    def AA30():
        aa6_1 = Coal.AA6()
        var_1 = equal(aa6_1, 0)
        aa27_1 = Coal.AA27()
        aa6_2 = Coal.AA6()
        var_2 = divide(aa27_1, aa6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AB30():
    # 'Coal'!AB30
    value = 0.0886946461855
    formula = "=IF(AB6=0,0,AB27/AB6)"
    @eval_fn
    def AB30():
        ab6_1 = Coal.AB6()
        var_1 = equal(ab6_1, 0)
        ab27_1 = Coal.AB27()
        ab6_2 = Coal.AB6()
        var_2 = divide(ab27_1, ab6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AC30():
    # 'Coal'!AC30
    value = 0.0886946461855
    formula = "=IF(AC6=0,0,AC27/AC6)"
    @eval_fn
    def AC30():
        ac6_1 = Coal.AC6()
        var_1 = equal(ac6_1, 0)
        ac27_1 = Coal.AC27()
        ac6_2 = Coal.AC6()
        var_2 = divide(ac27_1, ac6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AD30():
    # 'Coal'!AD30
    value = 0.0886946461855
    formula = "=IF(AD6=0,0,AD27/AD6)"
    @eval_fn
    def AD30():
        ad6_1 = Coal.AD6()
        var_1 = equal(ad6_1, 0)
        ad27_1 = Coal.AD27()
        ad6_2 = Coal.AD6()
        var_2 = divide(ad27_1, ad6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AE30():
    # 'Coal'!AE30
    value = 0.0886946461855
    formula = "=IF(AE6=0,0,AE27/AE6)"
    @eval_fn
    def AE30():
        ae6_1 = Coal.AE6()
        var_1 = equal(ae6_1, 0)
        ae27_1 = Coal.AE27()
        ae6_2 = Coal.AE6()
        var_2 = divide(ae27_1, ae6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AF30():
    # 'Coal'!AF30
    value = 0.0886946461855
    formula = "=IF(AF6=0,0,AF27/AF6)"
    @eval_fn
    def AF30():
        af6_1 = Coal.AF6()
        var_1 = equal(af6_1, 0)
        af27_1 = Coal.AF27()
        af6_2 = Coal.AF6()
        var_2 = divide(af27_1, af6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AG30():
    # 'Coal'!AG30
    value = 0.0886946461855
    formula = "=IF(AG6=0,0,AG27/AG6)"
    @eval_fn
    def AG30():
        ag6_1 = Coal.AG6()
        var_1 = equal(ag6_1, 0)
        ag27_1 = Coal.AG27()
        ag6_2 = Coal.AG6()
        var_2 = divide(ag27_1, ag6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AH30():
    # 'Coal'!AH30
    value = 0.0886946461855
    formula = "=IF(AH6=0,0,AH27/AH6)"
    @eval_fn
    def AH30():
        ah6_1 = Coal.AH6()
        var_1 = equal(ah6_1, 0)
        ah27_1 = Coal.AH27()
        ah6_2 = Coal.AH6()
        var_2 = divide(ah27_1, ah6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AI30():
    # 'Coal'!AI30
    value = 0.0886946461855
    formula = "=IF(AI6=0,0,AI27/AI6)"
    @eval_fn
    def AI30():
        ai6_1 = Coal.AI6()
        var_1 = equal(ai6_1, 0)
        ai27_1 = Coal.AI27()
        ai6_2 = Coal.AI6()
        var_2 = divide(ai27_1, ai6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AJ30():
    # 'Coal'!AJ30
    value = 0.0886946461855
    formula = "=IF(AJ6=0,0,AJ27/AJ6)"
    @eval_fn
    def AJ30():
        aj6_1 = Coal.AJ6()
        var_1 = equal(aj6_1, 0)
        aj27_1 = Coal.AJ27()
        aj6_2 = Coal.AJ6()
        var_2 = divide(aj27_1, aj6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AK30():
    # 'Coal'!AK30
    value = 0.0886946461855
    formula = "=IF(AK6=0,0,AK27/AK6)"
    @eval_fn
    def AK30():
        ak6_1 = Coal.AK6()
        var_1 = equal(ak6_1, 0)
        ak27_1 = Coal.AK27()
        ak6_2 = Coal.AK6()
        var_2 = divide(ak27_1, ak6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AL30():
    # 'Coal'!AL30
    value = 0.0886946461855
    formula = "=IF(AL6=0,0,AL27/AL6)"
    @eval_fn
    def AL30():
        al6_1 = Coal.AL6()
        var_1 = equal(al6_1, 0)
        al27_1 = Coal.AL27()
        al6_2 = Coal.AL6()
        var_2 = divide(al27_1, al6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AM30():
    # 'Coal'!AM30
    value = 0.0886946461855
    formula = "=IF(AM6=0,0,AM27/AM6)"
    @eval_fn
    def AM30():
        am6_1 = Coal.AM6()
        var_1 = equal(am6_1, 0)
        am27_1 = Coal.AM27()
        am6_2 = Coal.AM6()
        var_2 = divide(am27_1, am6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AN30():
    # 'Coal'!AN30
    value = 0.0886946461855
    formula = "=IF(AN6=0,0,AN27/AN6)"
    @eval_fn
    def AN30():
        an6_1 = Coal.AN6()
        var_1 = equal(an6_1, 0)
        an27_1 = Coal.AN27()
        an6_2 = Coal.AN6()
        var_2 = divide(an27_1, an6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AO30():
    # 'Coal'!AO30
    value = 0.0886946461855
    formula = "=IF(AO6=0,0,AO27/AO6)"
    @eval_fn
    def AO30():
        ao6_1 = Coal.AO6()
        var_1 = equal(ao6_1, 0)
        ao27_1 = Coal.AO27()
        ao6_2 = Coal.AO6()
        var_2 = divide(ao27_1, ao6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AP30():
    # 'Coal'!AP30
    value = 0.0886946461855
    formula = "=IF(AP6=0,0,AP27/AP6)"
    @eval_fn
    def AP30():
        ap6_1 = Coal.AP6()
        var_1 = equal(ap6_1, 0)
        ap27_1 = Coal.AP27()
        ap6_2 = Coal.AP6()
        var_2 = divide(ap27_1, ap6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AQ30():
    # 'Coal'!AQ30
    value = 0.0886946461855
    formula = "=IF(AQ6=0,0,AQ27/AQ6)"
    @eval_fn
    def AQ30():
        aq6_1 = Coal.AQ6()
        var_1 = equal(aq6_1, 0)
        aq27_1 = Coal.AQ27()
        aq6_2 = Coal.AQ6()
        var_2 = divide(aq27_1, aq6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AR30():
    # 'Coal'!AR30
    value = 0.0886946461855
    formula = "=IF(AR6=0,0,AR27/AR6)"
    @eval_fn
    def AR30():
        ar6_1 = Coal.AR6()
        var_1 = equal(ar6_1, 0)
        ar27_1 = Coal.AR27()
        ar6_2 = Coal.AR6()
        var_2 = divide(ar27_1, ar6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AS30():
    # 'Coal'!AS30
    value = 0.0886946461855
    formula = "=IF(AS6=0,0,AS27/AS6)"
    @eval_fn
    def AS30():
        as6_1 = Coal.AS6()
        var_1 = equal(as6_1, 0)
        as27_1 = Coal.AS27()
        as6_2 = Coal.AS6()
        var_2 = divide(as27_1, as6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AT30():
    # 'Coal'!AT30
    value = 0.0886946461855
    formula = "=IF(AT6=0,0,AT27/AT6)"
    @eval_fn
    def AT30():
        at6_1 = Coal.AT6()
        var_1 = equal(at6_1, 0)
        at27_1 = Coal.AT27()
        at6_2 = Coal.AT6()
        var_2 = divide(at27_1, at6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AU30():
    # 'Coal'!AU30
    value = 0.0886946461855
    formula = "=IF(AU6=0,0,AU27/AU6)"
    @eval_fn
    def AU30():
        au6_1 = Coal.AU6()
        var_1 = equal(au6_1, 0)
        au27_1 = Coal.AU27()
        au6_2 = Coal.AU6()
        var_2 = divide(au27_1, au6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AV30():
    # 'Coal'!AV30
    value = 0.0886946461855
    formula = "=IF(AV6=0,0,AV27/AV6)"
    @eval_fn
    def AV30():
        av6_1 = Coal.AV6()
        var_1 = equal(av6_1, 0)
        av27_1 = Coal.AV27()
        av6_2 = Coal.AV6()
        var_2 = divide(av27_1, av6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AW30():
    # 'Coal'!AW30
    value = 0.0886946461855
    formula = "=IF(AW6=0,0,AW27/AW6)"
    @eval_fn
    def AW30():
        aw6_1 = Coal.AW6()
        var_1 = equal(aw6_1, 0)
        aw27_1 = Coal.AW27()
        aw6_2 = Coal.AW6()
        var_2 = divide(aw27_1, aw6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AX30():
    # 'Coal'!AX30
    value = 0.0886946461855
    formula = "=IF(AX6=0,0,AX27/AX6)"
    @eval_fn
    def AX30():
        ax6_1 = Coal.AX6()
        var_1 = equal(ax6_1, 0)
        ax27_1 = Coal.AX27()
        ax6_2 = Coal.AX6()
        var_2 = divide(ax27_1, ax6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AY30():
    # 'Coal'!AY30
    value = 0.0886946461855
    formula = "=IF(AY6=0,0,AY27/AY6)"
    @eval_fn
    def AY30():
        ay6_1 = Coal.AY6()
        var_1 = equal(ay6_1, 0)
        ay27_1 = Coal.AY27()
        ay6_2 = Coal.AY6()
        var_2 = divide(ay27_1, ay6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class AZ30():
    # 'Coal'!AZ30
    value = 0.0886946461855
    formula = "=IF(AZ6=0,0,AZ27/AZ6)"
    @eval_fn
    def AZ30():
        az6_1 = Coal.AZ6()
        var_1 = equal(az6_1, 0)
        az27_1 = Coal.AZ27()
        az6_2 = Coal.AZ6()
        var_2 = divide(az27_1, az6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BA30():
    # 'Coal'!BA30
    value = 0.0886946461855
    formula = "=IF(BA6=0,0,BA27/BA6)"
    @eval_fn
    def BA30():
        ba6_1 = Coal.BA6()
        var_1 = equal(ba6_1, 0)
        ba27_1 = Coal.BA27()
        ba6_2 = Coal.BA6()
        var_2 = divide(ba27_1, ba6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BB30():
    # 'Coal'!BB30
    value = 0.0886946461855
    formula = "=IF(BB6=0,0,BB27/BB6)"
    @eval_fn
    def BB30():
        bb6_1 = Coal.BB6()
        var_1 = equal(bb6_1, 0)
        bb27_1 = Coal.BB27()
        bb6_2 = Coal.BB6()
        var_2 = divide(bb27_1, bb6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BC30():
    # 'Coal'!BC30
    value = 0.0886946461855
    formula = "=IF(BC6=0,0,BC27/BC6)"
    @eval_fn
    def BC30():
        bc6_1 = Coal.BC6()
        var_1 = equal(bc6_1, 0)
        bc27_1 = Coal.BC27()
        bc6_2 = Coal.BC6()
        var_2 = divide(bc27_1, bc6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BD30():
    # 'Coal'!BD30
    value = 0.0886946461855
    formula = "=IF(BD6=0,0,BD27/BD6)"
    @eval_fn
    def BD30():
        bd6_1 = Coal.BD6()
        var_1 = equal(bd6_1, 0)
        bd27_1 = Coal.BD27()
        bd6_2 = Coal.BD6()
        var_2 = divide(bd27_1, bd6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BE30():
    # 'Coal'!BE30
    value = 0.0886946461855
    formula = "=IF(BE6=0,0,BE27/BE6)"
    @eval_fn
    def BE30():
        be6_1 = Coal.BE6()
        var_1 = equal(be6_1, 0)
        be27_1 = Coal.BE27()
        be6_2 = Coal.BE6()
        var_2 = divide(be27_1, be6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BF30():
    # 'Coal'!BF30
    value = "#N/A"
    formula = "=IF(BF6=0,0,BF27/BF6)"
    @eval_fn
    def BF30():
        bf6_1 = Coal.BF6()
        var_1 = equal(bf6_1, 0)
        bf27_1 = Coal.BF27()
        bf6_2 = Coal.BF6()
        var_2 = divide(bf27_1, bf6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BG30():
    # 'Coal'!BG30
    value = "#N/A"
    formula = "=IF(BG6=0,0,BG27/BG6)"
    @eval_fn
    def BG30():
        bg6_1 = Coal.BG6()
        var_1 = equal(bg6_1, 0)
        bg27_1 = Coal.BG27()
        bg6_2 = Coal.BG6()
        var_2 = divide(bg27_1, bg6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BH30():
    # 'Coal'!BH30
    value = "#N/A"
    formula = "=IF(BH6=0,0,BH27/BH6)"
    @eval_fn
    def BH30():
        bh6_1 = Coal.BH6()
        var_1 = equal(bh6_1, 0)
        bh27_1 = Coal.BH27()
        bh6_2 = Coal.BH6()
        var_2 = divide(bh27_1, bh6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BI30():
    # 'Coal'!BI30
    value = "#N/A"
    formula = "=IF(BI6=0,0,BI27/BI6)"
    @eval_fn
    def BI30():
        bi6_1 = Coal.BI6()
        var_1 = equal(bi6_1, 0)
        bi27_1 = Coal.BI27()
        bi6_2 = Coal.BI6()
        var_2 = divide(bi27_1, bi6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BJ30():
    # 'Coal'!BJ30
    value = "#N/A"
    formula = "=IF(BJ6=0,0,BJ27/BJ6)"
    @eval_fn
    def BJ30():
        bj6_1 = Coal.BJ6()
        var_1 = equal(bj6_1, 0)
        bj27_1 = Coal.BJ27()
        bj6_2 = Coal.BJ6()
        var_2 = divide(bj27_1, bj6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BK30():
    # 'Coal'!BK30
    value = "#N/A"
    formula = "=IF(BK6=0,0,BK27/BK6)"
    @eval_fn
    def BK30():
        bk6_1 = Coal.BK6()
        var_1 = equal(bk6_1, 0)
        bk27_1 = Coal.BK27()
        bk6_2 = Coal.BK6()
        var_2 = divide(bk27_1, bk6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3

@register(Coal)
class BL30():
    # 'Coal'!BL30
    value = "#N/A"
    formula = "=IF(BL6=0,0,BL27/BL6)"
    @eval_fn
    def BL30():
        bl6_1 = Coal.BL6()
        var_1 = equal(bl6_1, 0)
        bl27_1 = Coal.BL27()
        bl6_2 = Coal.BL6()
        var_2 = divide(bl27_1, bl6_2)
        var_3 = IF(var_1, 0, var_2)
        return var_3