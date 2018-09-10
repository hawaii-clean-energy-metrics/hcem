# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M6 = Worksheet('Charts_M6', 10, 10)



@register(Charts_M6)
class B2():
    # 'Charts_M6'!B2
    value = "Metric 6: Green Job Creation in Private Sector"

@register(Charts_M6)
class D5():
    # 'Charts_M6'!D5
    value = 2005

@register(Charts_M6)
class E5():
    # 'Charts_M6'!E5
    value = 2006

@register(Charts_M6)
class F5():
    # 'Charts_M6'!F5
    value = 2007

@register(Charts_M6)
class G5():
    # 'Charts_M6'!G5
    value = 2008

@register(Charts_M6)
class H5():
    # 'Charts_M6'!H5
    value = 2009

@register(Charts_M6)
class I5():
    # 'Charts_M6'!I5
    value = 2010

@register(Charts_M6)
class J5():
    # 'Charts_M6'!J5
    value = 2011

@register(Charts_M6)
class B6():
    # 'Charts_M6'!B6
    value = "Bureau Labor Statistics"
    formula = "='Charts Data M6'!C12"
    @eval_fn
    def B6():
        c12_1 = Charts_Data_M6.C12()
        return c12_1

@register(Charts_M6)
class D6():
    # 'Charts_M6'!D6
    value = "#N/A"
    formula = "='Charts Data M6'!AI12"
    @eval_fn
    def D6():
        ai12_1 = Charts_Data_M6.AI12()
        return ai12_1

@register(Charts_M6)
class E6():
    # 'Charts_M6'!E6
    value = "#N/A"
    formula = "='Charts Data M6'!AM12"
    @eval_fn
    def E6():
        am12_1 = Charts_Data_M6.AM12()
        return am12_1

@register(Charts_M6)
class F6():
    # 'Charts_M6'!F6
    value = "#N/A"
    formula = "='Charts Data M6'!AQ12"
    @eval_fn
    def F6():
        aq12_1 = Charts_Data_M6.AQ12()
        return aq12_1

@register(Charts_M6)
class G6():
    # 'Charts_M6'!G6
    value = "#N/A"
    formula = "='Charts Data M6'!AU12"
    @eval_fn
    def G6():
        au12_1 = Charts_Data_M6.AU12()
        return au12_1

@register(Charts_M6)
class H6():
    # 'Charts_M6'!H6
    value = "#N/A"
    formula = "='Charts Data M6'!AY12"
    @eval_fn
    def H6():
        ay12_1 = Charts_Data_M6.AY12()
        return ay12_1

@register(Charts_M6)
class I6():
    # 'Charts_M6'!I6
    value = 15583
    formula = "='Charts Data M6'!BC12"
    @eval_fn
    def I6():
        bc12_1 = Charts_Data_M6.BC12()
        return bc12_1

@register(Charts_M6)
class J6():
    # 'Charts_M6'!J6
    value = 16080
    formula = "='Charts Data M6'!BF12"
    @eval_fn
    def J6():
        bf12_1 = Charts_Data_M6.BF12()
        return bf12_1

@register(Charts_M6)
class B7():
    # 'Charts_M6'!B7
    value = "DLIR"
    formula = "='Charts Data M6'!C13"
    @eval_fn
    def B7():
        c13_1 = Charts_Data_M6.C13()
        return c13_1

@register(Charts_M6)
class D7():
    # 'Charts_M6'!D7
    value = "#N/A"
    formula = "='Charts Data M6'!AI13"
    @eval_fn
    def D7():
        ai13_1 = Charts_Data_M6.AI13()
        return ai13_1

@register(Charts_M6)
class E7():
    # 'Charts_M6'!E7
    value = "#N/A"
    formula = "='Charts Data M6'!AM13"
    @eval_fn
    def E7():
        am13_1 = Charts_Data_M6.AM13()
        return am13_1

