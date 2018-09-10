# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
OLD_Input_EIA_Jet_Fuel_Price = Worksheet('OLD_Input_EIA_Jet_Fuel_Price', 10, 10)



@register(OLD_Input_EIA_Jet_Fuel_Price)
class B1():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B1
    value = "Data 1: Hawaii Kerosene-Type Jet Fuel Wholesale/Resale Price by Refiners (Dollars per Gallon)"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C2():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C2
    value = "Orange indicates input data"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D2():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D2
    value = "Orange indicates input data"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E2():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E2
    value = "Yellow Indicates Intermediate Calculation"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F2():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F2
    value = "Orange indicates input data"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A3():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A3
    value = "Average HI-Specific Factor"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B3():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B3
    value = 1.17384676208
    formula = "=AVERAGE(E:E)"
    @eval_fn
    def B3():
        range_1 = OLD_Input_EIA_Jet_Fuel_Price(5, 0, 5, 0)
        var_1 = AVERAGE(range_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D3():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D3
    value = "http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EER_EPJK_PF4_RGC_DPG&f=M"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F3():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F3
    value = "http://tonto.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMA_EPJK_PWG_SHI_DPG&f=M"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A5():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A5
    value = "Sourcekey"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B5():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B5
    value = "EMA_EPJK_PWG_SHI_DPG"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A6():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A6
    value = "Date"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B6():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B6
    value = "Hawaii Kerosene-Type Jet Fuel Wholesale/Resale Price by Refiners (Dollars per Gallon)"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C6():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C6
    value = "Date"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D6():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D6
    value = "U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB (Dollars per Gallon)"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F6():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F6
    value = "Hawaii Kerosene-Type Jet Fuel Wholesale/Resale Price by Refiners (Dollars per Gallon)"

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A7():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A7
    value = 30926
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C7():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C7
    value = 30940
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A8():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A8
    value = 30956
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C8():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C8
    value = 30970
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A9():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A9
    value = 30987
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C9():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C9
    value = 31001
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A10():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A10
    value = 31017
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C10():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C10
    value = 31031
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A11():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A11
    value = 31048
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C11():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C11
    value = 31062
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A12():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A12
    value = 31079
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C12():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C12
    value = 31093
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A13():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A13
    value = 31107
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C13():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C13
    value = 31121
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A14():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A14
    value = 31138
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C14():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C14
    value = 31152
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A15():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A15
    value = 31168
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C15():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C15
    value = 31182
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A16():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A16
    value = 31199
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C16():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C16
    value = 31213
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A17():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A17
    value = 31229
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C17():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C17
    value = 31243
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A18():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A18
    value = 31260
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C18():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C18
    value = 31274
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A19():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A19
    value = 31291
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C19():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C19
    value = 31305
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A20():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A20
    value = 31321
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C20():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C20
    value = 31335
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A21():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A21
    value = 31352
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C21():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C21
    value = 31366
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A22():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A22
    value = 31382
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C22():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C22
    value = 31396
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A23():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A23
    value = 31413
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C23():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C23
    value = 31427
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A24():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A24
    value = 31444
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C24():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C24
    value = 31458
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A25():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A25
    value = 31472
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C25():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C25
    value = 31486
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A26():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A26
    value = 31503
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C26():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C26
    value = 31517
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A27():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A27
    value = 31533
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C27():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C27
    value = 31547
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A28():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A28
    value = 31564
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C28():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C28
    value = 31578
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A29():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A29
    value = 31594
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C29():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C29
    value = 31608
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A30():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A30
    value = 31625
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C30():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C30
    value = 31639
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A31():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A31
    value = 31656
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C31():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C31
    value = 31670
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A32():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A32
    value = 31686
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C32():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C32
    value = 31700
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A33():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A33
    value = 31717
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C33():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C33
    value = 31731
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A34():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A34
    value = 31747
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C34():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C34
    value = 31761
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A35():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A35
    value = 31778
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C35():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C35
    value = 31792
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A36():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A36
    value = 31809
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C36():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C36
    value = 31823
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A37():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A37
    value = 31837
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C37():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C37
    value = 31851
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A38():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A38
    value = 31868
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C38():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C38
    value = 31882
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A39():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A39
    value = 31898
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C39():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C39
    value = 31912
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A40():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A40
    value = 31929
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C40():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C40
    value = 31943
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A41():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A41
    value = 31959
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C41():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C41
    value = 31973
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A42():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A42
    value = 31990
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C42():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C42
    value = 32004
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A43():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A43
    value = 32021
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C43():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C43
    value = 32035
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A44():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A44
    value = 32051
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C44():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C44
    value = 32065
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A45():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A45
    value = 32082
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C45():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C45
    value = 32096
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A46():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A46
    value = 32112
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C46():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C46
    value = 32126
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A47():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A47
    value = 32143
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C47():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C47
    value = 32157
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A48():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A48
    value = 32174
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C48():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C48
    value = 32188
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A49():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A49
    value = 32203
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C49():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C49
    value = 32217
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A50():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A50
    value = 32234
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C50():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C50
    value = 32248
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A51():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A51
    value = 32264
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B51():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B51
    value = 0.701

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C51():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C51
    value = 32278
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F51():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F51
    value = 0.701

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A52():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A52
    value = 32295
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C52():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C52
    value = 32309
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A53():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A53
    value = 32325
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C53():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C53
    value = 32339
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A54():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A54
    value = 32356
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C54():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C54
    value = 32370
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A55():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A55
    value = 32387
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C55():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C55
    value = 32401
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A56():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A56
    value = 32417
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C56():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C56
    value = 32431
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A57():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A57
    value = 32448
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C57():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C57
    value = 32462
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A58():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A58
    value = 32478
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B58():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B58
    value = 0.649

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C58():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C58
    value = 32492
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F58():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F58
    value = 0.649

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A59():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A59
    value = 32509
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C59():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C59
    value = 32523
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A60():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A60
    value = 32540
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C60():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C60
    value = 32554
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A61():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A61
    value = 32568
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C61():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C61
    value = 32582
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A62():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A62
    value = 32599
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C62():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C62
    value = 32613
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A63():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A63
    value = 32629
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B63():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B63
    value = 0.785

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C63():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C63
    value = 32643
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F63():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F63
    value = 0.785

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A64():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A64
    value = 32660
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C64():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C64
    value = 32674
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A65():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A65
    value = 32690
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C65():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C65
    value = 32704
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A66():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A66
    value = 32721
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C66():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C66
    value = 32735
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A67():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A67
    value = 32752
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C67():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C67
    value = 32766
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A68():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A68
    value = 32782
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C68():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C68
    value = 32796
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A69():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A69
    value = 32813
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B69():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B69
    value = 0.841

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C69():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C69
    value = 32827
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F69():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F69
    value = 0.841

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A70():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A70
    value = 32843
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C70():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C70
    value = 32857
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A71():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A71
    value = 32874
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C71():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C71
    value = 32888
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D71():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D71
    value = 0.54

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A72():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A72
    value = 32905
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C72():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C72
    value = 32919
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D72():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D72
    value = 0.54

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A73():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A73
    value = 32933
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C73():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C73
    value = 32947
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D73():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D73
    value = 0.54

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A74():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A74
    value = 32964
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B74():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B74
    value = 0.633877251524
    formula = "=D74*$B$3"
    @eval_fn
    def B74():
        d74_1 = OLD_Input_EIA_Jet_Fuel_Price.D74()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d74_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C74():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C74
    value = 32978
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D74():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D74
    value = 0.54

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E74():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E74
    value = None
    formula = '''=IF(F74>0,F74/D74,"")'''
    @eval_fn
    def E74():
        f74_1 = OLD_Input_EIA_Jet_Fuel_Price.F74()
        var_1 = greaterthan(f74_1, 0)
        f74_2 = OLD_Input_EIA_Jet_Fuel_Price.F74()
        d74_1 = OLD_Input_EIA_Jet_Fuel_Price.D74()
        var_2 = divide(f74_2, d74_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A75():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A75
    value = 32994
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B75():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B75
    value = 0.604531082472
    formula = "=D75*$B$3"
    @eval_fn
    def B75():
        d75_1 = OLD_Input_EIA_Jet_Fuel_Price.D75()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d75_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C75():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C75
    value = 33008
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D75():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D75
    value = 0.515

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E75():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E75
    value = None
    formula = '''=IF(F75>0,F75/D75,"")'''
    @eval_fn
    def E75():
        f75_1 = OLD_Input_EIA_Jet_Fuel_Price.F75()
        var_1 = greaterthan(f75_1, 0)
        f75_2 = OLD_Input_EIA_Jet_Fuel_Price.F75()
        d75_1 = OLD_Input_EIA_Jet_Fuel_Price.D75()
        var_2 = divide(f75_2, d75_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A76():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A76
    value = 33025
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B76():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B76
    value = 0.579880300468
    formula = "=D76*$B$3"
    @eval_fn
    def B76():
        d76_1 = OLD_Input_EIA_Jet_Fuel_Price.D76()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d76_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C76():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C76
    value = 33039
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D76():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D76
    value = 0.494

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E76():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E76
    value = None
    formula = '''=IF(F76>0,F76/D76,"")'''
    @eval_fn
    def E76():
        f76_1 = OLD_Input_EIA_Jet_Fuel_Price.F76()
        var_1 = greaterthan(f76_1, 0)
        f76_2 = OLD_Input_EIA_Jet_Fuel_Price.F76()
        d76_1 = OLD_Input_EIA_Jet_Fuel_Price.D76()
        var_2 = divide(f76_2, d76_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A77():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A77
    value = 33055
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B77():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B77
    value = 0.628008017714
    formula = "=D77*$B$3"
    @eval_fn
    def B77():
        d77_1 = OLD_Input_EIA_Jet_Fuel_Price.D77()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d77_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C77():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C77
    value = 33069
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D77():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D77
    value = 0.535

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E77():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E77
    value = None
    formula = '''=IF(F77>0,F77/D77,"")'''
    @eval_fn
    def E77():
        f77_1 = OLD_Input_EIA_Jet_Fuel_Price.F77()
        var_1 = greaterthan(f77_1, 0)
        f77_2 = OLD_Input_EIA_Jet_Fuel_Price.F77()
        d77_1 = OLD_Input_EIA_Jet_Fuel_Price.D77()
        var_2 = divide(f77_2, d77_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A78():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A78
    value = 33086
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B78():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B78
    value = 0.928512788806
    formula = "=D78*$B$3"
    @eval_fn
    def B78():
        d78_1 = OLD_Input_EIA_Jet_Fuel_Price.D78()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d78_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C78():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C78
    value = 33100
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D78():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D78
    value = 0.791

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E78():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E78
    value = None
    formula = '''=IF(F78>0,F78/D78,"")'''
    @eval_fn
    def E78():
        f78_1 = OLD_Input_EIA_Jet_Fuel_Price.F78()
        var_1 = greaterthan(f78_1, 0)
        f78_2 = OLD_Input_EIA_Jet_Fuel_Price.F78()
        d78_1 = OLD_Input_EIA_Jet_Fuel_Price.D78()
        var_2 = divide(f78_2, d78_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A79():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A79
    value = 33117
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B79():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B79
    value = 1.18793292323
    formula = "=D79*$B$3"
    @eval_fn
    def B79():
        d79_1 = OLD_Input_EIA_Jet_Fuel_Price.D79()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d79_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C79():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C79
    value = 33131
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D79():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D79
    value = 1.012

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E79():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E79
    value = None
    formula = '''=IF(F79>0,F79/D79,"")'''
    @eval_fn
    def E79():
        f79_1 = OLD_Input_EIA_Jet_Fuel_Price.F79()
        var_1 = greaterthan(f79_1, 0)
        f79_2 = OLD_Input_EIA_Jet_Fuel_Price.F79()
        d79_1 = OLD_Input_EIA_Jet_Fuel_Price.D79()
        var_2 = divide(f79_2, d79_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A80():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A80
    value = 33147
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B80():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B80
    value = 1.40392072745
    formula = "=D80*$B$3"
    @eval_fn
    def B80():
        d80_1 = OLD_Input_EIA_Jet_Fuel_Price.D80()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d80_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C80():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C80
    value = 33161
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D80():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D80
    value = 1.196

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E80():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E80
    value = None
    formula = '''=IF(F80>0,F80/D80,"")'''
    @eval_fn
    def E80():
        f80_1 = OLD_Input_EIA_Jet_Fuel_Price.F80()
        var_1 = greaterthan(f80_1, 0)
        f80_2 = OLD_Input_EIA_Jet_Fuel_Price.F80()
        d80_1 = OLD_Input_EIA_Jet_Fuel_Price.D80()
        var_2 = divide(f80_2, d80_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A81():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A81
    value = 33178
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B81():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B81
    value = 1.13980520598
    formula = "=D81*$B$3"
    @eval_fn
    def B81():
        d81_1 = OLD_Input_EIA_Jet_Fuel_Price.D81()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d81_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C81():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C81
    value = 33192
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D81():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D81
    value = 0.971

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E81():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E81
    value = None
    formula = '''=IF(F81>0,F81/D81,"")'''
    @eval_fn
    def E81():
        f81_1 = OLD_Input_EIA_Jet_Fuel_Price.F81()
        var_1 = greaterthan(f81_1, 0)
        f81_2 = OLD_Input_EIA_Jet_Fuel_Price.F81()
        d81_1 = OLD_Input_EIA_Jet_Fuel_Price.D81()
        var_2 = divide(f81_2, d81_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A82():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A82
    value = 33208
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B82():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B82
    value = 0.942598949951
    formula = "=D82*$B$3"
    @eval_fn
    def B82():
        d82_1 = OLD_Input_EIA_Jet_Fuel_Price.D82()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d82_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C82():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C82
    value = 33222
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D82():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D82
    value = 0.803

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E82():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E82
    value = None
    formula = '''=IF(F82>0,F82/D82,"")'''
    @eval_fn
    def E82():
        f82_1 = OLD_Input_EIA_Jet_Fuel_Price.F82()
        var_1 = greaterthan(f82_1, 0)
        f82_2 = OLD_Input_EIA_Jet_Fuel_Price.F82()
        d82_1 = OLD_Input_EIA_Jet_Fuel_Price.D82()
        var_2 = divide(f82_2, d82_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A83():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A83
    value = 33239
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B83():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B83
    value = 0.869820450702
    formula = "=D83*$B$3"
    @eval_fn
    def B83():
        d83_1 = OLD_Input_EIA_Jet_Fuel_Price.D83()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d83_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C83():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C83
    value = 33253
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D83():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D83
    value = 0.741

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E83():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E83
    value = None
    formula = '''=IF(F83>0,F83/D83,"")'''
    @eval_fn
    def E83():
        f83_1 = OLD_Input_EIA_Jet_Fuel_Price.F83()
        var_1 = greaterthan(f83_1, 0)
        f83_2 = OLD_Input_EIA_Jet_Fuel_Price.F83()
        d83_1 = OLD_Input_EIA_Jet_Fuel_Price.D83()
        var_2 = divide(f83_2, d83_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A84():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A84
    value = 33270
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B84():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B84
    value = 0.747740387446
    formula = "=D84*$B$3"
    @eval_fn
    def B84():
        d84_1 = OLD_Input_EIA_Jet_Fuel_Price.D84()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d84_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C84():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C84
    value = 33284
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D84():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D84
    value = 0.637

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E84():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E84
    value = None
    formula = '''=IF(F84>0,F84/D84,"")'''
    @eval_fn
    def E84():
        f84_1 = OLD_Input_EIA_Jet_Fuel_Price.F84()
        var_1 = greaterthan(f84_1, 0)
        f84_2 = OLD_Input_EIA_Jet_Fuel_Price.F84()
        d84_1 = OLD_Input_EIA_Jet_Fuel_Price.D84()
        var_2 = divide(f84_2, d84_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A85():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A85
    value = 33298
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B85():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B85
    value = 0.655006493241
    formula = "=D85*$B$3"
    @eval_fn
    def B85():
        d85_1 = OLD_Input_EIA_Jet_Fuel_Price.D85()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d85_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C85():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C85
    value = 33312
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D85():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D85
    value = 0.558

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E85():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E85
    value = None
    formula = '''=IF(F85>0,F85/D85,"")'''
    @eval_fn
    def E85():
        f85_1 = OLD_Input_EIA_Jet_Fuel_Price.F85()
        var_1 = greaterthan(f85_1, 0)
        f85_2 = OLD_Input_EIA_Jet_Fuel_Price.F85()
        d85_1 = OLD_Input_EIA_Jet_Fuel_Price.D85()
        var_2 = divide(f85_2, d85_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A86():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A86
    value = 33329
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B86():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B86
    value = 0.647963412669
    formula = "=D86*$B$3"
    @eval_fn
    def B86():
        d86_1 = OLD_Input_EIA_Jet_Fuel_Price.D86()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d86_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C86():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C86
    value = 33343
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D86():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D86
    value = 0.552

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E86():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E86
    value = None
    formula = '''=IF(F86>0,F86/D86,"")'''
    @eval_fn
    def E86():
        f86_1 = OLD_Input_EIA_Jet_Fuel_Price.F86()
        var_1 = greaterthan(f86_1, 0)
        f86_2 = OLD_Input_EIA_Jet_Fuel_Price.F86()
        d86_1 = OLD_Input_EIA_Jet_Fuel_Price.D86()
        var_2 = divide(f86_2, d86_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A87():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A87
    value = 33359
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B87():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B87
    value = 0.667918807624
    formula = "=D87*$B$3"
    @eval_fn
    def B87():
        d87_1 = OLD_Input_EIA_Jet_Fuel_Price.D87()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d87_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C87():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C87
    value = 33373
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D87():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D87
    value = 0.569

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E87():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E87
    value = None
    formula = '''=IF(F87>0,F87/D87,"")'''
    @eval_fn
    def E87():
        f87_1 = OLD_Input_EIA_Jet_Fuel_Price.F87()
        var_1 = greaterthan(f87_1, 0)
        f87_2 = OLD_Input_EIA_Jet_Fuel_Price.F87()
        d87_1 = OLD_Input_EIA_Jet_Fuel_Price.D87()
        var_2 = divide(f87_2, d87_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A88():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A88
    value = 33390
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B88():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B88
    value = 0.642094178859
    formula = "=D88*$B$3"
    @eval_fn
    def B88():
        d88_1 = OLD_Input_EIA_Jet_Fuel_Price.D88()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d88_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C88():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C88
    value = 33404
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D88():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D88
    value = 0.547

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E88():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E88
    value = None
    formula = '''=IF(F88>0,F88/D88,"")'''
    @eval_fn
    def E88():
        f88_1 = OLD_Input_EIA_Jet_Fuel_Price.F88()
        var_1 = greaterthan(f88_1, 0)
        f88_2 = OLD_Input_EIA_Jet_Fuel_Price.F88()
        d88_1 = OLD_Input_EIA_Jet_Fuel_Price.D88()
        var_2 = divide(f88_2, d88_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A89():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A89
    value = 33420
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B89():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B89
    value = 0.68787420258
    formula = "=D89*$B$3"
    @eval_fn
    def B89():
        d89_1 = OLD_Input_EIA_Jet_Fuel_Price.D89()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d89_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C89():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C89
    value = 33434
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D89():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D89
    value = 0.586

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E89():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E89
    value = None
    formula = '''=IF(F89>0,F89/D89,"")'''
    @eval_fn
    def E89():
        f89_1 = OLD_Input_EIA_Jet_Fuel_Price.F89()
        var_1 = greaterthan(f89_1, 0)
        f89_2 = OLD_Input_EIA_Jet_Fuel_Price.F89()
        d89_1 = OLD_Input_EIA_Jet_Fuel_Price.D89()
        var_2 = divide(f89_2, d89_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A90():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A90
    value = 33451
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B90():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B90
    value = 0.731306532777
    formula = "=D90*$B$3"
    @eval_fn
    def B90():
        d90_1 = OLD_Input_EIA_Jet_Fuel_Price.D90()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d90_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C90():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C90
    value = 33465
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D90():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D90
    value = 0.623

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E90():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E90
    value = None
    formula = '''=IF(F90>0,F90/D90,"")'''
    @eval_fn
    def E90():
        f90_1 = OLD_Input_EIA_Jet_Fuel_Price.F90()
        var_1 = greaterthan(f90_1, 0)
        f90_2 = OLD_Input_EIA_Jet_Fuel_Price.F90()
        d90_1 = OLD_Input_EIA_Jet_Fuel_Price.D90()
        var_2 = divide(f90_2, d90_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A91
    value = 33482
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B91
    value = 0.745392693922
    formula = "=D91*$B$3"
    @eval_fn
    def B91():
        d91_1 = OLD_Input_EIA_Jet_Fuel_Price.D91()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d91_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C91
    value = 33496
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D91
    value = 0.635

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E91
    value = 1.21732283465
    formula = '''=IF(F91>0,F91/D91,"")'''
    @eval_fn
    def E91():
        f91_1 = OLD_Input_EIA_Jet_Fuel_Price.F91()
        var_1 = greaterthan(f91_1, 0)
        f91_2 = OLD_Input_EIA_Jet_Fuel_Price.F91()
        d91_1 = OLD_Input_EIA_Jet_Fuel_Price.D91()
        var_2 = divide(f91_2, d91_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F91():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F91
    value = 0.773

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A92
    value = 33512
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B92
    value = 0.787651177357
    formula = "=D92*$B$3"
    @eval_fn
    def B92():
        d92_1 = OLD_Input_EIA_Jet_Fuel_Price.D92()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d92_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C92
    value = 33526
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D92
    value = 0.671

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E92
    value = 1.14605067064
    formula = '''=IF(F92>0,F92/D92,"")'''
    @eval_fn
    def E92():
        f92_1 = OLD_Input_EIA_Jet_Fuel_Price.F92()
        var_1 = greaterthan(f92_1, 0)
        f92_2 = OLD_Input_EIA_Jet_Fuel_Price.F92()
        d92_1 = OLD_Input_EIA_Jet_Fuel_Price.D92()
        var_2 = divide(f92_2, d92_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F92():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F92
    value = 0.769

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A93
    value = 33543
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B93
    value = 0.757131161543
    formula = "=D93*$B$3"
    @eval_fn
    def B93():
        d93_1 = OLD_Input_EIA_Jet_Fuel_Price.D93()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d93_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C93
    value = 33557
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D93
    value = 0.645

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E93
    value = 1.28527131783
    formula = '''=IF(F93>0,F93/D93,"")'''
    @eval_fn
    def E93():
        f93_1 = OLD_Input_EIA_Jet_Fuel_Price.F93()
        var_1 = greaterthan(f93_1, 0)
        f93_2 = OLD_Input_EIA_Jet_Fuel_Price.F93()
        d93_1 = OLD_Input_EIA_Jet_Fuel_Price.D93()
        var_2 = divide(f93_2, d93_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F93():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F93
    value = 0.829

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A94():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A94
    value = 33573
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B94():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B94
    value = 0.612748009807
    formula = "=D94*$B$3"
    @eval_fn
    def B94():
        d94_1 = OLD_Input_EIA_Jet_Fuel_Price.D94()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d94_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C94():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C94
    value = 33587
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D94():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D94
    value = 0.522

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E94():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E94
    value = None
    formula = '''=IF(F94>0,F94/D94,"")'''
    @eval_fn
    def E94():
        f94_1 = OLD_Input_EIA_Jet_Fuel_Price.F94()
        var_1 = greaterthan(f94_1, 0)
        f94_2 = OLD_Input_EIA_Jet_Fuel_Price.F94()
        d94_1 = OLD_Input_EIA_Jet_Fuel_Price.D94()
        var_2 = divide(f94_2, d94_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A95():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A95
    value = 33604
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B95():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B95
    value = 0.597488001899
    formula = "=D95*$B$3"
    @eval_fn
    def B95():
        d95_1 = OLD_Input_EIA_Jet_Fuel_Price.D95()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d95_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C95():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C95
    value = 33618
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D95():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D95
    value = 0.509

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E95():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E95
    value = None
    formula = '''=IF(F95>0,F95/D95,"")'''
    @eval_fn
    def E95():
        f95_1 = OLD_Input_EIA_Jet_Fuel_Price.F95()
        var_1 = greaterthan(f95_1, 0)
        f95_2 = OLD_Input_EIA_Jet_Fuel_Price.F95()
        d95_1 = OLD_Input_EIA_Jet_Fuel_Price.D95()
        var_2 = divide(f95_2, d95_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A96():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A96
    value = 33635
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B96():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B96
    value = 0.63739879181
    formula = "=D96*$B$3"
    @eval_fn
    def B96():
        d96_1 = OLD_Input_EIA_Jet_Fuel_Price.D96()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d96_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C96():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C96
    value = 33649
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D96():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D96
    value = 0.543

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E96():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E96
    value = None
    formula = '''=IF(F96>0,F96/D96,"")'''
    @eval_fn
    def E96():
        f96_1 = OLD_Input_EIA_Jet_Fuel_Price.F96()
        var_1 = greaterthan(f96_1, 0)
        f96_2 = OLD_Input_EIA_Jet_Fuel_Price.F96()
        d96_1 = OLD_Input_EIA_Jet_Fuel_Price.D96()
        var_2 = divide(f96_2, d96_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A97():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A97
    value = 33664
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B97():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B97
    value = 0.60335723571
    formula = "=D97*$B$3"
    @eval_fn
    def B97():
        d97_1 = OLD_Input_EIA_Jet_Fuel_Price.D97()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d97_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C97():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C97
    value = 33678
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D97():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D97
    value = 0.514

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E97():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E97
    value = None
    formula = '''=IF(F97>0,F97/D97,"")'''
    @eval_fn
    def E97():
        f97_1 = OLD_Input_EIA_Jet_Fuel_Price.F97()
        var_1 = greaterthan(f97_1, 0)
        f97_2 = OLD_Input_EIA_Jet_Fuel_Price.F97()
        d97_1 = OLD_Input_EIA_Jet_Fuel_Price.D97()
        var_2 = divide(f97_2, d97_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A98():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A98
    value = 33695
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B98():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B98
    value = 0.63739879181
    formula = "=D98*$B$3"
    @eval_fn
    def B98():
        d98_1 = OLD_Input_EIA_Jet_Fuel_Price.D98()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d98_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C98():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C98
    value = 33709
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D98():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D98
    value = 0.543

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E98():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E98
    value = None
    formula = '''=IF(F98>0,F98/D98,"")'''
    @eval_fn
    def E98():
        f98_1 = OLD_Input_EIA_Jet_Fuel_Price.F98()
        var_1 = greaterthan(f98_1, 0)
        f98_2 = OLD_Input_EIA_Jet_Fuel_Price.F98()
        d98_1 = OLD_Input_EIA_Jet_Fuel_Price.D98()
        var_2 = divide(f98_2, d98_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A99():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A99
    value = 33725
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B99():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B99
    value = 0.679657275245
    formula = "=D99*$B$3"
    @eval_fn
    def B99():
        d99_1 = OLD_Input_EIA_Jet_Fuel_Price.D99()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d99_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C99():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C99
    value = 33739
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D99():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D99
    value = 0.579

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E99():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E99
    value = None
    formula = '''=IF(F99>0,F99/D99,"")'''
    @eval_fn
    def E99():
        f99_1 = OLD_Input_EIA_Jet_Fuel_Price.F99()
        var_1 = greaterthan(f99_1, 0)
        f99_2 = OLD_Input_EIA_Jet_Fuel_Price.F99()
        d99_1 = OLD_Input_EIA_Jet_Fuel_Price.D99()
        var_2 = divide(f99_2, d99_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A100():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A100
    value = 33756
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B100():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B100
    value = 0.72191575868
    formula = "=D100*$B$3"
    @eval_fn
    def B100():
        d100_1 = OLD_Input_EIA_Jet_Fuel_Price.D100()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d100_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C100():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C100
    value = 33770
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D100():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D100
    value = 0.615

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E100():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E100
    value = None
    formula = '''=IF(F100>0,F100/D100,"")'''
    @eval_fn
    def E100():
        f100_1 = OLD_Input_EIA_Jet_Fuel_Price.F100()
        var_1 = greaterthan(f100_1, 0)
        f100_2 = OLD_Input_EIA_Jet_Fuel_Price.F100()
        d100_1 = OLD_Input_EIA_Jet_Fuel_Price.D100()
        var_2 = divide(f100_2, d100_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A101():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A101
    value = 33786
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B101():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B101
    value = 0.717220371632
    formula = "=D101*$B$3"
    @eval_fn
    def B101():
        d101_1 = OLD_Input_EIA_Jet_Fuel_Price.D101()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d101_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C101():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C101
    value = 33800
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D101():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D101
    value = 0.611

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E101():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E101
    value = None
    formula = '''=IF(F101>0,F101/D101,"")'''
    @eval_fn
    def E101():
        f101_1 = OLD_Input_EIA_Jet_Fuel_Price.F101()
        var_1 = greaterthan(f101_1, 0)
        f101_2 = OLD_Input_EIA_Jet_Fuel_Price.F101()
        d101_1 = OLD_Input_EIA_Jet_Fuel_Price.D101()
        var_2 = divide(f101_2, d101_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A102
    value = 33817
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B102
    value = 0.692569589628
    formula = "=D102*$B$3"
    @eval_fn
    def B102():
        d102_1 = OLD_Input_EIA_Jet_Fuel_Price.D102()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d102_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C102
    value = 33831
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D102
    value = 0.59

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E102
    value = 1.48305084746
    formula = '''=IF(F102>0,F102/D102,"")'''
    @eval_fn
    def E102():
        f102_1 = OLD_Input_EIA_Jet_Fuel_Price.F102()
        var_1 = greaterthan(f102_1, 0)
        f102_2 = OLD_Input_EIA_Jet_Fuel_Price.F102()
        d102_1 = OLD_Input_EIA_Jet_Fuel_Price.D102()
        var_2 = divide(f102_2, d102_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F102():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F102
    value = 0.875

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A103
    value = 33848
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B103
    value = 0.731306532777
    formula = "=D103*$B$3"
    @eval_fn
    def B103():
        d103_1 = OLD_Input_EIA_Jet_Fuel_Price.D103()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d103_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C103
    value = 33862
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D103
    value = 0.623

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E103
    value = 1.46388443018
    formula = '''=IF(F103>0,F103/D103,"")'''
    @eval_fn
    def E103():
        f103_1 = OLD_Input_EIA_Jet_Fuel_Price.F103()
        var_1 = greaterthan(f103_1, 0)
        f103_2 = OLD_Input_EIA_Jet_Fuel_Price.F103()
        d103_1 = OLD_Input_EIA_Jet_Fuel_Price.D103()
        var_2 = divide(f103_2, d103_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F103():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F103
    value = 0.912

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A104():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A104
    value = 33878
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B104():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B104
    value = 0.728958839253
    formula = "=D104*$B$3"
    @eval_fn
    def B104():
        d104_1 = OLD_Input_EIA_Jet_Fuel_Price.D104()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d104_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C104():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C104
    value = 33892
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D104():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D104
    value = 0.621

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E104():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E104
    value = None
    formula = '''=IF(F104>0,F104/D104,"")'''
    @eval_fn
    def E104():
        f104_1 = OLD_Input_EIA_Jet_Fuel_Price.F104()
        var_1 = greaterthan(f104_1, 0)
        f104_2 = OLD_Input_EIA_Jet_Fuel_Price.F104()
        d104_1 = OLD_Input_EIA_Jet_Fuel_Price.D104()
        var_2 = divide(f104_2, d104_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A105():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A105
    value = 33909
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B105():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B105
    value = 0.658528033528
    formula = "=D105*$B$3"
    @eval_fn
    def B105():
        d105_1 = OLD_Input_EIA_Jet_Fuel_Price.D105()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d105_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C105():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C105
    value = 33923
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D105():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D105
    value = 0.561

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E105():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E105
    value = None
    formula = '''=IF(F105>0,F105/D105,"")'''
    @eval_fn
    def E105():
        f105_1 = OLD_Input_EIA_Jet_Fuel_Price.F105()
        var_1 = greaterthan(f105_1, 0)
        f105_2 = OLD_Input_EIA_Jet_Fuel_Price.F105()
        d105_1 = OLD_Input_EIA_Jet_Fuel_Price.D105()
        var_2 = divide(f105_2, d105_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A106():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A106
    value = 33939
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B106():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B106
    value = 0.638572638572
    formula = "=D106*$B$3"
    @eval_fn
    def B106():
        d106_1 = OLD_Input_EIA_Jet_Fuel_Price.D106()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d106_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C106():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C106
    value = 33953
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D106():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D106
    value = 0.544

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E106():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E106
    value = None
    formula = '''=IF(F106>0,F106/D106,"")'''
    @eval_fn
    def E106():
        f106_1 = OLD_Input_EIA_Jet_Fuel_Price.F106()
        var_1 = greaterthan(f106_1, 0)
        f106_2 = OLD_Input_EIA_Jet_Fuel_Price.F106()
        d106_1 = OLD_Input_EIA_Jet_Fuel_Price.D106()
        var_2 = divide(f106_2, d106_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A107():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A107
    value = 33970
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B107():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B107
    value = 0.626834170951
    formula = "=D107*$B$3"
    @eval_fn
    def B107():
        d107_1 = OLD_Input_EIA_Jet_Fuel_Price.D107()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d107_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C107():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C107
    value = 33984
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D107():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D107
    value = 0.534

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E107():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E107
    value = None
    formula = '''=IF(F107>0,F107/D107,"")'''
    @eval_fn
    def E107():
        f107_1 = OLD_Input_EIA_Jet_Fuel_Price.F107()
        var_1 = greaterthan(f107_1, 0)
        f107_2 = OLD_Input_EIA_Jet_Fuel_Price.F107()
        d107_1 = OLD_Input_EIA_Jet_Fuel_Price.D107()
        var_2 = divide(f107_2, d107_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A108():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A108
    value = 34001
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B108():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B108
    value = 0.649137259431
    formula = "=D108*$B$3"
    @eval_fn
    def B108():
        d108_1 = OLD_Input_EIA_Jet_Fuel_Price.D108()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d108_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C108():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C108
    value = 34015
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D108():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D108
    value = 0.553

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E108():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E108
    value = None
    formula = '''=IF(F108>0,F108/D108,"")'''
    @eval_fn
    def E108():
        f108_1 = OLD_Input_EIA_Jet_Fuel_Price.F108()
        var_1 = greaterthan(f108_1, 0)
        f108_2 = OLD_Input_EIA_Jet_Fuel_Price.F108()
        d108_1 = OLD_Input_EIA_Jet_Fuel_Price.D108()
        var_2 = divide(f108_2, d108_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A109
    value = 34029
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B109
    value = 0.655006493241
    formula = "=D109*$B$3"
    @eval_fn
    def B109():
        d109_1 = OLD_Input_EIA_Jet_Fuel_Price.D109()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d109_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C109
    value = 34043
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D109
    value = 0.558

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E109
    value = 1.66308243728
    formula = '''=IF(F109>0,F109/D109,"")'''
    @eval_fn
    def E109():
        f109_1 = OLD_Input_EIA_Jet_Fuel_Price.F109()
        var_1 = greaterthan(f109_1, 0)
        f109_2 = OLD_Input_EIA_Jet_Fuel_Price.F109()
        d109_1 = OLD_Input_EIA_Jet_Fuel_Price.D109()
        var_2 = divide(f109_2, d109_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F109():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F109
    value = 0.928

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A110():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A110
    value = 34060
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B110():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B110
    value = 0.646789565907
    formula = "=D110*$B$3"
    @eval_fn
    def B110():
        d110_1 = OLD_Input_EIA_Jet_Fuel_Price.D110()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d110_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C110():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C110
    value = 34074
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D110():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D110
    value = 0.551

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E110():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E110
    value = None
    formula = '''=IF(F110>0,F110/D110,"")'''
    @eval_fn
    def E110():
        f110_1 = OLD_Input_EIA_Jet_Fuel_Price.F110()
        var_1 = greaterthan(f110_1, 0)
        f110_2 = OLD_Input_EIA_Jet_Fuel_Price.F110()
        d110_1 = OLD_Input_EIA_Jet_Fuel_Price.D110()
        var_2 = divide(f110_2, d110_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A111
    value = 34090
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B111
    value = 0.649137259431
    formula = "=D111*$B$3"
    @eval_fn
    def B111():
        d111_1 = OLD_Input_EIA_Jet_Fuel_Price.D111()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d111_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C111
    value = 34104
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D111
    value = 0.553

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E111
    value = 1.61663652803
    formula = '''=IF(F111>0,F111/D111,"")'''
    @eval_fn
    def E111():
        f111_1 = OLD_Input_EIA_Jet_Fuel_Price.F111()
        var_1 = greaterthan(f111_1, 0)
        f111_2 = OLD_Input_EIA_Jet_Fuel_Price.F111()
        d111_1 = OLD_Input_EIA_Jet_Fuel_Price.D111()
        var_2 = divide(f111_2, d111_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F111():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F111
    value = 0.894

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A112():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A112
    value = 34121
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B112():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B112
    value = 0.617443396855
    formula = "=D112*$B$3"
    @eval_fn
    def B112():
        d112_1 = OLD_Input_EIA_Jet_Fuel_Price.D112()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d112_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C112():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C112
    value = 34135
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D112():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D112
    value = 0.526

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E112():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E112
    value = None
    formula = '''=IF(F112>0,F112/D112,"")'''
    @eval_fn
    def E112():
        f112_1 = OLD_Input_EIA_Jet_Fuel_Price.F112()
        var_1 = greaterthan(f112_1, 0)
        f112_2 = OLD_Input_EIA_Jet_Fuel_Price.F112()
        d112_1 = OLD_Input_EIA_Jet_Fuel_Price.D112()
        var_2 = divide(f112_2, d112_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A113():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A113
    value = 34151
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B113():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B113
    value = 0.579880300468
    formula = "=D113*$B$3"
    @eval_fn
    def B113():
        d113_1 = OLD_Input_EIA_Jet_Fuel_Price.D113()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d113_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C113():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C113
    value = 34165
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D113():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D113
    value = 0.494

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E113():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E113
    value = None
    formula = '''=IF(F113>0,F113/D113,"")'''
    @eval_fn
    def E113():
        f113_1 = OLD_Input_EIA_Jet_Fuel_Price.F113()
        var_1 = greaterthan(f113_1, 0)
        f113_2 = OLD_Input_EIA_Jet_Fuel_Price.F113()
        d113_1 = OLD_Input_EIA_Jet_Fuel_Price.D113()
        var_2 = divide(f113_2, d113_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A114():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A114
    value = 34182
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B114():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B114
    value = 0.588097227803
    formula = "=D114*$B$3"
    @eval_fn
    def B114():
        d114_1 = OLD_Input_EIA_Jet_Fuel_Price.D114()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d114_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C114():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C114
    value = 34196
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D114():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D114
    value = 0.501

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E114():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E114
    value = None
    formula = '''=IF(F114>0,F114/D114,"")'''
    @eval_fn
    def E114():
        f114_1 = OLD_Input_EIA_Jet_Fuel_Price.F114()
        var_1 = greaterthan(f114_1, 0)
        f114_2 = OLD_Input_EIA_Jet_Fuel_Price.F114()
        d114_1 = OLD_Input_EIA_Jet_Fuel_Price.D114()
        var_2 = divide(f114_2, d114_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A115
    value = 34213
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B115
    value = 0.628008017714
    formula = "=D115*$B$3"
    @eval_fn
    def B115():
        d115_1 = OLD_Input_EIA_Jet_Fuel_Price.D115()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d115_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C115
    value = 34227
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D115
    value = 0.535

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E115
    value = 1.45794392523
    formula = '''=IF(F115>0,F115/D115,"")'''
    @eval_fn
    def E115():
        f115_1 = OLD_Input_EIA_Jet_Fuel_Price.F115()
        var_1 = greaterthan(f115_1, 0)
        f115_2 = OLD_Input_EIA_Jet_Fuel_Price.F115()
        d115_1 = OLD_Input_EIA_Jet_Fuel_Price.D115()
        var_2 = divide(f115_2, d115_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F115():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F115
    value = 0.78

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A116():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A116
    value = 34243
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B116():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B116
    value = 0.666744960862
    formula = "=D116*$B$3"
    @eval_fn
    def B116():
        d116_1 = OLD_Input_EIA_Jet_Fuel_Price.D116()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d116_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C116():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C116
    value = 34257
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D116():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D116
    value = 0.568

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E116():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E116
    value = None
    formula = '''=IF(F116>0,F116/D116,"")'''
    @eval_fn
    def E116():
        f116_1 = OLD_Input_EIA_Jet_Fuel_Price.F116()
        var_1 = greaterthan(f116_1, 0)
        f116_2 = OLD_Input_EIA_Jet_Fuel_Price.F116()
        d116_1 = OLD_Input_EIA_Jet_Fuel_Price.D116()
        var_2 = divide(f116_2, d116_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A117():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A117
    value = 34274
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B117():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B117
    value = 0.625660324189
    formula = "=D117*$B$3"
    @eval_fn
    def B117():
        d117_1 = OLD_Input_EIA_Jet_Fuel_Price.D117()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d117_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C117():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C117
    value = 34288
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D117():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D117
    value = 0.533

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E117():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E117
    value = None
    formula = '''=IF(F117>0,F117/D117,"")'''
    @eval_fn
    def E117():
        f117_1 = OLD_Input_EIA_Jet_Fuel_Price.F117()
        var_1 = greaterthan(f117_1, 0)
        f117_2 = OLD_Input_EIA_Jet_Fuel_Price.F117()
        d117_1 = OLD_Input_EIA_Jet_Fuel_Price.D117()
        var_2 = divide(f117_2, d117_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A118():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A118
    value = 34304
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B118():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B118
    value = 0.523535655888
    formula = "=D118*$B$3"
    @eval_fn
    def B118():
        d118_1 = OLD_Input_EIA_Jet_Fuel_Price.D118()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d118_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C118():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C118
    value = 34318
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D118():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D118
    value = 0.446

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E118():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E118
    value = None
    formula = '''=IF(F118>0,F118/D118,"")'''
    @eval_fn
    def E118():
        f118_1 = OLD_Input_EIA_Jet_Fuel_Price.F118()
        var_1 = greaterthan(f118_1, 0)
        f118_2 = OLD_Input_EIA_Jet_Fuel_Price.F118()
        d118_1 = OLD_Input_EIA_Jet_Fuel_Price.D118()
        var_2 = divide(f118_2, d118_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A119():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A119
    value = 34335
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B119():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B119
    value = 0.619791090379
    formula = "=D119*$B$3"
    @eval_fn
    def B119():
        d119_1 = OLD_Input_EIA_Jet_Fuel_Price.D119()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d119_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C119():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C119
    value = 34349
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D119():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D119
    value = 0.528

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E119():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E119
    value = None
    formula = '''=IF(F119>0,F119/D119,"")'''
    @eval_fn
    def E119():
        f119_1 = OLD_Input_EIA_Jet_Fuel_Price.F119()
        var_1 = greaterthan(f119_1, 0)
        f119_2 = OLD_Input_EIA_Jet_Fuel_Price.F119()
        d119_1 = OLD_Input_EIA_Jet_Fuel_Price.D119()
        var_2 = divide(f119_2, d119_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A120():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A120
    value = 34366
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B120():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B120
    value = 0.588097227803
    formula = "=D120*$B$3"
    @eval_fn
    def B120():
        d120_1 = OLD_Input_EIA_Jet_Fuel_Price.D120()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d120_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C120():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C120
    value = 34380
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D120():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D120
    value = 0.501

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E120():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E120
    value = None
    formula = '''=IF(F120>0,F120/D120,"")'''
    @eval_fn
    def E120():
        f120_1 = OLD_Input_EIA_Jet_Fuel_Price.F120()
        var_1 = greaterthan(f120_1, 0)
        f120_2 = OLD_Input_EIA_Jet_Fuel_Price.F120()
        d120_1 = OLD_Input_EIA_Jet_Fuel_Price.D120()
        var_2 = divide(f120_2, d120_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A121():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A121
    value = 34394
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B121():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B121
    value = 0.529404889699
    formula = "=D121*$B$3"
    @eval_fn
    def B121():
        d121_1 = OLD_Input_EIA_Jet_Fuel_Price.D121()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d121_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C121():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C121
    value = 34408
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D121():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D121
    value = 0.451

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E121():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E121
    value = None
    formula = '''=IF(F121>0,F121/D121,"")'''
    @eval_fn
    def E121():
        f121_1 = OLD_Input_EIA_Jet_Fuel_Price.F121()
        var_1 = greaterthan(f121_1, 0)
        f121_2 = OLD_Input_EIA_Jet_Fuel_Price.F121()
        d121_1 = OLD_Input_EIA_Jet_Fuel_Price.D121()
        var_2 = divide(f121_2, d121_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A122():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A122
    value = 34425
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B122():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B122
    value = 0.550534131416
    formula = "=D122*$B$3"
    @eval_fn
    def B122():
        d122_1 = OLD_Input_EIA_Jet_Fuel_Price.D122()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d122_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C122():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C122
    value = 34439
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D122():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D122
    value = 0.469

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E122():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E122
    value = None
    formula = '''=IF(F122>0,F122/D122,"")'''
    @eval_fn
    def E122():
        f122_1 = OLD_Input_EIA_Jet_Fuel_Price.F122()
        var_1 = greaterthan(f122_1, 0)
        f122_2 = OLD_Input_EIA_Jet_Fuel_Price.F122()
        d122_1 = OLD_Input_EIA_Jet_Fuel_Price.D122()
        var_2 = divide(f122_2, d122_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A123():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A123
    value = 34455
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B123():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B123
    value = 0.554055671702
    formula = "=D123*$B$3"
    @eval_fn
    def B123():
        d123_1 = OLD_Input_EIA_Jet_Fuel_Price.D123()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d123_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C123():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C123
    value = 34469
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D123():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D123
    value = 0.472

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E123():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E123
    value = None
    formula = '''=IF(F123>0,F123/D123,"")'''
    @eval_fn
    def E123():
        f123_1 = OLD_Input_EIA_Jet_Fuel_Price.F123()
        var_1 = greaterthan(f123_1, 0)
        f123_2 = OLD_Input_EIA_Jet_Fuel_Price.F123()
        d123_1 = OLD_Input_EIA_Jet_Fuel_Price.D123()
        var_2 = divide(f123_2, d123_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A124():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A124
    value = 34486
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B124():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B124
    value = 0.578706453706
    formula = "=D124*$B$3"
    @eval_fn
    def B124():
        d124_1 = OLD_Input_EIA_Jet_Fuel_Price.D124()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d124_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C124():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C124
    value = 34500
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D124():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D124
    value = 0.493

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E124():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E124
    value = None
    formula = '''=IF(F124>0,F124/D124,"")'''
    @eval_fn
    def E124():
        f124_1 = OLD_Input_EIA_Jet_Fuel_Price.F124()
        var_1 = greaterthan(f124_1, 0)
        f124_2 = OLD_Input_EIA_Jet_Fuel_Price.F124()
        d124_1 = OLD_Input_EIA_Jet_Fuel_Price.D124()
        var_2 = divide(f124_2, d124_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A125():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A125
    value = 34516
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B125():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B125
    value = 0.597488001899
    formula = "=D125*$B$3"
    @eval_fn
    def B125():
        d125_1 = OLD_Input_EIA_Jet_Fuel_Price.D125()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d125_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C125():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C125
    value = 34530
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D125():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D125
    value = 0.509

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E125():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E125
    value = None
    formula = '''=IF(F125>0,F125/D125,"")'''
    @eval_fn
    def E125():
        f125_1 = OLD_Input_EIA_Jet_Fuel_Price.F125()
        var_1 = greaterthan(f125_1, 0)
        f125_2 = OLD_Input_EIA_Jet_Fuel_Price.F125()
        d125_1 = OLD_Input_EIA_Jet_Fuel_Price.D125()
        var_2 = divide(f125_2, d125_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A126():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A126
    value = 34547
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B126():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B126
    value = 0.584575687517
    formula = "=D126*$B$3"
    @eval_fn
    def B126():
        d126_1 = OLD_Input_EIA_Jet_Fuel_Price.D126()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d126_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C126():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C126
    value = 34561
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D126():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D126
    value = 0.498

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E126():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E126
    value = None
    formula = '''=IF(F126>0,F126/D126,"")'''
    @eval_fn
    def E126():
        f126_1 = OLD_Input_EIA_Jet_Fuel_Price.F126()
        var_1 = greaterthan(f126_1, 0)
        f126_2 = OLD_Input_EIA_Jet_Fuel_Price.F126()
        d126_1 = OLD_Input_EIA_Jet_Fuel_Price.D126()
        var_2 = divide(f126_2, d126_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A127():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A127
    value = 34578
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B127():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B127
    value = 0.57518491342
    formula = "=D127*$B$3"
    @eval_fn
    def B127():
        d127_1 = OLD_Input_EIA_Jet_Fuel_Price.D127()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d127_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C127():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C127
    value = 34592
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D127():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D127
    value = 0.49

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E127():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E127
    value = None
    formula = '''=IF(F127>0,F127/D127,"")'''
    @eval_fn
    def E127():
        f127_1 = OLD_Input_EIA_Jet_Fuel_Price.F127()
        var_1 = greaterthan(f127_1, 0)
        f127_2 = OLD_Input_EIA_Jet_Fuel_Price.F127()
        d127_1 = OLD_Input_EIA_Jet_Fuel_Price.D127()
        var_2 = divide(f127_2, d127_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A128():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A128
    value = 34608
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B128():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B128
    value = 0.597488001899
    formula = "=D128*$B$3"
    @eval_fn
    def B128():
        d128_1 = OLD_Input_EIA_Jet_Fuel_Price.D128()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d128_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C128():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C128
    value = 34622
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D128():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D128
    value = 0.509

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E128():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E128
    value = None
    formula = '''=IF(F128>0,F128/D128,"")'''
    @eval_fn
    def E128():
        f128_1 = OLD_Input_EIA_Jet_Fuel_Price.F128()
        var_1 = greaterthan(f128_1, 0)
        f128_2 = OLD_Input_EIA_Jet_Fuel_Price.F128()
        d128_1 = OLD_Input_EIA_Jet_Fuel_Price.D128()
        var_2 = divide(f128_2, d128_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A129():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A129
    value = 34639
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B129():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B129
    value = 0.602183388948
    formula = "=D129*$B$3"
    @eval_fn
    def B129():
        d129_1 = OLD_Input_EIA_Jet_Fuel_Price.D129()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d129_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C129():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C129
    value = 34653
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D129():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D129
    value = 0.513

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E129():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E129
    value = None
    formula = '''=IF(F129>0,F129/D129,"")'''
    @eval_fn
    def E129():
        f129_1 = OLD_Input_EIA_Jet_Fuel_Price.F129()
        var_1 = greaterthan(f129_1, 0)
        f129_2 = OLD_Input_EIA_Jet_Fuel_Price.F129()
        d129_1 = OLD_Input_EIA_Jet_Fuel_Price.D129()
        var_2 = divide(f129_2, d129_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A130():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A130
    value = 34669
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B130():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B130
    value = 0.571663373134
    formula = "=D130*$B$3"
    @eval_fn
    def B130():
        d130_1 = OLD_Input_EIA_Jet_Fuel_Price.D130()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d130_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C130():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C130
    value = 34683
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D130():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D130
    value = 0.487

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E130():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E130
    value = None
    formula = '''=IF(F130>0,F130/D130,"")'''
    @eval_fn
    def E130():
        f130_1 = OLD_Input_EIA_Jet_Fuel_Price.F130()
        var_1 = greaterthan(f130_1, 0)
        f130_2 = OLD_Input_EIA_Jet_Fuel_Price.F130()
        d130_1 = OLD_Input_EIA_Jet_Fuel_Price.D130()
        var_2 = divide(f130_2, d130_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A131():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A131
    value = 34700
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B131():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B131
    value = 0.554055671702
    formula = "=D131*$B$3"
    @eval_fn
    def B131():
        d131_1 = OLD_Input_EIA_Jet_Fuel_Price.D131()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d131_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C131():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C131
    value = 34714
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D131():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D131
    value = 0.472

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E131():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E131
    value = None
    formula = '''=IF(F131>0,F131/D131,"")'''
    @eval_fn
    def E131():
        f131_1 = OLD_Input_EIA_Jet_Fuel_Price.F131()
        var_1 = greaterthan(f131_1, 0)
        f131_2 = OLD_Input_EIA_Jet_Fuel_Price.F131()
        d131_1 = OLD_Input_EIA_Jet_Fuel_Price.D131()
        var_2 = divide(f131_2, d131_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A132():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A132
    value = 34731
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B132():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B132
    value = 0.548186437892
    formula = "=D132*$B$3"
    @eval_fn
    def B132():
        d132_1 = OLD_Input_EIA_Jet_Fuel_Price.D132()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d132_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C132():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C132
    value = 34745
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D132():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D132
    value = 0.467

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E132():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E132
    value = None
    formula = '''=IF(F132>0,F132/D132,"")'''
    @eval_fn
    def E132():
        f132_1 = OLD_Input_EIA_Jet_Fuel_Price.F132()
        var_1 = greaterthan(f132_1, 0)
        f132_2 = OLD_Input_EIA_Jet_Fuel_Price.F132()
        d132_1 = OLD_Input_EIA_Jet_Fuel_Price.D132()
        var_2 = divide(f132_2, d132_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A133():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A133
    value = 34759
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B133():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B133
    value = 0.527057196175
    formula = "=D133*$B$3"
    @eval_fn
    def B133():
        d133_1 = OLD_Input_EIA_Jet_Fuel_Price.D133()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d133_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C133():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C133
    value = 34773
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D133():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D133
    value = 0.449

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E133():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E133
    value = None
    formula = '''=IF(F133>0,F133/D133,"")'''
    @eval_fn
    def E133():
        f133_1 = OLD_Input_EIA_Jet_Fuel_Price.F133()
        var_1 = greaterthan(f133_1, 0)
        f133_2 = OLD_Input_EIA_Jet_Fuel_Price.F133()
        d133_1 = OLD_Input_EIA_Jet_Fuel_Price.D133()
        var_2 = divide(f133_2, d133_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A134
    value = 34790
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B134
    value = 0.586923381041
    formula = "=D134*$B$3"
    @eval_fn
    def B134():
        d134_1 = OLD_Input_EIA_Jet_Fuel_Price.D134()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d134_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C134
    value = 34804
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D134
    value = 0.5

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E134
    value = 1.108
    formula = '''=IF(F134>0,F134/D134,"")'''
    @eval_fn
    def E134():
        f134_1 = OLD_Input_EIA_Jet_Fuel_Price.F134()
        var_1 = greaterthan(f134_1, 0)
        f134_2 = OLD_Input_EIA_Jet_Fuel_Price.F134()
        d134_1 = OLD_Input_EIA_Jet_Fuel_Price.D134()
        var_2 = divide(f134_2, d134_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F134():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F134
    value = 0.554

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A135():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A135
    value = 34820
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B135():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B135
    value = 0.599835695424
    formula = "=D135*$B$3"
    @eval_fn
    def B135():
        d135_1 = OLD_Input_EIA_Jet_Fuel_Price.D135()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d135_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C135():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C135
    value = 34834
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D135():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D135
    value = 0.511

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E135():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E135
    value = None
    formula = '''=IF(F135>0,F135/D135,"")'''
    @eval_fn
    def E135():
        f135_1 = OLD_Input_EIA_Jet_Fuel_Price.F135()
        var_1 = greaterthan(f135_1, 0)
        f135_2 = OLD_Input_EIA_Jet_Fuel_Price.F135()
        d135_1 = OLD_Input_EIA_Jet_Fuel_Price.D135()
        var_2 = divide(f135_2, d135_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A136():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A136
    value = 34851
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B136():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B136
    value = 0.561098752275
    formula = "=D136*$B$3"
    @eval_fn
    def B136():
        d136_1 = OLD_Input_EIA_Jet_Fuel_Price.D136()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d136_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C136():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C136
    value = 34865
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D136():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D136
    value = 0.478

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E136():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E136
    value = None
    formula = '''=IF(F136>0,F136/D136,"")'''
    @eval_fn
    def E136():
        f136_1 = OLD_Input_EIA_Jet_Fuel_Price.F136()
        var_1 = greaterthan(f136_1, 0)
        f136_2 = OLD_Input_EIA_Jet_Fuel_Price.F136()
        d136_1 = OLD_Input_EIA_Jet_Fuel_Price.D136()
        var_2 = divide(f136_2, d136_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A137():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A137
    value = 34881
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B137():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B137
    value = 0.548186437892
    formula = "=D137*$B$3"
    @eval_fn
    def B137():
        d137_1 = OLD_Input_EIA_Jet_Fuel_Price.D137()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d137_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C137():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C137
    value = 34895
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D137():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D137
    value = 0.467

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E137():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E137
    value = None
    formula = '''=IF(F137>0,F137/D137,"")'''
    @eval_fn
    def E137():
        f137_1 = OLD_Input_EIA_Jet_Fuel_Price.F137()
        var_1 = greaterthan(f137_1, 0)
        f137_2 = OLD_Input_EIA_Jet_Fuel_Price.F137()
        d137_1 = OLD_Input_EIA_Jet_Fuel_Price.D137()
        var_2 = divide(f137_2, d137_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A138
    value = 34912
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B138
    value = 0.582227993992
    formula = "=D138*$B$3"
    @eval_fn
    def B138():
        d138_1 = OLD_Input_EIA_Jet_Fuel_Price.D138()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d138_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C138
    value = 34926
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D138
    value = 0.496

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E138
    value = 1.14919354839
    formula = '''=IF(F138>0,F138/D138,"")'''
    @eval_fn
    def E138():
        f138_1 = OLD_Input_EIA_Jet_Fuel_Price.F138()
        var_1 = greaterthan(f138_1, 0)
        f138_2 = OLD_Input_EIA_Jet_Fuel_Price.F138()
        d138_1 = OLD_Input_EIA_Jet_Fuel_Price.D138()
        var_2 = divide(f138_2, d138_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F138():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F138
    value = 0.57

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A139
    value = 34943
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B139
    value = 0.602183388948
    formula = "=D139*$B$3"
    @eval_fn
    def B139():
        d139_1 = OLD_Input_EIA_Jet_Fuel_Price.D139()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d139_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C139
    value = 34957
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D139
    value = 0.513

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E139
    value = 1.14619883041
    formula = '''=IF(F139>0,F139/D139,"")'''
    @eval_fn
    def E139():
        f139_1 = OLD_Input_EIA_Jet_Fuel_Price.F139()
        var_1 = greaterthan(f139_1, 0)
        f139_2 = OLD_Input_EIA_Jet_Fuel_Price.F139()
        d139_1 = OLD_Input_EIA_Jet_Fuel_Price.D139()
        var_2 = divide(f139_2, d139_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F139():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F139
    value = 0.588

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A140():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A140
    value = 34973
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B140():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B140
    value = 0.589271074565
    formula = "=D140*$B$3"
    @eval_fn
    def B140():
        d140_1 = OLD_Input_EIA_Jet_Fuel_Price.D140()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d140_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C140():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C140
    value = 34987
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D140():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D140
    value = 0.502

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E140():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E140
    value = None
    formula = '''=IF(F140>0,F140/D140,"")'''
    @eval_fn
    def E140():
        f140_1 = OLD_Input_EIA_Jet_Fuel_Price.F140()
        var_1 = greaterthan(f140_1, 0)
        f140_2 = OLD_Input_EIA_Jet_Fuel_Price.F140()
        d140_1 = OLD_Input_EIA_Jet_Fuel_Price.D140()
        var_2 = divide(f140_2, d140_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A141():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A141
    value = 35004
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B141():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B141
    value = 0.615095703331
    formula = "=D141*$B$3"
    @eval_fn
    def B141():
        d141_1 = OLD_Input_EIA_Jet_Fuel_Price.D141()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d141_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C141():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C141
    value = 35018
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D141():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D141
    value = 0.524

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E141():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E141
    value = None
    formula = '''=IF(F141>0,F141/D141,"")'''
    @eval_fn
    def E141():
        f141_1 = OLD_Input_EIA_Jet_Fuel_Price.F141()
        var_1 = greaterthan(f141_1, 0)
        f141_2 = OLD_Input_EIA_Jet_Fuel_Price.F141()
        d141_1 = OLD_Input_EIA_Jet_Fuel_Price.D141()
        var_2 = divide(f141_2, d141_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A142():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A142
    value = 35034
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B142():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B142
    value = 0.649137259431
    formula = "=D142*$B$3"
    @eval_fn
    def B142():
        d142_1 = OLD_Input_EIA_Jet_Fuel_Price.D142()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d142_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C142():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C142
    value = 35048
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D142():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D142
    value = 0.553

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E142():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E142
    value = None
    formula = '''=IF(F142>0,F142/D142,"")'''
    @eval_fn
    def E142():
        f142_1 = OLD_Input_EIA_Jet_Fuel_Price.F142()
        var_1 = greaterthan(f142_1, 0)
        f142_2 = OLD_Input_EIA_Jet_Fuel_Price.F142()
        d142_1 = OLD_Input_EIA_Jet_Fuel_Price.D142()
        var_2 = divide(f142_2, d142_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A143():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A143
    value = 35065
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B143():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B143
    value = 0.645615719145
    formula = "=D143*$B$3"
    @eval_fn
    def B143():
        d143_1 = OLD_Input_EIA_Jet_Fuel_Price.D143()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d143_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C143():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C143
    value = 35079
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D143():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D143
    value = 0.55

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E143():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E143
    value = None
    formula = '''=IF(F143>0,F143/D143,"")'''
    @eval_fn
    def E143():
        f143_1 = OLD_Input_EIA_Jet_Fuel_Price.F143()
        var_1 = greaterthan(f143_1, 0)
        f143_2 = OLD_Input_EIA_Jet_Fuel_Price.F143()
        d143_1 = OLD_Input_EIA_Jet_Fuel_Price.D143()
        var_2 = divide(f143_2, d143_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A144():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A144
    value = 35096
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B144():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B144
    value = 0.653832646479
    formula = "=D144*$B$3"
    @eval_fn
    def B144():
        d144_1 = OLD_Input_EIA_Jet_Fuel_Price.D144()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d144_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C144():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C144
    value = 35110
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D144():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D144
    value = 0.557

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E144():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E144
    value = None
    formula = '''=IF(F144>0,F144/D144,"")'''
    @eval_fn
    def E144():
        f144_1 = OLD_Input_EIA_Jet_Fuel_Price.F144()
        var_1 = greaterthan(f144_1, 0)
        f144_2 = OLD_Input_EIA_Jet_Fuel_Price.F144()
        d144_1 = OLD_Input_EIA_Jet_Fuel_Price.D144()
        var_2 = divide(f144_2, d144_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A145():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A145
    value = 35125
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B145():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B145
    value = 0.68787420258
    formula = "=D145*$B$3"
    @eval_fn
    def B145():
        d145_1 = OLD_Input_EIA_Jet_Fuel_Price.D145()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d145_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C145():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C145
    value = 35139
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D145():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D145
    value = 0.586

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E145():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E145
    value = None
    formula = '''=IF(F145>0,F145/D145,"")'''
    @eval_fn
    def E145():
        f145_1 = OLD_Input_EIA_Jet_Fuel_Price.F145()
        var_1 = greaterthan(f145_1, 0)
        f145_2 = OLD_Input_EIA_Jet_Fuel_Price.F145()
        d145_1 = OLD_Input_EIA_Jet_Fuel_Price.D145()
        var_2 = divide(f145_2, d145_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A146():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A146
    value = 35156
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B146():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B146
    value = 0.724263452204
    formula = "=D146*$B$3"
    @eval_fn
    def B146():
        d146_1 = OLD_Input_EIA_Jet_Fuel_Price.D146()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d146_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C146():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C146
    value = 35170
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D146():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D146
    value = 0.617

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E146():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E146
    value = None
    formula = '''=IF(F146>0,F146/D146,"")'''
    @eval_fn
    def E146():
        f146_1 = OLD_Input_EIA_Jet_Fuel_Price.F146()
        var_1 = greaterthan(f146_1, 0)
        f146_2 = OLD_Input_EIA_Jet_Fuel_Price.F146()
        d146_1 = OLD_Input_EIA_Jet_Fuel_Price.D146()
        var_2 = divide(f146_2, d146_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A147():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A147
    value = 35186
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B147():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B147
    value = 0.653832646479
    formula = "=D147*$B$3"
    @eval_fn
    def B147():
        d147_1 = OLD_Input_EIA_Jet_Fuel_Price.D147()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d147_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C147():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C147
    value = 35200
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D147():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D147
    value = 0.557

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E147():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E147
    value = None
    formula = '''=IF(F147>0,F147/D147,"")'''
    @eval_fn
    def E147():
        f147_1 = OLD_Input_EIA_Jet_Fuel_Price.F147()
        var_1 = greaterthan(f147_1, 0)
        f147_2 = OLD_Input_EIA_Jet_Fuel_Price.F147()
        d147_1 = OLD_Input_EIA_Jet_Fuel_Price.D147()
        var_2 = divide(f147_2, d147_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A148():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A148
    value = 35217
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B148():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B148
    value = 0.605704929234
    formula = "=D148*$B$3"
    @eval_fn
    def B148():
        d148_1 = OLD_Input_EIA_Jet_Fuel_Price.D148()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d148_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C148():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C148
    value = 35231
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D148():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D148
    value = 0.516

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E148():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E148
    value = None
    formula = '''=IF(F148>0,F148/D148,"")'''
    @eval_fn
    def E148():
        f148_1 = OLD_Input_EIA_Jet_Fuel_Price.F148()
        var_1 = greaterthan(f148_1, 0)
        f148_2 = OLD_Input_EIA_Jet_Fuel_Price.F148()
        d148_1 = OLD_Input_EIA_Jet_Fuel_Price.D148()
        var_2 = divide(f148_2, d148_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A149():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A149
    value = 35247
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B149():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B149
    value = 0.652658799717
    formula = "=D149*$B$3"
    @eval_fn
    def B149():
        d149_1 = OLD_Input_EIA_Jet_Fuel_Price.D149()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d149_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C149():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C149
    value = 35261
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D149():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D149
    value = 0.556

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E149():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E149
    value = None
    formula = '''=IF(F149>0,F149/D149,"")'''
    @eval_fn
    def E149():
        f149_1 = OLD_Input_EIA_Jet_Fuel_Price.F149()
        var_1 = greaterthan(f149_1, 0)
        f149_2 = OLD_Input_EIA_Jet_Fuel_Price.F149()
        d149_1 = OLD_Input_EIA_Jet_Fuel_Price.D149()
        var_2 = divide(f149_2, d149_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A150():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A150
    value = 35278
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B150():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B150
    value = 0.72191575868
    formula = "=D150*$B$3"
    @eval_fn
    def B150():
        d150_1 = OLD_Input_EIA_Jet_Fuel_Price.D150()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d150_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C150():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C150
    value = 35292
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D150():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D150
    value = 0.615

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E150():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E150
    value = None
    formula = '''=IF(F150>0,F150/D150,"")'''
    @eval_fn
    def E150():
        f150_1 = OLD_Input_EIA_Jet_Fuel_Price.F150()
        var_1 = greaterthan(f150_1, 0)
        f150_2 = OLD_Input_EIA_Jet_Fuel_Price.F150()
        d150_1 = OLD_Input_EIA_Jet_Fuel_Price.D150()
        var_2 = divide(f150_2, d150_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A151():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A151
    value = 35309
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B151():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B151
    value = 0.80056349174
    formula = "=D151*$B$3"
    @eval_fn
    def B151():
        d151_1 = OLD_Input_EIA_Jet_Fuel_Price.D151()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d151_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C151():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C151
    value = 35323
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D151():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D151
    value = 0.682

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E151():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E151
    value = None
    formula = '''=IF(F151>0,F151/D151,"")'''
    @eval_fn
    def E151():
        f151_1 = OLD_Input_EIA_Jet_Fuel_Price.F151()
        var_1 = greaterthan(f151_1, 0)
        f151_2 = OLD_Input_EIA_Jet_Fuel_Price.F151()
        d151_1 = OLD_Input_EIA_Jet_Fuel_Price.D151()
        var_2 = divide(f151_2, d151_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A152():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A152
    value = 35339
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B152():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B152
    value = 0.825214273743
    formula = "=D152*$B$3"
    @eval_fn
    def B152():
        d152_1 = OLD_Input_EIA_Jet_Fuel_Price.D152()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d152_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C152():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C152
    value = 35353
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D152():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D152
    value = 0.703

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E152():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E152
    value = None
    formula = '''=IF(F152>0,F152/D152,"")'''
    @eval_fn
    def E152():
        f152_1 = OLD_Input_EIA_Jet_Fuel_Price.F152()
        var_1 = greaterthan(f152_1, 0)
        f152_2 = OLD_Input_EIA_Jet_Fuel_Price.F152()
        d152_1 = OLD_Input_EIA_Jet_Fuel_Price.D152()
        var_2 = divide(f152_2, d152_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A153():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A153
    value = 35370
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B153():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B153
    value = 0.816997346409
    formula = "=D153*$B$3"
    @eval_fn
    def B153():
        d153_1 = OLD_Input_EIA_Jet_Fuel_Price.D153()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d153_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C153():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C153
    value = 35384
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D153():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D153
    value = 0.696

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E153():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E153
    value = None
    formula = '''=IF(F153>0,F153/D153,"")'''
    @eval_fn
    def E153():
        f153_1 = OLD_Input_EIA_Jet_Fuel_Price.F153()
        var_1 = greaterthan(f153_1, 0)
        f153_2 = OLD_Input_EIA_Jet_Fuel_Price.F153()
        d153_1 = OLD_Input_EIA_Jet_Fuel_Price.D153()
        var_2 = divide(f153_2, d153_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A154():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A154
    value = 35400
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B154():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B154
    value = 0.813475806122
    formula = "=D154*$B$3"
    @eval_fn
    def B154():
        d154_1 = OLD_Input_EIA_Jet_Fuel_Price.D154()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d154_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C154():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C154
    value = 35414
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D154():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D154
    value = 0.693

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E154():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E154
    value = None
    formula = '''=IF(F154>0,F154/D154,"")'''
    @eval_fn
    def E154():
        f154_1 = OLD_Input_EIA_Jet_Fuel_Price.F154()
        var_1 = greaterthan(f154_1, 0)
        f154_2 = OLD_Input_EIA_Jet_Fuel_Price.F154()
        d154_1 = OLD_Input_EIA_Jet_Fuel_Price.D154()
        var_2 = divide(f154_2, d154_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A155():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A155
    value = 35431
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B155():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B155
    value = 0.798215798215
    formula = "=D155*$B$3"
    @eval_fn
    def B155():
        d155_1 = OLD_Input_EIA_Jet_Fuel_Price.D155()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d155_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C155():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C155
    value = 35445
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D155():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D155
    value = 0.68

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E155():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E155
    value = None
    formula = '''=IF(F155>0,F155/D155,"")'''
    @eval_fn
    def E155():
        f155_1 = OLD_Input_EIA_Jet_Fuel_Price.F155()
        var_1 = greaterthan(f155_1, 0)
        f155_2 = OLD_Input_EIA_Jet_Fuel_Price.F155()
        d155_1 = OLD_Input_EIA_Jet_Fuel_Price.D155()
        var_2 = divide(f155_2, d155_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A156():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A156
    value = 35462
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B156():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B156
    value = 0.726611145728
    formula = "=D156*$B$3"
    @eval_fn
    def B156():
        d156_1 = OLD_Input_EIA_Jet_Fuel_Price.D156()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d156_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C156():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C156
    value = 35476
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D156():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D156
    value = 0.619

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E156():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E156
    value = None
    formula = '''=IF(F156>0,F156/D156,"")'''
    @eval_fn
    def E156():
        f156_1 = OLD_Input_EIA_Jet_Fuel_Price.F156()
        var_1 = greaterthan(f156_1, 0)
        f156_2 = OLD_Input_EIA_Jet_Fuel_Price.F156()
        d156_1 = OLD_Input_EIA_Jet_Fuel_Price.D156()
        var_2 = divide(f156_2, d156_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A157():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A157
    value = 35490
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B157():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B157
    value = 0.653832646479
    formula = "=D157*$B$3"
    @eval_fn
    def B157():
        d157_1 = OLD_Input_EIA_Jet_Fuel_Price.D157()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d157_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C157():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C157
    value = 35504
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D157():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D157
    value = 0.557

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E157():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E157
    value = None
    formula = '''=IF(F157>0,F157/D157,"")'''
    @eval_fn
    def E157():
        f157_1 = OLD_Input_EIA_Jet_Fuel_Price.F157()
        var_1 = greaterthan(f157_1, 0)
        f157_2 = OLD_Input_EIA_Jet_Fuel_Price.F157()
        d157_1 = OLD_Input_EIA_Jet_Fuel_Price.D157()
        var_2 = divide(f157_2, d157_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A158():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A158
    value = 35521
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B158():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B158
    value = 0.635051098286
    formula = "=D158*$B$3"
    @eval_fn
    def B158():
        d158_1 = OLD_Input_EIA_Jet_Fuel_Price.D158()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d158_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C158():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C158
    value = 35535
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D158():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D158
    value = 0.541

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E158():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E158
    value = None
    formula = '''=IF(F158>0,F158/D158,"")'''
    @eval_fn
    def E158():
        f158_1 = OLD_Input_EIA_Jet_Fuel_Price.F158()
        var_1 = greaterthan(f158_1, 0)
        f158_2 = OLD_Input_EIA_Jet_Fuel_Price.F158()
        d158_1 = OLD_Input_EIA_Jet_Fuel_Price.D158()
        var_2 = divide(f158_2, d158_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A159():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A159
    value = 35551
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B159():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B159
    value = 0.644441872383
    formula = "=D159*$B$3"
    @eval_fn
    def B159():
        d159_1 = OLD_Input_EIA_Jet_Fuel_Price.D159()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d159_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C159():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C159
    value = 35565
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D159():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D159
    value = 0.549

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E159():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E159
    value = None
    formula = '''=IF(F159>0,F159/D159,"")'''
    @eval_fn
    def E159():
        f159_1 = OLD_Input_EIA_Jet_Fuel_Price.F159()
        var_1 = greaterthan(f159_1, 0)
        f159_2 = OLD_Input_EIA_Jet_Fuel_Price.F159()
        d159_1 = OLD_Input_EIA_Jet_Fuel_Price.D159()
        var_2 = divide(f159_2, d159_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A160():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A160
    value = 35582
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B160():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B160
    value = 0.613921856569
    formula = "=D160*$B$3"
    @eval_fn
    def B160():
        d160_1 = OLD_Input_EIA_Jet_Fuel_Price.D160()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d160_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C160():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C160
    value = 35596
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D160():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D160
    value = 0.523

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E160():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E160
    value = None
    formula = '''=IF(F160>0,F160/D160,"")'''
    @eval_fn
    def E160():
        f160_1 = OLD_Input_EIA_Jet_Fuel_Price.F160()
        var_1 = greaterthan(f160_1, 0)
        f160_2 = OLD_Input_EIA_Jet_Fuel_Price.F160()
        d160_1 = OLD_Input_EIA_Jet_Fuel_Price.D160()
        var_2 = divide(f160_2, d160_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A161():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A161
    value = 35612
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B161():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B161
    value = 0.629181864476
    formula = "=D161*$B$3"
    @eval_fn
    def B161():
        d161_1 = OLD_Input_EIA_Jet_Fuel_Price.D161()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d161_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C161():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C161
    value = 35626
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D161():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D161
    value = 0.536

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E161():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E161
    value = None
    formula = '''=IF(F161>0,F161/D161,"")'''
    @eval_fn
    def E161():
        f161_1 = OLD_Input_EIA_Jet_Fuel_Price.F161()
        var_1 = greaterthan(f161_1, 0)
        f161_2 = OLD_Input_EIA_Jet_Fuel_Price.F161()
        d161_1 = OLD_Input_EIA_Jet_Fuel_Price.D161()
        var_2 = divide(f161_2, d161_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A162():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A162
    value = 35643
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B162():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B162
    value = 0.656180340004
    formula = "=D162*$B$3"
    @eval_fn
    def B162():
        d162_1 = OLD_Input_EIA_Jet_Fuel_Price.D162()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d162_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C162():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C162
    value = 35657
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D162():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D162
    value = 0.559

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E162():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E162
    value = None
    formula = '''=IF(F162>0,F162/D162,"")'''
    @eval_fn
    def E162():
        f162_1 = OLD_Input_EIA_Jet_Fuel_Price.F162()
        var_1 = greaterthan(f162_1, 0)
        f162_2 = OLD_Input_EIA_Jet_Fuel_Price.F162()
        d162_1 = OLD_Input_EIA_Jet_Fuel_Price.D162()
        var_2 = divide(f162_2, d162_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A163():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A163
    value = 35674
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B163():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B163
    value = 0.635051098286
    formula = "=D163*$B$3"
    @eval_fn
    def B163():
        d163_1 = OLD_Input_EIA_Jet_Fuel_Price.D163()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d163_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C163():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C163
    value = 35688
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D163():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D163
    value = 0.541

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E163():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E163
    value = None
    formula = '''=IF(F163>0,F163/D163,"")'''
    @eval_fn
    def E163():
        f163_1 = OLD_Input_EIA_Jet_Fuel_Price.F163()
        var_1 = greaterthan(f163_1, 0)
        f163_2 = OLD_Input_EIA_Jet_Fuel_Price.F163()
        d163_1 = OLD_Input_EIA_Jet_Fuel_Price.D163()
        var_2 = divide(f163_2, d163_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A164():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A164
    value = 35704
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B164():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B164
    value = 0.670266501149
    formula = "=D164*$B$3"
    @eval_fn
    def B164():
        d164_1 = OLD_Input_EIA_Jet_Fuel_Price.D164()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d164_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C164():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C164
    value = 35718
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D164():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D164
    value = 0.571

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E164():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E164
    value = None
    formula = '''=IF(F164>0,F164/D164,"")'''
    @eval_fn
    def E164():
        f164_1 = OLD_Input_EIA_Jet_Fuel_Price.F164()
        var_1 = greaterthan(f164_1, 0)
        f164_2 = OLD_Input_EIA_Jet_Fuel_Price.F164()
        d164_1 = OLD_Input_EIA_Jet_Fuel_Price.D164()
        var_2 = divide(f164_2, d164_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A165():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A165
    value = 35735
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B165():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B165
    value = 0.644441872383
    formula = "=D165*$B$3"
    @eval_fn
    def B165():
        d165_1 = OLD_Input_EIA_Jet_Fuel_Price.D165()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d165_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C165():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C165
    value = 35749
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D165():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D165
    value = 0.549

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E165():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E165
    value = None
    formula = '''=IF(F165>0,F165/D165,"")'''
    @eval_fn
    def E165():
        f165_1 = OLD_Input_EIA_Jet_Fuel_Price.F165()
        var_1 = greaterthan(f165_1, 0)
        f165_2 = OLD_Input_EIA_Jet_Fuel_Price.F165()
        d165_1 = OLD_Input_EIA_Jet_Fuel_Price.D165()
        var_2 = divide(f165_2, d165_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A166():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A166
    value = 35765
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B166():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B166
    value = 0.582227993992
    formula = "=D166*$B$3"
    @eval_fn
    def B166():
        d166_1 = OLD_Input_EIA_Jet_Fuel_Price.D166()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d166_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C166():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C166
    value = 35779
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D166():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D166
    value = 0.496

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E166():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E166
    value = None
    formula = '''=IF(F166>0,F166/D166,"")'''
    @eval_fn
    def E166():
        f166_1 = OLD_Input_EIA_Jet_Fuel_Price.F166()
        var_1 = greaterthan(f166_1, 0)
        f166_2 = OLD_Input_EIA_Jet_Fuel_Price.F166()
        d166_1 = OLD_Input_EIA_Jet_Fuel_Price.D166()
        var_2 = divide(f166_2, d166_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A167():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A167
    value = 35796
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B167():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B167
    value = 0.558751058751
    formula = "=D167*$B$3"
    @eval_fn
    def B167():
        d167_1 = OLD_Input_EIA_Jet_Fuel_Price.D167()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d167_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C167():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C167
    value = 35810
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D167():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D167
    value = 0.476

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E167():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E167
    value = None
    formula = '''=IF(F167>0,F167/D167,"")'''
    @eval_fn
    def E167():
        f167_1 = OLD_Input_EIA_Jet_Fuel_Price.F167()
        var_1 = greaterthan(f167_1, 0)
        f167_2 = OLD_Input_EIA_Jet_Fuel_Price.F167()
        d167_1 = OLD_Input_EIA_Jet_Fuel_Price.D167()
        var_2 = divide(f167_2, d167_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A168():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A168
    value = 35827
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B168():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B168
    value = 0.527057196175
    formula = "=D168*$B$3"
    @eval_fn
    def B168():
        d168_1 = OLD_Input_EIA_Jet_Fuel_Price.D168()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d168_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C168():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C168
    value = 35841
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D168():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D168
    value = 0.449

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E168():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E168
    value = None
    formula = '''=IF(F168>0,F168/D168,"")'''
    @eval_fn
    def E168():
        f168_1 = OLD_Input_EIA_Jet_Fuel_Price.F168()
        var_1 = greaterthan(f168_1, 0)
        f168_2 = OLD_Input_EIA_Jet_Fuel_Price.F168()
        d168_1 = OLD_Input_EIA_Jet_Fuel_Price.D168()
        var_2 = divide(f168_2, d168_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A169():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A169
    value = 35855
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B169():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B169
    value = 0.48479871274
    formula = "=D169*$B$3"
    @eval_fn
    def B169():
        d169_1 = OLD_Input_EIA_Jet_Fuel_Price.D169()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d169_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C169():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C169
    value = 35869
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D169():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D169
    value = 0.413

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E169():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E169
    value = None
    formula = '''=IF(F169>0,F169/D169,"")'''
    @eval_fn
    def E169():
        f169_1 = OLD_Input_EIA_Jet_Fuel_Price.F169()
        var_1 = greaterthan(f169_1, 0)
        f169_2 = OLD_Input_EIA_Jet_Fuel_Price.F169()
        d169_1 = OLD_Input_EIA_Jet_Fuel_Price.D169()
        var_2 = divide(f169_2, d169_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A170():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A170
    value = 35886
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B170():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B170
    value = 0.500058720647
    formula = "=D170*$B$3"
    @eval_fn
    def B170():
        d170_1 = OLD_Input_EIA_Jet_Fuel_Price.D170()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d170_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C170():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C170
    value = 35900
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D170():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D170
    value = 0.426

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E170():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E170
    value = None
    formula = '''=IF(F170>0,F170/D170,"")'''
    @eval_fn
    def E170():
        f170_1 = OLD_Input_EIA_Jet_Fuel_Price.F170()
        var_1 = greaterthan(f170_1, 0)
        f170_2 = OLD_Input_EIA_Jet_Fuel_Price.F170()
        d170_1 = OLD_Input_EIA_Jet_Fuel_Price.D170()
        var_2 = divide(f170_2, d170_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A171():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A171
    value = 35916
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B171():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B171
    value = 0.488320253026
    formula = "=D171*$B$3"
    @eval_fn
    def B171():
        d171_1 = OLD_Input_EIA_Jet_Fuel_Price.D171()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d171_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C171():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C171
    value = 35930
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D171():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D171
    value = 0.416

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E171():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E171
    value = None
    formula = '''=IF(F171>0,F171/D171,"")'''
    @eval_fn
    def E171():
        f171_1 = OLD_Input_EIA_Jet_Fuel_Price.F171()
        var_1 = greaterthan(f171_1, 0)
        f171_2 = OLD_Input_EIA_Jet_Fuel_Price.F171()
        d171_1 = OLD_Input_EIA_Jet_Fuel_Price.D171()
        var_2 = divide(f171_2, d171_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A172():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A172
    value = 35947
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B172():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B172
    value = 0.45662639045
    formula = "=D172*$B$3"
    @eval_fn
    def B172():
        d172_1 = OLD_Input_EIA_Jet_Fuel_Price.D172()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d172_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C172():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C172
    value = 35961
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D172():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D172
    value = 0.389

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E172():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E172
    value = None
    formula = '''=IF(F172>0,F172/D172,"")'''
    @eval_fn
    def E172():
        f172_1 = OLD_Input_EIA_Jet_Fuel_Price.F172()
        var_1 = greaterthan(f172_1, 0)
        f172_2 = OLD_Input_EIA_Jet_Fuel_Price.F172()
        d172_1 = OLD_Input_EIA_Jet_Fuel_Price.D172()
        var_2 = divide(f172_2, d172_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A173():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A173
    value = 35977
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B173():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B173
    value = 0.453104850163
    formula = "=D173*$B$3"
    @eval_fn
    def B173():
        d173_1 = OLD_Input_EIA_Jet_Fuel_Price.D173()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d173_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C173():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C173
    value = 35991
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D173():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D173
    value = 0.386

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E173():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E173
    value = None
    formula = '''=IF(F173>0,F173/D173,"")'''
    @eval_fn
    def E173():
        f173_1 = OLD_Input_EIA_Jet_Fuel_Price.F173()
        var_1 = greaterthan(f173_1, 0)
        f173_2 = OLD_Input_EIA_Jet_Fuel_Price.F173()
        d173_1 = OLD_Input_EIA_Jet_Fuel_Price.D173()
        var_2 = divide(f173_2, d173_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A174():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A174
    value = 36008
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B174():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B174
    value = 0.436670995494
    formula = "=D174*$B$3"
    @eval_fn
    def B174():
        d174_1 = OLD_Input_EIA_Jet_Fuel_Price.D174()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d174_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C174():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C174
    value = 36022
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D174():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D174
    value = 0.372

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E174():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E174
    value = None
    formula = '''=IF(F174>0,F174/D174,"")'''
    @eval_fn
    def E174():
        f174_1 = OLD_Input_EIA_Jet_Fuel_Price.F174()
        var_1 = greaterthan(f174_1, 0)
        f174_2 = OLD_Input_EIA_Jet_Fuel_Price.F174()
        d174_1 = OLD_Input_EIA_Jet_Fuel_Price.D174()
        var_2 = divide(f174_2, d174_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A175():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A175
    value = 36039
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B175():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B175
    value = 0.493015640074
    formula = "=D175*$B$3"
    @eval_fn
    def B175():
        d175_1 = OLD_Input_EIA_Jet_Fuel_Price.D175()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d175_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C175():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C175
    value = 36053
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D175():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D175
    value = 0.42

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E175():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E175
    value = None
    formula = '''=IF(F175>0,F175/D175,"")'''
    @eval_fn
    def E175():
        f175_1 = OLD_Input_EIA_Jet_Fuel_Price.F175()
        var_1 = greaterthan(f175_1, 0)
        f175_2 = OLD_Input_EIA_Jet_Fuel_Price.F175()
        d175_1 = OLD_Input_EIA_Jet_Fuel_Price.D175()
        var_2 = divide(f175_2, d175_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A176():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A176
    value = 36069
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B176():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B176
    value = 0.493015640074
    formula = "=D176*$B$3"
    @eval_fn
    def B176():
        d176_1 = OLD_Input_EIA_Jet_Fuel_Price.D176()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d176_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C176():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C176
    value = 36083
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D176():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D176
    value = 0.42

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E176():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E176
    value = None
    formula = '''=IF(F176>0,F176/D176,"")'''
    @eval_fn
    def E176():
        f176_1 = OLD_Input_EIA_Jet_Fuel_Price.F176()
        var_1 = greaterthan(f176_1, 0)
        f176_2 = OLD_Input_EIA_Jet_Fuel_Price.F176()
        d176_1 = OLD_Input_EIA_Jet_Fuel_Price.D176()
        var_2 = divide(f176_2, d176_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A177():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A177
    value = 36100
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B177():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B177
    value = 0.435497148732
    formula = "=D177*$B$3"
    @eval_fn
    def B177():
        d177_1 = OLD_Input_EIA_Jet_Fuel_Price.D177()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d177_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C177():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C177
    value = 36114
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D177():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D177
    value = 0.371

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E177():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E177
    value = None
    formula = '''=IF(F177>0,F177/D177,"")'''
    @eval_fn
    def E177():
        f177_1 = OLD_Input_EIA_Jet_Fuel_Price.F177()
        var_1 = greaterthan(f177_1, 0)
        f177_2 = OLD_Input_EIA_Jet_Fuel_Price.F177()
        d177_1 = OLD_Input_EIA_Jet_Fuel_Price.D177()
        var_2 = divide(f177_2, d177_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A178():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A178
    value = 36130
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B178():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B178
    value = 0.356849415673
    formula = "=D178*$B$3"
    @eval_fn
    def B178():
        d178_1 = OLD_Input_EIA_Jet_Fuel_Price.D178()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d178_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C178():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C178
    value = 36144
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D178():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D178
    value = 0.304

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E178():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E178
    value = None
    formula = '''=IF(F178>0,F178/D178,"")'''
    @eval_fn
    def E178():
        f178_1 = OLD_Input_EIA_Jet_Fuel_Price.F178()
        var_1 = greaterthan(f178_1, 0)
        f178_2 = OLD_Input_EIA_Jet_Fuel_Price.F178()
        d178_1 = OLD_Input_EIA_Jet_Fuel_Price.D178()
        var_2 = divide(f178_2, d178_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A179():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A179
    value = 36161
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B179():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B179
    value = 0.392064818535
    formula = "=D179*$B$3"
    @eval_fn
    def B179():
        d179_1 = OLD_Input_EIA_Jet_Fuel_Price.D179()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d179_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C179():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C179
    value = 36175
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D179():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D179
    value = 0.334

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E179():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E179
    value = None
    formula = '''=IF(F179>0,F179/D179,"")'''
    @eval_fn
    def E179():
        f179_1 = OLD_Input_EIA_Jet_Fuel_Price.F179()
        var_1 = greaterthan(f179_1, 0)
        f179_2 = OLD_Input_EIA_Jet_Fuel_Price.F179()
        d179_1 = OLD_Input_EIA_Jet_Fuel_Price.D179()
        var_2 = divide(f179_2, d179_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A180():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A180
    value = 36192
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B180():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B180
    value = 0.362718649483
    formula = "=D180*$B$3"
    @eval_fn
    def B180():
        d180_1 = OLD_Input_EIA_Jet_Fuel_Price.D180()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d180_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C180():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C180
    value = 36206
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D180():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D180
    value = 0.309

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E180():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E180
    value = None
    formula = '''=IF(F180>0,F180/D180,"")'''
    @eval_fn
    def E180():
        f180_1 = OLD_Input_EIA_Jet_Fuel_Price.F180()
        var_1 = greaterthan(f180_1, 0)
        f180_2 = OLD_Input_EIA_Jet_Fuel_Price.F180()
        d180_1 = OLD_Input_EIA_Jet_Fuel_Price.D180()
        var_2 = divide(f180_2, d180_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A181():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A181
    value = 36220
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B181():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B181
    value = 0.443714076067
    formula = "=D181*$B$3"
    @eval_fn
    def B181():
        d181_1 = OLD_Input_EIA_Jet_Fuel_Price.D181()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d181_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C181():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C181
    value = 36234
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D181():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D181
    value = 0.378

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E181():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E181
    value = None
    formula = '''=IF(F181>0,F181/D181,"")'''
    @eval_fn
    def E181():
        f181_1 = OLD_Input_EIA_Jet_Fuel_Price.F181()
        var_1 = greaterthan(f181_1, 0)
        f181_2 = OLD_Input_EIA_Jet_Fuel_Price.F181()
        d181_1 = OLD_Input_EIA_Jet_Fuel_Price.D181()
        var_2 = divide(f181_2, d181_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A182():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A182
    value = 36251
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B182():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B182
    value = 0.504754107695
    formula = "=D182*$B$3"
    @eval_fn
    def B182():
        d182_1 = OLD_Input_EIA_Jet_Fuel_Price.D182()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d182_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C182():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C182
    value = 36265
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D182():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D182
    value = 0.43

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E182():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E182
    value = None
    formula = '''=IF(F182>0,F182/D182,"")'''
    @eval_fn
    def E182():
        f182_1 = OLD_Input_EIA_Jet_Fuel_Price.F182()
        var_1 = greaterthan(f182_1, 0)
        f182_2 = OLD_Input_EIA_Jet_Fuel_Price.F182()
        d182_1 = OLD_Input_EIA_Jet_Fuel_Price.D182()
        var_2 = divide(f182_2, d182_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A183():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A183
    value = 36281
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B183():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B183
    value = 0.487146406264
    formula = "=D183*$B$3"
    @eval_fn
    def B183():
        d183_1 = OLD_Input_EIA_Jet_Fuel_Price.D183()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d183_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C183():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C183
    value = 36295
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D183():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D183
    value = 0.415

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E183():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E183
    value = None
    formula = '''=IF(F183>0,F183/D183,"")'''
    @eval_fn
    def E183():
        f183_1 = OLD_Input_EIA_Jet_Fuel_Price.F183()
        var_1 = greaterthan(f183_1, 0)
        f183_2 = OLD_Input_EIA_Jet_Fuel_Price.F183()
        d183_1 = OLD_Input_EIA_Jet_Fuel_Price.D183()
        var_2 = divide(f183_2, d183_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A184():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A184
    value = 36312
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B184():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B184
    value = 0.516492575316
    formula = "=D184*$B$3"
    @eval_fn
    def B184():
        d184_1 = OLD_Input_EIA_Jet_Fuel_Price.D184()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d184_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C184():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C184
    value = 36326
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D184():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D184
    value = 0.44

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E184():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E184
    value = None
    formula = '''=IF(F184>0,F184/D184,"")'''
    @eval_fn
    def E184():
        f184_1 = OLD_Input_EIA_Jet_Fuel_Price.F184()
        var_1 = greaterthan(f184_1, 0)
        f184_2 = OLD_Input_EIA_Jet_Fuel_Price.F184()
        d184_1 = OLD_Input_EIA_Jet_Fuel_Price.D184()
        var_2 = divide(f184_2, d184_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A185():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A185
    value = 36342
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B185():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B185
    value = 0.601009542186
    formula = "=D185*$B$3"
    @eval_fn
    def B185():
        d185_1 = OLD_Input_EIA_Jet_Fuel_Price.D185()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d185_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C185():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C185
    value = 36356
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D185():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D185
    value = 0.512

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E185():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E185
    value = None
    formula = '''=IF(F185>0,F185/D185,"")'''
    @eval_fn
    def E185():
        f185_1 = OLD_Input_EIA_Jet_Fuel_Price.F185()
        var_1 = greaterthan(f185_1, 0)
        f185_2 = OLD_Input_EIA_Jet_Fuel_Price.F185()
        d185_1 = OLD_Input_EIA_Jet_Fuel_Price.D185()
        var_2 = divide(f185_2, d185_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A186():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A186
    value = 36373
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B186():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B186
    value = 0.662049573814
    formula = "=D186*$B$3"
    @eval_fn
    def B186():
        d186_1 = OLD_Input_EIA_Jet_Fuel_Price.D186()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d186_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C186():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C186
    value = 36387
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D186():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D186
    value = 0.564

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E186():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E186
    value = None
    formula = '''=IF(F186>0,F186/D186,"")'''
    @eval_fn
    def E186():
        f186_1 = OLD_Input_EIA_Jet_Fuel_Price.F186()
        var_1 = greaterthan(f186_1, 0)
        f186_2 = OLD_Input_EIA_Jet_Fuel_Price.F186()
        d186_1 = OLD_Input_EIA_Jet_Fuel_Price.D186()
        var_2 = divide(f186_2, d186_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A187():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A187
    value = 36404
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B187():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B187
    value = 0.720741911918
    formula = "=D187*$B$3"
    @eval_fn
    def B187():
        d187_1 = OLD_Input_EIA_Jet_Fuel_Price.D187()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d187_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C187():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C187
    value = 36418
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D187():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D187
    value = 0.614

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E187():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E187
    value = None
    formula = '''=IF(F187>0,F187/D187,"")'''
    @eval_fn
    def E187():
        f187_1 = OLD_Input_EIA_Jet_Fuel_Price.F187()
        var_1 = greaterthan(f187_1, 0)
        f187_2 = OLD_Input_EIA_Jet_Fuel_Price.F187()
        d187_1 = OLD_Input_EIA_Jet_Fuel_Price.D187()
        var_2 = divide(f187_2, d187_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A188():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A188
    value = 36434
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B188():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B188
    value = 0.698438823438
    formula = "=D188*$B$3"
    @eval_fn
    def B188():
        d188_1 = OLD_Input_EIA_Jet_Fuel_Price.D188()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d188_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C188():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C188
    value = 36448
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D188():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D188
    value = 0.595

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E188():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E188
    value = None
    formula = '''=IF(F188>0,F188/D188,"")'''
    @eval_fn
    def E188():
        f188_1 = OLD_Input_EIA_Jet_Fuel_Price.F188()
        var_1 = greaterthan(f188_1, 0)
        f188_2 = OLD_Input_EIA_Jet_Fuel_Price.F188()
        d188_1 = OLD_Input_EIA_Jet_Fuel_Price.D188()
        var_2 = divide(f188_2, d188_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A189():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A189
    value = 36465
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B189():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B189
    value = 0.775912709736
    formula = "=D189*$B$3"
    @eval_fn
    def B189():
        d189_1 = OLD_Input_EIA_Jet_Fuel_Price.D189()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d189_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C189():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C189
    value = 36479
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D189():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D189
    value = 0.661

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E189():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E189
    value = None
    formula = '''=IF(F189>0,F189/D189,"")'''
    @eval_fn
    def E189():
        f189_1 = OLD_Input_EIA_Jet_Fuel_Price.F189()
        var_1 = greaterthan(f189_1, 0)
        f189_2 = OLD_Input_EIA_Jet_Fuel_Price.F189()
        d189_1 = OLD_Input_EIA_Jet_Fuel_Price.D189()
        var_2 = divide(f189_2, d189_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A190
    value = 36495
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B190
    value = 0.822866580219
    formula = "=D190*$B$3"
    @eval_fn
    def B190():
        d190_1 = OLD_Input_EIA_Jet_Fuel_Price.D190()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d190_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C190
    value = 36509
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D190
    value = 0.701

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E190
    value = 1.23109843081
    formula = '''=IF(F190>0,F190/D190,"")'''
    @eval_fn
    def E190():
        f190_1 = OLD_Input_EIA_Jet_Fuel_Price.F190()
        var_1 = greaterthan(f190_1, 0)
        f190_2 = OLD_Input_EIA_Jet_Fuel_Price.F190()
        d190_1 = OLD_Input_EIA_Jet_Fuel_Price.D190()
        var_2 = divide(f190_2, d190_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F190():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F190
    value = 0.863

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A191():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A191
    value = 36526
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B191():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B191
    value = 0.916774321186
    formula = "=D191*$B$3"
    @eval_fn
    def B191():
        d191_1 = OLD_Input_EIA_Jet_Fuel_Price.D191()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d191_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C191():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C191
    value = 36540
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D191():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D191
    value = 0.781

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E191():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E191
    value = None
    formula = '''=IF(F191>0,F191/D191,"")'''
    @eval_fn
    def E191():
        f191_1 = OLD_Input_EIA_Jet_Fuel_Price.F191()
        var_1 = greaterthan(f191_1, 0)
        f191_2 = OLD_Input_EIA_Jet_Fuel_Price.F191()
        d191_1 = OLD_Input_EIA_Jet_Fuel_Price.D191()
        var_2 = divide(f191_2, d191_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A192
    value = 36557
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B192
    value = 0.915600474424
    formula = "=D192*$B$3"
    @eval_fn
    def B192():
        d192_1 = OLD_Input_EIA_Jet_Fuel_Price.D192()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d192_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C192
    value = 36571
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D192
    value = 0.78

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E192
    value = 1.27307692308
    formula = '''=IF(F192>0,F192/D192,"")'''
    @eval_fn
    def E192():
        f192_1 = OLD_Input_EIA_Jet_Fuel_Price.F192()
        var_1 = greaterthan(f192_1, 0)
        f192_2 = OLD_Input_EIA_Jet_Fuel_Price.F192()
        d192_1 = OLD_Input_EIA_Jet_Fuel_Price.D192()
        var_2 = divide(f192_2, d192_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F192():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F192
    value = 0.993

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A193():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A193
    value = 36586
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B193():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B193
    value = 0.905035853565
    formula = "=D193*$B$3"
    @eval_fn
    def B193():
        d193_1 = OLD_Input_EIA_Jet_Fuel_Price.D193()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d193_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C193():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C193
    value = 36600
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D193():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D193
    value = 0.771

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E193():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E193
    value = None
    formula = '''=IF(F193>0,F193/D193,"")'''
    @eval_fn
    def E193():
        f193_1 = OLD_Input_EIA_Jet_Fuel_Price.F193()
        var_1 = greaterthan(f193_1, 0)
        f193_2 = OLD_Input_EIA_Jet_Fuel_Price.F193()
        d193_1 = OLD_Input_EIA_Jet_Fuel_Price.D193()
        var_2 = divide(f193_2, d193_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A194():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A194
    value = 36617
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B194():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B194
    value = 0.843995821937
    formula = "=D194*$B$3"
    @eval_fn
    def B194():
        d194_1 = OLD_Input_EIA_Jet_Fuel_Price.D194()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d194_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C194():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C194
    value = 36631
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D194():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D194
    value = 0.719

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E194():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E194
    value = None
    formula = '''=IF(F194>0,F194/D194,"")'''
    @eval_fn
    def E194():
        f194_1 = OLD_Input_EIA_Jet_Fuel_Price.F194()
        var_1 = greaterthan(f194_1, 0)
        f194_2 = OLD_Input_EIA_Jet_Fuel_Price.F194()
        d194_1 = OLD_Input_EIA_Jet_Fuel_Price.D194()
        var_2 = divide(f194_2, d194_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A195():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A195
    value = 36647
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B195():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B195
    value = 0.894471232706
    formula = "=D195*$B$3"
    @eval_fn
    def B195():
        d195_1 = OLD_Input_EIA_Jet_Fuel_Price.D195()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d195_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C195():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C195
    value = 36661
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D195():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D195
    value = 0.762

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E195():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E195
    value = None
    formula = '''=IF(F195>0,F195/D195,"")'''
    @eval_fn
    def E195():
        f195_1 = OLD_Input_EIA_Jet_Fuel_Price.F195()
        var_1 = greaterthan(f195_1, 0)
        f195_2 = OLD_Input_EIA_Jet_Fuel_Price.F195()
        d195_1 = OLD_Input_EIA_Jet_Fuel_Price.D195()
        var_2 = divide(f195_2, d195_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A196():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A196
    value = 36678
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B196():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B196
    value = 0.921469708234
    formula = "=D196*$B$3"
    @eval_fn
    def B196():
        d196_1 = OLD_Input_EIA_Jet_Fuel_Price.D196()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d196_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C196():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C196
    value = 36692
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D196():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D196
    value = 0.785

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E196():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E196
    value = None
    formula = '''=IF(F196>0,F196/D196,"")'''
    @eval_fn
    def E196():
        f196_1 = OLD_Input_EIA_Jet_Fuel_Price.F196()
        var_1 = greaterthan(f196_1, 0)
        f196_2 = OLD_Input_EIA_Jet_Fuel_Price.F196()
        d196_1 = OLD_Input_EIA_Jet_Fuel_Price.D196()
        var_2 = divide(f196_2, d196_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A197():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A197
    value = 36708
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B197():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B197
    value = 0.934382022617
    formula = "=D197*$B$3"
    @eval_fn
    def B197():
        d197_1 = OLD_Input_EIA_Jet_Fuel_Price.D197()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d197_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C197():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C197
    value = 36722
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D197():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D197
    value = 0.796

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E197():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E197
    value = None
    formula = '''=IF(F197>0,F197/D197,"")'''
    @eval_fn
    def E197():
        f197_1 = OLD_Input_EIA_Jet_Fuel_Price.F197()
        var_1 = greaterthan(f197_1, 0)
        f197_2 = OLD_Input_EIA_Jet_Fuel_Price.F197()
        d197_1 = OLD_Input_EIA_Jet_Fuel_Price.D197()
        var_2 = divide(f197_2, d197_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A198():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A198
    value = 36739
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B198():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B198
    value = 1.05646208587
    formula = "=D198*$B$3"
    @eval_fn
    def B198():
        d198_1 = OLD_Input_EIA_Jet_Fuel_Price.D198()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d198_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C198():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C198
    value = 36753
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D198():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D198
    value = 0.9

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E198():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E198
    value = None
    formula = '''=IF(F198>0,F198/D198,"")'''
    @eval_fn
    def E198():
        f198_1 = OLD_Input_EIA_Jet_Fuel_Price.F198()
        var_1 = greaterthan(f198_1, 0)
        f198_2 = OLD_Input_EIA_Jet_Fuel_Price.F198()
        d198_1 = OLD_Input_EIA_Jet_Fuel_Price.D198()
        var_2 = divide(f198_2, d198_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A199():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A199
    value = 36770
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B199():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B199
    value = 1.19380215704
    formula = "=D199*$B$3"
    @eval_fn
    def B199():
        d199_1 = OLD_Input_EIA_Jet_Fuel_Price.D199()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d199_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C199():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C199
    value = 36784
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D199():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D199
    value = 1.017

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E199():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E199
    value = None
    formula = '''=IF(F199>0,F199/D199,"")'''
    @eval_fn
    def E199():
        f199_1 = OLD_Input_EIA_Jet_Fuel_Price.F199()
        var_1 = greaterthan(f199_1, 0)
        f199_2 = OLD_Input_EIA_Jet_Fuel_Price.F199()
        d199_1 = OLD_Input_EIA_Jet_Fuel_Price.D199()
        var_2 = divide(f199_2, d199_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A200():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A200
    value = 36800
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B200():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B200
    value = 1.15271752036
    formula = "=D200*$B$3"
    @eval_fn
    def B200():
        d200_1 = OLD_Input_EIA_Jet_Fuel_Price.D200()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d200_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C200():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C200
    value = 36814
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D200():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D200
    value = 0.982

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E200():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E200
    value = None
    formula = '''=IF(F200>0,F200/D200,"")'''
    @eval_fn
    def E200():
        f200_1 = OLD_Input_EIA_Jet_Fuel_Price.F200()
        var_1 = greaterthan(f200_1, 0)
        f200_2 = OLD_Input_EIA_Jet_Fuel_Price.F200()
        d200_1 = OLD_Input_EIA_Jet_Fuel_Price.D200()
        var_2 = divide(f200_2, d200_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A201():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A201
    value = 36831
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B201():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B201
    value = 1.20671447142
    formula = "=D201*$B$3"
    @eval_fn
    def B201():
        d201_1 = OLD_Input_EIA_Jet_Fuel_Price.D201()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d201_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C201():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C201
    value = 36845
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D201():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D201
    value = 1.028

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E201():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E201
    value = None
    formula = '''=IF(F201>0,F201/D201,"")'''
    @eval_fn
    def E201():
        f201_1 = OLD_Input_EIA_Jet_Fuel_Price.F201()
        var_1 = greaterthan(f201_1, 0)
        f201_2 = OLD_Input_EIA_Jet_Fuel_Price.F201()
        d201_1 = OLD_Input_EIA_Jet_Fuel_Price.D201()
        var_2 = divide(f201_2, d201_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A202():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A202
    value = 36861
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B202():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B202
    value = 1.01302975568
    formula = "=D202*$B$3"
    @eval_fn
    def B202():
        d202_1 = OLD_Input_EIA_Jet_Fuel_Price.D202()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d202_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C202():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C202
    value = 36875
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D202():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D202
    value = 0.863

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E202():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E202
    value = None
    formula = '''=IF(F202>0,F202/D202,"")'''
    @eval_fn
    def E202():
        f202_1 = OLD_Input_EIA_Jet_Fuel_Price.F202()
        var_1 = greaterthan(f202_1, 0)
        f202_2 = OLD_Input_EIA_Jet_Fuel_Price.F202()
        d202_1 = OLD_Input_EIA_Jet_Fuel_Price.D202()
        var_2 = divide(f202_2, d202_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A203():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A203
    value = 36892
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B203():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B203
    value = 1.02124668301
    formula = "=D203*$B$3"
    @eval_fn
    def B203():
        d203_1 = OLD_Input_EIA_Jet_Fuel_Price.D203()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d203_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C203():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C203
    value = 36906
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D203():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D203
    value = 0.87

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E203():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E203
    value = None
    formula = '''=IF(F203>0,F203/D203,"")'''
    @eval_fn
    def E203():
        f203_1 = OLD_Input_EIA_Jet_Fuel_Price.F203()
        var_1 = greaterthan(f203_1, 0)
        f203_2 = OLD_Input_EIA_Jet_Fuel_Price.F203()
        d203_1 = OLD_Input_EIA_Jet_Fuel_Price.D203()
        var_2 = divide(f203_2, d203_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A204():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A204
    value = 36923
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B204():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B204
    value = 0.956685111096
    formula = "=D204*$B$3"
    @eval_fn
    def B204():
        d204_1 = OLD_Input_EIA_Jet_Fuel_Price.D204()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d204_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C204():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C204
    value = 36937
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D204():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D204
    value = 0.815

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E204():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E204
    value = None
    formula = '''=IF(F204>0,F204/D204,"")'''
    @eval_fn
    def E204():
        f204_1 = OLD_Input_EIA_Jet_Fuel_Price.F204()
        var_1 = greaterthan(f204_1, 0)
        f204_2 = OLD_Input_EIA_Jet_Fuel_Price.F204()
        d204_1 = OLD_Input_EIA_Jet_Fuel_Price.D204()
        var_2 = divide(f204_2, d204_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A205():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A205
    value = 36951
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B205():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B205
    value = 0.878037378037
    formula = "=D205*$B$3"
    @eval_fn
    def B205():
        d205_1 = OLD_Input_EIA_Jet_Fuel_Price.D205()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d205_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C205():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C205
    value = 36965
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D205():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D205
    value = 0.748

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E205():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E205
    value = None
    formula = '''=IF(F205>0,F205/D205,"")'''
    @eval_fn
    def E205():
        f205_1 = OLD_Input_EIA_Jet_Fuel_Price.F205()
        var_1 = greaterthan(f205_1, 0)
        f205_2 = OLD_Input_EIA_Jet_Fuel_Price.F205()
        d205_1 = OLD_Input_EIA_Jet_Fuel_Price.D205()
        var_2 = divide(f205_2, d205_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A206():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A206
    value = 36982
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B206():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B206
    value = 0.903862006803
    formula = "=D206*$B$3"
    @eval_fn
    def B206():
        d206_1 = OLD_Input_EIA_Jet_Fuel_Price.D206()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d206_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C206():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C206
    value = 36996
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D206():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D206
    value = 0.77

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E206():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E206
    value = None
    formula = '''=IF(F206>0,F206/D206,"")'''
    @eval_fn
    def E206():
        f206_1 = OLD_Input_EIA_Jet_Fuel_Price.F206()
        var_1 = greaterthan(f206_1, 0)
        f206_2 = OLD_Input_EIA_Jet_Fuel_Price.F206()
        d206_1 = OLD_Input_EIA_Jet_Fuel_Price.D206()
        var_2 = divide(f206_2, d206_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A207():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A207
    value = 37012
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B207():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B207
    value = 0.963728191669
    formula = "=D207*$B$3"
    @eval_fn
    def B207():
        d207_1 = OLD_Input_EIA_Jet_Fuel_Price.D207()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d207_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C207():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C207
    value = 37026
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D207():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D207
    value = 0.821

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E207():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E207
    value = None
    formula = '''=IF(F207>0,F207/D207,"")'''
    @eval_fn
    def E207():
        f207_1 = OLD_Input_EIA_Jet_Fuel_Price.F207()
        var_1 = greaterthan(f207_1, 0)
        f207_2 = OLD_Input_EIA_Jet_Fuel_Price.F207()
        d207_1 = OLD_Input_EIA_Jet_Fuel_Price.D207()
        var_2 = divide(f207_2, d207_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A208():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A208
    value = 37043
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B208():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B208
    value = 0.900340466516
    formula = "=D208*$B$3"
    @eval_fn
    def B208():
        d208_1 = OLD_Input_EIA_Jet_Fuel_Price.D208()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d208_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C208():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C208
    value = 37057
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D208():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D208
    value = 0.767

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E208():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E208
    value = None
    formula = '''=IF(F208>0,F208/D208,"")'''
    @eval_fn
    def E208():
        f208_1 = OLD_Input_EIA_Jet_Fuel_Price.F208()
        var_1 = greaterthan(f208_1, 0)
        f208_2 = OLD_Input_EIA_Jet_Fuel_Price.F208()
        d208_1 = OLD_Input_EIA_Jet_Fuel_Price.D208()
        var_2 = divide(f208_2, d208_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A209():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A209
    value = 37073
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B209():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B209
    value = 0.83460504784
    formula = "=D209*$B$3"
    @eval_fn
    def B209():
        d209_1 = OLD_Input_EIA_Jet_Fuel_Price.D209()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d209_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C209():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C209
    value = 37087
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D209():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D209
    value = 0.711

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E209():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E209
    value = None
    formula = '''=IF(F209>0,F209/D209,"")'''
    @eval_fn
    def E209():
        f209_1 = OLD_Input_EIA_Jet_Fuel_Price.F209()
        var_1 = greaterthan(f209_1, 0)
        f209_2 = OLD_Input_EIA_Jet_Fuel_Price.F209()
        d209_1 = OLD_Input_EIA_Jet_Fuel_Price.D209()
        var_2 = divide(f209_2, d209_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A210():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A210
    value = 37104
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B210():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B210
    value = 0.89681892623
    formula = "=D210*$B$3"
    @eval_fn
    def B210():
        d210_1 = OLD_Input_EIA_Jet_Fuel_Price.D210()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d210_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C210():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C210
    value = 37118
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D210():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D210
    value = 0.764

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E210():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E210
    value = None
    formula = '''=IF(F210>0,F210/D210,"")'''
    @eval_fn
    def E210():
        f210_1 = OLD_Input_EIA_Jet_Fuel_Price.F210()
        var_1 = greaterthan(f210_1, 0)
        f210_2 = OLD_Input_EIA_Jet_Fuel_Price.F210()
        d210_1 = OLD_Input_EIA_Jet_Fuel_Price.D210()
        var_2 = divide(f210_2, d210_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A211():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A211
    value = 37135
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B211():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B211
    value = 0.866298910416
    formula = "=D211*$B$3"
    @eval_fn
    def B211():
        d211_1 = OLD_Input_EIA_Jet_Fuel_Price.D211()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d211_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C211():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C211
    value = 37149
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D211():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D211
    value = 0.738

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E211():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E211
    value = None
    formula = '''=IF(F211>0,F211/D211,"")'''
    @eval_fn
    def E211():
        f211_1 = OLD_Input_EIA_Jet_Fuel_Price.F211()
        var_1 = greaterthan(f211_1, 0)
        f211_2 = OLD_Input_EIA_Jet_Fuel_Price.F211()
        d211_1 = OLD_Input_EIA_Jet_Fuel_Price.D211()
        var_2 = divide(f211_2, d211_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A212():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A212
    value = 37165
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B212():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B212
    value = 0.730132686015
    formula = "=D212*$B$3"
    @eval_fn
    def B212():
        d212_1 = OLD_Input_EIA_Jet_Fuel_Price.D212()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d212_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C212():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C212
    value = 37179
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D212():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D212
    value = 0.622

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E212():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E212
    value = None
    formula = '''=IF(F212>0,F212/D212,"")'''
    @eval_fn
    def E212():
        f212_1 = OLD_Input_EIA_Jet_Fuel_Price.F212()
        var_1 = greaterthan(f212_1, 0)
        f212_2 = OLD_Input_EIA_Jet_Fuel_Price.F212()
        d212_1 = OLD_Input_EIA_Jet_Fuel_Price.D212()
        var_2 = divide(f212_2, d212_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A213():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A213
    value = 37196
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B213():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B213
    value = 0.63739879181
    formula = "=D213*$B$3"
    @eval_fn
    def B213():
        d213_1 = OLD_Input_EIA_Jet_Fuel_Price.D213()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d213_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C213():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C213
    value = 37210
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D213():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D213
    value = 0.543

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E213():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E213
    value = None
    formula = '''=IF(F213>0,F213/D213,"")'''
    @eval_fn
    def E213():
        f213_1 = OLD_Input_EIA_Jet_Fuel_Price.F213()
        var_1 = greaterthan(f213_1, 0)
        f213_2 = OLD_Input_EIA_Jet_Fuel_Price.F213()
        d213_1 = OLD_Input_EIA_Jet_Fuel_Price.D213()
        var_2 = divide(f213_2, d213_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A214():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A214
    value = 37226
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B214():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B214
    value = 0.604531082472
    formula = "=D214*$B$3"
    @eval_fn
    def B214():
        d214_1 = OLD_Input_EIA_Jet_Fuel_Price.D214()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d214_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C214():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C214
    value = 37240
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D214():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D214
    value = 0.515

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E214():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E214
    value = None
    formula = '''=IF(F214>0,F214/D214,"")'''
    @eval_fn
    def E214():
        f214_1 = OLD_Input_EIA_Jet_Fuel_Price.F214()
        var_1 = greaterthan(f214_1, 0)
        f214_2 = OLD_Input_EIA_Jet_Fuel_Price.F214()
        d214_1 = OLD_Input_EIA_Jet_Fuel_Price.D214()
        var_2 = divide(f214_2, d214_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A215():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A215
    value = 37257
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B215():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B215
    value = 0.625660324189
    formula = "=D215*$B$3"
    @eval_fn
    def B215():
        d215_1 = OLD_Input_EIA_Jet_Fuel_Price.D215()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d215_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C215():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C215
    value = 37271
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D215():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D215
    value = 0.533

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E215():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E215
    value = None
    formula = '''=IF(F215>0,F215/D215,"")'''
    @eval_fn
    def E215():
        f215_1 = OLD_Input_EIA_Jet_Fuel_Price.F215()
        var_1 = greaterthan(f215_1, 0)
        f215_2 = OLD_Input_EIA_Jet_Fuel_Price.F215()
        d215_1 = OLD_Input_EIA_Jet_Fuel_Price.D215()
        var_2 = divide(f215_2, d215_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A216():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A216
    value = 37288
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B216():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B216
    value = 0.646789565907
    formula = "=D216*$B$3"
    @eval_fn
    def B216():
        d216_1 = OLD_Input_EIA_Jet_Fuel_Price.D216()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d216_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C216():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C216
    value = 37302
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D216():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D216
    value = 0.551

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E216():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E216
    value = None
    formula = '''=IF(F216>0,F216/D216,"")'''
    @eval_fn
    def E216():
        f216_1 = OLD_Input_EIA_Jet_Fuel_Price.F216()
        var_1 = greaterthan(f216_1, 0)
        f216_2 = OLD_Input_EIA_Jet_Fuel_Price.F216()
        d216_1 = OLD_Input_EIA_Jet_Fuel_Price.D216()
        var_2 = divide(f216_2, d216_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A217():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A217
    value = 37316
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B217():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B217
    value = 0.739523460111
    formula = "=D217*$B$3"
    @eval_fn
    def B217():
        d217_1 = OLD_Input_EIA_Jet_Fuel_Price.D217()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d217_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C217():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C217
    value = 37330
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D217():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D217
    value = 0.63

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E217():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E217
    value = None
    formula = '''=IF(F217>0,F217/D217,"")'''
    @eval_fn
    def E217():
        f217_1 = OLD_Input_EIA_Jet_Fuel_Price.F217()
        var_1 = greaterthan(f217_1, 0)
        f217_2 = OLD_Input_EIA_Jet_Fuel_Price.F217()
        d217_1 = OLD_Input_EIA_Jet_Fuel_Price.D217()
        var_2 = divide(f217_2, d217_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A218():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A218
    value = 37347
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B218():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B218
    value = 0.785303483832
    formula = "=D218*$B$3"
    @eval_fn
    def B218():
        d218_1 = OLD_Input_EIA_Jet_Fuel_Price.D218()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d218_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C218():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C218
    value = 37361
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D218():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D218
    value = 0.669

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E218():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E218
    value = None
    formula = '''=IF(F218>0,F218/D218,"")'''
    @eval_fn
    def E218():
        f218_1 = OLD_Input_EIA_Jet_Fuel_Price.F218()
        var_1 = greaterthan(f218_1, 0)
        f218_2 = OLD_Input_EIA_Jet_Fuel_Price.F218()
        d218_1 = OLD_Input_EIA_Jet_Fuel_Price.D218()
        var_2 = divide(f218_2, d218_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A219():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A219
    value = 37377
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B219():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B219
    value = 0.781781943546
    formula = "=D219*$B$3"
    @eval_fn
    def B219():
        d219_1 = OLD_Input_EIA_Jet_Fuel_Price.D219()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d219_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C219():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C219
    value = 37391
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D219():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D219
    value = 0.666

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E219():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E219
    value = None
    formula = '''=IF(F219>0,F219/D219,"")'''
    @eval_fn
    def E219():
        f219_1 = OLD_Input_EIA_Jet_Fuel_Price.F219()
        var_1 = greaterthan(f219_1, 0)
        f219_2 = OLD_Input_EIA_Jet_Fuel_Price.F219()
        d219_1 = OLD_Input_EIA_Jet_Fuel_Price.D219()
        var_2 = divide(f219_2, d219_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A220():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A220
    value = 37408
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B220():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B220
    value = 0.766521935639
    formula = "=D220*$B$3"
    @eval_fn
    def B220():
        d220_1 = OLD_Input_EIA_Jet_Fuel_Price.D220()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d220_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C220():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C220
    value = 37422
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D220():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D220
    value = 0.653

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E220():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E220
    value = None
    formula = '''=IF(F220>0,F220/D220,"")'''
    @eval_fn
    def E220():
        f220_1 = OLD_Input_EIA_Jet_Fuel_Price.F220()
        var_1 = greaterthan(f220_1, 0)
        f220_2 = OLD_Input_EIA_Jet_Fuel_Price.F220()
        d220_1 = OLD_Input_EIA_Jet_Fuel_Price.D220()
        var_2 = divide(f220_2, d220_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A221():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A221
    value = 37438
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B221():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B221
    value = 0.811128112598
    formula = "=D221*$B$3"
    @eval_fn
    def B221():
        d221_1 = OLD_Input_EIA_Jet_Fuel_Price.D221()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d221_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C221():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C221
    value = 37452
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D221():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D221
    value = 0.691

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E221():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E221
    value = None
    formula = '''=IF(F221>0,F221/D221,"")'''
    @eval_fn
    def E221():
        f221_1 = OLD_Input_EIA_Jet_Fuel_Price.F221()
        var_1 = greaterthan(f221_1, 0)
        f221_2 = OLD_Input_EIA_Jet_Fuel_Price.F221()
        d221_1 = OLD_Input_EIA_Jet_Fuel_Price.D221()
        var_2 = divide(f221_2, d221_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A222():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A222
    value = 37469
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B222():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B222
    value = 0.847517362223
    formula = "=D222*$B$3"
    @eval_fn
    def B222():
        d222_1 = OLD_Input_EIA_Jet_Fuel_Price.D222()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d222_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C222():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C222
    value = 37483
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D222():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D222
    value = 0.722

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E222():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E222
    value = None
    formula = '''=IF(F222>0,F222/D222,"")'''
    @eval_fn
    def E222():
        f222_1 = OLD_Input_EIA_Jet_Fuel_Price.F222()
        var_1 = greaterthan(f222_1, 0)
        f222_2 = OLD_Input_EIA_Jet_Fuel_Price.F222()
        d222_1 = OLD_Input_EIA_Jet_Fuel_Price.D222()
        var_2 = divide(f222_2, d222_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A223():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A223
    value = 37500
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B223():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B223
    value = 0.939077409665
    formula = "=D223*$B$3"
    @eval_fn
    def B223():
        d223_1 = OLD_Input_EIA_Jet_Fuel_Price.D223()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d223_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C223():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C223
    value = 37514
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D223():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D223
    value = 0.8

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E223():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E223
    value = None
    formula = '''=IF(F223>0,F223/D223,"")'''
    @eval_fn
    def E223():
        f223_1 = OLD_Input_EIA_Jet_Fuel_Price.F223()
        var_1 = greaterthan(f223_1, 0)
        f223_2 = OLD_Input_EIA_Jet_Fuel_Price.F223()
        d223_1 = OLD_Input_EIA_Jet_Fuel_Price.D223()
        var_2 = divide(f223_2, d223_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A224():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A224
    value = 37530
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B224():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B224
    value = 0.927338942044
    formula = "=D224*$B$3"
    @eval_fn
    def B224():
        d224_1 = OLD_Input_EIA_Jet_Fuel_Price.D224()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d224_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C224():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C224
    value = 37544
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D224():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D224
    value = 0.79

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E224():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E224
    value = None
    formula = '''=IF(F224>0,F224/D224,"")'''
    @eval_fn
    def E224():
        f224_1 = OLD_Input_EIA_Jet_Fuel_Price.F224()
        var_1 = greaterthan(f224_1, 0)
        f224_2 = OLD_Input_EIA_Jet_Fuel_Price.F224()
        d224_1 = OLD_Input_EIA_Jet_Fuel_Price.D224()
        var_2 = divide(f224_2, d224_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A225():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A225
    value = 37561
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B225():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B225
    value = 0.831083507554
    formula = "=D225*$B$3"
    @eval_fn
    def B225():
        d225_1 = OLD_Input_EIA_Jet_Fuel_Price.D225()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d225_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C225():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C225
    value = 37575
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D225():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D225
    value = 0.708

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E225():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E225
    value = None
    formula = '''=IF(F225>0,F225/D225,"")'''
    @eval_fn
    def E225():
        f225_1 = OLD_Input_EIA_Jet_Fuel_Price.F225()
        var_1 = greaterthan(f225_1, 0)
        f225_2 = OLD_Input_EIA_Jet_Fuel_Price.F225()
        d225_1 = OLD_Input_EIA_Jet_Fuel_Price.D225()
        var_2 = divide(f225_2, d225_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A226():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A226
    value = 37591
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B226():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B226
    value = 0.951989724048
    formula = "=D226*$B$3"
    @eval_fn
    def B226():
        d226_1 = OLD_Input_EIA_Jet_Fuel_Price.D226()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d226_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C226():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C226
    value = 37605
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D226():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D226
    value = 0.811

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E226():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E226
    value = None
    formula = '''=IF(F226>0,F226/D226,"")'''
    @eval_fn
    def E226():
        f226_1 = OLD_Input_EIA_Jet_Fuel_Price.F226()
        var_1 = greaterthan(f226_1, 0)
        f226_2 = OLD_Input_EIA_Jet_Fuel_Price.F226()
        d226_1 = OLD_Input_EIA_Jet_Fuel_Price.D226()
        var_2 = divide(f226_2, d226_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A227():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A227
    value = 37622
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B227():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B227
    value = 1.04120207797
    formula = "=D227*$B$3"
    @eval_fn
    def B227():
        d227_1 = OLD_Input_EIA_Jet_Fuel_Price.D227()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d227_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C227():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C227
    value = 37636
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D227():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D227
    value = 0.887

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E227():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E227
    value = None
    formula = '''=IF(F227>0,F227/D227,"")'''
    @eval_fn
    def E227():
        f227_1 = OLD_Input_EIA_Jet_Fuel_Price.F227()
        var_1 = greaterthan(f227_1, 0)
        f227_2 = OLD_Input_EIA_Jet_Fuel_Price.F227()
        d227_1 = OLD_Input_EIA_Jet_Fuel_Price.D227()
        var_2 = divide(f227_2, d227_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A228():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A228
    value = 37653
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B228():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B228
    value = 1.238408334
    formula = "=D228*$B$3"
    @eval_fn
    def B228():
        d228_1 = OLD_Input_EIA_Jet_Fuel_Price.D228()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d228_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C228():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C228
    value = 37667
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D228():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D228
    value = 1.055

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E228():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E228
    value = None
    formula = '''=IF(F228>0,F228/D228,"")'''
    @eval_fn
    def E228():
        f228_1 = OLD_Input_EIA_Jet_Fuel_Price.F228()
        var_1 = greaterthan(f228_1, 0)
        f228_2 = OLD_Input_EIA_Jet_Fuel_Price.F228()
        d228_1 = OLD_Input_EIA_Jet_Fuel_Price.D228()
        var_2 = divide(f228_2, d228_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A229():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A229
    value = 37681
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B229():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B229
    value = 1.04824515854
    formula = "=D229*$B$3"
    @eval_fn
    def B229():
        d229_1 = OLD_Input_EIA_Jet_Fuel_Price.D229()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d229_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C229():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C229
    value = 37695
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D229():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D229
    value = 0.893

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E229():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E229
    value = None
    formula = '''=IF(F229>0,F229/D229,"")'''
    @eval_fn
    def E229():
        f229_1 = OLD_Input_EIA_Jet_Fuel_Price.F229()
        var_1 = greaterthan(f229_1, 0)
        f229_2 = OLD_Input_EIA_Jet_Fuel_Price.F229()
        d229_1 = OLD_Input_EIA_Jet_Fuel_Price.D229()
        var_2 = divide(f229_2, d229_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A230():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A230
    value = 37712
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B230():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B230
    value = 0.872168144227
    formula = "=D230*$B$3"
    @eval_fn
    def B230():
        d230_1 = OLD_Input_EIA_Jet_Fuel_Price.D230()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d230_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C230():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C230
    value = 37726
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D230():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D230
    value = 0.743

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E230():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E230
    value = None
    formula = '''=IF(F230>0,F230/D230,"")'''
    @eval_fn
    def E230():
        f230_1 = OLD_Input_EIA_Jet_Fuel_Price.F230()
        var_1 = greaterthan(f230_1, 0)
        f230_2 = OLD_Input_EIA_Jet_Fuel_Price.F230()
        d230_1 = OLD_Input_EIA_Jet_Fuel_Price.D230()
        var_2 = divide(f230_2, d230_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A231():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A231
    value = 37742
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B231():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B231
    value = 0.838126588126
    formula = "=D231*$B$3"
    @eval_fn
    def B231():
        d231_1 = OLD_Input_EIA_Jet_Fuel_Price.D231()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d231_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C231():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C231
    value = 37756
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D231():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D231
    value = 0.714

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E231():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E231
    value = None
    formula = '''=IF(F231>0,F231/D231,"")'''
    @eval_fn
    def E231():
        f231_1 = OLD_Input_EIA_Jet_Fuel_Price.F231()
        var_1 = greaterthan(f231_1, 0)
        f231_2 = OLD_Input_EIA_Jet_Fuel_Price.F231()
        d231_1 = OLD_Input_EIA_Jet_Fuel_Price.D231()
        var_2 = divide(f231_2, d231_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A232():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A232
    value = 37773
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B232():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B232
    value = 0.878037378037
    formula = "=D232*$B$3"
    @eval_fn
    def B232():
        d232_1 = OLD_Input_EIA_Jet_Fuel_Price.D232()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d232_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C232():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C232
    value = 37787
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D232():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D232
    value = 0.748

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E232():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E232
    value = None
    formula = '''=IF(F232>0,F232/D232,"")'''
    @eval_fn
    def E232():
        f232_1 = OLD_Input_EIA_Jet_Fuel_Price.F232()
        var_1 = greaterthan(f232_1, 0)
        f232_2 = OLD_Input_EIA_Jet_Fuel_Price.F232()
        d232_1 = OLD_Input_EIA_Jet_Fuel_Price.D232()
        var_2 = divide(f232_2, d232_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A233():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A233
    value = 37803
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B233():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B233
    value = 0.915600474424
    formula = "=D233*$B$3"
    @eval_fn
    def B233():
        d233_1 = OLD_Input_EIA_Jet_Fuel_Price.D233()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d233_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C233():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C233
    value = 37817
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D233():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D233
    value = 0.78

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E233():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E233
    value = None
    formula = '''=IF(F233>0,F233/D233,"")'''
    @eval_fn
    def E233():
        f233_1 = OLD_Input_EIA_Jet_Fuel_Price.F233()
        var_1 = greaterthan(f233_1, 0)
        f233_2 = OLD_Input_EIA_Jet_Fuel_Price.F233()
        d233_1 = OLD_Input_EIA_Jet_Fuel_Price.D233()
        var_2 = divide(f233_2, d233_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A234():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A234
    value = 37834
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B234():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B234
    value = 0.966075885193
    formula = "=D234*$B$3"
    @eval_fn
    def B234():
        d234_1 = OLD_Input_EIA_Jet_Fuel_Price.D234()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d234_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C234():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C234
    value = 37848
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D234():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D234
    value = 0.823

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E234():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E234
    value = None
    formula = '''=IF(F234>0,F234/D234,"")'''
    @eval_fn
    def E234():
        f234_1 = OLD_Input_EIA_Jet_Fuel_Price.F234()
        var_1 = greaterthan(f234_1, 0)
        f234_2 = OLD_Input_EIA_Jet_Fuel_Price.F234()
        d234_1 = OLD_Input_EIA_Jet_Fuel_Price.D234()
        var_2 = divide(f234_2, d234_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A235():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A235
    value = 37865
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B235():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B235
    value = 0.866298910416
    formula = "=D235*$B$3"
    @eval_fn
    def B235():
        d235_1 = OLD_Input_EIA_Jet_Fuel_Price.D235()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d235_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C235():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C235
    value = 37879
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D235():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D235
    value = 0.738

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E235():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E235
    value = None
    formula = '''=IF(F235>0,F235/D235,"")'''
    @eval_fn
    def E235():
        f235_1 = OLD_Input_EIA_Jet_Fuel_Price.F235()
        var_1 = greaterthan(f235_1, 0)
        f235_2 = OLD_Input_EIA_Jet_Fuel_Price.F235()
        d235_1 = OLD_Input_EIA_Jet_Fuel_Price.D235()
        var_2 = divide(f235_2, d235_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A236():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A236
    value = 37895
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B236():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B236
    value = 0.962554344907
    formula = "=D236*$B$3"
    @eval_fn
    def B236():
        d236_1 = OLD_Input_EIA_Jet_Fuel_Price.D236()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d236_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C236():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C236
    value = 37909
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D236():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D236
    value = 0.82

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E236():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E236
    value = None
    formula = '''=IF(F236>0,F236/D236,"")'''
    @eval_fn
    def E236():
        f236_1 = OLD_Input_EIA_Jet_Fuel_Price.F236()
        var_1 = greaterthan(f236_1, 0)
        f236_2 = OLD_Input_EIA_Jet_Fuel_Price.F236()
        d236_1 = OLD_Input_EIA_Jet_Fuel_Price.D236()
        var_2 = divide(f236_2, d236_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A237():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A237
    value = 37926
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B237():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B237
    value = 0.97546665929
    formula = "=D237*$B$3"
    @eval_fn
    def B237():
        d237_1 = OLD_Input_EIA_Jet_Fuel_Price.D237()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d237_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C237():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C237
    value = 37940
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D237():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D237
    value = 0.831

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E237():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E237
    value = None
    formula = '''=IF(F237>0,F237/D237,"")'''
    @eval_fn
    def E237():
        f237_1 = OLD_Input_EIA_Jet_Fuel_Price.F237()
        var_1 = greaterthan(f237_1, 0)
        f237_2 = OLD_Input_EIA_Jet_Fuel_Price.F237()
        d237_1 = OLD_Input_EIA_Jet_Fuel_Price.D237()
        var_2 = divide(f237_2, d237_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A238():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A238
    value = 37956
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B238():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B238
    value = 1.02828976358
    formula = "=D238*$B$3"
    @eval_fn
    def B238():
        d238_1 = OLD_Input_EIA_Jet_Fuel_Price.D238()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d238_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C238():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C238
    value = 37970
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D238():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D238
    value = 0.876

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E238():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E238
    value = None
    formula = '''=IF(F238>0,F238/D238,"")'''
    @eval_fn
    def E238():
        f238_1 = OLD_Input_EIA_Jet_Fuel_Price.F238()
        var_1 = greaterthan(f238_1, 0)
        f238_2 = OLD_Input_EIA_Jet_Fuel_Price.F238()
        d238_1 = OLD_Input_EIA_Jet_Fuel_Price.D238()
        var_2 = divide(f238_2, d238_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A239():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A239
    value = 37987
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B239():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B239
    value = 1.17149906856
    formula = "=D239*$B$3"
    @eval_fn
    def B239():
        d239_1 = OLD_Input_EIA_Jet_Fuel_Price.D239()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d239_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C239():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C239
    value = 38001
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D239():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D239
    value = 0.998

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E239():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E239
    value = None
    formula = '''=IF(F239>0,F239/D239,"")'''
    @eval_fn
    def E239():
        f239_1 = OLD_Input_EIA_Jet_Fuel_Price.F239()
        var_1 = greaterthan(f239_1, 0)
        f239_2 = OLD_Input_EIA_Jet_Fuel_Price.F239()
        d239_1 = OLD_Input_EIA_Jet_Fuel_Price.D239()
        var_2 = divide(f239_2, d239_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A240():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A240
    value = 38018
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B240():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B240
    value = 1.09519902902
    formula = "=D240*$B$3"
    @eval_fn
    def B240():
        d240_1 = OLD_Input_EIA_Jet_Fuel_Price.D240()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d240_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C240():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C240
    value = 38032
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D240():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D240
    value = 0.933

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E240():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E240
    value = None
    formula = '''=IF(F240>0,F240/D240,"")'''
    @eval_fn
    def E240():
        f240_1 = OLD_Input_EIA_Jet_Fuel_Price.F240()
        var_1 = greaterthan(f240_1, 0)
        f240_2 = OLD_Input_EIA_Jet_Fuel_Price.F240()
        d240_1 = OLD_Input_EIA_Jet_Fuel_Price.D240()
        var_2 = divide(f240_2, d240_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A241():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A241
    value = 38047
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B241():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B241
    value = 1.11163288369
    formula = "=D241*$B$3"
    @eval_fn
    def B241():
        d241_1 = OLD_Input_EIA_Jet_Fuel_Price.D241()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d241_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C241():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C241
    value = 38061
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D241():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D241
    value = 0.947

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E241():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E241
    value = None
    formula = '''=IF(F241>0,F241/D241,"")'''
    @eval_fn
    def E241():
        f241_1 = OLD_Input_EIA_Jet_Fuel_Price.F241()
        var_1 = greaterthan(f241_1, 0)
        f241_2 = OLD_Input_EIA_Jet_Fuel_Price.F241()
        d241_1 = OLD_Input_EIA_Jet_Fuel_Price.D241()
        var_2 = divide(f241_2, d241_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A242():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A242
    value = 38078
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B242():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B242
    value = 1.14215289951
    formula = "=D242*$B$3"
    @eval_fn
    def B242():
        d242_1 = OLD_Input_EIA_Jet_Fuel_Price.D242()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d242_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C242():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C242
    value = 38092
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D242():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D242
    value = 0.973

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E242():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E242
    value = None
    formula = '''=IF(F242>0,F242/D242,"")'''
    @eval_fn
    def E242():
        f242_1 = OLD_Input_EIA_Jet_Fuel_Price.F242()
        var_1 = greaterthan(f242_1, 0)
        f242_2 = OLD_Input_EIA_Jet_Fuel_Price.F242()
        d242_1 = OLD_Input_EIA_Jet_Fuel_Price.D242()
        var_2 = divide(f242_2, d242_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A243():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A243
    value = 38108
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B243():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B243
    value = 1.28184066419
    formula = "=D243*$B$3"
    @eval_fn
    def B243():
        d243_1 = OLD_Input_EIA_Jet_Fuel_Price.D243()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d243_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C243():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C243
    value = 38122
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D243():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D243
    value = 1.092

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E243():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E243
    value = None
    formula = '''=IF(F243>0,F243/D243,"")'''
    @eval_fn
    def E243():
        f243_1 = OLD_Input_EIA_Jet_Fuel_Price.F243()
        var_1 = greaterthan(f243_1, 0)
        f243_2 = OLD_Input_EIA_Jet_Fuel_Price.F243()
        d243_1 = OLD_Input_EIA_Jet_Fuel_Price.D243()
        var_2 = divide(f243_2, d243_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A244():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A244
    value = 38139
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B244():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B244
    value = 1.21140985847
    formula = "=D244*$B$3"
    @eval_fn
    def B244():
        d244_1 = OLD_Input_EIA_Jet_Fuel_Price.D244()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d244_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C244():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C244
    value = 38153
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D244():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D244
    value = 1.032

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E244():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E244
    value = None
    formula = '''=IF(F244>0,F244/D244,"")'''
    @eval_fn
    def E244():
        f244_1 = OLD_Input_EIA_Jet_Fuel_Price.F244()
        var_1 = greaterthan(f244_1, 0)
        f244_2 = OLD_Input_EIA_Jet_Fuel_Price.F244()
        d244_1 = OLD_Input_EIA_Jet_Fuel_Price.D244()
        var_2 = divide(f244_2, d244_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A245():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A245
    value = 38169
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B245():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B245
    value = 1.34405454258
    formula = "=D245*$B$3"
    @eval_fn
    def B245():
        d245_1 = OLD_Input_EIA_Jet_Fuel_Price.D245()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d245_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C245():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C245
    value = 38183
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D245():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D245
    value = 1.145

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E245():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E245
    value = None
    formula = '''=IF(F245>0,F245/D245,"")'''
    @eval_fn
    def E245():
        f245_1 = OLD_Input_EIA_Jet_Fuel_Price.F245()
        var_1 = greaterthan(f245_1, 0)
        f245_2 = OLD_Input_EIA_Jet_Fuel_Price.F245()
        d245_1 = OLD_Input_EIA_Jet_Fuel_Price.D245()
        var_2 = divide(f245_2, d245_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A246():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A246
    value = 38200
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B246():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B246
    value = 1.44030997707
    formula = "=D246*$B$3"
    @eval_fn
    def B246():
        d246_1 = OLD_Input_EIA_Jet_Fuel_Price.D246()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d246_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C246():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C246
    value = 38214
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D246():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D246
    value = 1.227

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E246():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E246
    value = None
    formula = '''=IF(F246>0,F246/D246,"")'''
    @eval_fn
    def E246():
        f246_1 = OLD_Input_EIA_Jet_Fuel_Price.F246()
        var_1 = greaterthan(f246_1, 0)
        f246_2 = OLD_Input_EIA_Jet_Fuel_Price.F246()
        d246_1 = OLD_Input_EIA_Jet_Fuel_Price.D246()
        var_2 = divide(f246_2, d246_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A247():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A247
    value = 38231
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B247():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B247
    value = 1.59877928995
    formula = "=D247*$B$3"
    @eval_fn
    def B247():
        d247_1 = OLD_Input_EIA_Jet_Fuel_Price.D247()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d247_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C247():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C247
    value = 38245
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D247():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D247
    value = 1.362

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E247():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E247
    value = None
    formula = '''=IF(F247>0,F247/D247,"")'''
    @eval_fn
    def E247():
        f247_1 = OLD_Input_EIA_Jet_Fuel_Price.F247()
        var_1 = greaterthan(f247_1, 0)
        f247_2 = OLD_Input_EIA_Jet_Fuel_Price.F247()
        d247_1 = OLD_Input_EIA_Jet_Fuel_Price.D247()
        var_2 = divide(f247_2, d247_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A248():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A248
    value = 38261
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B248():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B248
    value = 1.78424707836
    formula = "=D248*$B$3"
    @eval_fn
    def B248():
        d248_1 = OLD_Input_EIA_Jet_Fuel_Price.D248()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d248_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C248():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C248
    value = 38275
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D248():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D248
    value = 1.52

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E248():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E248
    value = None
    formula = '''=IF(F248>0,F248/D248,"")'''
    @eval_fn
    def E248():
        f248_1 = OLD_Input_EIA_Jet_Fuel_Price.F248()
        var_1 = greaterthan(f248_1, 0)
        f248_2 = OLD_Input_EIA_Jet_Fuel_Price.F248()
        d248_1 = OLD_Input_EIA_Jet_Fuel_Price.D248()
        var_2 = divide(f248_2, d248_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A249():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A249
    value = 38292
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B249():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B249
    value = 1.58117158852
    formula = "=D249*$B$3"
    @eval_fn
    def B249():
        d249_1 = OLD_Input_EIA_Jet_Fuel_Price.D249()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d249_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C249():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C249
    value = 38306
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D249():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D249
    value = 1.347

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E249():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E249
    value = None
    formula = '''=IF(F249>0,F249/D249,"")'''
    @eval_fn
    def E249():
        f249_1 = OLD_Input_EIA_Jet_Fuel_Price.F249()
        var_1 = greaterthan(f249_1, 0)
        f249_2 = OLD_Input_EIA_Jet_Fuel_Price.F249()
        d249_1 = OLD_Input_EIA_Jet_Fuel_Price.D249()
        var_2 = divide(f249_2, d249_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A250():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A250
    value = 38322
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B250():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B250
    value = 1.43561459003
    formula = "=D250*$B$3"
    @eval_fn
    def B250():
        d250_1 = OLD_Input_EIA_Jet_Fuel_Price.D250()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d250_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C250():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C250
    value = 38336
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D250():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D250
    value = 1.223

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E250():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E250
    value = None
    formula = '''=IF(F250>0,F250/D250,"")'''
    @eval_fn
    def E250():
        f250_1 = OLD_Input_EIA_Jet_Fuel_Price.F250()
        var_1 = greaterthan(f250_1, 0)
        f250_2 = OLD_Input_EIA_Jet_Fuel_Price.F250()
        d250_1 = OLD_Input_EIA_Jet_Fuel_Price.D250()
        var_2 = divide(f250_2, d250_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A251():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A251
    value = 38353
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B251():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B251
    value = 1.56591158062
    formula = "=D251*$B$3"
    @eval_fn
    def B251():
        d251_1 = OLD_Input_EIA_Jet_Fuel_Price.D251()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d251_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C251():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C251
    value = 38367
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D251():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D251
    value = 1.334

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E251():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E251
    value = None
    formula = '''=IF(F251>0,F251/D251,"")'''
    @eval_fn
    def E251():
        f251_1 = OLD_Input_EIA_Jet_Fuel_Price.F251()
        var_1 = greaterthan(f251_1, 0)
        f251_2 = OLD_Input_EIA_Jet_Fuel_Price.F251()
        d251_1 = OLD_Input_EIA_Jet_Fuel_Price.D251()
        var_2 = divide(f251_2, d251_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A252():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A252
    value = 38384
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B252():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B252
    value = 1.56591158062
    formula = "=D252*$B$3"
    @eval_fn
    def B252():
        d252_1 = OLD_Input_EIA_Jet_Fuel_Price.D252()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d252_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C252():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C252
    value = 38398
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D252():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D252
    value = 1.334

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E252():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E252
    value = None
    formula = '''=IF(F252>0,F252/D252,"")'''
    @eval_fn
    def E252():
        f252_1 = OLD_Input_EIA_Jet_Fuel_Price.F252()
        var_1 = greaterthan(f252_1, 0)
        f252_2 = OLD_Input_EIA_Jet_Fuel_Price.F252()
        d252_1 = OLD_Input_EIA_Jet_Fuel_Price.D252()
        var_2 = divide(f252_2, d252_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A253():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A253
    value = 38412
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B253():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B253
    value = 1.83354864237
    formula = "=D253*$B$3"
    @eval_fn
    def B253():
        d253_1 = OLD_Input_EIA_Jet_Fuel_Price.D253()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d253_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C253():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C253
    value = 38426
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D253():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D253
    value = 1.562

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E253():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E253
    value = None
    formula = '''=IF(F253>0,F253/D253,"")'''
    @eval_fn
    def E253():
        f253_1 = OLD_Input_EIA_Jet_Fuel_Price.F253()
        var_1 = greaterthan(f253_1, 0)
        f253_2 = OLD_Input_EIA_Jet_Fuel_Price.F253()
        d253_1 = OLD_Input_EIA_Jet_Fuel_Price.D253()
        var_2 = divide(f253_2, d253_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A254():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A254
    value = 38443
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B254():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B254
    value = 1.84646095675
    formula = "=D254*$B$3"
    @eval_fn
    def B254():
        d254_1 = OLD_Input_EIA_Jet_Fuel_Price.D254()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d254_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C254():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C254
    value = 38457
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D254():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D254
    value = 1.573

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E254():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E254
    value = None
    formula = '''=IF(F254>0,F254/D254,"")'''
    @eval_fn
    def E254():
        f254_1 = OLD_Input_EIA_Jet_Fuel_Price.F254()
        var_1 = greaterthan(f254_1, 0)
        f254_2 = OLD_Input_EIA_Jet_Fuel_Price.F254()
        d254_1 = OLD_Input_EIA_Jet_Fuel_Price.D254()
        var_2 = divide(f254_2, d254_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A255():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A255
    value = 38473
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B255():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B255
    value = 1.72672858702
    formula = "=D255*$B$3"
    @eval_fn
    def B255():
        d255_1 = OLD_Input_EIA_Jet_Fuel_Price.D255()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d255_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C255():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C255
    value = 38487
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D255():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D255
    value = 1.471

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E255():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E255
    value = None
    formula = '''=IF(F255>0,F255/D255,"")'''
    @eval_fn
    def E255():
        f255_1 = OLD_Input_EIA_Jet_Fuel_Price.F255()
        var_1 = greaterthan(f255_1, 0)
        f255_2 = OLD_Input_EIA_Jet_Fuel_Price.F255()
        d255_1 = OLD_Input_EIA_Jet_Fuel_Price.D255()
        var_2 = divide(f255_2, d255_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A256():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A256
    value = 38504
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B256():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B256
    value = 1.94154254448
    formula = "=D256*$B$3"
    @eval_fn
    def B256():
        d256_1 = OLD_Input_EIA_Jet_Fuel_Price.D256()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d256_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C256():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C256
    value = 38518
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D256():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D256
    value = 1.654

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E256():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E256
    value = None
    formula = '''=IF(F256>0,F256/D256,"")'''
    @eval_fn
    def E256():
        f256_1 = OLD_Input_EIA_Jet_Fuel_Price.F256()
        var_1 = greaterthan(f256_1, 0)
        f256_2 = OLD_Input_EIA_Jet_Fuel_Price.F256()
        d256_1 = OLD_Input_EIA_Jet_Fuel_Price.D256()
        var_2 = divide(f256_2, d256_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A257():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A257
    value = 38534
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B257():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B257
    value = 1.95445485887
    formula = "=D257*$B$3"
    @eval_fn
    def B257():
        d257_1 = OLD_Input_EIA_Jet_Fuel_Price.D257()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d257_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C257():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C257
    value = 38548
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D257():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D257
    value = 1.665

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E257():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E257
    value = None
    formula = '''=IF(F257>0,F257/D257,"")'''
    @eval_fn
    def E257():
        f257_1 = OLD_Input_EIA_Jet_Fuel_Price.F257()
        var_1 = greaterthan(f257_1, 0)
        f257_2 = OLD_Input_EIA_Jet_Fuel_Price.F257()
        d257_1 = OLD_Input_EIA_Jet_Fuel_Price.D257()
        var_2 = divide(f257_2, d257_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A258():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A258
    value = 38565
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B258():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B258
    value = 2.19978883214
    formula = "=D258*$B$3"
    @eval_fn
    def B258():
        d258_1 = OLD_Input_EIA_Jet_Fuel_Price.D258()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d258_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C258():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C258
    value = 38579
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D258():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D258
    value = 1.874

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E258():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E258
    value = None
    formula = '''=IF(F258>0,F258/D258,"")'''
    @eval_fn
    def E258():
        f258_1 = OLD_Input_EIA_Jet_Fuel_Price.F258()
        var_1 = greaterthan(f258_1, 0)
        f258_2 = OLD_Input_EIA_Jet_Fuel_Price.F258()
        d258_1 = OLD_Input_EIA_Jet_Fuel_Price.D258()
        var_2 = divide(f258_2, d258_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A259():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A259
    value = 38596
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B259():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B259
    value = 2.62002597297
    formula = "=D259*$B$3"
    @eval_fn
    def B259():
        d259_1 = OLD_Input_EIA_Jet_Fuel_Price.D259()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d259_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C259():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C259
    value = 38610
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D259():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D259
    value = 2.232

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E259():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E259
    value = None
    formula = '''=IF(F259>0,F259/D259,"")'''
    @eval_fn
    def E259():
        f259_1 = OLD_Input_EIA_Jet_Fuel_Price.F259()
        var_1 = greaterthan(f259_1, 0)
        f259_2 = OLD_Input_EIA_Jet_Fuel_Price.F259()
        d259_1 = OLD_Input_EIA_Jet_Fuel_Price.D259()
        var_2 = divide(f259_2, d259_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A260():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A260
    value = 38626
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B260():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B260
    value = 2.81488453547
    formula = "=D260*$B$3"
    @eval_fn
    def B260():
        d260_1 = OLD_Input_EIA_Jet_Fuel_Price.D260()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d260_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C260():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C260
    value = 38640
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D260():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D260
    value = 2.398

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E260():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E260
    value = None
    formula = '''=IF(F260>0,F260/D260,"")'''
    @eval_fn
    def E260():
        f260_1 = OLD_Input_EIA_Jet_Fuel_Price.F260()
        var_1 = greaterthan(f260_1, 0)
        f260_2 = OLD_Input_EIA_Jet_Fuel_Price.F260()
        d260_1 = OLD_Input_EIA_Jet_Fuel_Price.D260()
        var_2 = divide(f260_2, d260_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A261():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A261
    value = 38657
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B261():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B261
    value = 1.99319180201
    formula = "=D261*$B$3"
    @eval_fn
    def B261():
        d261_1 = OLD_Input_EIA_Jet_Fuel_Price.D261()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d261_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C261():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C261
    value = 38671
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D261():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D261
    value = 1.698

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E261():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E261
    value = None
    formula = '''=IF(F261>0,F261/D261,"")'''
    @eval_fn
    def E261():
        f261_1 = OLD_Input_EIA_Jet_Fuel_Price.F261()
        var_1 = greaterthan(f261_1, 0)
        f261_2 = OLD_Input_EIA_Jet_Fuel_Price.F261()
        d261_1 = OLD_Input_EIA_Jet_Fuel_Price.D261()
        var_2 = divide(f261_2, d261_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A262():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A262
    value = 38687
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B262():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B262
    value = 2.02723335811
    formula = "=D262*$B$3"
    @eval_fn
    def B262():
        d262_1 = OLD_Input_EIA_Jet_Fuel_Price.D262()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d262_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C262():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C262
    value = 38701
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D262():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D262
    value = 1.727

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E262():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E262
    value = None
    formula = '''=IF(F262>0,F262/D262,"")'''
    @eval_fn
    def E262():
        f262_1 = OLD_Input_EIA_Jet_Fuel_Price.F262()
        var_1 = greaterthan(f262_1, 0)
        f262_2 = OLD_Input_EIA_Jet_Fuel_Price.F262()
        d262_1 = OLD_Input_EIA_Jet_Fuel_Price.D262()
        var_2 = divide(f262_2, d262_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A263():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A263
    value = 38718
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B263():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B263
    value = 2.13170571994
    formula = "=D263*$B$3"
    @eval_fn
    def B263():
        d263_1 = OLD_Input_EIA_Jet_Fuel_Price.D263()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d263_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C263():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C263
    value = 38732
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D263():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D263
    value = 1.816

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E263():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E263
    value = None
    formula = '''=IF(F263>0,F263/D263,"")'''
    @eval_fn
    def E263():
        f263_1 = OLD_Input_EIA_Jet_Fuel_Price.F263()
        var_1 = greaterthan(f263_1, 0)
        f263_2 = OLD_Input_EIA_Jet_Fuel_Price.F263()
        d263_1 = OLD_Input_EIA_Jet_Fuel_Price.D263()
        var_2 = divide(f263_2, d263_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A264():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A264
    value = 38749
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B264():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B264
    value = 2.05892722069
    formula = "=D264*$B$3"
    @eval_fn
    def B264():
        d264_1 = OLD_Input_EIA_Jet_Fuel_Price.D264()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d264_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C264():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C264
    value = 38763
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D264():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D264
    value = 1.754

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E264():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E264
    value = None
    formula = '''=IF(F264>0,F264/D264,"")'''
    @eval_fn
    def E264():
        f264_1 = OLD_Input_EIA_Jet_Fuel_Price.F264()
        var_1 = greaterthan(f264_1, 0)
        f264_2 = OLD_Input_EIA_Jet_Fuel_Price.F264()
        d264_1 = OLD_Input_EIA_Jet_Fuel_Price.D264()
        var_2 = divide(f264_2, d264_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A265():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A265
    value = 38777
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B265():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B265
    value = 2.2009626789
    formula = "=D265*$B$3"
    @eval_fn
    def B265():
        d265_1 = OLD_Input_EIA_Jet_Fuel_Price.D265()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d265_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C265():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C265
    value = 38791
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D265():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D265
    value = 1.875

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E265():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E265
    value = None
    formula = '''=IF(F265>0,F265/D265,"")'''
    @eval_fn
    def E265():
        f265_1 = OLD_Input_EIA_Jet_Fuel_Price.F265()
        var_1 = greaterthan(f265_1, 0)
        f265_2 = OLD_Input_EIA_Jet_Fuel_Price.F265()
        d265_1 = OLD_Input_EIA_Jet_Fuel_Price.D265()
        var_2 = divide(f265_2, d265_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A266():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A266
    value = 38808
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B266():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B266
    value = 2.43455818456
    formula = "=D266*$B$3"
    @eval_fn
    def B266():
        d266_1 = OLD_Input_EIA_Jet_Fuel_Price.D266()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d266_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C266():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C266
    value = 38822
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D266():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D266
    value = 2.074

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E266():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E266
    value = None
    formula = '''=IF(F266>0,F266/D266,"")'''
    @eval_fn
    def E266():
        f266_1 = OLD_Input_EIA_Jet_Fuel_Price.F266()
        var_1 = greaterthan(f266_1, 0)
        f266_2 = OLD_Input_EIA_Jet_Fuel_Price.F266()
        d266_1 = OLD_Input_EIA_Jet_Fuel_Price.D266()
        var_2 = divide(f266_2, d266_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A267():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A267
    value = 38838
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B267():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B267
    value = 2.42986279751
    formula = "=D267*$B$3"
    @eval_fn
    def B267():
        d267_1 = OLD_Input_EIA_Jet_Fuel_Price.D267()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d267_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C267():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C267
    value = 38852
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D267():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D267
    value = 2.07

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E267():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E267
    value = None
    formula = '''=IF(F267>0,F267/D267,"")'''
    @eval_fn
    def E267():
        f267_1 = OLD_Input_EIA_Jet_Fuel_Price.F267()
        var_1 = greaterthan(f267_1, 0)
        f267_2 = OLD_Input_EIA_Jet_Fuel_Price.F267()
        d267_1 = OLD_Input_EIA_Jet_Fuel_Price.D267()
        var_2 = divide(f267_2, d267_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A268():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A268
    value = 38869
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B268():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B268
    value = 2.44277511189
    formula = "=D268*$B$3"
    @eval_fn
    def B268():
        d268_1 = OLD_Input_EIA_Jet_Fuel_Price.D268()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d268_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C268():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C268
    value = 38883
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D268():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D268
    value = 2.081

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E268():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E268
    value = None
    formula = '''=IF(F268>0,F268/D268,"")'''
    @eval_fn
    def E268():
        f268_1 = OLD_Input_EIA_Jet_Fuel_Price.F268()
        var_1 = greaterthan(f268_1, 0)
        f268_2 = OLD_Input_EIA_Jet_Fuel_Price.F268()
        d268_1 = OLD_Input_EIA_Jet_Fuel_Price.D268()
        var_2 = divide(f268_2, d268_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A269():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A269
    value = 38899
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B269():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B269
    value = 2.52846592552
    formula = "=D269*$B$3"
    @eval_fn
    def B269():
        d269_1 = OLD_Input_EIA_Jet_Fuel_Price.D269()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d269_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C269():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C269
    value = 38913
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D269():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D269
    value = 2.154

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E269():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E269
    value = None
    formula = '''=IF(F269>0,F269/D269,"")'''
    @eval_fn
    def E269():
        f269_1 = OLD_Input_EIA_Jet_Fuel_Price.F269()
        var_1 = greaterthan(f269_1, 0)
        f269_2 = OLD_Input_EIA_Jet_Fuel_Price.F269()
        d269_1 = OLD_Input_EIA_Jet_Fuel_Price.D269()
        var_2 = divide(f269_2, d269_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A270():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A270
    value = 38930
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B270():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B270
    value = 2.50381514352
    formula = "=D270*$B$3"
    @eval_fn
    def B270():
        d270_1 = OLD_Input_EIA_Jet_Fuel_Price.D270()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d270_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C270():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C270
    value = 38944
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D270():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D270
    value = 2.133

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E270():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E270
    value = None
    formula = '''=IF(F270>0,F270/D270,"")'''
    @eval_fn
    def E270():
        f270_1 = OLD_Input_EIA_Jet_Fuel_Price.F270()
        var_1 = greaterthan(f270_1, 0)
        f270_2 = OLD_Input_EIA_Jet_Fuel_Price.F270()
        d270_1 = OLD_Input_EIA_Jet_Fuel_Price.D270()
        var_2 = divide(f270_2, d270_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A271():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A271
    value = 38961
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B271():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B271
    value = 2.12466263937
    formula = "=D271*$B$3"
    @eval_fn
    def B271():
        d271_1 = OLD_Input_EIA_Jet_Fuel_Price.D271()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d271_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C271():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C271
    value = 38975
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D271():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D271
    value = 1.81

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E271():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E271
    value = None
    formula = '''=IF(F271>0,F271/D271,"")'''
    @eval_fn
    def E271():
        f271_1 = OLD_Input_EIA_Jet_Fuel_Price.F271()
        var_1 = greaterthan(f271_1, 0)
        f271_2 = OLD_Input_EIA_Jet_Fuel_Price.F271()
        d271_1 = OLD_Input_EIA_Jet_Fuel_Price.D271()
        var_2 = divide(f271_2, d271_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A272():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A272
    value = 38991
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B272():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B272
    value = 2.04131951926
    formula = "=D272*$B$3"
    @eval_fn
    def B272():
        d272_1 = OLD_Input_EIA_Jet_Fuel_Price.D272()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d272_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C272():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C272
    value = 39005
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D272():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D272
    value = 1.739

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E272():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E272
    value = None
    formula = '''=IF(F272>0,F272/D272,"")'''
    @eval_fn
    def E272():
        f272_1 = OLD_Input_EIA_Jet_Fuel_Price.F272()
        var_1 = greaterthan(f272_1, 0)
        f272_2 = OLD_Input_EIA_Jet_Fuel_Price.F272()
        d272_1 = OLD_Input_EIA_Jet_Fuel_Price.D272()
        var_2 = divide(f272_2, d272_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A273():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A273
    value = 39022
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B273():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B273
    value = 2.03427643869
    formula = "=D273*$B$3"
    @eval_fn
    def B273():
        d273_1 = OLD_Input_EIA_Jet_Fuel_Price.D273()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d273_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C273():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C273
    value = 39036
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D273():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D273
    value = 1.733

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E273():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E273
    value = None
    formula = '''=IF(F273>0,F273/D273,"")'''
    @eval_fn
    def E273():
        f273_1 = OLD_Input_EIA_Jet_Fuel_Price.F273()
        var_1 = greaterthan(f273_1, 0)
        f273_2 = OLD_Input_EIA_Jet_Fuel_Price.F273()
        d273_1 = OLD_Input_EIA_Jet_Fuel_Price.D273()
        var_2 = divide(f273_2, d273_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A274():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A274
    value = 39052
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B274():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B274
    value = 2.12466263937
    formula = "=D274*$B$3"
    @eval_fn
    def B274():
        d274_1 = OLD_Input_EIA_Jet_Fuel_Price.D274()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d274_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C274():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C274
    value = 39066
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D274():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D274
    value = 1.81

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E274():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E274
    value = None
    formula = '''=IF(F274>0,F274/D274,"")'''
    @eval_fn
    def E274():
        f274_1 = OLD_Input_EIA_Jet_Fuel_Price.F274()
        var_1 = greaterthan(f274_1, 0)
        f274_2 = OLD_Input_EIA_Jet_Fuel_Price.F274()
        d274_1 = OLD_Input_EIA_Jet_Fuel_Price.D274()
        var_2 = divide(f274_2, d274_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A275():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A275
    value = 39083
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B275():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B275
    value = 1.94154254448
    formula = "=D275*$B$3"
    @eval_fn
    def B275():
        d275_1 = OLD_Input_EIA_Jet_Fuel_Price.D275()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d275_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C275():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C275
    value = 39097
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D275():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D275
    value = 1.654

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E275():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E275
    value = None
    formula = '''=IF(F275>0,F275/D275,"")'''
    @eval_fn
    def E275():
        f275_1 = OLD_Input_EIA_Jet_Fuel_Price.F275()
        var_1 = greaterthan(f275_1, 0)
        f275_2 = OLD_Input_EIA_Jet_Fuel_Price.F275()
        d275_1 = OLD_Input_EIA_Jet_Fuel_Price.D275()
        var_2 = divide(f275_2, d275_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A276():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A276
    value = 39114
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B276():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B276
    value = 2.04249336602
    formula = "=D276*$B$3"
    @eval_fn
    def B276():
        d276_1 = OLD_Input_EIA_Jet_Fuel_Price.D276()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d276_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C276():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C276
    value = 39128
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D276():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D276
    value = 1.74

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E276():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E276
    value = None
    formula = '''=IF(F276>0,F276/D276,"")'''
    @eval_fn
    def E276():
        f276_1 = OLD_Input_EIA_Jet_Fuel_Price.F276()
        var_1 = greaterthan(f276_1, 0)
        f276_2 = OLD_Input_EIA_Jet_Fuel_Price.F276()
        d276_1 = OLD_Input_EIA_Jet_Fuel_Price.D276()
        var_2 = divide(f276_2, d276_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A277():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A277
    value = 39142
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B277():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B277
    value = 2.1669211228
    formula = "=D277*$B$3"
    @eval_fn
    def B277():
        d277_1 = OLD_Input_EIA_Jet_Fuel_Price.D277()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d277_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C277():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C277
    value = 39156
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D277():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D277
    value = 1.846

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E277():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E277
    value = None
    formula = '''=IF(F277>0,F277/D277,"")'''
    @eval_fn
    def E277():
        f277_1 = OLD_Input_EIA_Jet_Fuel_Price.F277()
        var_1 = greaterthan(f277_1, 0)
        f277_2 = OLD_Input_EIA_Jet_Fuel_Price.F277()
        d277_1 = OLD_Input_EIA_Jet_Fuel_Price.D277()
        var_2 = divide(f277_2, d277_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A278():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A278
    value = 39173
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B278():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B278
    value = 2.3899520076
    formula = "=D278*$B$3"
    @eval_fn
    def B278():
        d278_1 = OLD_Input_EIA_Jet_Fuel_Price.D278()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d278_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C278():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C278
    value = 39187
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D278():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D278
    value = 2.036

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E278():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E278
    value = None
    formula = '''=IF(F278>0,F278/D278,"")'''
    @eval_fn
    def E278():
        f278_1 = OLD_Input_EIA_Jet_Fuel_Price.F278()
        var_1 = greaterthan(f278_1, 0)
        f278_2 = OLD_Input_EIA_Jet_Fuel_Price.F278()
        d278_1 = OLD_Input_EIA_Jet_Fuel_Price.D278()
        var_2 = divide(f278_2, d278_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A279():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A279
    value = 39203
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B279():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B279
    value = 2.39934278169
    formula = "=D279*$B$3"
    @eval_fn
    def B279():
        d279_1 = OLD_Input_EIA_Jet_Fuel_Price.D279()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d279_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C279():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C279
    value = 39217
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D279():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D279
    value = 2.044

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E279():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E279
    value = None
    formula = '''=IF(F279>0,F279/D279,"")'''
    @eval_fn
    def E279():
        f279_1 = OLD_Input_EIA_Jet_Fuel_Price.F279()
        var_1 = greaterthan(f279_1, 0)
        f279_2 = OLD_Input_EIA_Jet_Fuel_Price.F279()
        d279_1 = OLD_Input_EIA_Jet_Fuel_Price.D279()
        var_2 = divide(f279_2, d279_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A280():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A280
    value = 39234
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B280():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B280
    value = 2.46390435361
    formula = "=D280*$B$3"
    @eval_fn
    def B280():
        d280_1 = OLD_Input_EIA_Jet_Fuel_Price.D280()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d280_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C280():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C280
    value = 39248
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D280():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D280
    value = 2.099

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E280():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E280
    value = None
    formula = '''=IF(F280>0,F280/D280,"")'''
    @eval_fn
    def E280():
        f280_1 = OLD_Input_EIA_Jet_Fuel_Price.F280()
        var_1 = greaterthan(f280_1, 0)
        f280_2 = OLD_Input_EIA_Jet_Fuel_Price.F280()
        d280_1 = OLD_Input_EIA_Jet_Fuel_Price.D280()
        var_2 = divide(f280_2, d280_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A281():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A281
    value = 39264
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B281():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B281
    value = 2.50851053057
    formula = "=D281*$B$3"
    @eval_fn
    def B281():
        d281_1 = OLD_Input_EIA_Jet_Fuel_Price.D281()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d281_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C281():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C281
    value = 39278
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D281():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D281
    value = 2.137

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E281():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E281
    value = None
    formula = '''=IF(F281>0,F281/D281,"")'''
    @eval_fn
    def E281():
        f281_1 = OLD_Input_EIA_Jet_Fuel_Price.F281()
        var_1 = greaterthan(f281_1, 0)
        f281_2 = OLD_Input_EIA_Jet_Fuel_Price.F281()
        d281_1 = OLD_Input_EIA_Jet_Fuel_Price.D281()
        var_2 = divide(f281_2, d281_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A282():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A282
    value = 39295
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B282():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B282
    value = 2.45568742627
    formula = "=D282*$B$3"
    @eval_fn
    def B282():
        d282_1 = OLD_Input_EIA_Jet_Fuel_Price.D282()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d282_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C282():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C282
    value = 39309
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D282():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D282
    value = 2.092

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E282():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E282
    value = None
    formula = '''=IF(F282>0,F282/D282,"")'''
    @eval_fn
    def E282():
        f282_1 = OLD_Input_EIA_Jet_Fuel_Price.F282()
        var_1 = greaterthan(f282_1, 0)
        f282_2 = OLD_Input_EIA_Jet_Fuel_Price.F282()
        d282_1 = OLD_Input_EIA_Jet_Fuel_Price.D282()
        var_2 = divide(f282_2, d282_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A283():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A283
    value = 39326
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B283():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B283
    value = 2.65876291611
    formula = "=D283*$B$3"
    @eval_fn
    def B283():
        d283_1 = OLD_Input_EIA_Jet_Fuel_Price.D283()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d283_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C283():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C283
    value = 39340
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D283():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D283
    value = 2.265

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E283():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E283
    value = None
    formula = '''=IF(F283>0,F283/D283,"")'''
    @eval_fn
    def E283():
        f283_1 = OLD_Input_EIA_Jet_Fuel_Price.F283()
        var_1 = greaterthan(f283_1, 0)
        f283_2 = OLD_Input_EIA_Jet_Fuel_Price.F283()
        d283_1 = OLD_Input_EIA_Jet_Fuel_Price.D283()
        var_2 = divide(f283_2, d283_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A284():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A284
    value = 39356
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B284():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B284
    value = 2.78436451966
    formula = "=D284*$B$3"
    @eval_fn
    def B284():
        d284_1 = OLD_Input_EIA_Jet_Fuel_Price.D284()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d284_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C284():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C284
    value = 39370
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D284():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D284
    value = 2.372

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E284():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E284
    value = None
    formula = '''=IF(F284>0,F284/D284,"")'''
    @eval_fn
    def E284():
        f284_1 = OLD_Input_EIA_Jet_Fuel_Price.F284()
        var_1 = greaterthan(f284_1, 0)
        f284_2 = OLD_Input_EIA_Jet_Fuel_Price.F284()
        d284_1 = OLD_Input_EIA_Jet_Fuel_Price.D284()
        var_2 = divide(f284_2, d284_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A285():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A285
    value = 39387
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B285():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B285
    value = 3.13769239504
    formula = "=D285*$B$3"
    @eval_fn
    def B285():
        d285_1 = OLD_Input_EIA_Jet_Fuel_Price.D285()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d285_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C285():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C285
    value = 39401
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D285():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D285
    value = 2.673

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E285():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E285
    value = None
    formula = '''=IF(F285>0,F285/D285,"")'''
    @eval_fn
    def E285():
        f285_1 = OLD_Input_EIA_Jet_Fuel_Price.F285()
        var_1 = greaterthan(f285_1, 0)
        f285_2 = OLD_Input_EIA_Jet_Fuel_Price.F285()
        d285_1 = OLD_Input_EIA_Jet_Fuel_Price.D285()
        var_2 = divide(f285_2, d285_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A286():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A286
    value = 39417
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B286():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B286
    value = 3.05317542817
    formula = "=D286*$B$3"
    @eval_fn
    def B286():
        d286_1 = OLD_Input_EIA_Jet_Fuel_Price.D286()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d286_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C286():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C286
    value = 39431
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D286():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D286
    value = 2.601

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E286():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E286
    value = None
    formula = '''=IF(F286>0,F286/D286,"")'''
    @eval_fn
    def E286():
        f286_1 = OLD_Input_EIA_Jet_Fuel_Price.F286()
        var_1 = greaterthan(f286_1, 0)
        f286_2 = OLD_Input_EIA_Jet_Fuel_Price.F286()
        d286_1 = OLD_Input_EIA_Jet_Fuel_Price.D286()
        var_2 = divide(f286_2, d286_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A287():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A287
    value = 39448
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B287():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B287
    value = 3.05787081522
    formula = "=D287*$B$3"
    @eval_fn
    def B287():
        d287_1 = OLD_Input_EIA_Jet_Fuel_Price.D287()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d287_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C287():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C287
    value = 39462
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D287():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D287
    value = 2.605

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E287():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E287
    value = None
    formula = '''=IF(F287>0,F287/D287,"")'''
    @eval_fn
    def E287():
        f287_1 = OLD_Input_EIA_Jet_Fuel_Price.F287()
        var_1 = greaterthan(f287_1, 0)
        f287_2 = OLD_Input_EIA_Jet_Fuel_Price.F287()
        d287_1 = OLD_Input_EIA_Jet_Fuel_Price.D287()
        var_2 = divide(f287_2, d287_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A288():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A288
    value = 39479
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B288():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B288
    value = 3.20225396696
    formula = "=D288*$B$3"
    @eval_fn
    def B288():
        d288_1 = OLD_Input_EIA_Jet_Fuel_Price.D288()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d288_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C288():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C288
    value = 39493
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D288():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D288
    value = 2.728

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E288():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E288
    value = None
    formula = '''=IF(F288>0,F288/D288,"")'''
    @eval_fn
    def E288():
        f288_1 = OLD_Input_EIA_Jet_Fuel_Price.F288()
        var_1 = greaterthan(f288_1, 0)
        f288_2 = OLD_Input_EIA_Jet_Fuel_Price.F288()
        d288_1 = OLD_Input_EIA_Jet_Fuel_Price.D288()
        var_2 = divide(f288_2, d288_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A289():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A289
    value = 39508
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B289():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B289
    value = 3.66709728474
    formula = "=D289*$B$3"
    @eval_fn
    def B289():
        d289_1 = OLD_Input_EIA_Jet_Fuel_Price.D289()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d289_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C289():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C289
    value = 39522
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D289():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D289
    value = 3.124

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E289():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E289
    value = None
    formula = '''=IF(F289>0,F289/D289,"")'''
    @eval_fn
    def E289():
        f289_1 = OLD_Input_EIA_Jet_Fuel_Price.F289()
        var_1 = greaterthan(f289_1, 0)
        f289_2 = OLD_Input_EIA_Jet_Fuel_Price.F289()
        d289_1 = OLD_Input_EIA_Jet_Fuel_Price.D289()
        var_2 = divide(f289_2, d289_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A290():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A290
    value = 39539
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B290():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B290
    value = 3.9499943544
    formula = "=D290*$B$3"
    @eval_fn
    def B290():
        d290_1 = OLD_Input_EIA_Jet_Fuel_Price.D290()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d290_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C290():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C290
    value = 39553
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D290():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D290
    value = 3.365

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E290():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E290
    value = None
    formula = '''=IF(F290>0,F290/D290,"")'''
    @eval_fn
    def E290():
        f290_1 = OLD_Input_EIA_Jet_Fuel_Price.F290()
        var_1 = greaterthan(f290_1, 0)
        f290_2 = OLD_Input_EIA_Jet_Fuel_Price.F290()
        d290_1 = OLD_Input_EIA_Jet_Fuel_Price.D290()
        var_2 = divide(f290_2, d290_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A291():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A291
    value = 39569
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B291():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B291
    value = 4.38783919666
    formula = "=D291*$B$3"
    @eval_fn
    def B291():
        d291_1 = OLD_Input_EIA_Jet_Fuel_Price.D291()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d291_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C291():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C291
    value = 39583
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D291():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D291
    value = 3.738

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E291():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E291
    value = None
    formula = '''=IF(F291>0,F291/D291,"")'''
    @eval_fn
    def E291():
        f291_1 = OLD_Input_EIA_Jet_Fuel_Price.F291()
        var_1 = greaterthan(f291_1, 0)
        f291_2 = OLD_Input_EIA_Jet_Fuel_Price.F291()
        d291_1 = OLD_Input_EIA_Jet_Fuel_Price.D291()
        var_2 = divide(f291_2, d291_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A292():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A292
    value = 39600
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B292():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B292
    value = 4.55217774335
    formula = "=D292*$B$3"
    @eval_fn
    def B292():
        d292_1 = OLD_Input_EIA_Jet_Fuel_Price.D292()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d292_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C292():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C292
    value = 39614
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D292():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D292
    value = 3.878

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E292():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E292
    value = None
    formula = '''=IF(F292>0,F292/D292,"")'''
    @eval_fn
    def E292():
        f292_1 = OLD_Input_EIA_Jet_Fuel_Price.F292()
        var_1 = greaterthan(f292_1, 0)
        f292_2 = OLD_Input_EIA_Jet_Fuel_Price.F292()
        d292_1 = OLD_Input_EIA_Jet_Fuel_Price.D292()
        var_2 = divide(f292_2, d292_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A293():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A293
    value = 39630
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B293():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B293
    value = 4.56156851745
    formula = "=D293*$B$3"
    @eval_fn
    def B293():
        d293_1 = OLD_Input_EIA_Jet_Fuel_Price.D293()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d293_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C293():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C293
    value = 39644
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D293():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D293
    value = 3.886

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E293():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E293
    value = None
    formula = '''=IF(F293>0,F293/D293,"")'''
    @eval_fn
    def E293():
        f293_1 = OLD_Input_EIA_Jet_Fuel_Price.F293()
        var_1 = greaterthan(f293_1, 0)
        f293_2 = OLD_Input_EIA_Jet_Fuel_Price.F293()
        d293_1 = OLD_Input_EIA_Jet_Fuel_Price.D293()
        var_2 = divide(f293_2, d293_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A294():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A294
    value = 39661
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B294():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B294
    value = 3.83965275877
    formula = "=D294*$B$3"
    @eval_fn
    def B294():
        d294_1 = OLD_Input_EIA_Jet_Fuel_Price.D294()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d294_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C294():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C294
    value = 39675
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D294():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D294
    value = 3.271

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E294():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E294
    value = None
    formula = '''=IF(F294>0,F294/D294,"")'''
    @eval_fn
    def E294():
        f294_1 = OLD_Input_EIA_Jet_Fuel_Price.F294()
        var_1 = greaterthan(f294_1, 0)
        f294_2 = OLD_Input_EIA_Jet_Fuel_Price.F294()
        d294_1 = OLD_Input_EIA_Jet_Fuel_Price.D294()
        var_2 = divide(f294_2, d294_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A295():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A295
    value = 39692
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B295():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B295
    value = 3.96173282202
    formula = "=D295*$B$3"
    @eval_fn
    def B295():
        d295_1 = OLD_Input_EIA_Jet_Fuel_Price.D295()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d295_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C295():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C295
    value = 39706
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D295():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D295
    value = 3.375

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E295():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E295
    value = None
    formula = '''=IF(F295>0,F295/D295,"")'''
    @eval_fn
    def E295():
        f295_1 = OLD_Input_EIA_Jet_Fuel_Price.F295()
        var_1 = greaterthan(f295_1, 0)
        f295_2 = OLD_Input_EIA_Jet_Fuel_Price.F295()
        d295_1 = OLD_Input_EIA_Jet_Fuel_Price.D295()
        var_2 = divide(f295_2, d295_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A296():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A296
    value = 39722
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B296():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B296
    value = 2.71745525422
    formula = "=D296*$B$3"
    @eval_fn
    def B296():
        d296_1 = OLD_Input_EIA_Jet_Fuel_Price.D296()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d296_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C296():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C296
    value = 39736
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D296():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D296
    value = 2.315

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E296():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E296
    value = None
    formula = '''=IF(F296>0,F296/D296,"")'''
    @eval_fn
    def E296():
        f296_1 = OLD_Input_EIA_Jet_Fuel_Price.F296()
        var_1 = greaterthan(f296_1, 0)
        f296_2 = OLD_Input_EIA_Jet_Fuel_Price.F296()
        d296_1 = OLD_Input_EIA_Jet_Fuel_Price.D296()
        var_2 = divide(f296_2, d296_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A297():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A297
    value = 39753
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B297():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B297
    value = 2.20683191271
    formula = "=D297*$B$3"
    @eval_fn
    def B297():
        d297_1 = OLD_Input_EIA_Jet_Fuel_Price.D297()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d297_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C297():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C297
    value = 39767
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D297():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D297
    value = 1.88

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E297():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E297
    value = None
    formula = '''=IF(F297>0,F297/D297,"")'''
    @eval_fn
    def E297():
        f297_1 = OLD_Input_EIA_Jet_Fuel_Price.F297()
        var_1 = greaterthan(f297_1, 0)
        f297_2 = OLD_Input_EIA_Jet_Fuel_Price.F297()
        d297_1 = OLD_Input_EIA_Jet_Fuel_Price.D297()
        var_2 = divide(f297_2, d297_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A298():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A298
    value = 39783
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B298():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B298
    value = 1.61403929786
    formula = "=D298*$B$3"
    @eval_fn
    def B298():
        d298_1 = OLD_Input_EIA_Jet_Fuel_Price.D298()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d298_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C298():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C298
    value = 39797
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D298():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D298
    value = 1.375

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E298():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E298
    value = None
    formula = '''=IF(F298>0,F298/D298,"")'''
    @eval_fn
    def E298():
        f298_1 = OLD_Input_EIA_Jet_Fuel_Price.F298()
        var_1 = greaterthan(f298_1, 0)
        f298_2 = OLD_Input_EIA_Jet_Fuel_Price.F298()
        d298_1 = OLD_Input_EIA_Jet_Fuel_Price.D298()
        var_2 = divide(f298_2, d298_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A299():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A299
    value = 39814
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B299():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B299
    value = 1.7243808935
    formula = "=D299*$B$3"
    @eval_fn
    def B299():
        d299_1 = OLD_Input_EIA_Jet_Fuel_Price.D299()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d299_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C299():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C299
    value = 39828
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D299():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D299
    value = 1.469

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E299():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E299
    value = None
    formula = '''=IF(F299>0,F299/D299,"")'''
    @eval_fn
    def E299():
        f299_1 = OLD_Input_EIA_Jet_Fuel_Price.F299()
        var_1 = greaterthan(f299_1, 0)
        f299_2 = OLD_Input_EIA_Jet_Fuel_Price.F299()
        d299_1 = OLD_Input_EIA_Jet_Fuel_Price.D299()
        var_2 = divide(f299_2, d299_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A300():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A300
    value = 39845
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B300():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B300
    value = 1.47787307346
    formula = "=D300*$B$3"
    @eval_fn
    def B300():
        d300_1 = OLD_Input_EIA_Jet_Fuel_Price.D300()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d300_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C300():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C300
    value = 39859
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D300():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D300
    value = 1.259

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E300():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E300
    value = None
    formula = '''=IF(F300>0,F300/D300,"")'''
    @eval_fn
    def E300():
        f300_1 = OLD_Input_EIA_Jet_Fuel_Price.F300()
        var_1 = greaterthan(f300_1, 0)
        f300_2 = OLD_Input_EIA_Jet_Fuel_Price.F300()
        d300_1 = OLD_Input_EIA_Jet_Fuel_Price.D300()
        var_2 = divide(f300_2, d300_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A301():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A301
    value = 39873
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B301():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B301
    value = 1.48843769432
    formula = "=D301*$B$3"
    @eval_fn
    def B301():
        d301_1 = OLD_Input_EIA_Jet_Fuel_Price.D301()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d301_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C301():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C301
    value = 39887
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D301():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D301
    value = 1.268

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E301():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E301
    value = None
    formula = '''=IF(F301>0,F301/D301,"")'''
    @eval_fn
    def E301():
        f301_1 = OLD_Input_EIA_Jet_Fuel_Price.F301()
        var_1 = greaterthan(f301_1, 0)
        f301_2 = OLD_Input_EIA_Jet_Fuel_Price.F301()
        d301_1 = OLD_Input_EIA_Jet_Fuel_Price.D301()
        var_2 = divide(f301_2, d301_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A302():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A302
    value = 39904
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B302():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B302
    value = 1.60699621729
    formula = "=D302*$B$3"
    @eval_fn
    def B302():
        d302_1 = OLD_Input_EIA_Jet_Fuel_Price.D302()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d302_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C302():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C302
    value = 39918
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D302():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D302
    value = 1.369

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E302():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E302
    value = None
    formula = '''=IF(F302>0,F302/D302,"")'''
    @eval_fn
    def E302():
        f302_1 = OLD_Input_EIA_Jet_Fuel_Price.F302()
        var_1 = greaterthan(f302_1, 0)
        f302_2 = OLD_Input_EIA_Jet_Fuel_Price.F302()
        d302_1 = OLD_Input_EIA_Jet_Fuel_Price.D302()
        var_2 = divide(f302_2, d302_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A303():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A303
    value = 39934
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B303():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B303
    value = 1.74668398198
    formula = "=D303*$B$3"
    @eval_fn
    def B303():
        d303_1 = OLD_Input_EIA_Jet_Fuel_Price.D303()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d303_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C303():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C303
    value = 39948
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D303():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D303
    value = 1.488

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E303():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E303
    value = None
    formula = '''=IF(F303>0,F303/D303,"")'''
    @eval_fn
    def E303():
        f303_1 = OLD_Input_EIA_Jet_Fuel_Price.F303()
        var_1 = greaterthan(f303_1, 0)
        f303_2 = OLD_Input_EIA_Jet_Fuel_Price.F303()
        d303_1 = OLD_Input_EIA_Jet_Fuel_Price.D303()
        var_2 = divide(f303_2, d303_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A304():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A304
    value = 39965
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B304():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B304
    value = 2.11879340556
    formula = "=D304*$B$3"
    @eval_fn
    def B304():
        d304_1 = OLD_Input_EIA_Jet_Fuel_Price.D304()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d304_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C304():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C304
    value = 39979
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D304():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D304
    value = 1.805

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E304():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E304
    value = None
    formula = '''=IF(F304>0,F304/D304,"")'''
    @eval_fn
    def E304():
        f304_1 = OLD_Input_EIA_Jet_Fuel_Price.F304()
        var_1 = greaterthan(f304_1, 0)
        f304_2 = OLD_Input_EIA_Jet_Fuel_Price.F304()
        d304_1 = OLD_Input_EIA_Jet_Fuel_Price.D304()
        var_2 = divide(f304_2, d304_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A305():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A305
    value = 39995
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B305():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B305
    value = 2.00962565668
    formula = "=D305*$B$3"
    @eval_fn
    def B305():
        d305_1 = OLD_Input_EIA_Jet_Fuel_Price.D305()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d305_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C305():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C305
    value = 40009
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D305():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D305
    value = 1.712

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E305():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E305
    value = None
    formula = '''=IF(F305>0,F305/D305,"")'''
    @eval_fn
    def E305():
        f305_1 = OLD_Input_EIA_Jet_Fuel_Price.F305()
        var_1 = greaterthan(f305_1, 0)
        f305_2 = OLD_Input_EIA_Jet_Fuel_Price.F305()
        d305_1 = OLD_Input_EIA_Jet_Fuel_Price.D305()
        var_2 = divide(f305_2, d305_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A306():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A306
    value = 40026
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B306():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B306
    value = 2.21270114652
    formula = "=D306*$B$3"
    @eval_fn
    def B306():
        d306_1 = OLD_Input_EIA_Jet_Fuel_Price.D306()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d306_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C306():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C306
    value = 40040
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D306():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D306
    value = 1.885

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E306():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E306
    value = None
    formula = '''=IF(F306>0,F306/D306,"")'''
    @eval_fn
    def E306():
        f306_1 = OLD_Input_EIA_Jet_Fuel_Price.F306()
        var_1 = greaterthan(f306_1, 0)
        f306_2 = OLD_Input_EIA_Jet_Fuel_Price.F306()
        d306_1 = OLD_Input_EIA_Jet_Fuel_Price.D306()
        var_2 = divide(f306_2, d306_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A307():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A307
    value = 40057
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B307():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B307
    value = 2.05305798688
    formula = "=D307*$B$3"
    @eval_fn
    def B307():
        d307_1 = OLD_Input_EIA_Jet_Fuel_Price.D307()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d307_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C307():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C307
    value = 40071
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D307():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D307
    value = 1.749

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E307():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E307
    value = None
    formula = '''=IF(F307>0,F307/D307,"")'''
    @eval_fn
    def E307():
        f307_1 = OLD_Input_EIA_Jet_Fuel_Price.F307()
        var_1 = greaterthan(f307_1, 0)
        f307_2 = OLD_Input_EIA_Jet_Fuel_Price.F307()
        d307_1 = OLD_Input_EIA_Jet_Fuel_Price.D307()
        var_2 = divide(f307_2, d307_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A308():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A308
    value = 40087
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B308():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B308
    value = 2.27961041196
    formula = "=D308*$B$3"
    @eval_fn
    def B308():
        d308_1 = OLD_Input_EIA_Jet_Fuel_Price.D308()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d308_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C308():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C308
    value = 40101
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D308():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D308
    value = 1.942

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E308():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E308
    value = None
    formula = '''=IF(F308>0,F308/D308,"")'''
    @eval_fn
    def E308():
        f308_1 = OLD_Input_EIA_Jet_Fuel_Price.F308()
        var_1 = greaterthan(f308_1, 0)
        f308_2 = OLD_Input_EIA_Jet_Fuel_Price.F308()
        d308_1 = OLD_Input_EIA_Jet_Fuel_Price.D308()
        var_2 = divide(f308_2, d308_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A309():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A309
    value = 40118
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B309():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B309
    value = 2.33125966949
    formula = "=D309*$B$3"
    @eval_fn
    def B309():
        d309_1 = OLD_Input_EIA_Jet_Fuel_Price.D309()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d309_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C309():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C309
    value = 40132
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D309():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D309
    value = 1.986

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E309():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E309
    value = None
    formula = '''=IF(F309>0,F309/D309,"")'''
    @eval_fn
    def E309():
        f309_1 = OLD_Input_EIA_Jet_Fuel_Price.F309()
        var_1 = greaterthan(f309_1, 0)
        f309_2 = OLD_Input_EIA_Jet_Fuel_Price.F309()
        d309_1 = OLD_Input_EIA_Jet_Fuel_Price.D309()
        var_2 = divide(f309_2, d309_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A310():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A310
    value = 40148
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B310():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B310
    value = 2.32304274216
    formula = "=D310*$B$3"
    @eval_fn
    def B310():
        d310_1 = OLD_Input_EIA_Jet_Fuel_Price.D310()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d310_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C310():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C310
    value = 40162
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D310():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D310
    value = 1.979

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E310():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E310
    value = None
    formula = '''=IF(F310>0,F310/D310,"")'''
    @eval_fn
    def E310():
        f310_1 = OLD_Input_EIA_Jet_Fuel_Price.F310()
        var_1 = greaterthan(f310_1, 0)
        f310_2 = OLD_Input_EIA_Jet_Fuel_Price.F310()
        d310_1 = OLD_Input_EIA_Jet_Fuel_Price.D310()
        var_2 = divide(f310_2, d310_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A311():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A311
    value = 40179
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B311():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B311
    value = 2.40873355579
    formula = "=D311*$B$3"
    @eval_fn
    def B311():
        d311_1 = OLD_Input_EIA_Jet_Fuel_Price.D311()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d311_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C311():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C311
    value = 40193
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D311():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D311
    value = 2.052

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E311():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E311
    value = None
    formula = '''=IF(F311>0,F311/D311,"")'''
    @eval_fn
    def E311():
        f311_1 = OLD_Input_EIA_Jet_Fuel_Price.F311()
        var_1 = greaterthan(f311_1, 0)
        f311_2 = OLD_Input_EIA_Jet_Fuel_Price.F311()
        d311_1 = OLD_Input_EIA_Jet_Fuel_Price.D311()
        var_2 = divide(f311_2, d311_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A312():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A312
    value = 40210
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B312():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B312
    value = 2.33478120978
    formula = "=D312*$B$3"
    @eval_fn
    def B312():
        d312_1 = OLD_Input_EIA_Jet_Fuel_Price.D312()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d312_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C312():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C312
    value = 40224
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D312():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D312
    value = 1.989

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E312():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E312
    value = None
    formula = '''=IF(F312>0,F312/D312,"")'''
    @eval_fn
    def E312():
        f312_1 = OLD_Input_EIA_Jet_Fuel_Price.F312()
        var_1 = greaterthan(f312_1, 0)
        f312_2 = OLD_Input_EIA_Jet_Fuel_Price.F312()
        d312_1 = OLD_Input_EIA_Jet_Fuel_Price.D312()
        var_2 = divide(f312_2, d312_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A313():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A313
    value = 40238
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B313():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B313
    value = 2.47446897447
    formula = "=D313*$B$3"
    @eval_fn
    def B313():
        d313_1 = OLD_Input_EIA_Jet_Fuel_Price.D313()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d313_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C313():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C313
    value = 40252
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D313():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D313
    value = 2.108

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E313():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E313
    value = None
    formula = '''=IF(F313>0,F313/D313,"")'''
    @eval_fn
    def E313():
        f313_1 = OLD_Input_EIA_Jet_Fuel_Price.F313()
        var_1 = greaterthan(f313_1, 0)
        f313_2 = OLD_Input_EIA_Jet_Fuel_Price.F313()
        d313_1 = OLD_Input_EIA_Jet_Fuel_Price.D313()
        var_2 = divide(f313_2, d313_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A314():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A314
    value = 40269
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B314():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B314
    value = 2.63293828735
    formula = "=D314*$B$3"
    @eval_fn
    def B314():
        d314_1 = OLD_Input_EIA_Jet_Fuel_Price.D314()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d314_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C314():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C314
    value = 40283
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D314():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D314
    value = 2.243

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E314():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E314
    value = None
    formula = '''=IF(F314>0,F314/D314,"")'''
    @eval_fn
    def E314():
        f314_1 = OLD_Input_EIA_Jet_Fuel_Price.F314()
        var_1 = greaterthan(f314_1, 0)
        f314_2 = OLD_Input_EIA_Jet_Fuel_Price.F314()
        d314_1 = OLD_Input_EIA_Jet_Fuel_Price.D314()
        var_2 = divide(f314_2, d314_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A315():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A315
    value = 40299
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B315():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B315
    value = 2.42164587017
    formula = "=D315*$B$3"
    @eval_fn
    def B315():
        d315_1 = OLD_Input_EIA_Jet_Fuel_Price.D315()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d315_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C315():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C315
    value = 40313
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D315():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D315
    value = 2.063

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E315():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E315
    value = None
    formula = '''=IF(F315>0,F315/D315,"")'''
    @eval_fn
    def E315():
        f315_1 = OLD_Input_EIA_Jet_Fuel_Price.F315()
        var_1 = greaterthan(f315_1, 0)
        f315_2 = OLD_Input_EIA_Jet_Fuel_Price.F315()
        d315_1 = OLD_Input_EIA_Jet_Fuel_Price.D315()
        var_2 = divide(f315_2, d315_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A316():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A316
    value = 40330
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B316():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B316
    value = 2.41577663636
    formula = "=D316*$B$3"
    @eval_fn
    def B316():
        d316_1 = OLD_Input_EIA_Jet_Fuel_Price.D316()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d316_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C316():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C316
    value = 40344
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D316():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D316
    value = 2.058

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E316():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E316
    value = None
    formula = '''=IF(F316>0,F316/D316,"")'''
    @eval_fn
    def E316():
        f316_1 = OLD_Input_EIA_Jet_Fuel_Price.F316()
        var_1 = greaterthan(f316_1, 0)
        f316_2 = OLD_Input_EIA_Jet_Fuel_Price.F316()
        d316_1 = OLD_Input_EIA_Jet_Fuel_Price.D316()
        var_2 = divide(f316_2, d316_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A317
    value = 40360
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B317
    value = 2.36999661264
    formula = "=D317*$B$3"
    @eval_fn
    def B317():
        d317_1 = OLD_Input_EIA_Jet_Fuel_Price.D317()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d317_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C317
    value = 40374
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D317
    value = 2.019

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E317
    value = 1.13075780089
    formula = '''=IF(F317>0,F317/D317,"")'''
    @eval_fn
    def E317():
        f317_1 = OLD_Input_EIA_Jet_Fuel_Price.F317()
        var_1 = greaterthan(f317_1, 0)
        f317_2 = OLD_Input_EIA_Jet_Fuel_Price.F317()
        d317_1 = OLD_Input_EIA_Jet_Fuel_Price.D317()
        var_2 = divide(f317_2, d317_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F317():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F317
    value = 2.283

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A318
    value = 40391
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B318
    value = 2.44512280542
    formula = "=D318*$B$3"
    @eval_fn
    def B318():
        d318_1 = OLD_Input_EIA_Jet_Fuel_Price.D318()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d318_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C318
    value = 40405
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D318
    value = 2.083

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E318
    value = 1.08737397984
    formula = '''=IF(F318>0,F318/D318,"")'''
    @eval_fn
    def E318():
        f318_1 = OLD_Input_EIA_Jet_Fuel_Price.F318()
        var_1 = greaterthan(f318_1, 0)
        f318_2 = OLD_Input_EIA_Jet_Fuel_Price.F318()
        d318_1 = OLD_Input_EIA_Jet_Fuel_Price.D318()
        var_2 = divide(f318_2, d318_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F318():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F318
    value = 2.265

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A319
    value = 40422
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B319
    value = 2.48151205504
    formula = "=D319*$B$3"
    @eval_fn
    def B319():
        d319_1 = OLD_Input_EIA_Jet_Fuel_Price.D319()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d319_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C319
    value = 40436
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D319
    value = 2.114

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E319
    value = 1.06480605487
    formula = '''=IF(F319>0,F319/D319,"")'''
    @eval_fn
    def E319():
        f319_1 = OLD_Input_EIA_Jet_Fuel_Price.F319()
        var_1 = greaterthan(f319_1, 0)
        f319_2 = OLD_Input_EIA_Jet_Fuel_Price.F319()
        d319_1 = OLD_Input_EIA_Jet_Fuel_Price.D319()
        var_2 = divide(f319_2, d319_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F319():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F319
    value = 2.251

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A320
    value = 40452
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B320
    value = 2.63880752116
    formula = "=D320*$B$3"
    @eval_fn
    def B320():
        d320_1 = OLD_Input_EIA_Jet_Fuel_Price.D320()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d320_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C320
    value = 40466
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D320
    value = 2.248

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E320
    value = 1.08140569395
    formula = '''=IF(F320>0,F320/D320,"")'''
    @eval_fn
    def E320():
        f320_1 = OLD_Input_EIA_Jet_Fuel_Price.F320()
        var_1 = greaterthan(f320_1, 0)
        f320_2 = OLD_Input_EIA_Jet_Fuel_Price.F320()
        d320_1 = OLD_Input_EIA_Jet_Fuel_Price.D320()
        var_2 = divide(f320_2, d320_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F320():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F320
    value = 2.431

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A321
    value = 40483
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B321
    value = 2.72684602832
    formula = "=D321*$B$3"
    @eval_fn
    def B321():
        d321_1 = OLD_Input_EIA_Jet_Fuel_Price.D321()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d321_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C321
    value = 40497
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D321
    value = 2.323

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E321
    value = 1.06973740852
    formula = '''=IF(F321>0,F321/D321,"")'''
    @eval_fn
    def E321():
        f321_1 = OLD_Input_EIA_Jet_Fuel_Price.F321()
        var_1 = greaterthan(f321_1, 0)
        f321_2 = OLD_Input_EIA_Jet_Fuel_Price.F321()
        d321_1 = OLD_Input_EIA_Jet_Fuel_Price.D321()
        var_2 = divide(f321_2, d321_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F321():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F321
    value = 2.485

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A322
    value = 40513
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B322
    value = 2.87944610739
    formula = "=D322*$B$3"
    @eval_fn
    def B322():
        d322_1 = OLD_Input_EIA_Jet_Fuel_Price.D322()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d322_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C322
    value = 40527
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D322
    value = 2.453

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E322
    value = 1.07011822258
    formula = '''=IF(F322>0,F322/D322,"")'''
    @eval_fn
    def E322():
        f322_1 = OLD_Input_EIA_Jet_Fuel_Price.F322()
        var_1 = greaterthan(f322_1, 0)
        f322_2 = OLD_Input_EIA_Jet_Fuel_Price.F322()
        d322_1 = OLD_Input_EIA_Jet_Fuel_Price.D322()
        var_2 = divide(f322_2, d322_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F322():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F322
    value = 2.625

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A323():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A323
    value = 40544
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B323():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B323
    value = 3.07430466989
    formula = "=D323*$B$3"
    @eval_fn
    def B323():
        d323_1 = OLD_Input_EIA_Jet_Fuel_Price.D323()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d323_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C323():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C323
    value = 40558
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D323():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D323
    value = 2.619

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E323():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E323
    value = None
    formula = '''=IF(F323>0,F323/D323,"")'''
    @eval_fn
    def E323():
        f323_1 = OLD_Input_EIA_Jet_Fuel_Price.F323()
        var_1 = greaterthan(f323_1, 0)
        f323_2 = OLD_Input_EIA_Jet_Fuel_Price.F323()
        d323_1 = OLD_Input_EIA_Jet_Fuel_Price.D323()
        var_2 = divide(f323_2, d323_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A324():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A324
    value = 40575
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B324():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B324
    value = 3.33255095755
    formula = "=D324*$B$3"
    @eval_fn
    def B324():
        d324_1 = OLD_Input_EIA_Jet_Fuel_Price.D324()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d324_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C324():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C324
    value = 40589
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D324():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D324
    value = 2.839

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E324():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E324
    value = None
    formula = '''=IF(F324>0,F324/D324,"")'''
    @eval_fn
    def E324():
        f324_1 = OLD_Input_EIA_Jet_Fuel_Price.F324()
        var_1 = greaterthan(f324_1, 0)
        f324_2 = OLD_Input_EIA_Jet_Fuel_Price.F324()
        d324_1 = OLD_Input_EIA_Jet_Fuel_Price.D324()
        var_2 = divide(f324_2, d324_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A325
    value = 40603
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B325
    value = 3.6682711315
    formula = "=D325*$B$3"
    @eval_fn
    def B325():
        d325_1 = OLD_Input_EIA_Jet_Fuel_Price.D325()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d325_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C325
    value = 40617
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D325
    value = 3.125

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E325
    value = 1.03744
    formula = '''=IF(F325>0,F325/D325,"")'''
    @eval_fn
    def E325():
        f325_1 = OLD_Input_EIA_Jet_Fuel_Price.F325()
        var_1 = greaterthan(f325_1, 0)
        f325_2 = OLD_Input_EIA_Jet_Fuel_Price.F325()
        d325_1 = OLD_Input_EIA_Jet_Fuel_Price.D325()
        var_2 = divide(f325_2, d325_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F325():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F325
    value = 3.242

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A326
    value = 40634
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B326
    value = 3.83495737172
    formula = "=D326*$B$3"
    @eval_fn
    def B326():
        d326_1 = OLD_Input_EIA_Jet_Fuel_Price.D326()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d326_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C326
    value = 40648
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D326
    value = 3.267

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E326
    value = 1.05479032752
    formula = '''=IF(F326>0,F326/D326,"")'''
    @eval_fn
    def E326():
        f326_1 = OLD_Input_EIA_Jet_Fuel_Price.F326()
        var_1 = greaterthan(f326_1, 0)
        f326_2 = OLD_Input_EIA_Jet_Fuel_Price.F326()
        d326_1 = OLD_Input_EIA_Jet_Fuel_Price.D326()
        var_2 = divide(f326_2, d326_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F326():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F326
    value = 3.446

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A327
    value = 40664
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B327
    value = 3.62131726102
    formula = "=D327*$B$3"
    @eval_fn
    def B327():
        d327_1 = OLD_Input_EIA_Jet_Fuel_Price.D327()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d327_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C327
    value = 40678
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D327
    value = 3.085

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E327
    value = 1.05089141005
    formula = '''=IF(F327>0,F327/D327,"")'''
    @eval_fn
    def E327():
        f327_1 = OLD_Input_EIA_Jet_Fuel_Price.F327()
        var_1 = greaterthan(f327_1, 0)
        f327_2 = OLD_Input_EIA_Jet_Fuel_Price.F327()
        d327_1 = OLD_Input_EIA_Jet_Fuel_Price.D327()
        var_2 = divide(f327_2, d327_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F327():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F327
    value = 3.242

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A328():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A328
    value = 40695
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B328():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B328
    value = 3.5755372373
    formula = "=D328*$B$3"
    @eval_fn
    def B328():
        d328_1 = OLD_Input_EIA_Jet_Fuel_Price.D328()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d328_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C328():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C328
    value = 40709
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D328():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D328
    value = 3.046

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E328():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E328
    value = None
    formula = '''=IF(F328>0,F328/D328,"")'''
    @eval_fn
    def E328():
        f328_1 = OLD_Input_EIA_Jet_Fuel_Price.F328()
        var_1 = greaterthan(f328_1, 0)
        f328_2 = OLD_Input_EIA_Jet_Fuel_Price.F328()
        d328_1 = OLD_Input_EIA_Jet_Fuel_Price.D328()
        var_2 = divide(f328_2, d328_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A329():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A329
    value = 40725
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B329():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B329
    value = 3.67531421208
    formula = "=D329*$B$3"
    @eval_fn
    def B329():
        d329_1 = OLD_Input_EIA_Jet_Fuel_Price.D329()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d329_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C329():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C329
    value = 40739
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D329():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D329
    value = 3.131

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E329():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E329
    value = None
    formula = '''=IF(F329>0,F329/D329,"")'''
    @eval_fn
    def E329():
        f329_1 = OLD_Input_EIA_Jet_Fuel_Price.F329()
        var_1 = greaterthan(f329_1, 0)
        f329_2 = OLD_Input_EIA_Jet_Fuel_Price.F329()
        d329_1 = OLD_Input_EIA_Jet_Fuel_Price.D329()
        var_2 = divide(f329_2, d329_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A330
    value = 40756
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B330
    value = 3.53093106034
    formula = "=D330*$B$3"
    @eval_fn
    def B330():
        d330_1 = OLD_Input_EIA_Jet_Fuel_Price.D330()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d330_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C330
    value = 40770
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D330
    value = 3.008

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E330
    value = 1.02493351064
    formula = '''=IF(F330>0,F330/D330,"")'''
    @eval_fn
    def E330():
        f330_1 = OLD_Input_EIA_Jet_Fuel_Price.F330()
        var_1 = greaterthan(f330_1, 0)
        f330_2 = OLD_Input_EIA_Jet_Fuel_Price.F330()
        d330_1 = OLD_Input_EIA_Jet_Fuel_Price.D330()
        var_2 = divide(f330_2, d330_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F330():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F330
    value = 3.083

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A331
    value = 40787
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B331
    value = 3.46050025462
    formula = "=D331*$B$3"
    @eval_fn
    def B331():
        d331_1 = OLD_Input_EIA_Jet_Fuel_Price.D331()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d331_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C331
    value = 40801
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D331
    value = 2.948

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E331
    value = 1.06852103121
    formula = '''=IF(F331>0,F331/D331,"")'''
    @eval_fn
    def E331():
        f331_1 = OLD_Input_EIA_Jet_Fuel_Price.F331()
        var_1 = greaterthan(f331_1, 0)
        f331_2 = OLD_Input_EIA_Jet_Fuel_Price.F331()
        d331_1 = OLD_Input_EIA_Jet_Fuel_Price.D331()
        var_2 = divide(f331_2, d331_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F331():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F331
    value = 3.15

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A332
    value = 40817
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B332
    value = 3.48162949633
    formula = "=D332*$B$3"
    @eval_fn
    def B332():
        d332_1 = OLD_Input_EIA_Jet_Fuel_Price.D332()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d332_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C332
    value = 40831
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D332
    value = 2.966

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E332
    value = 1.03809844909
    formula = '''=IF(F332>0,F332/D332,"")'''
    @eval_fn
    def E332():
        f332_1 = OLD_Input_EIA_Jet_Fuel_Price.F332()
        var_1 = greaterthan(f332_1, 0)
        f332_2 = OLD_Input_EIA_Jet_Fuel_Price.F332()
        d332_1 = OLD_Input_EIA_Jet_Fuel_Price.D332()
        var_2 = divide(f332_2, d332_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F332():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F332
    value = 3.079

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A333():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A333
    value = 40848
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B333():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B333
    value = 3.5755372373
    formula = "=D333*$B$3"
    @eval_fn
    def B333():
        d333_1 = OLD_Input_EIA_Jet_Fuel_Price.D333()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d333_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C333():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C333
    value = 40862
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D333():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D333
    value = 3.046

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E333():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E333
    value = None
    formula = '''=IF(F333>0,F333/D333,"")'''
    @eval_fn
    def E333():
        f333_1 = OLD_Input_EIA_Jet_Fuel_Price.F333()
        var_1 = greaterthan(f333_1, 0)
        f333_2 = OLD_Input_EIA_Jet_Fuel_Price.F333()
        d333_1 = OLD_Input_EIA_Jet_Fuel_Price.D333()
        var_2 = divide(f333_2, d333_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A334():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A334
    value = 40878
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B334():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B334
    value = 3.37246174746
    formula = "=D334*$B$3"
    @eval_fn
    def B334():
        d334_1 = OLD_Input_EIA_Jet_Fuel_Price.D334()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d334_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C334():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C334
    value = 40892
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D334():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D334
    value = 2.873

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E334():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E334
    value = None
    formula = '''=IF(F334>0,F334/D334,"")'''
    @eval_fn
    def E334():
        f334_1 = OLD_Input_EIA_Jet_Fuel_Price.F334()
        var_1 = greaterthan(f334_1, 0)
        f334_2 = OLD_Input_EIA_Jet_Fuel_Price.F334()
        d334_1 = OLD_Input_EIA_Jet_Fuel_Price.D334()
        var_2 = divide(f334_2, d334_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A335():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A335
    value = 40909
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B335():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B335
    value = 3.62366495455
    formula = "=D335*$B$3"
    @eval_fn
    def B335():
        d335_1 = OLD_Input_EIA_Jet_Fuel_Price.D335()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d335_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C335():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C335
    value = 40923
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D335():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D335
    value = 3.087

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E335():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E335
    value = None
    formula = '''=IF(F335>0,F335/D335,"")'''
    @eval_fn
    def E335():
        f335_1 = OLD_Input_EIA_Jet_Fuel_Price.F335()
        var_1 = greaterthan(f335_1, 0)
        f335_2 = OLD_Input_EIA_Jet_Fuel_Price.F335()
        d335_1 = OLD_Input_EIA_Jet_Fuel_Price.D335()
        var_2 = divide(f335_2, d335_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A336():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A336
    value = 40940
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B336():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B336
    value = 3.764526566
    formula = "=D336*$B$3"
    @eval_fn
    def B336():
        d336_1 = OLD_Input_EIA_Jet_Fuel_Price.D336()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d336_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C336():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C336
    value = 40954
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D336():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D336
    value = 3.207

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E336():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E336
    value = None
    formula = '''=IF(F336>0,F336/D336,"")'''
    @eval_fn
    def E336():
        f336_1 = OLD_Input_EIA_Jet_Fuel_Price.F336()
        var_1 = greaterthan(f336_1, 0)
        f336_2 = OLD_Input_EIA_Jet_Fuel_Price.F336()
        d336_1 = OLD_Input_EIA_Jet_Fuel_Price.D336()
        var_2 = divide(f336_2, d336_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A337():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A337
    value = 40969
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B337():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B337
    value = 3.82204505734
    formula = "=D337*$B$3"
    @eval_fn
    def B337():
        d337_1 = OLD_Input_EIA_Jet_Fuel_Price.D337()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d337_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C337():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C337
    value = 40983
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D337():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D337
    value = 3.256

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E337():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E337
    value = None
    formula = '''=IF(F337>0,F337/D337,"")'''
    @eval_fn
    def E337():
        f337_1 = OLD_Input_EIA_Jet_Fuel_Price.F337()
        var_1 = greaterthan(f337_1, 0)
        f337_2 = OLD_Input_EIA_Jet_Fuel_Price.F337()
        d337_1 = OLD_Input_EIA_Jet_Fuel_Price.D337()
        var_2 = divide(f337_2, d337_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A338():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A338
    value = 41000
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B338():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B338
    value = 3.78682965447
    formula = "=D338*$B$3"
    @eval_fn
    def B338():
        d338_1 = OLD_Input_EIA_Jet_Fuel_Price.D338()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d338_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C338():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C338
    value = 41014
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D338():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D338
    value = 3.226

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E338():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E338
    value = None
    formula = '''=IF(F338>0,F338/D338,"")'''
    @eval_fn
    def E338():
        f338_1 = OLD_Input_EIA_Jet_Fuel_Price.F338()
        var_1 = greaterthan(f338_1, 0)
        f338_2 = OLD_Input_EIA_Jet_Fuel_Price.F338()
        d338_1 = OLD_Input_EIA_Jet_Fuel_Price.D338()
        var_2 = divide(f338_2, d338_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A339
    value = 41030
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B339
    value = 3.49102027043
    formula = "=D339*$B$3"
    @eval_fn
    def B339():
        d339_1 = OLD_Input_EIA_Jet_Fuel_Price.D339()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d339_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C339
    value = 41044
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D339
    value = 2.974

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E339
    value = 1.03328850034
    formula = '''=IF(F339>0,F339/D339,"")'''
    @eval_fn
    def E339():
        f339_1 = OLD_Input_EIA_Jet_Fuel_Price.F339()
        var_1 = greaterthan(f339_1, 0)
        f339_2 = OLD_Input_EIA_Jet_Fuel_Price.F339()
        d339_1 = OLD_Input_EIA_Jet_Fuel_Price.D339()
        var_2 = divide(f339_2, d339_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F339():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F339
    value = 3.073

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A340
    value = 41061
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B340
    value = 3.14356162885
    formula = "=D340*$B$3"
    @eval_fn
    def B340():
        d340_1 = OLD_Input_EIA_Jet_Fuel_Price.D340()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d340_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C340
    value = 41075
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D340
    value = 2.678

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E340
    value = 1.03958177745
    formula = '''=IF(F340>0,F340/D340,"")'''
    @eval_fn
    def E340():
        f340_1 = OLD_Input_EIA_Jet_Fuel_Price.F340()
        var_1 = greaterthan(f340_1, 0)
        f340_2 = OLD_Input_EIA_Jet_Fuel_Price.F340()
        d340_1 = OLD_Input_EIA_Jet_Fuel_Price.D340()
        var_2 = divide(f340_2, d340_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F340():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F340
    value = 2.784

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A341():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A341
    value = 41091
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B341():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B341
    value = 3.39476483594
    formula = "=D341*$B$3"
    @eval_fn
    def B341():
        d341_1 = OLD_Input_EIA_Jet_Fuel_Price.D341()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d341_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C341():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C341
    value = 41105
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D341():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D341
    value = 2.892

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E341():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E341
    value = None
    formula = '''=IF(F341>0,F341/D341,"")'''
    @eval_fn
    def E341():
        f341_1 = OLD_Input_EIA_Jet_Fuel_Price.F341()
        var_1 = greaterthan(f341_1, 0)
        f341_2 = OLD_Input_EIA_Jet_Fuel_Price.F341()
        d341_1 = OLD_Input_EIA_Jet_Fuel_Price.D341()
        var_2 = divide(f341_2, d341_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A342
    value = 41122
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B342
    value = 3.70466038113
    formula = "=D342*$B$3"
    @eval_fn
    def B342():
        d342_1 = OLD_Input_EIA_Jet_Fuel_Price.D342()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d342_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C342
    value = 41136
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D342
    value = 3.156

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E342
    value = 1.02027883397
    formula = '''=IF(F342>0,F342/D342,"")'''
    @eval_fn
    def E342():
        f342_1 = OLD_Input_EIA_Jet_Fuel_Price.F342()
        var_1 = greaterthan(f342_1, 0)
        f342_2 = OLD_Input_EIA_Jet_Fuel_Price.F342()
        d342_1 = OLD_Input_EIA_Jet_Fuel_Price.D342()
        var_2 = divide(f342_2, d342_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F342():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F342
    value = 3.22

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A343():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A343
    value = 41153
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B343():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B343
    value = 3.7457450178
    formula = "=D343*$B$3"
    @eval_fn
    def B343():
        d343_1 = OLD_Input_EIA_Jet_Fuel_Price.D343()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d343_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C343():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C343
    value = 41167
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D343():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D343
    value = 3.191

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E343():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E343
    value = None
    formula = '''=IF(F343>0,F343/D343,"")'''
    @eval_fn
    def E343():
        f343_1 = OLD_Input_EIA_Jet_Fuel_Price.F343()
        var_1 = greaterthan(f343_1, 0)
        f343_2 = OLD_Input_EIA_Jet_Fuel_Price.F343()
        d343_1 = OLD_Input_EIA_Jet_Fuel_Price.D343()
        var_2 = divide(f343_2, d343_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A344():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A344
    value = 41183
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B344():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B344
    value = 3.65183727684
    formula = "=D344*$B$3"
    @eval_fn
    def B344():
        d344_1 = OLD_Input_EIA_Jet_Fuel_Price.D344()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d344_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C344():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C344
    value = 41197
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D344():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D344
    value = 3.111

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E344():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E344
    value = None
    formula = '''=IF(F344>0,F344/D344,"")'''
    @eval_fn
    def E344():
        f344_1 = OLD_Input_EIA_Jet_Fuel_Price.F344()
        var_1 = greaterthan(f344_1, 0)
        f344_2 = OLD_Input_EIA_Jet_Fuel_Price.F344()
        d344_1 = OLD_Input_EIA_Jet_Fuel_Price.D344()
        var_2 = divide(f344_2, d344_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A345():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A345
    value = 41214
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B345():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B345
    value = 3.47458641576
    formula = "=D345*$B$3"
    @eval_fn
    def B345():
        d345_1 = OLD_Input_EIA_Jet_Fuel_Price.D345()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d345_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C345():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C345
    value = 41228
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D345():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D345
    value = 2.96

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E345():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E345
    value = None
    formula = '''=IF(F345>0,F345/D345,"")'''
    @eval_fn
    def E345():
        f345_1 = OLD_Input_EIA_Jet_Fuel_Price.F345()
        var_1 = greaterthan(f345_1, 0)
        f345_2 = OLD_Input_EIA_Jet_Fuel_Price.F345()
        d345_1 = OLD_Input_EIA_Jet_Fuel_Price.D345()
        var_2 = divide(f345_2, d345_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A346():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A346
    value = 41244
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B346():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B346
    value = 3.45110948052
    formula = "=D346*$B$3"
    @eval_fn
    def B346():
        d346_1 = OLD_Input_EIA_Jet_Fuel_Price.D346()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d346_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C346():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C346
    value = 41258
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D346():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D346
    value = 2.94

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E346():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E346
    value = None
    formula = '''=IF(F346>0,F346/D346,"")'''
    @eval_fn
    def E346():
        f346_1 = OLD_Input_EIA_Jet_Fuel_Price.F346()
        var_1 = greaterthan(f346_1, 0)
        f346_2 = OLD_Input_EIA_Jet_Fuel_Price.F346()
        d346_1 = OLD_Input_EIA_Jet_Fuel_Price.D346()
        var_2 = divide(f346_2, d346_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A347():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A347
    value = 41275
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B347():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B347
    value = 3.62836034159
    formula = "=D347*$B$3"
    @eval_fn
    def B347():
        d347_1 = OLD_Input_EIA_Jet_Fuel_Price.D347()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d347_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C347():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C347
    value = 41289
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D347():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D347
    value = 3.091

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E347():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E347
    value = None
    formula = '''=IF(F347>0,F347/D347,"")'''
    @eval_fn
    def E347():
        f347_1 = OLD_Input_EIA_Jet_Fuel_Price.F347()
        var_1 = greaterthan(f347_1, 0)
        f347_2 = OLD_Input_EIA_Jet_Fuel_Price.F347()
        d347_1 = OLD_Input_EIA_Jet_Fuel_Price.D347()
        var_2 = divide(f347_2, d347_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A348
    value = 41306
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B348
    value = 3.77743888038
    formula = "=D348*$B$3"
    @eval_fn
    def B348():
        d348_1 = OLD_Input_EIA_Jet_Fuel_Price.D348()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d348_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C348
    value = 41320
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D348
    value = 3.218

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E348
    value = 1.05655686762
    formula = '''=IF(F348>0,F348/D348,"")'''
    @eval_fn
    def E348():
        f348_1 = OLD_Input_EIA_Jet_Fuel_Price.F348()
        var_1 = greaterthan(f348_1, 0)
        f348_2 = OLD_Input_EIA_Jet_Fuel_Price.F348()
        d348_1 = OLD_Input_EIA_Jet_Fuel_Price.D348()
        var_2 = divide(f348_2, d348_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F348():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F348
    value = 3.4

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A349():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A349
    value = 41334
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B349():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B349
    value = 3.48515103662
    formula = "=D349*$B$3"
    @eval_fn
    def B349():
        d349_1 = OLD_Input_EIA_Jet_Fuel_Price.D349()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d349_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C349():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C349
    value = 41348
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D349():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D349
    value = 2.969

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E349():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E349
    value = None
    formula = '''=IF(F349>0,F349/D349,"")'''
    @eval_fn
    def E349():
        f349_1 = OLD_Input_EIA_Jet_Fuel_Price.F349()
        var_1 = greaterthan(f349_1, 0)
        f349_2 = OLD_Input_EIA_Jet_Fuel_Price.F349()
        d349_1 = OLD_Input_EIA_Jet_Fuel_Price.D349()
        var_2 = divide(f349_2, d349_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A350():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A350
    value = 41365
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B350():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B350
    value = 3.29616170792
    formula = "=D350*$B$3"
    @eval_fn
    def B350():
        d350_1 = OLD_Input_EIA_Jet_Fuel_Price.D350()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d350_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C350():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C350
    value = 41379
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D350():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D350
    value = 2.808

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E350():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E350
    value = None
    formula = '''=IF(F350>0,F350/D350,"")'''
    @eval_fn
    def E350():
        f350_1 = OLD_Input_EIA_Jet_Fuel_Price.F350()
        var_1 = greaterthan(f350_1, 0)
        f350_2 = OLD_Input_EIA_Jet_Fuel_Price.F350()
        d350_1 = OLD_Input_EIA_Jet_Fuel_Price.D350()
        var_2 = divide(f350_2, d350_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A351():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A351
    value = 41395
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B351():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B351
    value = 3.19873242667
    formula = "=D351*$B$3"
    @eval_fn
    def B351():
        d351_1 = OLD_Input_EIA_Jet_Fuel_Price.D351()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d351_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C351():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C351
    value = 41409
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D351():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D351
    value = 2.725

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E351():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E351
    value = None
    formula = '''=IF(F351>0,F351/D351,"")'''
    @eval_fn
    def E351():
        f351_1 = OLD_Input_EIA_Jet_Fuel_Price.F351()
        var_1 = greaterthan(f351_1, 0)
        f351_2 = OLD_Input_EIA_Jet_Fuel_Price.F351()
        d351_1 = OLD_Input_EIA_Jet_Fuel_Price.D351()
        var_2 = divide(f351_2, d351_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A352():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A352
    value = 41426
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B352():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B352
    value = 3.2503816842
    formula = "=D352*$B$3"
    @eval_fn
    def B352():
        d352_1 = OLD_Input_EIA_Jet_Fuel_Price.D352()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d352_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C352():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C352
    value = 41440
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D352():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D352
    value = 2.769

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E352():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E352
    value = None
    formula = '''=IF(F352>0,F352/D352,"")'''
    @eval_fn
    def E352():
        f352_1 = OLD_Input_EIA_Jet_Fuel_Price.F352()
        var_1 = greaterthan(f352_1, 0)
        f352_2 = OLD_Input_EIA_Jet_Fuel_Price.F352()
        d352_1 = OLD_Input_EIA_Jet_Fuel_Price.D352()
        var_2 = divide(f352_2, d352_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A353():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A353
    value = 41456
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B353():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B353
    value = 3.39711252946
    formula = "=D353*$B$3"
    @eval_fn
    def B353():
        d353_1 = OLD_Input_EIA_Jet_Fuel_Price.D353()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d353_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C353():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C353
    value = 41470
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D353():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D353
    value = 2.894

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E353():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E353
    value = None
    formula = '''=IF(F353>0,F353/D353,"")'''
    @eval_fn
    def E353():
        f353_1 = OLD_Input_EIA_Jet_Fuel_Price.F353()
        var_1 = greaterthan(f353_1, 0)
        f353_2 = OLD_Input_EIA_Jet_Fuel_Price.F353()
        d353_1 = OLD_Input_EIA_Jet_Fuel_Price.D353()
        var_2 = divide(f353_2, d353_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A354():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A354
    value = 41487
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B354():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B354
    value = 3.52506182653
    formula = "=D354*$B$3"
    @eval_fn
    def B354():
        d354_1 = OLD_Input_EIA_Jet_Fuel_Price.D354()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d354_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C354():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C354
    value = 41501
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D354():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D354
    value = 3.003

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E354():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E354
    value = None
    formula = '''=IF(F354>0,F354/D354,"")'''
    @eval_fn
    def E354():
        f354_1 = OLD_Input_EIA_Jet_Fuel_Price.F354()
        var_1 = greaterthan(f354_1, 0)
        f354_2 = OLD_Input_EIA_Jet_Fuel_Price.F354()
        d354_1 = OLD_Input_EIA_Jet_Fuel_Price.D354()
        var_2 = divide(f354_2, d354_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A355
    value = 41518
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B355
    value = 3.44406639995
    formula = "=D355*$B$3"
    @eval_fn
    def B355():
        d355_1 = OLD_Input_EIA_Jet_Fuel_Price.D355()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d355_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C355
    value = 41532
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D355
    value = 2.934

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E355
    value = 1.04601226994
    formula = '''=IF(F355>0,F355/D355,"")'''
    @eval_fn
    def E355():
        f355_1 = OLD_Input_EIA_Jet_Fuel_Price.F355()
        var_1 = greaterthan(f355_1, 0)
        f355_2 = OLD_Input_EIA_Jet_Fuel_Price.F355()
        d355_1 = OLD_Input_EIA_Jet_Fuel_Price.D355()
        var_2 = divide(f355_2, d355_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class F355():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!F355
    value = 3.069

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A356():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A356
    value = 41548
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B356():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B356
    value = 3.3865479086
    formula = "=D356*$B$3"
    @eval_fn
    def B356():
        d356_1 = OLD_Input_EIA_Jet_Fuel_Price.D356()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d356_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C356():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C356
    value = 41562
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D356():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D356
    value = 2.885

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E356():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E356
    value = None
    formula = '''=IF(F356>0,F356/D356,"")'''
    @eval_fn
    def E356():
        f356_1 = OLD_Input_EIA_Jet_Fuel_Price.F356()
        var_1 = greaterthan(f356_1, 0)
        f356_2 = OLD_Input_EIA_Jet_Fuel_Price.F356()
        d356_1 = OLD_Input_EIA_Jet_Fuel_Price.D356()
        var_2 = divide(f356_2, d356_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A357():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A357
    value = 41579
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B357():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B357
    value = 3.32198633669
    formula = "=D357*$B$3"
    @eval_fn
    def B357():
        d357_1 = OLD_Input_EIA_Jet_Fuel_Price.D357()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d357_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C357():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C357
    value = 41593
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D357():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D357
    value = 2.83

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E357():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E357
    value = None
    formula = '''=IF(F357>0,F357/D357,"")'''
    @eval_fn
    def E357():
        f357_1 = OLD_Input_EIA_Jet_Fuel_Price.F357()
        var_1 = greaterthan(f357_1, 0)
        f357_2 = OLD_Input_EIA_Jet_Fuel_Price.F357()
        d357_1 = OLD_Input_EIA_Jet_Fuel_Price.D357()
        var_2 = divide(f357_2, d357_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A358():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A358
    value = 41609
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B358():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B358
    value = 3.46871718195
    formula = "=D358*$B$3"
    @eval_fn
    def B358():
        d358_1 = OLD_Input_EIA_Jet_Fuel_Price.D358()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d358_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C358():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C358
    value = 41623
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D358():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D358
    value = 2.955

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E358():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E358
    value = None
    formula = '''=IF(F358>0,F358/D358,"")'''
    @eval_fn
    def E358():
        f358_1 = OLD_Input_EIA_Jet_Fuel_Price.F358()
        var_1 = greaterthan(f358_1, 0)
        f358_2 = OLD_Input_EIA_Jet_Fuel_Price.F358()
        d358_1 = OLD_Input_EIA_Jet_Fuel_Price.D358()
        var_2 = divide(f358_2, d358_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A359():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A359
    value = 41640
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B359():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B359
    value = 3.42880639204
    formula = "=D359*$B$3"
    @eval_fn
    def B359():
        d359_1 = OLD_Input_EIA_Jet_Fuel_Price.D359()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d359_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C359():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C359
    value = 41654
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D359():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D359
    value = 2.921

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E359():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E359
    value = None
    formula = '''=IF(F359>0,F359/D359,"")'''
    @eval_fn
    def E359():
        f359_1 = OLD_Input_EIA_Jet_Fuel_Price.F359()
        var_1 = greaterthan(f359_1, 0)
        f359_2 = OLD_Input_EIA_Jet_Fuel_Price.F359()
        d359_1 = OLD_Input_EIA_Jet_Fuel_Price.D359()
        var_2 = divide(f359_2, d359_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A360():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A360
    value = 41671
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B360():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B360
    value = 3.48045564957
    formula = "=D360*$B$3"
    @eval_fn
    def B360():
        d360_1 = OLD_Input_EIA_Jet_Fuel_Price.D360()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d360_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C360():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C360
    value = 41685
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D360():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D360
    value = 2.965

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E360():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E360
    value = None
    formula = '''=IF(F360>0,F360/D360,"")'''
    @eval_fn
    def E360():
        f360_1 = OLD_Input_EIA_Jet_Fuel_Price.F360()
        var_1 = greaterthan(f360_1, 0)
        f360_2 = OLD_Input_EIA_Jet_Fuel_Price.F360()
        d360_1 = OLD_Input_EIA_Jet_Fuel_Price.D360()
        var_2 = divide(f360_2, d360_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A361():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A361
    value = 41699
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B361():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B361
    value = 3.39241714242
    formula = "=D361*$B$3"
    @eval_fn
    def B361():
        d361_1 = OLD_Input_EIA_Jet_Fuel_Price.D361()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d361_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C361():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C361
    value = 41713
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D361():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D361
    value = 2.89

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E361():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E361
    value = None
    formula = '''=IF(F361>0,F361/D361,"")'''
    @eval_fn
    def E361():
        f361_1 = OLD_Input_EIA_Jet_Fuel_Price.F361()
        var_1 = greaterthan(f361_1, 0)
        f361_2 = OLD_Input_EIA_Jet_Fuel_Price.F361()
        d361_1 = OLD_Input_EIA_Jet_Fuel_Price.D361()
        var_2 = divide(f361_2, d361_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A362():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A362
    value = 41730
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B362():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B362
    value = 3.39006944889
    formula = "=D362*$B$3"
    @eval_fn
    def B362():
        d362_1 = OLD_Input_EIA_Jet_Fuel_Price.D362()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d362_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C362():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C362
    value = 41744
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D362():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D362
    value = 2.888

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E362():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E362
    value = None
    formula = '''=IF(F362>0,F362/D362,"")'''
    @eval_fn
    def E362():
        f362_1 = OLD_Input_EIA_Jet_Fuel_Price.F362()
        var_1 = greaterthan(f362_1, 0)
        f362_2 = OLD_Input_EIA_Jet_Fuel_Price.F362()
        d362_1 = OLD_Input_EIA_Jet_Fuel_Price.D362()
        var_2 = divide(f362_2, d362_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A363():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A363
    value = 41760
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B363():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B363
    value = 3.36659251365
    formula = "=D363*$B$3"
    @eval_fn
    def B363():
        d363_1 = OLD_Input_EIA_Jet_Fuel_Price.D363()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d363_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C363():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C363
    value = 41774
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D363():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D363
    value = 2.868

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E363():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E363
    value = None
    formula = '''=IF(F363>0,F363/D363,"")'''
    @eval_fn
    def E363():
        f363_1 = OLD_Input_EIA_Jet_Fuel_Price.F363()
        var_1 = greaterthan(f363_1, 0)
        f363_2 = OLD_Input_EIA_Jet_Fuel_Price.F363()
        d363_1 = OLD_Input_EIA_Jet_Fuel_Price.D363()
        var_2 = divide(f363_2, d363_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A364():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A364
    value = 41791
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B364():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B364
    value = 3.38420021508
    formula = "=D364*$B$3"
    @eval_fn
    def B364():
        d364_1 = OLD_Input_EIA_Jet_Fuel_Price.D364()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d364_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C364():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C364
    value = 41805
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D364():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D364
    value = 2.883

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E364():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E364
    value = None
    formula = '''=IF(F364>0,F364/D364,"")'''
    @eval_fn
    def E364():
        f364_1 = OLD_Input_EIA_Jet_Fuel_Price.F364()
        var_1 = greaterthan(f364_1, 0)
        f364_2 = OLD_Input_EIA_Jet_Fuel_Price.F364()
        d364_1 = OLD_Input_EIA_Jet_Fuel_Price.D364()
        var_2 = divide(f364_2, d364_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A365():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A365
    value = 41821
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B365():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B365
    value = 3.30672632878
    formula = "=D365*$B$3"
    @eval_fn
    def B365():
        d365_1 = OLD_Input_EIA_Jet_Fuel_Price.D365()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d365_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C365():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C365
    value = 41835
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D365():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D365
    value = 2.817

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E365():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E365
    value = None
    formula = '''=IF(F365>0,F365/D365,"")'''
    @eval_fn
    def E365():
        f365_1 = OLD_Input_EIA_Jet_Fuel_Price.F365()
        var_1 = greaterthan(f365_1, 0)
        f365_2 = OLD_Input_EIA_Jet_Fuel_Price.F365()
        d365_1 = OLD_Input_EIA_Jet_Fuel_Price.D365()
        var_2 = divide(f365_2, d365_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A366():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A366
    value = 41852
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B366():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B366
    value = 3.33255095755
    formula = "=D366*$B$3"
    @eval_fn
    def B366():
        d366_1 = OLD_Input_EIA_Jet_Fuel_Price.D366()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d366_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C366():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C366
    value = 41866
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D366():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D366
    value = 2.839

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E366():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E366
    value = None
    formula = '''=IF(F366>0,F366/D366,"")'''
    @eval_fn
    def E366():
        f366_1 = OLD_Input_EIA_Jet_Fuel_Price.F366()
        var_1 = greaterthan(f366_1, 0)
        f366_2 = OLD_Input_EIA_Jet_Fuel_Price.F366()
        d366_1 = OLD_Input_EIA_Jet_Fuel_Price.D366()
        var_2 = divide(f366_2, d366_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A367():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A367
    value = 41883
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B367():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B367
    value = 3.20342781372
    formula = "=D367*$B$3"
    @eval_fn
    def B367():
        d367_1 = OLD_Input_EIA_Jet_Fuel_Price.D367()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d367_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C367():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C367
    value = 41897
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D367():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D367
    value = 2.729

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E367():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E367
    value = None
    formula = '''=IF(F367>0,F367/D367,"")'''
    @eval_fn
    def E367():
        f367_1 = OLD_Input_EIA_Jet_Fuel_Price.F367()
        var_1 = greaterthan(f367_1, 0)
        f367_2 = OLD_Input_EIA_Jet_Fuel_Price.F367()
        d367_1 = OLD_Input_EIA_Jet_Fuel_Price.D367()
        var_2 = divide(f367_2, d367_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A368():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A368
    value = 41913
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B368():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B368
    value = 2.88766303472
    formula = "=D368*$B$3"
    @eval_fn
    def B368():
        d368_1 = OLD_Input_EIA_Jet_Fuel_Price.D368()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d368_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C368():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C368
    value = 41927
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D368():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D368
    value = 2.46

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E368():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E368
    value = None
    formula = '''=IF(F368>0,F368/D368,"")'''
    @eval_fn
    def E368():
        f368_1 = OLD_Input_EIA_Jet_Fuel_Price.F368()
        var_1 = greaterthan(f368_1, 0)
        f368_2 = OLD_Input_EIA_Jet_Fuel_Price.F368()
        d368_1 = OLD_Input_EIA_Jet_Fuel_Price.D368()
        var_2 = divide(f368_2, d368_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A369():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A369
    value = 41944
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B369():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B369
    value = 2.6963260125
    formula = "=D369*$B$3"
    @eval_fn
    def B369():
        d369_1 = OLD_Input_EIA_Jet_Fuel_Price.D369()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d369_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C369():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C369
    value = 41958
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D369():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D369
    value = 2.297

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E369():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E369
    value = None
    formula = '''=IF(F369>0,F369/D369,"")'''
    @eval_fn
    def E369():
        f369_1 = OLD_Input_EIA_Jet_Fuel_Price.F369()
        var_1 = greaterthan(f369_1, 0)
        f369_2 = OLD_Input_EIA_Jet_Fuel_Price.F369()
        d369_1 = OLD_Input_EIA_Jet_Fuel_Price.D369()
        var_2 = divide(f369_2, d369_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A370():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A370
    value = 41974
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B370():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B370
    value = 2.11409801851
    formula = "=D370*$B$3"
    @eval_fn
    def B370():
        d370_1 = OLD_Input_EIA_Jet_Fuel_Price.D370()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d370_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C370():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C370
    value = 41988
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D370():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D370
    value = 1.801

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E370():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E370
    value = None
    formula = '''=IF(F370>0,F370/D370,"")'''
    @eval_fn
    def E370():
        f370_1 = OLD_Input_EIA_Jet_Fuel_Price.F370()
        var_1 = greaterthan(f370_1, 0)
        f370_2 = OLD_Input_EIA_Jet_Fuel_Price.F370()
        d370_1 = OLD_Input_EIA_Jet_Fuel_Price.D370()
        var_2 = divide(f370_2, d370_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A371():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A371
    value = 42005
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B371():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B371
    value = 1.75607475607
    formula = "=D371*$B$3"
    @eval_fn
    def B371():
        d371_1 = OLD_Input_EIA_Jet_Fuel_Price.D371()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d371_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C371():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C371
    value = 42019
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D371():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D371
    value = 1.496

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E371():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E371
    value = None
    formula = '''=IF(F371>0,F371/D371,"")'''
    @eval_fn
    def E371():
        f371_1 = OLD_Input_EIA_Jet_Fuel_Price.F371()
        var_1 = greaterthan(f371_1, 0)
        f371_2 = OLD_Input_EIA_Jet_Fuel_Price.F371()
        d371_1 = OLD_Input_EIA_Jet_Fuel_Price.D371()
        var_2 = divide(f371_2, d371_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A372():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A372
    value = 42036
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B372():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B372
    value = 2.07301338184
    formula = "=D372*$B$3"
    @eval_fn
    def B372():
        d372_1 = OLD_Input_EIA_Jet_Fuel_Price.D372()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d372_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C372():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C372
    value = 42050
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D372():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D372
    value = 1.766

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E372():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E372
    value = None
    formula = '''=IF(F372>0,F372/D372,"")'''
    @eval_fn
    def E372():
        f372_1 = OLD_Input_EIA_Jet_Fuel_Price.F372()
        var_1 = greaterthan(f372_1, 0)
        f372_2 = OLD_Input_EIA_Jet_Fuel_Price.F372()
        d372_1 = OLD_Input_EIA_Jet_Fuel_Price.D372()
        var_2 = divide(f372_2, d372_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A373():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A373
    value = 42064
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B373():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B373
    value = 1.91219637543
    formula = "=D373*$B$3"
    @eval_fn
    def B373():
        d373_1 = OLD_Input_EIA_Jet_Fuel_Price.D373()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d373_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C373():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C373
    value = 42078
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D373():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D373
    value = 1.629

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E373():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E373
    value = None
    formula = '''=IF(F373>0,F373/D373,"")'''
    @eval_fn
    def E373():
        f373_1 = OLD_Input_EIA_Jet_Fuel_Price.F373()
        var_1 = greaterthan(f373_1, 0)
        f373_2 = OLD_Input_EIA_Jet_Fuel_Price.F373()
        d373_1 = OLD_Input_EIA_Jet_Fuel_Price.D373()
        var_2 = divide(f373_2, d373_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A374():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A374
    value = 42095
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B374():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B374
    value = 1.99788718906
    formula = "=D374*$B$3"
    @eval_fn
    def B374():
        d374_1 = OLD_Input_EIA_Jet_Fuel_Price.D374()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d374_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C374():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C374
    value = 42109
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D374():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D374
    value = 1.702

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E374():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E374
    value = None
    formula = '''=IF(F374>0,F374/D374,"")'''
    @eval_fn
    def E374():
        f374_1 = OLD_Input_EIA_Jet_Fuel_Price.F374()
        var_1 = greaterthan(f374_1, 0)
        f374_2 = OLD_Input_EIA_Jet_Fuel_Price.F374()
        d374_1 = OLD_Input_EIA_Jet_Fuel_Price.D374()
        var_2 = divide(f374_2, d374_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A375():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A375
    value = 42125
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B375():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B375
    value = 2.17044266309
    formula = "=D375*$B$3"
    @eval_fn
    def B375():
        d375_1 = OLD_Input_EIA_Jet_Fuel_Price.D375()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d375_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C375():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C375
    value = 42139
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D375():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D375
    value = 1.849

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E375():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E375
    value = None
    formula = '''=IF(F375>0,F375/D375,"")'''
    @eval_fn
    def E375():
        f375_1 = OLD_Input_EIA_Jet_Fuel_Price.F375()
        var_1 = greaterthan(f375_1, 0)
        f375_2 = OLD_Input_EIA_Jet_Fuel_Price.F375()
        d375_1 = OLD_Input_EIA_Jet_Fuel_Price.D375()
        var_2 = divide(f375_2, d375_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A376():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A376
    value = 42156
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B376():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B376
    value = 2.03310259193
    formula = "=D376*$B$3"
    @eval_fn
    def B376():
        d376_1 = OLD_Input_EIA_Jet_Fuel_Price.D376()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d376_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C376():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C376
    value = 42170
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D376():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D376
    value = 1.732

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E376():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E376
    value = None
    formula = '''=IF(F376>0,F376/D376,"")'''
    @eval_fn
    def E376():
        f376_1 = OLD_Input_EIA_Jet_Fuel_Price.F376()
        var_1 = greaterthan(f376_1, 0)
        f376_2 = OLD_Input_EIA_Jet_Fuel_Price.F376()
        d376_1 = OLD_Input_EIA_Jet_Fuel_Price.D376()
        var_2 = divide(f376_2, d376_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A377():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A377
    value = 42186
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B377():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B377
    value = 1.81828863446
    formula = "=D377*$B$3"
    @eval_fn
    def B377():
        d377_1 = OLD_Input_EIA_Jet_Fuel_Price.D377()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d377_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C377():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C377
    value = 42200
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D377():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D377
    value = 1.549

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E377():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E377
    value = None
    formula = '''=IF(F377>0,F377/D377,"")'''
    @eval_fn
    def E377():
        f377_1 = OLD_Input_EIA_Jet_Fuel_Price.F377()
        var_1 = greaterthan(f377_1, 0)
        f377_2 = OLD_Input_EIA_Jet_Fuel_Price.F377()
        d377_1 = OLD_Input_EIA_Jet_Fuel_Price.D377()
        var_2 = divide(f377_2, d377_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A378():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A378
    value = 42217
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B378():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B378
    value = 1.63047315253
    formula = "=D378*$B$3"
    @eval_fn
    def B378():
        d378_1 = OLD_Input_EIA_Jet_Fuel_Price.D378()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d378_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C378():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C378
    value = 42231
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D378():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D378
    value = 1.389

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E378():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E378
    value = None
    formula = '''=IF(F378>0,F378/D378,"")'''
    @eval_fn
    def E378():
        f378_1 = OLD_Input_EIA_Jet_Fuel_Price.F378()
        var_1 = greaterthan(f378_1, 0)
        f378_2 = OLD_Input_EIA_Jet_Fuel_Price.F378()
        d378_1 = OLD_Input_EIA_Jet_Fuel_Price.D378()
        var_2 = divide(f378_2, d378_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A379():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A379
    value = 42248
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B379():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B379
    value = 1.6375162331
    formula = "=D379*$B$3"
    @eval_fn
    def B379():
        d379_1 = OLD_Input_EIA_Jet_Fuel_Price.D379()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d379_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C379():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C379
    value = 42262
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D379():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D379
    value = 1.395

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E379():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E379
    value = None
    formula = '''=IF(F379>0,F379/D379,"")'''
    @eval_fn
    def E379():
        f379_1 = OLD_Input_EIA_Jet_Fuel_Price.F379()
        var_1 = greaterthan(f379_1, 0)
        f379_2 = OLD_Input_EIA_Jet_Fuel_Price.F379()
        d379_1 = OLD_Input_EIA_Jet_Fuel_Price.D379()
        var_2 = divide(f379_2, d379_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A380():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A380
    value = 42278
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B380():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B380
    value = 1.63282084606
    formula = "=D380*$B$3"
    @eval_fn
    def B380():
        d380_1 = OLD_Input_EIA_Jet_Fuel_Price.D380()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d380_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C380():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C380
    value = 42292
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D380():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D380
    value = 1.391

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E380():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E380
    value = None
    formula = '''=IF(F380>0,F380/D380,"")'''
    @eval_fn
    def E380():
        f380_1 = OLD_Input_EIA_Jet_Fuel_Price.F380()
        var_1 = greaterthan(f380_1, 0)
        f380_2 = OLD_Input_EIA_Jet_Fuel_Price.F380()
        d380_1 = OLD_Input_EIA_Jet_Fuel_Price.D380()
        var_2 = divide(f380_2, d380_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A381():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A381
    value = 42309
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B381():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B381
    value = 1.55652080652
    formula = "=D381*$B$3"
    @eval_fn
    def B381():
        d381_1 = OLD_Input_EIA_Jet_Fuel_Price.D381()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d381_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C381():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C381
    value = 42323
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D381():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D381
    value = 1.326

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E381():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E381
    value = None
    formula = '''=IF(F381>0,F381/D381,"")'''
    @eval_fn
    def E381():
        f381_1 = OLD_Input_EIA_Jet_Fuel_Price.F381()
        var_1 = greaterthan(f381_1, 0)
        f381_2 = OLD_Input_EIA_Jet_Fuel_Price.F381()
        d381_1 = OLD_Input_EIA_Jet_Fuel_Price.D381()
        var_2 = divide(f381_2, d381_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A382():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A382
    value = 42339
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B382():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B382
    value = 1.27010219657
    formula = "=D382*$B$3"
    @eval_fn
    def B382():
        d382_1 = OLD_Input_EIA_Jet_Fuel_Price.D382()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d382_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C382():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C382
    value = 42353
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D382():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D382
    value = 1.082

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E382():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E382
    value = None
    formula = '''=IF(F382>0,F382/D382,"")'''
    @eval_fn
    def E382():
        f382_1 = OLD_Input_EIA_Jet_Fuel_Price.F382()
        var_1 = greaterthan(f382_1, 0)
        f382_2 = OLD_Input_EIA_Jet_Fuel_Price.F382()
        d382_1 = OLD_Input_EIA_Jet_Fuel_Price.D382()
        var_2 = divide(f382_2, d382_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A383():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A383
    value = 42370
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B383():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B383
    value = 1.09167748874
    formula = "=D383*$B$3"
    @eval_fn
    def B383():
        d383_1 = OLD_Input_EIA_Jet_Fuel_Price.D383()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d383_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C383():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C383
    value = 42384
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class D383():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!D383
    value = 0.93

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E383():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E383
    value = None
    formula = '''=IF(F383>0,F383/D383,"")'''
    @eval_fn
    def E383():
        f383_1 = OLD_Input_EIA_Jet_Fuel_Price.F383()
        var_1 = greaterthan(f383_1, 0)
        f383_2 = OLD_Input_EIA_Jet_Fuel_Price.F383()
        d383_1 = OLD_Input_EIA_Jet_Fuel_Price.D383()
        var_2 = divide(f383_2, d383_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A384():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A384
    value = 42401
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B384():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B384
    value = 0
    formula = "=D384*$B$3"
    @eval_fn
    def B384():
        d384_1 = OLD_Input_EIA_Jet_Fuel_Price.D384()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d384_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C384():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C384
    value = 42415
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E384():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E384
    value = None
    formula = '''=IF(F384>0,F384/D384,"")'''
    @eval_fn
    def E384():
        f384_1 = OLD_Input_EIA_Jet_Fuel_Price.F384()
        var_1 = greaterthan(f384_1, 0)
        f384_2 = OLD_Input_EIA_Jet_Fuel_Price.F384()
        d384_1 = OLD_Input_EIA_Jet_Fuel_Price.D384()
        var_2 = divide(f384_2, d384_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A385():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A385
    value = 42430
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B385():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B385
    value = 0
    formula = "=D385*$B$3"
    @eval_fn
    def B385():
        d385_1 = OLD_Input_EIA_Jet_Fuel_Price.D385()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d385_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C385():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C385
    value = 42444
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E385():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E385
    value = None
    formula = '''=IF(F385>0,F385/D385,"")'''
    @eval_fn
    def E385():
        f385_1 = OLD_Input_EIA_Jet_Fuel_Price.F385()
        var_1 = greaterthan(f385_1, 0)
        f385_2 = OLD_Input_EIA_Jet_Fuel_Price.F385()
        d385_1 = OLD_Input_EIA_Jet_Fuel_Price.D385()
        var_2 = divide(f385_2, d385_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A386():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A386
    value = 42461
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B386():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B386
    value = 0
    formula = "=D386*$B$3"
    @eval_fn
    def B386():
        d386_1 = OLD_Input_EIA_Jet_Fuel_Price.D386()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d386_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C386():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C386
    value = 42475
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E386():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E386
    value = None
    formula = '''=IF(F386>0,F386/D386,"")'''
    @eval_fn
    def E386():
        f386_1 = OLD_Input_EIA_Jet_Fuel_Price.F386()
        var_1 = greaterthan(f386_1, 0)
        f386_2 = OLD_Input_EIA_Jet_Fuel_Price.F386()
        d386_1 = OLD_Input_EIA_Jet_Fuel_Price.D386()
        var_2 = divide(f386_2, d386_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A387():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A387
    value = 42491
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B387():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B387
    value = 0
    formula = "=D387*$B$3"
    @eval_fn
    def B387():
        d387_1 = OLD_Input_EIA_Jet_Fuel_Price.D387()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d387_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C387():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C387
    value = 42505
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E387():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E387
    value = None
    formula = '''=IF(F387>0,F387/D387,"")'''
    @eval_fn
    def E387():
        f387_1 = OLD_Input_EIA_Jet_Fuel_Price.F387()
        var_1 = greaterthan(f387_1, 0)
        f387_2 = OLD_Input_EIA_Jet_Fuel_Price.F387()
        d387_1 = OLD_Input_EIA_Jet_Fuel_Price.D387()
        var_2 = divide(f387_2, d387_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A388():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A388
    value = 42522
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B388():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B388
    value = 0
    formula = "=D388*$B$3"
    @eval_fn
    def B388():
        d388_1 = OLD_Input_EIA_Jet_Fuel_Price.D388()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d388_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C388():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C388
    value = 42536
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E388():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E388
    value = None
    formula = '''=IF(F388>0,F388/D388,"")'''
    @eval_fn
    def E388():
        f388_1 = OLD_Input_EIA_Jet_Fuel_Price.F388()
        var_1 = greaterthan(f388_1, 0)
        f388_2 = OLD_Input_EIA_Jet_Fuel_Price.F388()
        d388_1 = OLD_Input_EIA_Jet_Fuel_Price.D388()
        var_2 = divide(f388_2, d388_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A389():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A389
    value = 42552
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B389():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B389
    value = 0
    formula = "=D389*$B$3"
    @eval_fn
    def B389():
        d389_1 = OLD_Input_EIA_Jet_Fuel_Price.D389()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d389_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C389():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C389
    value = 42566
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E389():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E389
    value = None
    formula = '''=IF(F389>0,F389/D389,"")'''
    @eval_fn
    def E389():
        f389_1 = OLD_Input_EIA_Jet_Fuel_Price.F389()
        var_1 = greaterthan(f389_1, 0)
        f389_2 = OLD_Input_EIA_Jet_Fuel_Price.F389()
        d389_1 = OLD_Input_EIA_Jet_Fuel_Price.D389()
        var_2 = divide(f389_2, d389_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A390():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A390
    value = 42583
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B390():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B390
    value = 0
    formula = "=D390*$B$3"
    @eval_fn
    def B390():
        d390_1 = OLD_Input_EIA_Jet_Fuel_Price.D390()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d390_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C390():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C390
    value = 42597
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E390():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E390
    value = None
    formula = '''=IF(F390>0,F390/D390,"")'''
    @eval_fn
    def E390():
        f390_1 = OLD_Input_EIA_Jet_Fuel_Price.F390()
        var_1 = greaterthan(f390_1, 0)
        f390_2 = OLD_Input_EIA_Jet_Fuel_Price.F390()
        d390_1 = OLD_Input_EIA_Jet_Fuel_Price.D390()
        var_2 = divide(f390_2, d390_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A391():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A391
    value = 42614
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B391():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B391
    value = 0
    formula = "=D391*$B$3"
    @eval_fn
    def B391():
        d391_1 = OLD_Input_EIA_Jet_Fuel_Price.D391()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d391_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C391():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C391
    value = 42628
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E391():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E391
    value = None
    formula = '''=IF(F391>0,F391/D391,"")'''
    @eval_fn
    def E391():
        f391_1 = OLD_Input_EIA_Jet_Fuel_Price.F391()
        var_1 = greaterthan(f391_1, 0)
        f391_2 = OLD_Input_EIA_Jet_Fuel_Price.F391()
        d391_1 = OLD_Input_EIA_Jet_Fuel_Price.D391()
        var_2 = divide(f391_2, d391_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A392():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A392
    value = 42644
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B392():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B392
    value = 0
    formula = "=D392*$B$3"
    @eval_fn
    def B392():
        d392_1 = OLD_Input_EIA_Jet_Fuel_Price.D392()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d392_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C392():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C392
    value = 42658
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E392():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E392
    value = None
    formula = '''=IF(F392>0,F392/D392,"")'''
    @eval_fn
    def E392():
        f392_1 = OLD_Input_EIA_Jet_Fuel_Price.F392()
        var_1 = greaterthan(f392_1, 0)
        f392_2 = OLD_Input_EIA_Jet_Fuel_Price.F392()
        d392_1 = OLD_Input_EIA_Jet_Fuel_Price.D392()
        var_2 = divide(f392_2, d392_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A393():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A393
    value = 42675
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B393():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B393
    value = 0
    formula = "=D393*$B$3"
    @eval_fn
    def B393():
        d393_1 = OLD_Input_EIA_Jet_Fuel_Price.D393()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d393_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C393():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C393
    value = 42689
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E393():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E393
    value = None
    formula = '''=IF(F393>0,F393/D393,"")'''
    @eval_fn
    def E393():
        f393_1 = OLD_Input_EIA_Jet_Fuel_Price.F393()
        var_1 = greaterthan(f393_1, 0)
        f393_2 = OLD_Input_EIA_Jet_Fuel_Price.F393()
        d393_1 = OLD_Input_EIA_Jet_Fuel_Price.D393()
        var_2 = divide(f393_2, d393_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A394():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A394
    value = 42705
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B394():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B394
    value = 0
    formula = "=D394*$B$3"
    @eval_fn
    def B394():
        d394_1 = OLD_Input_EIA_Jet_Fuel_Price.D394()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d394_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C394():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C394
    value = 42719
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E394():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E394
    value = None
    formula = '''=IF(F394>0,F394/D394,"")'''
    @eval_fn
    def E394():
        f394_1 = OLD_Input_EIA_Jet_Fuel_Price.F394()
        var_1 = greaterthan(f394_1, 0)
        f394_2 = OLD_Input_EIA_Jet_Fuel_Price.F394()
        d394_1 = OLD_Input_EIA_Jet_Fuel_Price.D394()
        var_2 = divide(f394_2, d394_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A395():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A395
    value = 42736
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B395():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B395
    value = 0
    formula = "=D395*$B$3"
    @eval_fn
    def B395():
        d395_1 = OLD_Input_EIA_Jet_Fuel_Price.D395()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d395_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C395():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C395
    value = 42750
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E395():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E395
    value = None
    formula = '''=IF(F395>0,F395/D395,"")'''
    @eval_fn
    def E395():
        f395_1 = OLD_Input_EIA_Jet_Fuel_Price.F395()
        var_1 = greaterthan(f395_1, 0)
        f395_2 = OLD_Input_EIA_Jet_Fuel_Price.F395()
        d395_1 = OLD_Input_EIA_Jet_Fuel_Price.D395()
        var_2 = divide(f395_2, d395_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A396():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A396
    value = 42767
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B396():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B396
    value = 0
    formula = "=D396*$B$3"
    @eval_fn
    def B396():
        d396_1 = OLD_Input_EIA_Jet_Fuel_Price.D396()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d396_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C396():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C396
    value = 42781
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E396():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E396
    value = None
    formula = '''=IF(F396>0,F396/D396,"")'''
    @eval_fn
    def E396():
        f396_1 = OLD_Input_EIA_Jet_Fuel_Price.F396()
        var_1 = greaterthan(f396_1, 0)
        f396_2 = OLD_Input_EIA_Jet_Fuel_Price.F396()
        d396_1 = OLD_Input_EIA_Jet_Fuel_Price.D396()
        var_2 = divide(f396_2, d396_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A397():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A397
    value = 42795
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B397():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B397
    value = 0
    formula = "=D397*$B$3"
    @eval_fn
    def B397():
        d397_1 = OLD_Input_EIA_Jet_Fuel_Price.D397()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d397_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C397():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C397
    value = 42809
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E397():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E397
    value = None
    formula = '''=IF(F397>0,F397/D397,"")'''
    @eval_fn
    def E397():
        f397_1 = OLD_Input_EIA_Jet_Fuel_Price.F397()
        var_1 = greaterthan(f397_1, 0)
        f397_2 = OLD_Input_EIA_Jet_Fuel_Price.F397()
        d397_1 = OLD_Input_EIA_Jet_Fuel_Price.D397()
        var_2 = divide(f397_2, d397_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A398():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A398
    value = 42826
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B398():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B398
    value = 0
    formula = "=D398*$B$3"
    @eval_fn
    def B398():
        d398_1 = OLD_Input_EIA_Jet_Fuel_Price.D398()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d398_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C398():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C398
    value = 42840
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E398():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E398
    value = None
    formula = '''=IF(F398>0,F398/D398,"")'''
    @eval_fn
    def E398():
        f398_1 = OLD_Input_EIA_Jet_Fuel_Price.F398()
        var_1 = greaterthan(f398_1, 0)
        f398_2 = OLD_Input_EIA_Jet_Fuel_Price.F398()
        d398_1 = OLD_Input_EIA_Jet_Fuel_Price.D398()
        var_2 = divide(f398_2, d398_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A399():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A399
    value = 42856
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B399():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B399
    value = 0
    formula = "=D399*$B$3"
    @eval_fn
    def B399():
        d399_1 = OLD_Input_EIA_Jet_Fuel_Price.D399()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d399_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C399():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C399
    value = 42870
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E399():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E399
    value = None
    formula = '''=IF(F399>0,F399/D399,"")'''
    @eval_fn
    def E399():
        f399_1 = OLD_Input_EIA_Jet_Fuel_Price.F399()
        var_1 = greaterthan(f399_1, 0)
        f399_2 = OLD_Input_EIA_Jet_Fuel_Price.F399()
        d399_1 = OLD_Input_EIA_Jet_Fuel_Price.D399()
        var_2 = divide(f399_2, d399_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A400():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A400
    value = 42887
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B400():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B400
    value = 0
    formula = "=D400*$B$3"
    @eval_fn
    def B400():
        d400_1 = OLD_Input_EIA_Jet_Fuel_Price.D400()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d400_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C400():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C400
    value = 42901
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E400():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E400
    value = None
    formula = '''=IF(F400>0,F400/D400,"")'''
    @eval_fn
    def E400():
        f400_1 = OLD_Input_EIA_Jet_Fuel_Price.F400()
        var_1 = greaterthan(f400_1, 0)
        f400_2 = OLD_Input_EIA_Jet_Fuel_Price.F400()
        d400_1 = OLD_Input_EIA_Jet_Fuel_Price.D400()
        var_2 = divide(f400_2, d400_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A401():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A401
    value = 42917
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B401():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B401
    value = 0
    formula = "=D401*$B$3"
    @eval_fn
    def B401():
        d401_1 = OLD_Input_EIA_Jet_Fuel_Price.D401()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d401_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C401():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C401
    value = 42931
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E401():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E401
    value = None
    formula = '''=IF(F401>0,F401/D401,"")'''
    @eval_fn
    def E401():
        f401_1 = OLD_Input_EIA_Jet_Fuel_Price.F401()
        var_1 = greaterthan(f401_1, 0)
        f401_2 = OLD_Input_EIA_Jet_Fuel_Price.F401()
        d401_1 = OLD_Input_EIA_Jet_Fuel_Price.D401()
        var_2 = divide(f401_2, d401_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A402():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A402
    value = 42948
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B402():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B402
    value = 0
    formula = "=D402*$B$3"
    @eval_fn
    def B402():
        d402_1 = OLD_Input_EIA_Jet_Fuel_Price.D402()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d402_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C402():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C402
    value = 42962
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E402():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E402
    value = None
    formula = '''=IF(F402>0,F402/D402,"")'''
    @eval_fn
    def E402():
        f402_1 = OLD_Input_EIA_Jet_Fuel_Price.F402()
        var_1 = greaterthan(f402_1, 0)
        f402_2 = OLD_Input_EIA_Jet_Fuel_Price.F402()
        d402_1 = OLD_Input_EIA_Jet_Fuel_Price.D402()
        var_2 = divide(f402_2, d402_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A403():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A403
    value = 42979
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B403():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B403
    value = 0
    formula = "=D403*$B$3"
    @eval_fn
    def B403():
        d403_1 = OLD_Input_EIA_Jet_Fuel_Price.D403()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d403_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C403():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C403
    value = 42993
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E403():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E403
    value = None
    formula = '''=IF(F403>0,F403/D403,"")'''
    @eval_fn
    def E403():
        f403_1 = OLD_Input_EIA_Jet_Fuel_Price.F403()
        var_1 = greaterthan(f403_1, 0)
        f403_2 = OLD_Input_EIA_Jet_Fuel_Price.F403()
        d403_1 = OLD_Input_EIA_Jet_Fuel_Price.D403()
        var_2 = divide(f403_2, d403_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A404():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A404
    value = 43009
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B404():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B404
    value = 0
    formula = "=D404*$B$3"
    @eval_fn
    def B404():
        d404_1 = OLD_Input_EIA_Jet_Fuel_Price.D404()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d404_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C404():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C404
    value = 43023
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E404():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E404
    value = None
    formula = '''=IF(F404>0,F404/D404,"")'''
    @eval_fn
    def E404():
        f404_1 = OLD_Input_EIA_Jet_Fuel_Price.F404()
        var_1 = greaterthan(f404_1, 0)
        f404_2 = OLD_Input_EIA_Jet_Fuel_Price.F404()
        d404_1 = OLD_Input_EIA_Jet_Fuel_Price.D404()
        var_2 = divide(f404_2, d404_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A405():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A405
    value = 43040
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B405():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B405
    value = 0
    formula = "=D405*$B$3"
    @eval_fn
    def B405():
        d405_1 = OLD_Input_EIA_Jet_Fuel_Price.D405()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d405_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C405():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C405
    value = 43054
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E405():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E405
    value = None
    formula = '''=IF(F405>0,F405/D405,"")'''
    @eval_fn
    def E405():
        f405_1 = OLD_Input_EIA_Jet_Fuel_Price.F405()
        var_1 = greaterthan(f405_1, 0)
        f405_2 = OLD_Input_EIA_Jet_Fuel_Price.F405()
        d405_1 = OLD_Input_EIA_Jet_Fuel_Price.D405()
        var_2 = divide(f405_2, d405_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A406():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A406
    value = 43070
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B406():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B406
    value = 0
    formula = "=D406*$B$3"
    @eval_fn
    def B406():
        d406_1 = OLD_Input_EIA_Jet_Fuel_Price.D406()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d406_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C406():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C406
    value = 43084
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E406():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E406
    value = None
    formula = '''=IF(F406>0,F406/D406,"")'''
    @eval_fn
    def E406():
        f406_1 = OLD_Input_EIA_Jet_Fuel_Price.F406()
        var_1 = greaterthan(f406_1, 0)
        f406_2 = OLD_Input_EIA_Jet_Fuel_Price.F406()
        d406_1 = OLD_Input_EIA_Jet_Fuel_Price.D406()
        var_2 = divide(f406_2, d406_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A407():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A407
    value = 43101
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B407():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B407
    value = 0
    formula = "=D407*$B$3"
    @eval_fn
    def B407():
        d407_1 = OLD_Input_EIA_Jet_Fuel_Price.D407()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d407_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C407():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C407
    value = 43115
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E407():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E407
    value = None
    formula = '''=IF(F407>0,F407/D407,"")'''
    @eval_fn
    def E407():
        f407_1 = OLD_Input_EIA_Jet_Fuel_Price.F407()
        var_1 = greaterthan(f407_1, 0)
        f407_2 = OLD_Input_EIA_Jet_Fuel_Price.F407()
        d407_1 = OLD_Input_EIA_Jet_Fuel_Price.D407()
        var_2 = divide(f407_2, d407_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A408():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A408
    value = 43132
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B408():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B408
    value = 0
    formula = "=D408*$B$3"
    @eval_fn
    def B408():
        d408_1 = OLD_Input_EIA_Jet_Fuel_Price.D408()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d408_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C408():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C408
    value = 43146
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E408():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E408
    value = None
    formula = '''=IF(F408>0,F408/D408,"")'''
    @eval_fn
    def E408():
        f408_1 = OLD_Input_EIA_Jet_Fuel_Price.F408()
        var_1 = greaterthan(f408_1, 0)
        f408_2 = OLD_Input_EIA_Jet_Fuel_Price.F408()
        d408_1 = OLD_Input_EIA_Jet_Fuel_Price.D408()
        var_2 = divide(f408_2, d408_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A409():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A409
    value = 43160
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B409():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B409
    value = 0
    formula = "=D409*$B$3"
    @eval_fn
    def B409():
        d409_1 = OLD_Input_EIA_Jet_Fuel_Price.D409()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d409_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C409():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C409
    value = 43174
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E409():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E409
    value = None
    formula = '''=IF(F409>0,F409/D409,"")'''
    @eval_fn
    def E409():
        f409_1 = OLD_Input_EIA_Jet_Fuel_Price.F409()
        var_1 = greaterthan(f409_1, 0)
        f409_2 = OLD_Input_EIA_Jet_Fuel_Price.F409()
        d409_1 = OLD_Input_EIA_Jet_Fuel_Price.D409()
        var_2 = divide(f409_2, d409_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A410():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A410
    value = 43191
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B410():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B410
    value = 0
    formula = "=D410*$B$3"
    @eval_fn
    def B410():
        d410_1 = OLD_Input_EIA_Jet_Fuel_Price.D410()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d410_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C410():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C410
    value = 43205
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E410():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E410
    value = None
    formula = '''=IF(F410>0,F410/D410,"")'''
    @eval_fn
    def E410():
        f410_1 = OLD_Input_EIA_Jet_Fuel_Price.F410()
        var_1 = greaterthan(f410_1, 0)
        f410_2 = OLD_Input_EIA_Jet_Fuel_Price.F410()
        d410_1 = OLD_Input_EIA_Jet_Fuel_Price.D410()
        var_2 = divide(f410_2, d410_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A411():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A411
    value = 43221
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B411():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B411
    value = 0
    formula = "=D411*$B$3"
    @eval_fn
    def B411():
        d411_1 = OLD_Input_EIA_Jet_Fuel_Price.D411()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d411_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C411():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C411
    value = 43235
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E411():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E411
    value = None
    formula = '''=IF(F411>0,F411/D411,"")'''
    @eval_fn
    def E411():
        f411_1 = OLD_Input_EIA_Jet_Fuel_Price.F411()
        var_1 = greaterthan(f411_1, 0)
        f411_2 = OLD_Input_EIA_Jet_Fuel_Price.F411()
        d411_1 = OLD_Input_EIA_Jet_Fuel_Price.D411()
        var_2 = divide(f411_2, d411_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A412():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A412
    value = 43252
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B412():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B412
    value = 0
    formula = "=D412*$B$3"
    @eval_fn
    def B412():
        d412_1 = OLD_Input_EIA_Jet_Fuel_Price.D412()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d412_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C412():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C412
    value = 43266
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E412():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E412
    value = None
    formula = '''=IF(F412>0,F412/D412,"")'''
    @eval_fn
    def E412():
        f412_1 = OLD_Input_EIA_Jet_Fuel_Price.F412()
        var_1 = greaterthan(f412_1, 0)
        f412_2 = OLD_Input_EIA_Jet_Fuel_Price.F412()
        d412_1 = OLD_Input_EIA_Jet_Fuel_Price.D412()
        var_2 = divide(f412_2, d412_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A413():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A413
    value = 43282
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B413():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B413
    value = 0
    formula = "=D413*$B$3"
    @eval_fn
    def B413():
        d413_1 = OLD_Input_EIA_Jet_Fuel_Price.D413()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d413_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C413():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C413
    value = 43296
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E413():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E413
    value = None
    formula = '''=IF(F413>0,F413/D413,"")'''
    @eval_fn
    def E413():
        f413_1 = OLD_Input_EIA_Jet_Fuel_Price.F413()
        var_1 = greaterthan(f413_1, 0)
        f413_2 = OLD_Input_EIA_Jet_Fuel_Price.F413()
        d413_1 = OLD_Input_EIA_Jet_Fuel_Price.D413()
        var_2 = divide(f413_2, d413_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A414():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A414
    value = 43313
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B414():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B414
    value = 0
    formula = "=D414*$B$3"
    @eval_fn
    def B414():
        d414_1 = OLD_Input_EIA_Jet_Fuel_Price.D414()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d414_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C414():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C414
    value = 43327
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E414():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E414
    value = None
    formula = '''=IF(F414>0,F414/D414,"")'''
    @eval_fn
    def E414():
        f414_1 = OLD_Input_EIA_Jet_Fuel_Price.F414()
        var_1 = greaterthan(f414_1, 0)
        f414_2 = OLD_Input_EIA_Jet_Fuel_Price.F414()
        d414_1 = OLD_Input_EIA_Jet_Fuel_Price.D414()
        var_2 = divide(f414_2, d414_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A415():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A415
    value = 43344
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B415():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B415
    value = 0
    formula = "=D415*$B$3"
    @eval_fn
    def B415():
        d415_1 = OLD_Input_EIA_Jet_Fuel_Price.D415()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d415_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C415():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C415
    value = 43358
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E415():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E415
    value = None
    formula = '''=IF(F415>0,F415/D415,"")'''
    @eval_fn
    def E415():
        f415_1 = OLD_Input_EIA_Jet_Fuel_Price.F415()
        var_1 = greaterthan(f415_1, 0)
        f415_2 = OLD_Input_EIA_Jet_Fuel_Price.F415()
        d415_1 = OLD_Input_EIA_Jet_Fuel_Price.D415()
        var_2 = divide(f415_2, d415_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A416():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A416
    value = 43374
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B416():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B416
    value = 0
    formula = "=D416*$B$3"
    @eval_fn
    def B416():
        d416_1 = OLD_Input_EIA_Jet_Fuel_Price.D416()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d416_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C416():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C416
    value = 43388
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E416():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E416
    value = None
    formula = '''=IF(F416>0,F416/D416,"")'''
    @eval_fn
    def E416():
        f416_1 = OLD_Input_EIA_Jet_Fuel_Price.F416()
        var_1 = greaterthan(f416_1, 0)
        f416_2 = OLD_Input_EIA_Jet_Fuel_Price.F416()
        d416_1 = OLD_Input_EIA_Jet_Fuel_Price.D416()
        var_2 = divide(f416_2, d416_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A417():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A417
    value = 43405
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B417():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B417
    value = 0
    formula = "=D417*$B$3"
    @eval_fn
    def B417():
        d417_1 = OLD_Input_EIA_Jet_Fuel_Price.D417()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d417_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C417():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C417
    value = 43419
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E417():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E417
    value = None
    formula = '''=IF(F417>0,F417/D417,"")'''
    @eval_fn
    def E417():
        f417_1 = OLD_Input_EIA_Jet_Fuel_Price.F417()
        var_1 = greaterthan(f417_1, 0)
        f417_2 = OLD_Input_EIA_Jet_Fuel_Price.F417()
        d417_1 = OLD_Input_EIA_Jet_Fuel_Price.D417()
        var_2 = divide(f417_2, d417_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A418():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A418
    value = 43435
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B418():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B418
    value = 0
    formula = "=D418*$B$3"
    @eval_fn
    def B418():
        d418_1 = OLD_Input_EIA_Jet_Fuel_Price.D418()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d418_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C418():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C418
    value = 43449
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E418():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E418
    value = None
    formula = '''=IF(F418>0,F418/D418,"")'''
    @eval_fn
    def E418():
        f418_1 = OLD_Input_EIA_Jet_Fuel_Price.F418()
        var_1 = greaterthan(f418_1, 0)
        f418_2 = OLD_Input_EIA_Jet_Fuel_Price.F418()
        d418_1 = OLD_Input_EIA_Jet_Fuel_Price.D418()
        var_2 = divide(f418_2, d418_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A419():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A419
    value = 43466
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B419():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B419
    value = 0
    formula = "=D419*$B$3"
    @eval_fn
    def B419():
        d419_1 = OLD_Input_EIA_Jet_Fuel_Price.D419()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d419_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C419():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C419
    value = 43480
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E419():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E419
    value = None
    formula = '''=IF(F419>0,F419/D419,"")'''
    @eval_fn
    def E419():
        f419_1 = OLD_Input_EIA_Jet_Fuel_Price.F419()
        var_1 = greaterthan(f419_1, 0)
        f419_2 = OLD_Input_EIA_Jet_Fuel_Price.F419()
        d419_1 = OLD_Input_EIA_Jet_Fuel_Price.D419()
        var_2 = divide(f419_2, d419_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A420():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A420
    value = 43497
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B420():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B420
    value = 0
    formula = "=D420*$B$3"
    @eval_fn
    def B420():
        d420_1 = OLD_Input_EIA_Jet_Fuel_Price.D420()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d420_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C420():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C420
    value = 43511
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E420():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E420
    value = None
    formula = '''=IF(F420>0,F420/D420,"")'''
    @eval_fn
    def E420():
        f420_1 = OLD_Input_EIA_Jet_Fuel_Price.F420()
        var_1 = greaterthan(f420_1, 0)
        f420_2 = OLD_Input_EIA_Jet_Fuel_Price.F420()
        d420_1 = OLD_Input_EIA_Jet_Fuel_Price.D420()
        var_2 = divide(f420_2, d420_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A421():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A421
    value = 43525
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B421():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B421
    value = 0
    formula = "=D421*$B$3"
    @eval_fn
    def B421():
        d421_1 = OLD_Input_EIA_Jet_Fuel_Price.D421()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d421_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C421():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C421
    value = 43539
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E421():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E421
    value = None
    formula = '''=IF(F421>0,F421/D421,"")'''
    @eval_fn
    def E421():
        f421_1 = OLD_Input_EIA_Jet_Fuel_Price.F421()
        var_1 = greaterthan(f421_1, 0)
        f421_2 = OLD_Input_EIA_Jet_Fuel_Price.F421()
        d421_1 = OLD_Input_EIA_Jet_Fuel_Price.D421()
        var_2 = divide(f421_2, d421_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A422():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A422
    value = 43556
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B422():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B422
    value = 0
    formula = "=D422*$B$3"
    @eval_fn
    def B422():
        d422_1 = OLD_Input_EIA_Jet_Fuel_Price.D422()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d422_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C422():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C422
    value = 43570
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E422():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E422
    value = None
    formula = '''=IF(F422>0,F422/D422,"")'''
    @eval_fn
    def E422():
        f422_1 = OLD_Input_EIA_Jet_Fuel_Price.F422()
        var_1 = greaterthan(f422_1, 0)
        f422_2 = OLD_Input_EIA_Jet_Fuel_Price.F422()
        d422_1 = OLD_Input_EIA_Jet_Fuel_Price.D422()
        var_2 = divide(f422_2, d422_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A423():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A423
    value = 43586
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B423():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B423
    value = 0
    formula = "=D423*$B$3"
    @eval_fn
    def B423():
        d423_1 = OLD_Input_EIA_Jet_Fuel_Price.D423()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d423_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C423():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C423
    value = 43600
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E423():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E423
    value = None
    formula = '''=IF(F423>0,F423/D423,"")'''
    @eval_fn
    def E423():
        f423_1 = OLD_Input_EIA_Jet_Fuel_Price.F423()
        var_1 = greaterthan(f423_1, 0)
        f423_2 = OLD_Input_EIA_Jet_Fuel_Price.F423()
        d423_1 = OLD_Input_EIA_Jet_Fuel_Price.D423()
        var_2 = divide(f423_2, d423_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A424():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A424
    value = 43617
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B424():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B424
    value = 0
    formula = "=D424*$B$3"
    @eval_fn
    def B424():
        d424_1 = OLD_Input_EIA_Jet_Fuel_Price.D424()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d424_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C424():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C424
    value = 43631
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E424():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E424
    value = None
    formula = '''=IF(F424>0,F424/D424,"")'''
    @eval_fn
    def E424():
        f424_1 = OLD_Input_EIA_Jet_Fuel_Price.F424()
        var_1 = greaterthan(f424_1, 0)
        f424_2 = OLD_Input_EIA_Jet_Fuel_Price.F424()
        d424_1 = OLD_Input_EIA_Jet_Fuel_Price.D424()
        var_2 = divide(f424_2, d424_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A425():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A425
    value = 43647
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B425():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B425
    value = 0
    formula = "=D425*$B$3"
    @eval_fn
    def B425():
        d425_1 = OLD_Input_EIA_Jet_Fuel_Price.D425()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d425_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C425():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C425
    value = 43661
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E425():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E425
    value = None
    formula = '''=IF(F425>0,F425/D425,"")'''
    @eval_fn
    def E425():
        f425_1 = OLD_Input_EIA_Jet_Fuel_Price.F425()
        var_1 = greaterthan(f425_1, 0)
        f425_2 = OLD_Input_EIA_Jet_Fuel_Price.F425()
        d425_1 = OLD_Input_EIA_Jet_Fuel_Price.D425()
        var_2 = divide(f425_2, d425_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A426():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A426
    value = 43678
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B426():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B426
    value = 0
    formula = "=D426*$B$3"
    @eval_fn
    def B426():
        d426_1 = OLD_Input_EIA_Jet_Fuel_Price.D426()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d426_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C426():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C426
    value = 43692
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E426():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E426
    value = None
    formula = '''=IF(F426>0,F426/D426,"")'''
    @eval_fn
    def E426():
        f426_1 = OLD_Input_EIA_Jet_Fuel_Price.F426()
        var_1 = greaterthan(f426_1, 0)
        f426_2 = OLD_Input_EIA_Jet_Fuel_Price.F426()
        d426_1 = OLD_Input_EIA_Jet_Fuel_Price.D426()
        var_2 = divide(f426_2, d426_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A427():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A427
    value = 43709
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B427():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B427
    value = 0
    formula = "=D427*$B$3"
    @eval_fn
    def B427():
        d427_1 = OLD_Input_EIA_Jet_Fuel_Price.D427()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d427_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C427():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C427
    value = 43723
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E427():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E427
    value = None
    formula = '''=IF(F427>0,F427/D427,"")'''
    @eval_fn
    def E427():
        f427_1 = OLD_Input_EIA_Jet_Fuel_Price.F427()
        var_1 = greaterthan(f427_1, 0)
        f427_2 = OLD_Input_EIA_Jet_Fuel_Price.F427()
        d427_1 = OLD_Input_EIA_Jet_Fuel_Price.D427()
        var_2 = divide(f427_2, d427_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A428():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A428
    value = 43739
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B428():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B428
    value = 0
    formula = "=D428*$B$3"
    @eval_fn
    def B428():
        d428_1 = OLD_Input_EIA_Jet_Fuel_Price.D428()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d428_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C428():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C428
    value = 43753
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E428():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E428
    value = None
    formula = '''=IF(F428>0,F428/D428,"")'''
    @eval_fn
    def E428():
        f428_1 = OLD_Input_EIA_Jet_Fuel_Price.F428()
        var_1 = greaterthan(f428_1, 0)
        f428_2 = OLD_Input_EIA_Jet_Fuel_Price.F428()
        d428_1 = OLD_Input_EIA_Jet_Fuel_Price.D428()
        var_2 = divide(f428_2, d428_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A429():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A429
    value = 43770
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B429():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B429
    value = 0
    formula = "=D429*$B$3"
    @eval_fn
    def B429():
        d429_1 = OLD_Input_EIA_Jet_Fuel_Price.D429()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d429_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C429():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C429
    value = 43784
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E429():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E429
    value = None
    formula = '''=IF(F429>0,F429/D429,"")'''
    @eval_fn
    def E429():
        f429_1 = OLD_Input_EIA_Jet_Fuel_Price.F429()
        var_1 = greaterthan(f429_1, 0)
        f429_2 = OLD_Input_EIA_Jet_Fuel_Price.F429()
        d429_1 = OLD_Input_EIA_Jet_Fuel_Price.D429()
        var_2 = divide(f429_2, d429_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A430():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A430
    value = 43800
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B430():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B430
    value = 0
    formula = "=D430*$B$3"
    @eval_fn
    def B430():
        d430_1 = OLD_Input_EIA_Jet_Fuel_Price.D430()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d430_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C430():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C430
    value = 43814
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E430():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E430
    value = None
    formula = '''=IF(F430>0,F430/D430,"")'''
    @eval_fn
    def E430():
        f430_1 = OLD_Input_EIA_Jet_Fuel_Price.F430()
        var_1 = greaterthan(f430_1, 0)
        f430_2 = OLD_Input_EIA_Jet_Fuel_Price.F430()
        d430_1 = OLD_Input_EIA_Jet_Fuel_Price.D430()
        var_2 = divide(f430_2, d430_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A431():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A431
    value = 43831
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B431():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B431
    value = 0
    formula = "=D431*$B$3"
    @eval_fn
    def B431():
        d431_1 = OLD_Input_EIA_Jet_Fuel_Price.D431()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d431_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C431():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C431
    value = 43845
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E431():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E431
    value = None
    formula = '''=IF(F431>0,F431/D431,"")'''
    @eval_fn
    def E431():
        f431_1 = OLD_Input_EIA_Jet_Fuel_Price.F431()
        var_1 = greaterthan(f431_1, 0)
        f431_2 = OLD_Input_EIA_Jet_Fuel_Price.F431()
        d431_1 = OLD_Input_EIA_Jet_Fuel_Price.D431()
        var_2 = divide(f431_2, d431_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A432():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A432
    value = 43862
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B432():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B432
    value = 0
    formula = "=D432*$B$3"
    @eval_fn
    def B432():
        d432_1 = OLD_Input_EIA_Jet_Fuel_Price.D432()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d432_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C432():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C432
    value = 43876
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E432():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E432
    value = None
    formula = '''=IF(F432>0,F432/D432,"")'''
    @eval_fn
    def E432():
        f432_1 = OLD_Input_EIA_Jet_Fuel_Price.F432()
        var_1 = greaterthan(f432_1, 0)
        f432_2 = OLD_Input_EIA_Jet_Fuel_Price.F432()
        d432_1 = OLD_Input_EIA_Jet_Fuel_Price.D432()
        var_2 = divide(f432_2, d432_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A433():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A433
    value = 43891
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B433():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B433
    value = 0
    formula = "=D433*$B$3"
    @eval_fn
    def B433():
        d433_1 = OLD_Input_EIA_Jet_Fuel_Price.D433()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d433_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C433():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C433
    value = 43905
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E433():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E433
    value = None
    formula = '''=IF(F433>0,F433/D433,"")'''
    @eval_fn
    def E433():
        f433_1 = OLD_Input_EIA_Jet_Fuel_Price.F433()
        var_1 = greaterthan(f433_1, 0)
        f433_2 = OLD_Input_EIA_Jet_Fuel_Price.F433()
        d433_1 = OLD_Input_EIA_Jet_Fuel_Price.D433()
        var_2 = divide(f433_2, d433_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A434():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A434
    value = 43922
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B434():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B434
    value = 0
    formula = "=D434*$B$3"
    @eval_fn
    def B434():
        d434_1 = OLD_Input_EIA_Jet_Fuel_Price.D434()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d434_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C434():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C434
    value = 43936
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E434():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E434
    value = None
    formula = '''=IF(F434>0,F434/D434,"")'''
    @eval_fn
    def E434():
        f434_1 = OLD_Input_EIA_Jet_Fuel_Price.F434()
        var_1 = greaterthan(f434_1, 0)
        f434_2 = OLD_Input_EIA_Jet_Fuel_Price.F434()
        d434_1 = OLD_Input_EIA_Jet_Fuel_Price.D434()
        var_2 = divide(f434_2, d434_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A435():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A435
    value = 43952
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B435():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B435
    value = 0
    formula = "=D435*$B$3"
    @eval_fn
    def B435():
        d435_1 = OLD_Input_EIA_Jet_Fuel_Price.D435()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d435_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C435():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C435
    value = 43966
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E435():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E435
    value = None
    formula = '''=IF(F435>0,F435/D435,"")'''
    @eval_fn
    def E435():
        f435_1 = OLD_Input_EIA_Jet_Fuel_Price.F435()
        var_1 = greaterthan(f435_1, 0)
        f435_2 = OLD_Input_EIA_Jet_Fuel_Price.F435()
        d435_1 = OLD_Input_EIA_Jet_Fuel_Price.D435()
        var_2 = divide(f435_2, d435_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A436():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A436
    value = 43983
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B436():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B436
    value = 0
    formula = "=D436*$B$3"
    @eval_fn
    def B436():
        d436_1 = OLD_Input_EIA_Jet_Fuel_Price.D436()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d436_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C436():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C436
    value = 43997
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E436():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E436
    value = None
    formula = '''=IF(F436>0,F436/D436,"")'''
    @eval_fn
    def E436():
        f436_1 = OLD_Input_EIA_Jet_Fuel_Price.F436()
        var_1 = greaterthan(f436_1, 0)
        f436_2 = OLD_Input_EIA_Jet_Fuel_Price.F436()
        d436_1 = OLD_Input_EIA_Jet_Fuel_Price.D436()
        var_2 = divide(f436_2, d436_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A437():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A437
    value = 44013
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B437():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B437
    value = 0
    formula = "=D437*$B$3"
    @eval_fn
    def B437():
        d437_1 = OLD_Input_EIA_Jet_Fuel_Price.D437()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d437_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C437():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C437
    value = 44027
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E437():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E437
    value = None
    formula = '''=IF(F437>0,F437/D437,"")'''
    @eval_fn
    def E437():
        f437_1 = OLD_Input_EIA_Jet_Fuel_Price.F437()
        var_1 = greaterthan(f437_1, 0)
        f437_2 = OLD_Input_EIA_Jet_Fuel_Price.F437()
        d437_1 = OLD_Input_EIA_Jet_Fuel_Price.D437()
        var_2 = divide(f437_2, d437_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A438():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A438
    value = 44044
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B438():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B438
    value = 0
    formula = "=D438*$B$3"
    @eval_fn
    def B438():
        d438_1 = OLD_Input_EIA_Jet_Fuel_Price.D438()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d438_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C438():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C438
    value = 44058
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E438():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E438
    value = None
    formula = '''=IF(F438>0,F438/D438,"")'''
    @eval_fn
    def E438():
        f438_1 = OLD_Input_EIA_Jet_Fuel_Price.F438()
        var_1 = greaterthan(f438_1, 0)
        f438_2 = OLD_Input_EIA_Jet_Fuel_Price.F438()
        d438_1 = OLD_Input_EIA_Jet_Fuel_Price.D438()
        var_2 = divide(f438_2, d438_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A439():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A439
    value = 44075
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B439():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B439
    value = 0
    formula = "=D439*$B$3"
    @eval_fn
    def B439():
        d439_1 = OLD_Input_EIA_Jet_Fuel_Price.D439()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d439_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C439():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C439
    value = 44089
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E439():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E439
    value = None
    formula = '''=IF(F439>0,F439/D439,"")'''
    @eval_fn
    def E439():
        f439_1 = OLD_Input_EIA_Jet_Fuel_Price.F439()
        var_1 = greaterthan(f439_1, 0)
        f439_2 = OLD_Input_EIA_Jet_Fuel_Price.F439()
        d439_1 = OLD_Input_EIA_Jet_Fuel_Price.D439()
        var_2 = divide(f439_2, d439_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A440():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A440
    value = 44105
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B440():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B440
    value = 0
    formula = "=D440*$B$3"
    @eval_fn
    def B440():
        d440_1 = OLD_Input_EIA_Jet_Fuel_Price.D440()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d440_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C440():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C440
    value = 44119
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E440():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E440
    value = None
    formula = '''=IF(F440>0,F440/D440,"")'''
    @eval_fn
    def E440():
        f440_1 = OLD_Input_EIA_Jet_Fuel_Price.F440()
        var_1 = greaterthan(f440_1, 0)
        f440_2 = OLD_Input_EIA_Jet_Fuel_Price.F440()
        d440_1 = OLD_Input_EIA_Jet_Fuel_Price.D440()
        var_2 = divide(f440_2, d440_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A441():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A441
    value = 44136
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B441():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B441
    value = 0
    formula = "=D441*$B$3"
    @eval_fn
    def B441():
        d441_1 = OLD_Input_EIA_Jet_Fuel_Price.D441()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d441_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C441():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C441
    value = 44150
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E441():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E441
    value = None
    formula = '''=IF(F441>0,F441/D441,"")'''
    @eval_fn
    def E441():
        f441_1 = OLD_Input_EIA_Jet_Fuel_Price.F441()
        var_1 = greaterthan(f441_1, 0)
        f441_2 = OLD_Input_EIA_Jet_Fuel_Price.F441()
        d441_1 = OLD_Input_EIA_Jet_Fuel_Price.D441()
        var_2 = divide(f441_2, d441_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A442():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A442
    value = 44166
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B442():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B442
    value = 0
    formula = "=D442*$B$3"
    @eval_fn
    def B442():
        d442_1 = OLD_Input_EIA_Jet_Fuel_Price.D442()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d442_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C442():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C442
    value = 44180
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E442():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E442
    value = None
    formula = '''=IF(F442>0,F442/D442,"")'''
    @eval_fn
    def E442():
        f442_1 = OLD_Input_EIA_Jet_Fuel_Price.F442()
        var_1 = greaterthan(f442_1, 0)
        f442_2 = OLD_Input_EIA_Jet_Fuel_Price.F442()
        d442_1 = OLD_Input_EIA_Jet_Fuel_Price.D442()
        var_2 = divide(f442_2, d442_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A443():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A443
    value = 44197
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B443():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B443
    value = 0
    formula = "=D443*$B$3"
    @eval_fn
    def B443():
        d443_1 = OLD_Input_EIA_Jet_Fuel_Price.D443()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d443_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C443():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C443
    value = 44211
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E443():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E443
    value = None
    formula = '''=IF(F443>0,F443/D443,"")'''
    @eval_fn
    def E443():
        f443_1 = OLD_Input_EIA_Jet_Fuel_Price.F443()
        var_1 = greaterthan(f443_1, 0)
        f443_2 = OLD_Input_EIA_Jet_Fuel_Price.F443()
        d443_1 = OLD_Input_EIA_Jet_Fuel_Price.D443()
        var_2 = divide(f443_2, d443_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A444():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A444
    value = 44228
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B444():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B444
    value = 0
    formula = "=D444*$B$3"
    @eval_fn
    def B444():
        d444_1 = OLD_Input_EIA_Jet_Fuel_Price.D444()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d444_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C444():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C444
    value = 44242
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E444():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E444
    value = None
    formula = '''=IF(F444>0,F444/D444,"")'''
    @eval_fn
    def E444():
        f444_1 = OLD_Input_EIA_Jet_Fuel_Price.F444()
        var_1 = greaterthan(f444_1, 0)
        f444_2 = OLD_Input_EIA_Jet_Fuel_Price.F444()
        d444_1 = OLD_Input_EIA_Jet_Fuel_Price.D444()
        var_2 = divide(f444_2, d444_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A445():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A445
    value = 44256
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B445():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B445
    value = 0
    formula = "=D445*$B$3"
    @eval_fn
    def B445():
        d445_1 = OLD_Input_EIA_Jet_Fuel_Price.D445()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d445_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C445():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C445
    value = 44270
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E445():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E445
    value = None
    formula = '''=IF(F445>0,F445/D445,"")'''
    @eval_fn
    def E445():
        f445_1 = OLD_Input_EIA_Jet_Fuel_Price.F445()
        var_1 = greaterthan(f445_1, 0)
        f445_2 = OLD_Input_EIA_Jet_Fuel_Price.F445()
        d445_1 = OLD_Input_EIA_Jet_Fuel_Price.D445()
        var_2 = divide(f445_2, d445_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A446():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A446
    value = 44287
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B446():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B446
    value = 0
    formula = "=D446*$B$3"
    @eval_fn
    def B446():
        d446_1 = OLD_Input_EIA_Jet_Fuel_Price.D446()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d446_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C446():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C446
    value = 44301
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E446():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E446
    value = None
    formula = '''=IF(F446>0,F446/D446,"")'''
    @eval_fn
    def E446():
        f446_1 = OLD_Input_EIA_Jet_Fuel_Price.F446()
        var_1 = greaterthan(f446_1, 0)
        f446_2 = OLD_Input_EIA_Jet_Fuel_Price.F446()
        d446_1 = OLD_Input_EIA_Jet_Fuel_Price.D446()
        var_2 = divide(f446_2, d446_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A447():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A447
    value = 44317
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B447():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B447
    value = 0
    formula = "=D447*$B$3"
    @eval_fn
    def B447():
        d447_1 = OLD_Input_EIA_Jet_Fuel_Price.D447()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d447_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C447():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C447
    value = 44331
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E447():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E447
    value = None
    formula = '''=IF(F447>0,F447/D447,"")'''
    @eval_fn
    def E447():
        f447_1 = OLD_Input_EIA_Jet_Fuel_Price.F447()
        var_1 = greaterthan(f447_1, 0)
        f447_2 = OLD_Input_EIA_Jet_Fuel_Price.F447()
        d447_1 = OLD_Input_EIA_Jet_Fuel_Price.D447()
        var_2 = divide(f447_2, d447_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A448():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A448
    value = 44348
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B448():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B448
    value = 0
    formula = "=D448*$B$3"
    @eval_fn
    def B448():
        d448_1 = OLD_Input_EIA_Jet_Fuel_Price.D448()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d448_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C448():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C448
    value = 44362
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E448():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E448
    value = None
    formula = '''=IF(F448>0,F448/D448,"")'''
    @eval_fn
    def E448():
        f448_1 = OLD_Input_EIA_Jet_Fuel_Price.F448()
        var_1 = greaterthan(f448_1, 0)
        f448_2 = OLD_Input_EIA_Jet_Fuel_Price.F448()
        d448_1 = OLD_Input_EIA_Jet_Fuel_Price.D448()
        var_2 = divide(f448_2, d448_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A449():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A449
    value = 44378
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B449():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B449
    value = 0
    formula = "=D449*$B$3"
    @eval_fn
    def B449():
        d449_1 = OLD_Input_EIA_Jet_Fuel_Price.D449()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d449_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C449():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C449
    value = 44392
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E449():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E449
    value = None
    formula = '''=IF(F449>0,F449/D449,"")'''
    @eval_fn
    def E449():
        f449_1 = OLD_Input_EIA_Jet_Fuel_Price.F449()
        var_1 = greaterthan(f449_1, 0)
        f449_2 = OLD_Input_EIA_Jet_Fuel_Price.F449()
        d449_1 = OLD_Input_EIA_Jet_Fuel_Price.D449()
        var_2 = divide(f449_2, d449_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A450():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A450
    value = 44409
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B450():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B450
    value = 0
    formula = "=D450*$B$3"
    @eval_fn
    def B450():
        d450_1 = OLD_Input_EIA_Jet_Fuel_Price.D450()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d450_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C450():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C450
    value = 44423
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E450():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E450
    value = None
    formula = '''=IF(F450>0,F450/D450,"")'''
    @eval_fn
    def E450():
        f450_1 = OLD_Input_EIA_Jet_Fuel_Price.F450()
        var_1 = greaterthan(f450_1, 0)
        f450_2 = OLD_Input_EIA_Jet_Fuel_Price.F450()
        d450_1 = OLD_Input_EIA_Jet_Fuel_Price.D450()
        var_2 = divide(f450_2, d450_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A451():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A451
    value = 44440
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B451():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B451
    value = 0
    formula = "=D451*$B$3"
    @eval_fn
    def B451():
        d451_1 = OLD_Input_EIA_Jet_Fuel_Price.D451()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d451_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C451():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C451
    value = 44454
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E451():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E451
    value = None
    formula = '''=IF(F451>0,F451/D451,"")'''
    @eval_fn
    def E451():
        f451_1 = OLD_Input_EIA_Jet_Fuel_Price.F451()
        var_1 = greaterthan(f451_1, 0)
        f451_2 = OLD_Input_EIA_Jet_Fuel_Price.F451()
        d451_1 = OLD_Input_EIA_Jet_Fuel_Price.D451()
        var_2 = divide(f451_2, d451_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A452():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A452
    value = 44470
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B452():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B452
    value = 0
    formula = "=D452*$B$3"
    @eval_fn
    def B452():
        d452_1 = OLD_Input_EIA_Jet_Fuel_Price.D452()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d452_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C452():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C452
    value = 44484
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E452():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E452
    value = None
    formula = '''=IF(F452>0,F452/D452,"")'''
    @eval_fn
    def E452():
        f452_1 = OLD_Input_EIA_Jet_Fuel_Price.F452()
        var_1 = greaterthan(f452_1, 0)
        f452_2 = OLD_Input_EIA_Jet_Fuel_Price.F452()
        d452_1 = OLD_Input_EIA_Jet_Fuel_Price.D452()
        var_2 = divide(f452_2, d452_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A453():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A453
    value = 44501
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B453():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B453
    value = 0
    formula = "=D453*$B$3"
    @eval_fn
    def B453():
        d453_1 = OLD_Input_EIA_Jet_Fuel_Price.D453()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d453_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C453():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C453
    value = 44515
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E453():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E453
    value = None
    formula = '''=IF(F453>0,F453/D453,"")'''
    @eval_fn
    def E453():
        f453_1 = OLD_Input_EIA_Jet_Fuel_Price.F453()
        var_1 = greaterthan(f453_1, 0)
        f453_2 = OLD_Input_EIA_Jet_Fuel_Price.F453()
        d453_1 = OLD_Input_EIA_Jet_Fuel_Price.D453()
        var_2 = divide(f453_2, d453_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A454():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A454
    value = 44531
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B454():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B454
    value = 0
    formula = "=D454*$B$3"
    @eval_fn
    def B454():
        d454_1 = OLD_Input_EIA_Jet_Fuel_Price.D454()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d454_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C454():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C454
    value = 44545
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E454():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E454
    value = None
    formula = '''=IF(F454>0,F454/D454,"")'''
    @eval_fn
    def E454():
        f454_1 = OLD_Input_EIA_Jet_Fuel_Price.F454()
        var_1 = greaterthan(f454_1, 0)
        f454_2 = OLD_Input_EIA_Jet_Fuel_Price.F454()
        d454_1 = OLD_Input_EIA_Jet_Fuel_Price.D454()
        var_2 = divide(f454_2, d454_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A455():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A455
    value = 44562
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B455():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B455
    value = 0
    formula = "=D455*$B$3"
    @eval_fn
    def B455():
        d455_1 = OLD_Input_EIA_Jet_Fuel_Price.D455()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d455_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C455():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C455
    value = 44576
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E455():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E455
    value = None
    formula = '''=IF(F455>0,F455/D455,"")'''
    @eval_fn
    def E455():
        f455_1 = OLD_Input_EIA_Jet_Fuel_Price.F455()
        var_1 = greaterthan(f455_1, 0)
        f455_2 = OLD_Input_EIA_Jet_Fuel_Price.F455()
        d455_1 = OLD_Input_EIA_Jet_Fuel_Price.D455()
        var_2 = divide(f455_2, d455_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A456():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A456
    value = 44593
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B456():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B456
    value = 0
    formula = "=D456*$B$3"
    @eval_fn
    def B456():
        d456_1 = OLD_Input_EIA_Jet_Fuel_Price.D456()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d456_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C456():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C456
    value = 44607
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E456():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E456
    value = None
    formula = '''=IF(F456>0,F456/D456,"")'''
    @eval_fn
    def E456():
        f456_1 = OLD_Input_EIA_Jet_Fuel_Price.F456()
        var_1 = greaterthan(f456_1, 0)
        f456_2 = OLD_Input_EIA_Jet_Fuel_Price.F456()
        d456_1 = OLD_Input_EIA_Jet_Fuel_Price.D456()
        var_2 = divide(f456_2, d456_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A457():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A457
    value = 44621
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B457():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B457
    value = 0
    formula = "=D457*$B$3"
    @eval_fn
    def B457():
        d457_1 = OLD_Input_EIA_Jet_Fuel_Price.D457()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d457_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C457():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C457
    value = 44635
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E457():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E457
    value = None
    formula = '''=IF(F457>0,F457/D457,"")'''
    @eval_fn
    def E457():
        f457_1 = OLD_Input_EIA_Jet_Fuel_Price.F457()
        var_1 = greaterthan(f457_1, 0)
        f457_2 = OLD_Input_EIA_Jet_Fuel_Price.F457()
        d457_1 = OLD_Input_EIA_Jet_Fuel_Price.D457()
        var_2 = divide(f457_2, d457_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A458():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A458
    value = 44652
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B458():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B458
    value = 0
    formula = "=D458*$B$3"
    @eval_fn
    def B458():
        d458_1 = OLD_Input_EIA_Jet_Fuel_Price.D458()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d458_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C458():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C458
    value = 44666
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E458():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E458
    value = None
    formula = '''=IF(F458>0,F458/D458,"")'''
    @eval_fn
    def E458():
        f458_1 = OLD_Input_EIA_Jet_Fuel_Price.F458()
        var_1 = greaterthan(f458_1, 0)
        f458_2 = OLD_Input_EIA_Jet_Fuel_Price.F458()
        d458_1 = OLD_Input_EIA_Jet_Fuel_Price.D458()
        var_2 = divide(f458_2, d458_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A459():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A459
    value = 44682
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B459():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B459
    value = 0
    formula = "=D459*$B$3"
    @eval_fn
    def B459():
        d459_1 = OLD_Input_EIA_Jet_Fuel_Price.D459()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d459_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C459():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C459
    value = 44696
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E459():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E459
    value = None
    formula = '''=IF(F459>0,F459/D459,"")'''
    @eval_fn
    def E459():
        f459_1 = OLD_Input_EIA_Jet_Fuel_Price.F459()
        var_1 = greaterthan(f459_1, 0)
        f459_2 = OLD_Input_EIA_Jet_Fuel_Price.F459()
        d459_1 = OLD_Input_EIA_Jet_Fuel_Price.D459()
        var_2 = divide(f459_2, d459_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A460():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A460
    value = 44713
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B460():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B460
    value = 0
    formula = "=D460*$B$3"
    @eval_fn
    def B460():
        d460_1 = OLD_Input_EIA_Jet_Fuel_Price.D460()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d460_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C460():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C460
    value = 44727
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E460():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E460
    value = None
    formula = '''=IF(F460>0,F460/D460,"")'''
    @eval_fn
    def E460():
        f460_1 = OLD_Input_EIA_Jet_Fuel_Price.F460()
        var_1 = greaterthan(f460_1, 0)
        f460_2 = OLD_Input_EIA_Jet_Fuel_Price.F460()
        d460_1 = OLD_Input_EIA_Jet_Fuel_Price.D460()
        var_2 = divide(f460_2, d460_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A461():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A461
    value = 44743
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B461():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B461
    value = 0
    formula = "=D461*$B$3"
    @eval_fn
    def B461():
        d461_1 = OLD_Input_EIA_Jet_Fuel_Price.D461()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d461_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C461():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C461
    value = 44757
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E461():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E461
    value = None
    formula = '''=IF(F461>0,F461/D461,"")'''
    @eval_fn
    def E461():
        f461_1 = OLD_Input_EIA_Jet_Fuel_Price.F461()
        var_1 = greaterthan(f461_1, 0)
        f461_2 = OLD_Input_EIA_Jet_Fuel_Price.F461()
        d461_1 = OLD_Input_EIA_Jet_Fuel_Price.D461()
        var_2 = divide(f461_2, d461_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A462():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A462
    value = 44774
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B462():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B462
    value = 0
    formula = "=D462*$B$3"
    @eval_fn
    def B462():
        d462_1 = OLD_Input_EIA_Jet_Fuel_Price.D462()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d462_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C462():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C462
    value = 44788
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E462():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E462
    value = None
    formula = '''=IF(F462>0,F462/D462,"")'''
    @eval_fn
    def E462():
        f462_1 = OLD_Input_EIA_Jet_Fuel_Price.F462()
        var_1 = greaterthan(f462_1, 0)
        f462_2 = OLD_Input_EIA_Jet_Fuel_Price.F462()
        d462_1 = OLD_Input_EIA_Jet_Fuel_Price.D462()
        var_2 = divide(f462_2, d462_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A463():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A463
    value = 44805
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B463():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B463
    value = 0
    formula = "=D463*$B$3"
    @eval_fn
    def B463():
        d463_1 = OLD_Input_EIA_Jet_Fuel_Price.D463()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d463_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C463():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C463
    value = 44819
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E463():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E463
    value = None
    formula = '''=IF(F463>0,F463/D463,"")'''
    @eval_fn
    def E463():
        f463_1 = OLD_Input_EIA_Jet_Fuel_Price.F463()
        var_1 = greaterthan(f463_1, 0)
        f463_2 = OLD_Input_EIA_Jet_Fuel_Price.F463()
        d463_1 = OLD_Input_EIA_Jet_Fuel_Price.D463()
        var_2 = divide(f463_2, d463_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A464():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A464
    value = 44835
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B464():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B464
    value = 0
    formula = "=D464*$B$3"
    @eval_fn
    def B464():
        d464_1 = OLD_Input_EIA_Jet_Fuel_Price.D464()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d464_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C464():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C464
    value = 44849
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E464():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E464
    value = None
    formula = '''=IF(F464>0,F464/D464,"")'''
    @eval_fn
    def E464():
        f464_1 = OLD_Input_EIA_Jet_Fuel_Price.F464()
        var_1 = greaterthan(f464_1, 0)
        f464_2 = OLD_Input_EIA_Jet_Fuel_Price.F464()
        d464_1 = OLD_Input_EIA_Jet_Fuel_Price.D464()
        var_2 = divide(f464_2, d464_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A465():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A465
    value = 44866
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B465():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B465
    value = 0
    formula = "=D465*$B$3"
    @eval_fn
    def B465():
        d465_1 = OLD_Input_EIA_Jet_Fuel_Price.D465()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d465_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C465():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C465
    value = 44880
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E465():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E465
    value = None
    formula = '''=IF(F465>0,F465/D465,"")'''
    @eval_fn
    def E465():
        f465_1 = OLD_Input_EIA_Jet_Fuel_Price.F465()
        var_1 = greaterthan(f465_1, 0)
        f465_2 = OLD_Input_EIA_Jet_Fuel_Price.F465()
        d465_1 = OLD_Input_EIA_Jet_Fuel_Price.D465()
        var_2 = divide(f465_2, d465_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A466():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A466
    value = 44896
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B466():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B466
    value = 0
    formula = "=D466*$B$3"
    @eval_fn
    def B466():
        d466_1 = OLD_Input_EIA_Jet_Fuel_Price.D466()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d466_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C466():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C466
    value = 44910
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E466():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E466
    value = None
    formula = '''=IF(F466>0,F466/D466,"")'''
    @eval_fn
    def E466():
        f466_1 = OLD_Input_EIA_Jet_Fuel_Price.F466()
        var_1 = greaterthan(f466_1, 0)
        f466_2 = OLD_Input_EIA_Jet_Fuel_Price.F466()
        d466_1 = OLD_Input_EIA_Jet_Fuel_Price.D466()
        var_2 = divide(f466_2, d466_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A467():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A467
    value = 44927
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B467():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B467
    value = 0
    formula = "=D467*$B$3"
    @eval_fn
    def B467():
        d467_1 = OLD_Input_EIA_Jet_Fuel_Price.D467()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d467_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C467():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C467
    value = 44941
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E467():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E467
    value = None
    formula = '''=IF(F467>0,F467/D467,"")'''
    @eval_fn
    def E467():
        f467_1 = OLD_Input_EIA_Jet_Fuel_Price.F467()
        var_1 = greaterthan(f467_1, 0)
        f467_2 = OLD_Input_EIA_Jet_Fuel_Price.F467()
        d467_1 = OLD_Input_EIA_Jet_Fuel_Price.D467()
        var_2 = divide(f467_2, d467_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A468():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A468
    value = 44958
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B468():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B468
    value = 0
    formula = "=D468*$B$3"
    @eval_fn
    def B468():
        d468_1 = OLD_Input_EIA_Jet_Fuel_Price.D468()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d468_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C468():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C468
    value = 44972
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E468():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E468
    value = None
    formula = '''=IF(F468>0,F468/D468,"")'''
    @eval_fn
    def E468():
        f468_1 = OLD_Input_EIA_Jet_Fuel_Price.F468()
        var_1 = greaterthan(f468_1, 0)
        f468_2 = OLD_Input_EIA_Jet_Fuel_Price.F468()
        d468_1 = OLD_Input_EIA_Jet_Fuel_Price.D468()
        var_2 = divide(f468_2, d468_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A469():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A469
    value = 44986
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B469():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B469
    value = 0
    formula = "=D469*$B$3"
    @eval_fn
    def B469():
        d469_1 = OLD_Input_EIA_Jet_Fuel_Price.D469()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d469_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C469():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C469
    value = 45000
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E469():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E469
    value = None
    formula = '''=IF(F469>0,F469/D469,"")'''
    @eval_fn
    def E469():
        f469_1 = OLD_Input_EIA_Jet_Fuel_Price.F469()
        var_1 = greaterthan(f469_1, 0)
        f469_2 = OLD_Input_EIA_Jet_Fuel_Price.F469()
        d469_1 = OLD_Input_EIA_Jet_Fuel_Price.D469()
        var_2 = divide(f469_2, d469_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A470():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A470
    value = 45017
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B470():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B470
    value = 0
    formula = "=D470*$B$3"
    @eval_fn
    def B470():
        d470_1 = OLD_Input_EIA_Jet_Fuel_Price.D470()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d470_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C470():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C470
    value = 45031
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E470():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E470
    value = None
    formula = '''=IF(F470>0,F470/D470,"")'''
    @eval_fn
    def E470():
        f470_1 = OLD_Input_EIA_Jet_Fuel_Price.F470()
        var_1 = greaterthan(f470_1, 0)
        f470_2 = OLD_Input_EIA_Jet_Fuel_Price.F470()
        d470_1 = OLD_Input_EIA_Jet_Fuel_Price.D470()
        var_2 = divide(f470_2, d470_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A471():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A471
    value = 45047
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B471():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B471
    value = 0
    formula = "=D471*$B$3"
    @eval_fn
    def B471():
        d471_1 = OLD_Input_EIA_Jet_Fuel_Price.D471()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d471_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C471():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C471
    value = 45061
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E471():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E471
    value = None
    formula = '''=IF(F471>0,F471/D471,"")'''
    @eval_fn
    def E471():
        f471_1 = OLD_Input_EIA_Jet_Fuel_Price.F471()
        var_1 = greaterthan(f471_1, 0)
        f471_2 = OLD_Input_EIA_Jet_Fuel_Price.F471()
        d471_1 = OLD_Input_EIA_Jet_Fuel_Price.D471()
        var_2 = divide(f471_2, d471_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A472():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A472
    value = 45078
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B472():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B472
    value = 0
    formula = "=D472*$B$3"
    @eval_fn
    def B472():
        d472_1 = OLD_Input_EIA_Jet_Fuel_Price.D472()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d472_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C472():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C472
    value = 45092
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E472():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E472
    value = None
    formula = '''=IF(F472>0,F472/D472,"")'''
    @eval_fn
    def E472():
        f472_1 = OLD_Input_EIA_Jet_Fuel_Price.F472()
        var_1 = greaterthan(f472_1, 0)
        f472_2 = OLD_Input_EIA_Jet_Fuel_Price.F472()
        d472_1 = OLD_Input_EIA_Jet_Fuel_Price.D472()
        var_2 = divide(f472_2, d472_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A473():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A473
    value = 45108
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B473():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B473
    value = 0
    formula = "=D473*$B$3"
    @eval_fn
    def B473():
        d473_1 = OLD_Input_EIA_Jet_Fuel_Price.D473()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d473_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C473():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C473
    value = 45122
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E473():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E473
    value = None
    formula = '''=IF(F473>0,F473/D473,"")'''
    @eval_fn
    def E473():
        f473_1 = OLD_Input_EIA_Jet_Fuel_Price.F473()
        var_1 = greaterthan(f473_1, 0)
        f473_2 = OLD_Input_EIA_Jet_Fuel_Price.F473()
        d473_1 = OLD_Input_EIA_Jet_Fuel_Price.D473()
        var_2 = divide(f473_2, d473_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A474():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A474
    value = 45139
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B474():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B474
    value = 0
    formula = "=D474*$B$3"
    @eval_fn
    def B474():
        d474_1 = OLD_Input_EIA_Jet_Fuel_Price.D474()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d474_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C474():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C474
    value = 45153
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E474():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E474
    value = None
    formula = '''=IF(F474>0,F474/D474,"")'''
    @eval_fn
    def E474():
        f474_1 = OLD_Input_EIA_Jet_Fuel_Price.F474()
        var_1 = greaterthan(f474_1, 0)
        f474_2 = OLD_Input_EIA_Jet_Fuel_Price.F474()
        d474_1 = OLD_Input_EIA_Jet_Fuel_Price.D474()
        var_2 = divide(f474_2, d474_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A475():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A475
    value = 45170
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B475():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B475
    value = 0
    formula = "=D475*$B$3"
    @eval_fn
    def B475():
        d475_1 = OLD_Input_EIA_Jet_Fuel_Price.D475()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d475_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C475():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C475
    value = 45184
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E475():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E475
    value = None
    formula = '''=IF(F475>0,F475/D475,"")'''
    @eval_fn
    def E475():
        f475_1 = OLD_Input_EIA_Jet_Fuel_Price.F475()
        var_1 = greaterthan(f475_1, 0)
        f475_2 = OLD_Input_EIA_Jet_Fuel_Price.F475()
        d475_1 = OLD_Input_EIA_Jet_Fuel_Price.D475()
        var_2 = divide(f475_2, d475_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A476():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A476
    value = 45200
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B476():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B476
    value = 0
    formula = "=D476*$B$3"
    @eval_fn
    def B476():
        d476_1 = OLD_Input_EIA_Jet_Fuel_Price.D476()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d476_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C476():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C476
    value = 45214
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E476():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E476
    value = None
    formula = '''=IF(F476>0,F476/D476,"")'''
    @eval_fn
    def E476():
        f476_1 = OLD_Input_EIA_Jet_Fuel_Price.F476()
        var_1 = greaterthan(f476_1, 0)
        f476_2 = OLD_Input_EIA_Jet_Fuel_Price.F476()
        d476_1 = OLD_Input_EIA_Jet_Fuel_Price.D476()
        var_2 = divide(f476_2, d476_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A477():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A477
    value = 45231
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B477():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B477
    value = 0
    formula = "=D477*$B$3"
    @eval_fn
    def B477():
        d477_1 = OLD_Input_EIA_Jet_Fuel_Price.D477()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d477_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C477():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C477
    value = 45245
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E477():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E477
    value = None
    formula = '''=IF(F477>0,F477/D477,"")'''
    @eval_fn
    def E477():
        f477_1 = OLD_Input_EIA_Jet_Fuel_Price.F477()
        var_1 = greaterthan(f477_1, 0)
        f477_2 = OLD_Input_EIA_Jet_Fuel_Price.F477()
        d477_1 = OLD_Input_EIA_Jet_Fuel_Price.D477()
        var_2 = divide(f477_2, d477_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A478():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A478
    value = 45261
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B478():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B478
    value = 0
    formula = "=D478*$B$3"
    @eval_fn
    def B478():
        d478_1 = OLD_Input_EIA_Jet_Fuel_Price.D478()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d478_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C478():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C478
    value = 45275
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E478():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E478
    value = None
    formula = '''=IF(F478>0,F478/D478,"")'''
    @eval_fn
    def E478():
        f478_1 = OLD_Input_EIA_Jet_Fuel_Price.F478()
        var_1 = greaterthan(f478_1, 0)
        f478_2 = OLD_Input_EIA_Jet_Fuel_Price.F478()
        d478_1 = OLD_Input_EIA_Jet_Fuel_Price.D478()
        var_2 = divide(f478_2, d478_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A479():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A479
    value = 45292
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B479():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B479
    value = 0
    formula = "=D479*$B$3"
    @eval_fn
    def B479():
        d479_1 = OLD_Input_EIA_Jet_Fuel_Price.D479()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d479_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C479():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C479
    value = 45306
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E479():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E479
    value = None
    formula = '''=IF(F479>0,F479/D479,"")'''
    @eval_fn
    def E479():
        f479_1 = OLD_Input_EIA_Jet_Fuel_Price.F479()
        var_1 = greaterthan(f479_1, 0)
        f479_2 = OLD_Input_EIA_Jet_Fuel_Price.F479()
        d479_1 = OLD_Input_EIA_Jet_Fuel_Price.D479()
        var_2 = divide(f479_2, d479_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A480():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A480
    value = 45323
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B480():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B480
    value = 0
    formula = "=D480*$B$3"
    @eval_fn
    def B480():
        d480_1 = OLD_Input_EIA_Jet_Fuel_Price.D480()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d480_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C480():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C480
    value = 45337
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E480():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E480
    value = None
    formula = '''=IF(F480>0,F480/D480,"")'''
    @eval_fn
    def E480():
        f480_1 = OLD_Input_EIA_Jet_Fuel_Price.F480()
        var_1 = greaterthan(f480_1, 0)
        f480_2 = OLD_Input_EIA_Jet_Fuel_Price.F480()
        d480_1 = OLD_Input_EIA_Jet_Fuel_Price.D480()
        var_2 = divide(f480_2, d480_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A481():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A481
    value = 45352
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B481():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B481
    value = 0
    formula = "=D481*$B$3"
    @eval_fn
    def B481():
        d481_1 = OLD_Input_EIA_Jet_Fuel_Price.D481()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d481_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C481():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C481
    value = 45366
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E481():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E481
    value = None
    formula = '''=IF(F481>0,F481/D481,"")'''
    @eval_fn
    def E481():
        f481_1 = OLD_Input_EIA_Jet_Fuel_Price.F481()
        var_1 = greaterthan(f481_1, 0)
        f481_2 = OLD_Input_EIA_Jet_Fuel_Price.F481()
        d481_1 = OLD_Input_EIA_Jet_Fuel_Price.D481()
        var_2 = divide(f481_2, d481_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A482():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A482
    value = 45383
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B482():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B482
    value = 0
    formula = "=D482*$B$3"
    @eval_fn
    def B482():
        d482_1 = OLD_Input_EIA_Jet_Fuel_Price.D482()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d482_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C482():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C482
    value = 45397
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E482():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E482
    value = None
    formula = '''=IF(F482>0,F482/D482,"")'''
    @eval_fn
    def E482():
        f482_1 = OLD_Input_EIA_Jet_Fuel_Price.F482()
        var_1 = greaterthan(f482_1, 0)
        f482_2 = OLD_Input_EIA_Jet_Fuel_Price.F482()
        d482_1 = OLD_Input_EIA_Jet_Fuel_Price.D482()
        var_2 = divide(f482_2, d482_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A483():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A483
    value = 45413
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B483():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B483
    value = 0
    formula = "=D483*$B$3"
    @eval_fn
    def B483():
        d483_1 = OLD_Input_EIA_Jet_Fuel_Price.D483()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d483_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C483():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C483
    value = 45427
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E483():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E483
    value = None
    formula = '''=IF(F483>0,F483/D483,"")'''
    @eval_fn
    def E483():
        f483_1 = OLD_Input_EIA_Jet_Fuel_Price.F483()
        var_1 = greaterthan(f483_1, 0)
        f483_2 = OLD_Input_EIA_Jet_Fuel_Price.F483()
        d483_1 = OLD_Input_EIA_Jet_Fuel_Price.D483()
        var_2 = divide(f483_2, d483_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A484():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A484
    value = 45444
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B484():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B484
    value = 0
    formula = "=D484*$B$3"
    @eval_fn
    def B484():
        d484_1 = OLD_Input_EIA_Jet_Fuel_Price.D484()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d484_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C484():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C484
    value = 45458
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E484():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E484
    value = None
    formula = '''=IF(F484>0,F484/D484,"")'''
    @eval_fn
    def E484():
        f484_1 = OLD_Input_EIA_Jet_Fuel_Price.F484()
        var_1 = greaterthan(f484_1, 0)
        f484_2 = OLD_Input_EIA_Jet_Fuel_Price.F484()
        d484_1 = OLD_Input_EIA_Jet_Fuel_Price.D484()
        var_2 = divide(f484_2, d484_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A485():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A485
    value = 45474
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B485():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B485
    value = 0
    formula = "=D485*$B$3"
    @eval_fn
    def B485():
        d485_1 = OLD_Input_EIA_Jet_Fuel_Price.D485()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d485_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C485():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C485
    value = 45488
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E485():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E485
    value = None
    formula = '''=IF(F485>0,F485/D485,"")'''
    @eval_fn
    def E485():
        f485_1 = OLD_Input_EIA_Jet_Fuel_Price.F485()
        var_1 = greaterthan(f485_1, 0)
        f485_2 = OLD_Input_EIA_Jet_Fuel_Price.F485()
        d485_1 = OLD_Input_EIA_Jet_Fuel_Price.D485()
        var_2 = divide(f485_2, d485_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A486():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A486
    value = 45505
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B486():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B486
    value = 0
    formula = "=D486*$B$3"
    @eval_fn
    def B486():
        d486_1 = OLD_Input_EIA_Jet_Fuel_Price.D486()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d486_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C486():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C486
    value = 45519
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E486():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E486
    value = None
    formula = '''=IF(F486>0,F486/D486,"")'''
    @eval_fn
    def E486():
        f486_1 = OLD_Input_EIA_Jet_Fuel_Price.F486()
        var_1 = greaterthan(f486_1, 0)
        f486_2 = OLD_Input_EIA_Jet_Fuel_Price.F486()
        d486_1 = OLD_Input_EIA_Jet_Fuel_Price.D486()
        var_2 = divide(f486_2, d486_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A487():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A487
    value = 45536
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B487():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B487
    value = 0
    formula = "=D487*$B$3"
    @eval_fn
    def B487():
        d487_1 = OLD_Input_EIA_Jet_Fuel_Price.D487()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d487_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C487():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C487
    value = 45550
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E487():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E487
    value = None
    formula = '''=IF(F487>0,F487/D487,"")'''
    @eval_fn
    def E487():
        f487_1 = OLD_Input_EIA_Jet_Fuel_Price.F487()
        var_1 = greaterthan(f487_1, 0)
        f487_2 = OLD_Input_EIA_Jet_Fuel_Price.F487()
        d487_1 = OLD_Input_EIA_Jet_Fuel_Price.D487()
        var_2 = divide(f487_2, d487_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A488():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A488
    value = 45566
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B488():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B488
    value = 0
    formula = "=D488*$B$3"
    @eval_fn
    def B488():
        d488_1 = OLD_Input_EIA_Jet_Fuel_Price.D488()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d488_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C488():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C488
    value = 45580
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E488():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E488
    value = None
    formula = '''=IF(F488>0,F488/D488,"")'''
    @eval_fn
    def E488():
        f488_1 = OLD_Input_EIA_Jet_Fuel_Price.F488()
        var_1 = greaterthan(f488_1, 0)
        f488_2 = OLD_Input_EIA_Jet_Fuel_Price.F488()
        d488_1 = OLD_Input_EIA_Jet_Fuel_Price.D488()
        var_2 = divide(f488_2, d488_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A489():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A489
    value = 45597
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B489():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B489
    value = 0
    formula = "=D489*$B$3"
    @eval_fn
    def B489():
        d489_1 = OLD_Input_EIA_Jet_Fuel_Price.D489()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d489_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C489():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C489
    value = 45611
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E489():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E489
    value = None
    formula = '''=IF(F489>0,F489/D489,"")'''
    @eval_fn
    def E489():
        f489_1 = OLD_Input_EIA_Jet_Fuel_Price.F489()
        var_1 = greaterthan(f489_1, 0)
        f489_2 = OLD_Input_EIA_Jet_Fuel_Price.F489()
        d489_1 = OLD_Input_EIA_Jet_Fuel_Price.D489()
        var_2 = divide(f489_2, d489_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A490():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A490
    value = 45627
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B490():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B490
    value = 0
    formula = "=D490*$B$3"
    @eval_fn
    def B490():
        d490_1 = OLD_Input_EIA_Jet_Fuel_Price.D490()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d490_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C490():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C490
    value = 45641
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E490():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E490
    value = None
    formula = '''=IF(F490>0,F490/D490,"")'''
    @eval_fn
    def E490():
        f490_1 = OLD_Input_EIA_Jet_Fuel_Price.F490()
        var_1 = greaterthan(f490_1, 0)
        f490_2 = OLD_Input_EIA_Jet_Fuel_Price.F490()
        d490_1 = OLD_Input_EIA_Jet_Fuel_Price.D490()
        var_2 = divide(f490_2, d490_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A491():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A491
    value = 45658
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B491():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B491
    value = 0
    formula = "=D491*$B$3"
    @eval_fn
    def B491():
        d491_1 = OLD_Input_EIA_Jet_Fuel_Price.D491()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d491_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C491():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C491
    value = 45672
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E491():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E491
    value = None
    formula = '''=IF(F491>0,F491/D491,"")'''
    @eval_fn
    def E491():
        f491_1 = OLD_Input_EIA_Jet_Fuel_Price.F491()
        var_1 = greaterthan(f491_1, 0)
        f491_2 = OLD_Input_EIA_Jet_Fuel_Price.F491()
        d491_1 = OLD_Input_EIA_Jet_Fuel_Price.D491()
        var_2 = divide(f491_2, d491_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A492():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A492
    value = 45689
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B492():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B492
    value = 0
    formula = "=D492*$B$3"
    @eval_fn
    def B492():
        d492_1 = OLD_Input_EIA_Jet_Fuel_Price.D492()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d492_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C492():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C492
    value = 45703
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E492():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E492
    value = None
    formula = '''=IF(F492>0,F492/D492,"")'''
    @eval_fn
    def E492():
        f492_1 = OLD_Input_EIA_Jet_Fuel_Price.F492()
        var_1 = greaterthan(f492_1, 0)
        f492_2 = OLD_Input_EIA_Jet_Fuel_Price.F492()
        d492_1 = OLD_Input_EIA_Jet_Fuel_Price.D492()
        var_2 = divide(f492_2, d492_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A493():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A493
    value = 45717
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B493():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B493
    value = 0
    formula = "=D493*$B$3"
    @eval_fn
    def B493():
        d493_1 = OLD_Input_EIA_Jet_Fuel_Price.D493()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d493_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C493():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C493
    value = 45731
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E493():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E493
    value = None
    formula = '''=IF(F493>0,F493/D493,"")'''
    @eval_fn
    def E493():
        f493_1 = OLD_Input_EIA_Jet_Fuel_Price.F493()
        var_1 = greaterthan(f493_1, 0)
        f493_2 = OLD_Input_EIA_Jet_Fuel_Price.F493()
        d493_1 = OLD_Input_EIA_Jet_Fuel_Price.D493()
        var_2 = divide(f493_2, d493_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A494():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A494
    value = 45748
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B494():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B494
    value = 0
    formula = "=D494*$B$3"
    @eval_fn
    def B494():
        d494_1 = OLD_Input_EIA_Jet_Fuel_Price.D494()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d494_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C494():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C494
    value = 45762
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E494():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E494
    value = None
    formula = '''=IF(F494>0,F494/D494,"")'''
    @eval_fn
    def E494():
        f494_1 = OLD_Input_EIA_Jet_Fuel_Price.F494()
        var_1 = greaterthan(f494_1, 0)
        f494_2 = OLD_Input_EIA_Jet_Fuel_Price.F494()
        d494_1 = OLD_Input_EIA_Jet_Fuel_Price.D494()
        var_2 = divide(f494_2, d494_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A495():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A495
    value = 45778
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B495():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B495
    value = 0
    formula = "=D495*$B$3"
    @eval_fn
    def B495():
        d495_1 = OLD_Input_EIA_Jet_Fuel_Price.D495()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d495_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C495():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C495
    value = 45792
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E495():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E495
    value = None
    formula = '''=IF(F495>0,F495/D495,"")'''
    @eval_fn
    def E495():
        f495_1 = OLD_Input_EIA_Jet_Fuel_Price.F495()
        var_1 = greaterthan(f495_1, 0)
        f495_2 = OLD_Input_EIA_Jet_Fuel_Price.F495()
        d495_1 = OLD_Input_EIA_Jet_Fuel_Price.D495()
        var_2 = divide(f495_2, d495_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A496():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A496
    value = 45809
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B496():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B496
    value = 0
    formula = "=D496*$B$3"
    @eval_fn
    def B496():
        d496_1 = OLD_Input_EIA_Jet_Fuel_Price.D496()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d496_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C496():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C496
    value = 45823
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E496():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E496
    value = None
    formula = '''=IF(F496>0,F496/D496,"")'''
    @eval_fn
    def E496():
        f496_1 = OLD_Input_EIA_Jet_Fuel_Price.F496()
        var_1 = greaterthan(f496_1, 0)
        f496_2 = OLD_Input_EIA_Jet_Fuel_Price.F496()
        d496_1 = OLD_Input_EIA_Jet_Fuel_Price.D496()
        var_2 = divide(f496_2, d496_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A497():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A497
    value = 45839
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B497():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B497
    value = 0
    formula = "=D497*$B$3"
    @eval_fn
    def B497():
        d497_1 = OLD_Input_EIA_Jet_Fuel_Price.D497()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d497_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C497():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C497
    value = 45853
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E497():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E497
    value = None
    formula = '''=IF(F497>0,F497/D497,"")'''
    @eval_fn
    def E497():
        f497_1 = OLD_Input_EIA_Jet_Fuel_Price.F497()
        var_1 = greaterthan(f497_1, 0)
        f497_2 = OLD_Input_EIA_Jet_Fuel_Price.F497()
        d497_1 = OLD_Input_EIA_Jet_Fuel_Price.D497()
        var_2 = divide(f497_2, d497_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A498():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A498
    value = 45870
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B498():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B498
    value = 0
    formula = "=D498*$B$3"
    @eval_fn
    def B498():
        d498_1 = OLD_Input_EIA_Jet_Fuel_Price.D498()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d498_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C498():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C498
    value = 45884
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E498():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E498
    value = None
    formula = '''=IF(F498>0,F498/D498,"")'''
    @eval_fn
    def E498():
        f498_1 = OLD_Input_EIA_Jet_Fuel_Price.F498()
        var_1 = greaterthan(f498_1, 0)
        f498_2 = OLD_Input_EIA_Jet_Fuel_Price.F498()
        d498_1 = OLD_Input_EIA_Jet_Fuel_Price.D498()
        var_2 = divide(f498_2, d498_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A499():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A499
    value = 45901
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B499():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B499
    value = 0
    formula = "=D499*$B$3"
    @eval_fn
    def B499():
        d499_1 = OLD_Input_EIA_Jet_Fuel_Price.D499()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d499_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C499():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C499
    value = 45915
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E499():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E499
    value = None
    formula = '''=IF(F499>0,F499/D499,"")'''
    @eval_fn
    def E499():
        f499_1 = OLD_Input_EIA_Jet_Fuel_Price.F499()
        var_1 = greaterthan(f499_1, 0)
        f499_2 = OLD_Input_EIA_Jet_Fuel_Price.F499()
        d499_1 = OLD_Input_EIA_Jet_Fuel_Price.D499()
        var_2 = divide(f499_2, d499_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A500():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A500
    value = 45931
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B500():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B500
    value = 0
    formula = "=D500*$B$3"
    @eval_fn
    def B500():
        d500_1 = OLD_Input_EIA_Jet_Fuel_Price.D500()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d500_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C500():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C500
    value = 45945
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E500():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E500
    value = None
    formula = '''=IF(F500>0,F500/D500,"")'''
    @eval_fn
    def E500():
        f500_1 = OLD_Input_EIA_Jet_Fuel_Price.F500()
        var_1 = greaterthan(f500_1, 0)
        f500_2 = OLD_Input_EIA_Jet_Fuel_Price.F500()
        d500_1 = OLD_Input_EIA_Jet_Fuel_Price.D500()
        var_2 = divide(f500_2, d500_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A501():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A501
    value = 45962
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B501():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B501
    value = 0
    formula = "=D501*$B$3"
    @eval_fn
    def B501():
        d501_1 = OLD_Input_EIA_Jet_Fuel_Price.D501()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d501_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C501():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C501
    value = 45976
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E501():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E501
    value = None
    formula = '''=IF(F501>0,F501/D501,"")'''
    @eval_fn
    def E501():
        f501_1 = OLD_Input_EIA_Jet_Fuel_Price.F501()
        var_1 = greaterthan(f501_1, 0)
        f501_2 = OLD_Input_EIA_Jet_Fuel_Price.F501()
        d501_1 = OLD_Input_EIA_Jet_Fuel_Price.D501()
        var_2 = divide(f501_2, d501_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A502():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A502
    value = 45992
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B502():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B502
    value = 0
    formula = "=D502*$B$3"
    @eval_fn
    def B502():
        d502_1 = OLD_Input_EIA_Jet_Fuel_Price.D502()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d502_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C502():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C502
    value = 46006
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E502():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E502
    value = None
    formula = '''=IF(F502>0,F502/D502,"")'''
    @eval_fn
    def E502():
        f502_1 = OLD_Input_EIA_Jet_Fuel_Price.F502()
        var_1 = greaterthan(f502_1, 0)
        f502_2 = OLD_Input_EIA_Jet_Fuel_Price.F502()
        d502_1 = OLD_Input_EIA_Jet_Fuel_Price.D502()
        var_2 = divide(f502_2, d502_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A503():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A503
    value = 46023
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B503():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B503
    value = 0
    formula = "=D503*$B$3"
    @eval_fn
    def B503():
        d503_1 = OLD_Input_EIA_Jet_Fuel_Price.D503()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d503_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C503():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C503
    value = 46037
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E503():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E503
    value = None
    formula = '''=IF(F503>0,F503/D503,"")'''
    @eval_fn
    def E503():
        f503_1 = OLD_Input_EIA_Jet_Fuel_Price.F503()
        var_1 = greaterthan(f503_1, 0)
        f503_2 = OLD_Input_EIA_Jet_Fuel_Price.F503()
        d503_1 = OLD_Input_EIA_Jet_Fuel_Price.D503()
        var_2 = divide(f503_2, d503_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A504():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A504
    value = 46054
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B504():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B504
    value = 0
    formula = "=D504*$B$3"
    @eval_fn
    def B504():
        d504_1 = OLD_Input_EIA_Jet_Fuel_Price.D504()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d504_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C504():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C504
    value = 46068
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E504():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E504
    value = None
    formula = '''=IF(F504>0,F504/D504,"")'''
    @eval_fn
    def E504():
        f504_1 = OLD_Input_EIA_Jet_Fuel_Price.F504()
        var_1 = greaterthan(f504_1, 0)
        f504_2 = OLD_Input_EIA_Jet_Fuel_Price.F504()
        d504_1 = OLD_Input_EIA_Jet_Fuel_Price.D504()
        var_2 = divide(f504_2, d504_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A505():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A505
    value = 46082
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B505():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B505
    value = 0
    formula = "=D505*$B$3"
    @eval_fn
    def B505():
        d505_1 = OLD_Input_EIA_Jet_Fuel_Price.D505()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d505_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C505():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C505
    value = 46096
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E505():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E505
    value = None
    formula = '''=IF(F505>0,F505/D505,"")'''
    @eval_fn
    def E505():
        f505_1 = OLD_Input_EIA_Jet_Fuel_Price.F505()
        var_1 = greaterthan(f505_1, 0)
        f505_2 = OLD_Input_EIA_Jet_Fuel_Price.F505()
        d505_1 = OLD_Input_EIA_Jet_Fuel_Price.D505()
        var_2 = divide(f505_2, d505_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A506():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A506
    value = 46113
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B506():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B506
    value = 0
    formula = "=D506*$B$3"
    @eval_fn
    def B506():
        d506_1 = OLD_Input_EIA_Jet_Fuel_Price.D506()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d506_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C506():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C506
    value = 46127
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E506():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E506
    value = None
    formula = '''=IF(F506>0,F506/D506,"")'''
    @eval_fn
    def E506():
        f506_1 = OLD_Input_EIA_Jet_Fuel_Price.F506()
        var_1 = greaterthan(f506_1, 0)
        f506_2 = OLD_Input_EIA_Jet_Fuel_Price.F506()
        d506_1 = OLD_Input_EIA_Jet_Fuel_Price.D506()
        var_2 = divide(f506_2, d506_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A507():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A507
    value = 46143
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B507():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B507
    value = 0
    formula = "=D507*$B$3"
    @eval_fn
    def B507():
        d507_1 = OLD_Input_EIA_Jet_Fuel_Price.D507()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d507_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C507():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C507
    value = 46157
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E507():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E507
    value = None
    formula = '''=IF(F507>0,F507/D507,"")'''
    @eval_fn
    def E507():
        f507_1 = OLD_Input_EIA_Jet_Fuel_Price.F507()
        var_1 = greaterthan(f507_1, 0)
        f507_2 = OLD_Input_EIA_Jet_Fuel_Price.F507()
        d507_1 = OLD_Input_EIA_Jet_Fuel_Price.D507()
        var_2 = divide(f507_2, d507_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A508():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A508
    value = 46174
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B508():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B508
    value = 0
    formula = "=D508*$B$3"
    @eval_fn
    def B508():
        d508_1 = OLD_Input_EIA_Jet_Fuel_Price.D508()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d508_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C508():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C508
    value = 46188
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E508():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E508
    value = None
    formula = '''=IF(F508>0,F508/D508,"")'''
    @eval_fn
    def E508():
        f508_1 = OLD_Input_EIA_Jet_Fuel_Price.F508()
        var_1 = greaterthan(f508_1, 0)
        f508_2 = OLD_Input_EIA_Jet_Fuel_Price.F508()
        d508_1 = OLD_Input_EIA_Jet_Fuel_Price.D508()
        var_2 = divide(f508_2, d508_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A509():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A509
    value = 46204
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B509():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B509
    value = 0
    formula = "=D509*$B$3"
    @eval_fn
    def B509():
        d509_1 = OLD_Input_EIA_Jet_Fuel_Price.D509()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d509_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C509():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C509
    value = 46218
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E509():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E509
    value = None
    formula = '''=IF(F509>0,F509/D509,"")'''
    @eval_fn
    def E509():
        f509_1 = OLD_Input_EIA_Jet_Fuel_Price.F509()
        var_1 = greaterthan(f509_1, 0)
        f509_2 = OLD_Input_EIA_Jet_Fuel_Price.F509()
        d509_1 = OLD_Input_EIA_Jet_Fuel_Price.D509()
        var_2 = divide(f509_2, d509_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A510():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A510
    value = 46235
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B510():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B510
    value = 0
    formula = "=D510*$B$3"
    @eval_fn
    def B510():
        d510_1 = OLD_Input_EIA_Jet_Fuel_Price.D510()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d510_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C510():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C510
    value = 46249
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E510():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E510
    value = None
    formula = '''=IF(F510>0,F510/D510,"")'''
    @eval_fn
    def E510():
        f510_1 = OLD_Input_EIA_Jet_Fuel_Price.F510()
        var_1 = greaterthan(f510_1, 0)
        f510_2 = OLD_Input_EIA_Jet_Fuel_Price.F510()
        d510_1 = OLD_Input_EIA_Jet_Fuel_Price.D510()
        var_2 = divide(f510_2, d510_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A511():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A511
    value = 46266
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B511():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B511
    value = 0
    formula = "=D511*$B$3"
    @eval_fn
    def B511():
        d511_1 = OLD_Input_EIA_Jet_Fuel_Price.D511()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d511_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C511():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C511
    value = 46280
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E511():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E511
    value = None
    formula = '''=IF(F511>0,F511/D511,"")'''
    @eval_fn
    def E511():
        f511_1 = OLD_Input_EIA_Jet_Fuel_Price.F511()
        var_1 = greaterthan(f511_1, 0)
        f511_2 = OLD_Input_EIA_Jet_Fuel_Price.F511()
        d511_1 = OLD_Input_EIA_Jet_Fuel_Price.D511()
        var_2 = divide(f511_2, d511_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A512():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A512
    value = 46296
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B512():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B512
    value = 0
    formula = "=D512*$B$3"
    @eval_fn
    def B512():
        d512_1 = OLD_Input_EIA_Jet_Fuel_Price.D512()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d512_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C512():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C512
    value = 46310
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E512():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E512
    value = None
    formula = '''=IF(F512>0,F512/D512,"")'''
    @eval_fn
    def E512():
        f512_1 = OLD_Input_EIA_Jet_Fuel_Price.F512()
        var_1 = greaterthan(f512_1, 0)
        f512_2 = OLD_Input_EIA_Jet_Fuel_Price.F512()
        d512_1 = OLD_Input_EIA_Jet_Fuel_Price.D512()
        var_2 = divide(f512_2, d512_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A513():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A513
    value = 46327
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B513():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B513
    value = 0
    formula = "=D513*$B$3"
    @eval_fn
    def B513():
        d513_1 = OLD_Input_EIA_Jet_Fuel_Price.D513()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d513_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C513():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C513
    value = 46341
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E513():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E513
    value = None
    formula = '''=IF(F513>0,F513/D513,"")'''
    @eval_fn
    def E513():
        f513_1 = OLD_Input_EIA_Jet_Fuel_Price.F513()
        var_1 = greaterthan(f513_1, 0)
        f513_2 = OLD_Input_EIA_Jet_Fuel_Price.F513()
        d513_1 = OLD_Input_EIA_Jet_Fuel_Price.D513()
        var_2 = divide(f513_2, d513_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A514():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A514
    value = 46357
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B514():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B514
    value = 0
    formula = "=D514*$B$3"
    @eval_fn
    def B514():
        d514_1 = OLD_Input_EIA_Jet_Fuel_Price.D514()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d514_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C514():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C514
    value = 46371
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E514():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E514
    value = None
    formula = '''=IF(F514>0,F514/D514,"")'''
    @eval_fn
    def E514():
        f514_1 = OLD_Input_EIA_Jet_Fuel_Price.F514()
        var_1 = greaterthan(f514_1, 0)
        f514_2 = OLD_Input_EIA_Jet_Fuel_Price.F514()
        d514_1 = OLD_Input_EIA_Jet_Fuel_Price.D514()
        var_2 = divide(f514_2, d514_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A515():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A515
    value = 46388
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B515():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B515
    value = 0
    formula = "=D515*$B$3"
    @eval_fn
    def B515():
        d515_1 = OLD_Input_EIA_Jet_Fuel_Price.D515()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d515_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C515():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C515
    value = 46402
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E515():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E515
    value = None
    formula = '''=IF(F515>0,F515/D515,"")'''
    @eval_fn
    def E515():
        f515_1 = OLD_Input_EIA_Jet_Fuel_Price.F515()
        var_1 = greaterthan(f515_1, 0)
        f515_2 = OLD_Input_EIA_Jet_Fuel_Price.F515()
        d515_1 = OLD_Input_EIA_Jet_Fuel_Price.D515()
        var_2 = divide(f515_2, d515_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A516():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A516
    value = 46419
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B516():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B516
    value = 0
    formula = "=D516*$B$3"
    @eval_fn
    def B516():
        d516_1 = OLD_Input_EIA_Jet_Fuel_Price.D516()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d516_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C516():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C516
    value = 46433
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E516():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E516
    value = None
    formula = '''=IF(F516>0,F516/D516,"")'''
    @eval_fn
    def E516():
        f516_1 = OLD_Input_EIA_Jet_Fuel_Price.F516()
        var_1 = greaterthan(f516_1, 0)
        f516_2 = OLD_Input_EIA_Jet_Fuel_Price.F516()
        d516_1 = OLD_Input_EIA_Jet_Fuel_Price.D516()
        var_2 = divide(f516_2, d516_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A517():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A517
    value = 46447
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B517():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B517
    value = 0
    formula = "=D517*$B$3"
    @eval_fn
    def B517():
        d517_1 = OLD_Input_EIA_Jet_Fuel_Price.D517()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d517_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C517():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C517
    value = 46461
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E517():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E517
    value = None
    formula = '''=IF(F517>0,F517/D517,"")'''
    @eval_fn
    def E517():
        f517_1 = OLD_Input_EIA_Jet_Fuel_Price.F517()
        var_1 = greaterthan(f517_1, 0)
        f517_2 = OLD_Input_EIA_Jet_Fuel_Price.F517()
        d517_1 = OLD_Input_EIA_Jet_Fuel_Price.D517()
        var_2 = divide(f517_2, d517_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A518():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A518
    value = 46478
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B518():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B518
    value = 0
    formula = "=D518*$B$3"
    @eval_fn
    def B518():
        d518_1 = OLD_Input_EIA_Jet_Fuel_Price.D518()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d518_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C518():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C518
    value = 46492
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E518():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E518
    value = None
    formula = '''=IF(F518>0,F518/D518,"")'''
    @eval_fn
    def E518():
        f518_1 = OLD_Input_EIA_Jet_Fuel_Price.F518()
        var_1 = greaterthan(f518_1, 0)
        f518_2 = OLD_Input_EIA_Jet_Fuel_Price.F518()
        d518_1 = OLD_Input_EIA_Jet_Fuel_Price.D518()
        var_2 = divide(f518_2, d518_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A519():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A519
    value = 46508
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B519():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B519
    value = 0
    formula = "=D519*$B$3"
    @eval_fn
    def B519():
        d519_1 = OLD_Input_EIA_Jet_Fuel_Price.D519()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d519_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C519():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C519
    value = 46522
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E519():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E519
    value = None
    formula = '''=IF(F519>0,F519/D519,"")'''
    @eval_fn
    def E519():
        f519_1 = OLD_Input_EIA_Jet_Fuel_Price.F519()
        var_1 = greaterthan(f519_1, 0)
        f519_2 = OLD_Input_EIA_Jet_Fuel_Price.F519()
        d519_1 = OLD_Input_EIA_Jet_Fuel_Price.D519()
        var_2 = divide(f519_2, d519_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A520():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A520
    value = 46539
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B520():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B520
    value = 0
    formula = "=D520*$B$3"
    @eval_fn
    def B520():
        d520_1 = OLD_Input_EIA_Jet_Fuel_Price.D520()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d520_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C520():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C520
    value = 46553
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E520():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E520
    value = None
    formula = '''=IF(F520>0,F520/D520,"")'''
    @eval_fn
    def E520():
        f520_1 = OLD_Input_EIA_Jet_Fuel_Price.F520()
        var_1 = greaterthan(f520_1, 0)
        f520_2 = OLD_Input_EIA_Jet_Fuel_Price.F520()
        d520_1 = OLD_Input_EIA_Jet_Fuel_Price.D520()
        var_2 = divide(f520_2, d520_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A521():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A521
    value = 46569
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B521():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B521
    value = 0
    formula = "=D521*$B$3"
    @eval_fn
    def B521():
        d521_1 = OLD_Input_EIA_Jet_Fuel_Price.D521()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d521_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C521():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C521
    value = 46583
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E521():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E521
    value = None
    formula = '''=IF(F521>0,F521/D521,"")'''
    @eval_fn
    def E521():
        f521_1 = OLD_Input_EIA_Jet_Fuel_Price.F521()
        var_1 = greaterthan(f521_1, 0)
        f521_2 = OLD_Input_EIA_Jet_Fuel_Price.F521()
        d521_1 = OLD_Input_EIA_Jet_Fuel_Price.D521()
        var_2 = divide(f521_2, d521_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A522():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A522
    value = 46600
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B522():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B522
    value = 0
    formula = "=D522*$B$3"
    @eval_fn
    def B522():
        d522_1 = OLD_Input_EIA_Jet_Fuel_Price.D522()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d522_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C522():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C522
    value = 46614
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E522():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E522
    value = None
    formula = '''=IF(F522>0,F522/D522,"")'''
    @eval_fn
    def E522():
        f522_1 = OLD_Input_EIA_Jet_Fuel_Price.F522()
        var_1 = greaterthan(f522_1, 0)
        f522_2 = OLD_Input_EIA_Jet_Fuel_Price.F522()
        d522_1 = OLD_Input_EIA_Jet_Fuel_Price.D522()
        var_2 = divide(f522_2, d522_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A523():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A523
    value = 46631
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B523():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B523
    value = 0
    formula = "=D523*$B$3"
    @eval_fn
    def B523():
        d523_1 = OLD_Input_EIA_Jet_Fuel_Price.D523()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d523_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C523():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C523
    value = 46645
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E523():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E523
    value = None
    formula = '''=IF(F523>0,F523/D523,"")'''
    @eval_fn
    def E523():
        f523_1 = OLD_Input_EIA_Jet_Fuel_Price.F523()
        var_1 = greaterthan(f523_1, 0)
        f523_2 = OLD_Input_EIA_Jet_Fuel_Price.F523()
        d523_1 = OLD_Input_EIA_Jet_Fuel_Price.D523()
        var_2 = divide(f523_2, d523_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A524():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A524
    value = 46661
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B524():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B524
    value = 0
    formula = "=D524*$B$3"
    @eval_fn
    def B524():
        d524_1 = OLD_Input_EIA_Jet_Fuel_Price.D524()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d524_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C524():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C524
    value = 46675
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E524():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E524
    value = None
    formula = '''=IF(F524>0,F524/D524,"")'''
    @eval_fn
    def E524():
        f524_1 = OLD_Input_EIA_Jet_Fuel_Price.F524()
        var_1 = greaterthan(f524_1, 0)
        f524_2 = OLD_Input_EIA_Jet_Fuel_Price.F524()
        d524_1 = OLD_Input_EIA_Jet_Fuel_Price.D524()
        var_2 = divide(f524_2, d524_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A525():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A525
    value = 46692
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B525():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B525
    value = 0
    formula = "=D525*$B$3"
    @eval_fn
    def B525():
        d525_1 = OLD_Input_EIA_Jet_Fuel_Price.D525()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d525_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C525():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C525
    value = 46706
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E525():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E525
    value = None
    formula = '''=IF(F525>0,F525/D525,"")'''
    @eval_fn
    def E525():
        f525_1 = OLD_Input_EIA_Jet_Fuel_Price.F525()
        var_1 = greaterthan(f525_1, 0)
        f525_2 = OLD_Input_EIA_Jet_Fuel_Price.F525()
        d525_1 = OLD_Input_EIA_Jet_Fuel_Price.D525()
        var_2 = divide(f525_2, d525_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A526():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A526
    value = 46722
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B526():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B526
    value = 0
    formula = "=D526*$B$3"
    @eval_fn
    def B526():
        d526_1 = OLD_Input_EIA_Jet_Fuel_Price.D526()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d526_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C526():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C526
    value = 46736
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E526():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E526
    value = None
    formula = '''=IF(F526>0,F526/D526,"")'''
    @eval_fn
    def E526():
        f526_1 = OLD_Input_EIA_Jet_Fuel_Price.F526()
        var_1 = greaterthan(f526_1, 0)
        f526_2 = OLD_Input_EIA_Jet_Fuel_Price.F526()
        d526_1 = OLD_Input_EIA_Jet_Fuel_Price.D526()
        var_2 = divide(f526_2, d526_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A527():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A527
    value = 46753
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B527():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B527
    value = 0
    formula = "=D527*$B$3"
    @eval_fn
    def B527():
        d527_1 = OLD_Input_EIA_Jet_Fuel_Price.D527()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d527_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C527():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C527
    value = 46767
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E527():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E527
    value = None
    formula = '''=IF(F527>0,F527/D527,"")'''
    @eval_fn
    def E527():
        f527_1 = OLD_Input_EIA_Jet_Fuel_Price.F527()
        var_1 = greaterthan(f527_1, 0)
        f527_2 = OLD_Input_EIA_Jet_Fuel_Price.F527()
        d527_1 = OLD_Input_EIA_Jet_Fuel_Price.D527()
        var_2 = divide(f527_2, d527_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A528():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A528
    value = 46784
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B528():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B528
    value = 0
    formula = "=D528*$B$3"
    @eval_fn
    def B528():
        d528_1 = OLD_Input_EIA_Jet_Fuel_Price.D528()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d528_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C528():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C528
    value = 46798
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E528():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E528
    value = None
    formula = '''=IF(F528>0,F528/D528,"")'''
    @eval_fn
    def E528():
        f528_1 = OLD_Input_EIA_Jet_Fuel_Price.F528()
        var_1 = greaterthan(f528_1, 0)
        f528_2 = OLD_Input_EIA_Jet_Fuel_Price.F528()
        d528_1 = OLD_Input_EIA_Jet_Fuel_Price.D528()
        var_2 = divide(f528_2, d528_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A529():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A529
    value = 46813
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B529():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B529
    value = 0
    formula = "=D529*$B$3"
    @eval_fn
    def B529():
        d529_1 = OLD_Input_EIA_Jet_Fuel_Price.D529()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d529_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C529():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C529
    value = 46827
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E529():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E529
    value = None
    formula = '''=IF(F529>0,F529/D529,"")'''
    @eval_fn
    def E529():
        f529_1 = OLD_Input_EIA_Jet_Fuel_Price.F529()
        var_1 = greaterthan(f529_1, 0)
        f529_2 = OLD_Input_EIA_Jet_Fuel_Price.F529()
        d529_1 = OLD_Input_EIA_Jet_Fuel_Price.D529()
        var_2 = divide(f529_2, d529_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A530():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A530
    value = 46844
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B530():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B530
    value = 0
    formula = "=D530*$B$3"
    @eval_fn
    def B530():
        d530_1 = OLD_Input_EIA_Jet_Fuel_Price.D530()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d530_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C530():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C530
    value = 46858
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E530():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E530
    value = None
    formula = '''=IF(F530>0,F530/D530,"")'''
    @eval_fn
    def E530():
        f530_1 = OLD_Input_EIA_Jet_Fuel_Price.F530()
        var_1 = greaterthan(f530_1, 0)
        f530_2 = OLD_Input_EIA_Jet_Fuel_Price.F530()
        d530_1 = OLD_Input_EIA_Jet_Fuel_Price.D530()
        var_2 = divide(f530_2, d530_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A531():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A531
    value = 46874
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B531():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B531
    value = 0
    formula = "=D531*$B$3"
    @eval_fn
    def B531():
        d531_1 = OLD_Input_EIA_Jet_Fuel_Price.D531()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d531_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C531():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C531
    value = 46888
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E531():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E531
    value = None
    formula = '''=IF(F531>0,F531/D531,"")'''
    @eval_fn
    def E531():
        f531_1 = OLD_Input_EIA_Jet_Fuel_Price.F531()
        var_1 = greaterthan(f531_1, 0)
        f531_2 = OLD_Input_EIA_Jet_Fuel_Price.F531()
        d531_1 = OLD_Input_EIA_Jet_Fuel_Price.D531()
        var_2 = divide(f531_2, d531_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A532():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A532
    value = 46905
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B532():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B532
    value = 0
    formula = "=D532*$B$3"
    @eval_fn
    def B532():
        d532_1 = OLD_Input_EIA_Jet_Fuel_Price.D532()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d532_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C532():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C532
    value = 46919
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E532():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E532
    value = None
    formula = '''=IF(F532>0,F532/D532,"")'''
    @eval_fn
    def E532():
        f532_1 = OLD_Input_EIA_Jet_Fuel_Price.F532()
        var_1 = greaterthan(f532_1, 0)
        f532_2 = OLD_Input_EIA_Jet_Fuel_Price.F532()
        d532_1 = OLD_Input_EIA_Jet_Fuel_Price.D532()
        var_2 = divide(f532_2, d532_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A533():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A533
    value = 46935
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B533():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B533
    value = 0
    formula = "=D533*$B$3"
    @eval_fn
    def B533():
        d533_1 = OLD_Input_EIA_Jet_Fuel_Price.D533()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d533_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C533():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C533
    value = 46949
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E533():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E533
    value = None
    formula = '''=IF(F533>0,F533/D533,"")'''
    @eval_fn
    def E533():
        f533_1 = OLD_Input_EIA_Jet_Fuel_Price.F533()
        var_1 = greaterthan(f533_1, 0)
        f533_2 = OLD_Input_EIA_Jet_Fuel_Price.F533()
        d533_1 = OLD_Input_EIA_Jet_Fuel_Price.D533()
        var_2 = divide(f533_2, d533_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A534():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A534
    value = 46966
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B534():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B534
    value = 0
    formula = "=D534*$B$3"
    @eval_fn
    def B534():
        d534_1 = OLD_Input_EIA_Jet_Fuel_Price.D534()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d534_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C534():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C534
    value = 46980
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E534():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E534
    value = None
    formula = '''=IF(F534>0,F534/D534,"")'''
    @eval_fn
    def E534():
        f534_1 = OLD_Input_EIA_Jet_Fuel_Price.F534()
        var_1 = greaterthan(f534_1, 0)
        f534_2 = OLD_Input_EIA_Jet_Fuel_Price.F534()
        d534_1 = OLD_Input_EIA_Jet_Fuel_Price.D534()
        var_2 = divide(f534_2, d534_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A535():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A535
    value = 46997
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B535():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B535
    value = 0
    formula = "=D535*$B$3"
    @eval_fn
    def B535():
        d535_1 = OLD_Input_EIA_Jet_Fuel_Price.D535()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d535_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C535():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C535
    value = 47011
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E535():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E535
    value = None
    formula = '''=IF(F535>0,F535/D535,"")'''
    @eval_fn
    def E535():
        f535_1 = OLD_Input_EIA_Jet_Fuel_Price.F535()
        var_1 = greaterthan(f535_1, 0)
        f535_2 = OLD_Input_EIA_Jet_Fuel_Price.F535()
        d535_1 = OLD_Input_EIA_Jet_Fuel_Price.D535()
        var_2 = divide(f535_2, d535_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A536():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A536
    value = 47027
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B536():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B536
    value = 0
    formula = "=D536*$B$3"
    @eval_fn
    def B536():
        d536_1 = OLD_Input_EIA_Jet_Fuel_Price.D536()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d536_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C536():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C536
    value = 47041
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E536():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E536
    value = None
    formula = '''=IF(F536>0,F536/D536,"")'''
    @eval_fn
    def E536():
        f536_1 = OLD_Input_EIA_Jet_Fuel_Price.F536()
        var_1 = greaterthan(f536_1, 0)
        f536_2 = OLD_Input_EIA_Jet_Fuel_Price.F536()
        d536_1 = OLD_Input_EIA_Jet_Fuel_Price.D536()
        var_2 = divide(f536_2, d536_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A537():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A537
    value = 47058
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B537():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B537
    value = 0
    formula = "=D537*$B$3"
    @eval_fn
    def B537():
        d537_1 = OLD_Input_EIA_Jet_Fuel_Price.D537()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d537_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C537():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C537
    value = 47072
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E537():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E537
    value = None
    formula = '''=IF(F537>0,F537/D537,"")'''
    @eval_fn
    def E537():
        f537_1 = OLD_Input_EIA_Jet_Fuel_Price.F537()
        var_1 = greaterthan(f537_1, 0)
        f537_2 = OLD_Input_EIA_Jet_Fuel_Price.F537()
        d537_1 = OLD_Input_EIA_Jet_Fuel_Price.D537()
        var_2 = divide(f537_2, d537_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A538():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A538
    value = 47088
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B538():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B538
    value = 0
    formula = "=D538*$B$3"
    @eval_fn
    def B538():
        d538_1 = OLD_Input_EIA_Jet_Fuel_Price.D538()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d538_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C538():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C538
    value = 47102
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E538():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E538
    value = None
    formula = '''=IF(F538>0,F538/D538,"")'''
    @eval_fn
    def E538():
        f538_1 = OLD_Input_EIA_Jet_Fuel_Price.F538()
        var_1 = greaterthan(f538_1, 0)
        f538_2 = OLD_Input_EIA_Jet_Fuel_Price.F538()
        d538_1 = OLD_Input_EIA_Jet_Fuel_Price.D538()
        var_2 = divide(f538_2, d538_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A539():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A539
    value = 47119
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B539():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B539
    value = 0
    formula = "=D539*$B$3"
    @eval_fn
    def B539():
        d539_1 = OLD_Input_EIA_Jet_Fuel_Price.D539()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d539_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C539():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C539
    value = 47133
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E539():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E539
    value = None
    formula = '''=IF(F539>0,F539/D539,"")'''
    @eval_fn
    def E539():
        f539_1 = OLD_Input_EIA_Jet_Fuel_Price.F539()
        var_1 = greaterthan(f539_1, 0)
        f539_2 = OLD_Input_EIA_Jet_Fuel_Price.F539()
        d539_1 = OLD_Input_EIA_Jet_Fuel_Price.D539()
        var_2 = divide(f539_2, d539_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A540():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A540
    value = 47150
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B540():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B540
    value = 0
    formula = "=D540*$B$3"
    @eval_fn
    def B540():
        d540_1 = OLD_Input_EIA_Jet_Fuel_Price.D540()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d540_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C540():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C540
    value = 47164
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E540():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E540
    value = None
    formula = '''=IF(F540>0,F540/D540,"")'''
    @eval_fn
    def E540():
        f540_1 = OLD_Input_EIA_Jet_Fuel_Price.F540()
        var_1 = greaterthan(f540_1, 0)
        f540_2 = OLD_Input_EIA_Jet_Fuel_Price.F540()
        d540_1 = OLD_Input_EIA_Jet_Fuel_Price.D540()
        var_2 = divide(f540_2, d540_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A541():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A541
    value = 47178
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B541():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B541
    value = 0
    formula = "=D541*$B$3"
    @eval_fn
    def B541():
        d541_1 = OLD_Input_EIA_Jet_Fuel_Price.D541()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d541_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C541():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C541
    value = 47192
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E541():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E541
    value = None
    formula = '''=IF(F541>0,F541/D541,"")'''
    @eval_fn
    def E541():
        f541_1 = OLD_Input_EIA_Jet_Fuel_Price.F541()
        var_1 = greaterthan(f541_1, 0)
        f541_2 = OLD_Input_EIA_Jet_Fuel_Price.F541()
        d541_1 = OLD_Input_EIA_Jet_Fuel_Price.D541()
        var_2 = divide(f541_2, d541_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A542():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A542
    value = 47209
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B542():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B542
    value = 0
    formula = "=D542*$B$3"
    @eval_fn
    def B542():
        d542_1 = OLD_Input_EIA_Jet_Fuel_Price.D542()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d542_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C542():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C542
    value = 47223
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E542():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E542
    value = None
    formula = '''=IF(F542>0,F542/D542,"")'''
    @eval_fn
    def E542():
        f542_1 = OLD_Input_EIA_Jet_Fuel_Price.F542()
        var_1 = greaterthan(f542_1, 0)
        f542_2 = OLD_Input_EIA_Jet_Fuel_Price.F542()
        d542_1 = OLD_Input_EIA_Jet_Fuel_Price.D542()
        var_2 = divide(f542_2, d542_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A543():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A543
    value = 47239
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B543():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B543
    value = 0
    formula = "=D543*$B$3"
    @eval_fn
    def B543():
        d543_1 = OLD_Input_EIA_Jet_Fuel_Price.D543()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d543_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C543():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C543
    value = 47253
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E543():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E543
    value = None
    formula = '''=IF(F543>0,F543/D543,"")'''
    @eval_fn
    def E543():
        f543_1 = OLD_Input_EIA_Jet_Fuel_Price.F543()
        var_1 = greaterthan(f543_1, 0)
        f543_2 = OLD_Input_EIA_Jet_Fuel_Price.F543()
        d543_1 = OLD_Input_EIA_Jet_Fuel_Price.D543()
        var_2 = divide(f543_2, d543_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A544():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A544
    value = 47270
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B544():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B544
    value = 0
    formula = "=D544*$B$3"
    @eval_fn
    def B544():
        d544_1 = OLD_Input_EIA_Jet_Fuel_Price.D544()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d544_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C544():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C544
    value = 47284
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E544():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E544
    value = None
    formula = '''=IF(F544>0,F544/D544,"")'''
    @eval_fn
    def E544():
        f544_1 = OLD_Input_EIA_Jet_Fuel_Price.F544()
        var_1 = greaterthan(f544_1, 0)
        f544_2 = OLD_Input_EIA_Jet_Fuel_Price.F544()
        d544_1 = OLD_Input_EIA_Jet_Fuel_Price.D544()
        var_2 = divide(f544_2, d544_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A545():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A545
    value = 47300
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B545():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B545
    value = 0
    formula = "=D545*$B$3"
    @eval_fn
    def B545():
        d545_1 = OLD_Input_EIA_Jet_Fuel_Price.D545()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d545_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C545():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C545
    value = 47314
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E545():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E545
    value = None
    formula = '''=IF(F545>0,F545/D545,"")'''
    @eval_fn
    def E545():
        f545_1 = OLD_Input_EIA_Jet_Fuel_Price.F545()
        var_1 = greaterthan(f545_1, 0)
        f545_2 = OLD_Input_EIA_Jet_Fuel_Price.F545()
        d545_1 = OLD_Input_EIA_Jet_Fuel_Price.D545()
        var_2 = divide(f545_2, d545_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A546():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A546
    value = 47331
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B546():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B546
    value = 0
    formula = "=D546*$B$3"
    @eval_fn
    def B546():
        d546_1 = OLD_Input_EIA_Jet_Fuel_Price.D546()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d546_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C546():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C546
    value = 47345
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E546():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E546
    value = None
    formula = '''=IF(F546>0,F546/D546,"")'''
    @eval_fn
    def E546():
        f546_1 = OLD_Input_EIA_Jet_Fuel_Price.F546()
        var_1 = greaterthan(f546_1, 0)
        f546_2 = OLD_Input_EIA_Jet_Fuel_Price.F546()
        d546_1 = OLD_Input_EIA_Jet_Fuel_Price.D546()
        var_2 = divide(f546_2, d546_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A547():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A547
    value = 47362
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B547():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B547
    value = 0
    formula = "=D547*$B$3"
    @eval_fn
    def B547():
        d547_1 = OLD_Input_EIA_Jet_Fuel_Price.D547()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d547_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C547():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C547
    value = 47376
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E547():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E547
    value = None
    formula = '''=IF(F547>0,F547/D547,"")'''
    @eval_fn
    def E547():
        f547_1 = OLD_Input_EIA_Jet_Fuel_Price.F547()
        var_1 = greaterthan(f547_1, 0)
        f547_2 = OLD_Input_EIA_Jet_Fuel_Price.F547()
        d547_1 = OLD_Input_EIA_Jet_Fuel_Price.D547()
        var_2 = divide(f547_2, d547_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A548():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A548
    value = 47392
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B548():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B548
    value = 0
    formula = "=D548*$B$3"
    @eval_fn
    def B548():
        d548_1 = OLD_Input_EIA_Jet_Fuel_Price.D548()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d548_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C548():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C548
    value = 47406
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E548():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E548
    value = None
    formula = '''=IF(F548>0,F548/D548,"")'''
    @eval_fn
    def E548():
        f548_1 = OLD_Input_EIA_Jet_Fuel_Price.F548()
        var_1 = greaterthan(f548_1, 0)
        f548_2 = OLD_Input_EIA_Jet_Fuel_Price.F548()
        d548_1 = OLD_Input_EIA_Jet_Fuel_Price.D548()
        var_2 = divide(f548_2, d548_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A549():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A549
    value = 47423
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B549():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B549
    value = 0
    formula = "=D549*$B$3"
    @eval_fn
    def B549():
        d549_1 = OLD_Input_EIA_Jet_Fuel_Price.D549()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d549_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C549():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C549
    value = 47437
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E549():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E549
    value = None
    formula = '''=IF(F549>0,F549/D549,"")'''
    @eval_fn
    def E549():
        f549_1 = OLD_Input_EIA_Jet_Fuel_Price.F549()
        var_1 = greaterthan(f549_1, 0)
        f549_2 = OLD_Input_EIA_Jet_Fuel_Price.F549()
        d549_1 = OLD_Input_EIA_Jet_Fuel_Price.D549()
        var_2 = divide(f549_2, d549_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A550():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A550
    value = 47453
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B550():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B550
    value = 0
    formula = "=D550*$B$3"
    @eval_fn
    def B550():
        d550_1 = OLD_Input_EIA_Jet_Fuel_Price.D550()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d550_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C550():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C550
    value = 47467
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E550():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E550
    value = None
    formula = '''=IF(F550>0,F550/D550,"")'''
    @eval_fn
    def E550():
        f550_1 = OLD_Input_EIA_Jet_Fuel_Price.F550()
        var_1 = greaterthan(f550_1, 0)
        f550_2 = OLD_Input_EIA_Jet_Fuel_Price.F550()
        d550_1 = OLD_Input_EIA_Jet_Fuel_Price.D550()
        var_2 = divide(f550_2, d550_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A551():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A551
    value = 47484
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B551():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B551
    value = 0
    formula = "=D551*$B$3"
    @eval_fn
    def B551():
        d551_1 = OLD_Input_EIA_Jet_Fuel_Price.D551()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d551_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C551():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C551
    value = 47498
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E551():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E551
    value = None
    formula = '''=IF(F551>0,F551/D551,"")'''
    @eval_fn
    def E551():
        f551_1 = OLD_Input_EIA_Jet_Fuel_Price.F551()
        var_1 = greaterthan(f551_1, 0)
        f551_2 = OLD_Input_EIA_Jet_Fuel_Price.F551()
        d551_1 = OLD_Input_EIA_Jet_Fuel_Price.D551()
        var_2 = divide(f551_2, d551_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A552():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A552
    value = 47515
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B552():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B552
    value = 0
    formula = "=D552*$B$3"
    @eval_fn
    def B552():
        d552_1 = OLD_Input_EIA_Jet_Fuel_Price.D552()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d552_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C552():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C552
    value = 47529
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E552():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E552
    value = None
    formula = '''=IF(F552>0,F552/D552,"")'''
    @eval_fn
    def E552():
        f552_1 = OLD_Input_EIA_Jet_Fuel_Price.F552()
        var_1 = greaterthan(f552_1, 0)
        f552_2 = OLD_Input_EIA_Jet_Fuel_Price.F552()
        d552_1 = OLD_Input_EIA_Jet_Fuel_Price.D552()
        var_2 = divide(f552_2, d552_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A553():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A553
    value = 47543
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B553():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B553
    value = 0
    formula = "=D553*$B$3"
    @eval_fn
    def B553():
        d553_1 = OLD_Input_EIA_Jet_Fuel_Price.D553()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d553_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C553():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C553
    value = 47557
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E553():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E553
    value = None
    formula = '''=IF(F553>0,F553/D553,"")'''
    @eval_fn
    def E553():
        f553_1 = OLD_Input_EIA_Jet_Fuel_Price.F553()
        var_1 = greaterthan(f553_1, 0)
        f553_2 = OLD_Input_EIA_Jet_Fuel_Price.F553()
        d553_1 = OLD_Input_EIA_Jet_Fuel_Price.D553()
        var_2 = divide(f553_2, d553_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A554():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A554
    value = 47574
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B554():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B554
    value = 0
    formula = "=D554*$B$3"
    @eval_fn
    def B554():
        d554_1 = OLD_Input_EIA_Jet_Fuel_Price.D554()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d554_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C554():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C554
    value = 47588
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E554():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E554
    value = None
    formula = '''=IF(F554>0,F554/D554,"")'''
    @eval_fn
    def E554():
        f554_1 = OLD_Input_EIA_Jet_Fuel_Price.F554()
        var_1 = greaterthan(f554_1, 0)
        f554_2 = OLD_Input_EIA_Jet_Fuel_Price.F554()
        d554_1 = OLD_Input_EIA_Jet_Fuel_Price.D554()
        var_2 = divide(f554_2, d554_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A555():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A555
    value = 47604
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B555():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B555
    value = 0
    formula = "=D555*$B$3"
    @eval_fn
    def B555():
        d555_1 = OLD_Input_EIA_Jet_Fuel_Price.D555()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d555_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C555():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C555
    value = 47618
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E555():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E555
    value = None
    formula = '''=IF(F555>0,F555/D555,"")'''
    @eval_fn
    def E555():
        f555_1 = OLD_Input_EIA_Jet_Fuel_Price.F555()
        var_1 = greaterthan(f555_1, 0)
        f555_2 = OLD_Input_EIA_Jet_Fuel_Price.F555()
        d555_1 = OLD_Input_EIA_Jet_Fuel_Price.D555()
        var_2 = divide(f555_2, d555_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A556():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A556
    value = 47635
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B556():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B556
    value = 0
    formula = "=D556*$B$3"
    @eval_fn
    def B556():
        d556_1 = OLD_Input_EIA_Jet_Fuel_Price.D556()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d556_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C556():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C556
    value = 47649
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E556():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E556
    value = None
    formula = '''=IF(F556>0,F556/D556,"")'''
    @eval_fn
    def E556():
        f556_1 = OLD_Input_EIA_Jet_Fuel_Price.F556()
        var_1 = greaterthan(f556_1, 0)
        f556_2 = OLD_Input_EIA_Jet_Fuel_Price.F556()
        d556_1 = OLD_Input_EIA_Jet_Fuel_Price.D556()
        var_2 = divide(f556_2, d556_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A557():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A557
    value = 47665
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B557():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B557
    value = 0
    formula = "=D557*$B$3"
    @eval_fn
    def B557():
        d557_1 = OLD_Input_EIA_Jet_Fuel_Price.D557()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d557_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C557():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C557
    value = 47679
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E557():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E557
    value = None
    formula = '''=IF(F557>0,F557/D557,"")'''
    @eval_fn
    def E557():
        f557_1 = OLD_Input_EIA_Jet_Fuel_Price.F557()
        var_1 = greaterthan(f557_1, 0)
        f557_2 = OLD_Input_EIA_Jet_Fuel_Price.F557()
        d557_1 = OLD_Input_EIA_Jet_Fuel_Price.D557()
        var_2 = divide(f557_2, d557_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A558():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A558
    value = 47696
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B558():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B558
    value = 0
    formula = "=D558*$B$3"
    @eval_fn
    def B558():
        d558_1 = OLD_Input_EIA_Jet_Fuel_Price.D558()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d558_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C558():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C558
    value = 47710
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E558():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E558
    value = None
    formula = '''=IF(F558>0,F558/D558,"")'''
    @eval_fn
    def E558():
        f558_1 = OLD_Input_EIA_Jet_Fuel_Price.F558()
        var_1 = greaterthan(f558_1, 0)
        f558_2 = OLD_Input_EIA_Jet_Fuel_Price.F558()
        d558_1 = OLD_Input_EIA_Jet_Fuel_Price.D558()
        var_2 = divide(f558_2, d558_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A559():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A559
    value = 47727
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B559():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B559
    value = 0
    formula = "=D559*$B$3"
    @eval_fn
    def B559():
        d559_1 = OLD_Input_EIA_Jet_Fuel_Price.D559()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d559_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C559():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C559
    value = 47741
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E559():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E559
    value = None
    formula = '''=IF(F559>0,F559/D559,"")'''
    @eval_fn
    def E559():
        f559_1 = OLD_Input_EIA_Jet_Fuel_Price.F559()
        var_1 = greaterthan(f559_1, 0)
        f559_2 = OLD_Input_EIA_Jet_Fuel_Price.F559()
        d559_1 = OLD_Input_EIA_Jet_Fuel_Price.D559()
        var_2 = divide(f559_2, d559_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A560():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A560
    value = 47757
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B560():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B560
    value = 0
    formula = "=D560*$B$3"
    @eval_fn
    def B560():
        d560_1 = OLD_Input_EIA_Jet_Fuel_Price.D560()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d560_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C560():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C560
    value = 47771
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E560():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E560
    value = None
    formula = '''=IF(F560>0,F560/D560,"")'''
    @eval_fn
    def E560():
        f560_1 = OLD_Input_EIA_Jet_Fuel_Price.F560()
        var_1 = greaterthan(f560_1, 0)
        f560_2 = OLD_Input_EIA_Jet_Fuel_Price.F560()
        d560_1 = OLD_Input_EIA_Jet_Fuel_Price.D560()
        var_2 = divide(f560_2, d560_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A561():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A561
    value = 47788
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B561():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B561
    value = 0
    formula = "=D561*$B$3"
    @eval_fn
    def B561():
        d561_1 = OLD_Input_EIA_Jet_Fuel_Price.D561()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d561_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C561():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C561
    value = 47802
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E561():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E561
    value = None
    formula = '''=IF(F561>0,F561/D561,"")'''
    @eval_fn
    def E561():
        f561_1 = OLD_Input_EIA_Jet_Fuel_Price.F561()
        var_1 = greaterthan(f561_1, 0)
        f561_2 = OLD_Input_EIA_Jet_Fuel_Price.F561()
        d561_1 = OLD_Input_EIA_Jet_Fuel_Price.D561()
        var_2 = divide(f561_2, d561_1)
        var_3 = IF(var_1, var_2, "")
        return var_3

@register(OLD_Input_EIA_Jet_Fuel_Price)
class A562():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!A562
    value = 47818
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class B562():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!B562
    value = 0
    formula = "=D562*$B$3"
    @eval_fn
    def B562():
        d562_1 = OLD_Input_EIA_Jet_Fuel_Price.D562()
        b3_1 = OLD_Input_EIA_Jet_Fuel_Price.B3()
        var_1 = mult(d562_1, b3_1)
        return var_1

@register(OLD_Input_EIA_Jet_Fuel_Price)
class C562():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!C562
    value = 47832
    isdatetime = True

@register(OLD_Input_EIA_Jet_Fuel_Price)
class E562():
    # 'OLD_Input_EIA_Jet_Fuel_Price'!E562
    value = None
    formula = '''=IF(F562>0,F562/D562,"")'''
    @eval_fn
    def E562():
        f562_1 = OLD_Input_EIA_Jet_Fuel_Price.F562()
        var_1 = greaterthan(f562_1, 0)
        f562_2 = OLD_Input_EIA_Jet_Fuel_Price.F562()
        d562_1 = OLD_Input_EIA_Jet_Fuel_Price.D562()
        var_2 = divide(f562_2, d562_1)
        var_3 = IF(var_1, var_2, "")
        return var_3