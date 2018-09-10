# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M5_Price = Worksheet('Charts_M5_Price', 10, 10)



@register(Charts_M5_Price)
class B2():
    # 'Charts_M5_Price'!B2
    value = 11

@register(Charts_M5_Price)
class D2():
    # 'Charts_M5_Price'!D2
    value = "Metric 5: Hawaii energy portfolio price (EPC) correlation to world crude petroleum price"

@register(Charts_M5_Price)
class B3():
    # 'Charts_M5_Price'!B3
    value = 3

@register(Charts_M5_Price)
class B5():
    # 'Charts_M5_Price'!B5
    value = "Month Lag:"

@register(Charts_M5_Price)
class C5():
    # 'Charts_M5_Price'!C5
    value = 2

@register(Charts_M5_Price)
class C8():
    # 'Charts_M5_Price'!C8
    value = 2006

@register(Charts_M5_Price)
class D8():
    # 'Charts_M5_Price'!D8
    value = 2007

@register(Charts_M5_Price)
class E8():
    # 'Charts_M5_Price'!E8
    value = 2008

@register(Charts_M5_Price)
class F8():
    # 'Charts_M5_Price'!F8
    value = 2009

@register(Charts_M5_Price)
class G8():
    # 'Charts_M5_Price'!G8
    value = 2010

@register(Charts_M5_Price)
class H8():
    # 'Charts_M5_Price'!H8
    value = 2011

@register(Charts_M5_Price)
class I8():
    # 'Charts_M5_Price'!I8
    value = 2012

@register(Charts_M5_Price)
class J8():
    # 'Charts_M5_Price'!J8
    value = 2013

@register(Charts_M5_Price)
class K8():
    # 'Charts_M5_Price'!K8
    value = 2014

@register(Charts_M5_Price)
class L8():
    # 'Charts_M5_Price'!L8
    value = 2015

@register(Charts_M5_Price)
class M8():
    # 'Charts_M5_Price'!M8
    value = 2016

@register(Charts_M5_Price)
class N8():
    # 'Charts_M5_Price'!N8
    value = 2017

@register(Charts_M5_Price)
class O8():
    # 'Charts_M5_Price'!O8
    value = 2018

@register(Charts_M5_Price)
class P8():
    # 'Charts_M5_Price'!P8
    value = "* A correlation of 1 means that Hawaiian EPC is 100% corelated to crude oil"

@register(Charts_M5_Price)
class B9():
    # 'Charts_M5_Price'!B9
    value = "Total ($ millions)"

@register(Charts_M5_Price)
class C9():
    # 'Charts_M5_Price'!C9
    value = 0.831101520934
    formula = "=IFERROR('Dashboard M5 Price Monthly'!G84,0)"
    @eval_fn
    def C9():
        g84_1 = Dashboard_M5_Price_Monthly.G84()
        var_1 = IFERROR(g84_1, 0)
        return var_1

@register(Charts_M5_Price)
class D9():
    # 'Charts_M5_Price'!D9
    value = 0.913164912871
    formula = "=IFERROR('Dashboard M5 Price Monthly'!H84,0)"
    @eval_fn
    def D9():
        h84_1 = Dashboard_M5_Price_Monthly.H84()
        var_1 = IFERROR(h84_1, 0)
        return var_1

@register(Charts_M5_Price)
class E9():
    # 'Charts_M5_Price'!E9
    value = 0.919584396848
    formula = "=IFERROR('Dashboard M5 Price Monthly'!I84,0)"
    @eval_fn
    def E9():
        i84_1 = Dashboard_M5_Price_Monthly.I84()
        var_1 = IFERROR(i84_1, 0)
        return var_1

@register(Charts_M5_Price)
class F9():
    # 'Charts_M5_Price'!F9
    value = 0.934761556021
    formula = "=IFERROR('Dashboard M5 Price Monthly'!J84,0)"
    @eval_fn
    def F9():
        j84_1 = Dashboard_M5_Price_Monthly.J84()
        var_1 = IFERROR(j84_1, 0)
        return var_1

@register(Charts_M5_Price)
class G9():
    # 'Charts_M5_Price'!G9
    value = 0.594354265397
    formula = "=IFERROR('Dashboard M5 Price Monthly'!K84,0)"
    @eval_fn
    def G9():
        k84_1 = Dashboard_M5_Price_Monthly.K84()
        var_1 = IFERROR(k84_1, 0)
        return var_1

