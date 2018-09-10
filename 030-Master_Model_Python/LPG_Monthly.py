# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
LPG_Monthly = Worksheet('LPG_Monthly', 10, 10)



@register(LPG_Monthly)
class A1():
    # 'LPG_Monthly'!A1
    value = "LPG Monthly Spot Price"

@register(LPG_Monthly)
class A2():
    # 'LPG_Monthly'!A2
    value = "Year"

@register(LPG_Monthly)
class C2():
    # 'LPG_Monthly'!C2
    value = 1992
    formula = "=YEAR(C3)"
    @eval_fn
    def C2():
        c3_1 = LPG_Monthly.C3()
        var_1 = YEAR(c3_1)
        return var_1

@register(LPG_Monthly)
class D2():
    # 'LPG_Monthly'!D2
    value = 1992
    formula = "=YEAR(D3)"
    @eval_fn
    def D2():
        d3_1 = LPG_Monthly.D3()
        var_1 = YEAR(d3_1)
        return var_1

@register(LPG_Monthly)
class E2():
    # 'LPG_Monthly'!E2
    value = 1992
    formula = "=YEAR(E3)"
    @eval_fn
    def E2():
        e3_1 = LPG_Monthly.E3()
        var_1 = YEAR(e3_1)
        return var_1

@register(LPG_Monthly)
class F2():
    # 'LPG_Monthly'!F2
    value = 1992
    formula = "=YEAR(F3)"
    @eval_fn
    def F2():
        f3_1 = LPG_Monthly.F3()
        var_1 = YEAR(f3_1)
        return var_1

@register(LPG_Monthly)
class G2():
    # 'LPG_Monthly'!G2
    value = 1992
    formula = "=YEAR(G3)"
    @eval_fn
    def G2():
        g3_1 = LPG_Monthly.G3()
        var_1 = YEAR(g3_1)
        return var_1

@register(LPG_Monthly)
class H2():
    # 'LPG_Monthly'!H2
    value = 1992
    formula = "=YEAR(H3)"
    @eval_fn
    def H2():
        h3_1 = LPG_Monthly.H3()
        var_1 = YEAR(h3_1)
        return var_1

@register(LPG_Monthly)
class I2():
    # 'LPG_Monthly'!I2
    value = 1992
    formula = "=YEAR(I3)"
    @eval_fn
    def I2():
        i3_1 = LPG_Monthly.I3()
        var_1 = YEAR(i3_1)
        return var_1

@register(LPG_Monthly)
class J2():
    # 'LPG_Monthly'!J2
    value = 1993
    formula = "=YEAR(J3)"
    @eval_fn
    def J2():
        j3_1 = LPG_Monthly.J3()
        var_1 = YEAR(j3_1)
        return var_1

@register(LPG_Monthly)
class K2():
    # 'LPG_Monthly'!K2
    value = 1993
    formula = "=YEAR(K3)"
    @eval_fn
    def K2():
        k3_1 = LPG_Monthly.K3()
        var_1 = YEAR(k3_1)
        return var_1

@register(LPG_Monthly)
class L2():
    # 'LPG_Monthly'!L2
    value = 1993
    formula = "=YEAR(L3)"
    @eval_fn
    def L2():
        l3_1 = LPG_Monthly.L3()
        var_1 = YEAR(l3_1)
        return var_1

@register(LPG_Monthly)
class M2():
    # 'LPG_Monthly'!M2
    value = 1993
    formula = "=YEAR(M3)"
    @eval_fn
    def M2():
        m3_1 = LPG_Monthly.M3()
        var_1 = YEAR(m3_1)
        return var_1

@register(LPG_Monthly)
class N2():
    # 'LPG_Monthly'!N2
    value = 1993
    formula = "=YEAR(N3)"
    @eval_fn
    def N2():
        n3_1 = LPG_Monthly.N3()
        var_1 = YEAR(n3_1)
        return var_1

@register(LPG_Monthly)
class O2():
    # 'LPG_Monthly'!O2
    value = 1993
    formula = "=YEAR(O3)"
    @eval_fn
    def O2():
        o3_1 = LPG_Monthly.O3()
        var_1 = YEAR(o3_1)
        return var_1

@register(LPG_Monthly)
class P2():
    # 'LPG_Monthly'!P2
    value = 1993
    formula = "=YEAR(P3)"
    @eval_fn
    def P2():
        p3_1 = LPG_Monthly.P3()
        var_1 = YEAR(p3_1)
        return var_1

@register(LPG_Monthly)
class Q2():
    # 'LPG_Monthly'!Q2
    value = 1993
    formula = "=YEAR(Q3)"
    @eval_fn
    def Q2():
        q3_1 = LPG_Monthly.Q3()
        var_1 = YEAR(q3_1)
        return var_1

@register(LPG_Monthly)
class R2():
    # 'LPG_Monthly'!R2
    value = 1993
    formula = "=YEAR(R3)"
    @eval_fn
    def R2():
        r3_1 = LPG_Monthly.R3()
        var_1 = YEAR(r3_1)
        return var_1

@register(LPG_Monthly)
class S2():
    # 'LPG_Monthly'!S2
    value = 1993
    formula = "=YEAR(S3)"
    @eval_fn
    def S2():
        s3_1 = LPG_Monthly.S3()
        var_1 = YEAR(s3_1)
        return var_1

@register(LPG_Monthly)
class T2():
    # 'LPG_Monthly'!T2
    value = 1993
    formula = "=YEAR(T3)"
    @eval_fn
    def T2():
        t3_1 = LPG_Monthly.T3()
        var_1 = YEAR(t3_1)
        return var_1

@register(LPG_Monthly)
class U2():
    # 'LPG_Monthly'!U2
    value = 1993
    formula = "=YEAR(U3)"
    @eval_fn
    def U2():
        u3_1 = LPG_Monthly.U3()
        var_1 = YEAR(u3_1)
        return var_1

@register(LPG_Monthly)
class V2():
    # 'LPG_Monthly'!V2
    value = 1994
    formula = "=YEAR(V3)"
    @eval_fn
    def V2():
        v3_1 = LPG_Monthly.V3()
        var_1 = YEAR(v3_1)
        return var_1

@register(LPG_Monthly)
class W2():
    # 'LPG_Monthly'!W2
    value = 1994
    formula = "=YEAR(W3)"
    @eval_fn
    def W2():
        w3_1 = LPG_Monthly.W3()
        var_1 = YEAR(w3_1)
        return var_1

@register(LPG_Monthly)
class X2():
    # 'LPG_Monthly'!X2
    value = 1994
    formula = "=YEAR(X3)"
    @eval_fn
    def X2():
        x3_1 = LPG_Monthly.X3()
        var_1 = YEAR(x3_1)
        return var_1

@register(LPG_Monthly)
class Y2():
    # 'LPG_Monthly'!Y2
    value = 1994
    formula = "=YEAR(Y3)"
    @eval_fn
    def Y2():
        y3_1 = LPG_Monthly.Y3()
        var_1 = YEAR(y3_1)
        return var_1

@register(LPG_Monthly)
class Z2():
    # 'LPG_Monthly'!Z2
    value = 1994
    formula = "=YEAR(Z3)"
    @eval_fn
    def Z2():
        z3_1 = LPG_Monthly.Z3()
        var_1 = YEAR(z3_1)
        return var_1

@register(LPG_Monthly)
class AA2():
    # 'LPG_Monthly'!AA2
    value = 1994
    formula = "=YEAR(AA3)"
    @eval_fn
    def AA2():
        aa3_1 = LPG_Monthly.AA3()
        var_1 = YEAR(aa3_1)
        return var_1

@register(LPG_Monthly)
class AB2():
    # 'LPG_Monthly'!AB2
    value = 1994
    formula = "=YEAR(AB3)"
    @eval_fn
    def AB2():
        ab3_1 = LPG_Monthly.AB3()
        var_1 = YEAR(ab3_1)
        return var_1

@register(LPG_Monthly)
class AC2():
    # 'LPG_Monthly'!AC2
    value = 1994
    formula = "=YEAR(AC3)"
    @eval_fn
    def AC2():
        ac3_1 = LPG_Monthly.AC3()
        var_1 = YEAR(ac3_1)
        return var_1

@register(LPG_Monthly)
class AD2():
    # 'LPG_Monthly'!AD2
    value = 1994
    formula = "=YEAR(AD3)"
    @eval_fn
    def AD2():
        ad3_1 = LPG_Monthly.AD3()
        var_1 = YEAR(ad3_1)
        return var_1

@register(LPG_Monthly)
class AE2():
    # 'LPG_Monthly'!AE2
    value = 1994
    formula = "=YEAR(AE3)"
    @eval_fn
    def AE2():
        ae3_1 = LPG_Monthly.AE3()
        var_1 = YEAR(ae3_1)
        return var_1

@register(LPG_Monthly)
class AF2():
    # 'LPG_Monthly'!AF2
    value = 1994
    formula = "=YEAR(AF3)"
    @eval_fn
    def AF2():
        af3_1 = LPG_Monthly.AF3()
        var_1 = YEAR(af3_1)
        return var_1

@register(LPG_Monthly)
class AG2():
    # 'LPG_Monthly'!AG2
    value = 1994
    formula = "=YEAR(AG3)"
    @eval_fn
    def AG2():
        ag3_1 = LPG_Monthly.AG3()
        var_1 = YEAR(ag3_1)
        return var_1

@register(LPG_Monthly)
class AH2():
    # 'LPG_Monthly'!AH2
    value = 1995
    formula = "=YEAR(AH3)"
    @eval_fn
    def AH2():
        ah3_1 = LPG_Monthly.AH3()
        var_1 = YEAR(ah3_1)
        return var_1

@register(LPG_Monthly)
class AI2():
    # 'LPG_Monthly'!AI2
    value = 1995
    formula = "=YEAR(AI3)"
    @eval_fn
    def AI2():
        ai3_1 = LPG_Monthly.AI3()
        var_1 = YEAR(ai3_1)
        return var_1

@register(LPG_Monthly)
class AJ2():
    # 'LPG_Monthly'!AJ2
    value = 1995
    formula = "=YEAR(AJ3)"
    @eval_fn
    def AJ2():
        aj3_1 = LPG_Monthly.AJ3()
        var_1 = YEAR(aj3_1)
        return var_1

@register(LPG_Monthly)
class AK2():
    # 'LPG_Monthly'!AK2
    value = 1995
    formula = "=YEAR(AK3)"
    @eval_fn
    def AK2():
        ak3_1 = LPG_Monthly.AK3()
        var_1 = YEAR(ak3_1)
        return var_1

@register(LPG_Monthly)
class AL2():
    # 'LPG_Monthly'!AL2
    value = 1995
    formula = "=YEAR(AL3)"
    @eval_fn
    def AL2():
        al3_1 = LPG_Monthly.AL3()
        var_1 = YEAR(al3_1)
        return var_1

@register(LPG_Monthly)
class AM2():
    # 'LPG_Monthly'!AM2
    value = 1995
    formula = "=YEAR(AM3)"
    @eval_fn
    def AM2():
        am3_1 = LPG_Monthly.AM3()
        var_1 = YEAR(am3_1)
        return var_1

@register(LPG_Monthly)
class AN2():
    # 'LPG_Monthly'!AN2
    value = 1995
    formula = "=YEAR(AN3)"
    @eval_fn
    def AN2():
        an3_1 = LPG_Monthly.AN3()
        var_1 = YEAR(an3_1)
        return var_1

@register(LPG_Monthly)
class AO2():
    # 'LPG_Monthly'!AO2
    value = 1995
    formula = "=YEAR(AO3)"
    @eval_fn
    def AO2():
        ao3_1 = LPG_Monthly.AO3()
        var_1 = YEAR(ao3_1)
        return var_1

@register(LPG_Monthly)
class AP2():
    # 'LPG_Monthly'!AP2
    value = 1995
    formula = "=YEAR(AP3)"
    @eval_fn
    def AP2():
        ap3_1 = LPG_Monthly.AP3()
        var_1 = YEAR(ap3_1)
        return var_1

@register(LPG_Monthly)
class AQ2():
    # 'LPG_Monthly'!AQ2
    value = 1995
    formula = "=YEAR(AQ3)"
    @eval_fn
    def AQ2():
        aq3_1 = LPG_Monthly.AQ3()
        var_1 = YEAR(aq3_1)
        return var_1

@register(LPG_Monthly)
class AR2():
    # 'LPG_Monthly'!AR2
    value = 1995
    formula = "=YEAR(AR3)"
    @eval_fn
    def AR2():
        ar3_1 = LPG_Monthly.AR3()
        var_1 = YEAR(ar3_1)
        return var_1

@register(LPG_Monthly)
class AS2():
    # 'LPG_Monthly'!AS2
    value = 1995
    formula = "=YEAR(AS3)"
    @eval_fn
    def AS2():
        as3_1 = LPG_Monthly.AS3()
        var_1 = YEAR(as3_1)
        return var_1

@register(LPG_Monthly)
class AT2():
    # 'LPG_Monthly'!AT2
    value = 1996
    formula = "=YEAR(AT3)"
    @eval_fn
    def AT2():
        at3_1 = LPG_Monthly.AT3()
        var_1 = YEAR(at3_1)
        return var_1

@register(LPG_Monthly)
class AU2():
    # 'LPG_Monthly'!AU2
    value = 1996
    formula = "=YEAR(AU3)"
    @eval_fn
    def AU2():
        au3_1 = LPG_Monthly.AU3()
        var_1 = YEAR(au3_1)
        return var_1

@register(LPG_Monthly)
class AV2():
    # 'LPG_Monthly'!AV2
    value = 1996
    formula = "=YEAR(AV3)"
    @eval_fn
    def AV2():
        av3_1 = LPG_Monthly.AV3()
        var_1 = YEAR(av3_1)
        return var_1

@register(LPG_Monthly)
class AW2():
    # 'LPG_Monthly'!AW2
    value = 1996
    formula = "=YEAR(AW3)"
    @eval_fn
    def AW2():
        aw3_1 = LPG_Monthly.AW3()
        var_1 = YEAR(aw3_1)
        return var_1

@register(LPG_Monthly)
class AX2():
    # 'LPG_Monthly'!AX2
    value = 1996
    formula = "=YEAR(AX3)"
    @eval_fn
    def AX2():
        ax3_1 = LPG_Monthly.AX3()
        var_1 = YEAR(ax3_1)
        return var_1

@register(LPG_Monthly)
class AY2():
    # 'LPG_Monthly'!AY2
    value = 1996
    formula = "=YEAR(AY3)"
    @eval_fn
    def AY2():
        ay3_1 = LPG_Monthly.AY3()
        var_1 = YEAR(ay3_1)
        return var_1

@register(LPG_Monthly)
class AZ2():
    # 'LPG_Monthly'!AZ2
    value = 1996
    formula = "=YEAR(AZ3)"
    @eval_fn
    def AZ2():
        az3_1 = LPG_Monthly.AZ3()
        var_1 = YEAR(az3_1)
        return var_1

@register(LPG_Monthly)
class BA2():
    # 'LPG_Monthly'!BA2
    value = 1996
    formula = "=YEAR(BA3)"
    @eval_fn
    def BA2():
        ba3_1 = LPG_Monthly.BA3()
        var_1 = YEAR(ba3_1)
        return var_1

@register(LPG_Monthly)
class BB2():
    # 'LPG_Monthly'!BB2
    value = 1996
    formula = "=YEAR(BB3)"
    @eval_fn
    def BB2():
        bb3_1 = LPG_Monthly.BB3()
        var_1 = YEAR(bb3_1)
        return var_1

@register(LPG_Monthly)
class BC2():
    # 'LPG_Monthly'!BC2
    value = 1996
    formula = "=YEAR(BC3)"
    @eval_fn
    def BC2():
        bc3_1 = LPG_Monthly.BC3()
        var_1 = YEAR(bc3_1)
        return var_1

@register(LPG_Monthly)
class BD2():
    # 'LPG_Monthly'!BD2
    value = 1996
    formula = "=YEAR(BD3)"
    @eval_fn
    def BD2():
        bd3_1 = LPG_Monthly.BD3()
        var_1 = YEAR(bd3_1)
        return var_1

@register(LPG_Monthly)
class BE2():
    # 'LPG_Monthly'!BE2
    value = 1996
    formula = "=YEAR(BE3)"
    @eval_fn
    def BE2():
        be3_1 = LPG_Monthly.BE3()
        var_1 = YEAR(be3_1)
        return var_1

@register(LPG_Monthly)
class BF2():
    # 'LPG_Monthly'!BF2
    value = 1997
    formula = "=YEAR(BF3)"
    @eval_fn
    def BF2():
        bf3_1 = LPG_Monthly.BF3()
        var_1 = YEAR(bf3_1)
        return var_1

@register(LPG_Monthly)
class BG2():
    # 'LPG_Monthly'!BG2
    value = 1997
    formula = "=YEAR(BG3)"
    @eval_fn
    def BG2():
        bg3_1 = LPG_Monthly.BG3()
        var_1 = YEAR(bg3_1)
        return var_1

@register(LPG_Monthly)
class BH2():
    # 'LPG_Monthly'!BH2
    value = 1997
    formula = "=YEAR(BH3)"
    @eval_fn
    def BH2():
        bh3_1 = LPG_Monthly.BH3()
        var_1 = YEAR(bh3_1)
        return var_1

@register(LPG_Monthly)
class BI2():
    # 'LPG_Monthly'!BI2
    value = 1997
    formula = "=YEAR(BI3)"
    @eval_fn
    def BI2():
        bi3_1 = LPG_Monthly.BI3()
        var_1 = YEAR(bi3_1)
        return var_1

@register(LPG_Monthly)
class BJ2():
    # 'LPG_Monthly'!BJ2
    value = 1997
    formula = "=YEAR(BJ3)"
    @eval_fn
    def BJ2():
        bj3_1 = LPG_Monthly.BJ3()
        var_1 = YEAR(bj3_1)
        return var_1

@register(LPG_Monthly)
class BK2():
    # 'LPG_Monthly'!BK2
    value = 1997
    formula = "=YEAR(BK3)"
    @eval_fn
    def BK2():
        bk3_1 = LPG_Monthly.BK3()
        var_1 = YEAR(bk3_1)
        return var_1

@register(LPG_Monthly)
class BL2():
    # 'LPG_Monthly'!BL2
    value = 1997
    formula = "=YEAR(BL3)"
    @eval_fn
    def BL2():
        bl3_1 = LPG_Monthly.BL3()
        var_1 = YEAR(bl3_1)
        return var_1

@register(LPG_Monthly)
class BM2():
    # 'LPG_Monthly'!BM2
    value = 1997
    formula = "=YEAR(BM3)"
    @eval_fn
    def BM2():
        bm3_1 = LPG_Monthly.BM3()
        var_1 = YEAR(bm3_1)
        return var_1

@register(LPG_Monthly)
class BN2():
    # 'LPG_Monthly'!BN2
    value = 1997
    formula = "=YEAR(BN3)"
    @eval_fn
    def BN2():
        bn3_1 = LPG_Monthly.BN3()
        var_1 = YEAR(bn3_1)
        return var_1

@register(LPG_Monthly)
class BO2():
    # 'LPG_Monthly'!BO2
    value = 1997
    formula = "=YEAR(BO3)"
    @eval_fn
    def BO2():
        bo3_1 = LPG_Monthly.BO3()
        var_1 = YEAR(bo3_1)
        return var_1

@register(LPG_Monthly)
class BP2():
    # 'LPG_Monthly'!BP2
    value = 1997
    formula = "=YEAR(BP3)"
    @eval_fn
    def BP2():
        bp3_1 = LPG_Monthly.BP3()
        var_1 = YEAR(bp3_1)
        return var_1

@register(LPG_Monthly)
class BQ2():
    # 'LPG_Monthly'!BQ2
    value = 1997
    formula = "=YEAR(BQ3)"
    @eval_fn
    def BQ2():
        bq3_1 = LPG_Monthly.BQ3()
        var_1 = YEAR(bq3_1)
        return var_1

@register(LPG_Monthly)
class BR2():
    # 'LPG_Monthly'!BR2
    value = 1998
    formula = "=YEAR(BR3)"
    @eval_fn
    def BR2():
        br3_1 = LPG_Monthly.BR3()
        var_1 = YEAR(br3_1)
        return var_1

@register(LPG_Monthly)
class BS2():
    # 'LPG_Monthly'!BS2
    value = 1998
    formula = "=YEAR(BS3)"
    @eval_fn
    def BS2():
        bs3_1 = LPG_Monthly.BS3()
        var_1 = YEAR(bs3_1)
        return var_1

@register(LPG_Monthly)
class BT2():
    # 'LPG_Monthly'!BT2
    value = 1998
    formula = "=YEAR(BT3)"
    @eval_fn
    def BT2():
        bt3_1 = LPG_Monthly.BT3()
        var_1 = YEAR(bt3_1)
        return var_1

@register(LPG_Monthly)
class BU2():
    # 'LPG_Monthly'!BU2
    value = 1998
    formula = "=YEAR(BU3)"
    @eval_fn
    def BU2():
        bu3_1 = LPG_Monthly.BU3()
        var_1 = YEAR(bu3_1)
        return var_1

@register(LPG_Monthly)
class BV2():
    # 'LPG_Monthly'!BV2
    value = 1998
    formula = "=YEAR(BV3)"
    @eval_fn
    def BV2():
        bv3_1 = LPG_Monthly.BV3()
        var_1 = YEAR(bv3_1)
        return var_1

@register(LPG_Monthly)
class BW2():
    # 'LPG_Monthly'!BW2
    value = 1998
    formula = "=YEAR(BW3)"
    @eval_fn
    def BW2():
        bw3_1 = LPG_Monthly.BW3()
        var_1 = YEAR(bw3_1)
        return var_1

@register(LPG_Monthly)
class BX2():
    # 'LPG_Monthly'!BX2
    value = 1998
    formula = "=YEAR(BX3)"
    @eval_fn
    def BX2():
        bx3_1 = LPG_Monthly.BX3()
        var_1 = YEAR(bx3_1)
        return var_1

@register(LPG_Monthly)
class BY2():
    # 'LPG_Monthly'!BY2
    value = 1998
    formula = "=YEAR(BY3)"
    @eval_fn
    def BY2():
        by3_1 = LPG_Monthly.BY3()
        var_1 = YEAR(by3_1)
        return var_1

@register(LPG_Monthly)
class BZ2():
    # 'LPG_Monthly'!BZ2
    value = 1998
    formula = "=YEAR(BZ3)"
    @eval_fn
    def BZ2():
        bz3_1 = LPG_Monthly.BZ3()
        var_1 = YEAR(bz3_1)
        return var_1

@register(LPG_Monthly)
class CA2():
    # 'LPG_Monthly'!CA2
    value = 1998
    formula = "=YEAR(CA3)"
    @eval_fn
    def CA2():
        ca3_1 = LPG_Monthly.CA3()
        var_1 = YEAR(ca3_1)
        return var_1

@register(LPG_Monthly)
class CB2():
    # 'LPG_Monthly'!CB2
    value = 1998
    formula = "=YEAR(CB3)"
    @eval_fn
    def CB2():
        cb3_1 = LPG_Monthly.CB3()
        var_1 = YEAR(cb3_1)
        return var_1

@register(LPG_Monthly)
class CC2():
    # 'LPG_Monthly'!CC2
    value = 1998
    formula = "=YEAR(CC3)"
    @eval_fn
    def CC2():
        cc3_1 = LPG_Monthly.CC3()
        var_1 = YEAR(cc3_1)
        return var_1

@register(LPG_Monthly)
class CD2():
    # 'LPG_Monthly'!CD2
    value = 1999
    formula = "=YEAR(CD3)"
    @eval_fn
    def CD2():
        cd3_1 = LPG_Monthly.CD3()
        var_1 = YEAR(cd3_1)
        return var_1

@register(LPG_Monthly)
class CE2():
    # 'LPG_Monthly'!CE2
    value = 1999
    formula = "=YEAR(CE3)"
    @eval_fn
    def CE2():
        ce3_1 = LPG_Monthly.CE3()
        var_1 = YEAR(ce3_1)
        return var_1

@register(LPG_Monthly)
class CF2():
    # 'LPG_Monthly'!CF2
    value = 1999
    formula = "=YEAR(CF3)"
    @eval_fn
    def CF2():
        cf3_1 = LPG_Monthly.CF3()
        var_1 = YEAR(cf3_1)
        return var_1

@register(LPG_Monthly)
class CG2():
    # 'LPG_Monthly'!CG2
    value = 1999
    formula = "=YEAR(CG3)"
    @eval_fn
    def CG2():
        cg3_1 = LPG_Monthly.CG3()
        var_1 = YEAR(cg3_1)
        return var_1

@register(LPG_Monthly)
class CH2():
    # 'LPG_Monthly'!CH2
    value = 1999
    formula = "=YEAR(CH3)"
    @eval_fn
    def CH2():
        ch3_1 = LPG_Monthly.CH3()
        var_1 = YEAR(ch3_1)
        return var_1

@register(LPG_Monthly)
class CI2():
    # 'LPG_Monthly'!CI2
    value = 1999
    formula = "=YEAR(CI3)"
    @eval_fn
    def CI2():
        ci3_1 = LPG_Monthly.CI3()
        var_1 = YEAR(ci3_1)
        return var_1

@register(LPG_Monthly)
class CJ2():
    # 'LPG_Monthly'!CJ2
    value = 1999
    formula = "=YEAR(CJ3)"
    @eval_fn
    def CJ2():
        cj3_1 = LPG_Monthly.CJ3()
        var_1 = YEAR(cj3_1)
        return var_1

@register(LPG_Monthly)
class CK2():
    # 'LPG_Monthly'!CK2
    value = 1999
    formula = "=YEAR(CK3)"
    @eval_fn
    def CK2():
        ck3_1 = LPG_Monthly.CK3()
        var_1 = YEAR(ck3_1)
        return var_1

@register(LPG_Monthly)
class CL2():
    # 'LPG_Monthly'!CL2
    value = 1999
    formula = "=YEAR(CL3)"
    @eval_fn
    def CL2():
        cl3_1 = LPG_Monthly.CL3()
        var_1 = YEAR(cl3_1)
        return var_1

@register(LPG_Monthly)
class CM2():
    # 'LPG_Monthly'!CM2
    value = 1999
    formula = "=YEAR(CM3)"
    @eval_fn
    def CM2():
        cm3_1 = LPG_Monthly.CM3()
        var_1 = YEAR(cm3_1)
        return var_1

@register(LPG_Monthly)
class CN2():
    # 'LPG_Monthly'!CN2
    value = 1999
    formula = "=YEAR(CN3)"
    @eval_fn
    def CN2():
        cn3_1 = LPG_Monthly.CN3()
        var_1 = YEAR(cn3_1)
        return var_1

@register(LPG_Monthly)
class CO2():
    # 'LPG_Monthly'!CO2
    value = 1999
    formula = "=YEAR(CO3)"
    @eval_fn
    def CO2():
        co3_1 = LPG_Monthly.CO3()
        var_1 = YEAR(co3_1)
        return var_1

@register(LPG_Monthly)
class CP2():
    # 'LPG_Monthly'!CP2
    value = 2000
    formula = "=YEAR(CP3)"
    @eval_fn
    def CP2():
        cp3_1 = LPG_Monthly.CP3()
        var_1 = YEAR(cp3_1)
        return var_1

@register(LPG_Monthly)
class CQ2():
    # 'LPG_Monthly'!CQ2
    value = 2000
    formula = "=YEAR(CQ3)"
    @eval_fn
    def CQ2():
        cq3_1 = LPG_Monthly.CQ3()
        var_1 = YEAR(cq3_1)
        return var_1

@register(LPG_Monthly)
class CR2():
    # 'LPG_Monthly'!CR2
    value = 2000
    formula = "=YEAR(CR3)"
    @eval_fn
    def CR2():
        cr3_1 = LPG_Monthly.CR3()
        var_1 = YEAR(cr3_1)
        return var_1

@register(LPG_Monthly)
class CS2():
    # 'LPG_Monthly'!CS2
    value = 2000
    formula = "=YEAR(CS3)"
    @eval_fn
    def CS2():
        cs3_1 = LPG_Monthly.CS3()
        var_1 = YEAR(cs3_1)
        return var_1

@register(LPG_Monthly)
class CT2():
    # 'LPG_Monthly'!CT2
    value = 2000
    formula = "=YEAR(CT3)"
    @eval_fn
    def CT2():
        ct3_1 = LPG_Monthly.CT3()
        var_1 = YEAR(ct3_1)
        return var_1

@register(LPG_Monthly)
class CU2():
    # 'LPG_Monthly'!CU2
    value = 2000
    formula = "=YEAR(CU3)"
    @eval_fn
    def CU2():
        cu3_1 = LPG_Monthly.CU3()
        var_1 = YEAR(cu3_1)
        return var_1

@register(LPG_Monthly)
class CV2():
    # 'LPG_Monthly'!CV2
    value = 2000
    formula = "=YEAR(CV3)"
    @eval_fn
    def CV2():
        cv3_1 = LPG_Monthly.CV3()
        var_1 = YEAR(cv3_1)
        return var_1

@register(LPG_Monthly)
class CW2():
    # 'LPG_Monthly'!CW2
    value = 2000
    formula = "=YEAR(CW3)"
    @eval_fn
    def CW2():
        cw3_1 = LPG_Monthly.CW3()
        var_1 = YEAR(cw3_1)
        return var_1

@register(LPG_Monthly)
class CX2():
    # 'LPG_Monthly'!CX2
    value = 2000
    formula = "=YEAR(CX3)"
    @eval_fn
    def CX2():
        cx3_1 = LPG_Monthly.CX3()
        var_1 = YEAR(cx3_1)
        return var_1

@register(LPG_Monthly)
class CY2():
    # 'LPG_Monthly'!CY2
    value = 2000
    formula = "=YEAR(CY3)"
    @eval_fn
    def CY2():
        cy3_1 = LPG_Monthly.CY3()
        var_1 = YEAR(cy3_1)
        return var_1

@register(LPG_Monthly)
class CZ2():
    # 'LPG_Monthly'!CZ2
    value = 2000
    formula = "=YEAR(CZ3)"
    @eval_fn
    def CZ2():
        cz3_1 = LPG_Monthly.CZ3()
        var_1 = YEAR(cz3_1)
        return var_1

@register(LPG_Monthly)
class DA2():
    # 'LPG_Monthly'!DA2
    value = 2000
    formula = "=YEAR(DA3)"
    @eval_fn
    def DA2():
        da3_1 = LPG_Monthly.DA3()
        var_1 = YEAR(da3_1)
        return var_1

@register(LPG_Monthly)
class DB2():
    # 'LPG_Monthly'!DB2
    value = 2001
    formula = "=YEAR(DB3)"
    @eval_fn
    def DB2():
        db3_1 = LPG_Monthly.DB3()
        var_1 = YEAR(db3_1)
        return var_1

@register(LPG_Monthly)
class DC2():
    # 'LPG_Monthly'!DC2
    value = 2001
    formula = "=YEAR(DC3)"
    @eval_fn
    def DC2():
        dc3_1 = LPG_Monthly.DC3()
        var_1 = YEAR(dc3_1)
        return var_1

@register(LPG_Monthly)
class DD2():
    # 'LPG_Monthly'!DD2
    value = 2001
    formula = "=YEAR(DD3)"
    @eval_fn
    def DD2():
        dd3_1 = LPG_Monthly.DD3()
        var_1 = YEAR(dd3_1)
        return var_1

@register(LPG_Monthly)
class DE2():
    # 'LPG_Monthly'!DE2
    value = 2001
    formula = "=YEAR(DE3)"
    @eval_fn
    def DE2():
        de3_1 = LPG_Monthly.DE3()
        var_1 = YEAR(de3_1)
        return var_1

@register(LPG_Monthly)
class DF2():
    # 'LPG_Monthly'!DF2
    value = 2001
    formula = "=YEAR(DF3)"
    @eval_fn
    def DF2():
        df3_1 = LPG_Monthly.DF3()
        var_1 = YEAR(df3_1)
        return var_1

@register(LPG_Monthly)
class DG2():
    # 'LPG_Monthly'!DG2
    value = 2001
    formula = "=YEAR(DG3)"
    @eval_fn
    def DG2():
        dg3_1 = LPG_Monthly.DG3()
        var_1 = YEAR(dg3_1)
        return var_1

@register(LPG_Monthly)
class DH2():
    # 'LPG_Monthly'!DH2
    value = 2001
    formula = "=YEAR(DH3)"
    @eval_fn
    def DH2():
        dh3_1 = LPG_Monthly.DH3()
        var_1 = YEAR(dh3_1)
        return var_1

@register(LPG_Monthly)
class DI2():
    # 'LPG_Monthly'!DI2
    value = 2001
    formula = "=YEAR(DI3)"
    @eval_fn
    def DI2():
        di3_1 = LPG_Monthly.DI3()
        var_1 = YEAR(di3_1)
        return var_1

@register(LPG_Monthly)
class DJ2():
    # 'LPG_Monthly'!DJ2
    value = 2001
    formula = "=YEAR(DJ3)"
    @eval_fn
    def DJ2():
        dj3_1 = LPG_Monthly.DJ3()
        var_1 = YEAR(dj3_1)
        return var_1

@register(LPG_Monthly)
class DK2():
    # 'LPG_Monthly'!DK2
    value = 2001
    formula = "=YEAR(DK3)"
    @eval_fn
    def DK2():
        dk3_1 = LPG_Monthly.DK3()
        var_1 = YEAR(dk3_1)
        return var_1

@register(LPG_Monthly)
class DL2():
    # 'LPG_Monthly'!DL2
    value = 2001
    formula = "=YEAR(DL3)"
    @eval_fn
    def DL2():
        dl3_1 = LPG_Monthly.DL3()
        var_1 = YEAR(dl3_1)
        return var_1

@register(LPG_Monthly)
class DM2():
    # 'LPG_Monthly'!DM2
    value = 2001
    formula = "=YEAR(DM3)"
    @eval_fn
    def DM2():
        dm3_1 = LPG_Monthly.DM3()
        var_1 = YEAR(dm3_1)
        return var_1

@register(LPG_Monthly)
class DN2():
    # 'LPG_Monthly'!DN2
    value = 2002
    formula = "=YEAR(DN3)"
    @eval_fn
    def DN2():
        dn3_1 = LPG_Monthly.DN3()
        var_1 = YEAR(dn3_1)
        return var_1

@register(LPG_Monthly)
class DO2():
    # 'LPG_Monthly'!DO2
    value = 2002
    formula = "=YEAR(DO3)"
    @eval_fn
    def DO2():
        do3_1 = LPG_Monthly.DO3()
        var_1 = YEAR(do3_1)
        return var_1

@register(LPG_Monthly)
class DP2():
    # 'LPG_Monthly'!DP2
    value = 2002
    formula = "=YEAR(DP3)"
    @eval_fn
    def DP2():
        dp3_1 = LPG_Monthly.DP3()
        var_1 = YEAR(dp3_1)
        return var_1

@register(LPG_Monthly)
class DQ2():
    # 'LPG_Monthly'!DQ2
    value = 2002
    formula = "=YEAR(DQ3)"
    @eval_fn
    def DQ2():
        dq3_1 = LPG_Monthly.DQ3()
        var_1 = YEAR(dq3_1)
        return var_1

@register(LPG_Monthly)
class DR2():
    # 'LPG_Monthly'!DR2
    value = 2002
    formula = "=YEAR(DR3)"
    @eval_fn
    def DR2():
        dr3_1 = LPG_Monthly.DR3()
        var_1 = YEAR(dr3_1)
        return var_1

@register(LPG_Monthly)
class DS2():
    # 'LPG_Monthly'!DS2
    value = 2002
    formula = "=YEAR(DS3)"
    @eval_fn
    def DS2():
        ds3_1 = LPG_Monthly.DS3()
        var_1 = YEAR(ds3_1)
        return var_1

@register(LPG_Monthly)
class DT2():
    # 'LPG_Monthly'!DT2
    value = 2002
    formula = "=YEAR(DT3)"
    @eval_fn
    def DT2():
        dt3_1 = LPG_Monthly.DT3()
        var_1 = YEAR(dt3_1)
        return var_1

@register(LPG_Monthly)
class DU2():
    # 'LPG_Monthly'!DU2
    value = 2002
    formula = "=YEAR(DU3)"
    @eval_fn
    def DU2():
        du3_1 = LPG_Monthly.DU3()
        var_1 = YEAR(du3_1)
        return var_1

@register(LPG_Monthly)
class DV2():
    # 'LPG_Monthly'!DV2
    value = 2002
    formula = "=YEAR(DV3)"
    @eval_fn
    def DV2():
        dv3_1 = LPG_Monthly.DV3()
        var_1 = YEAR(dv3_1)
        return var_1

@register(LPG_Monthly)
class DW2():
    # 'LPG_Monthly'!DW2
    value = 2002
    formula = "=YEAR(DW3)"
    @eval_fn
    def DW2():
        dw3_1 = LPG_Monthly.DW3()
        var_1 = YEAR(dw3_1)
        return var_1

@register(LPG_Monthly)
class DX2():
    # 'LPG_Monthly'!DX2
    value = 2002
    formula = "=YEAR(DX3)"
    @eval_fn
    def DX2():
        dx3_1 = LPG_Monthly.DX3()
        var_1 = YEAR(dx3_1)
        return var_1

@register(LPG_Monthly)
class DY2():
    # 'LPG_Monthly'!DY2
    value = 2002
    formula = "=YEAR(DY3)"
    @eval_fn
    def DY2():
        dy3_1 = LPG_Monthly.DY3()
        var_1 = YEAR(dy3_1)
        return var_1

@register(LPG_Monthly)
class DZ2():
    # 'LPG_Monthly'!DZ2
    value = 2003
    formula = "=YEAR(DZ3)"
    @eval_fn
    def DZ2():
        dz3_1 = LPG_Monthly.DZ3()
        var_1 = YEAR(dz3_1)
        return var_1

@register(LPG_Monthly)
class EA2():
    # 'LPG_Monthly'!EA2
    value = 2003
    formula = "=YEAR(EA3)"
    @eval_fn
    def EA2():
        ea3_1 = LPG_Monthly.EA3()
        var_1 = YEAR(ea3_1)
        return var_1

@register(LPG_Monthly)
class EB2():
    # 'LPG_Monthly'!EB2
    value = 2003
    formula = "=YEAR(EB3)"
    @eval_fn
    def EB2():
        eb3_1 = LPG_Monthly.EB3()
        var_1 = YEAR(eb3_1)
        return var_1

@register(LPG_Monthly)
class EC2():
    # 'LPG_Monthly'!EC2
    value = 2003
    formula = "=YEAR(EC3)"
    @eval_fn
    def EC2():
        ec3_1 = LPG_Monthly.EC3()
        var_1 = YEAR(ec3_1)
        return var_1

@register(LPG_Monthly)
class ED2():
    # 'LPG_Monthly'!ED2
    value = 2003
    formula = "=YEAR(ED3)"
    @eval_fn
    def ED2():
        ed3_1 = LPG_Monthly.ED3()
        var_1 = YEAR(ed3_1)
        return var_1

@register(LPG_Monthly)
class EE2():
    # 'LPG_Monthly'!EE2
    value = 2003
    formula = "=YEAR(EE3)"
    @eval_fn
    def EE2():
        ee3_1 = LPG_Monthly.EE3()
        var_1 = YEAR(ee3_1)
        return var_1

@register(LPG_Monthly)
class EF2():
    # 'LPG_Monthly'!EF2
    value = 2003
    formula = "=YEAR(EF3)"
    @eval_fn
    def EF2():
        ef3_1 = LPG_Monthly.EF3()
        var_1 = YEAR(ef3_1)
        return var_1

@register(LPG_Monthly)
class EG2():
    # 'LPG_Monthly'!EG2
    value = 2003
    formula = "=YEAR(EG3)"
    @eval_fn
    def EG2():
        eg3_1 = LPG_Monthly.EG3()
        var_1 = YEAR(eg3_1)
        return var_1

@register(LPG_Monthly)
class EH2():
    # 'LPG_Monthly'!EH2
    value = 2003
    formula = "=YEAR(EH3)"
    @eval_fn
    def EH2():
        eh3_1 = LPG_Monthly.EH3()
        var_1 = YEAR(eh3_1)
        return var_1

@register(LPG_Monthly)
class EI2():
    # 'LPG_Monthly'!EI2
    value = 2003
    formula = "=YEAR(EI3)"
    @eval_fn
    def EI2():
        ei3_1 = LPG_Monthly.EI3()
        var_1 = YEAR(ei3_1)
        return var_1

@register(LPG_Monthly)
class EJ2():
    # 'LPG_Monthly'!EJ2
    value = 2003
    formula = "=YEAR(EJ3)"
    @eval_fn
    def EJ2():
        ej3_1 = LPG_Monthly.EJ3()
        var_1 = YEAR(ej3_1)
        return var_1

@register(LPG_Monthly)
class EK2():
    # 'LPG_Monthly'!EK2
    value = 2003
    formula = "=YEAR(EK3)"
    @eval_fn
    def EK2():
        ek3_1 = LPG_Monthly.EK3()
        var_1 = YEAR(ek3_1)
        return var_1

@register(LPG_Monthly)
class EL2():
    # 'LPG_Monthly'!EL2
    value = 2004
    formula = "=YEAR(EL3)"
    @eval_fn
    def EL2():
        el3_1 = LPG_Monthly.EL3()
        var_1 = YEAR(el3_1)
        return var_1

@register(LPG_Monthly)
class EM2():
    # 'LPG_Monthly'!EM2
    value = 2004
    formula = "=YEAR(EM3)"
    @eval_fn
    def EM2():
        em3_1 = LPG_Monthly.EM3()
        var_1 = YEAR(em3_1)
        return var_1

@register(LPG_Monthly)
class EN2():
    # 'LPG_Monthly'!EN2
    value = 2004
    formula = "=YEAR(EN3)"
    @eval_fn
    def EN2():
        en3_1 = LPG_Monthly.EN3()
        var_1 = YEAR(en3_1)
        return var_1

@register(LPG_Monthly)
class EO2():
    # 'LPG_Monthly'!EO2
    value = 2004
    formula = "=YEAR(EO3)"
    @eval_fn
    def EO2():
        eo3_1 = LPG_Monthly.EO3()
        var_1 = YEAR(eo3_1)
        return var_1

@register(LPG_Monthly)
class EP2():
    # 'LPG_Monthly'!EP2
    value = 2004
    formula = "=YEAR(EP3)"
    @eval_fn
    def EP2():
        ep3_1 = LPG_Monthly.EP3()
        var_1 = YEAR(ep3_1)
        return var_1

@register(LPG_Monthly)
class EQ2():
    # 'LPG_Monthly'!EQ2
    value = 2004
    formula = "=YEAR(EQ3)"
    @eval_fn
    def EQ2():
        eq3_1 = LPG_Monthly.EQ3()
        var_1 = YEAR(eq3_1)
        return var_1

@register(LPG_Monthly)
class ER2():
    # 'LPG_Monthly'!ER2
    value = 2004
    formula = "=YEAR(ER3)"
    @eval_fn
    def ER2():
        er3_1 = LPG_Monthly.ER3()
        var_1 = YEAR(er3_1)
        return var_1

@register(LPG_Monthly)
class ES2():
    # 'LPG_Monthly'!ES2
    value = 2004
    formula = "=YEAR(ES3)"
    @eval_fn
    def ES2():
        es3_1 = LPG_Monthly.ES3()
        var_1 = YEAR(es3_1)
        return var_1

@register(LPG_Monthly)
class ET2():
    # 'LPG_Monthly'!ET2
    value = 2004
    formula = "=YEAR(ET3)"
    @eval_fn
    def ET2():
        et3_1 = LPG_Monthly.ET3()
        var_1 = YEAR(et3_1)
        return var_1

@register(LPG_Monthly)
class EU2():
    # 'LPG_Monthly'!EU2
    value = 2004
    formula = "=YEAR(EU3)"
    @eval_fn
    def EU2():
        eu3_1 = LPG_Monthly.EU3()
        var_1 = YEAR(eu3_1)
        return var_1

@register(LPG_Monthly)
class EV2():
    # 'LPG_Monthly'!EV2
    value = 2004
    formula = "=YEAR(EV3)"
    @eval_fn
    def EV2():
        ev3_1 = LPG_Monthly.EV3()
        var_1 = YEAR(ev3_1)
        return var_1

@register(LPG_Monthly)
class EW2():
    # 'LPG_Monthly'!EW2
    value = 2004
    formula = "=YEAR(EW3)"
    @eval_fn
    def EW2():
        ew3_1 = LPG_Monthly.EW3()
        var_1 = YEAR(ew3_1)
        return var_1

@register(LPG_Monthly)
class EX2():
    # 'LPG_Monthly'!EX2
    value = 2005
    formula = "=YEAR(EX3)"
    @eval_fn
    def EX2():
        ex3_1 = LPG_Monthly.EX3()
        var_1 = YEAR(ex3_1)
        return var_1

@register(LPG_Monthly)
class EY2():
    # 'LPG_Monthly'!EY2
    value = 2005
    formula = "=YEAR(EY3)"
    @eval_fn
    def EY2():
        ey3_1 = LPG_Monthly.EY3()
        var_1 = YEAR(ey3_1)
        return var_1

@register(LPG_Monthly)
class EZ2():
    # 'LPG_Monthly'!EZ2
    value = 2005
    formula = "=YEAR(EZ3)"
    @eval_fn
    def EZ2():
        ez3_1 = LPG_Monthly.EZ3()
        var_1 = YEAR(ez3_1)
        return var_1

@register(LPG_Monthly)
class FA2():
    # 'LPG_Monthly'!FA2
    value = 2005
    formula = "=YEAR(FA3)"
    @eval_fn
    def FA2():
        fa3_1 = LPG_Monthly.FA3()
        var_1 = YEAR(fa3_1)
        return var_1

@register(LPG_Monthly)
class FB2():
    # 'LPG_Monthly'!FB2
    value = 2005
    formula = "=YEAR(FB3)"
    @eval_fn
    def FB2():
        fb3_1 = LPG_Monthly.FB3()
        var_1 = YEAR(fb3_1)
        return var_1

@register(LPG_Monthly)
class FC2():
    # 'LPG_Monthly'!FC2
    value = 2005
    formula = "=YEAR(FC3)"
    @eval_fn
    def FC2():
        fc3_1 = LPG_Monthly.FC3()
        var_1 = YEAR(fc3_1)
        return var_1

@register(LPG_Monthly)
class FD2():
    # 'LPG_Monthly'!FD2
    value = 2005
    formula = "=YEAR(FD3)"
    @eval_fn
    def FD2():
        fd3_1 = LPG_Monthly.FD3()
        var_1 = YEAR(fd3_1)
        return var_1

@register(LPG_Monthly)
class FE2():
    # 'LPG_Monthly'!FE2
    value = 2005
    formula = "=YEAR(FE3)"
    @eval_fn
    def FE2():
        fe3_1 = LPG_Monthly.FE3()
        var_1 = YEAR(fe3_1)
        return var_1

@register(LPG_Monthly)
class FF2():
    # 'LPG_Monthly'!FF2
    value = 2005
    formula = "=YEAR(FF3)"
    @eval_fn
    def FF2():
        ff3_1 = LPG_Monthly.FF3()
        var_1 = YEAR(ff3_1)
        return var_1

@register(LPG_Monthly)
class FG2():
    # 'LPG_Monthly'!FG2
    value = 2005
    formula = "=YEAR(FG3)"
    @eval_fn
    def FG2():
        fg3_1 = LPG_Monthly.FG3()
        var_1 = YEAR(fg3_1)
        return var_1

@register(LPG_Monthly)
class FH2():
    # 'LPG_Monthly'!FH2
    value = 2005
    formula = "=YEAR(FH3)"
    @eval_fn
    def FH2():
        fh3_1 = LPG_Monthly.FH3()
        var_1 = YEAR(fh3_1)
        return var_1

@register(LPG_Monthly)
class FI2():
    # 'LPG_Monthly'!FI2
    value = 2005
    formula = "=YEAR(FI3)"
    @eval_fn
    def FI2():
        fi3_1 = LPG_Monthly.FI3()
        var_1 = YEAR(fi3_1)
        return var_1

@register(LPG_Monthly)
class FJ2():
    # 'LPG_Monthly'!FJ2
    value = 2006
    formula = "=YEAR(FJ3)"
    @eval_fn
    def FJ2():
        fj3_1 = LPG_Monthly.FJ3()
        var_1 = YEAR(fj3_1)
        return var_1

@register(LPG_Monthly)
class FK2():
    # 'LPG_Monthly'!FK2
    value = 2006
    formula = "=YEAR(FK3)"
    @eval_fn
    def FK2():
        fk3_1 = LPG_Monthly.FK3()
        var_1 = YEAR(fk3_1)
        return var_1

@register(LPG_Monthly)
class FL2():
    # 'LPG_Monthly'!FL2
    value = 2006
    formula = "=YEAR(FL3)"
    @eval_fn
    def FL2():
        fl3_1 = LPG_Monthly.FL3()
        var_1 = YEAR(fl3_1)
        return var_1

@register(LPG_Monthly)
class FM2():
    # 'LPG_Monthly'!FM2
    value = 2006
    formula = "=YEAR(FM3)"
    @eval_fn
    def FM2():
        fm3_1 = LPG_Monthly.FM3()
        var_1 = YEAR(fm3_1)
        return var_1

@register(LPG_Monthly)
class FN2():
    # 'LPG_Monthly'!FN2
    value = 2006
    formula = "=YEAR(FN3)"
    @eval_fn
    def FN2():
        fn3_1 = LPG_Monthly.FN3()
        var_1 = YEAR(fn3_1)
        return var_1

@register(LPG_Monthly)
class FO2():
    # 'LPG_Monthly'!FO2
    value = 2006
    formula = "=YEAR(FO3)"
    @eval_fn
    def FO2():
        fo3_1 = LPG_Monthly.FO3()
        var_1 = YEAR(fo3_1)
        return var_1

@register(LPG_Monthly)
class FP2():
    # 'LPG_Monthly'!FP2
    value = 2006
    formula = "=YEAR(FP3)"
    @eval_fn
    def FP2():
        fp3_1 = LPG_Monthly.FP3()
        var_1 = YEAR(fp3_1)
        return var_1

@register(LPG_Monthly)
class FQ2():
    # 'LPG_Monthly'!FQ2
    value = 2006
    formula = "=YEAR(FQ3)"
    @eval_fn
    def FQ2():
        fq3_1 = LPG_Monthly.FQ3()
        var_1 = YEAR(fq3_1)
        return var_1

@register(LPG_Monthly)
class FR2():
    # 'LPG_Monthly'!FR2
    value = 2006
    formula = "=YEAR(FR3)"
    @eval_fn
    def FR2():
        fr3_1 = LPG_Monthly.FR3()
        var_1 = YEAR(fr3_1)
        return var_1

@register(LPG_Monthly)
class FS2():
    # 'LPG_Monthly'!FS2
    value = 2006
    formula = "=YEAR(FS3)"
    @eval_fn
    def FS2():
        fs3_1 = LPG_Monthly.FS3()
        var_1 = YEAR(fs3_1)
        return var_1

@register(LPG_Monthly)
class FT2():
    # 'LPG_Monthly'!FT2
    value = 2006
    formula = "=YEAR(FT3)"
    @eval_fn
    def FT2():
        ft3_1 = LPG_Monthly.FT3()
        var_1 = YEAR(ft3_1)
        return var_1

@register(LPG_Monthly)
class FU2():
    # 'LPG_Monthly'!FU2
    value = 2006
    formula = "=YEAR(FU3)"
    @eval_fn
    def FU2():
        fu3_1 = LPG_Monthly.FU3()
        var_1 = YEAR(fu3_1)
        return var_1

@register(LPG_Monthly)
class FV2():
    # 'LPG_Monthly'!FV2
    value = 2007
    formula = "=YEAR(FV3)"
    @eval_fn
    def FV2():
        fv3_1 = LPG_Monthly.FV3()
        var_1 = YEAR(fv3_1)
        return var_1

@register(LPG_Monthly)
class FW2():
    # 'LPG_Monthly'!FW2
    value = 2007
    formula = "=YEAR(FW3)"
    @eval_fn
    def FW2():
        fw3_1 = LPG_Monthly.FW3()
        var_1 = YEAR(fw3_1)
        return var_1

@register(LPG_Monthly)
class FX2():
    # 'LPG_Monthly'!FX2
    value = 2007
    formula = "=YEAR(FX3)"
    @eval_fn
    def FX2():
        fx3_1 = LPG_Monthly.FX3()
        var_1 = YEAR(fx3_1)
        return var_1

@register(LPG_Monthly)
class FY2():
    # 'LPG_Monthly'!FY2
    value = 2007
    formula = "=YEAR(FY3)"
    @eval_fn
    def FY2():
        fy3_1 = LPG_Monthly.FY3()
        var_1 = YEAR(fy3_1)
        return var_1

@register(LPG_Monthly)
class FZ2():
    # 'LPG_Monthly'!FZ2
    value = 2007
    formula = "=YEAR(FZ3)"
    @eval_fn
    def FZ2():
        fz3_1 = LPG_Monthly.FZ3()
        var_1 = YEAR(fz3_1)
        return var_1

@register(LPG_Monthly)
class GA2():
    # 'LPG_Monthly'!GA2
    value = 2007
    formula = "=YEAR(GA3)"
    @eval_fn
    def GA2():
        ga3_1 = LPG_Monthly.GA3()
        var_1 = YEAR(ga3_1)
        return var_1

@register(LPG_Monthly)
class GB2():
    # 'LPG_Monthly'!GB2
    value = 2007
    formula = "=YEAR(GB3)"
    @eval_fn
    def GB2():
        gb3_1 = LPG_Monthly.GB3()
        var_1 = YEAR(gb3_1)
        return var_1

@register(LPG_Monthly)
class GC2():
    # 'LPG_Monthly'!GC2
    value = 2007
    formula = "=YEAR(GC3)"
    @eval_fn
    def GC2():
        gc3_1 = LPG_Monthly.GC3()
        var_1 = YEAR(gc3_1)
        return var_1

@register(LPG_Monthly)
class GD2():
    # 'LPG_Monthly'!GD2
    value = 2007
    formula = "=YEAR(GD3)"
    @eval_fn
    def GD2():
        gd3_1 = LPG_Monthly.GD3()
        var_1 = YEAR(gd3_1)
        return var_1

@register(LPG_Monthly)
class GE2():
    # 'LPG_Monthly'!GE2
    value = 2007
    formula = "=YEAR(GE3)"
    @eval_fn
    def GE2():
        ge3_1 = LPG_Monthly.GE3()
        var_1 = YEAR(ge3_1)
        return var_1

@register(LPG_Monthly)
class GF2():
    # 'LPG_Monthly'!GF2
    value = 2007
    formula = "=YEAR(GF3)"
    @eval_fn
    def GF2():
        gf3_1 = LPG_Monthly.GF3()
        var_1 = YEAR(gf3_1)
        return var_1

@register(LPG_Monthly)
class GG2():
    # 'LPG_Monthly'!GG2
    value = 2007
    formula = "=YEAR(GG3)"
    @eval_fn
    def GG2():
        gg3_1 = LPG_Monthly.GG3()
        var_1 = YEAR(gg3_1)
        return var_1

@register(LPG_Monthly)
class GH2():
    # 'LPG_Monthly'!GH2
    value = 2008
    formula = "=YEAR(GH3)"
    @eval_fn
    def GH2():
        gh3_1 = LPG_Monthly.GH3()
        var_1 = YEAR(gh3_1)
        return var_1

@register(LPG_Monthly)
class GI2():
    # 'LPG_Monthly'!GI2
    value = 2008
    formula = "=YEAR(GI3)"
    @eval_fn
    def GI2():
        gi3_1 = LPG_Monthly.GI3()
        var_1 = YEAR(gi3_1)
        return var_1

@register(LPG_Monthly)
class GJ2():
    # 'LPG_Monthly'!GJ2
    value = 2008
    formula = "=YEAR(GJ3)"
    @eval_fn
    def GJ2():
        gj3_1 = LPG_Monthly.GJ3()
        var_1 = YEAR(gj3_1)
        return var_1

@register(LPG_Monthly)
class GK2():
    # 'LPG_Monthly'!GK2
    value = 2008
    formula = "=YEAR(GK3)"
    @eval_fn
    def GK2():
        gk3_1 = LPG_Monthly.GK3()
        var_1 = YEAR(gk3_1)
        return var_1

@register(LPG_Monthly)
class GL2():
    # 'LPG_Monthly'!GL2
    value = 2008
    formula = "=YEAR(GL3)"
    @eval_fn
    def GL2():
        gl3_1 = LPG_Monthly.GL3()
        var_1 = YEAR(gl3_1)
        return var_1

@register(LPG_Monthly)
class GM2():
    # 'LPG_Monthly'!GM2
    value = 2008
    formula = "=YEAR(GM3)"
    @eval_fn
    def GM2():
        gm3_1 = LPG_Monthly.GM3()
        var_1 = YEAR(gm3_1)
        return var_1

@register(LPG_Monthly)
class GN2():
    # 'LPG_Monthly'!GN2
    value = 2008
    formula = "=YEAR(GN3)"
    @eval_fn
    def GN2():
        gn3_1 = LPG_Monthly.GN3()
        var_1 = YEAR(gn3_1)
        return var_1

@register(LPG_Monthly)
class GO2():
    # 'LPG_Monthly'!GO2
    value = 2008
    formula = "=YEAR(GO3)"
    @eval_fn
    def GO2():
        go3_1 = LPG_Monthly.GO3()
        var_1 = YEAR(go3_1)
        return var_1

@register(LPG_Monthly)
class GP2():
    # 'LPG_Monthly'!GP2
    value = 2008
    formula = "=YEAR(GP3)"
    @eval_fn
    def GP2():
        gp3_1 = LPG_Monthly.GP3()
        var_1 = YEAR(gp3_1)
        return var_1

@register(LPG_Monthly)
class GQ2():
    # 'LPG_Monthly'!GQ2
    value = 2008
    formula = "=YEAR(GQ3)"
    @eval_fn
    def GQ2():
        gq3_1 = LPG_Monthly.GQ3()
        var_1 = YEAR(gq3_1)
        return var_1

@register(LPG_Monthly)
class GR2():
    # 'LPG_Monthly'!GR2
    value = 2008
    formula = "=YEAR(GR3)"
    @eval_fn
    def GR2():
        gr3_1 = LPG_Monthly.GR3()
        var_1 = YEAR(gr3_1)
        return var_1

@register(LPG_Monthly)
class GS2():
    # 'LPG_Monthly'!GS2
    value = 2008
    formula = "=YEAR(GS3)"
    @eval_fn
    def GS2():
        gs3_1 = LPG_Monthly.GS3()
        var_1 = YEAR(gs3_1)
        return var_1

@register(LPG_Monthly)
class GT2():
    # 'LPG_Monthly'!GT2
    value = 2009
    formula = "=YEAR(GT3)"
    @eval_fn
    def GT2():
        gt3_1 = LPG_Monthly.GT3()
        var_1 = YEAR(gt3_1)
        return var_1

@register(LPG_Monthly)
class GU2():
    # 'LPG_Monthly'!GU2
    value = 2009
    formula = "=YEAR(GU3)"
    @eval_fn
    def GU2():
        gu3_1 = LPG_Monthly.GU3()
        var_1 = YEAR(gu3_1)
        return var_1

@register(LPG_Monthly)
class GV2():
    # 'LPG_Monthly'!GV2
    value = 2009
    formula = "=YEAR(GV3)"
    @eval_fn
    def GV2():
        gv3_1 = LPG_Monthly.GV3()
        var_1 = YEAR(gv3_1)
        return var_1

@register(LPG_Monthly)
class GW2():
    # 'LPG_Monthly'!GW2
    value = 2009
    formula = "=YEAR(GW3)"
    @eval_fn
    def GW2():
        gw3_1 = LPG_Monthly.GW3()
        var_1 = YEAR(gw3_1)
        return var_1

@register(LPG_Monthly)
class GX2():
    # 'LPG_Monthly'!GX2
    value = 2009
    formula = "=YEAR(GX3)"
    @eval_fn
    def GX2():
        gx3_1 = LPG_Monthly.GX3()
        var_1 = YEAR(gx3_1)
        return var_1

@register(LPG_Monthly)
class GY2():
    # 'LPG_Monthly'!GY2
    value = 2009
    formula = "=YEAR(GY3)"
    @eval_fn
    def GY2():
        gy3_1 = LPG_Monthly.GY3()
        var_1 = YEAR(gy3_1)
        return var_1

@register(LPG_Monthly)
class GZ2():
    # 'LPG_Monthly'!GZ2
    value = 2009
    formula = "=YEAR(GZ3)"
    @eval_fn
    def GZ2():
        gz3_1 = LPG_Monthly.GZ3()
        var_1 = YEAR(gz3_1)
        return var_1

@register(LPG_Monthly)
class HA2():
    # 'LPG_Monthly'!HA2
    value = 2009
    formula = "=YEAR(HA3)"
    @eval_fn
    def HA2():
        ha3_1 = LPG_Monthly.HA3()
        var_1 = YEAR(ha3_1)
        return var_1

@register(LPG_Monthly)
class HB2():
    # 'LPG_Monthly'!HB2
    value = 2009
    formula = "=YEAR(HB3)"
    @eval_fn
    def HB2():
        hb3_1 = LPG_Monthly.HB3()
        var_1 = YEAR(hb3_1)
        return var_1

@register(LPG_Monthly)
class HC2():
    # 'LPG_Monthly'!HC2
    value = 2009
    formula = "=YEAR(HC3)"
    @eval_fn
    def HC2():
        hc3_1 = LPG_Monthly.HC3()
        var_1 = YEAR(hc3_1)
        return var_1

@register(LPG_Monthly)
class HD2():
    # 'LPG_Monthly'!HD2
    value = 2009
    formula = "=YEAR(HD3)"
    @eval_fn
    def HD2():
        hd3_1 = LPG_Monthly.HD3()
        var_1 = YEAR(hd3_1)
        return var_1

@register(LPG_Monthly)
class HE2():
    # 'LPG_Monthly'!HE2
    value = 2009
    formula = "=YEAR(HE3)"
    @eval_fn
    def HE2():
        he3_1 = LPG_Monthly.HE3()
        var_1 = YEAR(he3_1)
        return var_1

@register(LPG_Monthly)
class HF2():
    # 'LPG_Monthly'!HF2
    value = 2010
    formula = "=YEAR(HF3)"
    @eval_fn
    def HF2():
        hf3_1 = LPG_Monthly.HF3()
        var_1 = YEAR(hf3_1)
        return var_1

@register(LPG_Monthly)
class HG2():
    # 'LPG_Monthly'!HG2
    value = 2010
    formula = "=YEAR(HG3)"
    @eval_fn
    def HG2():
        hg3_1 = LPG_Monthly.HG3()
        var_1 = YEAR(hg3_1)
        return var_1

@register(LPG_Monthly)
class HH2():
    # 'LPG_Monthly'!HH2
    value = 2010
    formula = "=YEAR(HH3)"
    @eval_fn
    def HH2():
        hh3_1 = LPG_Monthly.HH3()
        var_1 = YEAR(hh3_1)
        return var_1

@register(LPG_Monthly)
class HI2():
    # 'LPG_Monthly'!HI2
    value = 2010
    formula = "=YEAR(HI3)"
    @eval_fn
    def HI2():
        hi3_1 = LPG_Monthly.HI3()
        var_1 = YEAR(hi3_1)
        return var_1

@register(LPG_Monthly)
class HJ2():
    # 'LPG_Monthly'!HJ2
    value = 2010
    formula = "=YEAR(HJ3)"
    @eval_fn
    def HJ2():
        hj3_1 = LPG_Monthly.HJ3()
        var_1 = YEAR(hj3_1)
        return var_1

@register(LPG_Monthly)
class HK2():
    # 'LPG_Monthly'!HK2
    value = 2010
    formula = "=YEAR(HK3)"
    @eval_fn
    def HK2():
        hk3_1 = LPG_Monthly.HK3()
        var_1 = YEAR(hk3_1)
        return var_1

@register(LPG_Monthly)
class HL2():
    # 'LPG_Monthly'!HL2
    value = 2010
    formula = "=YEAR(HL3)"
    @eval_fn
    def HL2():
        hl3_1 = LPG_Monthly.HL3()
        var_1 = YEAR(hl3_1)
        return var_1

@register(LPG_Monthly)
class HM2():
    # 'LPG_Monthly'!HM2
    value = 2010
    formula = "=YEAR(HM3)"
    @eval_fn
    def HM2():
        hm3_1 = LPG_Monthly.HM3()
        var_1 = YEAR(hm3_1)
        return var_1

@register(LPG_Monthly)
class HN2():
    # 'LPG_Monthly'!HN2
    value = 2010
    formula = "=YEAR(HN3)"
    @eval_fn
    def HN2():
        hn3_1 = LPG_Monthly.HN3()
        var_1 = YEAR(hn3_1)
        return var_1

@register(LPG_Monthly)
class HO2():
    # 'LPG_Monthly'!HO2
    value = 2010
    formula = "=YEAR(HO3)"
    @eval_fn
    def HO2():
        ho3_1 = LPG_Monthly.HO3()
        var_1 = YEAR(ho3_1)
        return var_1

@register(LPG_Monthly)
class HP2():
    # 'LPG_Monthly'!HP2
    value = 2010
    formula = "=YEAR(HP3)"
    @eval_fn
    def HP2():
        hp3_1 = LPG_Monthly.HP3()
        var_1 = YEAR(hp3_1)
        return var_1

@register(LPG_Monthly)
class HQ2():
    # 'LPG_Monthly'!HQ2
    value = 2010
    formula = "=YEAR(HQ3)"
    @eval_fn
    def HQ2():
        hq3_1 = LPG_Monthly.HQ3()
        var_1 = YEAR(hq3_1)
        return var_1

@register(LPG_Monthly)
class HR2():
    # 'LPG_Monthly'!HR2
    value = 2011
    formula = "=YEAR(HR3)"
    @eval_fn
    def HR2():
        hr3_1 = LPG_Monthly.HR3()
        var_1 = YEAR(hr3_1)
        return var_1

@register(LPG_Monthly)
class HS2():
    # 'LPG_Monthly'!HS2
    value = 2011
    formula = "=YEAR(HS3)"
    @eval_fn
    def HS2():
        hs3_1 = LPG_Monthly.HS3()
        var_1 = YEAR(hs3_1)
        return var_1

@register(LPG_Monthly)
class HT2():
    # 'LPG_Monthly'!HT2
    value = 2011
    formula = "=YEAR(HT3)"
    @eval_fn
    def HT2():
        ht3_1 = LPG_Monthly.HT3()
        var_1 = YEAR(ht3_1)
        return var_1

@register(LPG_Monthly)
class HU2():
    # 'LPG_Monthly'!HU2
    value = 2011
    formula = "=YEAR(HU3)"
    @eval_fn
    def HU2():
        hu3_1 = LPG_Monthly.HU3()
        var_1 = YEAR(hu3_1)
        return var_1

@register(LPG_Monthly)
class HV2():
    # 'LPG_Monthly'!HV2
    value = 2011
    formula = "=YEAR(HV3)"
    @eval_fn
    def HV2():
        hv3_1 = LPG_Monthly.HV3()
        var_1 = YEAR(hv3_1)
        return var_1

@register(LPG_Monthly)
class HW2():
    # 'LPG_Monthly'!HW2
    value = 2011
    formula = "=YEAR(HW3)"
    @eval_fn
    def HW2():
        hw3_1 = LPG_Monthly.HW3()
        var_1 = YEAR(hw3_1)
        return var_1

@register(LPG_Monthly)
class HX2():
    # 'LPG_Monthly'!HX2
    value = 2011
    formula = "=YEAR(HX3)"
    @eval_fn
    def HX2():
        hx3_1 = LPG_Monthly.HX3()
        var_1 = YEAR(hx3_1)
        return var_1

@register(LPG_Monthly)
class HY2():
    # 'LPG_Monthly'!HY2
    value = 2011
    formula = "=YEAR(HY3)"
    @eval_fn
    def HY2():
        hy3_1 = LPG_Monthly.HY3()
        var_1 = YEAR(hy3_1)
        return var_1

@register(LPG_Monthly)
class HZ2():
    # 'LPG_Monthly'!HZ2
    value = 2011
    formula = "=YEAR(HZ3)"
    @eval_fn
    def HZ2():
        hz3_1 = LPG_Monthly.HZ3()
        var_1 = YEAR(hz3_1)
        return var_1

@register(LPG_Monthly)
class IA2():
    # 'LPG_Monthly'!IA2
    value = 2011
    formula = "=YEAR(IA3)"
    @eval_fn
    def IA2():
        ia3_1 = LPG_Monthly.IA3()
        var_1 = YEAR(ia3_1)
        return var_1

@register(LPG_Monthly)
class IB2():
    # 'LPG_Monthly'!IB2
    value = 2011
    formula = "=YEAR(IB3)"
    @eval_fn
    def IB2():
        ib3_1 = LPG_Monthly.IB3()
        var_1 = YEAR(ib3_1)
        return var_1

@register(LPG_Monthly)
class IC2():
    # 'LPG_Monthly'!IC2
    value = 2011
    formula = "=YEAR(IC3)"
    @eval_fn
    def IC2():
        ic3_1 = LPG_Monthly.IC3()
        var_1 = YEAR(ic3_1)
        return var_1

@register(LPG_Monthly)
class ID2():
    # 'LPG_Monthly'!ID2
    value = 2012
    formula = "=YEAR(ID3)"
    @eval_fn
    def ID2():
        id3_1 = LPG_Monthly.ID3()
        var_1 = YEAR(id3_1)
        return var_1

@register(LPG_Monthly)
class IE2():
    # 'LPG_Monthly'!IE2
    value = 2012
    formula = "=YEAR(IE3)"
    @eval_fn
    def IE2():
        ie3_1 = LPG_Monthly.IE3()
        var_1 = YEAR(ie3_1)
        return var_1

@register(LPG_Monthly)
class IF2():
    # 'LPG_Monthly'!IF2
    value = 2012
    formula = "=YEAR(IF3)"
    @eval_fn
    def IF2():
        if3_1 = LPG_Monthly.IF3()
        var_1 = YEAR(if3_1)
        return var_1

@register(LPG_Monthly)
class IG2():
    # 'LPG_Monthly'!IG2
    value = 2012
    formula = "=YEAR(IG3)"
    @eval_fn
    def IG2():
        ig3_1 = LPG_Monthly.IG3()
        var_1 = YEAR(ig3_1)
        return var_1

@register(LPG_Monthly)
class IH2():
    # 'LPG_Monthly'!IH2
    value = 2012
    formula = "=YEAR(IH3)"
    @eval_fn
    def IH2():
        ih3_1 = LPG_Monthly.IH3()
        var_1 = YEAR(ih3_1)
        return var_1

@register(LPG_Monthly)
class II2():
    # 'LPG_Monthly'!II2
    value = 2012
    formula = "=YEAR(II3)"
    @eval_fn
    def II2():
        ii3_1 = LPG_Monthly.II3()
        var_1 = YEAR(ii3_1)
        return var_1

@register(LPG_Monthly)
class IJ2():
    # 'LPG_Monthly'!IJ2
    value = 2012
    formula = "=YEAR(IJ3)"
    @eval_fn
    def IJ2():
        ij3_1 = LPG_Monthly.IJ3()
        var_1 = YEAR(ij3_1)
        return var_1

@register(LPG_Monthly)
class IK2():
    # 'LPG_Monthly'!IK2
    value = 2012
    formula = "=YEAR(IK3)"
    @eval_fn
    def IK2():
        ik3_1 = LPG_Monthly.IK3()
        var_1 = YEAR(ik3_1)
        return var_1

@register(LPG_Monthly)
class IL2():
    # 'LPG_Monthly'!IL2
    value = 2012
    formula = "=YEAR(IL3)"
    @eval_fn
    def IL2():
        il3_1 = LPG_Monthly.IL3()
        var_1 = YEAR(il3_1)
        return var_1

@register(LPG_Monthly)
class IM2():
    # 'LPG_Monthly'!IM2
    value = 2012
    formula = "=YEAR(IM3)"
    @eval_fn
    def IM2():
        im3_1 = LPG_Monthly.IM3()
        var_1 = YEAR(im3_1)
        return var_1

@register(LPG_Monthly)
class IN2():
    # 'LPG_Monthly'!IN2
    value = 2012
    formula = "=YEAR(IN3)"
    @eval_fn
    def IN2():
        in3_1 = LPG_Monthly.IN3()
        var_1 = YEAR(in3_1)
        return var_1

@register(LPG_Monthly)
class IO2():
    # 'LPG_Monthly'!IO2
    value = 2012
    formula = "=YEAR(IO3)"
    @eval_fn
    def IO2():
        io3_1 = LPG_Monthly.IO3()
        var_1 = YEAR(io3_1)
        return var_1

@register(LPG_Monthly)
class IP2():
    # 'LPG_Monthly'!IP2
    value = 2013
    formula = "=YEAR(IP3)"
    @eval_fn
    def IP2():
        ip3_1 = LPG_Monthly.IP3()
        var_1 = YEAR(ip3_1)
        return var_1

@register(LPG_Monthly)
class IQ2():
    # 'LPG_Monthly'!IQ2
    value = 2013
    formula = "=YEAR(IQ3)"
    @eval_fn
    def IQ2():
        iq3_1 = LPG_Monthly.IQ3()
        var_1 = YEAR(iq3_1)
        return var_1

@register(LPG_Monthly)
class IR2():
    # 'LPG_Monthly'!IR2
    value = 2013
    formula = "=YEAR(IR3)"
    @eval_fn
    def IR2():
        ir3_1 = LPG_Monthly.IR3()
        var_1 = YEAR(ir3_1)
        return var_1

@register(LPG_Monthly)
class IS2():
    # 'LPG_Monthly'!IS2
    value = 2013
    formula = "=YEAR(IS3)"
    @eval_fn
    def IS2():
        is3_1 = LPG_Monthly.IS3()
        var_1 = YEAR(is3_1)
        return var_1

@register(LPG_Monthly)
class IT2():
    # 'LPG_Monthly'!IT2
    value = 2013
    formula = "=YEAR(IT3)"
    @eval_fn
    def IT2():
        it3_1 = LPG_Monthly.IT3()
        var_1 = YEAR(it3_1)
        return var_1

@register(LPG_Monthly)
class IU2():
    # 'LPG_Monthly'!IU2
    value = 2013
    formula = "=YEAR(IU3)"
    @eval_fn
    def IU2():
        iu3_1 = LPG_Monthly.IU3()
        var_1 = YEAR(iu3_1)
        return var_1

@register(LPG_Monthly)
class IV2():
    # 'LPG_Monthly'!IV2
    value = 2013
    formula = "=YEAR(IV3)"
    @eval_fn
    def IV2():
        iv3_1 = LPG_Monthly.IV3()
        var_1 = YEAR(iv3_1)
        return var_1

@register(LPG_Monthly)
class IW2():
    # 'LPG_Monthly'!IW2
    value = 2013
    formula = "=YEAR(IW3)"
    @eval_fn
    def IW2():
        iw3_1 = LPG_Monthly.IW3()
        var_1 = YEAR(iw3_1)
        return var_1

@register(LPG_Monthly)
class IX2():
    # 'LPG_Monthly'!IX2
    value = 2013
    formula = "=YEAR(IX3)"
    @eval_fn
    def IX2():
        ix3_1 = LPG_Monthly.IX3()
        var_1 = YEAR(ix3_1)
        return var_1

@register(LPG_Monthly)
class IY2():
    # 'LPG_Monthly'!IY2
    value = 2013
    formula = "=YEAR(IY3)"
    @eval_fn
    def IY2():
        iy3_1 = LPG_Monthly.IY3()
        var_1 = YEAR(iy3_1)
        return var_1

@register(LPG_Monthly)
class IZ2():
    # 'LPG_Monthly'!IZ2
    value = 2013
    formula = "=YEAR(IZ3)"
    @eval_fn
    def IZ2():
        iz3_1 = LPG_Monthly.IZ3()
        var_1 = YEAR(iz3_1)
        return var_1

@register(LPG_Monthly)
class JA2():
    # 'LPG_Monthly'!JA2
    value = 2013
    formula = "=YEAR(JA3)"
    @eval_fn
    def JA2():
        ja3_1 = LPG_Monthly.JA3()
        var_1 = YEAR(ja3_1)
        return var_1

@register(LPG_Monthly)
class JB2():
    # 'LPG_Monthly'!JB2
    value = 2014
    formula = "=YEAR(JB3)"
    @eval_fn
    def JB2():
        jb3_1 = LPG_Monthly.JB3()
        var_1 = YEAR(jb3_1)
        return var_1

@register(LPG_Monthly)
class JC2():
    # 'LPG_Monthly'!JC2
    value = 2014
    formula = "=YEAR(JC3)"
    @eval_fn
    def JC2():
        jc3_1 = LPG_Monthly.JC3()
        var_1 = YEAR(jc3_1)
        return var_1

@register(LPG_Monthly)
class JD2():
    # 'LPG_Monthly'!JD2
    value = 2014
    formula = "=YEAR(JD3)"
    @eval_fn
    def JD2():
        jd3_1 = LPG_Monthly.JD3()
        var_1 = YEAR(jd3_1)
        return var_1

@register(LPG_Monthly)
class JE2():
    # 'LPG_Monthly'!JE2
    value = 2014
    formula = "=YEAR(JE3)"
    @eval_fn
    def JE2():
        je3_1 = LPG_Monthly.JE3()
        var_1 = YEAR(je3_1)
        return var_1

@register(LPG_Monthly)
class JF2():
    # 'LPG_Monthly'!JF2
    value = 2014
    formula = "=YEAR(JF3)"
    @eval_fn
    def JF2():
        jf3_1 = LPG_Monthly.JF3()
        var_1 = YEAR(jf3_1)
        return var_1

@register(LPG_Monthly)
class JG2():
    # 'LPG_Monthly'!JG2
    value = 2014
    formula = "=YEAR(JG3)"
    @eval_fn
    def JG2():
        jg3_1 = LPG_Monthly.JG3()
        var_1 = YEAR(jg3_1)
        return var_1

@register(LPG_Monthly)
class JH2():
    # 'LPG_Monthly'!JH2
    value = 2014
    formula = "=YEAR(JH3)"
    @eval_fn
    def JH2():
        jh3_1 = LPG_Monthly.JH3()
        var_1 = YEAR(jh3_1)
        return var_1

@register(LPG_Monthly)
class JI2():
    # 'LPG_Monthly'!JI2
    value = 2014
    formula = "=YEAR(JI3)"
    @eval_fn
    def JI2():
        ji3_1 = LPG_Monthly.JI3()
        var_1 = YEAR(ji3_1)
        return var_1

@register(LPG_Monthly)
class JJ2():
    # 'LPG_Monthly'!JJ2
    value = 2014
    formula = "=YEAR(JJ3)"
    @eval_fn
    def JJ2():
        jj3_1 = LPG_Monthly.JJ3()
        var_1 = YEAR(jj3_1)
        return var_1

@register(LPG_Monthly)
class JK2():
    # 'LPG_Monthly'!JK2
    value = 2014
    formula = "=YEAR(JK3)"
    @eval_fn
    def JK2():
        jk3_1 = LPG_Monthly.JK3()
        var_1 = YEAR(jk3_1)
        return var_1

@register(LPG_Monthly)
class JL2():
    # 'LPG_Monthly'!JL2
    value = 2014
    formula = "=YEAR(JL3)"
    @eval_fn
    def JL2():
        jl3_1 = LPG_Monthly.JL3()
        var_1 = YEAR(jl3_1)
        return var_1

@register(LPG_Monthly)
class JM2():
    # 'LPG_Monthly'!JM2
    value = 2014
    formula = "=YEAR(JM3)"
    @eval_fn
    def JM2():
        jm3_1 = LPG_Monthly.JM3()
        var_1 = YEAR(jm3_1)
        return var_1

@register(LPG_Monthly)
class JN2():
    # 'LPG_Monthly'!JN2
    value = 2015
    formula = "=YEAR(JN3)"
    @eval_fn
    def JN2():
        jn3_1 = LPG_Monthly.JN3()
        var_1 = YEAR(jn3_1)
        return var_1

@register(LPG_Monthly)
class JO2():
    # 'LPG_Monthly'!JO2
    value = 2015
    formula = "=YEAR(JO3)"
    @eval_fn
    def JO2():
        jo3_1 = LPG_Monthly.JO3()
        var_1 = YEAR(jo3_1)
        return var_1

@register(LPG_Monthly)
class JP2():
    # 'LPG_Monthly'!JP2
    value = 2015
    formula = "=YEAR(JP3)"
    @eval_fn
    def JP2():
        jp3_1 = LPG_Monthly.JP3()
        var_1 = YEAR(jp3_1)
        return var_1

@register(LPG_Monthly)
class JQ2():
    # 'LPG_Monthly'!JQ2
    value = 2015
    formula = "=YEAR(JQ3)"
    @eval_fn
    def JQ2():
        jq3_1 = LPG_Monthly.JQ3()
        var_1 = YEAR(jq3_1)
        return var_1

@register(LPG_Monthly)
class JR2():
    # 'LPG_Monthly'!JR2
    value = 2015
    formula = "=YEAR(JR3)"
    @eval_fn
    def JR2():
        jr3_1 = LPG_Monthly.JR3()
        var_1 = YEAR(jr3_1)
        return var_1

@register(LPG_Monthly)
class JS2():
    # 'LPG_Monthly'!JS2
    value = 2015
    formula = "=YEAR(JS3)"
    @eval_fn
    def JS2():
        js3_1 = LPG_Monthly.JS3()
        var_1 = YEAR(js3_1)
        return var_1

@register(LPG_Monthly)
class JT2():
    # 'LPG_Monthly'!JT2
    value = 2015
    formula = "=YEAR(JT3)"
    @eval_fn
    def JT2():
        jt3_1 = LPG_Monthly.JT3()
        var_1 = YEAR(jt3_1)
        return var_1

@register(LPG_Monthly)
class JU2():
    # 'LPG_Monthly'!JU2
    value = 2015
    formula = "=YEAR(JU3)"
    @eval_fn
    def JU2():
        ju3_1 = LPG_Monthly.JU3()
        var_1 = YEAR(ju3_1)
        return var_1

@register(LPG_Monthly)
class JV2():
    # 'LPG_Monthly'!JV2
    value = 2015
    formula = "=YEAR(JV3)"
    @eval_fn
    def JV2():
        jv3_1 = LPG_Monthly.JV3()
        var_1 = YEAR(jv3_1)
        return var_1

@register(LPG_Monthly)
class JW2():
    # 'LPG_Monthly'!JW2
    value = 2015
    formula = "=YEAR(JW3)"
    @eval_fn
    def JW2():
        jw3_1 = LPG_Monthly.JW3()
        var_1 = YEAR(jw3_1)
        return var_1

@register(LPG_Monthly)
class JX2():
    # 'LPG_Monthly'!JX2
    value = 2015
    formula = "=YEAR(JX3)"
    @eval_fn
    def JX2():
        jx3_1 = LPG_Monthly.JX3()
        var_1 = YEAR(jx3_1)
        return var_1

@register(LPG_Monthly)
class JY2():
    # 'LPG_Monthly'!JY2
    value = 2015
    formula = "=YEAR(JY3)"
    @eval_fn
    def JY2():
        jy3_1 = LPG_Monthly.JY3()
        var_1 = YEAR(jy3_1)
        return var_1

@register(LPG_Monthly)
class JZ2():
    # 'LPG_Monthly'!JZ2
    value = 2016
    formula = "=YEAR(JZ3)"
    @eval_fn
    def JZ2():
        jz3_1 = LPG_Monthly.JZ3()
        var_1 = YEAR(jz3_1)
        return var_1

@register(LPG_Monthly)
class KA2():
    # 'LPG_Monthly'!KA2
    value = 2016
    formula = "=YEAR(KA3)"
    @eval_fn
    def KA2():
        ka3_1 = LPG_Monthly.KA3()
        var_1 = YEAR(ka3_1)
        return var_1

@register(LPG_Monthly)
class KB2():
    # 'LPG_Monthly'!KB2
    value = 2016
    formula = "=YEAR(KB3)"
    @eval_fn
    def KB2():
        kb3_1 = LPG_Monthly.KB3()
        var_1 = YEAR(kb3_1)
        return var_1

@register(LPG_Monthly)
class KC2():
    # 'LPG_Monthly'!KC2
    value = 2016
    formula = "=YEAR(KC3)"
    @eval_fn
    def KC2():
        kc3_1 = LPG_Monthly.KC3()
        var_1 = YEAR(kc3_1)
        return var_1

@register(LPG_Monthly)
class KD2():
    # 'LPG_Monthly'!KD2
    value = 2016
    formula = "=YEAR(KD3)"
    @eval_fn
    def KD2():
        kd3_1 = LPG_Monthly.KD3()
        var_1 = YEAR(kd3_1)
        return var_1

@register(LPG_Monthly)
class KE2():
    # 'LPG_Monthly'!KE2
    value = 2016
    formula = "=YEAR(KE3)"
    @eval_fn
    def KE2():
        ke3_1 = LPG_Monthly.KE3()
        var_1 = YEAR(ke3_1)
        return var_1

@register(LPG_Monthly)
class KF2():
    # 'LPG_Monthly'!KF2
    value = 2016
    formula = "=YEAR(KF3)"
    @eval_fn
    def KF2():
        kf3_1 = LPG_Monthly.KF3()
        var_1 = YEAR(kf3_1)
        return var_1

@register(LPG_Monthly)
class KG2():
    # 'LPG_Monthly'!KG2
    value = 2016
    formula = "=YEAR(KG3)"
    @eval_fn
    def KG2():
        kg3_1 = LPG_Monthly.KG3()
        var_1 = YEAR(kg3_1)
        return var_1

@register(LPG_Monthly)
class KH2():
    # 'LPG_Monthly'!KH2
    value = 2016
    formula = "=YEAR(KH3)"
    @eval_fn
    def KH2():
        kh3_1 = LPG_Monthly.KH3()
        var_1 = YEAR(kh3_1)
        return var_1

@register(LPG_Monthly)
class KI2():
    # 'LPG_Monthly'!KI2
    value = 2016
    formula = "=YEAR(KI3)"
    @eval_fn
    def KI2():
        ki3_1 = LPG_Monthly.KI3()
        var_1 = YEAR(ki3_1)
        return var_1

@register(LPG_Monthly)
class KJ2():
    # 'LPG_Monthly'!KJ2
    value = 2016
    formula = "=YEAR(KJ3)"
    @eval_fn
    def KJ2():
        kj3_1 = LPG_Monthly.KJ3()
        var_1 = YEAR(kj3_1)
        return var_1

@register(LPG_Monthly)
class KK2():
    # 'LPG_Monthly'!KK2
    value = 2016
    formula = "=YEAR(KK3)"
    @eval_fn
    def KK2():
        kk3_1 = LPG_Monthly.KK3()
        var_1 = YEAR(kk3_1)
        return var_1

@register(LPG_Monthly)
class KL2():
    # 'LPG_Monthly'!KL2
    value = 2017
    formula = "=YEAR(KL3)"
    @eval_fn
    def KL2():
        kl3_1 = LPG_Monthly.KL3()
        var_1 = YEAR(kl3_1)
        return var_1

@register(LPG_Monthly)
class KM2():
    # 'LPG_Monthly'!KM2
    value = 2017
    formula = "=YEAR(KM3)"
    @eval_fn
    def KM2():
        km3_1 = LPG_Monthly.KM3()
        var_1 = YEAR(km3_1)
        return var_1

@register(LPG_Monthly)
class KN2():
    # 'LPG_Monthly'!KN2
    value = 2017
    formula = "=YEAR(KN3)"
    @eval_fn
    def KN2():
        kn3_1 = LPG_Monthly.KN3()
        var_1 = YEAR(kn3_1)
        return var_1

@register(LPG_Monthly)
class KO2():
    # 'LPG_Monthly'!KO2
    value = 2017
    formula = "=YEAR(KO3)"
    @eval_fn
    def KO2():
        ko3_1 = LPG_Monthly.KO3()
        var_1 = YEAR(ko3_1)
        return var_1

@register(LPG_Monthly)
class KP2():
    # 'LPG_Monthly'!KP2
    value = 2017
    formula = "=YEAR(KP3)"
    @eval_fn
    def KP2():
        kp3_1 = LPG_Monthly.KP3()
        var_1 = YEAR(kp3_1)
        return var_1

@register(LPG_Monthly)
class KQ2():
    # 'LPG_Monthly'!KQ2
    value = 2017
    formula = "=YEAR(KQ3)"
    @eval_fn
    def KQ2():
        kq3_1 = LPG_Monthly.KQ3()
        var_1 = YEAR(kq3_1)
        return var_1

@register(LPG_Monthly)
class KR2():
    # 'LPG_Monthly'!KR2
    value = 2017
    formula = "=YEAR(KR3)"
    @eval_fn
    def KR2():
        kr3_1 = LPG_Monthly.KR3()
        var_1 = YEAR(kr3_1)
        return var_1

@register(LPG_Monthly)
class KS2():
    # 'LPG_Monthly'!KS2
    value = 2017
    formula = "=YEAR(KS3)"
    @eval_fn
    def KS2():
        ks3_1 = LPG_Monthly.KS3()
        var_1 = YEAR(ks3_1)
        return var_1

@register(LPG_Monthly)
class KT2():
    # 'LPG_Monthly'!KT2
    value = 2017
    formula = "=YEAR(KT3)"
    @eval_fn
    def KT2():
        kt3_1 = LPG_Monthly.KT3()
        var_1 = YEAR(kt3_1)
        return var_1

@register(LPG_Monthly)
class KU2():
    # 'LPG_Monthly'!KU2
    value = 2017
    formula = "=YEAR(KU3)"
    @eval_fn
    def KU2():
        ku3_1 = LPG_Monthly.KU3()
        var_1 = YEAR(ku3_1)
        return var_1

@register(LPG_Monthly)
class KV2():
    # 'LPG_Monthly'!KV2
    value = 2017
    formula = "=YEAR(KV3)"
    @eval_fn
    def KV2():
        kv3_1 = LPG_Monthly.KV3()
        var_1 = YEAR(kv3_1)
        return var_1

@register(LPG_Monthly)
class KW2():
    # 'LPG_Monthly'!KW2
    value = 2017
    formula = "=YEAR(KW3)"
    @eval_fn
    def KW2():
        kw3_1 = LPG_Monthly.KW3()
        var_1 = YEAR(kw3_1)
        return var_1

@register(LPG_Monthly)
class KX2():
    # 'LPG_Monthly'!KX2
    value = 2018
    formula = "=YEAR(KX3)"
    @eval_fn
    def KX2():
        kx3_1 = LPG_Monthly.KX3()
        var_1 = YEAR(kx3_1)
        return var_1

@register(LPG_Monthly)
class KY2():
    # 'LPG_Monthly'!KY2
    value = 2018
    formula = "=YEAR(KY3)"
    @eval_fn
    def KY2():
        ky3_1 = LPG_Monthly.KY3()
        var_1 = YEAR(ky3_1)
        return var_1

@register(LPG_Monthly)
class KZ2():
    # 'LPG_Monthly'!KZ2
    value = 2018
    formula = "=YEAR(KZ3)"
    @eval_fn
    def KZ2():
        kz3_1 = LPG_Monthly.KZ3()
        var_1 = YEAR(kz3_1)
        return var_1

@register(LPG_Monthly)
class LA2():
    # 'LPG_Monthly'!LA2
    value = 2018
    formula = "=YEAR(LA3)"
    @eval_fn
    def LA2():
        la3_1 = LPG_Monthly.LA3()
        var_1 = YEAR(la3_1)
        return var_1

@register(LPG_Monthly)
class LB2():
    # 'LPG_Monthly'!LB2
    value = 2018
    formula = "=YEAR(LB3)"
    @eval_fn
    def LB2():
        lb3_1 = LPG_Monthly.LB3()
        var_1 = YEAR(lb3_1)
        return var_1

@register(LPG_Monthly)
class LC2():
    # 'LPG_Monthly'!LC2
    value = 2018
    formula = "=YEAR(LC3)"
    @eval_fn
    def LC2():
        lc3_1 = LPG_Monthly.LC3()
        var_1 = YEAR(lc3_1)
        return var_1

@register(LPG_Monthly)
class LD2():
    # 'LPG_Monthly'!LD2
    value = 2018
    formula = "=YEAR(LD3)"
    @eval_fn
    def LD2():
        ld3_1 = LPG_Monthly.LD3()
        var_1 = YEAR(ld3_1)
        return var_1

@register(LPG_Monthly)
class LE2():
    # 'LPG_Monthly'!LE2
    value = 2018
    formula = "=YEAR(LE3)"
    @eval_fn
    def LE2():
        le3_1 = LPG_Monthly.LE3()
        var_1 = YEAR(le3_1)
        return var_1

@register(LPG_Monthly)
class LF2():
    # 'LPG_Monthly'!LF2
    value = 2018
    formula = "=YEAR(LF3)"
    @eval_fn
    def LF2():
        lf3_1 = LPG_Monthly.LF3()
        var_1 = YEAR(lf3_1)
        return var_1

@register(LPG_Monthly)
class LG2():
    # 'LPG_Monthly'!LG2
    value = 2018
    formula = "=YEAR(LG3)"
    @eval_fn
    def LG2():
        lg3_1 = LPG_Monthly.LG3()
        var_1 = YEAR(lg3_1)
        return var_1

@register(LPG_Monthly)
class LH2():
    # 'LPG_Monthly'!LH2
    value = 2018
    formula = "=YEAR(LH3)"
    @eval_fn
    def LH2():
        lh3_1 = LPG_Monthly.LH3()
        var_1 = YEAR(lh3_1)
        return var_1

@register(LPG_Monthly)
class LI2():
    # 'LPG_Monthly'!LI2
    value = 2018
    formula = "=YEAR(LI3)"
    @eval_fn
    def LI2():
        li3_1 = LPG_Monthly.LI3()
        var_1 = YEAR(li3_1)
        return var_1

@register(LPG_Monthly)
class LJ2():
    # 'LPG_Monthly'!LJ2
    value = 2019
    formula = "=YEAR(LJ3)"
    @eval_fn
    def LJ2():
        lj3_1 = LPG_Monthly.LJ3()
        var_1 = YEAR(lj3_1)
        return var_1

@register(LPG_Monthly)
class LK2():
    # 'LPG_Monthly'!LK2
    value = 2019
    formula = "=YEAR(LK3)"
    @eval_fn
    def LK2():
        lk3_1 = LPG_Monthly.LK3()
        var_1 = YEAR(lk3_1)
        return var_1

@register(LPG_Monthly)
class LL2():
    # 'LPG_Monthly'!LL2
    value = 2019
    formula = "=YEAR(LL3)"
    @eval_fn
    def LL2():
        ll3_1 = LPG_Monthly.LL3()
        var_1 = YEAR(ll3_1)
        return var_1

@register(LPG_Monthly)
class LM2():
    # 'LPG_Monthly'!LM2
    value = 2019
    formula = "=YEAR(LM3)"
    @eval_fn
    def LM2():
        lm3_1 = LPG_Monthly.LM3()
        var_1 = YEAR(lm3_1)
        return var_1

@register(LPG_Monthly)
class LN2():
    # 'LPG_Monthly'!LN2
    value = 2019
    formula = "=YEAR(LN3)"
    @eval_fn
    def LN2():
        ln3_1 = LPG_Monthly.LN3()
        var_1 = YEAR(ln3_1)
        return var_1

@register(LPG_Monthly)
class LO2():
    # 'LPG_Monthly'!LO2
    value = 2019
    formula = "=YEAR(LO3)"
    @eval_fn
    def LO2():
        lo3_1 = LPG_Monthly.LO3()
        var_1 = YEAR(lo3_1)
        return var_1

@register(LPG_Monthly)
class LP2():
    # 'LPG_Monthly'!LP2
    value = 2019
    formula = "=YEAR(LP3)"
    @eval_fn
    def LP2():
        lp3_1 = LPG_Monthly.LP3()
        var_1 = YEAR(lp3_1)
        return var_1

@register(LPG_Monthly)
class LQ2():
    # 'LPG_Monthly'!LQ2
    value = 2019
    formula = "=YEAR(LQ3)"
    @eval_fn
    def LQ2():
        lq3_1 = LPG_Monthly.LQ3()
        var_1 = YEAR(lq3_1)
        return var_1

@register(LPG_Monthly)
class LR2():
    # 'LPG_Monthly'!LR2
    value = 2019
    formula = "=YEAR(LR3)"
    @eval_fn
    def LR2():
        lr3_1 = LPG_Monthly.LR3()
        var_1 = YEAR(lr3_1)
        return var_1

@register(LPG_Monthly)
class LS2():
    # 'LPG_Monthly'!LS2
    value = 2019
    formula = "=YEAR(LS3)"
    @eval_fn
    def LS2():
        ls3_1 = LPG_Monthly.LS3()
        var_1 = YEAR(ls3_1)
        return var_1

@register(LPG_Monthly)
class LT2():
    # 'LPG_Monthly'!LT2
    value = 2019
    formula = "=YEAR(LT3)"
    @eval_fn
    def LT2():
        lt3_1 = LPG_Monthly.LT3()
        var_1 = YEAR(lt3_1)
        return var_1

@register(LPG_Monthly)
class LU2():
    # 'LPG_Monthly'!LU2
    value = 2019
    formula = "=YEAR(LU3)"
    @eval_fn
    def LU2():
        lu3_1 = LPG_Monthly.LU3()
        var_1 = YEAR(lu3_1)
        return var_1

@register(LPG_Monthly)
class LV2():
    # 'LPG_Monthly'!LV2
    value = 2020
    formula = "=YEAR(LV3)"
    @eval_fn
    def LV2():
        lv3_1 = LPG_Monthly.LV3()
        var_1 = YEAR(lv3_1)
        return var_1

@register(LPG_Monthly)
class LW2():
    # 'LPG_Monthly'!LW2
    value = 2020
    formula = "=YEAR(LW3)"
    @eval_fn
    def LW2():
        lw3_1 = LPG_Monthly.LW3()
        var_1 = YEAR(lw3_1)
        return var_1

@register(LPG_Monthly)
class LX2():
    # 'LPG_Monthly'!LX2
    value = 2020
    formula = "=YEAR(LX3)"
    @eval_fn
    def LX2():
        lx3_1 = LPG_Monthly.LX3()
        var_1 = YEAR(lx3_1)
        return var_1

@register(LPG_Monthly)
class LY2():
    # 'LPG_Monthly'!LY2
    value = 2020
    formula = "=YEAR(LY3)"
    @eval_fn
    def LY2():
        ly3_1 = LPG_Monthly.LY3()
        var_1 = YEAR(ly3_1)
        return var_1

@register(LPG_Monthly)
class LZ2():
    # 'LPG_Monthly'!LZ2
    value = 2020
    formula = "=YEAR(LZ3)"
    @eval_fn
    def LZ2():
        lz3_1 = LPG_Monthly.LZ3()
        var_1 = YEAR(lz3_1)
        return var_1

@register(LPG_Monthly)
class MA2():
    # 'LPG_Monthly'!MA2
    value = 2020
    formula = "=YEAR(MA3)"
    @eval_fn
    def MA2():
        ma3_1 = LPG_Monthly.MA3()
        var_1 = YEAR(ma3_1)
        return var_1

@register(LPG_Monthly)
class MB2():
    # 'LPG_Monthly'!MB2
    value = 2020
    formula = "=YEAR(MB3)"
    @eval_fn
    def MB2():
        mb3_1 = LPG_Monthly.MB3()
        var_1 = YEAR(mb3_1)
        return var_1

@register(LPG_Monthly)
class MC2():
    # 'LPG_Monthly'!MC2
    value = 2020
    formula = "=YEAR(MC3)"
    @eval_fn
    def MC2():
        mc3_1 = LPG_Monthly.MC3()
        var_1 = YEAR(mc3_1)
        return var_1

@register(LPG_Monthly)
class MD2():
    # 'LPG_Monthly'!MD2
    value = 2020
    formula = "=YEAR(MD3)"
    @eval_fn
    def MD2():
        md3_1 = LPG_Monthly.MD3()
        var_1 = YEAR(md3_1)
        return var_1

@register(LPG_Monthly)
class ME2():
    # 'LPG_Monthly'!ME2
    value = 2020
    formula = "=YEAR(ME3)"
    @eval_fn
    def ME2():
        me3_1 = LPG_Monthly.ME3()
        var_1 = YEAR(me3_1)
        return var_1

@register(LPG_Monthly)
class MF2():
    # 'LPG_Monthly'!MF2
    value = 2020
    formula = "=YEAR(MF3)"
    @eval_fn
    def MF2():
        mf3_1 = LPG_Monthly.MF3()
        var_1 = YEAR(mf3_1)
        return var_1

@register(LPG_Monthly)
class MG2():
    # 'LPG_Monthly'!MG2
    value = 2020
    formula = "=YEAR(MG3)"
    @eval_fn
    def MG2():
        mg3_1 = LPG_Monthly.MG3()
        var_1 = YEAR(mg3_1)
        return var_1

@register(LPG_Monthly)
class MH2():
    # 'LPG_Monthly'!MH2
    value = 2021
    formula = "=YEAR(MH3)"
    @eval_fn
    def MH2():
        mh3_1 = LPG_Monthly.MH3()
        var_1 = YEAR(mh3_1)
        return var_1

@register(LPG_Monthly)
class MI2():
    # 'LPG_Monthly'!MI2
    value = 2021
    formula = "=YEAR(MI3)"
    @eval_fn
    def MI2():
        mi3_1 = LPG_Monthly.MI3()
        var_1 = YEAR(mi3_1)
        return var_1

@register(LPG_Monthly)
class MJ2():
    # 'LPG_Monthly'!MJ2
    value = 2021
    formula = "=YEAR(MJ3)"
    @eval_fn
    def MJ2():
        mj3_1 = LPG_Monthly.MJ3()
        var_1 = YEAR(mj3_1)
        return var_1

@register(LPG_Monthly)
class MK2():
    # 'LPG_Monthly'!MK2
    value = 2021
    formula = "=YEAR(MK3)"
    @eval_fn
    def MK2():
        mk3_1 = LPG_Monthly.MK3()
        var_1 = YEAR(mk3_1)
        return var_1

@register(LPG_Monthly)
class ML2():
    # 'LPG_Monthly'!ML2
    value = 2021
    formula = "=YEAR(ML3)"
    @eval_fn
    def ML2():
        ml3_1 = LPG_Monthly.ML3()
        var_1 = YEAR(ml3_1)
        return var_1

@register(LPG_Monthly)
class MM2():
    # 'LPG_Monthly'!MM2
    value = 2021
    formula = "=YEAR(MM3)"
    @eval_fn
    def MM2():
        mm3_1 = LPG_Monthly.MM3()
        var_1 = YEAR(mm3_1)
        return var_1

@register(LPG_Monthly)
class MN2():
    # 'LPG_Monthly'!MN2
    value = 2021
    formula = "=YEAR(MN3)"
    @eval_fn
    def MN2():
        mn3_1 = LPG_Monthly.MN3()
        var_1 = YEAR(mn3_1)
        return var_1

@register(LPG_Monthly)
class MO2():
    # 'LPG_Monthly'!MO2
    value = 2021
    formula = "=YEAR(MO3)"
    @eval_fn
    def MO2():
        mo3_1 = LPG_Monthly.MO3()
        var_1 = YEAR(mo3_1)
        return var_1

@register(LPG_Monthly)
class MP2():
    # 'LPG_Monthly'!MP2
    value = 2021
    formula = "=YEAR(MP3)"
    @eval_fn
    def MP2():
        mp3_1 = LPG_Monthly.MP3()
        var_1 = YEAR(mp3_1)
        return var_1

@register(LPG_Monthly)
class MQ2():
    # 'LPG_Monthly'!MQ2
    value = 2021
    formula = "=YEAR(MQ3)"
    @eval_fn
    def MQ2():
        mq3_1 = LPG_Monthly.MQ3()
        var_1 = YEAR(mq3_1)
        return var_1

@register(LPG_Monthly)
class MR2():
    # 'LPG_Monthly'!MR2
    value = 2021
    formula = "=YEAR(MR3)"
    @eval_fn
    def MR2():
        mr3_1 = LPG_Monthly.MR3()
        var_1 = YEAR(mr3_1)
        return var_1

@register(LPG_Monthly)
class MS2():
    # 'LPG_Monthly'!MS2
    value = 2021
    formula = "=YEAR(MS3)"
    @eval_fn
    def MS2():
        ms3_1 = LPG_Monthly.MS3()
        var_1 = YEAR(ms3_1)
        return var_1

@register(LPG_Monthly)
class MT2():
    # 'LPG_Monthly'!MT2
    value = 2022
    formula = "=YEAR(MT3)"
    @eval_fn
    def MT2():
        mt3_1 = LPG_Monthly.MT3()
        var_1 = YEAR(mt3_1)
        return var_1

@register(LPG_Monthly)
class MU2():
    # 'LPG_Monthly'!MU2
    value = 2022
    formula = "=YEAR(MU3)"
    @eval_fn
    def MU2():
        mu3_1 = LPG_Monthly.MU3()
        var_1 = YEAR(mu3_1)
        return var_1

@register(LPG_Monthly)
class MV2():
    # 'LPG_Monthly'!MV2
    value = 2022
    formula = "=YEAR(MV3)"
    @eval_fn
    def MV2():
        mv3_1 = LPG_Monthly.MV3()
        var_1 = YEAR(mv3_1)
        return var_1

@register(LPG_Monthly)
class MW2():
    # 'LPG_Monthly'!MW2
    value = 2022
    formula = "=YEAR(MW3)"
    @eval_fn
    def MW2():
        mw3_1 = LPG_Monthly.MW3()
        var_1 = YEAR(mw3_1)
        return var_1

@register(LPG_Monthly)
class MX2():
    # 'LPG_Monthly'!MX2
    value = 2022
    formula = "=YEAR(MX3)"
    @eval_fn
    def MX2():
        mx3_1 = LPG_Monthly.MX3()
        var_1 = YEAR(mx3_1)
        return var_1

@register(LPG_Monthly)
class MY2():
    # 'LPG_Monthly'!MY2
    value = 2022
    formula = "=YEAR(MY3)"
    @eval_fn
    def MY2():
        my3_1 = LPG_Monthly.MY3()
        var_1 = YEAR(my3_1)
        return var_1

@register(LPG_Monthly)
class MZ2():
    # 'LPG_Monthly'!MZ2
    value = 2022
    formula = "=YEAR(MZ3)"
    @eval_fn
    def MZ2():
        mz3_1 = LPG_Monthly.MZ3()
        var_1 = YEAR(mz3_1)
        return var_1

@register(LPG_Monthly)
class NA2():
    # 'LPG_Monthly'!NA2
    value = 2022
    formula = "=YEAR(NA3)"
    @eval_fn
    def NA2():
        na3_1 = LPG_Monthly.NA3()
        var_1 = YEAR(na3_1)
        return var_1

@register(LPG_Monthly)
class NB2():
    # 'LPG_Monthly'!NB2
    value = 2022
    formula = "=YEAR(NB3)"
    @eval_fn
    def NB2():
        nb3_1 = LPG_Monthly.NB3()
        var_1 = YEAR(nb3_1)
        return var_1

@register(LPG_Monthly)
class NC2():
    # 'LPG_Monthly'!NC2
    value = 2022
    formula = "=YEAR(NC3)"
    @eval_fn
    def NC2():
        nc3_1 = LPG_Monthly.NC3()
        var_1 = YEAR(nc3_1)
        return var_1

@register(LPG_Monthly)
class ND2():
    # 'LPG_Monthly'!ND2
    value = 2022
    formula = "=YEAR(ND3)"
    @eval_fn
    def ND2():
        nd3_1 = LPG_Monthly.ND3()
        var_1 = YEAR(nd3_1)
        return var_1

@register(LPG_Monthly)
class NE2():
    # 'LPG_Monthly'!NE2
    value = 2022
    formula = "=YEAR(NE3)"
    @eval_fn
    def NE2():
        ne3_1 = LPG_Monthly.NE3()
        var_1 = YEAR(ne3_1)
        return var_1

@register(LPG_Monthly)
class NF2():
    # 'LPG_Monthly'!NF2
    value = 2023
    formula = "=YEAR(NF3)"
    @eval_fn
    def NF2():
        nf3_1 = LPG_Monthly.NF3()
        var_1 = YEAR(nf3_1)
        return var_1

@register(LPG_Monthly)
class NG2():
    # 'LPG_Monthly'!NG2
    value = 2023
    formula = "=YEAR(NG3)"
    @eval_fn
    def NG2():
        ng3_1 = LPG_Monthly.NG3()
        var_1 = YEAR(ng3_1)
        return var_1

@register(LPG_Monthly)
class NH2():
    # 'LPG_Monthly'!NH2
    value = 2023
    formula = "=YEAR(NH3)"
    @eval_fn
    def NH2():
        nh3_1 = LPG_Monthly.NH3()
        var_1 = YEAR(nh3_1)
        return var_1

@register(LPG_Monthly)
class NI2():
    # 'LPG_Monthly'!NI2
    value = 2023
    formula = "=YEAR(NI3)"
    @eval_fn
    def NI2():
        ni3_1 = LPG_Monthly.NI3()
        var_1 = YEAR(ni3_1)
        return var_1

@register(LPG_Monthly)
class NJ2():
    # 'LPG_Monthly'!NJ2
    value = 2023
    formula = "=YEAR(NJ3)"
    @eval_fn
    def NJ2():
        nj3_1 = LPG_Monthly.NJ3()
        var_1 = YEAR(nj3_1)
        return var_1

@register(LPG_Monthly)
class NK2():
    # 'LPG_Monthly'!NK2
    value = 2023
    formula = "=YEAR(NK3)"
    @eval_fn
    def NK2():
        nk3_1 = LPG_Monthly.NK3()
        var_1 = YEAR(nk3_1)
        return var_1

@register(LPG_Monthly)
class NL2():
    # 'LPG_Monthly'!NL2
    value = 2023
    formula = "=YEAR(NL3)"
    @eval_fn
    def NL2():
        nl3_1 = LPG_Monthly.NL3()
        var_1 = YEAR(nl3_1)
        return var_1

@register(LPG_Monthly)
class NM2():
    # 'LPG_Monthly'!NM2
    value = 2023
    formula = "=YEAR(NM3)"
    @eval_fn
    def NM2():
        nm3_1 = LPG_Monthly.NM3()
        var_1 = YEAR(nm3_1)
        return var_1

@register(LPG_Monthly)
class NN2():
    # 'LPG_Monthly'!NN2
    value = 2023
    formula = "=YEAR(NN3)"
    @eval_fn
    def NN2():
        nn3_1 = LPG_Monthly.NN3()
        var_1 = YEAR(nn3_1)
        return var_1

@register(LPG_Monthly)
class NO2():
    # 'LPG_Monthly'!NO2
    value = 2023
    formula = "=YEAR(NO3)"
    @eval_fn
    def NO2():
        no3_1 = LPG_Monthly.NO3()
        var_1 = YEAR(no3_1)
        return var_1

@register(LPG_Monthly)
class NP2():
    # 'LPG_Monthly'!NP2
    value = 2023
    formula = "=YEAR(NP3)"
    @eval_fn
    def NP2():
        np3_1 = LPG_Monthly.NP3()
        var_1 = YEAR(np3_1)
        return var_1

@register(LPG_Monthly)
class NQ2():
    # 'LPG_Monthly'!NQ2
    value = 2023
    formula = "=YEAR(NQ3)"
    @eval_fn
    def NQ2():
        nq3_1 = LPG_Monthly.NQ3()
        var_1 = YEAR(nq3_1)
        return var_1

@register(LPG_Monthly)
class NR2():
    # 'LPG_Monthly'!NR2
    value = 2024
    formula = "=YEAR(NR3)"
    @eval_fn
    def NR2():
        nr3_1 = LPG_Monthly.NR3()
        var_1 = YEAR(nr3_1)
        return var_1

@register(LPG_Monthly)
class NS2():
    # 'LPG_Monthly'!NS2
    value = 2024
    formula = "=YEAR(NS3)"
    @eval_fn
    def NS2():
        ns3_1 = LPG_Monthly.NS3()
        var_1 = YEAR(ns3_1)
        return var_1

@register(LPG_Monthly)
class NT2():
    # 'LPG_Monthly'!NT2
    value = 2024
    formula = "=YEAR(NT3)"
    @eval_fn
    def NT2():
        nt3_1 = LPG_Monthly.NT3()
        var_1 = YEAR(nt3_1)
        return var_1

@register(LPG_Monthly)
class NU2():
    # 'LPG_Monthly'!NU2
    value = 2024
    formula = "=YEAR(NU3)"
    @eval_fn
    def NU2():
        nu3_1 = LPG_Monthly.NU3()
        var_1 = YEAR(nu3_1)
        return var_1

@register(LPG_Monthly)
class NV2():
    # 'LPG_Monthly'!NV2
    value = 2024
    formula = "=YEAR(NV3)"
    @eval_fn
    def NV2():
        nv3_1 = LPG_Monthly.NV3()
        var_1 = YEAR(nv3_1)
        return var_1

@register(LPG_Monthly)
class NW2():
    # 'LPG_Monthly'!NW2
    value = 2024
    formula = "=YEAR(NW3)"
    @eval_fn
    def NW2():
        nw3_1 = LPG_Monthly.NW3()
        var_1 = YEAR(nw3_1)
        return var_1

@register(LPG_Monthly)
class NX2():
    # 'LPG_Monthly'!NX2
    value = 2024
    formula = "=YEAR(NX3)"
    @eval_fn
    def NX2():
        nx3_1 = LPG_Monthly.NX3()
        var_1 = YEAR(nx3_1)
        return var_1

@register(LPG_Monthly)
class NY2():
    # 'LPG_Monthly'!NY2
    value = 2024
    formula = "=YEAR(NY3)"
    @eval_fn
    def NY2():
        ny3_1 = LPG_Monthly.NY3()
        var_1 = YEAR(ny3_1)
        return var_1

@register(LPG_Monthly)
class NZ2():
    # 'LPG_Monthly'!NZ2
    value = 2024
    formula = "=YEAR(NZ3)"
    @eval_fn
    def NZ2():
        nz3_1 = LPG_Monthly.NZ3()
        var_1 = YEAR(nz3_1)
        return var_1

@register(LPG_Monthly)
class OA2():
    # 'LPG_Monthly'!OA2
    value = 2024
    formula = "=YEAR(OA3)"
    @eval_fn
    def OA2():
        oa3_1 = LPG_Monthly.OA3()
        var_1 = YEAR(oa3_1)
        return var_1

@register(LPG_Monthly)
class OB2():
    # 'LPG_Monthly'!OB2
    value = 2024
    formula = "=YEAR(OB3)"
    @eval_fn
    def OB2():
        ob3_1 = LPG_Monthly.OB3()
        var_1 = YEAR(ob3_1)
        return var_1

@register(LPG_Monthly)
class OC2():
    # 'LPG_Monthly'!OC2
    value = 2024
    formula = "=YEAR(OC3)"
    @eval_fn
    def OC2():
        oc3_1 = LPG_Monthly.OC3()
        var_1 = YEAR(oc3_1)
        return var_1

@register(LPG_Monthly)
class OD2():
    # 'LPG_Monthly'!OD2
    value = 2025
    formula = "=YEAR(OD3)"
    @eval_fn
    def OD2():
        od3_1 = LPG_Monthly.OD3()
        var_1 = YEAR(od3_1)
        return var_1

@register(LPG_Monthly)
class OE2():
    # 'LPG_Monthly'!OE2
    value = 2025
    formula = "=YEAR(OE3)"
    @eval_fn
    def OE2():
        oe3_1 = LPG_Monthly.OE3()
        var_1 = YEAR(oe3_1)
        return var_1

@register(LPG_Monthly)
class OF2():
    # 'LPG_Monthly'!OF2
    value = 2025
    formula = "=YEAR(OF3)"
    @eval_fn
    def OF2():
        of3_1 = LPG_Monthly.OF3()
        var_1 = YEAR(of3_1)
        return var_1

@register(LPG_Monthly)
class OG2():
    # 'LPG_Monthly'!OG2
    value = 2025
    formula = "=YEAR(OG3)"
    @eval_fn
    def OG2():
        og3_1 = LPG_Monthly.OG3()
        var_1 = YEAR(og3_1)
        return var_1

@register(LPG_Monthly)
class OH2():
    # 'LPG_Monthly'!OH2
    value = 2025
    formula = "=YEAR(OH3)"
    @eval_fn
    def OH2():
        oh3_1 = LPG_Monthly.OH3()
        var_1 = YEAR(oh3_1)
        return var_1

@register(LPG_Monthly)
class OI2():
    # 'LPG_Monthly'!OI2
    value = 2025
    formula = "=YEAR(OI3)"
    @eval_fn
    def OI2():
        oi3_1 = LPG_Monthly.OI3()
        var_1 = YEAR(oi3_1)
        return var_1

@register(LPG_Monthly)
class OJ2():
    # 'LPG_Monthly'!OJ2
    value = 2025
    formula = "=YEAR(OJ3)"
    @eval_fn
    def OJ2():
        oj3_1 = LPG_Monthly.OJ3()
        var_1 = YEAR(oj3_1)
        return var_1

@register(LPG_Monthly)
class OK2():
    # 'LPG_Monthly'!OK2
    value = 2025
    formula = "=YEAR(OK3)"
    @eval_fn
    def OK2():
        ok3_1 = LPG_Monthly.OK3()
        var_1 = YEAR(ok3_1)
        return var_1

@register(LPG_Monthly)
class OL2():
    # 'LPG_Monthly'!OL2
    value = 2025
    formula = "=YEAR(OL3)"
    @eval_fn
    def OL2():
        ol3_1 = LPG_Monthly.OL3()
        var_1 = YEAR(ol3_1)
        return var_1

@register(LPG_Monthly)
class OM2():
    # 'LPG_Monthly'!OM2
    value = 2025
    formula = "=YEAR(OM3)"
    @eval_fn
    def OM2():
        om3_1 = LPG_Monthly.OM3()
        var_1 = YEAR(om3_1)
        return var_1

@register(LPG_Monthly)
class ON2():
    # 'LPG_Monthly'!ON2
    value = 2025
    formula = "=YEAR(ON3)"
    @eval_fn
    def ON2():
        on3_1 = LPG_Monthly.ON3()
        var_1 = YEAR(on3_1)
        return var_1

@register(LPG_Monthly)
class OO2():
    # 'LPG_Monthly'!OO2
    value = 2025
    formula = "=YEAR(OO3)"
    @eval_fn
    def OO2():
        oo3_1 = LPG_Monthly.OO3()
        var_1 = YEAR(oo3_1)
        return var_1

@register(LPG_Monthly)
class OP2():
    # 'LPG_Monthly'!OP2
    value = 2026
    formula = "=YEAR(OP3)"
    @eval_fn
    def OP2():
        op3_1 = LPG_Monthly.OP3()
        var_1 = YEAR(op3_1)
        return var_1

@register(LPG_Monthly)
class OQ2():
    # 'LPG_Monthly'!OQ2
    value = 2026
    formula = "=YEAR(OQ3)"
    @eval_fn
    def OQ2():
        oq3_1 = LPG_Monthly.OQ3()
        var_1 = YEAR(oq3_1)
        return var_1

@register(LPG_Monthly)
class OR2():
    # 'LPG_Monthly'!OR2
    value = 2026
    formula = "=YEAR(OR3)"
    @eval_fn
    def OR2():
        or3_1 = LPG_Monthly.OR3()
        var_1 = YEAR(or3_1)
        return var_1

@register(LPG_Monthly)
class OS2():
    # 'LPG_Monthly'!OS2
    value = 2026
    formula = "=YEAR(OS3)"
    @eval_fn
    def OS2():
        os3_1 = LPG_Monthly.OS3()
        var_1 = YEAR(os3_1)
        return var_1

@register(LPG_Monthly)
class OT2():
    # 'LPG_Monthly'!OT2
    value = 2026
    formula = "=YEAR(OT3)"
    @eval_fn
    def OT2():
        ot3_1 = LPG_Monthly.OT3()
        var_1 = YEAR(ot3_1)
        return var_1

@register(LPG_Monthly)
class OU2():
    # 'LPG_Monthly'!OU2
    value = 2026
    formula = "=YEAR(OU3)"
    @eval_fn
    def OU2():
        ou3_1 = LPG_Monthly.OU3()
        var_1 = YEAR(ou3_1)
        return var_1

@register(LPG_Monthly)
class OV2():
    # 'LPG_Monthly'!OV2
    value = 2026
    formula = "=YEAR(OV3)"
    @eval_fn
    def OV2():
        ov3_1 = LPG_Monthly.OV3()
        var_1 = YEAR(ov3_1)
        return var_1

@register(LPG_Monthly)
class OW2():
    # 'LPG_Monthly'!OW2
    value = 2026
    formula = "=YEAR(OW3)"
    @eval_fn
    def OW2():
        ow3_1 = LPG_Monthly.OW3()
        var_1 = YEAR(ow3_1)
        return var_1

@register(LPG_Monthly)
class OX2():
    # 'LPG_Monthly'!OX2
    value = 2026
    formula = "=YEAR(OX3)"
    @eval_fn
    def OX2():
        ox3_1 = LPG_Monthly.OX3()
        var_1 = YEAR(ox3_1)
        return var_1

@register(LPG_Monthly)
class OY2():
    # 'LPG_Monthly'!OY2
    value = 2026
    formula = "=YEAR(OY3)"
    @eval_fn
    def OY2():
        oy3_1 = LPG_Monthly.OY3()
        var_1 = YEAR(oy3_1)
        return var_1

@register(LPG_Monthly)
class OZ2():
    # 'LPG_Monthly'!OZ2
    value = 2026
    formula = "=YEAR(OZ3)"
    @eval_fn
    def OZ2():
        oz3_1 = LPG_Monthly.OZ3()
        var_1 = YEAR(oz3_1)
        return var_1

@register(LPG_Monthly)
class PA2():
    # 'LPG_Monthly'!PA2
    value = 2026
    formula = "=YEAR(PA3)"
    @eval_fn
    def PA2():
        pa3_1 = LPG_Monthly.PA3()
        var_1 = YEAR(pa3_1)
        return var_1

@register(LPG_Monthly)
class PB2():
    # 'LPG_Monthly'!PB2
    value = 2027
    formula = "=YEAR(PB3)"
    @eval_fn
    def PB2():
        pb3_1 = LPG_Monthly.PB3()
        var_1 = YEAR(pb3_1)
        return var_1

@register(LPG_Monthly)
class PC2():
    # 'LPG_Monthly'!PC2
    value = 2027
    formula = "=YEAR(PC3)"
    @eval_fn
    def PC2():
        pc3_1 = LPG_Monthly.PC3()
        var_1 = YEAR(pc3_1)
        return var_1

@register(LPG_Monthly)
class PD2():
    # 'LPG_Monthly'!PD2
    value = 2027
    formula = "=YEAR(PD3)"
    @eval_fn
    def PD2():
        pd3_1 = LPG_Monthly.PD3()
        var_1 = YEAR(pd3_1)
        return var_1

@register(LPG_Monthly)
class PE2():
    # 'LPG_Monthly'!PE2
    value = 2027
    formula = "=YEAR(PE3)"
    @eval_fn
    def PE2():
        pe3_1 = LPG_Monthly.PE3()
        var_1 = YEAR(pe3_1)
        return var_1

@register(LPG_Monthly)
class PF2():
    # 'LPG_Monthly'!PF2
    value = 2027
    formula = "=YEAR(PF3)"
    @eval_fn
    def PF2():
        pf3_1 = LPG_Monthly.PF3()
        var_1 = YEAR(pf3_1)
        return var_1

@register(LPG_Monthly)
class PG2():
    # 'LPG_Monthly'!PG2
    value = 2027
    formula = "=YEAR(PG3)"
    @eval_fn
    def PG2():
        pg3_1 = LPG_Monthly.PG3()
        var_1 = YEAR(pg3_1)
        return var_1

@register(LPG_Monthly)
class PH2():
    # 'LPG_Monthly'!PH2
    value = 2027
    formula = "=YEAR(PH3)"
    @eval_fn
    def PH2():
        ph3_1 = LPG_Monthly.PH3()
        var_1 = YEAR(ph3_1)
        return var_1

@register(LPG_Monthly)
class PI2():
    # 'LPG_Monthly'!PI2
    value = 2027
    formula = "=YEAR(PI3)"
    @eval_fn
    def PI2():
        pi3_1 = LPG_Monthly.PI3()
        var_1 = YEAR(pi3_1)
        return var_1

@register(LPG_Monthly)
class PJ2():
    # 'LPG_Monthly'!PJ2
    value = 2027
    formula = "=YEAR(PJ3)"
    @eval_fn
    def PJ2():
        pj3_1 = LPG_Monthly.PJ3()
        var_1 = YEAR(pj3_1)
        return var_1

@register(LPG_Monthly)
class PK2():
    # 'LPG_Monthly'!PK2
    value = 2027
    formula = "=YEAR(PK3)"
    @eval_fn
    def PK2():
        pk3_1 = LPG_Monthly.PK3()
        var_1 = YEAR(pk3_1)
        return var_1

@register(LPG_Monthly)
class PL2():
    # 'LPG_Monthly'!PL2
    value = 2027
    formula = "=YEAR(PL3)"
    @eval_fn
    def PL2():
        pl3_1 = LPG_Monthly.PL3()
        var_1 = YEAR(pl3_1)
        return var_1

@register(LPG_Monthly)
class PM2():
    # 'LPG_Monthly'!PM2
    value = 2027
    formula = "=YEAR(PM3)"
    @eval_fn
    def PM2():
        pm3_1 = LPG_Monthly.PM3()
        var_1 = YEAR(pm3_1)
        return var_1

@register(LPG_Monthly)
class PN2():
    # 'LPG_Monthly'!PN2
    value = 2028
    formula = "=YEAR(PN3)"
    @eval_fn
    def PN2():
        pn3_1 = LPG_Monthly.PN3()
        var_1 = YEAR(pn3_1)
        return var_1

@register(LPG_Monthly)
class PO2():
    # 'LPG_Monthly'!PO2
    value = 2028
    formula = "=YEAR(PO3)"
    @eval_fn
    def PO2():
        po3_1 = LPG_Monthly.PO3()
        var_1 = YEAR(po3_1)
        return var_1

@register(LPG_Monthly)
class PP2():
    # 'LPG_Monthly'!PP2
    value = 2028
    formula = "=YEAR(PP3)"
    @eval_fn
    def PP2():
        pp3_1 = LPG_Monthly.PP3()
        var_1 = YEAR(pp3_1)
        return var_1

@register(LPG_Monthly)
class PQ2():
    # 'LPG_Monthly'!PQ2
    value = 2028
    formula = "=YEAR(PQ3)"
    @eval_fn
    def PQ2():
        pq3_1 = LPG_Monthly.PQ3()
        var_1 = YEAR(pq3_1)
        return var_1

@register(LPG_Monthly)
class PR2():
    # 'LPG_Monthly'!PR2
    value = 2028
    formula = "=YEAR(PR3)"
    @eval_fn
    def PR2():
        pr3_1 = LPG_Monthly.PR3()
        var_1 = YEAR(pr3_1)
        return var_1

@register(LPG_Monthly)
class PS2():
    # 'LPG_Monthly'!PS2
    value = 2028
    formula = "=YEAR(PS3)"
    @eval_fn
    def PS2():
        ps3_1 = LPG_Monthly.PS3()
        var_1 = YEAR(ps3_1)
        return var_1

@register(LPG_Monthly)
class PT2():
    # 'LPG_Monthly'!PT2
    value = 2028
    formula = "=YEAR(PT3)"
    @eval_fn
    def PT2():
        pt3_1 = LPG_Monthly.PT3()
        var_1 = YEAR(pt3_1)
        return var_1

@register(LPG_Monthly)
class PU2():
    # 'LPG_Monthly'!PU2
    value = 2028
    formula = "=YEAR(PU3)"
    @eval_fn
    def PU2():
        pu3_1 = LPG_Monthly.PU3()
        var_1 = YEAR(pu3_1)
        return var_1

@register(LPG_Monthly)
class PV2():
    # 'LPG_Monthly'!PV2
    value = 2028
    formula = "=YEAR(PV3)"
    @eval_fn
    def PV2():
        pv3_1 = LPG_Monthly.PV3()
        var_1 = YEAR(pv3_1)
        return var_1

@register(LPG_Monthly)
class PW2():
    # 'LPG_Monthly'!PW2
    value = 2028
    formula = "=YEAR(PW3)"
    @eval_fn
    def PW2():
        pw3_1 = LPG_Monthly.PW3()
        var_1 = YEAR(pw3_1)
        return var_1

@register(LPG_Monthly)
class PX2():
    # 'LPG_Monthly'!PX2
    value = 2028
    formula = "=YEAR(PX3)"
    @eval_fn
    def PX2():
        px3_1 = LPG_Monthly.PX3()
        var_1 = YEAR(px3_1)
        return var_1

@register(LPG_Monthly)
class PY2():
    # 'LPG_Monthly'!PY2
    value = 2028
    formula = "=YEAR(PY3)"
    @eval_fn
    def PY2():
        py3_1 = LPG_Monthly.PY3()
        var_1 = YEAR(py3_1)
        return var_1

@register(LPG_Monthly)
class PZ2():
    # 'LPG_Monthly'!PZ2
    value = 2029
    formula = "=YEAR(PZ3)"
    @eval_fn
    def PZ2():
        pz3_1 = LPG_Monthly.PZ3()
        var_1 = YEAR(pz3_1)
        return var_1

@register(LPG_Monthly)
class QA2():
    # 'LPG_Monthly'!QA2
    value = 2029
    formula = "=YEAR(QA3)"
    @eval_fn
    def QA2():
        qa3_1 = LPG_Monthly.QA3()
        var_1 = YEAR(qa3_1)
        return var_1

@register(LPG_Monthly)
class QB2():
    # 'LPG_Monthly'!QB2
    value = 2029
    formula = "=YEAR(QB3)"
    @eval_fn
    def QB2():
        qb3_1 = LPG_Monthly.QB3()
        var_1 = YEAR(qb3_1)
        return var_1

@register(LPG_Monthly)
class QC2():
    # 'LPG_Monthly'!QC2
    value = 2029
    formula = "=YEAR(QC3)"
    @eval_fn
    def QC2():
        qc3_1 = LPG_Monthly.QC3()
        var_1 = YEAR(qc3_1)
        return var_1

@register(LPG_Monthly)
class QD2():
    # 'LPG_Monthly'!QD2
    value = 2029
    formula = "=YEAR(QD3)"
    @eval_fn
    def QD2():
        qd3_1 = LPG_Monthly.QD3()
        var_1 = YEAR(qd3_1)
        return var_1

@register(LPG_Monthly)
class QE2():
    # 'LPG_Monthly'!QE2
    value = 2029
    formula = "=YEAR(QE3)"
    @eval_fn
    def QE2():
        qe3_1 = LPG_Monthly.QE3()
        var_1 = YEAR(qe3_1)
        return var_1

@register(LPG_Monthly)
class QF2():
    # 'LPG_Monthly'!QF2
    value = 2029
    formula = "=YEAR(QF3)"
    @eval_fn
    def QF2():
        qf3_1 = LPG_Monthly.QF3()
        var_1 = YEAR(qf3_1)
        return var_1

@register(LPG_Monthly)
class QG2():
    # 'LPG_Monthly'!QG2
    value = 2029
    formula = "=YEAR(QG3)"
    @eval_fn
    def QG2():
        qg3_1 = LPG_Monthly.QG3()
        var_1 = YEAR(qg3_1)
        return var_1

@register(LPG_Monthly)
class QH2():
    # 'LPG_Monthly'!QH2
    value = 2029
    formula = "=YEAR(QH3)"
    @eval_fn
    def QH2():
        qh3_1 = LPG_Monthly.QH3()
        var_1 = YEAR(qh3_1)
        return var_1

@register(LPG_Monthly)
class QI2():
    # 'LPG_Monthly'!QI2
    value = 2029
    formula = "=YEAR(QI3)"
    @eval_fn
    def QI2():
        qi3_1 = LPG_Monthly.QI3()
        var_1 = YEAR(qi3_1)
        return var_1

@register(LPG_Monthly)
class QJ2():
    # 'LPG_Monthly'!QJ2
    value = 2029
    formula = "=YEAR(QJ3)"
    @eval_fn
    def QJ2():
        qj3_1 = LPG_Monthly.QJ3()
        var_1 = YEAR(qj3_1)
        return var_1

@register(LPG_Monthly)
class QK2():
    # 'LPG_Monthly'!QK2
    value = 2029
    formula = "=YEAR(QK3)"
    @eval_fn
    def QK2():
        qk3_1 = LPG_Monthly.QK3()
        var_1 = YEAR(qk3_1)
        return var_1

@register(LPG_Monthly)
class QL2():
    # 'LPG_Monthly'!QL2
    value = 2030
    formula = "=YEAR(QL3)"
    @eval_fn
    def QL2():
        ql3_1 = LPG_Monthly.QL3()
        var_1 = YEAR(ql3_1)
        return var_1

@register(LPG_Monthly)
class QM2():
    # 'LPG_Monthly'!QM2
    value = 2030
    formula = "=YEAR(QM3)"
    @eval_fn
    def QM2():
        qm3_1 = LPG_Monthly.QM3()
        var_1 = YEAR(qm3_1)
        return var_1

@register(LPG_Monthly)
class QN2():
    # 'LPG_Monthly'!QN2
    value = 2030
    formula = "=YEAR(QN3)"
    @eval_fn
    def QN2():
        qn3_1 = LPG_Monthly.QN3()
        var_1 = YEAR(qn3_1)
        return var_1

@register(LPG_Monthly)
class QO2():
    # 'LPG_Monthly'!QO2
    value = 2030
    formula = "=YEAR(QO3)"
    @eval_fn
    def QO2():
        qo3_1 = LPG_Monthly.QO3()
        var_1 = YEAR(qo3_1)
        return var_1

@register(LPG_Monthly)
class QP2():
    # 'LPG_Monthly'!QP2
    value = 2030
    formula = "=YEAR(QP3)"
    @eval_fn
    def QP2():
        qp3_1 = LPG_Monthly.QP3()
        var_1 = YEAR(qp3_1)
        return var_1

@register(LPG_Monthly)
class QQ2():
    # 'LPG_Monthly'!QQ2
    value = 2030
    formula = "=YEAR(QQ3)"
    @eval_fn
    def QQ2():
        qq3_1 = LPG_Monthly.QQ3()
        var_1 = YEAR(qq3_1)
        return var_1

@register(LPG_Monthly)
class QR2():
    # 'LPG_Monthly'!QR2
    value = 2030
    formula = "=YEAR(QR3)"
    @eval_fn
    def QR2():
        qr3_1 = LPG_Monthly.QR3()
        var_1 = YEAR(qr3_1)
        return var_1

@register(LPG_Monthly)
class QS2():
    # 'LPG_Monthly'!QS2
    value = 2030
    formula = "=YEAR(QS3)"
    @eval_fn
    def QS2():
        qs3_1 = LPG_Monthly.QS3()
        var_1 = YEAR(qs3_1)
        return var_1

@register(LPG_Monthly)
class QT2():
    # 'LPG_Monthly'!QT2
    value = 2030
    formula = "=YEAR(QT3)"
    @eval_fn
    def QT2():
        qt3_1 = LPG_Monthly.QT3()
        var_1 = YEAR(qt3_1)
        return var_1

@register(LPG_Monthly)
class QU2():
    # 'LPG_Monthly'!QU2
    value = 2030
    formula = "=YEAR(QU3)"
    @eval_fn
    def QU2():
        qu3_1 = LPG_Monthly.QU3()
        var_1 = YEAR(qu3_1)
        return var_1

@register(LPG_Monthly)
class QV2():
    # 'LPG_Monthly'!QV2
    value = 2030
    formula = "=YEAR(QV3)"
    @eval_fn
    def QV2():
        qv3_1 = LPG_Monthly.QV3()
        var_1 = YEAR(qv3_1)
        return var_1

@register(LPG_Monthly)
class QW2():
    # 'LPG_Monthly'!QW2
    value = 2030
    formula = "=YEAR(QW3)"
    @eval_fn
    def QW2():
        qw3_1 = LPG_Monthly.QW3()
        var_1 = YEAR(qw3_1)
        return var_1

@register(LPG_Monthly)
class A3():
    # 'LPG_Monthly'!A3
    value = "Date"
    formula = "='Input EIA Propane Price'!A2"
    @eval_fn
    def A3():
        a2_1 = Input_EIA_Propane_Price.A2()
        return a2_1

@register(LPG_Monthly)
class B3():
    # 'LPG_Monthly'!B3
    value = "Unit"

@register(LPG_Monthly)
class C3():
    # 'LPG_Monthly'!C3
    value = 33770
    isdatetime = True

@register(LPG_Monthly)
class D3():
    # 'LPG_Monthly'!D3
    value = 33800
    isdatetime = True

@register(LPG_Monthly)
class E3():
    # 'LPG_Monthly'!E3
    value = 33831
    isdatetime = True

@register(LPG_Monthly)
class F3():
    # 'LPG_Monthly'!F3
    value = 33862
    isdatetime = True

@register(LPG_Monthly)
class G3():
    # 'LPG_Monthly'!G3
    value = 33892
    isdatetime = True

@register(LPG_Monthly)
class H3():
    # 'LPG_Monthly'!H3
    value = 33923
    isdatetime = True

@register(LPG_Monthly)
class I3():
    # 'LPG_Monthly'!I3
    value = 33953
    isdatetime = True

@register(LPG_Monthly)
class J3():
    # 'LPG_Monthly'!J3
    value = 33984
    isdatetime = True

@register(LPG_Monthly)
class K3():
    # 'LPG_Monthly'!K3
    value = 34015
    isdatetime = True

@register(LPG_Monthly)
class L3():
    # 'LPG_Monthly'!L3
    value = 34043
    isdatetime = True

@register(LPG_Monthly)
class M3():
    # 'LPG_Monthly'!M3
    value = 34074
    isdatetime = True

@register(LPG_Monthly)
class N3():
    # 'LPG_Monthly'!N3
    value = 34104
    isdatetime = True

@register(LPG_Monthly)
class O3():
    # 'LPG_Monthly'!O3
    value = 34135
    isdatetime = True

@register(LPG_Monthly)
class P3():
    # 'LPG_Monthly'!P3
    value = 34165
    isdatetime = True

@register(LPG_Monthly)
class Q3():
    # 'LPG_Monthly'!Q3
    value = 34196
    isdatetime = True

@register(LPG_Monthly)
class R3():
    # 'LPG_Monthly'!R3
    value = 34227
    isdatetime = True

@register(LPG_Monthly)
class S3():
    # 'LPG_Monthly'!S3
    value = 34257
    isdatetime = True

@register(LPG_Monthly)
class T3():
    # 'LPG_Monthly'!T3
    value = 34288
    isdatetime = True

@register(LPG_Monthly)
class U3():
    # 'LPG_Monthly'!U3
    value = 34318
    isdatetime = True

@register(LPG_Monthly)
class V3():
    # 'LPG_Monthly'!V3
    value = 34349
    isdatetime = True

@register(LPG_Monthly)
class W3():
    # 'LPG_Monthly'!W3
    value = 34380
    isdatetime = True

@register(LPG_Monthly)
class X3():
    # 'LPG_Monthly'!X3
    value = 34408
    isdatetime = True

@register(LPG_Monthly)
class Y3():
    # 'LPG_Monthly'!Y3
    value = 34439
    isdatetime = True

@register(LPG_Monthly)
class Z3():
    # 'LPG_Monthly'!Z3
    value = 34469
    isdatetime = True

@register(LPG_Monthly)
class AA3():
    # 'LPG_Monthly'!AA3
    value = 34500
    isdatetime = True

@register(LPG_Monthly)
class AB3():
    # 'LPG_Monthly'!AB3
    value = 34530
    isdatetime = True

@register(LPG_Monthly)
class AC3():
    # 'LPG_Monthly'!AC3
    value = 34561
    isdatetime = True

@register(LPG_Monthly)
class AD3():
    # 'LPG_Monthly'!AD3
    value = 34592
    isdatetime = True

@register(LPG_Monthly)
class AE3():
    # 'LPG_Monthly'!AE3
    value = 34622
    isdatetime = True

@register(LPG_Monthly)
class AF3():
    # 'LPG_Monthly'!AF3
    value = 34653
    isdatetime = True

@register(LPG_Monthly)
class AG3():
    # 'LPG_Monthly'!AG3
    value = 34683
    isdatetime = True

@register(LPG_Monthly)
class AH3():
    # 'LPG_Monthly'!AH3
    value = 34714
    isdatetime = True

@register(LPG_Monthly)
class AI3():
    # 'LPG_Monthly'!AI3
    value = 34745
    isdatetime = True

@register(LPG_Monthly)
class AJ3():
    # 'LPG_Monthly'!AJ3
    value = 34773
    isdatetime = True

@register(LPG_Monthly)
class AK3():
    # 'LPG_Monthly'!AK3
    value = 34804
    isdatetime = True

@register(LPG_Monthly)
class AL3():
    # 'LPG_Monthly'!AL3
    value = 34834
    isdatetime = True

@register(LPG_Monthly)
class AM3():
    # 'LPG_Monthly'!AM3
    value = 34865
    isdatetime = True

@register(LPG_Monthly)
class AN3():
    # 'LPG_Monthly'!AN3
    value = 34895
    isdatetime = True

@register(LPG_Monthly)
class AO3():
    # 'LPG_Monthly'!AO3
    value = 34926
    isdatetime = True

@register(LPG_Monthly)
class AP3():
    # 'LPG_Monthly'!AP3
    value = 34957
    isdatetime = True

@register(LPG_Monthly)
class AQ3():
    # 'LPG_Monthly'!AQ3
    value = 34987
    isdatetime = True

@register(LPG_Monthly)
class AR3():
    # 'LPG_Monthly'!AR3
    value = 35018
    isdatetime = True

@register(LPG_Monthly)
class AS3():
    # 'LPG_Monthly'!AS3
    value = 35048
    isdatetime = True

@register(LPG_Monthly)
class AT3():
    # 'LPG_Monthly'!AT3
    value = 35079
    isdatetime = True

@register(LPG_Monthly)
class AU3():
    # 'LPG_Monthly'!AU3
    value = 35110
    isdatetime = True

@register(LPG_Monthly)
class AV3():
    # 'LPG_Monthly'!AV3
    value = 35139
    isdatetime = True

@register(LPG_Monthly)
class AW3():
    # 'LPG_Monthly'!AW3
    value = 35170
    isdatetime = True

@register(LPG_Monthly)
class AX3():
    # 'LPG_Monthly'!AX3
    value = 35200
    isdatetime = True

@register(LPG_Monthly)
class AY3():
    # 'LPG_Monthly'!AY3
    value = 35231
    isdatetime = True

@register(LPG_Monthly)
class AZ3():
    # 'LPG_Monthly'!AZ3
    value = 35261
    isdatetime = True

@register(LPG_Monthly)
class BA3():
    # 'LPG_Monthly'!BA3
    value = 35292
    isdatetime = True

@register(LPG_Monthly)
class BB3():
    # 'LPG_Monthly'!BB3
    value = 35323
    isdatetime = True

@register(LPG_Monthly)
class BC3():
    # 'LPG_Monthly'!BC3
    value = 35353
    isdatetime = True

@register(LPG_Monthly)
class BD3():
    # 'LPG_Monthly'!BD3
    value = 35384
    isdatetime = True

@register(LPG_Monthly)
class BE3():
    # 'LPG_Monthly'!BE3
    value = 35414
    isdatetime = True

@register(LPG_Monthly)
class BF3():
    # 'LPG_Monthly'!BF3
    value = 35445
    isdatetime = True

@register(LPG_Monthly)
class BG3():
    # 'LPG_Monthly'!BG3
    value = 35476
    isdatetime = True

@register(LPG_Monthly)
class BH3():
    # 'LPG_Monthly'!BH3
    value = 35504
    isdatetime = True

@register(LPG_Monthly)
class BI3():
    # 'LPG_Monthly'!BI3
    value = 35535
    isdatetime = True

@register(LPG_Monthly)
class BJ3():
    # 'LPG_Monthly'!BJ3
    value = 35565
    isdatetime = True

@register(LPG_Monthly)
class BK3():
    # 'LPG_Monthly'!BK3
    value = 35596
    isdatetime = True

@register(LPG_Monthly)
class BL3():
    # 'LPG_Monthly'!BL3
    value = 35626
    isdatetime = True

@register(LPG_Monthly)
class BM3():
    # 'LPG_Monthly'!BM3
    value = 35657
    isdatetime = True

@register(LPG_Monthly)
class BN3():
    # 'LPG_Monthly'!BN3
    value = 35688
    isdatetime = True

@register(LPG_Monthly)
class BO3():
    # 'LPG_Monthly'!BO3
    value = 35718
    isdatetime = True

@register(LPG_Monthly)
class BP3():
    # 'LPG_Monthly'!BP3
    value = 35749
    isdatetime = True

@register(LPG_Monthly)
class BQ3():
    # 'LPG_Monthly'!BQ3
    value = 35779
    isdatetime = True

@register(LPG_Monthly)
class BR3():
    # 'LPG_Monthly'!BR3
    value = 35810
    isdatetime = True

@register(LPG_Monthly)
class BS3():
    # 'LPG_Monthly'!BS3
    value = 35841
    isdatetime = True

@register(LPG_Monthly)
class BT3():
    # 'LPG_Monthly'!BT3
    value = 35869
    isdatetime = True

@register(LPG_Monthly)
class BU3():
    # 'LPG_Monthly'!BU3
    value = 35900
    isdatetime = True

@register(LPG_Monthly)
class BV3():
    # 'LPG_Monthly'!BV3
    value = 35930
    isdatetime = True

@register(LPG_Monthly)
class BW3():
    # 'LPG_Monthly'!BW3
    value = 35961
    isdatetime = True

@register(LPG_Monthly)
class BX3():
    # 'LPG_Monthly'!BX3
    value = 35991
    isdatetime = True

@register(LPG_Monthly)
class BY3():
    # 'LPG_Monthly'!BY3
    value = 36022
    isdatetime = True

@register(LPG_Monthly)
class BZ3():
    # 'LPG_Monthly'!BZ3
    value = 36053
    isdatetime = True

@register(LPG_Monthly)
class CA3():
    # 'LPG_Monthly'!CA3
    value = 36083
    isdatetime = True

@register(LPG_Monthly)
class CB3():
    # 'LPG_Monthly'!CB3
    value = 36114
    isdatetime = True

@register(LPG_Monthly)
class CC3():
    # 'LPG_Monthly'!CC3
    value = 36144
    isdatetime = True

@register(LPG_Monthly)
class CD3():
    # 'LPG_Monthly'!CD3
    value = 36175
    isdatetime = True

@register(LPG_Monthly)
class CE3():
    # 'LPG_Monthly'!CE3
    value = 36206
    isdatetime = True

@register(LPG_Monthly)
class CF3():
    # 'LPG_Monthly'!CF3
    value = 36234
    isdatetime = True

@register(LPG_Monthly)
class CG3():
    # 'LPG_Monthly'!CG3
    value = 36265
    isdatetime = True

@register(LPG_Monthly)
class CH3():
    # 'LPG_Monthly'!CH3
    value = 36295
    isdatetime = True

@register(LPG_Monthly)
class CI3():
    # 'LPG_Monthly'!CI3
    value = 36326
    isdatetime = True

@register(LPG_Monthly)
class CJ3():
    # 'LPG_Monthly'!CJ3
    value = 36356
    isdatetime = True

@register(LPG_Monthly)
class CK3():
    # 'LPG_Monthly'!CK3
    value = 36387
    isdatetime = True

@register(LPG_Monthly)
class CL3():
    # 'LPG_Monthly'!CL3
    value = 36418
    isdatetime = True

@register(LPG_Monthly)
class CM3():
    # 'LPG_Monthly'!CM3
    value = 36448
    isdatetime = True

@register(LPG_Monthly)
class CN3():
    # 'LPG_Monthly'!CN3
    value = 36479
    isdatetime = True

@register(LPG_Monthly)
class CO3():
    # 'LPG_Monthly'!CO3
    value = 36509
    isdatetime = True

@register(LPG_Monthly)
class CP3():
    # 'LPG_Monthly'!CP3
    value = 36540
    isdatetime = True

@register(LPG_Monthly)
class CQ3():
    # 'LPG_Monthly'!CQ3
    value = 36571
    isdatetime = True

@register(LPG_Monthly)
class CR3():
    # 'LPG_Monthly'!CR3
    value = 36600
    isdatetime = True

@register(LPG_Monthly)
class CS3():
    # 'LPG_Monthly'!CS3
    value = 36631
    isdatetime = True

@register(LPG_Monthly)
class CT3():
    # 'LPG_Monthly'!CT3
    value = 36661
    isdatetime = True

@register(LPG_Monthly)
class CU3():
    # 'LPG_Monthly'!CU3
    value = 36692
    isdatetime = True

@register(LPG_Monthly)
class CV3():
    # 'LPG_Monthly'!CV3
    value = 36722
    isdatetime = True

@register(LPG_Monthly)
class CW3():
    # 'LPG_Monthly'!CW3
    value = 36753
    isdatetime = True

@register(LPG_Monthly)
class CX3():
    # 'LPG_Monthly'!CX3
    value = 36784
    isdatetime = True

@register(LPG_Monthly)
class CY3():
    # 'LPG_Monthly'!CY3
    value = 36814
    isdatetime = True

@register(LPG_Monthly)
class CZ3():
    # 'LPG_Monthly'!CZ3
    value = 36845
    isdatetime = True

@register(LPG_Monthly)
class DA3():
    # 'LPG_Monthly'!DA3
    value = 36875
    isdatetime = True

@register(LPG_Monthly)
class DB3():
    # 'LPG_Monthly'!DB3
    value = 36906
    isdatetime = True

@register(LPG_Monthly)
class DC3():
    # 'LPG_Monthly'!DC3
    value = 36937
    isdatetime = True

@register(LPG_Monthly)
class DD3():
    # 'LPG_Monthly'!DD3
    value = 36965
    isdatetime = True

@register(LPG_Monthly)
class DE3():
    # 'LPG_Monthly'!DE3
    value = 36996
    isdatetime = True

@register(LPG_Monthly)
class DF3():
    # 'LPG_Monthly'!DF3
    value = 37026
    isdatetime = True

@register(LPG_Monthly)
class DG3():
    # 'LPG_Monthly'!DG3
    value = 37057
    isdatetime = True

@register(LPG_Monthly)
class DH3():
    # 'LPG_Monthly'!DH3
    value = 37087
    isdatetime = True

@register(LPG_Monthly)
class DI3():
    # 'LPG_Monthly'!DI3
    value = 37118
    isdatetime = True

@register(LPG_Monthly)
class DJ3():
    # 'LPG_Monthly'!DJ3
    value = 37149
    isdatetime = True

@register(LPG_Monthly)
class DK3():
    # 'LPG_Monthly'!DK3
    value = 37179
    isdatetime = True

@register(LPG_Monthly)
class DL3():
    # 'LPG_Monthly'!DL3
    value = 37210
    isdatetime = True

@register(LPG_Monthly)
class DM3():
    # 'LPG_Monthly'!DM3
    value = 37240
    isdatetime = True

@register(LPG_Monthly)
class DN3():
    # 'LPG_Monthly'!DN3
    value = 37271
    isdatetime = True

@register(LPG_Monthly)
class DO3():
    # 'LPG_Monthly'!DO3
    value = 37302
    isdatetime = True

@register(LPG_Monthly)
class DP3():
    # 'LPG_Monthly'!DP3
    value = 37330
    isdatetime = True

@register(LPG_Monthly)
class DQ3():
    # 'LPG_Monthly'!DQ3
    value = 37361
    isdatetime = True

@register(LPG_Monthly)
class DR3():
    # 'LPG_Monthly'!DR3
    value = 37391
    isdatetime = True

@register(LPG_Monthly)
class DS3():
    # 'LPG_Monthly'!DS3
    value = 37422
    isdatetime = True

@register(LPG_Monthly)
class DT3():
    # 'LPG_Monthly'!DT3
    value = 37452
    isdatetime = True

@register(LPG_Monthly)
class DU3():
    # 'LPG_Monthly'!DU3
    value = 37483
    isdatetime = True

@register(LPG_Monthly)
class DV3():
    # 'LPG_Monthly'!DV3
    value = 37514
    isdatetime = True

@register(LPG_Monthly)
class DW3():
    # 'LPG_Monthly'!DW3
    value = 37544
    isdatetime = True

@register(LPG_Monthly)
class DX3():
    # 'LPG_Monthly'!DX3
    value = 37575
    isdatetime = True

@register(LPG_Monthly)
class DY3():
    # 'LPG_Monthly'!DY3
    value = 37605
    isdatetime = True

@register(LPG_Monthly)
class DZ3():
    # 'LPG_Monthly'!DZ3
    value = 37636
    isdatetime = True

@register(LPG_Monthly)
class EA3():
    # 'LPG_Monthly'!EA3
    value = 37667
    isdatetime = True

@register(LPG_Monthly)
class EB3():
    # 'LPG_Monthly'!EB3
    value = 37695
    isdatetime = True

@register(LPG_Monthly)
class EC3():
    # 'LPG_Monthly'!EC3
    value = 37726
    isdatetime = True

@register(LPG_Monthly)
class ED3():
    # 'LPG_Monthly'!ED3
    value = 37756
    isdatetime = True

@register(LPG_Monthly)
class EE3():
    # 'LPG_Monthly'!EE3
    value = 37787
    isdatetime = True

@register(LPG_Monthly)
class EF3():
    # 'LPG_Monthly'!EF3
    value = 37817
    isdatetime = True

@register(LPG_Monthly)
class EG3():
    # 'LPG_Monthly'!EG3
    value = 37848
    isdatetime = True

@register(LPG_Monthly)
class EH3():
    # 'LPG_Monthly'!EH3
    value = 37879
    isdatetime = True

@register(LPG_Monthly)
class EI3():
    # 'LPG_Monthly'!EI3
    value = 37909
    isdatetime = True

@register(LPG_Monthly)
class EJ3():
    # 'LPG_Monthly'!EJ3
    value = 37940
    isdatetime = True

@register(LPG_Monthly)
class EK3():
    # 'LPG_Monthly'!EK3
    value = 37970
    isdatetime = True

@register(LPG_Monthly)
class EL3():
    # 'LPG_Monthly'!EL3
    value = 38001
    isdatetime = True

@register(LPG_Monthly)
class EM3():
    # 'LPG_Monthly'!EM3
    value = 38032
    isdatetime = True

@register(LPG_Monthly)
class EN3():
    # 'LPG_Monthly'!EN3
    value = 38061
    isdatetime = True

@register(LPG_Monthly)
class EO3():
    # 'LPG_Monthly'!EO3
    value = 38092
    isdatetime = True

@register(LPG_Monthly)
class EP3():
    # 'LPG_Monthly'!EP3
    value = 38122
    isdatetime = True

@register(LPG_Monthly)
class EQ3():
    # 'LPG_Monthly'!EQ3
    value = 38153
    isdatetime = True

@register(LPG_Monthly)
class ER3():
    # 'LPG_Monthly'!ER3
    value = 38183
    isdatetime = True

@register(LPG_Monthly)
class ES3():
    # 'LPG_Monthly'!ES3
    value = 38214
    isdatetime = True

@register(LPG_Monthly)
class ET3():
    # 'LPG_Monthly'!ET3
    value = 38245
    isdatetime = True

@register(LPG_Monthly)
class EU3():
    # 'LPG_Monthly'!EU3
    value = 38275
    isdatetime = True

@register(LPG_Monthly)
class EV3():
    # 'LPG_Monthly'!EV3
    value = 38306
    isdatetime = True

@register(LPG_Monthly)
class EW3():
    # 'LPG_Monthly'!EW3
    value = 38336
    isdatetime = True

@register(LPG_Monthly)
class EX3():
    # 'LPG_Monthly'!EX3
    value = 38367
    isdatetime = True

@register(LPG_Monthly)
class EY3():
    # 'LPG_Monthly'!EY3
    value = 38398
    isdatetime = True

@register(LPG_Monthly)
class EZ3():
    # 'LPG_Monthly'!EZ3
    value = 38426
    isdatetime = True

@register(LPG_Monthly)
class FA3():
    # 'LPG_Monthly'!FA3
    value = 38457
    isdatetime = True

@register(LPG_Monthly)
class FB3():
    # 'LPG_Monthly'!FB3
    value = 38487
    isdatetime = True

@register(LPG_Monthly)
class FC3():
    # 'LPG_Monthly'!FC3
    value = 38518
    isdatetime = True

@register(LPG_Monthly)
class FD3():
    # 'LPG_Monthly'!FD3
    value = 38548
    isdatetime = True

@register(LPG_Monthly)
class FE3():
    # 'LPG_Monthly'!FE3
    value = 38579
    isdatetime = True

@register(LPG_Monthly)
class FF3():
    # 'LPG_Monthly'!FF3
    value = 38610
    isdatetime = True

@register(LPG_Monthly)
class FG3():
    # 'LPG_Monthly'!FG3
    value = 38640
    isdatetime = True

@register(LPG_Monthly)
class FH3():
    # 'LPG_Monthly'!FH3
    value = 38671
    isdatetime = True

@register(LPG_Monthly)
class FI3():
    # 'LPG_Monthly'!FI3
    value = 38701
    isdatetime = True

@register(LPG_Monthly)
class FJ3():
    # 'LPG_Monthly'!FJ3
    value = 38732
    isdatetime = True

@register(LPG_Monthly)
class FK3():
    # 'LPG_Monthly'!FK3
    value = 38763
    isdatetime = True

@register(LPG_Monthly)
class FL3():
    # 'LPG_Monthly'!FL3
    value = 38791
    isdatetime = True

@register(LPG_Monthly)
class FM3():
    # 'LPG_Monthly'!FM3
    value = 38822
    isdatetime = True

@register(LPG_Monthly)
class FN3():
    # 'LPG_Monthly'!FN3
    value = 38852
    isdatetime = True

@register(LPG_Monthly)
class FO3():
    # 'LPG_Monthly'!FO3
    value = 38883
    isdatetime = True

@register(LPG_Monthly)
class FP3():
    # 'LPG_Monthly'!FP3
    value = 38913
    isdatetime = True

@register(LPG_Monthly)
class FQ3():
    # 'LPG_Monthly'!FQ3
    value = 38944
    isdatetime = True

@register(LPG_Monthly)
class FR3():
    # 'LPG_Monthly'!FR3
    value = 38975
    isdatetime = True

@register(LPG_Monthly)
class FS3():
    # 'LPG_Monthly'!FS3
    value = 39005
    isdatetime = True

@register(LPG_Monthly)
class FT3():
    # 'LPG_Monthly'!FT3
    value = 39036
    isdatetime = True

@register(LPG_Monthly)
class FU3():
    # 'LPG_Monthly'!FU3
    value = 39066
    isdatetime = True

@register(LPG_Monthly)
class FV3():
    # 'LPG_Monthly'!FV3
    value = 39097
    isdatetime = True

@register(LPG_Monthly)
class FW3():
    # 'LPG_Monthly'!FW3
    value = 39128
    isdatetime = True

@register(LPG_Monthly)
class FX3():
    # 'LPG_Monthly'!FX3
    value = 39156
    isdatetime = True

@register(LPG_Monthly)
class FY3():
    # 'LPG_Monthly'!FY3
    value = 39187
    isdatetime = True

@register(LPG_Monthly)
class FZ3():
    # 'LPG_Monthly'!FZ3
    value = 39217
    isdatetime = True

@register(LPG_Monthly)
class GA3():
    # 'LPG_Monthly'!GA3
    value = 39248
    isdatetime = True

@register(LPG_Monthly)
class GB3():
    # 'LPG_Monthly'!GB3
    value = 39278
    isdatetime = True

@register(LPG_Monthly)
class GC3():
    # 'LPG_Monthly'!GC3
    value = 39309
    isdatetime = True

@register(LPG_Monthly)
class GD3():
    # 'LPG_Monthly'!GD3
    value = 39340
    isdatetime = True

@register(LPG_Monthly)
class GE3():
    # 'LPG_Monthly'!GE3
    value = 39370
    isdatetime = True

@register(LPG_Monthly)
class GF3():
    # 'LPG_Monthly'!GF3
    value = 39401
    isdatetime = True

@register(LPG_Monthly)
class GG3():
    # 'LPG_Monthly'!GG3
    value = 39431
    isdatetime = True

@register(LPG_Monthly)
class GH3():
    # 'LPG_Monthly'!GH3
    value = 39462
    isdatetime = True

@register(LPG_Monthly)
class GI3():
    # 'LPG_Monthly'!GI3
    value = 39493
    isdatetime = True

@register(LPG_Monthly)
class GJ3():
    # 'LPG_Monthly'!GJ3
    value = 39522
    isdatetime = True

@register(LPG_Monthly)
class GK3():
    # 'LPG_Monthly'!GK3
    value = 39553
    isdatetime = True

@register(LPG_Monthly)
class GL3():
    # 'LPG_Monthly'!GL3
    value = 39583
    isdatetime = True

@register(LPG_Monthly)
class GM3():
    # 'LPG_Monthly'!GM3
    value = 39614
    isdatetime = True

@register(LPG_Monthly)
class GN3():
    # 'LPG_Monthly'!GN3
    value = 39644
    isdatetime = True

@register(LPG_Monthly)
class GO3():
    # 'LPG_Monthly'!GO3
    value = 39675
    isdatetime = True

@register(LPG_Monthly)
class GP3():
    # 'LPG_Monthly'!GP3
    value = 39706
    isdatetime = True

@register(LPG_Monthly)
class GQ3():
    # 'LPG_Monthly'!GQ3
    value = 39736
    isdatetime = True

@register(LPG_Monthly)
class GR3():
    # 'LPG_Monthly'!GR3
    value = 39767
    isdatetime = True

@register(LPG_Monthly)
class GS3():
    # 'LPG_Monthly'!GS3
    value = 39797
    isdatetime = True

@register(LPG_Monthly)
class GT3():
    # 'LPG_Monthly'!GT3
    value = 39828
    isdatetime = True

@register(LPG_Monthly)
class GU3():
    # 'LPG_Monthly'!GU3
    value = 39859
    isdatetime = True

@register(LPG_Monthly)
class GV3():
    # 'LPG_Monthly'!GV3
    value = 39887
    isdatetime = True

@register(LPG_Monthly)
class GW3():
    # 'LPG_Monthly'!GW3
    value = 39918
    isdatetime = True

@register(LPG_Monthly)
class GX3():
    # 'LPG_Monthly'!GX3
    value = 39948
    isdatetime = True

@register(LPG_Monthly)
class GY3():
    # 'LPG_Monthly'!GY3
    value = 39979
    isdatetime = True

@register(LPG_Monthly)
class GZ3():
    # 'LPG_Monthly'!GZ3
    value = 40009
    isdatetime = True

@register(LPG_Monthly)
class HA3():
    # 'LPG_Monthly'!HA3
    value = 40040
    isdatetime = True

@register(LPG_Monthly)
class HB3():
    # 'LPG_Monthly'!HB3
    value = 40071
    isdatetime = True

@register(LPG_Monthly)
class HC3():
    # 'LPG_Monthly'!HC3
    value = 40101
    isdatetime = True

@register(LPG_Monthly)
class HD3():
    # 'LPG_Monthly'!HD3
    value = 40132
    isdatetime = True

@register(LPG_Monthly)
class HE3():
    # 'LPG_Monthly'!HE3
    value = 40162
    isdatetime = True

@register(LPG_Monthly)
class HF3():
    # 'LPG_Monthly'!HF3
    value = 40193
    isdatetime = True

@register(LPG_Monthly)
class HG3():
    # 'LPG_Monthly'!HG3
    value = 40224
    isdatetime = True

@register(LPG_Monthly)
class HH3():
    # 'LPG_Monthly'!HH3
    value = 40252
    isdatetime = True

@register(LPG_Monthly)
class HI3():
    # 'LPG_Monthly'!HI3
    value = 40283
    isdatetime = True

@register(LPG_Monthly)
class HJ3():
    # 'LPG_Monthly'!HJ3
    value = 40313
    isdatetime = True

@register(LPG_Monthly)
class HK3():
    # 'LPG_Monthly'!HK3
    value = 40344
    isdatetime = True

@register(LPG_Monthly)
class HL3():
    # 'LPG_Monthly'!HL3
    value = 40374
    isdatetime = True

@register(LPG_Monthly)
class HM3():
    # 'LPG_Monthly'!HM3
    value = 40405
    isdatetime = True

@register(LPG_Monthly)
class HN3():
    # 'LPG_Monthly'!HN3
    value = 40436
    isdatetime = True

@register(LPG_Monthly)
class HO3():
    # 'LPG_Monthly'!HO3
    value = 40466
    isdatetime = True

@register(LPG_Monthly)
class HP3():
    # 'LPG_Monthly'!HP3
    value = 40497
    isdatetime = True

@register(LPG_Monthly)
class HQ3():
    # 'LPG_Monthly'!HQ3
    value = 40527
    isdatetime = True

@register(LPG_Monthly)
class HR3():
    # 'LPG_Monthly'!HR3
    value = 40558
    isdatetime = True

@register(LPG_Monthly)
class HS3():
    # 'LPG_Monthly'!HS3
    value = 40589
    isdatetime = True

@register(LPG_Monthly)
class HT3():
    # 'LPG_Monthly'!HT3
    value = 40617
    isdatetime = True

@register(LPG_Monthly)
class HU3():
    # 'LPG_Monthly'!HU3
    value = 40648
    isdatetime = True

@register(LPG_Monthly)
class HV3():
    # 'LPG_Monthly'!HV3
    value = 40678
    isdatetime = True

@register(LPG_Monthly)
class HW3():
    # 'LPG_Monthly'!HW3
    value = 40709
    isdatetime = True

@register(LPG_Monthly)
class HX3():
    # 'LPG_Monthly'!HX3
    value = 40739
    isdatetime = True

@register(LPG_Monthly)
class HY3():
    # 'LPG_Monthly'!HY3
    value = 40770
    isdatetime = True

@register(LPG_Monthly)
class HZ3():
    # 'LPG_Monthly'!HZ3
    value = 40801
    isdatetime = True

@register(LPG_Monthly)
class IA3():
    # 'LPG_Monthly'!IA3
    value = 40831
    isdatetime = True

@register(LPG_Monthly)
class IB3():
    # 'LPG_Monthly'!IB3
    value = 40862
    isdatetime = True

@register(LPG_Monthly)
class IC3():
    # 'LPG_Monthly'!IC3
    value = 40892
    isdatetime = True

@register(LPG_Monthly)
class ID3():
    # 'LPG_Monthly'!ID3
    value = 40923
    isdatetime = True

@register(LPG_Monthly)
class IE3():
    # 'LPG_Monthly'!IE3
    value = 40954
    isdatetime = True

@register(LPG_Monthly)
class IF3():
    # 'LPG_Monthly'!IF3
    value = 40983
    isdatetime = True

@register(LPG_Monthly)
class IG3():
    # 'LPG_Monthly'!IG3
    value = 41014
    isdatetime = True

@register(LPG_Monthly)
class IH3():
    # 'LPG_Monthly'!IH3
    value = 41044
    isdatetime = True

@register(LPG_Monthly)
class II3():
    # 'LPG_Monthly'!II3
    value = 41075
    isdatetime = True

@register(LPG_Monthly)
class IJ3():
    # 'LPG_Monthly'!IJ3
    value = 41105
    isdatetime = True

@register(LPG_Monthly)
class IK3():
    # 'LPG_Monthly'!IK3
    value = 41136
    isdatetime = True

@register(LPG_Monthly)
class IL3():
    # 'LPG_Monthly'!IL3
    value = 41167
    isdatetime = True

@register(LPG_Monthly)
class IM3():
    # 'LPG_Monthly'!IM3
    value = 41197
    isdatetime = True

@register(LPG_Monthly)
class IN3():
    # 'LPG_Monthly'!IN3
    value = 41228
    isdatetime = True

@register(LPG_Monthly)
class IO3():
    # 'LPG_Monthly'!IO3
    value = 41258
    isdatetime = True

@register(LPG_Monthly)
class IP3():
    # 'LPG_Monthly'!IP3
    value = 41289
    isdatetime = True

@register(LPG_Monthly)
class IQ3():
    # 'LPG_Monthly'!IQ3
    value = 41320
    isdatetime = True

@register(LPG_Monthly)
class IR3():
    # 'LPG_Monthly'!IR3
    value = 41348
    isdatetime = True

@register(LPG_Monthly)
class IS3():
    # 'LPG_Monthly'!IS3
    value = 41379
    isdatetime = True

@register(LPG_Monthly)
class IT3():
    # 'LPG_Monthly'!IT3
    value = 41409
    isdatetime = True

@register(LPG_Monthly)
class IU3():
    # 'LPG_Monthly'!IU3
    value = 41440
    isdatetime = True

@register(LPG_Monthly)
class IV3():
    # 'LPG_Monthly'!IV3
    value = 41470
    isdatetime = True

@register(LPG_Monthly)
class IW3():
    # 'LPG_Monthly'!IW3
    value = 41501
    isdatetime = True

@register(LPG_Monthly)
class IX3():
    # 'LPG_Monthly'!IX3
    value = 41532
    isdatetime = True

@register(LPG_Monthly)
class IY3():
    # 'LPG_Monthly'!IY3
    value = 41562
    isdatetime = True

@register(LPG_Monthly)
class IZ3():
    # 'LPG_Monthly'!IZ3
    value = 41593
    isdatetime = True

@register(LPG_Monthly)
class JA3():
    # 'LPG_Monthly'!JA3
    value = 41623
    isdatetime = True

@register(LPG_Monthly)
class JB3():
    # 'LPG_Monthly'!JB3
    value = 41654
    isdatetime = True

@register(LPG_Monthly)
class JC3():
    # 'LPG_Monthly'!JC3
    value = 41685
    isdatetime = True

@register(LPG_Monthly)
class JD3():
    # 'LPG_Monthly'!JD3
    value = 41713
    isdatetime = True

@register(LPG_Monthly)
class JE3():
    # 'LPG_Monthly'!JE3
    value = 41744
    isdatetime = True

@register(LPG_Monthly)
class JF3():
    # 'LPG_Monthly'!JF3
    value = 41774
    isdatetime = True

@register(LPG_Monthly)
class JG3():
    # 'LPG_Monthly'!JG3
    value = 41805
    isdatetime = True

@register(LPG_Monthly)
class JH3():
    # 'LPG_Monthly'!JH3
    value = 41835
    isdatetime = True

@register(LPG_Monthly)
class JI3():
    # 'LPG_Monthly'!JI3
    value = 41866
    isdatetime = True

@register(LPG_Monthly)
class JJ3():
    # 'LPG_Monthly'!JJ3
    value = 41897
    isdatetime = True

@register(LPG_Monthly)
class JK3():
    # 'LPG_Monthly'!JK3
    value = 41927
    isdatetime = True

@register(LPG_Monthly)
class JL3():
    # 'LPG_Monthly'!JL3
    value = 41958
    isdatetime = True

@register(LPG_Monthly)
class JM3():
    # 'LPG_Monthly'!JM3
    value = 41988
    isdatetime = True

@register(LPG_Monthly)
class JN3():
    # 'LPG_Monthly'!JN3
    value = 42019
    isdatetime = True

@register(LPG_Monthly)
class JO3():
    # 'LPG_Monthly'!JO3
    value = 42050
    isdatetime = True

@register(LPG_Monthly)
class JP3():
    # 'LPG_Monthly'!JP3
    value = 42078
    isdatetime = True

@register(LPG_Monthly)
class JQ3():
    # 'LPG_Monthly'!JQ3
    value = 42109
    isdatetime = True

@register(LPG_Monthly)
class JR3():
    # 'LPG_Monthly'!JR3
    value = 42139
    isdatetime = True

@register(LPG_Monthly)
class JS3():
    # 'LPG_Monthly'!JS3
    value = 42170
    isdatetime = True

@register(LPG_Monthly)
class JT3():
    # 'LPG_Monthly'!JT3
    value = 42200
    isdatetime = True

@register(LPG_Monthly)
class JU3():
    # 'LPG_Monthly'!JU3
    value = 42231
    isdatetime = True

@register(LPG_Monthly)
class JV3():
    # 'LPG_Monthly'!JV3
    value = 42262
    isdatetime = True

@register(LPG_Monthly)
class JW3():
    # 'LPG_Monthly'!JW3
    value = 42292
    isdatetime = True

@register(LPG_Monthly)
class JX3():
    # 'LPG_Monthly'!JX3
    value = 42323
    isdatetime = True

@register(LPG_Monthly)
class JY3():
    # 'LPG_Monthly'!JY3
    value = 42353
    isdatetime = True

@register(LPG_Monthly)
class JZ3():
    # 'LPG_Monthly'!JZ3
    value = 42384
    isdatetime = True

@register(LPG_Monthly)
class KA3():
    # 'LPG_Monthly'!KA3
    value = 42415
    isdatetime = True

@register(LPG_Monthly)
class KB3():
    # 'LPG_Monthly'!KB3
    value = 42444
    isdatetime = True

@register(LPG_Monthly)
class KC3():
    # 'LPG_Monthly'!KC3
    value = 42475
    isdatetime = True

@register(LPG_Monthly)
class KD3():
    # 'LPG_Monthly'!KD3
    value = 42505
    isdatetime = True

@register(LPG_Monthly)
class KE3():
    # 'LPG_Monthly'!KE3
    value = 42536
    isdatetime = True

@register(LPG_Monthly)
class KF3():
    # 'LPG_Monthly'!KF3
    value = 42566
    isdatetime = True

@register(LPG_Monthly)
class KG3():
    # 'LPG_Monthly'!KG3
    value = 42597
    isdatetime = True

@register(LPG_Monthly)
class KH3():
    # 'LPG_Monthly'!KH3
    value = 42628
    isdatetime = True

@register(LPG_Monthly)
class KI3():
    # 'LPG_Monthly'!KI3
    value = 42658
    isdatetime = True

@register(LPG_Monthly)
class KJ3():
    # 'LPG_Monthly'!KJ3
    value = 42689
    isdatetime = True

@register(LPG_Monthly)
class KK3():
    # 'LPG_Monthly'!KK3
    value = 42719
    isdatetime = True

@register(LPG_Monthly)
class KL3():
    # 'LPG_Monthly'!KL3
    value = 42750
    isdatetime = True

@register(LPG_Monthly)
class KM3():
    # 'LPG_Monthly'!KM3
    value = 42781
    isdatetime = True

@register(LPG_Monthly)
class KN3():
    # 'LPG_Monthly'!KN3
    value = 42809
    isdatetime = True

@register(LPG_Monthly)
class KO3():
    # 'LPG_Monthly'!KO3
    value = 42840
    isdatetime = True

@register(LPG_Monthly)
class KP3():
    # 'LPG_Monthly'!KP3
    value = 42870
    isdatetime = True

@register(LPG_Monthly)
class KQ3():
    # 'LPG_Monthly'!KQ3
    value = 42901
    isdatetime = True

@register(LPG_Monthly)
class KR3():
    # 'LPG_Monthly'!KR3
    value = 42931
    isdatetime = True

@register(LPG_Monthly)
class KS3():
    # 'LPG_Monthly'!KS3
    value = 42962
    isdatetime = True

@register(LPG_Monthly)
class KT3():
    # 'LPG_Monthly'!KT3
    value = 42993
    isdatetime = True

@register(LPG_Monthly)
class KU3():
    # 'LPG_Monthly'!KU3
    value = 43023
    isdatetime = True

@register(LPG_Monthly)
class KV3():
    # 'LPG_Monthly'!KV3
    value = 43054
    isdatetime = True

@register(LPG_Monthly)
class KW3():
    # 'LPG_Monthly'!KW3
    value = 43084
    isdatetime = True

@register(LPG_Monthly)
class KX3():
    # 'LPG_Monthly'!KX3
    value = 43115
    isdatetime = True

@register(LPG_Monthly)
class KY3():
    # 'LPG_Monthly'!KY3
    value = 43146
    isdatetime = True

@register(LPG_Monthly)
class KZ3():
    # 'LPG_Monthly'!KZ3
    value = 43174
    isdatetime = True

@register(LPG_Monthly)
class LA3():
    # 'LPG_Monthly'!LA3
    value = 43205
    isdatetime = True

@register(LPG_Monthly)
class LB3():
    # 'LPG_Monthly'!LB3
    value = 43235
    isdatetime = True

@register(LPG_Monthly)
class LC3():
    # 'LPG_Monthly'!LC3
    value = 43266
    isdatetime = True

@register(LPG_Monthly)
class LD3():
    # 'LPG_Monthly'!LD3
    value = 43296
    isdatetime = True

@register(LPG_Monthly)
class LE3():
    # 'LPG_Monthly'!LE3
    value = 43327
    isdatetime = True

@register(LPG_Monthly)
class LF3():
    # 'LPG_Monthly'!LF3
    value = 43358
    isdatetime = True

@register(LPG_Monthly)
class LG3():
    # 'LPG_Monthly'!LG3
    value = 43388
    isdatetime = True

@register(LPG_Monthly)
class LH3():
    # 'LPG_Monthly'!LH3
    value = 43419
    isdatetime = True

@register(LPG_Monthly)
class LI3():
    # 'LPG_Monthly'!LI3
    value = 43449
    isdatetime = True

@register(LPG_Monthly)
class LJ3():
    # 'LPG_Monthly'!LJ3
    value = 43480
    isdatetime = True

@register(LPG_Monthly)
class LK3():
    # 'LPG_Monthly'!LK3
    value = 43511
    isdatetime = True

@register(LPG_Monthly)
class LL3():
    # 'LPG_Monthly'!LL3
    value = 43539
    isdatetime = True

@register(LPG_Monthly)
class LM3():
    # 'LPG_Monthly'!LM3
    value = 43570
    isdatetime = True

@register(LPG_Monthly)
class LN3():
    # 'LPG_Monthly'!LN3
    value = 43600
    isdatetime = True

@register(LPG_Monthly)
class LO3():
    # 'LPG_Monthly'!LO3
    value = 43631
    isdatetime = True

@register(LPG_Monthly)
class LP3():
    # 'LPG_Monthly'!LP3
    value = 43661
    isdatetime = True

@register(LPG_Monthly)
class LQ3():
    # 'LPG_Monthly'!LQ3
    value = 43692
    isdatetime = True

@register(LPG_Monthly)
class LR3():
    # 'LPG_Monthly'!LR3
    value = 43723
    isdatetime = True

@register(LPG_Monthly)
class LS3():
    # 'LPG_Monthly'!LS3
    value = 43753
    isdatetime = True

@register(LPG_Monthly)
class LT3():
    # 'LPG_Monthly'!LT3
    value = 43784
    isdatetime = True

@register(LPG_Monthly)
class LU3():
    # 'LPG_Monthly'!LU3
    value = 43814
    isdatetime = True

@register(LPG_Monthly)
class LV3():
    # 'LPG_Monthly'!LV3
    value = 43845
    isdatetime = True

@register(LPG_Monthly)
class LW3():
    # 'LPG_Monthly'!LW3
    value = 43876
    isdatetime = True

@register(LPG_Monthly)
class LX3():
    # 'LPG_Monthly'!LX3
    value = 43905
    isdatetime = True

@register(LPG_Monthly)
class LY3():
    # 'LPG_Monthly'!LY3
    value = 43936
    isdatetime = True

@register(LPG_Monthly)
class LZ3():
    # 'LPG_Monthly'!LZ3
    value = 43966
    isdatetime = True

@register(LPG_Monthly)
class MA3():
    # 'LPG_Monthly'!MA3
    value = 43997
    isdatetime = True

@register(LPG_Monthly)
class MB3():
    # 'LPG_Monthly'!MB3
    value = 44027
    isdatetime = True

@register(LPG_Monthly)
class MC3():
    # 'LPG_Monthly'!MC3
    value = 44058
    isdatetime = True

@register(LPG_Monthly)
class MD3():
    # 'LPG_Monthly'!MD3
    value = 44089
    isdatetime = True

@register(LPG_Monthly)
class ME3():
    # 'LPG_Monthly'!ME3
    value = 44119
    isdatetime = True

@register(LPG_Monthly)
class MF3():
    # 'LPG_Monthly'!MF3
    value = 44150
    isdatetime = True

@register(LPG_Monthly)
class MG3():
    # 'LPG_Monthly'!MG3
    value = 44180
    isdatetime = True

@register(LPG_Monthly)
class MH3():
    # 'LPG_Monthly'!MH3
    value = 44211
    isdatetime = True

@register(LPG_Monthly)
class MI3():
    # 'LPG_Monthly'!MI3
    value = 44242
    isdatetime = True

@register(LPG_Monthly)
class MJ3():
    # 'LPG_Monthly'!MJ3
    value = 44270
    isdatetime = True

@register(LPG_Monthly)
class MK3():
    # 'LPG_Monthly'!MK3
    value = 44301
    isdatetime = True

@register(LPG_Monthly)
class ML3():
    # 'LPG_Monthly'!ML3
    value = 44331
    isdatetime = True

@register(LPG_Monthly)
class MM3():
    # 'LPG_Monthly'!MM3
    value = 44362
    isdatetime = True

@register(LPG_Monthly)
class MN3():
    # 'LPG_Monthly'!MN3
    value = 44392
    isdatetime = True

@register(LPG_Monthly)
class MO3():
    # 'LPG_Monthly'!MO3
    value = 44423
    isdatetime = True

@register(LPG_Monthly)
class MP3():
    # 'LPG_Monthly'!MP3
    value = 44454
    isdatetime = True

@register(LPG_Monthly)
class MQ3():
    # 'LPG_Monthly'!MQ3
    value = 44484
    isdatetime = True

@register(LPG_Monthly)
class MR3():
    # 'LPG_Monthly'!MR3
    value = 44515
    isdatetime = True

@register(LPG_Monthly)
class MS3():
    # 'LPG_Monthly'!MS3
    value = 44545
    isdatetime = True

@register(LPG_Monthly)
class MT3():
    # 'LPG_Monthly'!MT3
    value = 44576
    isdatetime = True

@register(LPG_Monthly)
class MU3():
    # 'LPG_Monthly'!MU3
    value = 44607
    isdatetime = True

@register(LPG_Monthly)
class MV3():
    # 'LPG_Monthly'!MV3
    value = 44635
    isdatetime = True

@register(LPG_Monthly)
class MW3():
    # 'LPG_Monthly'!MW3
    value = 44666
    isdatetime = True

@register(LPG_Monthly)
class MX3():
    # 'LPG_Monthly'!MX3
    value = 44696
    isdatetime = True

@register(LPG_Monthly)
class MY3():
    # 'LPG_Monthly'!MY3
    value = 44727
    isdatetime = True

@register(LPG_Monthly)
class MZ3():
    # 'LPG_Monthly'!MZ3
    value = 44757
    isdatetime = True

@register(LPG_Monthly)
class NA3():
    # 'LPG_Monthly'!NA3
    value = 44788
    isdatetime = True

@register(LPG_Monthly)
class NB3():
    # 'LPG_Monthly'!NB3
    value = 44819
    isdatetime = True

@register(LPG_Monthly)
class NC3():
    # 'LPG_Monthly'!NC3
    value = 44849
    isdatetime = True

@register(LPG_Monthly)
class ND3():
    # 'LPG_Monthly'!ND3
    value = 44880
    isdatetime = True

@register(LPG_Monthly)
class NE3():
    # 'LPG_Monthly'!NE3
    value = 44910
    isdatetime = True

@register(LPG_Monthly)
class NF3():
    # 'LPG_Monthly'!NF3
    value = 44941
    isdatetime = True

@register(LPG_Monthly)
class NG3():
    # 'LPG_Monthly'!NG3
    value = 44972
    isdatetime = True

@register(LPG_Monthly)
class NH3():
    # 'LPG_Monthly'!NH3
    value = 45000
    isdatetime = True

@register(LPG_Monthly)
class NI3():
    # 'LPG_Monthly'!NI3
    value = 45031
    isdatetime = True

@register(LPG_Monthly)
class NJ3():
    # 'LPG_Monthly'!NJ3
    value = 45061
    isdatetime = True

@register(LPG_Monthly)
class NK3():
    # 'LPG_Monthly'!NK3
    value = 45092
    isdatetime = True

@register(LPG_Monthly)
class NL3():
    # 'LPG_Monthly'!NL3
    value = 45122
    isdatetime = True

@register(LPG_Monthly)
class NM3():
    # 'LPG_Monthly'!NM3
    value = 45153
    isdatetime = True

@register(LPG_Monthly)
class NN3():
    # 'LPG_Monthly'!NN3
    value = 45184
    isdatetime = True

@register(LPG_Monthly)
class NO3():
    # 'LPG_Monthly'!NO3
    value = 45214
    isdatetime = True

@register(LPG_Monthly)
class NP3():
    # 'LPG_Monthly'!NP3
    value = 45245
    isdatetime = True

@register(LPG_Monthly)
class NQ3():
    # 'LPG_Monthly'!NQ3
    value = 45275
    isdatetime = True

@register(LPG_Monthly)
class NR3():
    # 'LPG_Monthly'!NR3
    value = 45306
    isdatetime = True

@register(LPG_Monthly)
class NS3():
    # 'LPG_Monthly'!NS3
    value = 45337
    isdatetime = True

@register(LPG_Monthly)
class NT3():
    # 'LPG_Monthly'!NT3
    value = 45366
    isdatetime = True

@register(LPG_Monthly)
class NU3():
    # 'LPG_Monthly'!NU3
    value = 45397
    isdatetime = True

@register(LPG_Monthly)
class NV3():
    # 'LPG_Monthly'!NV3
    value = 45427
    isdatetime = True

@register(LPG_Monthly)
class NW3():
    # 'LPG_Monthly'!NW3
    value = 45458
    isdatetime = True

@register(LPG_Monthly)
class NX3():
    # 'LPG_Monthly'!NX3
    value = 45488
    isdatetime = True

@register(LPG_Monthly)
class NY3():
    # 'LPG_Monthly'!NY3
    value = 45519
    isdatetime = True

@register(LPG_Monthly)
class NZ3():
    # 'LPG_Monthly'!NZ3
    value = 45550
    isdatetime = True

@register(LPG_Monthly)
class OA3():
    # 'LPG_Monthly'!OA3
    value = 45580
    isdatetime = True

@register(LPG_Monthly)
class OB3():
    # 'LPG_Monthly'!OB3
    value = 45611
    isdatetime = True

@register(LPG_Monthly)
class OC3():
    # 'LPG_Monthly'!OC3
    value = 45641
    isdatetime = True

@register(LPG_Monthly)
class OD3():
    # 'LPG_Monthly'!OD3
    value = 45672
    isdatetime = True

@register(LPG_Monthly)
class OE3():
    # 'LPG_Monthly'!OE3
    value = 45703
    isdatetime = True

@register(LPG_Monthly)
class OF3():
    # 'LPG_Monthly'!OF3
    value = 45731
    isdatetime = True

@register(LPG_Monthly)
class OG3():
    # 'LPG_Monthly'!OG3
    value = 45762
    isdatetime = True

@register(LPG_Monthly)
class OH3():
    # 'LPG_Monthly'!OH3
    value = 45792
    isdatetime = True

@register(LPG_Monthly)
class OI3():
    # 'LPG_Monthly'!OI3
    value = 45823
    isdatetime = True

@register(LPG_Monthly)
class OJ3():
    # 'LPG_Monthly'!OJ3
    value = 45853
    isdatetime = True

@register(LPG_Monthly)
class OK3():
    # 'LPG_Monthly'!OK3
    value = 45884
    isdatetime = True

@register(LPG_Monthly)
class OL3():
    # 'LPG_Monthly'!OL3
    value = 45915
    isdatetime = True

@register(LPG_Monthly)
class OM3():
    # 'LPG_Monthly'!OM3
    value = 45945
    isdatetime = True

@register(LPG_Monthly)
class ON3():
    # 'LPG_Monthly'!ON3
    value = 45976
    isdatetime = True

@register(LPG_Monthly)
class OO3():
    # 'LPG_Monthly'!OO3
    value = 46006
    isdatetime = True

@register(LPG_Monthly)
class OP3():
    # 'LPG_Monthly'!OP3
    value = 46037
    isdatetime = True

@register(LPG_Monthly)
class OQ3():
    # 'LPG_Monthly'!OQ3
    value = 46068
    isdatetime = True

@register(LPG_Monthly)
class OR3():
    # 'LPG_Monthly'!OR3
    value = 46096
    isdatetime = True

@register(LPG_Monthly)
class OS3():
    # 'LPG_Monthly'!OS3
    value = 46127
    isdatetime = True

@register(LPG_Monthly)
class OT3():
    # 'LPG_Monthly'!OT3
    value = 46157
    isdatetime = True

@register(LPG_Monthly)
class OU3():
    # 'LPG_Monthly'!OU3
    value = 46188
    isdatetime = True

@register(LPG_Monthly)
class OV3():
    # 'LPG_Monthly'!OV3
    value = 46218
    isdatetime = True

@register(LPG_Monthly)
class OW3():
    # 'LPG_Monthly'!OW3
    value = 46249
    isdatetime = True

@register(LPG_Monthly)
class OX3():
    # 'LPG_Monthly'!OX3
    value = 46280
    isdatetime = True

@register(LPG_Monthly)
class OY3():
    # 'LPG_Monthly'!OY3
    value = 46310
    isdatetime = True

@register(LPG_Monthly)
class OZ3():
    # 'LPG_Monthly'!OZ3
    value = 46341
    isdatetime = True

@register(LPG_Monthly)
class PA3():
    # 'LPG_Monthly'!PA3
    value = 46371
    isdatetime = True

@register(LPG_Monthly)
class PB3():
    # 'LPG_Monthly'!PB3
    value = 46402
    isdatetime = True

@register(LPG_Monthly)
class PC3():
    # 'LPG_Monthly'!PC3
    value = 46433
    isdatetime = True

@register(LPG_Monthly)
class PD3():
    # 'LPG_Monthly'!PD3
    value = 46461
    isdatetime = True

@register(LPG_Monthly)
class PE3():
    # 'LPG_Monthly'!PE3
    value = 46492
    isdatetime = True

@register(LPG_Monthly)
class PF3():
    # 'LPG_Monthly'!PF3
    value = 46522
    isdatetime = True

@register(LPG_Monthly)
class PG3():
    # 'LPG_Monthly'!PG3
    value = 46553
    isdatetime = True

@register(LPG_Monthly)
class PH3():
    # 'LPG_Monthly'!PH3
    value = 46583
    isdatetime = True

@register(LPG_Monthly)
class PI3():
    # 'LPG_Monthly'!PI3
    value = 46614
    isdatetime = True

@register(LPG_Monthly)
class PJ3():
    # 'LPG_Monthly'!PJ3
    value = 46645
    isdatetime = True

@register(LPG_Monthly)
class PK3():
    # 'LPG_Monthly'!PK3
    value = 46675
    isdatetime = True

@register(LPG_Monthly)
class PL3():
    # 'LPG_Monthly'!PL3
    value = 46706
    isdatetime = True

@register(LPG_Monthly)
class PM3():
    # 'LPG_Monthly'!PM3
    value = 46736
    isdatetime = True

@register(LPG_Monthly)
class PN3():
    # 'LPG_Monthly'!PN3
    value = 46767
    isdatetime = True

@register(LPG_Monthly)
class PO3():
    # 'LPG_Monthly'!PO3
    value = 46798
    isdatetime = True

@register(LPG_Monthly)
class PP3():
    # 'LPG_Monthly'!PP3
    value = 46827
    isdatetime = True

@register(LPG_Monthly)
class PQ3():
    # 'LPG_Monthly'!PQ3
    value = 46858
    isdatetime = True

@register(LPG_Monthly)
class PR3():
    # 'LPG_Monthly'!PR3
    value = 46888
    isdatetime = True

@register(LPG_Monthly)
class PS3():
    # 'LPG_Monthly'!PS3
    value = 46919
    isdatetime = True

@register(LPG_Monthly)
class PT3():
    # 'LPG_Monthly'!PT3
    value = 46949
    isdatetime = True

@register(LPG_Monthly)
class PU3():
    # 'LPG_Monthly'!PU3
    value = 46980
    isdatetime = True

@register(LPG_Monthly)
class PV3():
    # 'LPG_Monthly'!PV3
    value = 47011
    isdatetime = True

@register(LPG_Monthly)
class PW3():
    # 'LPG_Monthly'!PW3
    value = 47041
    isdatetime = True

@register(LPG_Monthly)
class PX3():
    # 'LPG_Monthly'!PX3
    value = 47072
    isdatetime = True

@register(LPG_Monthly)
class PY3():
    # 'LPG_Monthly'!PY3
    value = 47102
    isdatetime = True

@register(LPG_Monthly)
class PZ3():
    # 'LPG_Monthly'!PZ3
    value = 47133
    isdatetime = True

@register(LPG_Monthly)
class QA3():
    # 'LPG_Monthly'!QA3
    value = 47164
    isdatetime = True

@register(LPG_Monthly)
class QB3():
    # 'LPG_Monthly'!QB3
    value = 47192
    isdatetime = True

@register(LPG_Monthly)
class QC3():
    # 'LPG_Monthly'!QC3
    value = 47223
    isdatetime = True

@register(LPG_Monthly)
class QD3():
    # 'LPG_Monthly'!QD3
    value = 47253
    isdatetime = True

@register(LPG_Monthly)
class QE3():
    # 'LPG_Monthly'!QE3
    value = 47284
    isdatetime = True

@register(LPG_Monthly)
class QF3():
    # 'LPG_Monthly'!QF3
    value = 47314
    isdatetime = True

@register(LPG_Monthly)
class QG3():
    # 'LPG_Monthly'!QG3
    value = 47345
    isdatetime = True

@register(LPG_Monthly)
class QH3():
    # 'LPG_Monthly'!QH3
    value = 47376
    isdatetime = True

@register(LPG_Monthly)
class QI3():
    # 'LPG_Monthly'!QI3
    value = 47406
    isdatetime = True

@register(LPG_Monthly)
class QJ3():
    # 'LPG_Monthly'!QJ3
    value = 47437
    isdatetime = True

@register(LPG_Monthly)
class QK3():
    # 'LPG_Monthly'!QK3
    value = 47467
    isdatetime = True

@register(LPG_Monthly)
class QL3():
    # 'LPG_Monthly'!QL3
    value = 47498
    isdatetime = True

@register(LPG_Monthly)
class QM3():
    # 'LPG_Monthly'!QM3
    value = 47529
    isdatetime = True

@register(LPG_Monthly)
class QN3():
    # 'LPG_Monthly'!QN3
    value = 47557
    isdatetime = True

@register(LPG_Monthly)
class QO3():
    # 'LPG_Monthly'!QO3
    value = 47588
    isdatetime = True

@register(LPG_Monthly)
class QP3():
    # 'LPG_Monthly'!QP3
    value = 47618
    isdatetime = True

@register(LPG_Monthly)
class QQ3():
    # 'LPG_Monthly'!QQ3
    value = 47649
    isdatetime = True

@register(LPG_Monthly)
class QR3():
    # 'LPG_Monthly'!QR3
    value = 47679
    isdatetime = True

@register(LPG_Monthly)
class QS3():
    # 'LPG_Monthly'!QS3
    value = 47710
    isdatetime = True

@register(LPG_Monthly)
class QT3():
    # 'LPG_Monthly'!QT3
    value = 47741
    isdatetime = True

@register(LPG_Monthly)
class QU3():
    # 'LPG_Monthly'!QU3
    value = 47771
    isdatetime = True

@register(LPG_Monthly)
class QV3():
    # 'LPG_Monthly'!QV3
    value = 47802
    isdatetime = True

@register(LPG_Monthly)
class QW3():
    # 'LPG_Monthly'!QW3
    value = 47832
    isdatetime = True

@register(LPG_Monthly)
class A4():
    # 'LPG_Monthly'!A4
    value = "Mont Belvieu, TX Propane Spot Price FOB (Dollars per Gallon)"
    formula = "='Input EIA Propane Price'!B2"
    @eval_fn
    def A4():
        b2_1 = Input_EIA_Propane_Price.B2()
        return b2_1

@register(LPG_Monthly)
class B4():
    # 'LPG_Monthly'!B4
    value = "Dollars per Gallon"

@register(LPG_Monthly)
class C4():
    # 'LPG_Monthly'!C4
    value = 0.344
    formula = "=VLOOKUP(C$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def C4():
        c3_1 = LPG_Monthly.C3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(c3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class D4():
    # 'LPG_Monthly'!D4
    value = 0.342
    formula = "=VLOOKUP(D$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def D4():
        d3_1 = LPG_Monthly.D3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(d3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class E4():
    # 'LPG_Monthly'!E4
    value = 0.354
    formula = "=VLOOKUP(E$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def E4():
        e3_1 = LPG_Monthly.E3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(e3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class F4():
    # 'LPG_Monthly'!F4
    value = 0.375
    formula = "=VLOOKUP(F$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def F4():
        f3_1 = LPG_Monthly.F3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(f3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class G4():
    # 'LPG_Monthly'!G4
    value = 0.354
    formula = "=VLOOKUP(G$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def G4():
        g3_1 = LPG_Monthly.G3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(g3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class H4():
    # 'LPG_Monthly'!H4
    value = 0.327
    formula = "=VLOOKUP(H$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def H4():
        h3_1 = LPG_Monthly.H3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(h3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class I4():
    # 'LPG_Monthly'!I4
    value = 0.312
    formula = "=VLOOKUP(I$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def I4():
        i3_1 = LPG_Monthly.I3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(i3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class J4():
    # 'LPG_Monthly'!J4
    value = 0.337
    formula = "=VLOOKUP(J$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def J4():
        j3_1 = LPG_Monthly.J3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(j3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class K4():
    # 'LPG_Monthly'!K4
    value = 0.33
    formula = "=VLOOKUP(K$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def K4():
        k3_1 = LPG_Monthly.K3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(k3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class L4():
    # 'LPG_Monthly'!L4
    value = 0.342
    formula = "=VLOOKUP(L$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def L4():
        l3_1 = LPG_Monthly.L3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(l3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class M4():
    # 'LPG_Monthly'!M4
    value = 0.344
    formula = "=VLOOKUP(M$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def M4():
        m3_1 = LPG_Monthly.M3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(m3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class N4():
    # 'LPG_Monthly'!N4
    value = 0.328
    formula = "=VLOOKUP(N$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def N4():
        n3_1 = LPG_Monthly.N3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(n3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class O4():
    # 'LPG_Monthly'!O4
    value = 0.328
    formula = "=VLOOKUP(O$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def O4():
        o3_1 = LPG_Monthly.O3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(o3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class P4():
    # 'LPG_Monthly'!P4
    value = 0.314
    formula = "=VLOOKUP(P$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def P4():
        p3_1 = LPG_Monthly.P3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(p3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class Q4():
    # 'LPG_Monthly'!Q4
    value = 0.305
    formula = "=VLOOKUP(Q$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def Q4():
        q3_1 = LPG_Monthly.Q3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(q3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class R4():
    # 'LPG_Monthly'!R4
    value = 0.299
    formula = "=VLOOKUP(R$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def R4():
        r3_1 = LPG_Monthly.R3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(r3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class S4():
    # 'LPG_Monthly'!S4
    value = 0.293
    formula = "=VLOOKUP(S$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def S4():
        s3_1 = LPG_Monthly.S3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(s3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class T4():
    # 'LPG_Monthly'!T4
    value = 0.275
    formula = "=VLOOKUP(T$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def T4():
        t3_1 = LPG_Monthly.T3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(t3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class U4():
    # 'LPG_Monthly'!U4
    value = 0.245
    formula = "=VLOOKUP(U$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def U4():
        u3_1 = LPG_Monthly.U3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(u3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class V4():
    # 'LPG_Monthly'!V4
    value = 0.263
    formula = "=VLOOKUP(V$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def V4():
        v3_1 = LPG_Monthly.V3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(v3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class W4():
    # 'LPG_Monthly'!W4
    value = 0.29
    formula = "=VLOOKUP(W$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def W4():
        w3_1 = LPG_Monthly.W3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(w3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class X4():
    # 'LPG_Monthly'!X4
    value = 0.284
    formula = "=VLOOKUP(X$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def X4():
        x3_1 = LPG_Monthly.X3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(x3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class Y4():
    # 'LPG_Monthly'!Y4
    value = 0.289
    formula = "=VLOOKUP(Y$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def Y4():
        y3_1 = LPG_Monthly.Y3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(y3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class Z4():
    # 'LPG_Monthly'!Z4
    value = 0.296
    formula = "=VLOOKUP(Z$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def Z4():
        z3_1 = LPG_Monthly.Z3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(z3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AA4():
    # 'LPG_Monthly'!AA4
    value = 0.288
    formula = "=VLOOKUP(AA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AA4():
        aa3_1 = LPG_Monthly.AA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(aa3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AB4():
    # 'LPG_Monthly'!AB4
    value = 0.292
    formula = "=VLOOKUP(AB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AB4():
        ab3_1 = LPG_Monthly.AB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ab3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AC4():
    # 'LPG_Monthly'!AC4
    value = 0.3
    formula = "=VLOOKUP(AC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AC4():
        ac3_1 = LPG_Monthly.AC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ac3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AD4():
    # 'LPG_Monthly'!AD4
    value = 0.299
    formula = "=VLOOKUP(AD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AD4():
        ad3_1 = LPG_Monthly.AD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ad3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AE4():
    # 'LPG_Monthly'!AE4
    value = 0.324
    formula = "=VLOOKUP(AE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AE4():
        ae3_1 = LPG_Monthly.AE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ae3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AF4():
    # 'LPG_Monthly'!AF4
    value = 0.344
    formula = "=VLOOKUP(AF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AF4():
        af3_1 = LPG_Monthly.AF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(af3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AG4():
    # 'LPG_Monthly'!AG4
    value = 0.333
    formula = "=VLOOKUP(AG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AG4():
        ag3_1 = LPG_Monthly.AG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ag3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AH4():
    # 'LPG_Monthly'!AH4
    value = 0.327
    formula = "=VLOOKUP(AH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AH4():
        ah3_1 = LPG_Monthly.AH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ah3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AI4():
    # 'LPG_Monthly'!AI4
    value = 0.316
    formula = "=VLOOKUP(AI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AI4():
        ai3_1 = LPG_Monthly.AI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ai3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AJ4():
    # 'LPG_Monthly'!AJ4
    value = 0.327
    formula = "=VLOOKUP(AJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AJ4():
        aj3_1 = LPG_Monthly.AJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(aj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AK4():
    # 'LPG_Monthly'!AK4
    value = 0.323
    formula = "=VLOOKUP(AK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AK4():
        ak3_1 = LPG_Monthly.AK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ak3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AL4():
    # 'LPG_Monthly'!AL4
    value = 0.327
    formula = "=VLOOKUP(AL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AL4():
        al3_1 = LPG_Monthly.AL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(al3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AM4():
    # 'LPG_Monthly'!AM4
    value = 0.318
    formula = "=VLOOKUP(AM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AM4():
        am3_1 = LPG_Monthly.AM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(am3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AN4():
    # 'LPG_Monthly'!AN4
    value = 0.308
    formula = "=VLOOKUP(AN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AN4():
        an3_1 = LPG_Monthly.AN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(an3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AO4():
    # 'LPG_Monthly'!AO4
    value = 0.313
    formula = "=VLOOKUP(AO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AO4():
        ao3_1 = LPG_Monthly.AO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ao3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AP4():
    # 'LPG_Monthly'!AP4
    value = 0.313
    formula = "=VLOOKUP(AP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AP4():
        ap3_1 = LPG_Monthly.AP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ap3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AQ4():
    # 'LPG_Monthly'!AQ4
    value = 0.309
    formula = "=VLOOKUP(AQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AQ4():
        aq3_1 = LPG_Monthly.AQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(aq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AR4():
    # 'LPG_Monthly'!AR4
    value = 0.31
    formula = "=VLOOKUP(AR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AR4():
        ar3_1 = LPG_Monthly.AR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ar3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AS4():
    # 'LPG_Monthly'!AS4
    value = 0.354
    formula = "=VLOOKUP(AS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AS4():
        as3_1 = LPG_Monthly.AS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(as3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AT4():
    # 'LPG_Monthly'!AT4
    value = 0.354
    formula = "=VLOOKUP(AT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AT4():
        at3_1 = LPG_Monthly.AT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(at3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AU4():
    # 'LPG_Monthly'!AU4
    value = 0.39
    formula = "=VLOOKUP(AU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AU4():
        au3_1 = LPG_Monthly.AU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(au3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AV4():
    # 'LPG_Monthly'!AV4
    value = 0.369
    formula = "=VLOOKUP(AV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AV4():
        av3_1 = LPG_Monthly.AV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(av3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AW4():
    # 'LPG_Monthly'!AW4
    value = 0.356
    formula = "=VLOOKUP(AW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AW4():
        aw3_1 = LPG_Monthly.AW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(aw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AX4():
    # 'LPG_Monthly'!AX4
    value = 0.348
    formula = "=VLOOKUP(AX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AX4():
        ax3_1 = LPG_Monthly.AX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ax3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AY4():
    # 'LPG_Monthly'!AY4
    value = 0.348
    formula = "=VLOOKUP(AY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AY4():
        ay3_1 = LPG_Monthly.AY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ay3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class AZ4():
    # 'LPG_Monthly'!AZ4
    value = 0.356
    formula = "=VLOOKUP(AZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def AZ4():
        az3_1 = LPG_Monthly.AZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(az3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BA4():
    # 'LPG_Monthly'!BA4
    value = 0.384
    formula = "=VLOOKUP(BA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BA4():
        ba3_1 = LPG_Monthly.BA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ba3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BB4():
    # 'LPG_Monthly'!BB4
    value = 0.47
    formula = "=VLOOKUP(BB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BB4():
        bb3_1 = LPG_Monthly.BB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BC4():
    # 'LPG_Monthly'!BC4
    value = 0.513
    formula = "=VLOOKUP(BC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BC4():
        bc3_1 = LPG_Monthly.BC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BD4():
    # 'LPG_Monthly'!BD4
    value = 0.583
    formula = "=VLOOKUP(BD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BD4():
        bd3_1 = LPG_Monthly.BD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BE4():
    # 'LPG_Monthly'!BE4
    value = 0.608
    formula = "=VLOOKUP(BE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BE4():
        be3_1 = LPG_Monthly.BE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(be3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BF4():
    # 'LPG_Monthly'!BF4
    value = 0.474
    formula = "=VLOOKUP(BF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BF4():
        bf3_1 = LPG_Monthly.BF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BG4():
    # 'LPG_Monthly'!BG4
    value = 0.386
    formula = "=VLOOKUP(BG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BG4():
        bg3_1 = LPG_Monthly.BG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BH4():
    # 'LPG_Monthly'!BH4
    value = 0.385
    formula = "=VLOOKUP(BH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BH4():
        bh3_1 = LPG_Monthly.BH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BI4():
    # 'LPG_Monthly'!BI4
    value = 0.349
    formula = "=VLOOKUP(BI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BI4():
        bi3_1 = LPG_Monthly.BI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BJ4():
    # 'LPG_Monthly'!BJ4
    value = 0.353
    formula = "=VLOOKUP(BJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BJ4():
        bj3_1 = LPG_Monthly.BJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BK4():
    # 'LPG_Monthly'!BK4
    value = 0.344
    formula = "=VLOOKUP(BK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BK4():
        bk3_1 = LPG_Monthly.BK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BL4():
    # 'LPG_Monthly'!BL4
    value = 0.348
    formula = "=VLOOKUP(BL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BL4():
        bl3_1 = LPG_Monthly.BL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BM4():
    # 'LPG_Monthly'!BM4
    value = 0.369
    formula = "=VLOOKUP(BM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BM4():
        bm3_1 = LPG_Monthly.BM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BN4():
    # 'LPG_Monthly'!BN4
    value = 0.387
    formula = "=VLOOKUP(BN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BN4():
        bn3_1 = LPG_Monthly.BN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BO4():
    # 'LPG_Monthly'!BO4
    value = 0.398
    formula = "=VLOOKUP(BO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BO4():
        bo3_1 = LPG_Monthly.BO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BP4():
    # 'LPG_Monthly'!BP4
    value = 0.36
    formula = "=VLOOKUP(BP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BP4():
        bp3_1 = LPG_Monthly.BP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BQ4():
    # 'LPG_Monthly'!BQ4
    value = 0.336
    formula = "=VLOOKUP(BQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BQ4():
        bq3_1 = LPG_Monthly.BQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BR4():
    # 'LPG_Monthly'!BR4
    value = 0.302
    formula = "=VLOOKUP(BR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BR4():
        br3_1 = LPG_Monthly.BR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(br3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BS4():
    # 'LPG_Monthly'!BS4
    value = 0.298
    formula = "=VLOOKUP(BS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BS4():
        bs3_1 = LPG_Monthly.BS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BT4():
    # 'LPG_Monthly'!BT4
    value = 0.275
    formula = "=VLOOKUP(BT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BT4():
        bt3_1 = LPG_Monthly.BT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BU4():
    # 'LPG_Monthly'!BU4
    value = 0.291
    formula = "=VLOOKUP(BU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BU4():
        bu3_1 = LPG_Monthly.BU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BV4():
    # 'LPG_Monthly'!BV4
    value = 0.274
    formula = "=VLOOKUP(BV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BV4():
        bv3_1 = LPG_Monthly.BV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BW4():
    # 'LPG_Monthly'!BW4
    value = 0.245
    formula = "=VLOOKUP(BW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BW4():
        bw3_1 = LPG_Monthly.BW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BX4():
    # 'LPG_Monthly'!BX4
    value = 0.246
    formula = "=VLOOKUP(BX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BX4():
        bx3_1 = LPG_Monthly.BX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BY4():
    # 'LPG_Monthly'!BY4
    value = 0.241
    formula = "=VLOOKUP(BY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BY4():
        by3_1 = LPG_Monthly.BY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(by3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class BZ4():
    # 'LPG_Monthly'!BZ4
    value = 0.249
    formula = "=VLOOKUP(BZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def BZ4():
        bz3_1 = LPG_Monthly.BZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(bz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CA4():
    # 'LPG_Monthly'!CA4
    value = 0.257
    formula = "=VLOOKUP(CA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CA4():
        ca3_1 = LPG_Monthly.CA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ca3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CB4():
    # 'LPG_Monthly'!CB4
    value = 0.248
    formula = "=VLOOKUP(CB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CB4():
        cb3_1 = LPG_Monthly.CB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CC4():
    # 'LPG_Monthly'!CC4
    value = 0.209
    formula = "=VLOOKUP(CC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CC4():
        cc3_1 = LPG_Monthly.CC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CD4():
    # 'LPG_Monthly'!CD4
    value = 0.217
    formula = "=VLOOKUP(CD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CD4():
        cd3_1 = LPG_Monthly.CD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CE4():
    # 'LPG_Monthly'!CE4
    value = 0.224
    formula = "=VLOOKUP(CE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CE4():
        ce3_1 = LPG_Monthly.CE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ce3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CF4():
    # 'LPG_Monthly'!CF4
    value = 0.242
    formula = "=VLOOKUP(CF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CF4():
        cf3_1 = LPG_Monthly.CF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CG4():
    # 'LPG_Monthly'!CG4
    value = 0.282
    formula = "=VLOOKUP(CG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CG4():
        cg3_1 = LPG_Monthly.CG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CH4():
    # 'LPG_Monthly'!CH4
    value = 0.283
    formula = "=VLOOKUP(CH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CH4():
        ch3_1 = LPG_Monthly.CH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ch3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CI4():
    # 'LPG_Monthly'!CI4
    value = 0.309
    formula = "=VLOOKUP(CI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CI4():
        ci3_1 = LPG_Monthly.CI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ci3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CJ4():
    # 'LPG_Monthly'!CJ4
    value = 0.372
    formula = "=VLOOKUP(CJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CJ4():
        cj3_1 = LPG_Monthly.CJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CK4():
    # 'LPG_Monthly'!CK4
    value = 0.406
    formula = "=VLOOKUP(CK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CK4():
        ck3_1 = LPG_Monthly.CK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ck3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CL4():
    # 'LPG_Monthly'!CL4
    value = 0.432
    formula = "=VLOOKUP(CL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CL4():
        cl3_1 = LPG_Monthly.CL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CM4():
    # 'LPG_Monthly'!CM4
    value = 0.454
    formula = "=VLOOKUP(CM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CM4():
        cm3_1 = LPG_Monthly.CM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CN4():
    # 'LPG_Monthly'!CN4
    value = 0.436
    formula = "=VLOOKUP(CN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CN4():
        cn3_1 = LPG_Monthly.CN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CO4():
    # 'LPG_Monthly'!CO4
    value = 0.428
    formula = "=VLOOKUP(CO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CO4():
        co3_1 = LPG_Monthly.CO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(co3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CP4():
    # 'LPG_Monthly'!CP4
    value = 0.555
    formula = "=VLOOKUP(CP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CP4():
        cp3_1 = LPG_Monthly.CP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CQ4():
    # 'LPG_Monthly'!CQ4
    value = 0.596
    formula = "=VLOOKUP(CQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CQ4():
        cq3_1 = LPG_Monthly.CQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CR4():
    # 'LPG_Monthly'!CR4
    value = 0.512
    formula = "=VLOOKUP(CR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CR4():
        cr3_1 = LPG_Monthly.CR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CS4():
    # 'LPG_Monthly'!CS4
    value = 0.469
    formula = "=VLOOKUP(CS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CS4():
        cs3_1 = LPG_Monthly.CS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CT4():
    # 'LPG_Monthly'!CT4
    value = 0.512
    formula = "=VLOOKUP(CT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CT4():
        ct3_1 = LPG_Monthly.CT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ct3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CU4():
    # 'LPG_Monthly'!CU4
    value = 0.555
    formula = "=VLOOKUP(CU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CU4():
        cu3_1 = LPG_Monthly.CU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CV4():
    # 'LPG_Monthly'!CV4
    value = 0.551
    formula = "=VLOOKUP(CV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CV4():
        cv3_1 = LPG_Monthly.CV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CW4():
    # 'LPG_Monthly'!CW4
    value = 0.583
    formula = "=VLOOKUP(CW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CW4():
        cw3_1 = LPG_Monthly.CW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CX4():
    # 'LPG_Monthly'!CX4
    value = 0.643
    formula = "=VLOOKUP(CX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CX4():
        cx3_1 = LPG_Monthly.CX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CY4():
    # 'LPG_Monthly'!CY4
    value = 0.62
    formula = "=VLOOKUP(CY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CY4():
        cy3_1 = LPG_Monthly.CY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class CZ4():
    # 'LPG_Monthly'!CZ4
    value = 0.608
    formula = "=VLOOKUP(CZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def CZ4():
        cz3_1 = LPG_Monthly.CZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(cz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DA4():
    # 'LPG_Monthly'!DA4
    value = 0.775
    formula = "=VLOOKUP(DA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DA4():
        da3_1 = LPG_Monthly.DA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(da3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DB4():
    # 'LPG_Monthly'!DB4
    value = 0.774
    formula = "=VLOOKUP(DB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DB4():
        db3_1 = LPG_Monthly.DB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(db3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DC4():
    # 'LPG_Monthly'!DC4
    value = 0.593
    formula = "=VLOOKUP(DC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DC4():
        dc3_1 = LPG_Monthly.DC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DD4():
    # 'LPG_Monthly'!DD4
    value = 0.558
    formula = "=VLOOKUP(DD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DD4():
        dd3_1 = LPG_Monthly.DD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DE4():
    # 'LPG_Monthly'!DE4
    value = 0.547
    formula = "=VLOOKUP(DE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DE4():
        de3_1 = LPG_Monthly.DE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(de3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DF4():
    # 'LPG_Monthly'!DF4
    value = 0.513
    formula = "=VLOOKUP(DF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DF4():
        df3_1 = LPG_Monthly.DF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(df3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DG4():
    # 'LPG_Monthly'!DG4
    value = 0.431
    formula = "=VLOOKUP(DG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DG4():
        dg3_1 = LPG_Monthly.DG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DH4():
    # 'LPG_Monthly'!DH4
    value = 0.39
    formula = "=VLOOKUP(DH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DH4():
        dh3_1 = LPG_Monthly.DH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DI4():
    # 'LPG_Monthly'!DI4
    value = 0.415
    formula = "=VLOOKUP(DI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DI4():
        di3_1 = LPG_Monthly.DI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(di3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DJ4():
    # 'LPG_Monthly'!DJ4
    value = 0.421
    formula = "=VLOOKUP(DJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DJ4():
        dj3_1 = LPG_Monthly.DJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DK4():
    # 'LPG_Monthly'!DK4
    value = 0.395
    formula = "=VLOOKUP(DK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DK4():
        dk3_1 = LPG_Monthly.DK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DL4():
    # 'LPG_Monthly'!DL4
    value = 0.331
    formula = "=VLOOKUP(DL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DL4():
        dl3_1 = LPG_Monthly.DL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DM4():
    # 'LPG_Monthly'!DM4
    value = 0.301
    formula = "=VLOOKUP(DM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DM4():
        dm3_1 = LPG_Monthly.DM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DN4():
    # 'LPG_Monthly'!DN4
    value = 0.291
    formula = "=VLOOKUP(DN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DN4():
        dn3_1 = LPG_Monthly.DN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DO4():
    # 'LPG_Monthly'!DO4
    value = 0.313
    formula = "=VLOOKUP(DO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DO4():
        do3_1 = LPG_Monthly.DO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(do3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DP4():
    # 'LPG_Monthly'!DP4
    value = 0.38
    formula = "=VLOOKUP(DP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DP4():
        dp3_1 = LPG_Monthly.DP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DQ4():
    # 'LPG_Monthly'!DQ4
    value = 0.415
    formula = "=VLOOKUP(DQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DQ4():
        dq3_1 = LPG_Monthly.DQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DR4():
    # 'LPG_Monthly'!DR4
    value = 0.406
    formula = "=VLOOKUP(DR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DR4():
        dr3_1 = LPG_Monthly.DR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DS4():
    # 'LPG_Monthly'!DS4
    value = 0.375
    formula = "=VLOOKUP(DS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DS4():
        ds3_1 = LPG_Monthly.DS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ds3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DT4():
    # 'LPG_Monthly'!DT4
    value = 0.372
    formula = "=VLOOKUP(DT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DT4():
        dt3_1 = LPG_Monthly.DT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DU4():
    # 'LPG_Monthly'!DU4
    value = 0.415
    formula = "=VLOOKUP(DU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DU4():
        du3_1 = LPG_Monthly.DU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(du3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DV4():
    # 'LPG_Monthly'!DV4
    value = 0.471
    formula = "=VLOOKUP(DV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DV4():
        dv3_1 = LPG_Monthly.DV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DW4():
    # 'LPG_Monthly'!DW4
    value = 0.479
    formula = "=VLOOKUP(DW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DW4():
        dw3_1 = LPG_Monthly.DW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DX4():
    # 'LPG_Monthly'!DX4
    value = 0.472
    formula = "=VLOOKUP(DX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DX4():
        dx3_1 = LPG_Monthly.DX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DY4():
    # 'LPG_Monthly'!DY4
    value = 0.523
    formula = "=VLOOKUP(DY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DY4():
        dy3_1 = LPG_Monthly.DY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class DZ4():
    # 'LPG_Monthly'!DZ4
    value = 0.606
    formula = "=VLOOKUP(DZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def DZ4():
        dz3_1 = LPG_Monthly.DZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(dz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EA4():
    # 'LPG_Monthly'!EA4
    value = 0.775
    formula = "=VLOOKUP(EA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EA4():
        ea3_1 = LPG_Monthly.EA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ea3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EB4():
    # 'LPG_Monthly'!EB4
    value = 0.623
    formula = "=VLOOKUP(EB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EB4():
        eb3_1 = LPG_Monthly.EB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EC4():
    # 'LPG_Monthly'!EC4
    value = 0.504
    formula = "=VLOOKUP(EC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EC4():
        ec3_1 = LPG_Monthly.EC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ec3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ED4():
    # 'LPG_Monthly'!ED4
    value = 0.541
    formula = "=VLOOKUP(ED$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ED4():
        ed3_1 = LPG_Monthly.ED3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ed3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EE4():
    # 'LPG_Monthly'!EE4
    value = 0.559
    formula = "=VLOOKUP(EE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EE4():
        ee3_1 = LPG_Monthly.EE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ee3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EF4():
    # 'LPG_Monthly'!EF4
    value = 0.53
    formula = "=VLOOKUP(EF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EF4():
        ef3_1 = LPG_Monthly.EF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ef3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EG4():
    # 'LPG_Monthly'!EG4
    value = 0.548
    formula = "=VLOOKUP(EG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EG4():
        eg3_1 = LPG_Monthly.EG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EH4():
    # 'LPG_Monthly'!EH4
    value = 0.519
    formula = "=VLOOKUP(EH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EH4():
        eh3_1 = LPG_Monthly.EH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EI4():
    # 'LPG_Monthly'!EI4
    value = 0.553
    formula = "=VLOOKUP(EI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EI4():
        ei3_1 = LPG_Monthly.EI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ei3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EJ4():
    # 'LPG_Monthly'!EJ4
    value = 0.547
    formula = "=VLOOKUP(EJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EJ4():
        ej3_1 = LPG_Monthly.EJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ej3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EK4():
    # 'LPG_Monthly'!EK4
    value = 0.628
    formula = "=VLOOKUP(EK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EK4():
        ek3_1 = LPG_Monthly.EK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ek3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EL4():
    # 'LPG_Monthly'!EL4
    value = 0.745
    formula = "=VLOOKUP(EL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EL4():
        el3_1 = LPG_Monthly.EL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(el3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EM4():
    # 'LPG_Monthly'!EM4
    value = 0.704
    formula = "=VLOOKUP(EM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EM4():
        em3_1 = LPG_Monthly.EM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(em3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EN4():
    # 'LPG_Monthly'!EN4
    value = 0.585
    formula = "=VLOOKUP(EN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EN4():
        en3_1 = LPG_Monthly.EN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(en3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EO4():
    # 'LPG_Monthly'!EO4
    value = 0.607
    formula = "=VLOOKUP(EO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EO4():
        eo3_1 = LPG_Monthly.EO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EP4():
    # 'LPG_Monthly'!EP4
    value = 0.677
    formula = "=VLOOKUP(EP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EP4():
        ep3_1 = LPG_Monthly.EP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ep3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EQ4():
    # 'LPG_Monthly'!EQ4
    value = 0.67
    formula = "=VLOOKUP(EQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EQ4():
        eq3_1 = LPG_Monthly.EQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ER4():
    # 'LPG_Monthly'!ER4
    value = 0.741
    formula = "=VLOOKUP(ER$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ER4():
        er3_1 = LPG_Monthly.ER3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(er3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ES4():
    # 'LPG_Monthly'!ES4
    value = 0.837
    formula = "=VLOOKUP(ES$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ES4():
        es3_1 = LPG_Monthly.ES3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(es3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ET4():
    # 'LPG_Monthly'!ET4
    value = 0.802
    formula = "=VLOOKUP(ET$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ET4():
        et3_1 = LPG_Monthly.ET3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(et3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EU4():
    # 'LPG_Monthly'!EU4
    value = 0.906
    formula = "=VLOOKUP(EU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EU4():
        eu3_1 = LPG_Monthly.EU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(eu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EV4():
    # 'LPG_Monthly'!EV4
    value = 0.863
    formula = "=VLOOKUP(EV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EV4():
        ev3_1 = LPG_Monthly.EV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ev3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EW4():
    # 'LPG_Monthly'!EW4
    value = 0.774
    formula = "=VLOOKUP(EW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EW4():
        ew3_1 = LPG_Monthly.EW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ew3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EX4():
    # 'LPG_Monthly'!EX4
    value = 0.737
    formula = "=VLOOKUP(EX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EX4():
        ex3_1 = LPG_Monthly.EX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ex3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EY4():
    # 'LPG_Monthly'!EY4
    value = 0.758
    formula = "=VLOOKUP(EY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EY4():
        ey3_1 = LPG_Monthly.EY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ey3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class EZ4():
    # 'LPG_Monthly'!EZ4
    value = 0.878
    formula = "=VLOOKUP(EZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def EZ4():
        ez3_1 = LPG_Monthly.EZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ez3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FA4():
    # 'LPG_Monthly'!FA4
    value = 0.854
    formula = "=VLOOKUP(FA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FA4():
        fa3_1 = LPG_Monthly.FA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fa3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FB4():
    # 'LPG_Monthly'!FB4
    value = 0.797
    formula = "=VLOOKUP(FB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FB4():
        fb3_1 = LPG_Monthly.FB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FC4():
    # 'LPG_Monthly'!FC4
    value = 0.818
    formula = "=VLOOKUP(FC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FC4():
        fc3_1 = LPG_Monthly.FC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FD4():
    # 'LPG_Monthly'!FD4
    value = 0.845
    formula = "=VLOOKUP(FD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FD4():
        fd3_1 = LPG_Monthly.FD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FE4():
    # 'LPG_Monthly'!FE4
    value = 0.941
    formula = "=VLOOKUP(FE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FE4():
        fe3_1 = LPG_Monthly.FE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fe3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FF4():
    # 'LPG_Monthly'!FF4
    value = 1.13
    formula = "=VLOOKUP(FF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FF4():
        ff3_1 = LPG_Monthly.FF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ff3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FG4():
    # 'LPG_Monthly'!FG4
    value = 1.137
    formula = "=VLOOKUP(FG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FG4():
        fg3_1 = LPG_Monthly.FG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FH4():
    # 'LPG_Monthly'!FH4
    value = 0.999
    formula = "=VLOOKUP(FH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FH4():
        fh3_1 = LPG_Monthly.FH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FI4():
    # 'LPG_Monthly'!FI4
    value = 1.056
    formula = "=VLOOKUP(FI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FI4():
        fi3_1 = LPG_Monthly.FI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FJ4():
    # 'LPG_Monthly'!FJ4
    value = 0.989
    formula = "=VLOOKUP(FJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FJ4():
        fj3_1 = LPG_Monthly.FJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FK4():
    # 'LPG_Monthly'!FK4
    value = 0.919
    formula = "=VLOOKUP(FK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FK4():
        fk3_1 = LPG_Monthly.FK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FL4():
    # 'LPG_Monthly'!FL4
    value = 0.926
    formula = "=VLOOKUP(FL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FL4():
        fl3_1 = LPG_Monthly.FL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FM4():
    # 'LPG_Monthly'!FM4
    value = 1.016
    formula = "=VLOOKUP(FM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FM4():
        fm3_1 = LPG_Monthly.FM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FN4():
    # 'LPG_Monthly'!FN4
    value = 1.041
    formula = "=VLOOKUP(FN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FN4():
        fn3_1 = LPG_Monthly.FN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FO4():
    # 'LPG_Monthly'!FO4
    value = 1.097
    formula = "=VLOOKUP(FO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FO4():
        fo3_1 = LPG_Monthly.FO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FP4():
    # 'LPG_Monthly'!FP4
    value = 1.165
    formula = "=VLOOKUP(FP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FP4():
        fp3_1 = LPG_Monthly.FP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FQ4():
    # 'LPG_Monthly'!FQ4
    value = 1.138
    formula = "=VLOOKUP(FQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FQ4():
        fq3_1 = LPG_Monthly.FQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FR4():
    # 'LPG_Monthly'!FR4
    value = 1.012
    formula = "=VLOOKUP(FR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FR4():
        fr3_1 = LPG_Monthly.FR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FS4():
    # 'LPG_Monthly'!FS4
    value = 0.938
    formula = "=VLOOKUP(FS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FS4():
        fs3_1 = LPG_Monthly.FS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FT4():
    # 'LPG_Monthly'!FT4
    value = 0.954
    formula = "=VLOOKUP(FT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FT4():
        ft3_1 = LPG_Monthly.FT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ft3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FU4():
    # 'LPG_Monthly'!FU4
    value = 0.966
    formula = "=VLOOKUP(FU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FU4():
        fu3_1 = LPG_Monthly.FU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FV4():
    # 'LPG_Monthly'!FV4
    value = 0.893
    formula = "=VLOOKUP(FV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FV4():
        fv3_1 = LPG_Monthly.FV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FW4():
    # 'LPG_Monthly'!FW4
    value = 0.975
    formula = "=VLOOKUP(FW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FW4():
        fw3_1 = LPG_Monthly.FW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FX4():
    # 'LPG_Monthly'!FX4
    value = 1.037
    formula = "=VLOOKUP(FX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FX4():
        fx3_1 = LPG_Monthly.FX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FY4():
    # 'LPG_Monthly'!FY4
    value = 1.108
    formula = "=VLOOKUP(FY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FY4():
        fy3_1 = LPG_Monthly.FY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class FZ4():
    # 'LPG_Monthly'!FZ4
    value = 1.149
    formula = "=VLOOKUP(FZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def FZ4():
        fz3_1 = LPG_Monthly.FZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(fz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GA4():
    # 'LPG_Monthly'!GA4
    value = 1.139
    formula = "=VLOOKUP(GA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GA4():
        ga3_1 = LPG_Monthly.GA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ga3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GB4():
    # 'LPG_Monthly'!GB4
    value = 1.19
    formula = "=VLOOKUP(GB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GB4():
        gb3_1 = LPG_Monthly.GB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GC4():
    # 'LPG_Monthly'!GC4
    value = 1.186
    formula = "=VLOOKUP(GC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GC4():
        gc3_1 = LPG_Monthly.GC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GD4():
    # 'LPG_Monthly'!GD4
    value = 1.295
    formula = "=VLOOKUP(GD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GD4():
        gd3_1 = LPG_Monthly.GD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GE4():
    # 'LPG_Monthly'!GE4
    value = 1.432
    formula = "=VLOOKUP(GE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GE4():
        ge3_1 = LPG_Monthly.GE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ge3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GF4():
    # 'LPG_Monthly'!GF4
    value = 1.556
    formula = "=VLOOKUP(GF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GF4():
        gf3_1 = LPG_Monthly.GF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GG4():
    # 'LPG_Monthly'!GG4
    value = 1.529
    formula = "=VLOOKUP(GG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GG4():
        gg3_1 = LPG_Monthly.GG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GH4():
    # 'LPG_Monthly'!GH4
    value = 1.506
    formula = "=VLOOKUP(GH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GH4():
        gh3_1 = LPG_Monthly.GH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GI4():
    # 'LPG_Monthly'!GI4
    value = 1.425
    formula = "=VLOOKUP(GI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GI4():
        gi3_1 = LPG_Monthly.GI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GJ4():
    # 'LPG_Monthly'!GJ4
    value = 1.475
    formula = "=VLOOKUP(GJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GJ4():
        gj3_1 = LPG_Monthly.GJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GK4():
    # 'LPG_Monthly'!GK4
    value = 1.59
    formula = "=VLOOKUP(GK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GK4():
        gk3_1 = LPG_Monthly.GK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GL4():
    # 'LPG_Monthly'!GL4
    value = 1.7
    formula = "=VLOOKUP(GL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GL4():
        gl3_1 = LPG_Monthly.GL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GM4():
    # 'LPG_Monthly'!GM4
    value = 1.813
    formula = "=VLOOKUP(GM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GM4():
        gm3_1 = LPG_Monthly.GM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GN4():
    # 'LPG_Monthly'!GN4
    value = 1.862
    formula = "=VLOOKUP(GN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GN4():
        gn3_1 = LPG_Monthly.GN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GO4():
    # 'LPG_Monthly'!GO4
    value = 1.651
    formula = "=VLOOKUP(GO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GO4():
        go3_1 = LPG_Monthly.GO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(go3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GP4():
    # 'LPG_Monthly'!GP4
    value = 1.53
    formula = "=VLOOKUP(GP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GP4():
        gp3_1 = LPG_Monthly.GP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GQ4():
    # 'LPG_Monthly'!GQ4
    value = 1.045
    formula = "=VLOOKUP(GQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GQ4():
        gq3_1 = LPG_Monthly.GQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GR4():
    # 'LPG_Monthly'!GR4
    value = 0.738
    formula = "=VLOOKUP(GR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GR4():
        gr3_1 = LPG_Monthly.GR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GS4():
    # 'LPG_Monthly'!GS4
    value = 0.61
    formula = "=VLOOKUP(GS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GS4():
        gs3_1 = LPG_Monthly.GS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GT4():
    # 'LPG_Monthly'!GT4
    value = 0.727
    formula = "=VLOOKUP(GT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GT4():
        gt3_1 = LPG_Monthly.GT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GU4():
    # 'LPG_Monthly'!GU4
    value = 0.659
    formula = "=VLOOKUP(GU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GU4():
        gu3_1 = LPG_Monthly.GU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GV4():
    # 'LPG_Monthly'!GV4
    value = 0.653
    formula = "=VLOOKUP(GV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GV4():
        gv3_1 = LPG_Monthly.GV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GW4():
    # 'LPG_Monthly'!GW4
    value = 0.638
    formula = "=VLOOKUP(GW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GW4():
        gw3_1 = LPG_Monthly.GW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GX4():
    # 'LPG_Monthly'!GX4
    value = 0.701
    formula = "=VLOOKUP(GX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GX4():
        gx3_1 = LPG_Monthly.GX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GY4():
    # 'LPG_Monthly'!GY4
    value = 0.846
    formula = "=VLOOKUP(GY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GY4():
        gy3_1 = LPG_Monthly.GY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class GZ4():
    # 'LPG_Monthly'!GZ4
    value = 0.752
    formula = "=VLOOKUP(GZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def GZ4():
        gz3_1 = LPG_Monthly.GZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(gz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HA4():
    # 'LPG_Monthly'!HA4
    value = 0.906
    formula = "=VLOOKUP(HA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HA4():
        ha3_1 = LPG_Monthly.HA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ha3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HB4():
    # 'LPG_Monthly'!HB4
    value = 0.946
    formula = "=VLOOKUP(HB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HB4():
        hb3_1 = LPG_Monthly.HB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HC4():
    # 'LPG_Monthly'!HC4
    value = 1.008
    formula = "=VLOOKUP(HC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HC4():
        hc3_1 = LPG_Monthly.HC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HD4():
    # 'LPG_Monthly'!HD4
    value = 1.076
    formula = "=VLOOKUP(HD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HD4():
        hd3_1 = LPG_Monthly.HD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HE4():
    # 'LPG_Monthly'!HE4
    value = 1.19
    formula = "=VLOOKUP(HE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HE4():
        he3_1 = LPG_Monthly.HE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(he3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HF4():
    # 'LPG_Monthly'!HF4
    value = 1.312
    formula = "=VLOOKUP(HF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HF4():
        hf3_1 = LPG_Monthly.HF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HG4():
    # 'LPG_Monthly'!HG4
    value = 1.284
    formula = "=VLOOKUP(HG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HG4():
        hg3_1 = LPG_Monthly.HG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HH4():
    # 'LPG_Monthly'!HH4
    value = 1.136
    formula = "=VLOOKUP(HH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HH4():
        hh3_1 = LPG_Monthly.HH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HI4():
    # 'LPG_Monthly'!HI4
    value = 1.137
    formula = "=VLOOKUP(HI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HI4():
        hi3_1 = LPG_Monthly.HI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HJ4():
    # 'LPG_Monthly'!HJ4
    value = 1.082
    formula = "=VLOOKUP(HJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HJ4():
        hj3_1 = LPG_Monthly.HJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HK4():
    # 'LPG_Monthly'!HK4
    value = 1.037
    formula = "=VLOOKUP(HK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HK4():
        hk3_1 = LPG_Monthly.HK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HL4():
    # 'LPG_Monthly'!HL4
    value = 1.01
    formula = "=VLOOKUP(HL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HL4():
        hl3_1 = LPG_Monthly.HL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HM4():
    # 'LPG_Monthly'!HM4
    value = 1.072
    formula = "=VLOOKUP(HM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HM4():
        hm3_1 = LPG_Monthly.HM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HN4():
    # 'LPG_Monthly'!HN4
    value = 1.132
    formula = "=VLOOKUP(HN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HN4():
        hn3_1 = LPG_Monthly.HN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HO4():
    # 'LPG_Monthly'!HO4
    value = 1.234
    formula = "=VLOOKUP(HO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HO4():
        ho3_1 = LPG_Monthly.HO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ho3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HP4():
    # 'LPG_Monthly'!HP4
    value = 1.254
    formula = "=VLOOKUP(HP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HP4():
        hp3_1 = LPG_Monthly.HP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HQ4():
    # 'LPG_Monthly'!HQ4
    value = 1.296
    formula = "=VLOOKUP(HQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HQ4():
        hq3_1 = LPG_Monthly.HQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HR4():
    # 'LPG_Monthly'!HR4
    value = 1.348
    formula = "=VLOOKUP(HR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HR4():
        hr3_1 = LPG_Monthly.HR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HS4():
    # 'LPG_Monthly'!HS4
    value = 1.379
    formula = "=VLOOKUP(HS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HS4():
        hs3_1 = LPG_Monthly.HS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HT4():
    # 'LPG_Monthly'!HT4
    value = 1.397
    formula = "=VLOOKUP(HT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HT4():
        ht3_1 = LPG_Monthly.HT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ht3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HU4():
    # 'LPG_Monthly'!HU4
    value = 1.454
    formula = "=VLOOKUP(HU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HU4():
        hu3_1 = LPG_Monthly.HU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HV4():
    # 'LPG_Monthly'!HV4
    value = 1.521
    formula = "=VLOOKUP(HV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HV4():
        hv3_1 = LPG_Monthly.HV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HW4():
    # 'LPG_Monthly'!HW4
    value = 1.52
    formula = "=VLOOKUP(HW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HW4():
        hw3_1 = LPG_Monthly.HW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HX4():
    # 'LPG_Monthly'!HX4
    value = 1.528
    formula = "=VLOOKUP(HX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HX4():
        hx3_1 = LPG_Monthly.HX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HY4():
    # 'LPG_Monthly'!HY4
    value = 1.528
    formula = "=VLOOKUP(HY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HY4():
        hy3_1 = LPG_Monthly.HY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class HZ4():
    # 'LPG_Monthly'!HZ4
    value = 1.56
    formula = "=VLOOKUP(HZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def HZ4():
        hz3_1 = LPG_Monthly.HZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(hz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IA4():
    # 'LPG_Monthly'!IA4
    value = 1.472
    formula = "=VLOOKUP(IA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IA4():
        ia3_1 = LPG_Monthly.IA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ia3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IB4():
    # 'LPG_Monthly'!IB4
    value = 1.458
    formula = "=VLOOKUP(IB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IB4():
        ib3_1 = LPG_Monthly.IB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ib3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IC4():
    # 'LPG_Monthly'!IC4
    value = 1.395
    formula = "=VLOOKUP(IC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IC4():
        ic3_1 = LPG_Monthly.IC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ic3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ID4():
    # 'LPG_Monthly'!ID4
    value = 1.294
    formula = "=VLOOKUP(ID$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ID4():
        id3_1 = LPG_Monthly.ID3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(id3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IE4():
    # 'LPG_Monthly'!IE4
    value = 1.22
    formula = "=VLOOKUP(IE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IE4():
        ie3_1 = LPG_Monthly.IE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ie3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IF4():
    # 'LPG_Monthly'!IF4
    value = 1.261
    formula = "=VLOOKUP(IF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IF4():
        if3_1 = LPG_Monthly.IF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(if3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IG4():
    # 'LPG_Monthly'!IG4
    value = 1.196
    formula = "=VLOOKUP(IG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IG4():
        ig3_1 = LPG_Monthly.IG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ig3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IH4():
    # 'LPG_Monthly'!IH4
    value = 0.954
    formula = "=VLOOKUP(IH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IH4():
        ih3_1 = LPG_Monthly.IH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ih3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class II4():
    # 'LPG_Monthly'!II4
    value = 0.788
    formula = "=VLOOKUP(II$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def II4():
        ii3_1 = LPG_Monthly.II3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ii3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IJ4():
    # 'LPG_Monthly'!IJ4
    value = 0.874
    formula = "=VLOOKUP(IJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IJ4():
        ij3_1 = LPG_Monthly.IJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ij3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IK4():
    # 'LPG_Monthly'!IK4
    value = 0.901
    formula = "=VLOOKUP(IK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IK4():
        ik3_1 = LPG_Monthly.IK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ik3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IL4():
    # 'LPG_Monthly'!IL4
    value = 0.91
    formula = "=VLOOKUP(IL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IL4():
        il3_1 = LPG_Monthly.IL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(il3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IM4():
    # 'LPG_Monthly'!IM4
    value = 0.962
    formula = "=VLOOKUP(IM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IM4():
        im3_1 = LPG_Monthly.IM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(im3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IN4():
    # 'LPG_Monthly'!IN4
    value = 0.89
    formula = "=VLOOKUP(IN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IN4():
        in3_1 = LPG_Monthly.IN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(in3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IO4():
    # 'LPG_Monthly'!IO4
    value = 0.797
    formula = "=VLOOKUP(IO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IO4():
        io3_1 = LPG_Monthly.IO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(io3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IP4():
    # 'LPG_Monthly'!IP4
    value = 0.838
    formula = "=VLOOKUP(IP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IP4():
        ip3_1 = LPG_Monthly.IP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ip3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IQ4():
    # 'LPG_Monthly'!IQ4
    value = 0.862
    formula = "=VLOOKUP(IQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IQ4():
        iq3_1 = LPG_Monthly.IQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IR4():
    # 'LPG_Monthly'!IR4
    value = 0.895
    formula = "=VLOOKUP(IR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IR4():
        ir3_1 = LPG_Monthly.IR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ir3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IS4():
    # 'LPG_Monthly'!IS4
    value = 0.939
    formula = "=VLOOKUP(IS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IS4():
        is3_1 = LPG_Monthly.IS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(is3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IT4():
    # 'LPG_Monthly'!IT4
    value = 0.932
    formula = "=VLOOKUP(IT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IT4():
        it3_1 = LPG_Monthly.IT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(it3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IU4():
    # 'LPG_Monthly'!IU4
    value = 0.863
    formula = "=VLOOKUP(IU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IU4():
        iu3_1 = LPG_Monthly.IU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IV4():
    # 'LPG_Monthly'!IV4
    value = 0.92
    formula = "=VLOOKUP(IV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IV4():
        iv3_1 = LPG_Monthly.IV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IW4():
    # 'LPG_Monthly'!IW4
    value = 1.061
    formula = "=VLOOKUP(IW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IW4():
        iw3_1 = LPG_Monthly.IW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IX4():
    # 'LPG_Monthly'!IX4
    value = 1.107
    formula = "=VLOOKUP(IX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IX4():
        ix3_1 = LPG_Monthly.IX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ix3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IY4():
    # 'LPG_Monthly'!IY4
    value = 1.136
    formula = "=VLOOKUP(IY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IY4():
        iy3_1 = LPG_Monthly.IY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class IZ4():
    # 'LPG_Monthly'!IZ4
    value = 1.181
    formula = "=VLOOKUP(IZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def IZ4():
        iz3_1 = LPG_Monthly.IZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(iz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JA4():
    # 'LPG_Monthly'!JA4
    value = 1.275
    formula = "=VLOOKUP(JA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JA4():
        ja3_1 = LPG_Monthly.JA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ja3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JB4():
    # 'LPG_Monthly'!JB4
    value = 1.395
    formula = "=VLOOKUP(JB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JB4():
        jb3_1 = LPG_Monthly.JB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JC4():
    # 'LPG_Monthly'!JC4
    value = 1.443
    formula = "=VLOOKUP(JC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JC4():
        jc3_1 = LPG_Monthly.JC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JD4():
    # 'LPG_Monthly'!JD4
    value = 1.064
    formula = "=VLOOKUP(JD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JD4():
        jd3_1 = LPG_Monthly.JD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JE4():
    # 'LPG_Monthly'!JE4
    value = 1.101
    formula = "=VLOOKUP(JE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JE4():
        je3_1 = LPG_Monthly.JE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(je3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JF4():
    # 'LPG_Monthly'!JF4
    value = 1.043
    formula = "=VLOOKUP(JF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JF4():
        jf3_1 = LPG_Monthly.JF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JG4():
    # 'LPG_Monthly'!JG4
    value = 1.046
    formula = "=VLOOKUP(JG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JG4():
        jg3_1 = LPG_Monthly.JG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JH4():
    # 'LPG_Monthly'!JH4
    value = 1.036
    formula = "=VLOOKUP(JH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JH4():
        jh3_1 = LPG_Monthly.JH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JI4():
    # 'LPG_Monthly'!JI4
    value = 1.018
    formula = "=VLOOKUP(JI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JI4():
        ji3_1 = LPG_Monthly.JI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ji3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JJ4():
    # 'LPG_Monthly'!JJ4
    value = 1.062
    formula = "=VLOOKUP(JJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JJ4():
        jj3_1 = LPG_Monthly.JJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JK4():
    # 'LPG_Monthly'!JK4
    value = 0.936
    formula = "=VLOOKUP(JK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JK4():
        jk3_1 = LPG_Monthly.JK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JL4():
    # 'LPG_Monthly'!JL4
    value = 0.802
    formula = "=VLOOKUP(JL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JL4():
        jl3_1 = LPG_Monthly.JL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JM4():
    # 'LPG_Monthly'!JM4
    value = 0.558
    formula = "=VLOOKUP(JM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JM4():
        jm3_1 = LPG_Monthly.JM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JN4():
    # 'LPG_Monthly'!JN4
    value = 0.478
    formula = "=VLOOKUP(JN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JN4():
        jn3_1 = LPG_Monthly.JN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JO4():
    # 'LPG_Monthly'!JO4
    value = 0.573
    formula = "=VLOOKUP(JO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JO4():
        jo3_1 = LPG_Monthly.JO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JP4():
    # 'LPG_Monthly'!JP4
    value = 0.542
    formula = "=VLOOKUP(JP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JP4():
        jp3_1 = LPG_Monthly.JP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JQ4():
    # 'LPG_Monthly'!JQ4
    value = 0.548
    formula = "=VLOOKUP(JQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JQ4():
        jq3_1 = LPG_Monthly.JQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JR4():
    # 'LPG_Monthly'!JR4
    value = 0.47
    formula = "=VLOOKUP(JR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JR4():
        jr3_1 = LPG_Monthly.JR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JS4():
    # 'LPG_Monthly'!JS4
    value = 0.369
    formula = "=VLOOKUP(JS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JS4():
        js3_1 = LPG_Monthly.JS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(js3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JT4():
    # 'LPG_Monthly'!JT4
    value = 0.409
    formula = "=VLOOKUP(JT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JT4():
        jt3_1 = LPG_Monthly.JT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JU4():
    # 'LPG_Monthly'!JU4
    value = 0.374
    formula = "=VLOOKUP(JU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JU4():
        ju3_1 = LPG_Monthly.JU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ju3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JV4():
    # 'LPG_Monthly'!JV4
    value = 0.453
    formula = "=VLOOKUP(JV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JV4():
        jv3_1 = LPG_Monthly.JV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JW4():
    # 'LPG_Monthly'!JW4
    value = 0.451
    formula = "=VLOOKUP(JW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JW4():
        jw3_1 = LPG_Monthly.JW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JX4():
    # 'LPG_Monthly'!JX4
    value = 0.43
    formula = "=VLOOKUP(JX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JX4():
        jx3_1 = LPG_Monthly.JX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JY4():
    # 'LPG_Monthly'!JY4
    value = 0.387
    formula = "=VLOOKUP(JY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JY4():
        jy3_1 = LPG_Monthly.JY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class JZ4():
    # 'LPG_Monthly'!JZ4
    value = 0.336
    formula = "=VLOOKUP(JZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def JZ4():
        jz3_1 = LPG_Monthly.JZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(jz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KA4():
    # 'LPG_Monthly'!KA4
    value = "#N/A"
    formula = "=VLOOKUP(KA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KA4():
        ka3_1 = LPG_Monthly.KA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ka3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KB4():
    # 'LPG_Monthly'!KB4
    value = "#N/A"
    formula = "=VLOOKUP(KB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KB4():
        kb3_1 = LPG_Monthly.KB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KC4():
    # 'LPG_Monthly'!KC4
    value = "#N/A"
    formula = "=VLOOKUP(KC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KC4():
        kc3_1 = LPG_Monthly.KC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KD4():
    # 'LPG_Monthly'!KD4
    value = "#N/A"
    formula = "=VLOOKUP(KD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KD4():
        kd3_1 = LPG_Monthly.KD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KE4():
    # 'LPG_Monthly'!KE4
    value = "#N/A"
    formula = "=VLOOKUP(KE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KE4():
        ke3_1 = LPG_Monthly.KE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ke3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KF4():
    # 'LPG_Monthly'!KF4
    value = "#N/A"
    formula = "=VLOOKUP(KF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KF4():
        kf3_1 = LPG_Monthly.KF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KG4():
    # 'LPG_Monthly'!KG4
    value = "#N/A"
    formula = "=VLOOKUP(KG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KG4():
        kg3_1 = LPG_Monthly.KG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KH4():
    # 'LPG_Monthly'!KH4
    value = "#N/A"
    formula = "=VLOOKUP(KH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KH4():
        kh3_1 = LPG_Monthly.KH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KI4():
    # 'LPG_Monthly'!KI4
    value = "#N/A"
    formula = "=VLOOKUP(KI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KI4():
        ki3_1 = LPG_Monthly.KI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ki3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KJ4():
    # 'LPG_Monthly'!KJ4
    value = "#N/A"
    formula = "=VLOOKUP(KJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KJ4():
        kj3_1 = LPG_Monthly.KJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KK4():
    # 'LPG_Monthly'!KK4
    value = "#N/A"
    formula = "=VLOOKUP(KK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KK4():
        kk3_1 = LPG_Monthly.KK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KL4():
    # 'LPG_Monthly'!KL4
    value = "#N/A"
    formula = "=VLOOKUP(KL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KL4():
        kl3_1 = LPG_Monthly.KL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KM4():
    # 'LPG_Monthly'!KM4
    value = "#N/A"
    formula = "=VLOOKUP(KM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KM4():
        km3_1 = LPG_Monthly.KM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(km3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KN4():
    # 'LPG_Monthly'!KN4
    value = "#N/A"
    formula = "=VLOOKUP(KN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KN4():
        kn3_1 = LPG_Monthly.KN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KO4():
    # 'LPG_Monthly'!KO4
    value = "#N/A"
    formula = "=VLOOKUP(KO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KO4():
        ko3_1 = LPG_Monthly.KO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ko3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KP4():
    # 'LPG_Monthly'!KP4
    value = "#N/A"
    formula = "=VLOOKUP(KP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KP4():
        kp3_1 = LPG_Monthly.KP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KQ4():
    # 'LPG_Monthly'!KQ4
    value = "#N/A"
    formula = "=VLOOKUP(KQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KQ4():
        kq3_1 = LPG_Monthly.KQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KR4():
    # 'LPG_Monthly'!KR4
    value = "#N/A"
    formula = "=VLOOKUP(KR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KR4():
        kr3_1 = LPG_Monthly.KR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KS4():
    # 'LPG_Monthly'!KS4
    value = "#N/A"
    formula = "=VLOOKUP(KS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KS4():
        ks3_1 = LPG_Monthly.KS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ks3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KT4():
    # 'LPG_Monthly'!KT4
    value = "#N/A"
    formula = "=VLOOKUP(KT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KT4():
        kt3_1 = LPG_Monthly.KT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KU4():
    # 'LPG_Monthly'!KU4
    value = "#N/A"
    formula = "=VLOOKUP(KU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KU4():
        ku3_1 = LPG_Monthly.KU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ku3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KV4():
    # 'LPG_Monthly'!KV4
    value = "#N/A"
    formula = "=VLOOKUP(KV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KV4():
        kv3_1 = LPG_Monthly.KV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KW4():
    # 'LPG_Monthly'!KW4
    value = "#N/A"
    formula = "=VLOOKUP(KW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KW4():
        kw3_1 = LPG_Monthly.KW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KX4():
    # 'LPG_Monthly'!KX4
    value = "#N/A"
    formula = "=VLOOKUP(KX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KX4():
        kx3_1 = LPG_Monthly.KX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KY4():
    # 'LPG_Monthly'!KY4
    value = "#N/A"
    formula = "=VLOOKUP(KY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KY4():
        ky3_1 = LPG_Monthly.KY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ky3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class KZ4():
    # 'LPG_Monthly'!KZ4
    value = "#N/A"
    formula = "=VLOOKUP(KZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def KZ4():
        kz3_1 = LPG_Monthly.KZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(kz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LA4():
    # 'LPG_Monthly'!LA4
    value = "#N/A"
    formula = "=VLOOKUP(LA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LA4():
        la3_1 = LPG_Monthly.LA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(la3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LB4():
    # 'LPG_Monthly'!LB4
    value = "#N/A"
    formula = "=VLOOKUP(LB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LB4():
        lb3_1 = LPG_Monthly.LB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LC4():
    # 'LPG_Monthly'!LC4
    value = "#N/A"
    formula = "=VLOOKUP(LC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LC4():
        lc3_1 = LPG_Monthly.LC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LD4():
    # 'LPG_Monthly'!LD4
    value = "#N/A"
    formula = "=VLOOKUP(LD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LD4():
        ld3_1 = LPG_Monthly.LD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ld3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LE4():
    # 'LPG_Monthly'!LE4
    value = "#N/A"
    formula = "=VLOOKUP(LE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LE4():
        le3_1 = LPG_Monthly.LE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(le3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LF4():
    # 'LPG_Monthly'!LF4
    value = "#N/A"
    formula = "=VLOOKUP(LF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LF4():
        lf3_1 = LPG_Monthly.LF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LG4():
    # 'LPG_Monthly'!LG4
    value = "#N/A"
    formula = "=VLOOKUP(LG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LG4():
        lg3_1 = LPG_Monthly.LG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LH4():
    # 'LPG_Monthly'!LH4
    value = "#N/A"
    formula = "=VLOOKUP(LH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LH4():
        lh3_1 = LPG_Monthly.LH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LI4():
    # 'LPG_Monthly'!LI4
    value = "#N/A"
    formula = "=VLOOKUP(LI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LI4():
        li3_1 = LPG_Monthly.LI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(li3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LJ4():
    # 'LPG_Monthly'!LJ4
    value = "#N/A"
    formula = "=VLOOKUP(LJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LJ4():
        lj3_1 = LPG_Monthly.LJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LK4():
    # 'LPG_Monthly'!LK4
    value = "#N/A"
    formula = "=VLOOKUP(LK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LK4():
        lk3_1 = LPG_Monthly.LK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LL4():
    # 'LPG_Monthly'!LL4
    value = "#N/A"
    formula = "=VLOOKUP(LL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LL4():
        ll3_1 = LPG_Monthly.LL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ll3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LM4():
    # 'LPG_Monthly'!LM4
    value = "#N/A"
    formula = "=VLOOKUP(LM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LM4():
        lm3_1 = LPG_Monthly.LM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LN4():
    # 'LPG_Monthly'!LN4
    value = "#N/A"
    formula = "=VLOOKUP(LN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LN4():
        ln3_1 = LPG_Monthly.LN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ln3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LO4():
    # 'LPG_Monthly'!LO4
    value = "#N/A"
    formula = "=VLOOKUP(LO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LO4():
        lo3_1 = LPG_Monthly.LO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LP4():
    # 'LPG_Monthly'!LP4
    value = "#N/A"
    formula = "=VLOOKUP(LP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LP4():
        lp3_1 = LPG_Monthly.LP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LQ4():
    # 'LPG_Monthly'!LQ4
    value = "#N/A"
    formula = "=VLOOKUP(LQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LQ4():
        lq3_1 = LPG_Monthly.LQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LR4():
    # 'LPG_Monthly'!LR4
    value = "#N/A"
    formula = "=VLOOKUP(LR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LR4():
        lr3_1 = LPG_Monthly.LR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LS4():
    # 'LPG_Monthly'!LS4
    value = "#N/A"
    formula = "=VLOOKUP(LS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LS4():
        ls3_1 = LPG_Monthly.LS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ls3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LT4():
    # 'LPG_Monthly'!LT4
    value = "#N/A"
    formula = "=VLOOKUP(LT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LT4():
        lt3_1 = LPG_Monthly.LT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LU4():
    # 'LPG_Monthly'!LU4
    value = "#N/A"
    formula = "=VLOOKUP(LU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LU4():
        lu3_1 = LPG_Monthly.LU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LV4():
    # 'LPG_Monthly'!LV4
    value = "#N/A"
    formula = "=VLOOKUP(LV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LV4():
        lv3_1 = LPG_Monthly.LV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LW4():
    # 'LPG_Monthly'!LW4
    value = "#N/A"
    formula = "=VLOOKUP(LW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LW4():
        lw3_1 = LPG_Monthly.LW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LX4():
    # 'LPG_Monthly'!LX4
    value = "#N/A"
    formula = "=VLOOKUP(LX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LX4():
        lx3_1 = LPG_Monthly.LX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LY4():
    # 'LPG_Monthly'!LY4
    value = "#N/A"
    formula = "=VLOOKUP(LY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LY4():
        ly3_1 = LPG_Monthly.LY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ly3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class LZ4():
    # 'LPG_Monthly'!LZ4
    value = "#N/A"
    formula = "=VLOOKUP(LZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def LZ4():
        lz3_1 = LPG_Monthly.LZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(lz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MA4():
    # 'LPG_Monthly'!MA4
    value = "#N/A"
    formula = "=VLOOKUP(MA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MA4():
        ma3_1 = LPG_Monthly.MA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ma3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MB4():
    # 'LPG_Monthly'!MB4
    value = "#N/A"
    formula = "=VLOOKUP(MB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MB4():
        mb3_1 = LPG_Monthly.MB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MC4():
    # 'LPG_Monthly'!MC4
    value = "#N/A"
    formula = "=VLOOKUP(MC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MC4():
        mc3_1 = LPG_Monthly.MC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MD4():
    # 'LPG_Monthly'!MD4
    value = "#N/A"
    formula = "=VLOOKUP(MD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MD4():
        md3_1 = LPG_Monthly.MD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(md3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ME4():
    # 'LPG_Monthly'!ME4
    value = "#N/A"
    formula = "=VLOOKUP(ME$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ME4():
        me3_1 = LPG_Monthly.ME3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(me3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MF4():
    # 'LPG_Monthly'!MF4
    value = "#N/A"
    formula = "=VLOOKUP(MF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MF4():
        mf3_1 = LPG_Monthly.MF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MG4():
    # 'LPG_Monthly'!MG4
    value = "#N/A"
    formula = "=VLOOKUP(MG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MG4():
        mg3_1 = LPG_Monthly.MG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MH4():
    # 'LPG_Monthly'!MH4
    value = "#N/A"
    formula = "=VLOOKUP(MH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MH4():
        mh3_1 = LPG_Monthly.MH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MI4():
    # 'LPG_Monthly'!MI4
    value = "#N/A"
    formula = "=VLOOKUP(MI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MI4():
        mi3_1 = LPG_Monthly.MI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MJ4():
    # 'LPG_Monthly'!MJ4
    value = "#N/A"
    formula = "=VLOOKUP(MJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MJ4():
        mj3_1 = LPG_Monthly.MJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MK4():
    # 'LPG_Monthly'!MK4
    value = "#N/A"
    formula = "=VLOOKUP(MK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MK4():
        mk3_1 = LPG_Monthly.MK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ML4():
    # 'LPG_Monthly'!ML4
    value = "#N/A"
    formula = "=VLOOKUP(ML$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ML4():
        ml3_1 = LPG_Monthly.ML3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ml3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MM4():
    # 'LPG_Monthly'!MM4
    value = "#N/A"
    formula = "=VLOOKUP(MM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MM4():
        mm3_1 = LPG_Monthly.MM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MN4():
    # 'LPG_Monthly'!MN4
    value = "#N/A"
    formula = "=VLOOKUP(MN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MN4():
        mn3_1 = LPG_Monthly.MN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MO4():
    # 'LPG_Monthly'!MO4
    value = "#N/A"
    formula = "=VLOOKUP(MO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MO4():
        mo3_1 = LPG_Monthly.MO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MP4():
    # 'LPG_Monthly'!MP4
    value = "#N/A"
    formula = "=VLOOKUP(MP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MP4():
        mp3_1 = LPG_Monthly.MP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MQ4():
    # 'LPG_Monthly'!MQ4
    value = "#N/A"
    formula = "=VLOOKUP(MQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MQ4():
        mq3_1 = LPG_Monthly.MQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MR4():
    # 'LPG_Monthly'!MR4
    value = "#N/A"
    formula = "=VLOOKUP(MR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MR4():
        mr3_1 = LPG_Monthly.MR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MS4():
    # 'LPG_Monthly'!MS4
    value = "#N/A"
    formula = "=VLOOKUP(MS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MS4():
        ms3_1 = LPG_Monthly.MS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ms3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MT4():
    # 'LPG_Monthly'!MT4
    value = "#N/A"
    formula = "=VLOOKUP(MT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MT4():
        mt3_1 = LPG_Monthly.MT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MU4():
    # 'LPG_Monthly'!MU4
    value = "#N/A"
    formula = "=VLOOKUP(MU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MU4():
        mu3_1 = LPG_Monthly.MU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MV4():
    # 'LPG_Monthly'!MV4
    value = "#N/A"
    formula = "=VLOOKUP(MV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MV4():
        mv3_1 = LPG_Monthly.MV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MW4():
    # 'LPG_Monthly'!MW4
    value = "#N/A"
    formula = "=VLOOKUP(MW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MW4():
        mw3_1 = LPG_Monthly.MW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MX4():
    # 'LPG_Monthly'!MX4
    value = "#N/A"
    formula = "=VLOOKUP(MX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MX4():
        mx3_1 = LPG_Monthly.MX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MY4():
    # 'LPG_Monthly'!MY4
    value = "#N/A"
    formula = "=VLOOKUP(MY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MY4():
        my3_1 = LPG_Monthly.MY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(my3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class MZ4():
    # 'LPG_Monthly'!MZ4
    value = "#N/A"
    formula = "=VLOOKUP(MZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def MZ4():
        mz3_1 = LPG_Monthly.MZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(mz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NA4():
    # 'LPG_Monthly'!NA4
    value = "#N/A"
    formula = "=VLOOKUP(NA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NA4():
        na3_1 = LPG_Monthly.NA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(na3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NB4():
    # 'LPG_Monthly'!NB4
    value = "#N/A"
    formula = "=VLOOKUP(NB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NB4():
        nb3_1 = LPG_Monthly.NB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NC4():
    # 'LPG_Monthly'!NC4
    value = "#N/A"
    formula = "=VLOOKUP(NC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NC4():
        nc3_1 = LPG_Monthly.NC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ND4():
    # 'LPG_Monthly'!ND4
    value = "#N/A"
    formula = "=VLOOKUP(ND$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ND4():
        nd3_1 = LPG_Monthly.ND3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NE4():
    # 'LPG_Monthly'!NE4
    value = "#N/A"
    formula = "=VLOOKUP(NE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NE4():
        ne3_1 = LPG_Monthly.NE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ne3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NF4():
    # 'LPG_Monthly'!NF4
    value = "#N/A"
    formula = "=VLOOKUP(NF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NF4():
        nf3_1 = LPG_Monthly.NF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NG4():
    # 'LPG_Monthly'!NG4
    value = "#N/A"
    formula = "=VLOOKUP(NG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NG4():
        ng3_1 = LPG_Monthly.NG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ng3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NH4():
    # 'LPG_Monthly'!NH4
    value = "#N/A"
    formula = "=VLOOKUP(NH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NH4():
        nh3_1 = LPG_Monthly.NH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NI4():
    # 'LPG_Monthly'!NI4
    value = "#N/A"
    formula = "=VLOOKUP(NI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NI4():
        ni3_1 = LPG_Monthly.NI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ni3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NJ4():
    # 'LPG_Monthly'!NJ4
    value = "#N/A"
    formula = "=VLOOKUP(NJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NJ4():
        nj3_1 = LPG_Monthly.NJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NK4():
    # 'LPG_Monthly'!NK4
    value = "#N/A"
    formula = "=VLOOKUP(NK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NK4():
        nk3_1 = LPG_Monthly.NK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NL4():
    # 'LPG_Monthly'!NL4
    value = "#N/A"
    formula = "=VLOOKUP(NL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NL4():
        nl3_1 = LPG_Monthly.NL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NM4():
    # 'LPG_Monthly'!NM4
    value = "#N/A"
    formula = "=VLOOKUP(NM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NM4():
        nm3_1 = LPG_Monthly.NM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NN4():
    # 'LPG_Monthly'!NN4
    value = "#N/A"
    formula = "=VLOOKUP(NN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NN4():
        nn3_1 = LPG_Monthly.NN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NO4():
    # 'LPG_Monthly'!NO4
    value = "#N/A"
    formula = "=VLOOKUP(NO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NO4():
        no3_1 = LPG_Monthly.NO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(no3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NP4():
    # 'LPG_Monthly'!NP4
    value = "#N/A"
    formula = "=VLOOKUP(NP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NP4():
        np3_1 = LPG_Monthly.NP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(np3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NQ4():
    # 'LPG_Monthly'!NQ4
    value = "#N/A"
    formula = "=VLOOKUP(NQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NQ4():
        nq3_1 = LPG_Monthly.NQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NR4():
    # 'LPG_Monthly'!NR4
    value = "#N/A"
    formula = "=VLOOKUP(NR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NR4():
        nr3_1 = LPG_Monthly.NR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NS4():
    # 'LPG_Monthly'!NS4
    value = "#N/A"
    formula = "=VLOOKUP(NS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NS4():
        ns3_1 = LPG_Monthly.NS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ns3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NT4():
    # 'LPG_Monthly'!NT4
    value = "#N/A"
    formula = "=VLOOKUP(NT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NT4():
        nt3_1 = LPG_Monthly.NT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NU4():
    # 'LPG_Monthly'!NU4
    value = "#N/A"
    formula = "=VLOOKUP(NU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NU4():
        nu3_1 = LPG_Monthly.NU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NV4():
    # 'LPG_Monthly'!NV4
    value = "#N/A"
    formula = "=VLOOKUP(NV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NV4():
        nv3_1 = LPG_Monthly.NV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NW4():
    # 'LPG_Monthly'!NW4
    value = "#N/A"
    formula = "=VLOOKUP(NW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NW4():
        nw3_1 = LPG_Monthly.NW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NX4():
    # 'LPG_Monthly'!NX4
    value = "#N/A"
    formula = "=VLOOKUP(NX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NX4():
        nx3_1 = LPG_Monthly.NX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nx3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NY4():
    # 'LPG_Monthly'!NY4
    value = "#N/A"
    formula = "=VLOOKUP(NY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NY4():
        ny3_1 = LPG_Monthly.NY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ny3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class NZ4():
    # 'LPG_Monthly'!NZ4
    value = "#N/A"
    formula = "=VLOOKUP(NZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def NZ4():
        nz3_1 = LPG_Monthly.NZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(nz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OA4():
    # 'LPG_Monthly'!OA4
    value = "#N/A"
    formula = "=VLOOKUP(OA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OA4():
        oa3_1 = LPG_Monthly.OA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oa3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OB4():
    # 'LPG_Monthly'!OB4
    value = "#N/A"
    formula = "=VLOOKUP(OB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OB4():
        ob3_1 = LPG_Monthly.OB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ob3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OC4():
    # 'LPG_Monthly'!OC4
    value = "#N/A"
    formula = "=VLOOKUP(OC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OC4():
        oc3_1 = LPG_Monthly.OC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OD4():
    # 'LPG_Monthly'!OD4
    value = "#N/A"
    formula = "=VLOOKUP(OD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OD4():
        od3_1 = LPG_Monthly.OD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(od3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OE4():
    # 'LPG_Monthly'!OE4
    value = "#N/A"
    formula = "=VLOOKUP(OE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OE4():
        oe3_1 = LPG_Monthly.OE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oe3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OF4():
    # 'LPG_Monthly'!OF4
    value = "#N/A"
    formula = "=VLOOKUP(OF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OF4():
        of3_1 = LPG_Monthly.OF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(of3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OG4():
    # 'LPG_Monthly'!OG4
    value = "#N/A"
    formula = "=VLOOKUP(OG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OG4():
        og3_1 = LPG_Monthly.OG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(og3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OH4():
    # 'LPG_Monthly'!OH4
    value = "#N/A"
    formula = "=VLOOKUP(OH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OH4():
        oh3_1 = LPG_Monthly.OH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OI4():
    # 'LPG_Monthly'!OI4
    value = "#N/A"
    formula = "=VLOOKUP(OI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OI4():
        oi3_1 = LPG_Monthly.OI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OJ4():
    # 'LPG_Monthly'!OJ4
    value = "#N/A"
    formula = "=VLOOKUP(OJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OJ4():
        oj3_1 = LPG_Monthly.OJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OK4():
    # 'LPG_Monthly'!OK4
    value = "#N/A"
    formula = "=VLOOKUP(OK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OK4():
        ok3_1 = LPG_Monthly.OK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ok3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OL4():
    # 'LPG_Monthly'!OL4
    value = "#N/A"
    formula = "=VLOOKUP(OL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OL4():
        ol3_1 = LPG_Monthly.OL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ol3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OM4():
    # 'LPG_Monthly'!OM4
    value = "#N/A"
    formula = "=VLOOKUP(OM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OM4():
        om3_1 = LPG_Monthly.OM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(om3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class ON4():
    # 'LPG_Monthly'!ON4
    value = "#N/A"
    formula = "=VLOOKUP(ON$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def ON4():
        on3_1 = LPG_Monthly.ON3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(on3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OO4():
    # 'LPG_Monthly'!OO4
    value = "#N/A"
    formula = "=VLOOKUP(OO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OO4():
        oo3_1 = LPG_Monthly.OO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OP4():
    # 'LPG_Monthly'!OP4
    value = "#N/A"
    formula = "=VLOOKUP(OP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OP4():
        op3_1 = LPG_Monthly.OP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(op3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OQ4():
    # 'LPG_Monthly'!OQ4
    value = "#N/A"
    formula = "=VLOOKUP(OQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OQ4():
        oq3_1 = LPG_Monthly.OQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OR4():
    # 'LPG_Monthly'!OR4
    value = "#N/A"
    formula = "=VLOOKUP(OR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OR4():
        or3_1 = LPG_Monthly.OR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(or3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OS4():
    # 'LPG_Monthly'!OS4
    value = "#N/A"
    formula = "=VLOOKUP(OS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OS4():
        os3_1 = LPG_Monthly.OS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(os3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OT4():
    # 'LPG_Monthly'!OT4
    value = "#N/A"
    formula = "=VLOOKUP(OT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OT4():
        ot3_1 = LPG_Monthly.OT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ot3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OU4():
    # 'LPG_Monthly'!OU4
    value = "#N/A"
    formula = "=VLOOKUP(OU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OU4():
        ou3_1 = LPG_Monthly.OU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ou3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OV4():
    # 'LPG_Monthly'!OV4
    value = "#N/A"
    formula = "=VLOOKUP(OV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OV4():
        ov3_1 = LPG_Monthly.OV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ov3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OW4():
    # 'LPG_Monthly'!OW4
    value = "#N/A"
    formula = "=VLOOKUP(OW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OW4():
        ow3_1 = LPG_Monthly.OW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ow3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OX4():
    # 'LPG_Monthly'!OX4
    value = "#N/A"
    formula = "=VLOOKUP(OX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OX4():
        ox3_1 = LPG_Monthly.OX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ox3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OY4():
    # 'LPG_Monthly'!OY4
    value = "#N/A"
    formula = "=VLOOKUP(OY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OY4():
        oy3_1 = LPG_Monthly.OY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oy3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class OZ4():
    # 'LPG_Monthly'!OZ4
    value = "#N/A"
    formula = "=VLOOKUP(OZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def OZ4():
        oz3_1 = LPG_Monthly.OZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(oz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PA4():
    # 'LPG_Monthly'!PA4
    value = "#N/A"
    formula = "=VLOOKUP(PA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PA4():
        pa3_1 = LPG_Monthly.PA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pa3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PB4():
    # 'LPG_Monthly'!PB4
    value = "#N/A"
    formula = "=VLOOKUP(PB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PB4():
        pb3_1 = LPG_Monthly.PB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PC4():
    # 'LPG_Monthly'!PC4
    value = "#N/A"
    formula = "=VLOOKUP(PC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PC4():
        pc3_1 = LPG_Monthly.PC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PD4():
    # 'LPG_Monthly'!PD4
    value = "#N/A"
    formula = "=VLOOKUP(PD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PD4():
        pd3_1 = LPG_Monthly.PD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PE4():
    # 'LPG_Monthly'!PE4
    value = "#N/A"
    formula = "=VLOOKUP(PE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PE4():
        pe3_1 = LPG_Monthly.PE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pe3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PF4():
    # 'LPG_Monthly'!PF4
    value = "#N/A"
    formula = "=VLOOKUP(PF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PF4():
        pf3_1 = LPG_Monthly.PF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PG4():
    # 'LPG_Monthly'!PG4
    value = "#N/A"
    formula = "=VLOOKUP(PG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PG4():
        pg3_1 = LPG_Monthly.PG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PH4():
    # 'LPG_Monthly'!PH4
    value = "#N/A"
    formula = "=VLOOKUP(PH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PH4():
        ph3_1 = LPG_Monthly.PH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ph3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PI4():
    # 'LPG_Monthly'!PI4
    value = "#N/A"
    formula = "=VLOOKUP(PI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PI4():
        pi3_1 = LPG_Monthly.PI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PJ4():
    # 'LPG_Monthly'!PJ4
    value = "#N/A"
    formula = "=VLOOKUP(PJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PJ4():
        pj3_1 = LPG_Monthly.PJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PK4():
    # 'LPG_Monthly'!PK4
    value = "#N/A"
    formula = "=VLOOKUP(PK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PK4():
        pk3_1 = LPG_Monthly.PK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PL4():
    # 'LPG_Monthly'!PL4
    value = "#N/A"
    formula = "=VLOOKUP(PL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PL4():
        pl3_1 = LPG_Monthly.PL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pl3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PM4():
    # 'LPG_Monthly'!PM4
    value = "#N/A"
    formula = "=VLOOKUP(PM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PM4():
        pm3_1 = LPG_Monthly.PM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PN4():
    # 'LPG_Monthly'!PN4
    value = "#N/A"
    formula = "=VLOOKUP(PN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PN4():
        pn3_1 = LPG_Monthly.PN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PO4():
    # 'LPG_Monthly'!PO4
    value = "#N/A"
    formula = "=VLOOKUP(PO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PO4():
        po3_1 = LPG_Monthly.PO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(po3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PP4():
    # 'LPG_Monthly'!PP4
    value = "#N/A"
    formula = "=VLOOKUP(PP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PP4():
        pp3_1 = LPG_Monthly.PP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PQ4():
    # 'LPG_Monthly'!PQ4
    value = "#N/A"
    formula = "=VLOOKUP(PQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PQ4():
        pq3_1 = LPG_Monthly.PQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PR4():
    # 'LPG_Monthly'!PR4
    value = "#N/A"
    formula = "=VLOOKUP(PR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PR4():
        pr3_1 = LPG_Monthly.PR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PS4():
    # 'LPG_Monthly'!PS4
    value = "#N/A"
    formula = "=VLOOKUP(PS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PS4():
        ps3_1 = LPG_Monthly.PS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ps3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PT4():
    # 'LPG_Monthly'!PT4
    value = "#N/A"
    formula = "=VLOOKUP(PT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PT4():
        pt3_1 = LPG_Monthly.PT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PU4():
    # 'LPG_Monthly'!PU4
    value = "#N/A"
    formula = "=VLOOKUP(PU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PU4():
        pu3_1 = LPG_Monthly.PU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PV4():
    # 'LPG_Monthly'!PV4
    value = "#N/A"
    formula = "=VLOOKUP(PV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PV4():
        pv3_1 = LPG_Monthly.PV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PW4():
    # 'LPG_Monthly'!PW4
    value = "#N/A"
    formula = "=VLOOKUP(PW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PW4():
        pw3_1 = LPG_Monthly.PW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PX4():
    # 'LPG_Monthly'!PX4
    value = "#N/A"
    formula = "=VLOOKUP(PX$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PX4():
        px3_1 = LPG_Monthly.PX3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(px3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PY4():
    # 'LPG_Monthly'!PY4
    value = "#N/A"
    formula = "=VLOOKUP(PY$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PY4():
        py3_1 = LPG_Monthly.PY3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(py3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class PZ4():
    # 'LPG_Monthly'!PZ4
    value = "#N/A"
    formula = "=VLOOKUP(PZ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def PZ4():
        pz3_1 = LPG_Monthly.PZ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(pz3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QA4():
    # 'LPG_Monthly'!QA4
    value = "#N/A"
    formula = "=VLOOKUP(QA$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QA4():
        qa3_1 = LPG_Monthly.QA3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qa3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QB4():
    # 'LPG_Monthly'!QB4
    value = "#N/A"
    formula = "=VLOOKUP(QB$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QB4():
        qb3_1 = LPG_Monthly.QB3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qb3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QC4():
    # 'LPG_Monthly'!QC4
    value = "#N/A"
    formula = "=VLOOKUP(QC$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QC4():
        qc3_1 = LPG_Monthly.QC3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qc3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QD4():
    # 'LPG_Monthly'!QD4
    value = "#N/A"
    formula = "=VLOOKUP(QD$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QD4():
        qd3_1 = LPG_Monthly.QD3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qd3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QE4():
    # 'LPG_Monthly'!QE4
    value = "#N/A"
    formula = "=VLOOKUP(QE$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QE4():
        qe3_1 = LPG_Monthly.QE3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qe3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QF4():
    # 'LPG_Monthly'!QF4
    value = "#N/A"
    formula = "=VLOOKUP(QF$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QF4():
        qf3_1 = LPG_Monthly.QF3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qf3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QG4():
    # 'LPG_Monthly'!QG4
    value = "#N/A"
    formula = "=VLOOKUP(QG$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QG4():
        qg3_1 = LPG_Monthly.QG3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qg3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QH4():
    # 'LPG_Monthly'!QH4
    value = "#N/A"
    formula = "=VLOOKUP(QH$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QH4():
        qh3_1 = LPG_Monthly.QH3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qh3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QI4():
    # 'LPG_Monthly'!QI4
    value = "#N/A"
    formula = "=VLOOKUP(QI$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QI4():
        qi3_1 = LPG_Monthly.QI3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qi3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QJ4():
    # 'LPG_Monthly'!QJ4
    value = "#N/A"
    formula = "=VLOOKUP(QJ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QJ4():
        qj3_1 = LPG_Monthly.QJ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qj3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QK4():
    # 'LPG_Monthly'!QK4
    value = "#N/A"
    formula = "=VLOOKUP(QK$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QK4():
        qk3_1 = LPG_Monthly.QK3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qk3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QL4():
    # 'LPG_Monthly'!QL4
    value = "#N/A"
    formula = "=VLOOKUP(QL$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QL4():
        ql3_1 = LPG_Monthly.QL3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(ql3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QM4():
    # 'LPG_Monthly'!QM4
    value = "#N/A"
    formula = "=VLOOKUP(QM$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QM4():
        qm3_1 = LPG_Monthly.QM3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qm3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QN4():
    # 'LPG_Monthly'!QN4
    value = "#N/A"
    formula = "=VLOOKUP(QN$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QN4():
        qn3_1 = LPG_Monthly.QN3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qn3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QO4():
    # 'LPG_Monthly'!QO4
    value = "#N/A"
    formula = "=VLOOKUP(QO$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QO4():
        qo3_1 = LPG_Monthly.QO3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qo3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QP4():
    # 'LPG_Monthly'!QP4
    value = "#N/A"
    formula = "=VLOOKUP(QP$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QP4():
        qp3_1 = LPG_Monthly.QP3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qp3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QQ4():
    # 'LPG_Monthly'!QQ4
    value = "#N/A"
    formula = "=VLOOKUP(QQ$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QQ4():
        qq3_1 = LPG_Monthly.QQ3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qq3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QR4():
    # 'LPG_Monthly'!QR4
    value = "#N/A"
    formula = "=VLOOKUP(QR$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QR4():
        qr3_1 = LPG_Monthly.QR3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qr3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QS4():
    # 'LPG_Monthly'!QS4
    value = "#N/A"
    formula = "=VLOOKUP(QS$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QS4():
        qs3_1 = LPG_Monthly.QS3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qs3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QT4():
    # 'LPG_Monthly'!QT4
    value = "#N/A"
    formula = "=VLOOKUP(QT$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QT4():
        qt3_1 = LPG_Monthly.QT3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qt3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QU4():
    # 'LPG_Monthly'!QU4
    value = "#N/A"
    formula = "=VLOOKUP(QU$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QU4():
        qu3_1 = LPG_Monthly.QU3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qu3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QV4():
    # 'LPG_Monthly'!QV4
    value = "#N/A"
    formula = "=VLOOKUP(QV$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QV4():
        qv3_1 = LPG_Monthly.QV3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qv3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class QW4():
    # 'LPG_Monthly'!QW4
    value = "#N/A"
    formula = "=VLOOKUP(QW$3,'Input EIA Propane Price'!$A:$B,2,FALSE)"
    @eval_fn
    def QW4():
        qw3_1 = LPG_Monthly.QW3()
        range_1 = Input_EIA_Propane_Price(1, 0, 2, 0)
        var_1 = VLOOKUP(qw3_1, range_1, 2, "FALSE")
        return var_1

@register(LPG_Monthly)
class A5():
    # 'LPG_Monthly'!A5
    value = "Hawaii Propane Estimate Price"

@register(LPG_Monthly)
class B5():
    # 'LPG_Monthly'!B5
    value = "Dollars per Gallon"

@register(LPG_Monthly)
class C5():
    # 'LPG_Monthly'!C5
    value = 0.978500401021
    formula = "=C4*'LPG Annual'!$C$6"
    @eval_fn
    def C5():
        c4_1 = LPG_Monthly.C4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(c4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class D5():
    # 'LPG_Monthly'!D5
    value = 0.972811445201
    formula = "=D4*'LPG Annual'!$C$6"
    @eval_fn
    def D5():
        d4_1 = LPG_Monthly.D4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(d4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class E5():
    # 'LPG_Monthly'!E5
    value = 1.00694518012
    formula = "=E4*'LPG Annual'!$C$6"
    @eval_fn
    def E5():
        e4_1 = LPG_Monthly.E4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(e4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class F5():
    # 'LPG_Monthly'!F5
    value = 1.06667921623
    formula = "=F4*'LPG Annual'!$C$6"
    @eval_fn
    def F5():
        f4_1 = LPG_Monthly.F4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(f4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class G5():
    # 'LPG_Monthly'!G5
    value = 1.00694518012
    formula = "=G4*'LPG Annual'!$C$6"
    @eval_fn
    def G5():
        g4_1 = LPG_Monthly.G4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(g4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class H5():
    # 'LPG_Monthly'!H5
    value = 0.930144276552
    formula = "=H4*'LPG Annual'!$C$6"
    @eval_fn
    def H5():
        h4_1 = LPG_Monthly.H4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(h4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class I5():
    # 'LPG_Monthly'!I5
    value = 0.887477107903
    formula = "=I4*'LPG Annual'!$C$6"
    @eval_fn
    def I5():
        i4_1 = LPG_Monthly.I4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(i4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class J5():
    # 'LPG_Monthly'!J5
    value = 0.958589055652
    formula = "=J4*'LPG Annual'!$C$6"
    @eval_fn
    def J5():
        j4_1 = LPG_Monthly.J4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(j4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class K5():
    # 'LPG_Monthly'!K5
    value = 0.938677710282
    formula = "=K4*'LPG Annual'!$C$6"
    @eval_fn
    def K5():
        k4_1 = LPG_Monthly.K4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(k4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class L5():
    # 'LPG_Monthly'!L5
    value = 0.972811445201
    formula = "=L4*'LPG Annual'!$C$6"
    @eval_fn
    def L5():
        l4_1 = LPG_Monthly.L4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(l4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class M5():
    # 'LPG_Monthly'!M5
    value = 0.978500401021
    formula = "=M4*'LPG Annual'!$C$6"
    @eval_fn
    def M5():
        m4_1 = LPG_Monthly.M4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(m4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class N5():
    # 'LPG_Monthly'!N5
    value = 0.932988754462
    formula = "=N4*'LPG Annual'!$C$6"
    @eval_fn
    def N5():
        n4_1 = LPG_Monthly.N4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(n4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class O5():
    # 'LPG_Monthly'!O5
    value = 0.932988754462
    formula = "=O4*'LPG Annual'!$C$6"
    @eval_fn
    def O5():
        o4_1 = LPG_Monthly.O4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(o4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class P5():
    # 'LPG_Monthly'!P5
    value = 0.893166063723
    formula = "=P4*'LPG Annual'!$C$6"
    @eval_fn
    def P5():
        p4_1 = LPG_Monthly.P4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(p4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class Q5():
    # 'LPG_Monthly'!Q5
    value = 0.867565762533
    formula = "=Q4*'LPG Annual'!$C$6"
    @eval_fn
    def Q5():
        q4_1 = LPG_Monthly.Q4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(q4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class R5():
    # 'LPG_Monthly'!R5
    value = 0.850498895074
    formula = "=R4*'LPG Annual'!$C$6"
    @eval_fn
    def R5():
        r4_1 = LPG_Monthly.R4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(r4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class S5():
    # 'LPG_Monthly'!S5
    value = 0.833432027614
    formula = "=S4*'LPG Annual'!$C$6"
    @eval_fn
    def S5():
        s4_1 = LPG_Monthly.S4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(s4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class T5():
    # 'LPG_Monthly'!T5
    value = 0.782231425235
    formula = "=T4*'LPG Annual'!$C$6"
    @eval_fn
    def T5():
        t4_1 = LPG_Monthly.T4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(t4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class U5():
    # 'LPG_Monthly'!U5
    value = 0.696897087937
    formula = "=U4*'LPG Annual'!$C$6"
    @eval_fn
    def U5():
        u4_1 = LPG_Monthly.U4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(u4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class V5():
    # 'LPG_Monthly'!V5
    value = 0.748097690316
    formula = "=V4*'LPG Annual'!$C$6"
    @eval_fn
    def V5():
        v4_1 = LPG_Monthly.V4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(v4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class W5():
    # 'LPG_Monthly'!W5
    value = 0.824898593884
    formula = "=W4*'LPG Annual'!$C$6"
    @eval_fn
    def W5():
        w4_1 = LPG_Monthly.W4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(w4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class X5():
    # 'LPG_Monthly'!X5
    value = 0.807831726425
    formula = "=X4*'LPG Annual'!$C$6"
    @eval_fn
    def X5():
        x4_1 = LPG_Monthly.X4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(x4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class Y5():
    # 'LPG_Monthly'!Y5
    value = 0.822054115974
    formula = "=Y4*'LPG Annual'!$C$6"
    @eval_fn
    def Y5():
        y4_1 = LPG_Monthly.Y4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(y4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class Z5():
    # 'LPG_Monthly'!Z5
    value = 0.841965461344
    formula = "=Z4*'LPG Annual'!$C$6"
    @eval_fn
    def Z5():
        z4_1 = LPG_Monthly.Z4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(z4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AA5():
    # 'LPG_Monthly'!AA5
    value = 0.819209638064
    formula = "=AA4*'LPG Annual'!$C$6"
    @eval_fn
    def AA5():
        aa4_1 = LPG_Monthly.AA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(aa4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AB5():
    # 'LPG_Monthly'!AB5
    value = 0.830587549704
    formula = "=AB4*'LPG Annual'!$C$6"
    @eval_fn
    def AB5():
        ab4_1 = LPG_Monthly.AB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ab4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AC5():
    # 'LPG_Monthly'!AC5
    value = 0.853343372984
    formula = "=AC4*'LPG Annual'!$C$6"
    @eval_fn
    def AC5():
        ac4_1 = LPG_Monthly.AC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ac4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AD5():
    # 'LPG_Monthly'!AD5
    value = 0.850498895074
    formula = "=AD4*'LPG Annual'!$C$6"
    @eval_fn
    def AD5():
        ad4_1 = LPG_Monthly.AD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ad4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AE5():
    # 'LPG_Monthly'!AE5
    value = 0.921610842822
    formula = "=AE4*'LPG Annual'!$C$6"
    @eval_fn
    def AE5():
        ae4_1 = LPG_Monthly.AE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ae4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AF5():
    # 'LPG_Monthly'!AF5
    value = 0.978500401021
    formula = "=AF4*'LPG Annual'!$C$6"
    @eval_fn
    def AF5():
        af4_1 = LPG_Monthly.AF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(af4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AG5():
    # 'LPG_Monthly'!AG5
    value = 0.947211144012
    formula = "=AG4*'LPG Annual'!$C$6"
    @eval_fn
    def AG5():
        ag4_1 = LPG_Monthly.AG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ag4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AH5():
    # 'LPG_Monthly'!AH5
    value = 0.930144276552
    formula = "=AH4*'LPG Annual'!$C$6"
    @eval_fn
    def AH5():
        ah4_1 = LPG_Monthly.AH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ah4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AI5():
    # 'LPG_Monthly'!AI5
    value = 0.898855019543
    formula = "=AI4*'LPG Annual'!$C$6"
    @eval_fn
    def AI5():
        ai4_1 = LPG_Monthly.AI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ai4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AJ5():
    # 'LPG_Monthly'!AJ5
    value = 0.930144276552
    formula = "=AJ4*'LPG Annual'!$C$6"
    @eval_fn
    def AJ5():
        aj4_1 = LPG_Monthly.AJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(aj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AK5():
    # 'LPG_Monthly'!AK5
    value = 0.918766364912
    formula = "=AK4*'LPG Annual'!$C$6"
    @eval_fn
    def AK5():
        ak4_1 = LPG_Monthly.AK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ak4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AL5():
    # 'LPG_Monthly'!AL5
    value = 0.930144276552
    formula = "=AL4*'LPG Annual'!$C$6"
    @eval_fn
    def AL5():
        al4_1 = LPG_Monthly.AL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(al4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AM5():
    # 'LPG_Monthly'!AM5
    value = 0.904543975363
    formula = "=AM4*'LPG Annual'!$C$6"
    @eval_fn
    def AM5():
        am4_1 = LPG_Monthly.AM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(am4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AN5():
    # 'LPG_Monthly'!AN5
    value = 0.876099196263
    formula = "=AN4*'LPG Annual'!$C$6"
    @eval_fn
    def AN5():
        an4_1 = LPG_Monthly.AN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(an4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AO5():
    # 'LPG_Monthly'!AO5
    value = 0.890321585813
    formula = "=AO4*'LPG Annual'!$C$6"
    @eval_fn
    def AO5():
        ao4_1 = LPG_Monthly.AO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ao4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AP5():
    # 'LPG_Monthly'!AP5
    value = 0.890321585813
    formula = "=AP4*'LPG Annual'!$C$6"
    @eval_fn
    def AP5():
        ap4_1 = LPG_Monthly.AP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ap4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AQ5():
    # 'LPG_Monthly'!AQ5
    value = 0.878943674173
    formula = "=AQ4*'LPG Annual'!$C$6"
    @eval_fn
    def AQ5():
        aq4_1 = LPG_Monthly.AQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(aq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AR5():
    # 'LPG_Monthly'!AR5
    value = 0.881788152083
    formula = "=AR4*'LPG Annual'!$C$6"
    @eval_fn
    def AR5():
        ar4_1 = LPG_Monthly.AR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ar4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AS5():
    # 'LPG_Monthly'!AS5
    value = 1.00694518012
    formula = "=AS4*'LPG Annual'!$C$6"
    @eval_fn
    def AS5():
        as4_1 = LPG_Monthly.AS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(as4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AT5():
    # 'LPG_Monthly'!AT5
    value = 1.00694518012
    formula = "=AT4*'LPG Annual'!$C$6"
    @eval_fn
    def AT5():
        at4_1 = LPG_Monthly.AT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(at4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AU5():
    # 'LPG_Monthly'!AU5
    value = 1.10934638488
    formula = "=AU4*'LPG Annual'!$C$6"
    @eval_fn
    def AU5():
        au4_1 = LPG_Monthly.AU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(au4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AV5():
    # 'LPG_Monthly'!AV5
    value = 1.04961234877
    formula = "=AV4*'LPG Annual'!$C$6"
    @eval_fn
    def AV5():
        av4_1 = LPG_Monthly.AV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(av4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AW5():
    # 'LPG_Monthly'!AW5
    value = 1.01263413594
    formula = "=AW4*'LPG Annual'!$C$6"
    @eval_fn
    def AW5():
        aw4_1 = LPG_Monthly.AW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(aw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AX5():
    # 'LPG_Monthly'!AX5
    value = 0.989878312661
    formula = "=AX4*'LPG Annual'!$C$6"
    @eval_fn
    def AX5():
        ax4_1 = LPG_Monthly.AX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ax4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AY5():
    # 'LPG_Monthly'!AY5
    value = 0.989878312661
    formula = "=AY4*'LPG Annual'!$C$6"
    @eval_fn
    def AY5():
        ay4_1 = LPG_Monthly.AY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ay4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class AZ5():
    # 'LPG_Monthly'!AZ5
    value = 1.01263413594
    formula = "=AZ4*'LPG Annual'!$C$6"
    @eval_fn
    def AZ5():
        az4_1 = LPG_Monthly.AZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(az4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BA5():
    # 'LPG_Monthly'!BA5
    value = 1.09227951742
    formula = "=BA4*'LPG Annual'!$C$6"
    @eval_fn
    def BA5():
        ba4_1 = LPG_Monthly.BA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ba4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BB5():
    # 'LPG_Monthly'!BB5
    value = 1.33690461767
    formula = "=BB4*'LPG Annual'!$C$6"
    @eval_fn
    def BB5():
        bb4_1 = LPG_Monthly.BB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BC5():
    # 'LPG_Monthly'!BC5
    value = 1.4592171678
    formula = "=BC4*'LPG Annual'!$C$6"
    @eval_fn
    def BC5():
        bc4_1 = LPG_Monthly.BC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BD5():
    # 'LPG_Monthly'!BD5
    value = 1.6583306215
    formula = "=BD4*'LPG Annual'!$C$6"
    @eval_fn
    def BD5():
        bd4_1 = LPG_Monthly.BD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BE5():
    # 'LPG_Monthly'!BE5
    value = 1.72944256925
    formula = "=BE4*'LPG Annual'!$C$6"
    @eval_fn
    def BE5():
        be4_1 = LPG_Monthly.BE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(be4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BF5():
    # 'LPG_Monthly'!BF5
    value = 1.34828252931
    formula = "=BF4*'LPG Annual'!$C$6"
    @eval_fn
    def BF5():
        bf4_1 = LPG_Monthly.BF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BG5():
    # 'LPG_Monthly'!BG5
    value = 1.09796847324
    formula = "=BG4*'LPG Annual'!$C$6"
    @eval_fn
    def BG5():
        bg4_1 = LPG_Monthly.BG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BH5():
    # 'LPG_Monthly'!BH5
    value = 1.09512399533
    formula = "=BH4*'LPG Annual'!$C$6"
    @eval_fn
    def BH5():
        bh4_1 = LPG_Monthly.BH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BI5():
    # 'LPG_Monthly'!BI5
    value = 0.992722790571
    formula = "=BI4*'LPG Annual'!$C$6"
    @eval_fn
    def BI5():
        bi4_1 = LPG_Monthly.BI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BJ5():
    # 'LPG_Monthly'!BJ5
    value = 1.00410070221
    formula = "=BJ4*'LPG Annual'!$C$6"
    @eval_fn
    def BJ5():
        bj4_1 = LPG_Monthly.BJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BK5():
    # 'LPG_Monthly'!BK5
    value = 0.978500401021
    formula = "=BK4*'LPG Annual'!$C$6"
    @eval_fn
    def BK5():
        bk4_1 = LPG_Monthly.BK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BL5():
    # 'LPG_Monthly'!BL5
    value = 0.989878312661
    formula = "=BL4*'LPG Annual'!$C$6"
    @eval_fn
    def BL5():
        bl4_1 = LPG_Monthly.BL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BM5():
    # 'LPG_Monthly'!BM5
    value = 1.04961234877
    formula = "=BM4*'LPG Annual'!$C$6"
    @eval_fn
    def BM5():
        bm4_1 = LPG_Monthly.BM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BN5():
    # 'LPG_Monthly'!BN5
    value = 1.10081295115
    formula = "=BN4*'LPG Annual'!$C$6"
    @eval_fn
    def BN5():
        bn4_1 = LPG_Monthly.BN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BO5():
    # 'LPG_Monthly'!BO5
    value = 1.13210220816
    formula = "=BO4*'LPG Annual'!$C$6"
    @eval_fn
    def BO5():
        bo4_1 = LPG_Monthly.BO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BP5():
    # 'LPG_Monthly'!BP5
    value = 1.02401204758
    formula = "=BP4*'LPG Annual'!$C$6"
    @eval_fn
    def BP5():
        bp4_1 = LPG_Monthly.BP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BQ5():
    # 'LPG_Monthly'!BQ5
    value = 0.955744577742
    formula = "=BQ4*'LPG Annual'!$C$6"
    @eval_fn
    def BQ5():
        bq4_1 = LPG_Monthly.BQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BR5():
    # 'LPG_Monthly'!BR5
    value = 0.859032328804
    formula = "=BR4*'LPG Annual'!$C$6"
    @eval_fn
    def BR5():
        br4_1 = LPG_Monthly.BR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(br4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BS5():
    # 'LPG_Monthly'!BS5
    value = 0.847654417164
    formula = "=BS4*'LPG Annual'!$C$6"
    @eval_fn
    def BS5():
        bs4_1 = LPG_Monthly.BS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BT5():
    # 'LPG_Monthly'!BT5
    value = 0.782231425235
    formula = "=BT4*'LPG Annual'!$C$6"
    @eval_fn
    def BT5():
        bt4_1 = LPG_Monthly.BT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BU5():
    # 'LPG_Monthly'!BU5
    value = 0.827743071794
    formula = "=BU4*'LPG Annual'!$C$6"
    @eval_fn
    def BU5():
        bu4_1 = LPG_Monthly.BU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BV5():
    # 'LPG_Monthly'!BV5
    value = 0.779386947325
    formula = "=BV4*'LPG Annual'!$C$6"
    @eval_fn
    def BV5():
        bv4_1 = LPG_Monthly.BV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BW5():
    # 'LPG_Monthly'!BW5
    value = 0.696897087937
    formula = "=BW4*'LPG Annual'!$C$6"
    @eval_fn
    def BW5():
        bw4_1 = LPG_Monthly.BW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BX5():
    # 'LPG_Monthly'!BX5
    value = 0.699741565847
    formula = "=BX4*'LPG Annual'!$C$6"
    @eval_fn
    def BX5():
        bx4_1 = LPG_Monthly.BX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BY5():
    # 'LPG_Monthly'!BY5
    value = 0.685519176297
    formula = "=BY4*'LPG Annual'!$C$6"
    @eval_fn
    def BY5():
        by4_1 = LPG_Monthly.BY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(by4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class BZ5():
    # 'LPG_Monthly'!BZ5
    value = 0.708274999576
    formula = "=BZ4*'LPG Annual'!$C$6"
    @eval_fn
    def BZ5():
        bz4_1 = LPG_Monthly.BZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(bz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CA5():
    # 'LPG_Monthly'!CA5
    value = 0.731030822856
    formula = "=CA4*'LPG Annual'!$C$6"
    @eval_fn
    def CA5():
        ca4_1 = LPG_Monthly.CA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ca4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CB5():
    # 'LPG_Monthly'!CB5
    value = 0.705430521666
    formula = "=CB4*'LPG Annual'!$C$6"
    @eval_fn
    def CB5():
        cb4_1 = LPG_Monthly.CB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CC5():
    # 'LPG_Monthly'!CC5
    value = 0.594495883179
    formula = "=CC4*'LPG Annual'!$C$6"
    @eval_fn
    def CC5():
        cc4_1 = LPG_Monthly.CC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CD5():
    # 'LPG_Monthly'!CD5
    value = 0.617251706458
    formula = "=CD4*'LPG Annual'!$C$6"
    @eval_fn
    def CD5():
        cd4_1 = LPG_Monthly.CD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CE5():
    # 'LPG_Monthly'!CE5
    value = 0.637163051828
    formula = "=CE4*'LPG Annual'!$C$6"
    @eval_fn
    def CE5():
        ce4_1 = LPG_Monthly.CE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ce4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CF5():
    # 'LPG_Monthly'!CF5
    value = 0.688363654207
    formula = "=CF4*'LPG Annual'!$C$6"
    @eval_fn
    def CF5():
        cf4_1 = LPG_Monthly.CF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CG5():
    # 'LPG_Monthly'!CG5
    value = 0.802142770605
    formula = "=CG4*'LPG Annual'!$C$6"
    @eval_fn
    def CG5():
        cg4_1 = LPG_Monthly.CG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CH5():
    # 'LPG_Monthly'!CH5
    value = 0.804987248515
    formula = "=CH4*'LPG Annual'!$C$6"
    @eval_fn
    def CH5():
        ch4_1 = LPG_Monthly.CH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ch4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CI5():
    # 'LPG_Monthly'!CI5
    value = 0.878943674173
    formula = "=CI4*'LPG Annual'!$C$6"
    @eval_fn
    def CI5():
        ci4_1 = LPG_Monthly.CI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ci4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CJ5():
    # 'LPG_Monthly'!CJ5
    value = 1.0581457825
    formula = "=CJ4*'LPG Annual'!$C$6"
    @eval_fn
    def CJ5():
        cj4_1 = LPG_Monthly.CJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CK5():
    # 'LPG_Monthly'!CK5
    value = 1.15485803144
    formula = "=CK4*'LPG Annual'!$C$6"
    @eval_fn
    def CK5():
        ck4_1 = LPG_Monthly.CK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ck4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CL5():
    # 'LPG_Monthly'!CL5
    value = 1.2288144571
    formula = "=CL4*'LPG Annual'!$C$6"
    @eval_fn
    def CL5():
        cl4_1 = LPG_Monthly.CL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CM5():
    # 'LPG_Monthly'!CM5
    value = 1.29139297112
    formula = "=CM4*'LPG Annual'!$C$6"
    @eval_fn
    def CM5():
        cm4_1 = LPG_Monthly.CM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CN5():
    # 'LPG_Monthly'!CN5
    value = 1.24019236874
    formula = "=CN4*'LPG Annual'!$C$6"
    @eval_fn
    def CN5():
        cn4_1 = LPG_Monthly.CN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CO5():
    # 'LPG_Monthly'!CO5
    value = 1.21743654546
    formula = "=CO4*'LPG Annual'!$C$6"
    @eval_fn
    def CO5():
        co4_1 = LPG_Monthly.CO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(co4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CP5():
    # 'LPG_Monthly'!CP5
    value = 1.57868524002
    formula = "=CP4*'LPG Annual'!$C$6"
    @eval_fn
    def CP5():
        cp4_1 = LPG_Monthly.CP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CQ5():
    # 'LPG_Monthly'!CQ5
    value = 1.69530883433
    formula = "=CQ4*'LPG Annual'!$C$6"
    @eval_fn
    def CQ5():
        cq4_1 = LPG_Monthly.CQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CR5():
    # 'LPG_Monthly'!CR5
    value = 1.45637268989
    formula = "=CR4*'LPG Annual'!$C$6"
    @eval_fn
    def CR5():
        cr4_1 = LPG_Monthly.CR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CS5():
    # 'LPG_Monthly'!CS5
    value = 1.33406013976
    formula = "=CS4*'LPG Annual'!$C$6"
    @eval_fn
    def CS5():
        cs4_1 = LPG_Monthly.CS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CT5():
    # 'LPG_Monthly'!CT5
    value = 1.45637268989
    formula = "=CT4*'LPG Annual'!$C$6"
    @eval_fn
    def CT5():
        ct4_1 = LPG_Monthly.CT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ct4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CU5():
    # 'LPG_Monthly'!CU5
    value = 1.57868524002
    formula = "=CU4*'LPG Annual'!$C$6"
    @eval_fn
    def CU5():
        cu4_1 = LPG_Monthly.CU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CV5():
    # 'LPG_Monthly'!CV5
    value = 1.56730732838
    formula = "=CV4*'LPG Annual'!$C$6"
    @eval_fn
    def CV5():
        cv4_1 = LPG_Monthly.CV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CW5():
    # 'LPG_Monthly'!CW5
    value = 1.6583306215
    formula = "=CW4*'LPG Annual'!$C$6"
    @eval_fn
    def CW5():
        cw4_1 = LPG_Monthly.CW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CX5():
    # 'LPG_Monthly'!CX5
    value = 1.82899929609
    formula = "=CX4*'LPG Annual'!$C$6"
    @eval_fn
    def CX5():
        cx4_1 = LPG_Monthly.CX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CY5():
    # 'LPG_Monthly'!CY5
    value = 1.76357630417
    formula = "=CY4*'LPG Annual'!$C$6"
    @eval_fn
    def CY5():
        cy4_1 = LPG_Monthly.CY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class CZ5():
    # 'LPG_Monthly'!CZ5
    value = 1.72944256925
    formula = "=CZ4*'LPG Annual'!$C$6"
    @eval_fn
    def CZ5():
        cz4_1 = LPG_Monthly.CZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(cz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DA5():
    # 'LPG_Monthly'!DA5
    value = 2.20447038021
    formula = "=DA4*'LPG Annual'!$C$6"
    @eval_fn
    def DA5():
        da4_1 = LPG_Monthly.DA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(da4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DB5():
    # 'LPG_Monthly'!DB5
    value = 2.2016259023
    formula = "=DB4*'LPG Annual'!$C$6"
    @eval_fn
    def DB5():
        db4_1 = LPG_Monthly.DB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(db4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DC5():
    # 'LPG_Monthly'!DC5
    value = 1.6867754006
    formula = "=DC4*'LPG Annual'!$C$6"
    @eval_fn
    def DC5():
        dc4_1 = LPG_Monthly.DC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DD5():
    # 'LPG_Monthly'!DD5
    value = 1.58721867375
    formula = "=DD4*'LPG Annual'!$C$6"
    @eval_fn
    def DD5():
        dd4_1 = LPG_Monthly.DD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DE5():
    # 'LPG_Monthly'!DE5
    value = 1.55592941674
    formula = "=DE4*'LPG Annual'!$C$6"
    @eval_fn
    def DE5():
        de4_1 = LPG_Monthly.DE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(de4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DF5():
    # 'LPG_Monthly'!DF5
    value = 1.4592171678
    formula = "=DF4*'LPG Annual'!$C$6"
    @eval_fn
    def DF5():
        df4_1 = LPG_Monthly.DF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(df4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DG5():
    # 'LPG_Monthly'!DG5
    value = 1.22596997919
    formula = "=DG4*'LPG Annual'!$C$6"
    @eval_fn
    def DG5():
        dg4_1 = LPG_Monthly.DG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DH5():
    # 'LPG_Monthly'!DH5
    value = 1.10934638488
    formula = "=DH4*'LPG Annual'!$C$6"
    @eval_fn
    def DH5():
        dh4_1 = LPG_Monthly.DH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DI5():
    # 'LPG_Monthly'!DI5
    value = 1.18045833263
    formula = "=DI4*'LPG Annual'!$C$6"
    @eval_fn
    def DI5():
        di4_1 = LPG_Monthly.DI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(di4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DJ5():
    # 'LPG_Monthly'!DJ5
    value = 1.19752520009
    formula = "=DJ4*'LPG Annual'!$C$6"
    @eval_fn
    def DJ5():
        dj4_1 = LPG_Monthly.DJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DK5():
    # 'LPG_Monthly'!DK5
    value = 1.12356877443
    formula = "=DK4*'LPG Annual'!$C$6"
    @eval_fn
    def DK5():
        dk4_1 = LPG_Monthly.DK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DL5():
    # 'LPG_Monthly'!DL5
    value = 0.941522188192
    formula = "=DL4*'LPG Annual'!$C$6"
    @eval_fn
    def DL5():
        dl4_1 = LPG_Monthly.DL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DM5():
    # 'LPG_Monthly'!DM5
    value = 0.856187850894
    formula = "=DM4*'LPG Annual'!$C$6"
    @eval_fn
    def DM5():
        dm4_1 = LPG_Monthly.DM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DN5():
    # 'LPG_Monthly'!DN5
    value = 0.827743071794
    formula = "=DN4*'LPG Annual'!$C$6"
    @eval_fn
    def DN5():
        dn4_1 = LPG_Monthly.DN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DO5():
    # 'LPG_Monthly'!DO5
    value = 0.890321585813
    formula = "=DO4*'LPG Annual'!$C$6"
    @eval_fn
    def DO5():
        do4_1 = LPG_Monthly.DO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(do4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DP5():
    # 'LPG_Monthly'!DP5
    value = 1.08090160578
    formula = "=DP4*'LPG Annual'!$C$6"
    @eval_fn
    def DP5():
        dp4_1 = LPG_Monthly.DP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DQ5():
    # 'LPG_Monthly'!DQ5
    value = 1.18045833263
    formula = "=DQ4*'LPG Annual'!$C$6"
    @eval_fn
    def DQ5():
        dq4_1 = LPG_Monthly.DQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DR5():
    # 'LPG_Monthly'!DR5
    value = 1.15485803144
    formula = "=DR4*'LPG Annual'!$C$6"
    @eval_fn
    def DR5():
        dr4_1 = LPG_Monthly.DR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DS5():
    # 'LPG_Monthly'!DS5
    value = 1.06667921623
    formula = "=DS4*'LPG Annual'!$C$6"
    @eval_fn
    def DS5():
        ds4_1 = LPG_Monthly.DS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ds4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DT5():
    # 'LPG_Monthly'!DT5
    value = 1.0581457825
    formula = "=DT4*'LPG Annual'!$C$6"
    @eval_fn
    def DT5():
        dt4_1 = LPG_Monthly.DT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DU5():
    # 'LPG_Monthly'!DU5
    value = 1.18045833263
    formula = "=DU4*'LPG Annual'!$C$6"
    @eval_fn
    def DU5():
        du4_1 = LPG_Monthly.DU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(du4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DV5():
    # 'LPG_Monthly'!DV5
    value = 1.33974909558
    formula = "=DV4*'LPG Annual'!$C$6"
    @eval_fn
    def DV5():
        dv4_1 = LPG_Monthly.DV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DW5():
    # 'LPG_Monthly'!DW5
    value = 1.36250491886
    formula = "=DW4*'LPG Annual'!$C$6"
    @eval_fn
    def DW5():
        dw4_1 = LPG_Monthly.DW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DX5():
    # 'LPG_Monthly'!DX5
    value = 1.34259357349
    formula = "=DX4*'LPG Annual'!$C$6"
    @eval_fn
    def DX5():
        dx4_1 = LPG_Monthly.DX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DY5():
    # 'LPG_Monthly'!DY5
    value = 1.4876619469
    formula = "=DY4*'LPG Annual'!$C$6"
    @eval_fn
    def DY5():
        dy4_1 = LPG_Monthly.DY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class DZ5():
    # 'LPG_Monthly'!DZ5
    value = 1.72375361343
    formula = "=DZ4*'LPG Annual'!$C$6"
    @eval_fn
    def DZ5():
        dz4_1 = LPG_Monthly.DZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(dz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EA5():
    # 'LPG_Monthly'!EA5
    value = 2.20447038021
    formula = "=EA4*'LPG Annual'!$C$6"
    @eval_fn
    def EA5():
        ea4_1 = LPG_Monthly.EA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ea4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EB5():
    # 'LPG_Monthly'!EB5
    value = 1.7721097379
    formula = "=EB4*'LPG Annual'!$C$6"
    @eval_fn
    def EB5():
        eb4_1 = LPG_Monthly.EB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EC5():
    # 'LPG_Monthly'!EC5
    value = 1.43361686661
    formula = "=EC4*'LPG Annual'!$C$6"
    @eval_fn
    def EC5():
        ec4_1 = LPG_Monthly.EC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ec4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ED5():
    # 'LPG_Monthly'!ED5
    value = 1.53886254928
    formula = "=ED4*'LPG Annual'!$C$6"
    @eval_fn
    def ED5():
        ed4_1 = LPG_Monthly.ED4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ed4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EE5():
    # 'LPG_Monthly'!EE5
    value = 1.59006315166
    formula = "=EE4*'LPG Annual'!$C$6"
    @eval_fn
    def EE5():
        ee4_1 = LPG_Monthly.EE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ee4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EF5():
    # 'LPG_Monthly'!EF5
    value = 1.50757329227
    formula = "=EF4*'LPG Annual'!$C$6"
    @eval_fn
    def EF5():
        ef4_1 = LPG_Monthly.EF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ef4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EG5():
    # 'LPG_Monthly'!EG5
    value = 1.55877389465
    formula = "=EG4*'LPG Annual'!$C$6"
    @eval_fn
    def EG5():
        eg4_1 = LPG_Monthly.EG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EH5():
    # 'LPG_Monthly'!EH5
    value = 1.47628403526
    formula = "=EH4*'LPG Annual'!$C$6"
    @eval_fn
    def EH5():
        eh4_1 = LPG_Monthly.EH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EI5():
    # 'LPG_Monthly'!EI5
    value = 1.5729962842
    formula = "=EI4*'LPG Annual'!$C$6"
    @eval_fn
    def EI5():
        ei4_1 = LPG_Monthly.EI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ei4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EJ5():
    # 'LPG_Monthly'!EJ5
    value = 1.55592941674
    formula = "=EJ4*'LPG Annual'!$C$6"
    @eval_fn
    def EJ5():
        ej4_1 = LPG_Monthly.EJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ej4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EK5():
    # 'LPG_Monthly'!EK5
    value = 1.78633212745
    formula = "=EK4*'LPG Annual'!$C$6"
    @eval_fn
    def EK5():
        ek4_1 = LPG_Monthly.EK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ek4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EL5():
    # 'LPG_Monthly'!EL5
    value = 2.11913604291
    formula = "=EL4*'LPG Annual'!$C$6"
    @eval_fn
    def EL5():
        el4_1 = LPG_Monthly.EL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(el4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EM5():
    # 'LPG_Monthly'!EM5
    value = 2.0025124486
    formula = "=EM4*'LPG Annual'!$C$6"
    @eval_fn
    def EM5():
        em4_1 = LPG_Monthly.EM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(em4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EN5():
    # 'LPG_Monthly'!EN5
    value = 1.66401957732
    formula = "=EN4*'LPG Annual'!$C$6"
    @eval_fn
    def EN5():
        en4_1 = LPG_Monthly.EN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(en4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EO5():
    # 'LPG_Monthly'!EO5
    value = 1.72659809134
    formula = "=EO4*'LPG Annual'!$C$6"
    @eval_fn
    def EO5():
        eo4_1 = LPG_Monthly.EO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EP5():
    # 'LPG_Monthly'!EP5
    value = 1.92571154503
    formula = "=EP4*'LPG Annual'!$C$6"
    @eval_fn
    def EP5():
        ep4_1 = LPG_Monthly.EP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ep4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EQ5():
    # 'LPG_Monthly'!EQ5
    value = 1.90580019966
    formula = "=EQ4*'LPG Annual'!$C$6"
    @eval_fn
    def EQ5():
        eq4_1 = LPG_Monthly.EQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ER5():
    # 'LPG_Monthly'!ER5
    value = 2.10775813127
    formula = "=ER4*'LPG Annual'!$C$6"
    @eval_fn
    def ER5():
        er4_1 = LPG_Monthly.ER4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(er4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ES5():
    # 'LPG_Monthly'!ES5
    value = 2.38082801062
    formula = "=ES4*'LPG Annual'!$C$6"
    @eval_fn
    def ES5():
        es4_1 = LPG_Monthly.ES4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(es4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ET5():
    # 'LPG_Monthly'!ET5
    value = 2.28127128378
    formula = "=ET4*'LPG Annual'!$C$6"
    @eval_fn
    def ET5():
        et4_1 = LPG_Monthly.ET4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(et4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EU5():
    # 'LPG_Monthly'!EU5
    value = 2.57709698641
    formula = "=EU4*'LPG Annual'!$C$6"
    @eval_fn
    def EU5():
        eu4_1 = LPG_Monthly.EU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(eu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EV5():
    # 'LPG_Monthly'!EV5
    value = 2.45478443628
    formula = "=EV4*'LPG Annual'!$C$6"
    @eval_fn
    def EV5():
        ev4_1 = LPG_Monthly.EV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ev4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EW5():
    # 'LPG_Monthly'!EW5
    value = 2.2016259023
    formula = "=EW4*'LPG Annual'!$C$6"
    @eval_fn
    def EW5():
        ew4_1 = LPG_Monthly.EW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ew4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EX5():
    # 'LPG_Monthly'!EX5
    value = 2.09638021963
    formula = "=EX4*'LPG Annual'!$C$6"
    @eval_fn
    def EX5():
        ex4_1 = LPG_Monthly.EX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ex4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EY5():
    # 'LPG_Monthly'!EY5
    value = 2.15611425574
    formula = "=EY4*'LPG Annual'!$C$6"
    @eval_fn
    def EY5():
        ey4_1 = LPG_Monthly.EY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ey4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class EZ5():
    # 'LPG_Monthly'!EZ5
    value = 2.49745160493
    formula = "=EZ4*'LPG Annual'!$C$6"
    @eval_fn
    def EZ5():
        ez4_1 = LPG_Monthly.EZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ez4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FA5():
    # 'LPG_Monthly'!FA5
    value = 2.42918413509
    formula = "=FA4*'LPG Annual'!$C$6"
    @eval_fn
    def FA5():
        fa4_1 = LPG_Monthly.FA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fa4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FB5():
    # 'LPG_Monthly'!FB5
    value = 2.26704889423
    formula = "=FB4*'LPG Annual'!$C$6"
    @eval_fn
    def FB5():
        fb4_1 = LPG_Monthly.FB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FC5():
    # 'LPG_Monthly'!FC5
    value = 2.32678293034
    formula = "=FC4*'LPG Annual'!$C$6"
    @eval_fn
    def FC5():
        fc4_1 = LPG_Monthly.FC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FD5():
    # 'LPG_Monthly'!FD5
    value = 2.4035838339
    formula = "=FD4*'LPG Annual'!$C$6"
    @eval_fn
    def FD5():
        fd4_1 = LPG_Monthly.FD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FE5():
    # 'LPG_Monthly'!FE5
    value = 2.67665371326
    formula = "=FE4*'LPG Annual'!$C$6"
    @eval_fn
    def FE5():
        fe4_1 = LPG_Monthly.FE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fe4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FF5():
    # 'LPG_Monthly'!FF5
    value = 3.21426003824
    formula = "=FF4*'LPG Annual'!$C$6"
    @eval_fn
    def FF5():
        ff4_1 = LPG_Monthly.FF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ff4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FG5():
    # 'LPG_Monthly'!FG5
    value = 3.23417138361
    formula = "=FG4*'LPG Annual'!$C$6"
    @eval_fn
    def FG5():
        fg4_1 = LPG_Monthly.FG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FH5():
    # 'LPG_Monthly'!FH5
    value = 2.84163343204
    formula = "=FH4*'LPG Annual'!$C$6"
    @eval_fn
    def FH5():
        fh4_1 = LPG_Monthly.FH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FI5():
    # 'LPG_Monthly'!FI5
    value = 3.0037686729
    formula = "=FI4*'LPG Annual'!$C$6"
    @eval_fn
    def FI5():
        fi4_1 = LPG_Monthly.FI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FJ5():
    # 'LPG_Monthly'!FJ5
    value = 2.81318865294
    formula = "=FJ4*'LPG Annual'!$C$6"
    @eval_fn
    def FJ5():
        fj4_1 = LPG_Monthly.FJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FK5():
    # 'LPG_Monthly'!FK5
    value = 2.61407519924
    formula = "=FK4*'LPG Annual'!$C$6"
    @eval_fn
    def FK5():
        fk4_1 = LPG_Monthly.FK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FL5():
    # 'LPG_Monthly'!FL5
    value = 2.63398654461
    formula = "=FL4*'LPG Annual'!$C$6"
    @eval_fn
    def FL5():
        fl4_1 = LPG_Monthly.FL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FM5():
    # 'LPG_Monthly'!FM5
    value = 2.8899895565
    formula = "=FM4*'LPG Annual'!$C$6"
    @eval_fn
    def FM5():
        fm4_1 = LPG_Monthly.FM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FN5():
    # 'LPG_Monthly'!FN5
    value = 2.96110150425
    formula = "=FN4*'LPG Annual'!$C$6"
    @eval_fn
    def FN5():
        fn4_1 = LPG_Monthly.FN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FO5():
    # 'LPG_Monthly'!FO5
    value = 3.12039226721
    formula = "=FO4*'LPG Annual'!$C$6"
    @eval_fn
    def FO5():
        fo4_1 = LPG_Monthly.FO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FP5():
    # 'LPG_Monthly'!FP5
    value = 3.31381676509
    formula = "=FP4*'LPG Annual'!$C$6"
    @eval_fn
    def FP5():
        fp4_1 = LPG_Monthly.FP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FQ5():
    # 'LPG_Monthly'!FQ5
    value = 3.23701586152
    formula = "=FQ4*'LPG Annual'!$C$6"
    @eval_fn
    def FQ5():
        fq4_1 = LPG_Monthly.FQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FR5():
    # 'LPG_Monthly'!FR5
    value = 2.87861164486
    formula = "=FR4*'LPG Annual'!$C$6"
    @eval_fn
    def FR5():
        fr4_1 = LPG_Monthly.FR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FS5():
    # 'LPG_Monthly'!FS5
    value = 2.66812027953
    formula = "=FS4*'LPG Annual'!$C$6"
    @eval_fn
    def FS5():
        fs4_1 = LPG_Monthly.FS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FT5():
    # 'LPG_Monthly'!FT5
    value = 2.71363192609
    formula = "=FT4*'LPG Annual'!$C$6"
    @eval_fn
    def FT5():
        ft4_1 = LPG_Monthly.FT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ft4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FU5():
    # 'LPG_Monthly'!FU5
    value = 2.74776566101
    formula = "=FU4*'LPG Annual'!$C$6"
    @eval_fn
    def FU5():
        fu4_1 = LPG_Monthly.FU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FV5():
    # 'LPG_Monthly'!FV5
    value = 2.54011877358
    formula = "=FV4*'LPG Annual'!$C$6"
    @eval_fn
    def FV5():
        fv4_1 = LPG_Monthly.FV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FW5():
    # 'LPG_Monthly'!FW5
    value = 2.7733659622
    formula = "=FW4*'LPG Annual'!$C$6"
    @eval_fn
    def FW5():
        fw4_1 = LPG_Monthly.FW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FX5():
    # 'LPG_Monthly'!FX5
    value = 2.94972359261
    formula = "=FX4*'LPG Annual'!$C$6"
    @eval_fn
    def FX5():
        fx4_1 = LPG_Monthly.FX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FY5():
    # 'LPG_Monthly'!FY5
    value = 3.15168152422
    formula = "=FY4*'LPG Annual'!$C$6"
    @eval_fn
    def FY5():
        fy4_1 = LPG_Monthly.FY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class FZ5():
    # 'LPG_Monthly'!FZ5
    value = 3.26830511853
    formula = "=FZ4*'LPG Annual'!$C$6"
    @eval_fn
    def FZ5():
        fz4_1 = LPG_Monthly.FZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(fz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GA5():
    # 'LPG_Monthly'!GA5
    value = 3.23986033943
    formula = "=GA4*'LPG Annual'!$C$6"
    @eval_fn
    def GA5():
        ga4_1 = LPG_Monthly.GA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ga4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GB5():
    # 'LPG_Monthly'!GB5
    value = 3.38492871284
    formula = "=GB4*'LPG Annual'!$C$6"
    @eval_fn
    def GB5():
        gb4_1 = LPG_Monthly.GB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GC5():
    # 'LPG_Monthly'!GC5
    value = 3.3735508012
    formula = "=GC4*'LPG Annual'!$C$6"
    @eval_fn
    def GC5():
        gc4_1 = LPG_Monthly.GC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GD5():
    # 'LPG_Monthly'!GD5
    value = 3.68359889338
    formula = "=GD4*'LPG Annual'!$C$6"
    @eval_fn
    def GD5():
        gd4_1 = LPG_Monthly.GD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GE5():
    # 'LPG_Monthly'!GE5
    value = 4.07329236704
    formula = "=GE4*'LPG Annual'!$C$6"
    @eval_fn
    def GE5():
        ge4_1 = LPG_Monthly.GE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ge4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GF5():
    # 'LPG_Monthly'!GF5
    value = 4.42600762788
    formula = "=GF4*'LPG Annual'!$C$6"
    @eval_fn
    def GF5():
        gf4_1 = LPG_Monthly.GF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GG5():
    # 'LPG_Monthly'!GG5
    value = 4.34920672431
    formula = "=GG4*'LPG Annual'!$C$6"
    @eval_fn
    def GG5():
        gg4_1 = LPG_Monthly.GG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GH5():
    # 'LPG_Monthly'!GH5
    value = 4.28378373238
    formula = "=GH4*'LPG Annual'!$C$6"
    @eval_fn
    def GH5():
        gh4_1 = LPG_Monthly.GH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GI5():
    # 'LPG_Monthly'!GI5
    value = 4.05338102167
    formula = "=GI4*'LPG Annual'!$C$6"
    @eval_fn
    def GI5():
        gi4_1 = LPG_Monthly.GI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GJ5():
    # 'LPG_Monthly'!GJ5
    value = 4.19560491717
    formula = "=GJ4*'LPG Annual'!$C$6"
    @eval_fn
    def GJ5():
        gj4_1 = LPG_Monthly.GJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GK5():
    # 'LPG_Monthly'!GK5
    value = 4.52271987681
    formula = "=GK4*'LPG Annual'!$C$6"
    @eval_fn
    def GK5():
        gk4_1 = LPG_Monthly.GK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GL5():
    # 'LPG_Monthly'!GL5
    value = 4.83561244691
    formula = "=GL4*'LPG Annual'!$C$6"
    @eval_fn
    def GL5():
        gl4_1 = LPG_Monthly.GL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GM5():
    # 'LPG_Monthly'!GM5
    value = 5.15703845073
    formula = "=GM4*'LPG Annual'!$C$6"
    @eval_fn
    def GM5():
        gm4_1 = LPG_Monthly.GM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GN5():
    # 'LPG_Monthly'!GN5
    value = 5.29641786832
    formula = "=GN4*'LPG Annual'!$C$6"
    @eval_fn
    def GN5():
        gn4_1 = LPG_Monthly.GN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GO5():
    # 'LPG_Monthly'!GO5
    value = 4.69623302932
    formula = "=GO4*'LPG Annual'!$C$6"
    @eval_fn
    def GO5():
        go4_1 = LPG_Monthly.GO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(go4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GP5():
    # 'LPG_Monthly'!GP5
    value = 4.35205120222
    formula = "=GP4*'LPG Annual'!$C$6"
    @eval_fn
    def GP5():
        gp4_1 = LPG_Monthly.GP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GQ5():
    # 'LPG_Monthly'!GQ5
    value = 2.97247941589
    formula = "=GQ4*'LPG Annual'!$C$6"
    @eval_fn
    def GQ5():
        gq4_1 = LPG_Monthly.GQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GR5():
    # 'LPG_Monthly'!GR5
    value = 2.09922469754
    formula = "=GR4*'LPG Annual'!$C$6"
    @eval_fn
    def GR5():
        gr4_1 = LPG_Monthly.GR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GS5():
    # 'LPG_Monthly'!GS5
    value = 1.73513152507
    formula = "=GS4*'LPG Annual'!$C$6"
    @eval_fn
    def GS5():
        gs4_1 = LPG_Monthly.GS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GT5():
    # 'LPG_Monthly'!GT5
    value = 2.06793544053
    formula = "=GT4*'LPG Annual'!$C$6"
    @eval_fn
    def GT5():
        gt4_1 = LPG_Monthly.GT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GU5():
    # 'LPG_Monthly'!GU5
    value = 1.87451094265
    formula = "=GU4*'LPG Annual'!$C$6"
    @eval_fn
    def GU5():
        gu4_1 = LPG_Monthly.GU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GV5():
    # 'LPG_Monthly'!GV5
    value = 1.85744407519
    formula = "=GV4*'LPG Annual'!$C$6"
    @eval_fn
    def GV5():
        gv4_1 = LPG_Monthly.GV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GW5():
    # 'LPG_Monthly'!GW5
    value = 1.81477690655
    formula = "=GW4*'LPG Annual'!$C$6"
    @eval_fn
    def GW5():
        gw4_1 = LPG_Monthly.GW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GX5():
    # 'LPG_Monthly'!GX5
    value = 1.99397901487
    formula = "=GX4*'LPG Annual'!$C$6"
    @eval_fn
    def GX5():
        gx4_1 = LPG_Monthly.GX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GY5():
    # 'LPG_Monthly'!GY5
    value = 2.40642831181
    formula = "=GY4*'LPG Annual'!$C$6"
    @eval_fn
    def GY5():
        gy4_1 = LPG_Monthly.GY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class GZ5():
    # 'LPG_Monthly'!GZ5
    value = 2.13904738828
    formula = "=GZ4*'LPG Annual'!$C$6"
    @eval_fn
    def GZ5():
        gz4_1 = LPG_Monthly.GZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(gz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HA5():
    # 'LPG_Monthly'!HA5
    value = 2.57709698641
    formula = "=HA4*'LPG Annual'!$C$6"
    @eval_fn
    def HA5():
        ha4_1 = LPG_Monthly.HA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ha4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HB5():
    # 'LPG_Monthly'!HB5
    value = 2.69087610281
    formula = "=HB4*'LPG Annual'!$C$6"
    @eval_fn
    def HB5():
        hb4_1 = LPG_Monthly.HB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HC5():
    # 'LPG_Monthly'!HC5
    value = 2.86723373323
    formula = "=HC4*'LPG Annual'!$C$6"
    @eval_fn
    def HC5():
        hc4_1 = LPG_Monthly.HC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HD5():
    # 'LPG_Monthly'!HD5
    value = 3.0606582311
    formula = "=HD4*'LPG Annual'!$C$6"
    @eval_fn
    def HD5():
        hd4_1 = LPG_Monthly.HD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HE5():
    # 'LPG_Monthly'!HE5
    value = 3.38492871284
    formula = "=HE4*'LPG Annual'!$C$6"
    @eval_fn
    def HE5():
        he4_1 = LPG_Monthly.HE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(he4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HF5():
    # 'LPG_Monthly'!HF5
    value = 3.73195501785
    formula = "=HF4*'LPG Annual'!$C$6"
    @eval_fn
    def HF5():
        hf4_1 = LPG_Monthly.HF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HG5():
    # 'LPG_Monthly'!HG5
    value = 3.65230963637
    formula = "=HG4*'LPG Annual'!$C$6"
    @eval_fn
    def HG5():
        hg4_1 = LPG_Monthly.HG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HH5():
    # 'LPG_Monthly'!HH5
    value = 3.2313269057
    formula = "=HH4*'LPG Annual'!$C$6"
    @eval_fn
    def HH5():
        hh4_1 = LPG_Monthly.HH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HI5():
    # 'LPG_Monthly'!HI5
    value = 3.23417138361
    formula = "=HI4*'LPG Annual'!$C$6"
    @eval_fn
    def HI5():
        hi4_1 = LPG_Monthly.HI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HJ5():
    # 'LPG_Monthly'!HJ5
    value = 3.07772509856
    formula = "=HJ4*'LPG Annual'!$C$6"
    @eval_fn
    def HJ5():
        hj4_1 = LPG_Monthly.HJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HK5():
    # 'LPG_Monthly'!HK5
    value = 2.94972359261
    formula = "=HK4*'LPG Annual'!$C$6"
    @eval_fn
    def HK5():
        hk4_1 = LPG_Monthly.HK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HL5():
    # 'LPG_Monthly'!HL5
    value = 2.87292268904
    formula = "=HL4*'LPG Annual'!$C$6"
    @eval_fn
    def HL5():
        hl4_1 = LPG_Monthly.HL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HM5():
    # 'LPG_Monthly'!HM5
    value = 3.04928031946
    formula = "=HM4*'LPG Annual'!$C$6"
    @eval_fn
    def HM5():
        hm4_1 = LPG_Monthly.HM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HN5():
    # 'LPG_Monthly'!HN5
    value = 3.21994899406
    formula = "=HN4*'LPG Annual'!$C$6"
    @eval_fn
    def HN5():
        hn4_1 = LPG_Monthly.HN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HO5():
    # 'LPG_Monthly'!HO5
    value = 3.51008574087
    formula = "=HO4*'LPG Annual'!$C$6"
    @eval_fn
    def HO5():
        ho4_1 = LPG_Monthly.HO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ho4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HP5():
    # 'LPG_Monthly'!HP5
    value = 3.56697529907
    formula = "=HP4*'LPG Annual'!$C$6"
    @eval_fn
    def HP5():
        hp4_1 = LPG_Monthly.HP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HQ5():
    # 'LPG_Monthly'!HQ5
    value = 3.68644337129
    formula = "=HQ4*'LPG Annual'!$C$6"
    @eval_fn
    def HQ5():
        hq4_1 = LPG_Monthly.HQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HR5():
    # 'LPG_Monthly'!HR5
    value = 3.83435622261
    formula = "=HR4*'LPG Annual'!$C$6"
    @eval_fn
    def HR5():
        hr4_1 = LPG_Monthly.HR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HS5():
    # 'LPG_Monthly'!HS5
    value = 3.92253503781
    formula = "=HS4*'LPG Annual'!$C$6"
    @eval_fn
    def HS5():
        hs4_1 = LPG_Monthly.HS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HT5():
    # 'LPG_Monthly'!HT5
    value = 3.97373564019
    formula = "=HT4*'LPG Annual'!$C$6"
    @eval_fn
    def HT5():
        ht4_1 = LPG_Monthly.HT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ht4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HU5():
    # 'LPG_Monthly'!HU5
    value = 4.13587088106
    formula = "=HU4*'LPG Annual'!$C$6"
    @eval_fn
    def HU5():
        hu4_1 = LPG_Monthly.HU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HV5():
    # 'LPG_Monthly'!HV5
    value = 4.32645090103
    formula = "=HV4*'LPG Annual'!$C$6"
    @eval_fn
    def HV5():
        hv4_1 = LPG_Monthly.HV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HW5():
    # 'LPG_Monthly'!HW5
    value = 4.32360642312
    formula = "=HW4*'LPG Annual'!$C$6"
    @eval_fn
    def HW5():
        hw4_1 = LPG_Monthly.HW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HX5():
    # 'LPG_Monthly'!HX5
    value = 4.3463622464
    formula = "=HX4*'LPG Annual'!$C$6"
    @eval_fn
    def HX5():
        hx4_1 = LPG_Monthly.HX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HY5():
    # 'LPG_Monthly'!HY5
    value = 4.3463622464
    formula = "=HY4*'LPG Annual'!$C$6"
    @eval_fn
    def HY5():
        hy4_1 = LPG_Monthly.HY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class HZ5():
    # 'LPG_Monthly'!HZ5
    value = 4.43738553951
    formula = "=HZ4*'LPG Annual'!$C$6"
    @eval_fn
    def HZ5():
        hz4_1 = LPG_Monthly.HZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(hz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IA5():
    # 'LPG_Monthly'!IA5
    value = 4.18707148344
    formula = "=IA4*'LPG Annual'!$C$6"
    @eval_fn
    def IA5():
        ia4_1 = LPG_Monthly.IA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ia4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IB5():
    # 'LPG_Monthly'!IB5
    value = 4.1472487927
    formula = "=IB4*'LPG Annual'!$C$6"
    @eval_fn
    def IB5():
        ib4_1 = LPG_Monthly.IB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ib4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IC5():
    # 'LPG_Monthly'!IC5
    value = 3.96804668437
    formula = "=IC4*'LPG Annual'!$C$6"
    @eval_fn
    def IC5():
        ic4_1 = LPG_Monthly.IC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ic4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ID5():
    # 'LPG_Monthly'!ID5
    value = 3.68075441547
    formula = "=ID4*'LPG Annual'!$C$6"
    @eval_fn
    def ID5():
        id4_1 = LPG_Monthly.ID4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(id4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IE5():
    # 'LPG_Monthly'!IE5
    value = 3.47026305013
    formula = "=IE4*'LPG Annual'!$C$6"
    @eval_fn
    def IE5():
        ie4_1 = LPG_Monthly.IE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ie4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IF5():
    # 'LPG_Monthly'!IF5
    value = 3.58688664444
    formula = "=IF4*'LPG Annual'!$C$6"
    @eval_fn
    def IF5():
        if4_1 = LPG_Monthly.IF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(if4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IG5():
    # 'LPG_Monthly'!IG5
    value = 3.40199558029
    formula = "=IG4*'LPG Annual'!$C$6"
    @eval_fn
    def IG5():
        ig4_1 = LPG_Monthly.IG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ig4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IH5():
    # 'LPG_Monthly'!IH5
    value = 2.71363192609
    formula = "=IH4*'LPG Annual'!$C$6"
    @eval_fn
    def IH5():
        ih4_1 = LPG_Monthly.IH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ih4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class II5():
    # 'LPG_Monthly'!II5
    value = 2.24144859304
    formula = "=II4*'LPG Annual'!$C$6"
    @eval_fn
    def II5():
        ii4_1 = LPG_Monthly.II4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ii4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IJ5():
    # 'LPG_Monthly'!IJ5
    value = 2.48607369329
    formula = "=IJ4*'LPG Annual'!$C$6"
    @eval_fn
    def IJ5():
        ij4_1 = LPG_Monthly.IJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ij4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IK5():
    # 'LPG_Monthly'!IK5
    value = 2.56287459686
    formula = "=IK4*'LPG Annual'!$C$6"
    @eval_fn
    def IK5():
        ik4_1 = LPG_Monthly.IK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ik4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IL5():
    # 'LPG_Monthly'!IL5
    value = 2.58847489805
    formula = "=IL4*'LPG Annual'!$C$6"
    @eval_fn
    def IL5():
        il4_1 = LPG_Monthly.IL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(il4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IM5():
    # 'LPG_Monthly'!IM5
    value = 2.73638774937
    formula = "=IM4*'LPG Annual'!$C$6"
    @eval_fn
    def IM5():
        im4_1 = LPG_Monthly.IM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(im4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IN5():
    # 'LPG_Monthly'!IN5
    value = 2.53158533985
    formula = "=IN4*'LPG Annual'!$C$6"
    @eval_fn
    def IN5():
        in4_1 = LPG_Monthly.IN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(in4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IO5():
    # 'LPG_Monthly'!IO5
    value = 2.26704889423
    formula = "=IO4*'LPG Annual'!$C$6"
    @eval_fn
    def IO5():
        io4_1 = LPG_Monthly.IO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(io4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IP5():
    # 'LPG_Monthly'!IP5
    value = 2.38367248853
    formula = "=IP4*'LPG Annual'!$C$6"
    @eval_fn
    def IP5():
        ip4_1 = LPG_Monthly.IP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ip4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IQ5():
    # 'LPG_Monthly'!IQ5
    value = 2.45193995837
    formula = "=IQ4*'LPG Annual'!$C$6"
    @eval_fn
    def IQ5():
        iq4_1 = LPG_Monthly.IQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IR5():
    # 'LPG_Monthly'!IR5
    value = 2.5458077294
    formula = "=IR4*'LPG Annual'!$C$6"
    @eval_fn
    def IR5():
        ir4_1 = LPG_Monthly.IR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ir4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IS5():
    # 'LPG_Monthly'!IS5
    value = 2.67096475744
    formula = "=IS4*'LPG Annual'!$C$6"
    @eval_fn
    def IS5():
        is4_1 = LPG_Monthly.IS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(is4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IT5():
    # 'LPG_Monthly'!IT5
    value = 2.65105341207
    formula = "=IT4*'LPG Annual'!$C$6"
    @eval_fn
    def IT5():
        it4_1 = LPG_Monthly.IT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(it4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IU5():
    # 'LPG_Monthly'!IU5
    value = 2.45478443628
    formula = "=IU4*'LPG Annual'!$C$6"
    @eval_fn
    def IU5():
        iu4_1 = LPG_Monthly.IU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IV5():
    # 'LPG_Monthly'!IV5
    value = 2.61691967715
    formula = "=IV4*'LPG Annual'!$C$6"
    @eval_fn
    def IV5():
        iv4_1 = LPG_Monthly.IV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IW5():
    # 'LPG_Monthly'!IW5
    value = 3.01799106245
    formula = "=IW4*'LPG Annual'!$C$6"
    @eval_fn
    def IW5():
        iw4_1 = LPG_Monthly.IW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IX5():
    # 'LPG_Monthly'!IX5
    value = 3.14883704631
    formula = "=IX4*'LPG Annual'!$C$6"
    @eval_fn
    def IX5():
        ix4_1 = LPG_Monthly.IX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ix4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IY5():
    # 'LPG_Monthly'!IY5
    value = 3.2313269057
    formula = "=IY4*'LPG Annual'!$C$6"
    @eval_fn
    def IY5():
        iy4_1 = LPG_Monthly.IY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class IZ5():
    # 'LPG_Monthly'!IZ5
    value = 3.35932841165
    formula = "=IZ4*'LPG Annual'!$C$6"
    @eval_fn
    def IZ5():
        iz4_1 = LPG_Monthly.IZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(iz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JA5():
    # 'LPG_Monthly'!JA5
    value = 3.62670933518
    formula = "=JA4*'LPG Annual'!$C$6"
    @eval_fn
    def JA5():
        ja4_1 = LPG_Monthly.JA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ja4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JB5():
    # 'LPG_Monthly'!JB5
    value = 3.96804668437
    formula = "=JB4*'LPG Annual'!$C$6"
    @eval_fn
    def JB5():
        jb4_1 = LPG_Monthly.JB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JC5():
    # 'LPG_Monthly'!JC5
    value = 4.10458162405
    formula = "=JC4*'LPG Annual'!$C$6"
    @eval_fn
    def JC5():
        jc4_1 = LPG_Monthly.JC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JD5():
    # 'LPG_Monthly'!JD5
    value = 3.02652449618
    formula = "=JD4*'LPG Annual'!$C$6"
    @eval_fn
    def JD5():
        jd4_1 = LPG_Monthly.JD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JE5():
    # 'LPG_Monthly'!JE5
    value = 3.13177017885
    formula = "=JE4*'LPG Annual'!$C$6"
    @eval_fn
    def JE5():
        je4_1 = LPG_Monthly.JE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(je4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JF5():
    # 'LPG_Monthly'!JF5
    value = 2.96679046007
    formula = "=JF4*'LPG Annual'!$C$6"
    @eval_fn
    def JF5():
        jf4_1 = LPG_Monthly.JF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JG5():
    # 'LPG_Monthly'!JG5
    value = 2.9753238938
    formula = "=JG4*'LPG Annual'!$C$6"
    @eval_fn
    def JG5():
        jg4_1 = LPG_Monthly.JG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JH5():
    # 'LPG_Monthly'!JH5
    value = 2.9468791147
    formula = "=JH4*'LPG Annual'!$C$6"
    @eval_fn
    def JH5():
        jh4_1 = LPG_Monthly.JH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JI5():
    # 'LPG_Monthly'!JI5
    value = 2.89567851232
    formula = "=JI4*'LPG Annual'!$C$6"
    @eval_fn
    def JI5():
        ji4_1 = LPG_Monthly.JI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ji4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JJ5():
    # 'LPG_Monthly'!JJ5
    value = 3.02083554036
    formula = "=JJ4*'LPG Annual'!$C$6"
    @eval_fn
    def JJ5():
        jj4_1 = LPG_Monthly.JJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JK5():
    # 'LPG_Monthly'!JK5
    value = 2.66243132371
    formula = "=JK4*'LPG Annual'!$C$6"
    @eval_fn
    def JK5():
        jk4_1 = LPG_Monthly.JK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JL5():
    # 'LPG_Monthly'!JL5
    value = 2.28127128378
    formula = "=JL4*'LPG Annual'!$C$6"
    @eval_fn
    def JL5():
        jl4_1 = LPG_Monthly.JL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JM5():
    # 'LPG_Monthly'!JM5
    value = 1.58721867375
    formula = "=JM4*'LPG Annual'!$C$6"
    @eval_fn
    def JM5():
        jm4_1 = LPG_Monthly.JM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JN5():
    # 'LPG_Monthly'!JN5
    value = 1.35966044095
    formula = "=JN4*'LPG Annual'!$C$6"
    @eval_fn
    def JN5():
        jn4_1 = LPG_Monthly.JN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JO5():
    # 'LPG_Monthly'!JO5
    value = 1.6298858424
    formula = "=JO4*'LPG Annual'!$C$6"
    @eval_fn
    def JO5():
        jo4_1 = LPG_Monthly.JO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JP5():
    # 'LPG_Monthly'!JP5
    value = 1.54170702719
    formula = "=JP4*'LPG Annual'!$C$6"
    @eval_fn
    def JP5():
        jp4_1 = LPG_Monthly.JP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JQ5():
    # 'LPG_Monthly'!JQ5
    value = 1.55877389465
    formula = "=JQ4*'LPG Annual'!$C$6"
    @eval_fn
    def JQ5():
        jq4_1 = LPG_Monthly.JQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JR5():
    # 'LPG_Monthly'!JR5
    value = 1.33690461767
    formula = "=JR4*'LPG Annual'!$C$6"
    @eval_fn
    def JR5():
        jr4_1 = LPG_Monthly.JR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JS5():
    # 'LPG_Monthly'!JS5
    value = 1.04961234877
    formula = "=JS4*'LPG Annual'!$C$6"
    @eval_fn
    def JS5():
        js4_1 = LPG_Monthly.JS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(js4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JT5():
    # 'LPG_Monthly'!JT5
    value = 1.16339146517
    formula = "=JT4*'LPG Annual'!$C$6"
    @eval_fn
    def JT5():
        jt4_1 = LPG_Monthly.JT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JU5():
    # 'LPG_Monthly'!JU5
    value = 1.06383473832
    formula = "=JU4*'LPG Annual'!$C$6"
    @eval_fn
    def JU5():
        ju4_1 = LPG_Monthly.JU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ju4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JV5():
    # 'LPG_Monthly'!JV5
    value = 1.28854849321
    formula = "=JV4*'LPG Annual'!$C$6"
    @eval_fn
    def JV5():
        jv4_1 = LPG_Monthly.JV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JW5():
    # 'LPG_Monthly'!JW5
    value = 1.28285953739
    formula = "=JW4*'LPG Annual'!$C$6"
    @eval_fn
    def JW5():
        jw4_1 = LPG_Monthly.JW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JX5():
    # 'LPG_Monthly'!JX5
    value = 1.22312550128
    formula = "=JX4*'LPG Annual'!$C$6"
    @eval_fn
    def JX5():
        jx4_1 = LPG_Monthly.JX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JY5():
    # 'LPG_Monthly'!JY5
    value = 1.10081295115
    formula = "=JY4*'LPG Annual'!$C$6"
    @eval_fn
    def JY5():
        jy4_1 = LPG_Monthly.JY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class JZ5():
    # 'LPG_Monthly'!JZ5
    value = 0.955744577742
    formula = "=JZ4*'LPG Annual'!$C$6"
    @eval_fn
    def JZ5():
        jz4_1 = LPG_Monthly.JZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(jz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KA5():
    # 'LPG_Monthly'!KA5
    value = "#N/A"
    formula = "=KA4*'LPG Annual'!$C$6"
    @eval_fn
    def KA5():
        ka4_1 = LPG_Monthly.KA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ka4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KB5():
    # 'LPG_Monthly'!KB5
    value = "#N/A"
    formula = "=KB4*'LPG Annual'!$C$6"
    @eval_fn
    def KB5():
        kb4_1 = LPG_Monthly.KB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KC5():
    # 'LPG_Monthly'!KC5
    value = "#N/A"
    formula = "=KC4*'LPG Annual'!$C$6"
    @eval_fn
    def KC5():
        kc4_1 = LPG_Monthly.KC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KD5():
    # 'LPG_Monthly'!KD5
    value = "#N/A"
    formula = "=KD4*'LPG Annual'!$C$6"
    @eval_fn
    def KD5():
        kd4_1 = LPG_Monthly.KD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KE5():
    # 'LPG_Monthly'!KE5
    value = "#N/A"
    formula = "=KE4*'LPG Annual'!$C$6"
    @eval_fn
    def KE5():
        ke4_1 = LPG_Monthly.KE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ke4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KF5():
    # 'LPG_Monthly'!KF5
    value = "#N/A"
    formula = "=KF4*'LPG Annual'!$C$6"
    @eval_fn
    def KF5():
        kf4_1 = LPG_Monthly.KF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KG5():
    # 'LPG_Monthly'!KG5
    value = "#N/A"
    formula = "=KG4*'LPG Annual'!$C$6"
    @eval_fn
    def KG5():
        kg4_1 = LPG_Monthly.KG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KH5():
    # 'LPG_Monthly'!KH5
    value = "#N/A"
    formula = "=KH4*'LPG Annual'!$C$6"
    @eval_fn
    def KH5():
        kh4_1 = LPG_Monthly.KH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KI5():
    # 'LPG_Monthly'!KI5
    value = "#N/A"
    formula = "=KI4*'LPG Annual'!$C$6"
    @eval_fn
    def KI5():
        ki4_1 = LPG_Monthly.KI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ki4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KJ5():
    # 'LPG_Monthly'!KJ5
    value = "#N/A"
    formula = "=KJ4*'LPG Annual'!$C$6"
    @eval_fn
    def KJ5():
        kj4_1 = LPG_Monthly.KJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KK5():
    # 'LPG_Monthly'!KK5
    value = "#N/A"
    formula = "=KK4*'LPG Annual'!$C$6"
    @eval_fn
    def KK5():
        kk4_1 = LPG_Monthly.KK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KL5():
    # 'LPG_Monthly'!KL5
    value = "#N/A"
    formula = "=KL4*'LPG Annual'!$C$6"
    @eval_fn
    def KL5():
        kl4_1 = LPG_Monthly.KL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KM5():
    # 'LPG_Monthly'!KM5
    value = "#N/A"
    formula = "=KM4*'LPG Annual'!$C$6"
    @eval_fn
    def KM5():
        km4_1 = LPG_Monthly.KM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(km4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KN5():
    # 'LPG_Monthly'!KN5
    value = "#N/A"
    formula = "=KN4*'LPG Annual'!$C$6"
    @eval_fn
    def KN5():
        kn4_1 = LPG_Monthly.KN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KO5():
    # 'LPG_Monthly'!KO5
    value = "#N/A"
    formula = "=KO4*'LPG Annual'!$C$6"
    @eval_fn
    def KO5():
        ko4_1 = LPG_Monthly.KO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ko4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KP5():
    # 'LPG_Monthly'!KP5
    value = "#N/A"
    formula = "=KP4*'LPG Annual'!$C$6"
    @eval_fn
    def KP5():
        kp4_1 = LPG_Monthly.KP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KQ5():
    # 'LPG_Monthly'!KQ5
    value = "#N/A"
    formula = "=KQ4*'LPG Annual'!$C$6"
    @eval_fn
    def KQ5():
        kq4_1 = LPG_Monthly.KQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KR5():
    # 'LPG_Monthly'!KR5
    value = "#N/A"
    formula = "=KR4*'LPG Annual'!$C$6"
    @eval_fn
    def KR5():
        kr4_1 = LPG_Monthly.KR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KS5():
    # 'LPG_Monthly'!KS5
    value = "#N/A"
    formula = "=KS4*'LPG Annual'!$C$6"
    @eval_fn
    def KS5():
        ks4_1 = LPG_Monthly.KS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ks4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KT5():
    # 'LPG_Monthly'!KT5
    value = "#N/A"
    formula = "=KT4*'LPG Annual'!$C$6"
    @eval_fn
    def KT5():
        kt4_1 = LPG_Monthly.KT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KU5():
    # 'LPG_Monthly'!KU5
    value = "#N/A"
    formula = "=KU4*'LPG Annual'!$C$6"
    @eval_fn
    def KU5():
        ku4_1 = LPG_Monthly.KU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ku4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KV5():
    # 'LPG_Monthly'!KV5
    value = "#N/A"
    formula = "=KV4*'LPG Annual'!$C$6"
    @eval_fn
    def KV5():
        kv4_1 = LPG_Monthly.KV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KW5():
    # 'LPG_Monthly'!KW5
    value = "#N/A"
    formula = "=KW4*'LPG Annual'!$C$6"
    @eval_fn
    def KW5():
        kw4_1 = LPG_Monthly.KW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KX5():
    # 'LPG_Monthly'!KX5
    value = "#N/A"
    formula = "=KX4*'LPG Annual'!$C$6"
    @eval_fn
    def KX5():
        kx4_1 = LPG_Monthly.KX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KY5():
    # 'LPG_Monthly'!KY5
    value = "#N/A"
    formula = "=KY4*'LPG Annual'!$C$6"
    @eval_fn
    def KY5():
        ky4_1 = LPG_Monthly.KY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ky4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class KZ5():
    # 'LPG_Monthly'!KZ5
    value = "#N/A"
    formula = "=KZ4*'LPG Annual'!$C$6"
    @eval_fn
    def KZ5():
        kz4_1 = LPG_Monthly.KZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(kz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LA5():
    # 'LPG_Monthly'!LA5
    value = "#N/A"
    formula = "=LA4*'LPG Annual'!$C$6"
    @eval_fn
    def LA5():
        la4_1 = LPG_Monthly.LA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(la4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LB5():
    # 'LPG_Monthly'!LB5
    value = "#N/A"
    formula = "=LB4*'LPG Annual'!$C$6"
    @eval_fn
    def LB5():
        lb4_1 = LPG_Monthly.LB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LC5():
    # 'LPG_Monthly'!LC5
    value = "#N/A"
    formula = "=LC4*'LPG Annual'!$C$6"
    @eval_fn
    def LC5():
        lc4_1 = LPG_Monthly.LC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LD5():
    # 'LPG_Monthly'!LD5
    value = "#N/A"
    formula = "=LD4*'LPG Annual'!$C$6"
    @eval_fn
    def LD5():
        ld4_1 = LPG_Monthly.LD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ld4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LE5():
    # 'LPG_Monthly'!LE5
    value = "#N/A"
    formula = "=LE4*'LPG Annual'!$C$6"
    @eval_fn
    def LE5():
        le4_1 = LPG_Monthly.LE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(le4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LF5():
    # 'LPG_Monthly'!LF5
    value = "#N/A"
    formula = "=LF4*'LPG Annual'!$C$6"
    @eval_fn
    def LF5():
        lf4_1 = LPG_Monthly.LF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LG5():
    # 'LPG_Monthly'!LG5
    value = "#N/A"
    formula = "=LG4*'LPG Annual'!$C$6"
    @eval_fn
    def LG5():
        lg4_1 = LPG_Monthly.LG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LH5():
    # 'LPG_Monthly'!LH5
    value = "#N/A"
    formula = "=LH4*'LPG Annual'!$C$6"
    @eval_fn
    def LH5():
        lh4_1 = LPG_Monthly.LH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LI5():
    # 'LPG_Monthly'!LI5
    value = "#N/A"
    formula = "=LI4*'LPG Annual'!$C$6"
    @eval_fn
    def LI5():
        li4_1 = LPG_Monthly.LI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(li4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LJ5():
    # 'LPG_Monthly'!LJ5
    value = "#N/A"
    formula = "=LJ4*'LPG Annual'!$C$6"
    @eval_fn
    def LJ5():
        lj4_1 = LPG_Monthly.LJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LK5():
    # 'LPG_Monthly'!LK5
    value = "#N/A"
    formula = "=LK4*'LPG Annual'!$C$6"
    @eval_fn
    def LK5():
        lk4_1 = LPG_Monthly.LK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LL5():
    # 'LPG_Monthly'!LL5
    value = "#N/A"
    formula = "=LL4*'LPG Annual'!$C$6"
    @eval_fn
    def LL5():
        ll4_1 = LPG_Monthly.LL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ll4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LM5():
    # 'LPG_Monthly'!LM5
    value = "#N/A"
    formula = "=LM4*'LPG Annual'!$C$6"
    @eval_fn
    def LM5():
        lm4_1 = LPG_Monthly.LM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LN5():
    # 'LPG_Monthly'!LN5
    value = "#N/A"
    formula = "=LN4*'LPG Annual'!$C$6"
    @eval_fn
    def LN5():
        ln4_1 = LPG_Monthly.LN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ln4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LO5():
    # 'LPG_Monthly'!LO5
    value = "#N/A"
    formula = "=LO4*'LPG Annual'!$C$6"
    @eval_fn
    def LO5():
        lo4_1 = LPG_Monthly.LO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LP5():
    # 'LPG_Monthly'!LP5
    value = "#N/A"
    formula = "=LP4*'LPG Annual'!$C$6"
    @eval_fn
    def LP5():
        lp4_1 = LPG_Monthly.LP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LQ5():
    # 'LPG_Monthly'!LQ5
    value = "#N/A"
    formula = "=LQ4*'LPG Annual'!$C$6"
    @eval_fn
    def LQ5():
        lq4_1 = LPG_Monthly.LQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LR5():
    # 'LPG_Monthly'!LR5
    value = "#N/A"
    formula = "=LR4*'LPG Annual'!$C$6"
    @eval_fn
    def LR5():
        lr4_1 = LPG_Monthly.LR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LS5():
    # 'LPG_Monthly'!LS5
    value = "#N/A"
    formula = "=LS4*'LPG Annual'!$C$6"
    @eval_fn
    def LS5():
        ls4_1 = LPG_Monthly.LS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ls4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LT5():
    # 'LPG_Monthly'!LT5
    value = "#N/A"
    formula = "=LT4*'LPG Annual'!$C$6"
    @eval_fn
    def LT5():
        lt4_1 = LPG_Monthly.LT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LU5():
    # 'LPG_Monthly'!LU5
    value = "#N/A"
    formula = "=LU4*'LPG Annual'!$C$6"
    @eval_fn
    def LU5():
        lu4_1 = LPG_Monthly.LU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LV5():
    # 'LPG_Monthly'!LV5
    value = "#N/A"
    formula = "=LV4*'LPG Annual'!$C$6"
    @eval_fn
    def LV5():
        lv4_1 = LPG_Monthly.LV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LW5():
    # 'LPG_Monthly'!LW5
    value = "#N/A"
    formula = "=LW4*'LPG Annual'!$C$6"
    @eval_fn
    def LW5():
        lw4_1 = LPG_Monthly.LW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LX5():
    # 'LPG_Monthly'!LX5
    value = "#N/A"
    formula = "=LX4*'LPG Annual'!$C$6"
    @eval_fn
    def LX5():
        lx4_1 = LPG_Monthly.LX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LY5():
    # 'LPG_Monthly'!LY5
    value = "#N/A"
    formula = "=LY4*'LPG Annual'!$C$6"
    @eval_fn
    def LY5():
        ly4_1 = LPG_Monthly.LY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ly4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class LZ5():
    # 'LPG_Monthly'!LZ5
    value = "#N/A"
    formula = "=LZ4*'LPG Annual'!$C$6"
    @eval_fn
    def LZ5():
        lz4_1 = LPG_Monthly.LZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(lz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MA5():
    # 'LPG_Monthly'!MA5
    value = "#N/A"
    formula = "=MA4*'LPG Annual'!$C$6"
    @eval_fn
    def MA5():
        ma4_1 = LPG_Monthly.MA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ma4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MB5():
    # 'LPG_Monthly'!MB5
    value = "#N/A"
    formula = "=MB4*'LPG Annual'!$C$6"
    @eval_fn
    def MB5():
        mb4_1 = LPG_Monthly.MB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MC5():
    # 'LPG_Monthly'!MC5
    value = "#N/A"
    formula = "=MC4*'LPG Annual'!$C$6"
    @eval_fn
    def MC5():
        mc4_1 = LPG_Monthly.MC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MD5():
    # 'LPG_Monthly'!MD5
    value = "#N/A"
    formula = "=MD4*'LPG Annual'!$C$6"
    @eval_fn
    def MD5():
        md4_1 = LPG_Monthly.MD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(md4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ME5():
    # 'LPG_Monthly'!ME5
    value = "#N/A"
    formula = "=ME4*'LPG Annual'!$C$6"
    @eval_fn
    def ME5():
        me4_1 = LPG_Monthly.ME4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(me4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MF5():
    # 'LPG_Monthly'!MF5
    value = "#N/A"
    formula = "=MF4*'LPG Annual'!$C$6"
    @eval_fn
    def MF5():
        mf4_1 = LPG_Monthly.MF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MG5():
    # 'LPG_Monthly'!MG5
    value = "#N/A"
    formula = "=MG4*'LPG Annual'!$C$6"
    @eval_fn
    def MG5():
        mg4_1 = LPG_Monthly.MG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MH5():
    # 'LPG_Monthly'!MH5
    value = "#N/A"
    formula = "=MH4*'LPG Annual'!$C$6"
    @eval_fn
    def MH5():
        mh4_1 = LPG_Monthly.MH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MI5():
    # 'LPG_Monthly'!MI5
    value = "#N/A"
    formula = "=MI4*'LPG Annual'!$C$6"
    @eval_fn
    def MI5():
        mi4_1 = LPG_Monthly.MI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MJ5():
    # 'LPG_Monthly'!MJ5
    value = "#N/A"
    formula = "=MJ4*'LPG Annual'!$C$6"
    @eval_fn
    def MJ5():
        mj4_1 = LPG_Monthly.MJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MK5():
    # 'LPG_Monthly'!MK5
    value = "#N/A"
    formula = "=MK4*'LPG Annual'!$C$6"
    @eval_fn
    def MK5():
        mk4_1 = LPG_Monthly.MK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ML5():
    # 'LPG_Monthly'!ML5
    value = "#N/A"
    formula = "=ML4*'LPG Annual'!$C$6"
    @eval_fn
    def ML5():
        ml4_1 = LPG_Monthly.ML4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ml4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MM5():
    # 'LPG_Monthly'!MM5
    value = "#N/A"
    formula = "=MM4*'LPG Annual'!$C$6"
    @eval_fn
    def MM5():
        mm4_1 = LPG_Monthly.MM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MN5():
    # 'LPG_Monthly'!MN5
    value = "#N/A"
    formula = "=MN4*'LPG Annual'!$C$6"
    @eval_fn
    def MN5():
        mn4_1 = LPG_Monthly.MN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MO5():
    # 'LPG_Monthly'!MO5
    value = "#N/A"
    formula = "=MO4*'LPG Annual'!$C$6"
    @eval_fn
    def MO5():
        mo4_1 = LPG_Monthly.MO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MP5():
    # 'LPG_Monthly'!MP5
    value = "#N/A"
    formula = "=MP4*'LPG Annual'!$C$6"
    @eval_fn
    def MP5():
        mp4_1 = LPG_Monthly.MP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MQ5():
    # 'LPG_Monthly'!MQ5
    value = "#N/A"
    formula = "=MQ4*'LPG Annual'!$C$6"
    @eval_fn
    def MQ5():
        mq4_1 = LPG_Monthly.MQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MR5():
    # 'LPG_Monthly'!MR5
    value = "#N/A"
    formula = "=MR4*'LPG Annual'!$C$6"
    @eval_fn
    def MR5():
        mr4_1 = LPG_Monthly.MR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MS5():
    # 'LPG_Monthly'!MS5
    value = "#N/A"
    formula = "=MS4*'LPG Annual'!$C$6"
    @eval_fn
    def MS5():
        ms4_1 = LPG_Monthly.MS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ms4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MT5():
    # 'LPG_Monthly'!MT5
    value = "#N/A"
    formula = "=MT4*'LPG Annual'!$C$6"
    @eval_fn
    def MT5():
        mt4_1 = LPG_Monthly.MT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MU5():
    # 'LPG_Monthly'!MU5
    value = "#N/A"
    formula = "=MU4*'LPG Annual'!$C$6"
    @eval_fn
    def MU5():
        mu4_1 = LPG_Monthly.MU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MV5():
    # 'LPG_Monthly'!MV5
    value = "#N/A"
    formula = "=MV4*'LPG Annual'!$C$6"
    @eval_fn
    def MV5():
        mv4_1 = LPG_Monthly.MV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MW5():
    # 'LPG_Monthly'!MW5
    value = "#N/A"
    formula = "=MW4*'LPG Annual'!$C$6"
    @eval_fn
    def MW5():
        mw4_1 = LPG_Monthly.MW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MX5():
    # 'LPG_Monthly'!MX5
    value = "#N/A"
    formula = "=MX4*'LPG Annual'!$C$6"
    @eval_fn
    def MX5():
        mx4_1 = LPG_Monthly.MX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MY5():
    # 'LPG_Monthly'!MY5
    value = "#N/A"
    formula = "=MY4*'LPG Annual'!$C$6"
    @eval_fn
    def MY5():
        my4_1 = LPG_Monthly.MY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(my4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class MZ5():
    # 'LPG_Monthly'!MZ5
    value = "#N/A"
    formula = "=MZ4*'LPG Annual'!$C$6"
    @eval_fn
    def MZ5():
        mz4_1 = LPG_Monthly.MZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(mz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NA5():
    # 'LPG_Monthly'!NA5
    value = "#N/A"
    formula = "=NA4*'LPG Annual'!$C$6"
    @eval_fn
    def NA5():
        na4_1 = LPG_Monthly.NA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(na4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NB5():
    # 'LPG_Monthly'!NB5
    value = "#N/A"
    formula = "=NB4*'LPG Annual'!$C$6"
    @eval_fn
    def NB5():
        nb4_1 = LPG_Monthly.NB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NC5():
    # 'LPG_Monthly'!NC5
    value = "#N/A"
    formula = "=NC4*'LPG Annual'!$C$6"
    @eval_fn
    def NC5():
        nc4_1 = LPG_Monthly.NC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ND5():
    # 'LPG_Monthly'!ND5
    value = "#N/A"
    formula = "=ND4*'LPG Annual'!$C$6"
    @eval_fn
    def ND5():
        nd4_1 = LPG_Monthly.ND4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NE5():
    # 'LPG_Monthly'!NE5
    value = "#N/A"
    formula = "=NE4*'LPG Annual'!$C$6"
    @eval_fn
    def NE5():
        ne4_1 = LPG_Monthly.NE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ne4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NF5():
    # 'LPG_Monthly'!NF5
    value = "#N/A"
    formula = "=NF4*'LPG Annual'!$C$6"
    @eval_fn
    def NF5():
        nf4_1 = LPG_Monthly.NF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NG5():
    # 'LPG_Monthly'!NG5
    value = "#N/A"
    formula = "=NG4*'LPG Annual'!$C$6"
    @eval_fn
    def NG5():
        ng4_1 = LPG_Monthly.NG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ng4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NH5():
    # 'LPG_Monthly'!NH5
    value = "#N/A"
    formula = "=NH4*'LPG Annual'!$C$6"
    @eval_fn
    def NH5():
        nh4_1 = LPG_Monthly.NH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NI5():
    # 'LPG_Monthly'!NI5
    value = "#N/A"
    formula = "=NI4*'LPG Annual'!$C$6"
    @eval_fn
    def NI5():
        ni4_1 = LPG_Monthly.NI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ni4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NJ5():
    # 'LPG_Monthly'!NJ5
    value = "#N/A"
    formula = "=NJ4*'LPG Annual'!$C$6"
    @eval_fn
    def NJ5():
        nj4_1 = LPG_Monthly.NJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NK5():
    # 'LPG_Monthly'!NK5
    value = "#N/A"
    formula = "=NK4*'LPG Annual'!$C$6"
    @eval_fn
    def NK5():
        nk4_1 = LPG_Monthly.NK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NL5():
    # 'LPG_Monthly'!NL5
    value = "#N/A"
    formula = "=NL4*'LPG Annual'!$C$6"
    @eval_fn
    def NL5():
        nl4_1 = LPG_Monthly.NL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NM5():
    # 'LPG_Monthly'!NM5
    value = "#N/A"
    formula = "=NM4*'LPG Annual'!$C$6"
    @eval_fn
    def NM5():
        nm4_1 = LPG_Monthly.NM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NN5():
    # 'LPG_Monthly'!NN5
    value = "#N/A"
    formula = "=NN4*'LPG Annual'!$C$6"
    @eval_fn
    def NN5():
        nn4_1 = LPG_Monthly.NN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NO5():
    # 'LPG_Monthly'!NO5
    value = "#N/A"
    formula = "=NO4*'LPG Annual'!$C$6"
    @eval_fn
    def NO5():
        no4_1 = LPG_Monthly.NO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(no4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NP5():
    # 'LPG_Monthly'!NP5
    value = "#N/A"
    formula = "=NP4*'LPG Annual'!$C$6"
    @eval_fn
    def NP5():
        np4_1 = LPG_Monthly.NP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(np4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NQ5():
    # 'LPG_Monthly'!NQ5
    value = "#N/A"
    formula = "=NQ4*'LPG Annual'!$C$6"
    @eval_fn
    def NQ5():
        nq4_1 = LPG_Monthly.NQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NR5():
    # 'LPG_Monthly'!NR5
    value = "#N/A"
    formula = "=NR4*'LPG Annual'!$C$6"
    @eval_fn
    def NR5():
        nr4_1 = LPG_Monthly.NR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NS5():
    # 'LPG_Monthly'!NS5
    value = "#N/A"
    formula = "=NS4*'LPG Annual'!$C$6"
    @eval_fn
    def NS5():
        ns4_1 = LPG_Monthly.NS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ns4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NT5():
    # 'LPG_Monthly'!NT5
    value = "#N/A"
    formula = "=NT4*'LPG Annual'!$C$6"
    @eval_fn
    def NT5():
        nt4_1 = LPG_Monthly.NT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NU5():
    # 'LPG_Monthly'!NU5
    value = "#N/A"
    formula = "=NU4*'LPG Annual'!$C$6"
    @eval_fn
    def NU5():
        nu4_1 = LPG_Monthly.NU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NV5():
    # 'LPG_Monthly'!NV5
    value = "#N/A"
    formula = "=NV4*'LPG Annual'!$C$6"
    @eval_fn
    def NV5():
        nv4_1 = LPG_Monthly.NV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NW5():
    # 'LPG_Monthly'!NW5
    value = "#N/A"
    formula = "=NW4*'LPG Annual'!$C$6"
    @eval_fn
    def NW5():
        nw4_1 = LPG_Monthly.NW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NX5():
    # 'LPG_Monthly'!NX5
    value = "#N/A"
    formula = "=NX4*'LPG Annual'!$C$6"
    @eval_fn
    def NX5():
        nx4_1 = LPG_Monthly.NX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nx4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NY5():
    # 'LPG_Monthly'!NY5
    value = "#N/A"
    formula = "=NY4*'LPG Annual'!$C$6"
    @eval_fn
    def NY5():
        ny4_1 = LPG_Monthly.NY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ny4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class NZ5():
    # 'LPG_Monthly'!NZ5
    value = "#N/A"
    formula = "=NZ4*'LPG Annual'!$C$6"
    @eval_fn
    def NZ5():
        nz4_1 = LPG_Monthly.NZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(nz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OA5():
    # 'LPG_Monthly'!OA5
    value = "#N/A"
    formula = "=OA4*'LPG Annual'!$C$6"
    @eval_fn
    def OA5():
        oa4_1 = LPG_Monthly.OA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oa4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OB5():
    # 'LPG_Monthly'!OB5
    value = "#N/A"
    formula = "=OB4*'LPG Annual'!$C$6"
    @eval_fn
    def OB5():
        ob4_1 = LPG_Monthly.OB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ob4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OC5():
    # 'LPG_Monthly'!OC5
    value = "#N/A"
    formula = "=OC4*'LPG Annual'!$C$6"
    @eval_fn
    def OC5():
        oc4_1 = LPG_Monthly.OC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OD5():
    # 'LPG_Monthly'!OD5
    value = "#N/A"
    formula = "=OD4*'LPG Annual'!$C$6"
    @eval_fn
    def OD5():
        od4_1 = LPG_Monthly.OD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(od4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OE5():
    # 'LPG_Monthly'!OE5
    value = "#N/A"
    formula = "=OE4*'LPG Annual'!$C$6"
    @eval_fn
    def OE5():
        oe4_1 = LPG_Monthly.OE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oe4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OF5():
    # 'LPG_Monthly'!OF5
    value = "#N/A"
    formula = "=OF4*'LPG Annual'!$C$6"
    @eval_fn
    def OF5():
        of4_1 = LPG_Monthly.OF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(of4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OG5():
    # 'LPG_Monthly'!OG5
    value = "#N/A"
    formula = "=OG4*'LPG Annual'!$C$6"
    @eval_fn
    def OG5():
        og4_1 = LPG_Monthly.OG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(og4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OH5():
    # 'LPG_Monthly'!OH5
    value = "#N/A"
    formula = "=OH4*'LPG Annual'!$C$6"
    @eval_fn
    def OH5():
        oh4_1 = LPG_Monthly.OH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OI5():
    # 'LPG_Monthly'!OI5
    value = "#N/A"
    formula = "=OI4*'LPG Annual'!$C$6"
    @eval_fn
    def OI5():
        oi4_1 = LPG_Monthly.OI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OJ5():
    # 'LPG_Monthly'!OJ5
    value = "#N/A"
    formula = "=OJ4*'LPG Annual'!$C$6"
    @eval_fn
    def OJ5():
        oj4_1 = LPG_Monthly.OJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OK5():
    # 'LPG_Monthly'!OK5
    value = "#N/A"
    formula = "=OK4*'LPG Annual'!$C$6"
    @eval_fn
    def OK5():
        ok4_1 = LPG_Monthly.OK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ok4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OL5():
    # 'LPG_Monthly'!OL5
    value = "#N/A"
    formula = "=OL4*'LPG Annual'!$C$6"
    @eval_fn
    def OL5():
        ol4_1 = LPG_Monthly.OL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ol4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OM5():
    # 'LPG_Monthly'!OM5
    value = "#N/A"
    formula = "=OM4*'LPG Annual'!$C$6"
    @eval_fn
    def OM5():
        om4_1 = LPG_Monthly.OM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(om4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class ON5():
    # 'LPG_Monthly'!ON5
    value = "#N/A"
    formula = "=ON4*'LPG Annual'!$C$6"
    @eval_fn
    def ON5():
        on4_1 = LPG_Monthly.ON4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(on4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OO5():
    # 'LPG_Monthly'!OO5
    value = "#N/A"
    formula = "=OO4*'LPG Annual'!$C$6"
    @eval_fn
    def OO5():
        oo4_1 = LPG_Monthly.OO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OP5():
    # 'LPG_Monthly'!OP5
    value = "#N/A"
    formula = "=OP4*'LPG Annual'!$C$6"
    @eval_fn
    def OP5():
        op4_1 = LPG_Monthly.OP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(op4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OQ5():
    # 'LPG_Monthly'!OQ5
    value = "#N/A"
    formula = "=OQ4*'LPG Annual'!$C$6"
    @eval_fn
    def OQ5():
        oq4_1 = LPG_Monthly.OQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OR5():
    # 'LPG_Monthly'!OR5
    value = "#N/A"
    formula = "=OR4*'LPG Annual'!$C$6"
    @eval_fn
    def OR5():
        or4_1 = LPG_Monthly.OR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(or4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OS5():
    # 'LPG_Monthly'!OS5
    value = "#N/A"
    formula = "=OS4*'LPG Annual'!$C$6"
    @eval_fn
    def OS5():
        os4_1 = LPG_Monthly.OS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(os4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OT5():
    # 'LPG_Monthly'!OT5
    value = "#N/A"
    formula = "=OT4*'LPG Annual'!$C$6"
    @eval_fn
    def OT5():
        ot4_1 = LPG_Monthly.OT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ot4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OU5():
    # 'LPG_Monthly'!OU5
    value = "#N/A"
    formula = "=OU4*'LPG Annual'!$C$6"
    @eval_fn
    def OU5():
        ou4_1 = LPG_Monthly.OU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ou4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OV5():
    # 'LPG_Monthly'!OV5
    value = "#N/A"
    formula = "=OV4*'LPG Annual'!$C$6"
    @eval_fn
    def OV5():
        ov4_1 = LPG_Monthly.OV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ov4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OW5():
    # 'LPG_Monthly'!OW5
    value = "#N/A"
    formula = "=OW4*'LPG Annual'!$C$6"
    @eval_fn
    def OW5():
        ow4_1 = LPG_Monthly.OW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ow4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OX5():
    # 'LPG_Monthly'!OX5
    value = "#N/A"
    formula = "=OX4*'LPG Annual'!$C$6"
    @eval_fn
    def OX5():
        ox4_1 = LPG_Monthly.OX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ox4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OY5():
    # 'LPG_Monthly'!OY5
    value = "#N/A"
    formula = "=OY4*'LPG Annual'!$C$6"
    @eval_fn
    def OY5():
        oy4_1 = LPG_Monthly.OY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oy4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class OZ5():
    # 'LPG_Monthly'!OZ5
    value = "#N/A"
    formula = "=OZ4*'LPG Annual'!$C$6"
    @eval_fn
    def OZ5():
        oz4_1 = LPG_Monthly.OZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(oz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PA5():
    # 'LPG_Monthly'!PA5
    value = "#N/A"
    formula = "=PA4*'LPG Annual'!$C$6"
    @eval_fn
    def PA5():
        pa4_1 = LPG_Monthly.PA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pa4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PB5():
    # 'LPG_Monthly'!PB5
    value = "#N/A"
    formula = "=PB4*'LPG Annual'!$C$6"
    @eval_fn
    def PB5():
        pb4_1 = LPG_Monthly.PB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PC5():
    # 'LPG_Monthly'!PC5
    value = "#N/A"
    formula = "=PC4*'LPG Annual'!$C$6"
    @eval_fn
    def PC5():
        pc4_1 = LPG_Monthly.PC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PD5():
    # 'LPG_Monthly'!PD5
    value = "#N/A"
    formula = "=PD4*'LPG Annual'!$C$6"
    @eval_fn
    def PD5():
        pd4_1 = LPG_Monthly.PD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PE5():
    # 'LPG_Monthly'!PE5
    value = "#N/A"
    formula = "=PE4*'LPG Annual'!$C$6"
    @eval_fn
    def PE5():
        pe4_1 = LPG_Monthly.PE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pe4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PF5():
    # 'LPG_Monthly'!PF5
    value = "#N/A"
    formula = "=PF4*'LPG Annual'!$C$6"
    @eval_fn
    def PF5():
        pf4_1 = LPG_Monthly.PF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PG5():
    # 'LPG_Monthly'!PG5
    value = "#N/A"
    formula = "=PG4*'LPG Annual'!$C$6"
    @eval_fn
    def PG5():
        pg4_1 = LPG_Monthly.PG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PH5():
    # 'LPG_Monthly'!PH5
    value = "#N/A"
    formula = "=PH4*'LPG Annual'!$C$6"
    @eval_fn
    def PH5():
        ph4_1 = LPG_Monthly.PH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ph4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PI5():
    # 'LPG_Monthly'!PI5
    value = "#N/A"
    formula = "=PI4*'LPG Annual'!$C$6"
    @eval_fn
    def PI5():
        pi4_1 = LPG_Monthly.PI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PJ5():
    # 'LPG_Monthly'!PJ5
    value = "#N/A"
    formula = "=PJ4*'LPG Annual'!$C$6"
    @eval_fn
    def PJ5():
        pj4_1 = LPG_Monthly.PJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PK5():
    # 'LPG_Monthly'!PK5
    value = "#N/A"
    formula = "=PK4*'LPG Annual'!$C$6"
    @eval_fn
    def PK5():
        pk4_1 = LPG_Monthly.PK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PL5():
    # 'LPG_Monthly'!PL5
    value = "#N/A"
    formula = "=PL4*'LPG Annual'!$C$6"
    @eval_fn
    def PL5():
        pl4_1 = LPG_Monthly.PL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pl4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PM5():
    # 'LPG_Monthly'!PM5
    value = "#N/A"
    formula = "=PM4*'LPG Annual'!$C$6"
    @eval_fn
    def PM5():
        pm4_1 = LPG_Monthly.PM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PN5():
    # 'LPG_Monthly'!PN5
    value = "#N/A"
    formula = "=PN4*'LPG Annual'!$C$6"
    @eval_fn
    def PN5():
        pn4_1 = LPG_Monthly.PN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PO5():
    # 'LPG_Monthly'!PO5
    value = "#N/A"
    formula = "=PO4*'LPG Annual'!$C$6"
    @eval_fn
    def PO5():
        po4_1 = LPG_Monthly.PO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(po4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PP5():
    # 'LPG_Monthly'!PP5
    value = "#N/A"
    formula = "=PP4*'LPG Annual'!$C$6"
    @eval_fn
    def PP5():
        pp4_1 = LPG_Monthly.PP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PQ5():
    # 'LPG_Monthly'!PQ5
    value = "#N/A"
    formula = "=PQ4*'LPG Annual'!$C$6"
    @eval_fn
    def PQ5():
        pq4_1 = LPG_Monthly.PQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PR5():
    # 'LPG_Monthly'!PR5
    value = "#N/A"
    formula = "=PR4*'LPG Annual'!$C$6"
    @eval_fn
    def PR5():
        pr4_1 = LPG_Monthly.PR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PS5():
    # 'LPG_Monthly'!PS5
    value = "#N/A"
    formula = "=PS4*'LPG Annual'!$C$6"
    @eval_fn
    def PS5():
        ps4_1 = LPG_Monthly.PS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ps4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PT5():
    # 'LPG_Monthly'!PT5
    value = "#N/A"
    formula = "=PT4*'LPG Annual'!$C$6"
    @eval_fn
    def PT5():
        pt4_1 = LPG_Monthly.PT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PU5():
    # 'LPG_Monthly'!PU5
    value = "#N/A"
    formula = "=PU4*'LPG Annual'!$C$6"
    @eval_fn
    def PU5():
        pu4_1 = LPG_Monthly.PU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PV5():
    # 'LPG_Monthly'!PV5
    value = "#N/A"
    formula = "=PV4*'LPG Annual'!$C$6"
    @eval_fn
    def PV5():
        pv4_1 = LPG_Monthly.PV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PW5():
    # 'LPG_Monthly'!PW5
    value = "#N/A"
    formula = "=PW4*'LPG Annual'!$C$6"
    @eval_fn
    def PW5():
        pw4_1 = LPG_Monthly.PW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pw4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PX5():
    # 'LPG_Monthly'!PX5
    value = "#N/A"
    formula = "=PX4*'LPG Annual'!$C$6"
    @eval_fn
    def PX5():
        px4_1 = LPG_Monthly.PX4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(px4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PY5():
    # 'LPG_Monthly'!PY5
    value = "#N/A"
    formula = "=PY4*'LPG Annual'!$C$6"
    @eval_fn
    def PY5():
        py4_1 = LPG_Monthly.PY4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(py4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class PZ5():
    # 'LPG_Monthly'!PZ5
    value = "#N/A"
    formula = "=PZ4*'LPG Annual'!$C$6"
    @eval_fn
    def PZ5():
        pz4_1 = LPG_Monthly.PZ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(pz4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QA5():
    # 'LPG_Monthly'!QA5
    value = "#N/A"
    formula = "=QA4*'LPG Annual'!$C$6"
    @eval_fn
    def QA5():
        qa4_1 = LPG_Monthly.QA4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qa4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QB5():
    # 'LPG_Monthly'!QB5
    value = "#N/A"
    formula = "=QB4*'LPG Annual'!$C$6"
    @eval_fn
    def QB5():
        qb4_1 = LPG_Monthly.QB4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qb4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QC5():
    # 'LPG_Monthly'!QC5
    value = "#N/A"
    formula = "=QC4*'LPG Annual'!$C$6"
    @eval_fn
    def QC5():
        qc4_1 = LPG_Monthly.QC4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qc4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QD5():
    # 'LPG_Monthly'!QD5
    value = "#N/A"
    formula = "=QD4*'LPG Annual'!$C$6"
    @eval_fn
    def QD5():
        qd4_1 = LPG_Monthly.QD4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qd4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QE5():
    # 'LPG_Monthly'!QE5
    value = "#N/A"
    formula = "=QE4*'LPG Annual'!$C$6"
    @eval_fn
    def QE5():
        qe4_1 = LPG_Monthly.QE4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qe4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QF5():
    # 'LPG_Monthly'!QF5
    value = "#N/A"
    formula = "=QF4*'LPG Annual'!$C$6"
    @eval_fn
    def QF5():
        qf4_1 = LPG_Monthly.QF4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qf4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QG5():
    # 'LPG_Monthly'!QG5
    value = "#N/A"
    formula = "=QG4*'LPG Annual'!$C$6"
    @eval_fn
    def QG5():
        qg4_1 = LPG_Monthly.QG4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qg4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QH5():
    # 'LPG_Monthly'!QH5
    value = "#N/A"
    formula = "=QH4*'LPG Annual'!$C$6"
    @eval_fn
    def QH5():
        qh4_1 = LPG_Monthly.QH4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qh4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QI5():
    # 'LPG_Monthly'!QI5
    value = "#N/A"
    formula = "=QI4*'LPG Annual'!$C$6"
    @eval_fn
    def QI5():
        qi4_1 = LPG_Monthly.QI4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qi4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QJ5():
    # 'LPG_Monthly'!QJ5
    value = "#N/A"
    formula = "=QJ4*'LPG Annual'!$C$6"
    @eval_fn
    def QJ5():
        qj4_1 = LPG_Monthly.QJ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qj4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QK5():
    # 'LPG_Monthly'!QK5
    value = "#N/A"
    formula = "=QK4*'LPG Annual'!$C$6"
    @eval_fn
    def QK5():
        qk4_1 = LPG_Monthly.QK4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qk4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QL5():
    # 'LPG_Monthly'!QL5
    value = "#N/A"
    formula = "=QL4*'LPG Annual'!$C$6"
    @eval_fn
    def QL5():
        ql4_1 = LPG_Monthly.QL4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(ql4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QM5():
    # 'LPG_Monthly'!QM5
    value = "#N/A"
    formula = "=QM4*'LPG Annual'!$C$6"
    @eval_fn
    def QM5():
        qm4_1 = LPG_Monthly.QM4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qm4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QN5():
    # 'LPG_Monthly'!QN5
    value = "#N/A"
    formula = "=QN4*'LPG Annual'!$C$6"
    @eval_fn
    def QN5():
        qn4_1 = LPG_Monthly.QN4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qn4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QO5():
    # 'LPG_Monthly'!QO5
    value = "#N/A"
    formula = "=QO4*'LPG Annual'!$C$6"
    @eval_fn
    def QO5():
        qo4_1 = LPG_Monthly.QO4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qo4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QP5():
    # 'LPG_Monthly'!QP5
    value = "#N/A"
    formula = "=QP4*'LPG Annual'!$C$6"
    @eval_fn
    def QP5():
        qp4_1 = LPG_Monthly.QP4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qp4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QQ5():
    # 'LPG_Monthly'!QQ5
    value = "#N/A"
    formula = "=QQ4*'LPG Annual'!$C$6"
    @eval_fn
    def QQ5():
        qq4_1 = LPG_Monthly.QQ4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qq4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QR5():
    # 'LPG_Monthly'!QR5
    value = "#N/A"
    formula = "=QR4*'LPG Annual'!$C$6"
    @eval_fn
    def QR5():
        qr4_1 = LPG_Monthly.QR4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qr4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QS5():
    # 'LPG_Monthly'!QS5
    value = "#N/A"
    formula = "=QS4*'LPG Annual'!$C$6"
    @eval_fn
    def QS5():
        qs4_1 = LPG_Monthly.QS4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qs4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QT5():
    # 'LPG_Monthly'!QT5
    value = "#N/A"
    formula = "=QT4*'LPG Annual'!$C$6"
    @eval_fn
    def QT5():
        qt4_1 = LPG_Monthly.QT4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qt4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QU5():
    # 'LPG_Monthly'!QU5
    value = "#N/A"
    formula = "=QU4*'LPG Annual'!$C$6"
    @eval_fn
    def QU5():
        qu4_1 = LPG_Monthly.QU4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qu4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QV5():
    # 'LPG_Monthly'!QV5
    value = "#N/A"
    formula = "=QV4*'LPG Annual'!$C$6"
    @eval_fn
    def QV5():
        qv4_1 = LPG_Monthly.QV4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qv4_1, c6_1)
        return var_1

@register(LPG_Monthly)
class QW5():
    # 'LPG_Monthly'!QW5
    value = "#N/A"
    formula = "=QW4*'LPG Annual'!$C$6"
    @eval_fn
    def QW5():
        qw4_1 = LPG_Monthly.QW4()
        c6_1 = LPG_Annual.C6()
        var_1 = mult(qw4_1, c6_1)
        return var_1