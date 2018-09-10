# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M7 = Worksheet('Charts_M7', 10, 10)



@register(Charts_M7)
class D2():
    # 'Charts_M7'!D2
    value = "Metric 7: Hawaii energy portfolio price risk factor"

@register(Charts_M7)
class D7():
    # 'Charts_M7'!D7
    value = '''Metric 7, HEPF's request to assess the risks associated with Hawaii's energy portfolio, was drafted in largely undefined terms. In the metrics development document, the description recommends considering the "reliability of resource type and the geographic reliability of supply" and states that "The metric would b e a function of Hawai'i's evolving fuel mix and sources as well as determination of risk for each fuel type and source". This analysis suggests that the question of risk is most heavily based on the matter of price rather than simply supply. In other words, as supply lessons, the impacts on Hawaii will likely be how much the price of fuels and power go up rather than whether they will or will not have accessibility to fuel and/or power. Therefore, rather than attempt to create a broad-reaching methology on fuel and geographic risk factors, this analysis considers previously calculated metrics regarding pricing, metrics, 2, 4, 5, and 8. The write-up for this analysis will include further discussion'''