# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M8_Alt = Worksheet('Charts_M8_Alt', 10, 10)



@register(Charts_M8_Alt)
class B2():
    # 'Charts_M8_Alt'!B2
    value = "Metric 8: Maintaining affordability of energy costs"