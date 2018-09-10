# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M1 = Worksheet('Charts_M1', 10, 10)



@register(Charts_M1)
class B1():
    # 'Charts_M1'!B1
    value = 1

@register(Charts_M1)
class B2():
    # 'Charts_M1'!B2
    value = 5

@register(Charts_M1)
class D2():
    # 'Charts_M1'!D2
    value = "Metric 1: Fossil energy content of Hawaii fuel use (BTU) per capita"

@register(Charts_M1)
class S2():
    # 'Charts_M1'!S2
    value = "Note: Fuel content is broken down by each sector's direct use. Conversions of fuel to electricity by the power sector is not carried through to each sector. "

@register(Charts_M1)
class B3():
    # 'Charts_M1'!B3
    value = 1

@register(Charts_M1)
class B4():
    # 'Charts_M1'!B4
    value = 53

@register(Charts_M1)
class D5():
    # 'Charts_M1'!D5
    value = "(Select comparison variable, sector, and fuel type from dropdowns on left)"

@register(Charts_M1)
class B8():
    # 'Charts_M1'!B8
    value = "Fossil Fuel Content of Hawaii (MMBtu/GSP)"
    formula = "='Charts Data M1'!$C$20"
    @eval_fn
    def B8():
        c20_1 = Charts_Data_M1.C20()
        return c20_1

@register(Charts_M1)
class O8():
    # 'Charts_M1'!O8
    value = "Life Cycle Petroleum Consumed in 2012"
    formula = "='Charts Data M1'!$C$23"
    @eval_fn
    def O8():
        c23_1 = Charts_Data_M1.C23()
        return c23_1

@register(Charts_M1)
class B21():
    # 'Charts_M1'!B21
    value = "Life Cycle Analysis Comparison (MMBtu/GSP)"
    formula = "='Charts Data M1'!$C$21"
    @eval_fn
    def B21():
        c21_1 = Charts_Data_M1.C21()
        return c21_1