@register(Charts_M6)
class F7():
    # 'Charts_M6'!F7
    value = "#N/A"
    formula = "='Charts Data M6'!AQ13"
    @eval_fn
    def F7():
        aq13_1 = Charts_Data_M6.AQ13()
        return aq13_1

@register(Charts_M6)
class G7():
    # 'Charts_M6'!G7
    value = "#N/A"
    formula = "='Charts Data M6'!AU13"
    @eval_fn
    def G7():
        au13_1 = Charts_Data_M6.AU13()
        return au13_1

@register(Charts_M6)
class H7():
    # 'Charts_M6'!H7
    value = "#N/A"
    formula = "='Charts Data M6'!AY13"
    @eval_fn
    def H7():
        ay13_1 = Charts_Data_M6.AY13()
        return ay13_1

@register(Charts_M6)
class I7():
    # 'Charts_M6'!I7
    value = 11148
    formula = "='Charts Data M6'!BC13"
    @eval_fn
    def I7():
        bc13_1 = Charts_Data_M6.BC13()
        return bc13_1

@register(Charts_M6)
class J7():
    # 'Charts_M6'!J7
    value = 11284
    formula = "='Charts Data M6'!BF13"
    @eval_fn
    def J7():
        bf13_1 = Charts_Data_M6.BF13()
        return bf13_1

@register(Charts_M6)
class B8():
    # 'Charts_M6'!B8
    value = "Brookings"
    formula = "='Charts Data M6'!C14"
    @eval_fn
    def B8():
        c14_1 = Charts_Data_M6.C14()
        return c14_1

@register(Charts_M6)
class D8():
    # 'Charts_M6'!D8
    value = 7869
    formula = "='Charts Data M6'!AI14"
    @eval_fn
    def D8():
        ai14_1 = Charts_Data_M6.AI14()
        return ai14_1

@register(Charts_M6)
class E8():
    # 'Charts_M6'!E8
    value = 8410
    formula = "='Charts Data M6'!AM14"
    @eval_fn
    def E8():
        am14_1 = Charts_Data_M6.AM14()
        return am14_1

@register(Charts_M6)
class F8():
    # 'Charts_M6'!F8
    value = 8885
    formula = "='Charts Data M6'!AQ14"
    @eval_fn
    def F8():
        aq14_1 = Charts_Data_M6.AQ14()
        return aq14_1

@register(Charts_M6)
class G8():
    # 'Charts_M6'!G8
    value = 9089
    formula = "='Charts Data M6'!AU14"
    @eval_fn
    def G8():
        au14_1 = Charts_Data_M6.AU14()
        return au14_1

@register(Charts_M6)
class H8():
    # 'Charts_M6'!H8
    value = 11087
    formula = "='Charts Data M6'!AY14"
    @eval_fn
    def H8():
        ay14_1 = Charts_Data_M6.AY14()
        return ay14_1

@register(Charts_M6)
class I8():
    # 'Charts_M6'!I8
    value = 11113
    formula = "='Charts Data M6'!BC14"
    @eval_fn
    def I8():
        bc14_1 = Charts_Data_M6.BC14()
        return bc14_1

@register(Charts_M6)
class J8():
    # 'Charts_M6'!J8
    value = "#N/A"
    formula = "='Charts Data M6'!BF14"
    @eval_fn
    def J8():
        bf14_1 = Charts_Data_M6.BF14()
        return bf14_1

@register(Charts_M6)
class B10():
    # 'Charts_M6'!B10
    value = "Hawaii -Percent of Green Jobs"

@register(Charts_M6)
class R12():
    # 'Charts_M6'!R12
    value = "Please Note:  Different methodologies were used to calculate green job creation. This chart shows them to vary significantly from one another. The Workforce Development Council Study is no longer being published. Moving forward, it is expected that the Bureau Labor Statistics will be the source used. Should additional studies be available, they will be considered as well."

@register(Charts_M6)
class B26():
    # 'Charts_M6'!B26
    value = "Hawaii - Total Green Jobs"