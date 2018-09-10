# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Cover = Worksheet('Cover', 10, 10)



@register(Cover)
class C9():
    # 'Cover'!C9
    value = "Hawaii Clean Energy Status Model"

@register(Cover)
class C10():
    # 'Cover'!C10
    value = "Objective: Calculate Hawaii Energy Policy Forum's Clean Energy Status Metrics"