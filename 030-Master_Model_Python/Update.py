# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Update = Worksheet('Update', 10, 10)



@register(Update)
class A1():
    # 'Update'!A1
    value = "http://tonto.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RBRTE&f=M"

@register(Update)
class B1():
    # 'Update'!B1
    value = "Cell"

@register(Update)
class C1():
    # 'Update'!C1
    value = "Source"

@register(Update)
class D1():
    # 'Update'!D1
    value = "Freq"

@register(Update)
class E1():
    # 'Update'!E1
    value = "Date of Release"

@register(Update)
class F1():
    # 'Update'!F1
    value = "Time to update"

@register(Update)
class G1():
    # 'Update'!G1
    value = "File Name"

@register(Update)
class H1():
    # 'Update'!H1
    value = "Automatable"

@register(Update)
class I1():
    # 'Update'!I1
    value = "In Metrics"

@register(Update)
class J1():
    # 'Update'!J1
    value = 1
    formula = "=(COLUMN(J1)-COLUMN($J1)+1)"
    @eval_fn
    def J1():
        range_1 = Update(10, 0, 10, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class K1():
    # 'Update'!K1
    value = 2
    formula = "=(COLUMN(K1)-COLUMN($J1)+1)"
    @eval_fn
    def K1():
        range_1 = Update(11, 0, 11, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class L1():
    # 'Update'!L1
    value = 3
    formula = "=(COLUMN(L1)-COLUMN($J1)+1)"
    @eval_fn
    def L1():
        range_1 = Update(12, 0, 12, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class M1():
    # 'Update'!M1
    value = 4
    formula = "=(COLUMN(M1)-COLUMN($J1)+1)"
    @eval_fn
    def M1():
        range_1 = Update(13, 0, 13, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class N1():
    # 'Update'!N1
    value = 5
    formula = "=(COLUMN(N1)-COLUMN($J1)+1)"
    @eval_fn
    def N1():
        range_1 = Update(14, 0, 14, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class O1():
    # 'Update'!O1
    value = 6
    formula = "=(COLUMN(O1)-COLUMN($J1)+1)"
    @eval_fn
    def O1():
        range_1 = Update(15, 0, 15, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class P1():
    # 'Update'!P1
    value = 7
    formula = "=(COLUMN(P1)-COLUMN($J1)+1)"
    @eval_fn
    def P1():
        range_1 = Update(16, 0, 16, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class Q1():
    # 'Update'!Q1
    value = 8
    formula = "=(COLUMN(Q1)-COLUMN($J1)+1)"
    @eval_fn
    def Q1():
        range_1 = Update(17, 0, 17, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class R1():
    # 'Update'!R1
    value = 9
    formula = "=(COLUMN(R1)-COLUMN($J1)+1)"
    @eval_fn
    def R1():
        range_1 = Update(18, 0, 18, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class S1():
    # 'Update'!S1
    value = 10
    formula = "=(COLUMN(S1)-COLUMN($J1)+1)"
    @eval_fn
    def S1():
        range_1 = Update(19, 0, 19, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class T1():
    # 'Update'!T1
    value = 11
    formula = "=(COLUMN(T1)-COLUMN($J1)+1)"
    @eval_fn
    def T1():
        range_1 = Update(20, 0, 20, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class U1():
    # 'Update'!U1
    value = 12
    formula = "=(COLUMN(U1)-COLUMN($J1)+1)"
    @eval_fn
    def U1():
        range_1 = Update(21, 0, 21, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class V1():
    # 'Update'!V1
    value = 13
    formula = "=(COLUMN(V1)-COLUMN($J1)+1)"
    @eval_fn
    def V1():
        range_1 = Update(22, 0, 22, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class W1():
    # 'Update'!W1
    value = 14
    formula = "=(COLUMN(W1)-COLUMN($J1)+1)"
    @eval_fn
    def W1():
        range_1 = Update(23, 0, 23, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class X1():
    # 'Update'!X1
    value = 15
    formula = "=(COLUMN(X1)-COLUMN($J1)+1)"
    @eval_fn
    def X1():
        range_1 = Update(24, 0, 24, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class Y1():
    # 'Update'!Y1
    value = 16
    formula = "=(COLUMN(Y1)-COLUMN($J1)+1)"
    @eval_fn
    def Y1():
        range_1 = Update(25, 0, 25, 0)
        var_1 = COLUMN(range_1)
        range_2 = Update(10, 0, 10, 0)
        var_2 = COLUMN(range_2)
        var_3 = sub(var_1, var_2)
        var_4 = add(var_3, 1)
        return var_4

@register(Update)
class Z1():
    # 'Update'!Z1
    value = "Notes"

@register(Update)
class A2():
    # 'Update'!A2
    value = "BLS Data"

@register(Update)
class B2():
    # 'Update'!B2
    value = "B8"

@register(Update)
class C2():
    # 'Update'!C2
    value = "http://www.bls.gov/ggs"

@register(Update)
class D2():
    # 'Update'!D2
    value = "NA"

@register(Update)
class E2():
    # 'Update'!E2
    value = "NA"

@register(Update)
class F2():
    # 'Update'!F2
    value = "NA"

@register(Update)
class G2():
    # 'Update'!G2
    value = "ggqcew.pdf"

@register(Update)
class H2():
    # 'Update'!H2
    value = "N"

@register(Update)
class I2():
    # 'Update'!I2
    value = 6

@register(Update)
class J2():
    # 'Update'!J2
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def J2():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K2():
    # 'Update'!K2
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def K2():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L2():
    # 'Update'!L2
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def L2():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M2():
    # 'Update'!M2
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def M2():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N2():
    # 'Update'!N2
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def N2():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O2():
    # 'Update'!O2
    value = "X"
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def O2():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P2():
    # 'Update'!P2
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def P2():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q2():
    # 'Update'!Q2
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def Q2():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R2():
    # 'Update'!R2
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def R2():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S2():
    # 'Update'!S2
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def S2():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T2():
    # 'Update'!T2
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def T2():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U2():
    # 'Update'!U2
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def U2():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V2():
    # 'Update'!V2
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def V2():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W2():
    # 'Update'!W2
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def W2():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X2():
    # 'Update'!X2
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def X2():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y2():
    # 'Update'!Y2
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I2&" ")),"","X")'''
    @eval_fn
    def Y2():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i2_1 = Update.I2()
        var_2 = concat(i2_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z2():
    # 'Update'!Z2
    value = "Best bet, but not expected to continue GGS"

@register(Update)
class A3():
    # 'Update'!A3
    value = "BrentCrudeMonthly"

@register(Update)
class B3():
    # 'Update'!B3
    value = "A316, A327"

@register(Update)
class C3():
    # 'Update'!C3
    value = "http://tonto.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RBRTE&f=M"

@register(Update)
class D3():
    # 'Update'!D3
    value = "M"

@register(Update)
class E3():
    # 'Update'!E3
    value = "~30th of each month"

@register(Update)
class F3():
    # 'Update'!F3
    value = "20 Minutes"

@register(Update)
class G3():
    # 'Update'!G3
    value = "RBRTEm.xls"

@register(Update)
class H3():
    # 'Update'!H3
    value = "Y"

@register(Update)
class I3():
    # 'Update'!I3
    value = "2 4 5 8 "

@register(Update)
class J3():
    # 'Update'!J3
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def J3():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K3():
    # 'Update'!K3
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def K3():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L3():
    # 'Update'!L3
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def L3():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M3():
    # 'Update'!M3
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def M3():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N3():
    # 'Update'!N3
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def N3():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O3():
    # 'Update'!O3
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def O3():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P3():
    # 'Update'!P3
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def P3():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q3():
    # 'Update'!Q3
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def Q3():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R3():
    # 'Update'!R3
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def R3():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S3():
    # 'Update'!S3
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def S3():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T3():
    # 'Update'!T3
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def T3():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U3():
    # 'Update'!U3
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def U3():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V3():
    # 'Update'!V3
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def V3():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W3():
    # 'Update'!W3
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def W3():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X3():
    # 'Update'!X3
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def X3():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y3():
    # 'Update'!Y3
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I3&" ")),"","X")'''
    @eval_fn
    def Y3():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i3_1 = Update.I3()
        var_2 = concat(i3_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z3():
    # 'Update'!Z3
    value = "Click Download Data (XLS File)"

@register(Update)
class A4():
    # 'Update'!A4
    value = "CarbonCoefficients"

@register(Update)
class B4():
    # 'Update'!B4
    value = "D:D"

@register(Update)
class C4():
    # 'Update'!C4
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Update)
class D4():
    # 'Update'!D4
    value = "NA"

@register(Update)
class E4():
    # 'Update'!E4
    value = "NA"

@register(Update)
class F4():
    # 'Update'!F4
    value = "2 Hours"

@register(Update)
class G4():
    # 'Update'!G4
    value = "US-GHG-Inventory-2010-Annexes.pdf"

@register(Update)
class I4():
    # 'Update'!I4
    value = "1 3"

@register(Update)
class J4():
    # 'Update'!J4
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def J4():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K4():
    # 'Update'!K4
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def K4():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L4():
    # 'Update'!L4
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def L4():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M4():
    # 'Update'!M4
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def M4():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N4():
    # 'Update'!N4
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def N4():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O4():
    # 'Update'!O4
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def O4():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P4():
    # 'Update'!P4
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def P4():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q4():
    # 'Update'!Q4
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def Q4():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R4():
    # 'Update'!R4
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def R4():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S4():
    # 'Update'!S4
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def S4():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T4():
    # 'Update'!T4
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def T4():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U4():
    # 'Update'!U4
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def U4():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V4():
    # 'Update'!V4
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def V4():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W4():
    # 'Update'!W4
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def W4():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X4():
    # 'Update'!X4
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def X4():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y4():
    # 'Update'!Y4
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I4&" ")),"","X")'''
    @eval_fn
    def Y4():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i4_1 = Update.I4()
        var_2 = concat(i4_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z4():
    # 'Update'!Z4
    value = "No updates expected, but if new numbers become available, update tables for all fuels, available throughout document"

@register(Update)
class A5():
    # 'Update'!A5
    value = "CoalForeignImports"

@register(Update)
class B5():
    # 'Update'!B5
    value = "A78"

@register(Update)
class C5():
    # 'Update'!C5
    value = "http://www.eia.gov/coal/archive/coal_historical_imports.xls"

@register(Update)
class D5():
    # 'Update'!D5
    value = "Q"

@register(Update)
class E5():
    # 'Update'!E5
    value = 41395

@register(Update)
class F5():
    # 'Update'!F5
    value = "20 Minutes"

@register(Update)
class G5():
    # 'Update'!G5
    value = "coal_historical_imports.xls"

@register(Update)
class I5():
    # 'Update'!I5
    value = 2

@register(Update)
class J5():
    # 'Update'!J5
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def J5():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K5():
    # 'Update'!K5
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def K5():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L5():
    # 'Update'!L5
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def L5():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M5():
    # 'Update'!M5
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def M5():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N5():
    # 'Update'!N5
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def N5():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O5():
    # 'Update'!O5
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def O5():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P5():
    # 'Update'!P5
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def P5():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q5():
    # 'Update'!Q5
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def Q5():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R5():
    # 'Update'!R5
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def R5():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S5():
    # 'Update'!S5
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def S5():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T5():
    # 'Update'!T5
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def T5():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U5():
    # 'Update'!U5
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def U5():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V5():
    # 'Update'!V5
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def V5():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W5():
    # 'Update'!W5
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def W5():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X5():
    # 'Update'!X5
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def X5():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y5():
    # 'Update'!Y5
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I5&" ")),"","X")'''
    @eval_fn
    def Y5():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i5_1 = Update.I5()
        var_2 = concat(i5_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z5():
    # 'Update'!Z5
    value = "Need to sort and copy only for port in Honolulu, HI. If full link doesn't work, try http://www.eia.gov/coal/data.cfm#imports; Check that columns are the same"

@register(Update)
class A6():
    # 'Update'!A6
    value = "DBEDT"

@register(Update)
class B6():
    # 'Update'!B6
    value = "CC5"

@register(Update)
class C6():
    # 'Update'!C6
    value = "http://files.hawaii.gov/dbedt/economic/data_reports/energy-trends/Monthly_Energy_Data.xlsx"

@register(Update)
class D6():
    # 'Update'!D6
    value = "M"

@register(Update)
class E6():
    # 'Update'!E6
    value = "~7th of each month"

@register(Update)
class F6():
    # 'Update'!F6
    value = "25 Minutes"

@register(Update)
class G6():
    # 'Update'!G6
    value = "Monthly_Energy_Data.xlsx"

@register(Update)
class H6():
    # 'Update'!H6
    value = "Y"

@register(Update)
class I6():
    # 'Update'!I6
    value = "1 2 3 4 5 8 12"

@register(Update)
class J6():
    # 'Update'!J6
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def J6():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K6():
    # 'Update'!K6
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def K6():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L6():
    # 'Update'!L6
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def L6():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M6():
    # 'Update'!M6
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def M6():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N6():
    # 'Update'!N6
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def N6():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O6():
    # 'Update'!O6
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def O6():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P6():
    # 'Update'!P6
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def P6():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q6():
    # 'Update'!Q6
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def Q6():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R6():
    # 'Update'!R6
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def R6():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S6():
    # 'Update'!S6
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def S6():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T6():
    # 'Update'!T6
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def T6():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U6():
    # 'Update'!U6
    value = "X"
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def U6():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V6():
    # 'Update'!V6
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def V6():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W6():
    # 'Update'!W6
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def W6():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X6():
    # 'Update'!X6
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def X6():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y6():
    # 'Update'!Y6
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I6&" ")),"","X")'''
    @eval_fn
    def Y6():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i6_1 = Update.I6()
        var_2 = concat(i6_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z6():
    # 'Update'!Z6
    value = '''Look for "Monthly Energy Trends" link. Biodiesel is presented by DEBDT on a monthly basis. Eia will begin to report on biodiesel in 2011. Check that rows are the same'''

@register(Update)
class A7():
    # 'Update'!A7
    value = "DomesticCoalImports"

@register(Update)
class B7():
    # 'Update'!B7
    value = "A7"

@register(Update)
class C7():
    # 'Update'!C7
    value = "http://www.eia.gov/coal/distribution/quarterly/"

@register(Update)
class D7():
    # 'Update'!D7
    value = "Q"

@register(Update)
class E7():
    # 'Update'!E7
    value = "Jan. Apr, Jul, Oct"

@register(Update)
class F7():
    # 'Update'!F7
    value = "25 Minutes"

@register(Update)
class G7():
    # 'Update'!G7
    value = "12q4_destination.xls"

@register(Update)
class I7():
    # 'Update'!I7
    value = 2

@register(Update)
class J7():
    # 'Update'!J7
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def J7():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K7():
    # 'Update'!K7
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def K7():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L7():
    # 'Update'!L7
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def L7():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M7():
    # 'Update'!M7
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def M7():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N7():
    # 'Update'!N7
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def N7():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O7():
    # 'Update'!O7
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def O7():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P7():
    # 'Update'!P7
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def P7():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q7():
    # 'Update'!Q7
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def Q7():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R7():
    # 'Update'!R7
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def R7():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S7():
    # 'Update'!S7
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def S7():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T7():
    # 'Update'!T7
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def T7():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U7():
    # 'Update'!U7
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def U7():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V7():
    # 'Update'!V7
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def V7():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W7():
    # 'Update'!W7
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def W7():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X7():
    # 'Update'!X7
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def X7():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y7():
    # 'Update'!Y7
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I7&" ")),"","X")'''
    @eval_fn
    def Y7():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i7_1 = Update.I7()
        var_2 = concat(i7_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z7():
    # 'Update'!Z7
    value = '''Update the most recent quarter at the bottom of the list. Use the "By Destination State" file; Check that columns are the same'''

@register(Update)
class A8():
    # 'Update'!A8
    value = "EIA Consumption"

@register(Update)
class B8():
    # 'Update'!B8
    value = "BD3"

@register(Update)
class C8():
    # 'Update'!C8
    value = "http://www.eia.gov/state/seds/seds-states.cfm?q_state_a=HI&q_state=Hawaii#undefined "

@register(Update)
class D8():
    # 'Update'!D8
    value = "A"

@register(Update)
class E8():
    # 'Update'!E8
    value = "~June 28th"

@register(Update)
class F8():
    # 'Update'!F8
    value = "25 Minutes"

@register(Update)
class G8():
    # 'Update'!G8
    value = "use_HI.csv"

@register(Update)
class H8():
    # 'Update'!H8
    value = "Y"

@register(Update)
class I8():
    # 'Update'!I8
    value = "1 2 3 4 5 8 12"

@register(Update)
class J8():
    # 'Update'!J8
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def J8():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K8():
    # 'Update'!K8
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def K8():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L8():
    # 'Update'!L8
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def L8():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M8():
    # 'Update'!M8
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def M8():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N8():
    # 'Update'!N8
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def N8():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O8():
    # 'Update'!O8
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def O8():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P8():
    # 'Update'!P8
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def P8():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q8():
    # 'Update'!Q8
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def Q8():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R8():
    # 'Update'!R8
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def R8():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S8():
    # 'Update'!S8
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def S8():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T8():
    # 'Update'!T8
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def T8():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U8():
    # 'Update'!U8
    value = "X"
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def U8():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V8():
    # 'Update'!V8
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def V8():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W8():
    # 'Update'!W8
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def W8():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X8():
    # 'Update'!X8
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def X8():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y8():
    # 'Update'!Y8
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I8&" ")),"","X")'''
    @eval_fn
    def Y8():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i8_1 = Update.I8()
        var_2 = concat(i8_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z8():
    # 'Update'!Z8
    value = '''Click on "Consumption" heating.  Download "All Consumption Estimates" CSV for Hawaii only. This is in the right column of links. Check that rows are the same'''

@register(Update)
class A9():
    # 'Update'!A9
    value = "EIA Expenditures"

@register(Update)
class B9():
    # 'Update'!B9
    value = "BD3"

@register(Update)
class C9():
    # 'Update'!C9
    value = "http://www.eia.gov/beta/state/seds/seds-data-complete.cfm?sid=HI#Prices & Expenditures "

@register(Update)
class D9():
    # 'Update'!D9
    value = "A"

@register(Update)
class E9():
    # 'Update'!E9
    value = "~June 28th"

@register(Update)
class F9():
    # 'Update'!F9
    value = "25 Minutes"

@register(Update)
class G9():
    # 'Update'!G9
    value = "pr_HI.csv"

@register(Update)
class H9():
    # 'Update'!H9
    value = "Y"

@register(Update)
class I9():
    # 'Update'!I9
    value = "2 4 5 8 "

@register(Update)
class J9():
    # 'Update'!J9
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def J9():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K9():
    # 'Update'!K9
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def K9():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L9():
    # 'Update'!L9
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def L9():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M9():
    # 'Update'!M9
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def M9():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N9():
    # 'Update'!N9
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def N9():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O9():
    # 'Update'!O9
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def O9():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P9():
    # 'Update'!P9
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def P9():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q9():
    # 'Update'!Q9
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def Q9():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R9():
    # 'Update'!R9
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def R9():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S9():
    # 'Update'!S9
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def S9():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T9():
    # 'Update'!T9
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def T9():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U9():
    # 'Update'!U9
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def U9():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V9():
    # 'Update'!V9
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def V9():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W9():
    # 'Update'!W9
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def W9():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X9():
    # 'Update'!X9
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def X9():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y9():
    # 'Update'!Y9
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I9&" ")),"","X")'''
    @eval_fn
    def Y9():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i9_1 = Update.I9()
        var_2 = concat(i9_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z9():
    # 'Update'!Z9
    value = '''In web page, click on "Prices and Expenditures"; click on "All Price and Expenditure Estimates" CSV. Check that all rows are the same'''

@register(Update)
class A10():
    # 'Update'!A10
    value = "Emissions"

@register(Update)
class B10():
    # 'Update'!B10
    value = "X4"

@register(Update)
class C10():
    # 'Update'!C10
    value = "http://epa.gov/statelocalclimate/resources/state_energyco2inv.html"

@register(Update)
class D10():
    # 'Update'!D10
    value = "A"

@register(Update)
class E10():
    # 'Update'!E10
    value = "~ July 23"

@register(Update)
class F10():
    # 'Update'!F10
    value = "20 Minutes"

@register(Update)
class G10():
    # 'Update'!G10
    value = "CO2FFC_2010.xlsx"

@register(Update)
class H10():
    # 'Update'!H10
    value = "Y"

@register(Update)
class I10():
    # 'Update'!I10
    value = "13 14 "

@register(Update)
class J10():
    # 'Update'!J10
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def J10():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K10():
    # 'Update'!K10
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def K10():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L10():
    # 'Update'!L10
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def L10():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M10():
    # 'Update'!M10
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def M10():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N10():
    # 'Update'!N10
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def N10():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O10():
    # 'Update'!O10
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def O10():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P10():
    # 'Update'!P10
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def P10():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q10():
    # 'Update'!Q10
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def Q10():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R10():
    # 'Update'!R10
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def R10():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S10():
    # 'Update'!S10
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def S10():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T10():
    # 'Update'!T10
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def T10():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U10():
    # 'Update'!U10
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def U10():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V10():
    # 'Update'!V10
    value = "X"
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def V10():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W10():
    # 'Update'!W10
    value = "X"
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def W10():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X10():
    # 'Update'!X10
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def X10():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y10():
    # 'Update'!Y10
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I10&" ")),"","X")'''
    @eval_fn
    def Y10():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i10_1 = Update.I10()
        var_2 = concat(i10_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z10():
    # 'Update'!Z10
    value = "Go to website and download most recent XLS"

@register(Update)
class A11():
    # 'Update'!A11
    value = "EthanolMonthly"

@register(Update)
class B11():
    # 'Update'!B11
    value = "A91"

@register(Update)
class C11():
    # 'Update'!C11
    value = "http://www.afdc.energy.gov/fuels/prices.html "

@register(Update)
class D11():
    # 'Update'!D11
    value = "Q"

@register(Update)
class E11():
    # 'Update'!E11
    value = "Jan. Apr, Jul, Oct"

@register(Update)
class F11():
    # 'Update'!F11
    value = "25 Minutes"

@register(Update)
class G11():
    # 'Update'!G11
    value = "alternative_fuel_price_report_april_2013.pdf"

@register(Update)
class H11():
    # 'Update'!H11
    value = "N"

@register(Update)
class I11():
    # 'Update'!I11
    value = "2 4 5 8"

@register(Update)
class J11():
    # 'Update'!J11
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def J11():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K11():
    # 'Update'!K11
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def K11():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L11():
    # 'Update'!L11
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def L11():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M11():
    # 'Update'!M11
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def M11():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N11():
    # 'Update'!N11
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def N11():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O11():
    # 'Update'!O11
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def O11():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P11():
    # 'Update'!P11
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def P11():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q11():
    # 'Update'!Q11
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def Q11():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R11():
    # 'Update'!R11
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def R11():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S11():
    # 'Update'!S11
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def S11():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T11():
    # 'Update'!T11
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def T11():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U11():
    # 'Update'!U11
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def U11():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V11():
    # 'Update'!V11
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def V11():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W11():
    # 'Update'!W11
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def W11():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X11():
    # 'Update'!X11
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def X11():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y11():
    # 'Update'!Y11
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I11&" ")),"","X")'''
    @eval_fn
    def Y11():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i11_1 = Update.I11()
        var_2 = concat(i11_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z11():
    # 'Update'!Z11
    value = "This is a PDF; use average Gulf Coast price for Ethanol E85 in table 7 for each month included in the average"

@register(Update)
class A12():
    # 'Update'!A12
    value = "existing_capacity_state"

@register(Update)
class B12():
    # 'Update'!B12
    value = "A32063"

@register(Update)
class C12():
    # 'Update'!C12
    value = "http://www.eia.gov/electricity/capacity/"

@register(Update)
class D12():
    # 'Update'!D12
    value = "6 MO."

@register(Update)
class E12():
    # 'Update'!E12
    value = "Jan; Aug"

@register(Update)
class F12():
    # 'Update'!F12
    value = "25 Minutes"

@register(Update)
class G12():
    # 'Update'!G12
    value = "existing_gen_units_2011.xls"

@register(Update)
class I12():
    # 'Update'!I12
    value = 15

@register(Update)
class J12():
    # 'Update'!J12
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def J12():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K12():
    # 'Update'!K12
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def K12():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L12():
    # 'Update'!L12
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def L12():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M12():
    # 'Update'!M12
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def M12():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N12():
    # 'Update'!N12
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def N12():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O12():
    # 'Update'!O12
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def O12():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P12():
    # 'Update'!P12
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def P12():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q12():
    # 'Update'!Q12
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def Q12():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R12():
    # 'Update'!R12
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def R12():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S12():
    # 'Update'!S12
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def S12():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T12():
    # 'Update'!T12
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def T12():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U12():
    # 'Update'!U12
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def U12():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V12():
    # 'Update'!V12
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def V12():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W12():
    # 'Update'!W12
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def W12():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X12():
    # 'Update'!X12
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def X12():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y12():
    # 'Update'!Y12
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I12&" ")),"","X")'''
    @eval_fn
    def Y12():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i12_1 = Update.I12()
        var_2 = concat(i12_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z12():
    # 'Update'!Z12
    value = '''Download "Existing Units by Energy Source" and sort by state. Be sure to allign columns correctly'''

@register(Update)
class A13():
    # 'Update'!A13
    value = "GSP"

@register(Update)
class B13():
    # 'Update'!B13
    value = "BD3"

@register(Update)
class C13():
    # 'Update'!C13
    value = "http://www.bea.gov/"

@register(Update)
class D13():
    # 'Update'!D13
    value = "A"

@register(Update)
class E13():
    # 'Update'!E13
    value = "~June 5th"

@register(Update)
class F13():
    # 'Update'!F13
    value = "25 Minutes"

@register(Update)
class G13():
    # 'Update'!G13
    value = "download.xls"

@register(Update)
class I13():
    # 'Update'!I13
    value = " 1 3 4 5 8 "

@register(Update)
class J13():
    # 'Update'!J13
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def J13():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K13():
    # 'Update'!K13
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def K13():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L13():
    # 'Update'!L13
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def L13():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M13():
    # 'Update'!M13
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def M13():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N13():
    # 'Update'!N13
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def N13():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O13():
    # 'Update'!O13
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def O13():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P13():
    # 'Update'!P13
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def P13():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q13():
    # 'Update'!Q13
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def Q13():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R13():
    # 'Update'!R13
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def R13():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S13():
    # 'Update'!S13
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def S13():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T13():
    # 'Update'!T13
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def T13():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U13():
    # 'Update'!U13
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def U13():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V13():
    # 'Update'!V13
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def V13():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W13():
    # 'Update'!W13
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def W13():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X13():
    # 'Update'!X13
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def X13():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y13():
    # 'Update'!Y13
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I13&" ")),"","X")'''
    @eval_fn
    def Y13():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i13_1 = Update.I13()
        var_2 = concat(i13_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z13():
    # 'Update'!Z13
    value = '''Go to the "Interactive Data" tab, Select GDP & Personal Income under Regional Economic Data heading. Expand Gross Domestic Prodcut By State, and click "Gross Domestic Product". Use NAICS from 1997 forward. Do not update row 4 - it is only for 1963-1994; '''

@register(Update)
class A14():
    # 'Update'!A14
    value = "GSP Deflator"

@register(Update)
class B14():
    # 'Update'!B14
    value = "AU3"

@register(Update)
class C14():
    # 'Update'!C14
    value = "http://www.ers.usda.gov/datafiles/International_Macroeconomic_Data/Historical_Data_Files/HistoricalGDPDeflatorValues.xls"

@register(Update)
class D14():
    # 'Update'!D14
    value = "A"

@register(Update)
class E14():
    # 'Update'!E14
    value = "End of November"

@register(Update)
class F14():
    # 'Update'!F14
    value = "25 Minutes"

@register(Update)
class G14():
    # 'Update'!G14
    value = "HistoricalGDPDeflatorValues.xls"

@register(Update)
class I14():
    # 'Update'!I14
    value = "1 3 4 5 8"

@register(Update)
class J14():
    # 'Update'!J14
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def J14():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K14():
    # 'Update'!K14
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def K14():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L14():
    # 'Update'!L14
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def L14():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M14():
    # 'Update'!M14
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def M14():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N14():
    # 'Update'!N14
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def N14():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O14():
    # 'Update'!O14
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def O14():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P14():
    # 'Update'!P14
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def P14():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q14():
    # 'Update'!Q14
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def Q14():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R14():
    # 'Update'!R14
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def R14():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S14():
    # 'Update'!S14
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def S14():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T14():
    # 'Update'!T14
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def T14():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U14():
    # 'Update'!U14
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def U14():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V14():
    # 'Update'!V14
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def V14():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W14():
    # 'Update'!W14
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def W14():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X14():
    # 'Update'!X14
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def X14():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y14():
    # 'Update'!Y14
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I14&" ")),"","X")'''
    @eval_fn
    def Y14():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i14_1 = Update.I14()
        var_2 = concat(i14_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class A15():
    # 'Update'!A15
    value = "Imports_Petrol"

@register(Update)
class B15():
    # 'Update'!B15
    value = "A3208"

@register(Update)
class C15():
    # 'Update'!C15
    value = '''http://www.eia.gov/petroleum/imports/companylevel/archive/
