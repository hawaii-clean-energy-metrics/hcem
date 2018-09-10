# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M3 = Worksheet('Charts_M3', 10, 10)



@register(Charts_M3)
class B1():
    # 'Charts_M3'!B1
    value = 3

@register(Charts_M3)
class B2():
    # 'Charts_M3'!B2
    value = 7

@register(Charts_M3)
class D2():
    # 'Charts_M3'!D2
    value = "Metric 3: Carbon content of Hawaii fossil fuel use"

@register(Charts_M3)
class S2():
    # 'Charts_M3'!S2
    value = "Note: Fuel content is broken down by each sector's direct use. Conversions of fuel to electricity by the power sector is not carried through to each sector. "

@register(Charts_M3)
class B3():
    # 'Charts_M3'!B3
    value = 15

@register(Charts_M3)
class B4():
    # 'Charts_M3'!B4
    value = 54

@register(Charts_M3)
class D5():
    # 'Charts_M3'!D5
    value = "(Select comparison variable, sector, and fuel type from dropdowns on left)"

@register(Charts_M3)
class B8():
    # 'Charts_M3'!B8
    value = "CO2e Emissions of Hawaii (CO2)"
    formula = "='Charts Data M3'!$C$20"
    @eval_fn
    def B8():
        c20_1 = Charts_Data_M3.C20()
        return c20_1

@register(Charts_M3)
class O8():
    # 'Charts_M3'!O8
    value = "All Fuels Life Cycle Emissions in 2013"
    formula = "='Charts Data M3'!$C$19"
    @eval_fn
    def O8():
        c19_1 = Charts_Data_M3.C19()
        return c19_1

@register(Charts_M3)
class B22():
    # 'Charts_M3'!B22
    value = "Life Cycle Analysis Comparison (CO2)"
    formula = "='Charts Data M3'!$C$21"
    @eval_fn
    def B22():
        c21_1 = Charts_Data_M3.C21()
        return c21_1