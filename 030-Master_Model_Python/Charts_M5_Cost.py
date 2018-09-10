# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M5_Cost = Worksheet('Charts_M5_Cost', 10, 10)



@register(Charts_M5_Cost)
class B2():
    # 'Charts_M5_Cost'!B2
    value = 11

@register(Charts_M5_Cost)
class D2():
    # 'Charts_M5_Cost'!D2
    value = "Metric 5: Hawaii energy portfolio Cost (ECC) correlation to world crude petroleum price"

@register(Charts_M5_Cost)
class B3():
    # 'Charts_M5_Cost'!B3
    value = 7

@register(Charts_M5_Cost)
class B5():
    # 'Charts_M5_Cost'!B5
    value = "Month Lag:"

@register(Charts_M5_Cost)
class C5():
    # 'Charts_M5_Cost'!C5
    value = 2

@register(Charts_M5_Cost)
class C8():
    # 'Charts_M5_Cost'!C8
    value = 2006

@register(Charts_M5_Cost)
class D8():
    # 'Charts_M5_Cost'!D8
    value = 2007

@register(Charts_M5_Cost)
class E8():
    # 'Charts_M5_Cost'!E8
    value = 2008

@register(Charts_M5_Cost)
class F8():
    # 'Charts_M5_Cost'!F8
    value = 2009

@register(Charts_M5_Cost)
class G8():
    # 'Charts_M5_Cost'!G8
    value = 2010

@register(Charts_M5_Cost)
class H8():
    # 'Charts_M5_Cost'!H8
    value = 2011

@register(Charts_M5_Cost)
class I8():
    # 'Charts_M5_Cost'!I8
    value = 2012

@register(Charts_M5_Cost)
class J8():
    # 'Charts_M5_Cost'!J8
    value = 2013

@register(Charts_M5_Cost)
class P8():
    # 'Charts_M5_Cost'!P8
    value = "* A correlation of 1 means that Hawaiian EPC is 100% corelated to crude oil"

@register(Charts_M5_Cost)
class B9():
    # 'Charts_M5_Cost'!B9
    value = "Total ($ millions)"

@register(Charts_M5_Cost)
class C9():
    # 'Charts_M5_Cost'!C9
    value = 0.782330054034
    formula = "='Dashboard M5 Cost Monthly'!G46"
    @eval_fn
    def C9():
        g46_1 = Dashboard_M5_Cost_Monthly.G46()
        return g46_1

@register(Charts_M5_Cost)
class D9():
    # 'Charts_M5_Cost'!D9
    value = 0.9610593448
    formula = "='Dashboard M5 Cost Monthly'!H46"
    @eval_fn
    def D9():
        h46_1 = Dashboard_M5_Cost_Monthly.H46()
        return h46_1

@register(Charts_M5_Cost)
class E9():
    # 'Charts_M5_Cost'!E9
    value = 0.439745552392
    formula = "='Dashboard M5 Cost Monthly'!I46"
    @eval_fn
    def E9():
        i46_1 = Dashboard_M5_Cost_Monthly.I46()
        return i46_1

@register(Charts_M5_Cost)
class F9():
    # 'Charts_M5_Cost'!F9
    value = 0.71739446205
    formula = "='Dashboard M5 Cost Monthly'!J46"
    @eval_fn
    def F9():
        j46_1 = Dashboard_M5_Cost_Monthly.J46()
        return j46_1

@register(Charts_M5_Cost)
class G9():
    # 'Charts_M5_Cost'!G9
    value = 0.723278582757
    formula = "='Dashboard M5 Cost Monthly'!K46"
    @eval_fn
    def G9():
        k46_1 = Dashboard_M5_Cost_Monthly.K46()
        return k46_1

@register(Charts_M5_Cost)
class H9():
    # 'Charts_M5_Cost'!H9
    value = 0.490281940399
    formula = "='Dashboard M5 Cost Monthly'!L46"
    @eval_fn
    def H9():
        l46_1 = Dashboard_M5_Cost_Monthly.L46()
        return l46_1

@register(Charts_M5_Cost)
class I9():
    # 'Charts_M5_Cost'!I9
    value = 0.115770376019
    formula = "='Dashboard M5 Cost Monthly'!M46"
    @eval_fn
    def I9():
        m46_1 = Dashboard_M5_Cost_Monthly.M46()
        return m46_1

@register(Charts_M5_Cost)
class J9():
    # 'Charts_M5_Cost'!J9
    value = 0.155413991899
    formula = "='Dashboard M5 Cost Monthly'!N46"
    @eval_fn
    def J9():
        n46_1 = Dashboard_M5_Cost_Monthly.N46()
        return n46_1

@register(Charts_M5_Cost)
class P9():
    # 'Charts_M5_Cost'!P9
    value = "* A correlation of -1 means that Hawaiian EPC and crude oil have opposite correlations"

@register(Charts_M5_Cost)
class B11():
    # 'Charts_M5_Cost'!B11
    value = "Actual Energy Portfolio Cost of SNG compared to World Crude Price (Million $)"
    formula = "='Charts Data M5 Monthly'!$J$17"
    @eval_fn
    def B11():
        j17_1 = Charts_Data_M5_Monthly.J17()
        return j17_1

@register(Charts_M5_Cost)
class S13():
    # 'Charts_M5_Cost'!S13
    value = "THIS CHART DOES NOT ACCOUNT FOR MONTH LAG INPUT"

@register(Charts_M5_Cost)
class B34():
    # 'Charts_M5_Cost'!B34
    value = "Price Correlation of SNG to World Crude Price"
    formula = "='Charts Data M5 Monthly'!$I$17"
    @eval_fn
    def B34():
        i17_1 = Charts_Data_M5_Monthly.I17()
        return i17_1