http://www.eia.gov/oil_gas/petroleum/data_publications/company_level_imports/cli_explanation.html '''

@register(Update)
class D15():
    # 'Update'!D15
    value = "M"

@register(Update)
class E15():
    # 'Update'!E15
    value = "~25th of each month"

@register(Update)
class F15():
    # 'Update'!F15
    value = "25 Minutes"

@register(Update)
class G15():
    # 'Update'!G15
    value = "import.xls"

@register(Update)
class I15():
    # 'Update'!I15
    value = "1 3 2"

@register(Update)
class J15():
    # 'Update'!J15
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def J15():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K15():
    # 'Update'!K15
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def K15():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L15():
    # 'Update'!L15
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def L15():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M15():
    # 'Update'!M15
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def M15():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N15():
    # 'Update'!N15
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def N15():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O15():
    # 'Update'!O15
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def O15():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P15():
    # 'Update'!P15
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def P15():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q15():
    # 'Update'!Q15
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def Q15():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R15():
    # 'Update'!R15
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def R15():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S15():
    # 'Update'!S15
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def S15():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T15():
    # 'Update'!T15
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def T15():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U15():
    # 'Update'!U15
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def U15():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V15():
    # 'Update'!V15
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def V15():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W15():
    # 'Update'!W15
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def W15():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X15():
    # 'Update'!X15
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def X15():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y15():
    # 'Update'!Y15
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I15&" ")),"","X")'''
    @eval_fn
    def Y15():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i15_1 = Update.I15()
        var_2 = concat(i15_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z15():
    # 'Update'!Z15
    value = "Check that columns are the same"

@register(Update)
class A16():
    # 'Update'!A16
    value = "RPS Inputs"

@register(Update)
class B16():
    # 'Update'!B16
    value = "T:T"

@register(Update)
class C16():
    # 'Update'!C16
    value = "http://www.heco.com/vcmcontent/StaticFiles/pdf/2012-05-04_RPS%20Report_2011.pdf  "

@register(Update)
class D16():
    # 'Update'!D16
    value = "A"

@register(Update)
class E16():
    # 'Update'!E16
    value = "November"

@register(Update)
class F16():
    # 'Update'!F16
    value = "2 Hours"

@register(Update)
class G16():
    # 'Update'!G16
    value = "2012-05-04_RPS Report_2011.pdf; FY 2012 HI PUC Annual Report.pdf"

@register(Update)
class H16():
    # 'Update'!H16
    value = "M"

@register(Update)
class I16():
    # 'Update'!I16
    value = "4 5 8 10 11 12 16"

@register(Update)
class J16():
    # 'Update'!J16
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def J16():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K16():
    # 'Update'!K16
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def K16():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L16():
    # 'Update'!L16
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def L16():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M16():
    # 'Update'!M16
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def M16():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N16():
    # 'Update'!N16
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def N16():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O16():
    # 'Update'!O16
    value = "X"
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def O16():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P16():
    # 'Update'!P16
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def P16():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q16():
    # 'Update'!Q16
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def Q16():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R16():
    # 'Update'!R16
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def R16():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S16():
    # 'Update'!S16
    value = "X"
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def S16():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T16():
    # 'Update'!T16
    value = "X"
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def T16():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U16():
    # 'Update'!U16
    value = "X"
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def U16():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V16():
    # 'Update'!V16
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def V16():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W16():
    # 'Update'!W16
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def W16():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X16():
    # 'Update'!X16
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def X16():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y16():
    # 'Update'!Y16
    value = "X"
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I16&" ")),"","X")'''
    @eval_fn
    def Y16():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i16_1 = Update.I16()
        var_2 = concat(i16_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z16():
    # 'Update'!Z16
    value = "PDF with a fairly manual update. Google HECO RPS REPORT for 2012; Report should contain tables detailing energy savings and renewable generation Note: Data are available in 2005 and later. A few aggregate datapoints are available prior to 2005 and are included. Should earlier data be found, they can be entered"

@register(Update)
class A17():
    # 'Update'!A17
    value = "RPS Inputs"

@register(Update)
class B17():
    # 'Update'!B17
    value = "T:T"

@register(Update)
class C17():
    # 'Update'!C17
    value = "http://puc.hawaii.gov/reports/puc-annual-reports"

@register(Update)
class D17():
    # 'Update'!D17
    value = "A"

@register(Update)
class E17():
    # 'Update'!E17
    value = "November"

@register(Update)
class F17():
    # 'Update'!F17
    value = "2 Hours"

@register(Update)
class G17():
    # 'Update'!G17
    value = "FY 2012 HI PUC Annual Report.pdf"

@register(Update)
class H17():
    # 'Update'!H17
    value = "M"

@register(Update)
class I17():
    # 'Update'!I17
    value = "4 5 8  10 11 12 15 16 "

@register(Update)
class J17():
    # 'Update'!J17
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def J17():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K17():
    # 'Update'!K17
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def K17():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L17():
    # 'Update'!L17
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def L17():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M17():
    # 'Update'!M17
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def M17():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N17():
    # 'Update'!N17
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def N17():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O17():
    # 'Update'!O17
    value = "X"
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def O17():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P17():
    # 'Update'!P17
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def P17():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q17():
    # 'Update'!Q17
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def Q17():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R17():
    # 'Update'!R17
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def R17():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S17():
    # 'Update'!S17
    value = "X"
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def S17():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T17():
    # 'Update'!T17
    value = "X"
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def T17():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U17():
    # 'Update'!U17
    value = "X"
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def U17():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V17():
    # 'Update'!V17
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def V17():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W17():
    # 'Update'!W17
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def W17():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X17():
    # 'Update'!X17
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def X17():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y17():
    # 'Update'!Y17
    value = "X"
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I17&" ")),"","X")'''
    @eval_fn
    def Y17():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i17_1 = Update.I17()
        var_2 = concat(i17_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z17():
    # 'Update'!Z17
    value = "Additional data, particularly for KIUC"

@register(Update)
class A18():
    # 'Update'!A18
    value = "Jet Fuel"

@register(Update)
class B18():
    # 'Update'!B18
    value = "C348"

@register(Update)
class C18():
    # 'Update'!C18
    value = "http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EER_EPJK_PF4_RGC_DPG&f=M"

@register(Update)
class D18():
    # 'Update'!D18
    value = "M"

@register(Update)
class E18():
    # 'Update'!E18
    value = "~30th of each month"

@register(Update)
class F18():
    # 'Update'!F18
    value = "20 Minutes"

@register(Update)
class G18():
    # 'Update'!G18
    value = "EER_EPJK_PF4_RGC_DPGm.xls"

@register(Update)
class I18():
    # 'Update'!I18
    value = "2 4 5 8"

@register(Update)
class J18():
    # 'Update'!J18
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def J18():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K18():
    # 'Update'!K18
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def K18():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L18():
    # 'Update'!L18
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def L18():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M18():
    # 'Update'!M18
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def M18():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N18():
    # 'Update'!N18
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def N18():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O18():
    # 'Update'!O18
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def O18():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P18():
    # 'Update'!P18
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def P18():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q18():
    # 'Update'!Q18
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def Q18():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R18():
    # 'Update'!R18
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def R18():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S18():
    # 'Update'!S18
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def S18():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T18():
    # 'Update'!T18
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def T18():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U18():
    # 'Update'!U18
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def U18():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V18():
    # 'Update'!V18
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def V18():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W18():
    # 'Update'!W18
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def W18():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X18():
    # 'Update'!X18
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def X18():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y18():
    # 'Update'!Y18
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I18&" ")),"","X")'''
    @eval_fn
    def Y18():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i18_1 = Update.I18()
        var_2 = concat(i18_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z18():
    # 'Update'!Z18
    value = "Click Download Data (XLS File)"

@register(Update)
class A19():
    # 'Update'!A19
    value = "LCEFbyFuelType"

@register(Update)
class B19():
    # 'Update'!B19
    value = "B4"

@register(Update)
class C19():
    # 'Update'!C19
    value = "http://www.netl.doe.gov/energy-analyses/pubs/NETL%20LCA%20Petroleum-based%20Fuels%20Nov%202008.pdf "

@register(Update)
class D19():
    # 'Update'!D19
    value = "NA"

@register(Update)
class E19():
    # 'Update'!E19
    value = "NA"

@register(Update)
class F19():
    # 'Update'!F19
    value = "45 minutes"

@register(Update)
class G19():
    # 'Update'!G19
    value = "NETL LCA Petroleum-based Fuels Nov 2008.pdf"

@register(Update)
class I19():
    # 'Update'!I19
    value = "1 3"

@register(Update)
class J19():
    # 'Update'!J19
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def J19():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K19():
    # 'Update'!K19
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def K19():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L19():
    # 'Update'!L19
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def L19():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M19():
    # 'Update'!M19
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def M19():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N19():
    # 'Update'!N19
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def N19():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O19():
    # 'Update'!O19
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def O19():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P19():
    # 'Update'!P19
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def P19():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q19():
    # 'Update'!Q19
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def Q19():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R19():
    # 'Update'!R19
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def R19():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S19():
    # 'Update'!S19
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def S19():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T19():
    # 'Update'!T19
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def T19():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U19():
    # 'Update'!U19
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def U19():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V19():
    # 'Update'!V19
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def V19():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W19():
    # 'Update'!W19
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def W19():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X19():
    # 'Update'!X19
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def X19():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y19():
    # 'Update'!Y19
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I19&" ")),"","X")'''
    @eval_fn
    def Y19():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i19_1 = Update.I19()
        var_2 = concat(i19_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z19():
    # 'Update'!Z19
    value = "No updates expected, but if new numbers become available, update tables for Jet Fuel, Gasoline, and Diesel"

@register(Update)
class A20():
    # 'Update'!A20
    value = "LCEFbyFuelType"

@register(Update)
class B20():
    # 'Update'!B20
    value = "B23"

@register(Update)
class C20():
    # 'Update'!C20
    value = "NG-GHG-LCI.pdf"

@register(Update)
class D20():
    # 'Update'!D20
    value = "NA"

@register(Update)
class E20():
    # 'Update'!E20
    value = "NA"

@register(Update)
class F20():
    # 'Update'!F20
    value = "45 minutes"

@register(Update)
class G20():
    # 'Update'!G20
    value = "NETL LCA Petroleum-based Fuels Nov 2008.pdf"

@register(Update)
class I20():
    # 'Update'!I20
    value = "1 3"

@register(Update)
class J20():
    # 'Update'!J20
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def J20():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K20():
    # 'Update'!K20
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def K20():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L20():
    # 'Update'!L20
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def L20():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M20():
    # 'Update'!M20
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def M20():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N20():
    # 'Update'!N20
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def N20():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O20():
    # 'Update'!O20
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def O20():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P20():
    # 'Update'!P20
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def P20():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q20():
    # 'Update'!Q20
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def Q20():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R20():
    # 'Update'!R20
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def R20():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S20():
    # 'Update'!S20
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def S20():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T20():
    # 'Update'!T20
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def T20():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U20():
    # 'Update'!U20
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def U20():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V20():
    # 'Update'!V20
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def V20():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W20():
    # 'Update'!W20
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def W20():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X20():
    # 'Update'!X20
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def X20():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y20():
    # 'Update'!Y20
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I20&" ")),"","X")'''
    @eval_fn
    def Y20():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i20_1 = Update.I20()
        var_2 = concat(i20_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z20():
    # 'Update'!Z20
    value = "No updates expected, but if new numbers become available, update tables for Natural Gas"

@register(Update)
class A21():
    # 'Update'!A21
    value = "LCEFbyFuelType"

@register(Update)
class B21():
    # 'Update'!B21
    value = "X13"

@register(Update)
class C21():
    # 'Update'!C21
    value = "http://www.uhero.hawaii.edu/assets/20120531_BiofuelLCAReportFinal_kt.pdf "

@register(Update)
class D21():
    # 'Update'!D21
    value = "NA"

@register(Update)
class E21():
    # 'Update'!E21
    value = "NA"

@register(Update)
class F21():
    # 'Update'!F21
    value = "45 minutes"

@register(Update)
class G21():
    # 'Update'!G21
    value = "20120531_BiofuelLCAReportFinal_kt.pdf"

@register(Update)
class I21():
    # 'Update'!I21
    value = "1 3"

@register(Update)
class J21():
    # 'Update'!J21
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def J21():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K21():
    # 'Update'!K21
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def K21():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L21():
    # 'Update'!L21
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def L21():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M21():
    # 'Update'!M21
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def M21():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N21():
    # 'Update'!N21
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def N21():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O21():
    # 'Update'!O21
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def O21():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P21():
    # 'Update'!P21
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def P21():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q21():
    # 'Update'!Q21
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def Q21():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R21():
    # 'Update'!R21
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def R21():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S21():
    # 'Update'!S21
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def S21():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T21():
    # 'Update'!T21
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def T21():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U21():
    # 'Update'!U21
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def U21():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V21():
    # 'Update'!V21
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def V21():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W21():
    # 'Update'!W21
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def W21():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X21():
    # 'Update'!X21
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def X21():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y21():
    # 'Update'!Y21
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I21&" ")),"","X")'''
    @eval_fn
    def Y21():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i21_1 = Update.I21()
        var_2 = concat(i21_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z21():
    # 'Update'!Z21
    value = "No updates expected, but if new numbers become available, update tables for Coal; See Table7: Emission factors for different stages of fuel processing (g CO2-eq/MJ)"

@register(Update)
class A22():
    # 'Update'!A22
    value = "LCEFbyFuelType"

@register(Update)
class B22():
    # 'Update'!B22
    value = "H23"

@register(Update)
class C22():
    # 'Update'!C22
    value = "http://www.netl.doe.gov/energy-analyses/pubs/NG-GHG-LCI.pdf "

@register(Update)
class D22():
    # 'Update'!D22
    value = "NA"

@register(Update)
class E22():
    # 'Update'!E22
    value = "NA"

@register(Update)
class F22():
    # 'Update'!F22
    value = "45 minutes"

@register(Update)
class G22():
    # 'Update'!G22
    value = "NG-GHG-LCI.pdf"

@register(Update)
class I22():
    # 'Update'!I22
    value = "1 3"

@register(Update)
class J22():
    # 'Update'!J22
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def J22():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K22():
    # 'Update'!K22
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def K22():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L22():
    # 'Update'!L22
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def L22():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M22():
    # 'Update'!M22
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def M22():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N22():
    # 'Update'!N22
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def N22():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O22():
    # 'Update'!O22
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def O22():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P22():
    # 'Update'!P22
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def P22():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q22():
    # 'Update'!Q22
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def Q22():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R22():
    # 'Update'!R22
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def R22():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S22():
    # 'Update'!S22
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def S22():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T22():
    # 'Update'!T22
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def T22():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U22():
    # 'Update'!U22
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def U22():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V22():
    # 'Update'!V22
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def V22():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W22():
    # 'Update'!W22
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def W22():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X22():
    # 'Update'!X22
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def X22():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y22():
    # 'Update'!Y22
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I22&" ")),"","X")'''
    @eval_fn
    def Y22():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i22_1 = Update.I22()
        var_2 = concat(i22_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z22():
    # 'Update'!Z22
    value = "No updates expected, but if new numbers become available, update tables for Coal; See figure 3-8 for data"

@register(Update)
class A23():
    # 'Update'!A23
    value = "LCEFbyFuelType"

@register(Update)
class B23():
    # 'Update'!B23
    value = "X28"

@register(Update)
class C23():
    # 'Update'!C23
    value = "http://www.netl.doe.gov/energy-analyses/pubs/EthFrBioLCA101811Pres.pdf"

@register(Update)
class D23():
    # 'Update'!D23
    value = "NA"

@register(Update)
class E23():
    # 'Update'!E23
    value = "NA"

@register(Update)
class F23():
    # 'Update'!F23
    value = "45 minutes"

@register(Update)
class G23():
    # 'Update'!G23
    value = "EthFrBioLCA101811Pres.pdf"

@register(Update)
class I23():
    # 'Update'!I23
    value = "1 3"

@register(Update)
class J23():
    # 'Update'!J23
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def J23():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K23():
    # 'Update'!K23
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def K23():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L23():
    # 'Update'!L23
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def L23():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M23():
    # 'Update'!M23
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def M23():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N23():
    # 'Update'!N23
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def N23():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O23():
    # 'Update'!O23
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def O23():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P23():
    # 'Update'!P23
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def P23():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q23():
    # 'Update'!Q23
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def Q23():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R23():
    # 'Update'!R23
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def R23():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S23():
    # 'Update'!S23
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def S23():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T23():
    # 'Update'!T23
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def T23():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U23():
    # 'Update'!U23
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def U23():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V23():
    # 'Update'!V23
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def V23():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W23():
    # 'Update'!W23
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def W23():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X23():
    # 'Update'!X23
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def X23():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y23():
    # 'Update'!Y23
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I23&" ")),"","X")'''
    @eval_fn
    def Y23():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i23_1 = Update.I23()
        var_2 = concat(i23_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z23():
    # 'Update'!Z23
    value = "No updates expected, but if new numbers become available, update tables for Ethanol; See Slide 26 for data"

@register(Update)
class A24():
    # 'Update'!A24
    value = "LPG"

@register(Update)
class B24():
    # 'Update'!B24
    value = "C254"

@register(Update)
class C24():
    # 'Update'!C24
    value = "http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=eer_epllpa_pf4_y44mb_dpg&f=d"

@register(Update)
class D24():
    # 'Update'!D24
    value = "M"

@register(Update)
class E24():
    # 'Update'!E24
    value = "~30th of each month"

@register(Update)
class F24():
    # 'Update'!F24
    value = "20 Minutes"

@register(Update)
class G24():
    # 'Update'!G24
    value = "EER_EPLLPA_PF4_Y44MB_DPGd.xls"

@register(Update)
class I24():
    # 'Update'!I24
    value = "4 5 8"

@register(Update)
class J24():
    # 'Update'!J24
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def J24():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K24():
    # 'Update'!K24
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def K24():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L24():
    # 'Update'!L24
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def L24():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M24():
    # 'Update'!M24
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def M24():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N24():
    # 'Update'!N24
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def N24():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O24():
    # 'Update'!O24
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def O24():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P24():
    # 'Update'!P24
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def P24():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q24():
    # 'Update'!Q24
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def Q24():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R24():
    # 'Update'!R24
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def R24():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S24():
    # 'Update'!S24
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def S24():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T24():
    # 'Update'!T24
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def T24():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U24():
    # 'Update'!U24
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def U24():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V24():
    # 'Update'!V24
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def V24():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W24():
    # 'Update'!W24
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def W24():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X24():
    # 'Update'!X24
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def X24():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y24():
    # 'Update'!Y24
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I24&" ")),"","X")'''
    @eval_fn
    def Y24():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i24_1 = Update.I24()
        var_2 = concat(i24_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z24():
    # 'Update'!Z24
    value = "Click Download Data (XLS File)"

@register(Update)
class A25():
    # 'Update'!A25
    value = "New Plants"

@register(Update)
class B25():
    # 'Update'!B25
    value = "A50"

@register(Update)
class C25():
    # 'Update'!C25
    value = "http://www.eia.gov/electricity/capacity/"

@register(Update)
class D25():
    # 'Update'!D25
    value = "6 MO."

@register(Update)
class E25():
    # 'Update'!E25
    value = "Jan; Aug"

@register(Update)
class F25():
    # 'Update'!F25
    value = "25 Minutes"

@register(Update)
class G25():
    # 'Update'!G25
    value = "additions_2011.xls"

@register(Update)
class I25():
    # 'Update'!I25
    value = "15"

@register(Update)
class J25():
    # 'Update'!J25
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def J25():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K25():
    # 'Update'!K25
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def K25():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L25():
    # 'Update'!L25
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def L25():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M25():
    # 'Update'!M25
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def M25():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N25():
    # 'Update'!N25
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def N25():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O25():
    # 'Update'!O25
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def O25():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P25():
    # 'Update'!P25
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def P25():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q25():
    # 'Update'!Q25
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def Q25():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R25():
    # 'Update'!R25
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def R25():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S25():
    # 'Update'!S25
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def S25():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T25():
    # 'Update'!T25
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def T25():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U25():
    # 'Update'!U25
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def U25():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V25():
    # 'Update'!V25
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def V25():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W25():
    # 'Update'!W25
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def W25():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X25():
    # 'Update'!X25
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def X25():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y25():
    # 'Update'!Y25
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I25&" ")),"","X")'''
    @eval_fn
    def Y25():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i25_1 = Update.I25()
        var_2 = concat(i25_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z25():
    # 'Update'!Z25
    value = '''Download "Unit Additions" and sort by state. Be sure to allign columns correctly; Data not used directly in calculations, but good for reference'''

@register(Update)
class A26():
    # 'Update'!A26
    value = "Planned Capacity"

@register(Update)
class B26():
    # 'Update'!B26
    value = "A438"

@register(Update)
class C26():
    # 'Update'!C26
    value = "http://www.eia.gov/cneaf/electricity/epa/planned_capacity_state.xls"

@register(Update)
class D26():
    # 'Update'!D26
    value = "Unsure"

@register(Update)
class E26():
    # 'Update'!E26
    value = "Supposedly Nov 2012, release not yet seen"

@register(Update)
class F26():
    # 'Update'!F26
    value = "20 Minutes"

@register(Update)
class G26():
    # 'Update'!G26
    value = "planned_capacity_state.xls"

@register(Update)
class I26():
    # 'Update'!I26
    value = "15"

@register(Update)
class J26():
    # 'Update'!J26
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def J26():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K26():
    # 'Update'!K26
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def K26():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L26():
    # 'Update'!L26
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def L26():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M26():
    # 'Update'!M26
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def M26():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N26():
    # 'Update'!N26
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def N26():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O26():
    # 'Update'!O26
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def O26():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P26():
    # 'Update'!P26
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def P26():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q26():
    # 'Update'!Q26
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def Q26():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R26():
    # 'Update'!R26
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def R26():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S26():
    # 'Update'!S26
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def S26():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T26():
    # 'Update'!T26
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def T26():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U26():
    # 'Update'!U26
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def U26():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V26():
    # 'Update'!V26
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def V26():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W26():
    # 'Update'!W26
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def W26():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X26():
    # 'Update'!X26
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def X26():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y26():
    # 'Update'!Y26
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I26&" ")),"","X")'''
    @eval_fn
    def Y26():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i26_1 = Update.I26()
        var_2 = concat(i26_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z26():
    # 'Update'!Z26
    value = "Link should provide most recent list of proposed generation;  Data not used directly in calculations, but good for reference"

@register(Update)
class A27():
    # 'Update'!A27
    value = "Population"

@register(Update)
class B27():
    # 'Update'!B27
    value = "C21"

@register(Update)
class C27():
    # 'Update'!C27
    value = '''http://www.quandl.com/UHERO-University-of-Hawaii/40_Y-Population-Hawaii-Statewide-annual
http://hawaii.gov/dbedt/info/economic/databook/2010-individual/13/130310.pdf '''

@register(Update)
class D27():
    # 'Update'!D27
    value = "A"

@register(Update)
class E27():
    # 'Update'!E27
    value = "Unknown"

@register(Update)
class F27():
    # 'Update'!F27
    value = "25 Minutes"

@register(Update)
class G27():
    # 'Update'!G27
    value = "40_Y.csv"

@register(Update)
class I27():
    # 'Update'!I27
    value = "1 3"

@register(Update)
class J27():
    # 'Update'!J27
    value = "X"
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def J27():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K27():
    # 'Update'!K27
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def K27():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L27():
    # 'Update'!L27
    value = "X"
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def L27():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M27():
    # 'Update'!M27
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def M27():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N27():
    # 'Update'!N27
    value = None
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def N27():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O27():
    # 'Update'!O27
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def O27():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P27():
    # 'Update'!P27
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def P27():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q27():
    # 'Update'!Q27
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def Q27():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R27():
    # 'Update'!R27
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def R27():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S27():
    # 'Update'!S27
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def S27():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T27():
    # 'Update'!T27
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def T27():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U27():
    # 'Update'!U27
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def U27():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V27():
    # 'Update'!V27
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def V27():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W27():
    # 'Update'!W27
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def W27():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X27():
    # 'Update'!X27
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def X27():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y27():
    # 'Update'!Y27
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I27&" ")),"","X")'''
    @eval_fn
    def Y27():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i27_1 = Update.I27()
        var_2 = concat(i27_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z27():
    # 'Update'!Z27
    value = "Make sure to get De Facto Population. Click on De Facto Population, then click download. You must create a free account and be logged in to download. Make sure columns are in the same order"

@register(Update)
class A28():
    # 'Update'!A28
    value = "Projects in Pipeline"

@register(Update)
class B28():
    # 'Update'!B28
    value = "A44"

@register(Update)
class C28():
    # 'Update'!C28
    value = "http://energy.hawaii.gov/programs/renewable-energy-projects-in-hawaii"

@register(Update)
class D28():
    # 'Update'!D28
    value = "Variable"

@register(Update)
class E28():
    # 'Update'!E28
    value = "last update seen in Oct 2012"

@register(Update)
class F28():
    # 'Update'!F28
    value = "15 Minutes"

@register(Update)
class G28():
    # 'Update'!G28
    value = "Website"

@register(Update)
class I28():
    # 'Update'!I28
    value = 15

@register(Update)
class J28():
    # 'Update'!J28
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def J28():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K28():
    # 'Update'!K28
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def K28():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L28():
    # 'Update'!L28
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def L28():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M28():
    # 'Update'!M28
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def M28():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N28():
    # 'Update'!N28
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def N28():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O28():
    # 'Update'!O28
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def O28():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P28():
    # 'Update'!P28
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def P28():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q28():
    # 'Update'!Q28
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def Q28():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R28():
    # 'Update'!R28
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def R28():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S28():
    # 'Update'!S28
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def S28():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T28():
    # 'Update'!T28
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def T28():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U28():
    # 'Update'!U28
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def U28():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V28():
    # 'Update'!V28
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def V28():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W28():
    # 'Update'!W28
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def W28():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X28():
    # 'Update'!X28
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def X28():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y28():
    # 'Update'!Y28
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I28&" ")),"","X")'''
    @eval_fn
    def Y28():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i28_1 = Update.I28()
        var_2 = concat(i28_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z28():
    # 'Update'!Z28
    value = "Link should provide most recent list of proposed generation;  Data not used directly in calculations, but good for reference"

@register(Update)
class A29():
    # 'Update'!A29
    value = "Projects List"

@register(Update)
class B29():
    # 'Update'!B29
    value = "A93"

@register(Update)
class C29():
    # 'Update'!C29
    value = "https://energy.ehawaii.gov/epd/public/energy-projects-list.html"

@register(Update)
class D29():
    # 'Update'!D29
    value = "Ongoing"

@register(Update)
class F29():
    # 'Update'!F29
    value = "15 Minutes"

@register(Update)
class G29():
    # 'Update'!G29
    value = "Website"

@register(Update)
class I29():
    # 'Update'!I29
    value = 15

@register(Update)
class J29():
    # 'Update'!J29
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def J29():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K29():
    # 'Update'!K29
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def K29():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L29():
    # 'Update'!L29
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def L29():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M29():
    # 'Update'!M29
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def M29():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N29():
    # 'Update'!N29
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def N29():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O29():
    # 'Update'!O29
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def O29():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P29():
    # 'Update'!P29
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def P29():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q29():
    # 'Update'!Q29
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def Q29():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R29():
    # 'Update'!R29
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def R29():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S29():
    # 'Update'!S29
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def S29():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T29():
    # 'Update'!T29
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def T29():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U29():
    # 'Update'!U29
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def U29():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V29():
    # 'Update'!V29
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def V29():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W29():
    # 'Update'!W29
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def W29():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X29():
    # 'Update'!X29
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def X29():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y29():
    # 'Update'!Y29
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I29&" ")),"","X")'''
    @eval_fn
    def Y29():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i29_1 = Update.I29()
        var_2 = concat(i29_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z29():
    # 'Update'!Z29
    value = "Link should provide most recent list of proposed generation;  Data not used directly in calculations, but good for reference"

@register(Update)
class A30():
    # 'Update'!A30
    value = "PV"

@register(Update)
class B30():
    # 'Update'!B30
    value = "P6"

@register(Update)
class C30():
    # 'Update'!C30
    value = "http://www.heco.com/portal/site/heco/menuitem.20516707928314340b4c0610c510b1ca/?vgnextoid=3be8e20c52a1b310VgnVCM10000005041aacRCRD&vgnextfmt=default "

@register(Update)
class D30():
    # 'Update'!D30
    value = "A"

@register(Update)
class E30():
    # 'Update'!E30
    value = "April"

@register(Update)
class F30():
    # 'Update'!F30
    value = "15 Minutes"

@register(Update)
class G30():
    # 'Update'!G30
    value = "PVSummary_1stQtr2013.pdf"

@register(Update)
class I30():
    # 'Update'!I30
    value = 15

@register(Update)
class J30():
    # 'Update'!J30
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def J30():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K30():
    # 'Update'!K30
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def K30():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L30():
    # 'Update'!L30
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def L30():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M30():
    # 'Update'!M30
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def M30():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N30():
    # 'Update'!N30
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def N30():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O30():
    # 'Update'!O30
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def O30():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P30():
    # 'Update'!P30
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def P30():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q30():
    # 'Update'!Q30
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def Q30():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R30():
    # 'Update'!R30
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def R30():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S30():
    # 'Update'!S30
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def S30():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T30():
    # 'Update'!T30
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def T30():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U30():
    # 'Update'!U30
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def U30():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V30():
    # 'Update'!V30
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def V30():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W30():
    # 'Update'!W30
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def W30():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X30():
    # 'Update'!X30
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def X30():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y30():
    # 'Update'!Y30
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I30&" ")),"","X")'''
    @eval_fn
    def Y30():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i30_1 = Update.I30()
        var_2 = concat(i30_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z30():
    # 'Update'!Z30
    value = "PDF document has updated PV capacity numbers"

@register(Update)
class A31():
    # 'Update'!A31
    value = "PV"

@register(Update)
class B31():
    # 'Update'!B31
    value = "P7"

@register(Update)
class C31():
    # 'Update'!C31
    value = "KIUC numbers can be found in NEM Filing to PUC"

@register(Update)
class D31():
    # 'Update'!D31
    value = "A"

@register(Update)
class E31():
    # 'Update'!E31
    value = "May"

@register(Update)
class F31():
    # 'Update'!F31
    value = "15 Minutes"

@register(Update)
class G31():
    # 'Update'!G31
    value = "KIUC NEM Report 2012.pdf"

@register(Update)
class I31():
    # 'Update'!I31
    value = 15

@register(Update)
class J31():
    # 'Update'!J31
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def J31():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K31():
    # 'Update'!K31
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def K31():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L31():
    # 'Update'!L31
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def L31():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M31():
    # 'Update'!M31
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def M31():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N31():
    # 'Update'!N31
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def N31():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O31():
    # 'Update'!O31
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def O31():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P31():
    # 'Update'!P31
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def P31():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q31():
    # 'Update'!Q31
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def Q31():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R31():
    # 'Update'!R31
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def R31():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S31():
    # 'Update'!S31
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def S31():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T31():
    # 'Update'!T31
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def T31():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U31():
    # 'Update'!U31
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def U31():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V31():
    # 'Update'!V31
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def V31():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W31():
    # 'Update'!W31
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def W31():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X31():
    # 'Update'!X31
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def X31():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y31():
    # 'Update'!Y31
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I31&" ")),"","X")'''
    @eval_fn
    def Y31():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i31_1 = Update.I31()
        var_2 = concat(i31_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z31():
    # 'Update'!Z31
    value = "PDF NEM Filing has updated PC capacity numbers"

@register(Update)
class A32():
    # 'Update'!A32
    value = "ResFuelOilMonthly"

@register(Update)
class B32():
    # 'Update'!B32
    value = "A326"

@register(Update)
class C32():
    # 'Update'!C32
    value = "http://tonto.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMA_EPPR_PWG_NUS_DPG&f=M"

@register(Update)
class D32():
    # 'Update'!D32
    value = "M"

@register(Update)
class E32():
    # 'Update'!E32
    value = "~30th of each month"

@register(Update)
class F32():
    # 'Update'!F32
    value = "20 Minutes"

@register(Update)
class G32():
    # 'Update'!G32
    value = "EMA_EPPR_PWG_NUS_DPGm.xls"

@register(Update)
class I32():
    # 'Update'!I32
    value = "2 4 5 8"

@register(Update)
class J32():
    # 'Update'!J32
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def J32():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K32():
    # 'Update'!K32
    value = "X"
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def K32():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L32():
    # 'Update'!L32
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def L32():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M32():
    # 'Update'!M32
    value = "X"
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def M32():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N32():
    # 'Update'!N32
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def N32():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O32():
    # 'Update'!O32
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def O32():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P32():
    # 'Update'!P32
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def P32():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q32():
    # 'Update'!Q32
    value = "X"
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def Q32():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R32():
    # 'Update'!R32
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def R32():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S32():
    # 'Update'!S32
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def S32():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T32():
    # 'Update'!T32
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def T32():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U32():
    # 'Update'!U32
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def U32():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V32():
    # 'Update'!V32
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def V32():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W32():
    # 'Update'!W32
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def W32():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X32():
    # 'Update'!X32
    value = None
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def X32():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y32():
    # 'Update'!Y32
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I32&" ")),"","X")'''
    @eval_fn
    def Y32():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i32_1 = Update.I32()
        var_2 = concat(i32_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z32():
    # 'Update'!Z32
    value = "Click Download Data (XLS File)"

@register(Update)
class A33():
    # 'Update'!A33
    value = "Retirements"

@register(Update)
class B33():
    # 'Update'!B33
    value = "A33"

@register(Update)
class C33():
    # 'Update'!C33
    value = "http://www.eia.gov/electricity/capacity/"

@register(Update)
class D33():
    # 'Update'!D33
    value = "6 MO."

@register(Update)
class E33():
    # 'Update'!E33
    value = "Jan; Aug"

@register(Update)
class F33():
    # 'Update'!F33
    value = "25 Minutes"

@register(Update)
class G33():
    # 'Update'!G33
    value = "retirements_2011.xls"

@register(Update)
class I33():
    # 'Update'!I33
    value = 15

@register(Update)
class J33():
    # 'Update'!J33
    value = None
    formula = '''=IF(ISERROR(FIND(J$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def J33():
        j1_1 = Update.J1()
        var_1 = concat(j1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class K33():
    # 'Update'!K33
    value = None
    formula = '''=IF(ISERROR(FIND(K$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def K33():
        k1_1 = Update.K1()
        var_1 = concat(k1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class L33():
    # 'Update'!L33
    value = None
    formula = '''=IF(ISERROR(FIND(L$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def L33():
        l1_1 = Update.L1()
        var_1 = concat(l1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class M33():
    # 'Update'!M33
    value = None
    formula = '''=IF(ISERROR(FIND(M$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def M33():
        m1_1 = Update.M1()
        var_1 = concat(m1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class N33():
    # 'Update'!N33
    value = "X"
    formula = '''=IF(ISERROR(FIND(N$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def N33():
        n1_1 = Update.N1()
        var_1 = concat(n1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class O33():
    # 'Update'!O33
    value = None
    formula = '''=IF(ISERROR(FIND(O$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def O33():
        o1_1 = Update.O1()
        var_1 = concat(o1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class P33():
    # 'Update'!P33
    value = None
    formula = '''=IF(ISERROR(FIND(P$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def P33():
        p1_1 = Update.P1()
        var_1 = concat(p1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Q33():
    # 'Update'!Q33
    value = None
    formula = '''=IF(ISERROR(FIND(Q$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def Q33():
        q1_1 = Update.Q1()
        var_1 = concat(q1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class R33():
    # 'Update'!R33
    value = None
    formula = '''=IF(ISERROR(FIND(R$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def R33():
        r1_1 = Update.R1()
        var_1 = concat(r1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class S33():
    # 'Update'!S33
    value = None
    formula = '''=IF(ISERROR(FIND(S$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def S33():
        s1_1 = Update.S1()
        var_1 = concat(s1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class T33():
    # 'Update'!T33
    value = None
    formula = '''=IF(ISERROR(FIND(T$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def T33():
        t1_1 = Update.T1()
        var_1 = concat(t1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class U33():
    # 'Update'!U33
    value = None
    formula = '''=IF(ISERROR(FIND(U$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def U33():
        u1_1 = Update.U1()
        var_1 = concat(u1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class V33():
    # 'Update'!V33
    value = None
    formula = '''=IF(ISERROR(FIND(V$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def V33():
        v1_1 = Update.V1()
        var_1 = concat(v1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class W33():
    # 'Update'!W33
    value = None
    formula = '''=IF(ISERROR(FIND(W$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def W33():
        w1_1 = Update.W1()
        var_1 = concat(w1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class X33():
    # 'Update'!X33
    value = "X"
    formula = '''=IF(ISERROR(FIND(X$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def X33():
        x1_1 = Update.X1()
        var_1 = concat(x1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Y33():
    # 'Update'!Y33
    value = None
    formula = '''=IF(ISERROR(FIND(Y$1&" ",$I33&" ")),"","X")'''
    @eval_fn
    def Y33():
        y1_1 = Update.Y1()
        var_1 = concat(y1_1, " ")
        i33_1 = Update.I33()
        var_2 = concat(i33_1, " ")
        var_3 = FIND(var_1, var_2)
        var_4 = ISERROR(var_3)
        var_5 = IF(var_4, "", "X")
        return var_5

@register(Update)
class Z33():
    # 'Update'!Z33
    value = '''Download "Unit Retirements" and sort by state.Be sure to allign columns correctly; Data not used directly in calculations, but good for reference'''

@register(Update)
class J34():
    # 'Update'!J34
    value = 14
    formula = '''=COUNTIF(J2:J33,"X")'''
    @eval_fn
    def J34():
        range_1 = Update(10, 2, 10, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class K34():
    # 'Update'!K34
    value = 12
    formula = '''=COUNTIF(K2:K33,"X")'''
    @eval_fn
    def K34():
        range_1 = Update(11, 2, 11, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class L34():
    # 'Update'!L34
    value = 13
    formula = '''=COUNTIF(L2:L33,"X")'''
    @eval_fn
    def L34():
        range_1 = Update(12, 2, 12, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class M34():
    # 'Update'!M34
    value = 13
    formula = '''=COUNTIF(M2:M33,"X")'''
    @eval_fn
    def M34():
        range_1 = Update(13, 2, 13, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class N34():
    # 'Update'!N34
    value = 20
    formula = '''=COUNTIF(N2:N33,"X")'''
    @eval_fn
    def N34():
        range_1 = Update(14, 2, 14, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class O34():
    # 'Update'!O34
    value = 3
    formula = '''=COUNTIF(O2:O33,"X")'''
    @eval_fn
    def O34():
        range_1 = Update(15, 2, 15, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class P34():
    # 'Update'!P34
    value = 0
    formula = '''=COUNTIF(P2:P33,"X")'''
    @eval_fn
    def P34():
        range_1 = Update(16, 2, 16, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class Q34():
    # 'Update'!Q34
    value = 12
    formula = '''=COUNTIF(Q2:Q33,"X")'''
    @eval_fn
    def Q34():
        range_1 = Update(17, 2, 17, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class R34():
    # 'Update'!R34
    value = 0
    formula = '''=COUNTIF(R2:R33,"X")'''
    @eval_fn
    def R34():
        range_1 = Update(18, 2, 18, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class S34():
    # 'Update'!S34
    value = 2
    formula = '''=COUNTIF(S2:S33,"X")'''
    @eval_fn
    def S34():
        range_1 = Update(19, 2, 19, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class T34():
    # 'Update'!T34
    value = 2
    formula = '''=COUNTIF(T2:T33,"X")'''
    @eval_fn
    def T34():
        range_1 = Update(20, 2, 20, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class U34():
    # 'Update'!U34
    value = 4
    formula = '''=COUNTIF(U2:U33,"X")'''
    @eval_fn
    def U34():
        range_1 = Update(21, 2, 21, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class V34():
    # 'Update'!V34
    value = 1
    formula = '''=COUNTIF(V2:V33,"X")'''
    @eval_fn
    def V34():
        range_1 = Update(22, 2, 22, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class W34():
    # 'Update'!W34
    value = 1
    formula = '''=COUNTIF(W2:W33,"X")'''
    @eval_fn
    def W34():
        range_1 = Update(23, 2, 23, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class X34():
    # 'Update'!X34
    value = 9
    formula = '''=COUNTIF(X2:X33,"X")'''
    @eval_fn
    def X34():
        range_1 = Update(24, 2, 24, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1

@register(Update)
class Y34():
    # 'Update'!Y34
    value = 2
    formula = '''=COUNTIF(Y2:Y33,"X")'''
    @eval_fn
    def Y34():
        range_1 = Update(25, 2, 25, 33)
        var_1 = COUNTIF(range_1, "X")
        return var_1