@register(Charts_M5_Price)
class H9():
    # 'Charts_M5_Price'!H9
    value = 0.64452667304
    formula = "=IFERROR('Dashboard M5 Price Monthly'!L84,0)"
    @eval_fn
    def H9():
        l84_1 = Dashboard_M5_Price_Monthly.L84()
        var_1 = IFERROR(l84_1, 0)
        return var_1

@register(Charts_M5_Price)
class I9():
    # 'Charts_M5_Price'!I9
    value = 0.800754200857
    formula = "=IFERROR('Dashboard M5 Price Monthly'!M84,0)"
    @eval_fn
    def I9():
        m84_1 = Dashboard_M5_Price_Monthly.M84()
        var_1 = IFERROR(m84_1, 0)
        return var_1

@register(Charts_M5_Price)
class J9():
    # 'Charts_M5_Price'!J9
    value = 0.42157903668
    formula = "=IFERROR('Dashboard M5 Price Monthly'!N84,0)"
    @eval_fn
    def J9():
        n84_1 = Dashboard_M5_Price_Monthly.N84()
        var_1 = IFERROR(n84_1, 0)
        return var_1

@register(Charts_M5_Price)
class K9():
    # 'Charts_M5_Price'!K9
    value = 0
    formula = "=IFERROR('Dashboard M5 Price Monthly'!O84,0)"
    @eval_fn
    def K9():
        o84_1 = Dashboard_M5_Price_Monthly.O84()
        var_1 = IFERROR(o84_1, 0)
        return var_1

@register(Charts_M5_Price)
class L9():
    # 'Charts_M5_Price'!L9
    value = 0
    formula = "=IFERROR('Dashboard M5 Price Monthly'!P84,0)"
    @eval_fn
    def L9():
        p84_1 = Dashboard_M5_Price_Monthly.P84()
        var_1 = IFERROR(p84_1, 0)
        return var_1

@register(Charts_M5_Price)
class M9():
    # 'Charts_M5_Price'!M9
    value = 0
    formula = "=IFERROR('Dashboard M5 Price Monthly'!Q84,0)"
    @eval_fn
    def M9():
        q84_1 = Dashboard_M5_Price_Monthly.Q84()
        var_1 = IFERROR(q84_1, 0)
        return var_1

@register(Charts_M5_Price)
class N9():
    # 'Charts_M5_Price'!N9
    value = 0
    formula = "=IFERROR('Dashboard M5 Price Monthly'!R84,0)"
    @eval_fn
    def N9():
        r84_1 = Dashboard_M5_Price_Monthly.R84()
        var_1 = IFERROR(r84_1, 0)
        return var_1

@register(Charts_M5_Price)
class O9():
    # 'Charts_M5_Price'!O9
    value = 0
    formula = "=IFERROR('Dashboard M5 Price Monthly'!S84,0)"
    @eval_fn
    def O9():
        s84_1 = Dashboard_M5_Price_Monthly.S84()
        var_1 = IFERROR(s84_1, 0)
        return var_1

@register(Charts_M5_Price)
class P9():
    # 'Charts_M5_Price'!P9
    value = "* A correlation of -1 means that Hawaiian EPC and crude oil have opposite correlations"

@register(Charts_M5_Price)
class B11():
    # 'Charts_M5_Price'!B11
    value = "Actual Energy Portfolio Price of Jet Fuel compared to World Crude Price ($/Gallon)"
    formula = "='Charts Data M5 Monthly'!$J$7"
    @eval_fn
    def B11():
        j7_1 = Charts_Data_M5_Monthly.J7()
        return j7_1

@register(Charts_M5_Price)
class S13():
    # 'Charts_M5_Price'!S13
    value = "THIS CHART DOES NOT ACCOUNT FOR MONTH LAG INPUT"

@register(Charts_M5_Price)
class B37():
    # 'Charts_M5_Price'!B37
    value = "Price Correlation of Jet Fuel to World Crude Price"
    formula = "='Charts Data M5 Monthly'!$I$7"
    @eval_fn
    def B37():
        i7_1 = Charts_Data_M5_Monthly.I7()
        return i7_1