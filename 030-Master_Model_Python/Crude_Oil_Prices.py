# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Crude_Oil_Prices = Worksheet('Crude_Oil_Prices', 10, 10)



@register(Crude_Oil_Prices)
class A1():
    # 'Crude_Oil_Prices'!A1
    value = "Data 1: Crude Oil"

@register(Crude_Oil_Prices)
class A2():
    # 'Crude_Oil_Prices'!A2
    value = "Sourcekey"

@register(Crude_Oil_Prices)
class B2():
    # 'Crude_Oil_Prices'!B2
    value = "RWTC"

@register(Crude_Oil_Prices)
class C2():
    # 'Crude_Oil_Prices'!C2
    value = "RBRTE"

@register(Crude_Oil_Prices)
class A4():
    # 'Crude_Oil_Prices'!A4
    value = "Date"

@register(Crude_Oil_Prices)
class B4():
    # 'Crude_Oil_Prices'!B4
    value = "Cushing, OK WTI Spot Price FOB (Dollars per Barrel)"

@register(Crude_Oil_Prices)
class C4():
    # 'Crude_Oil_Prices'!C4
    value = "Europe Brent Spot Price FOB (Dollars per Barrel)"

@register(Crude_Oil_Prices)
class A5():
    # 'Crude_Oil_Prices'!A5
    value = 31427
    isdatetime = True

@register(Crude_Oil_Prices)
class B5():
    # 'Crude_Oil_Prices'!B5
    value = 22.93
    formula = "='Input EIA Crude WTI'!B3"
    @eval_fn
    def B5():
        b3_1 = Input_EIA_Crude_WTI.B3()
        return b3_1

@register(Crude_Oil_Prices)
class A6():
    # 'Crude_Oil_Prices'!A6
    value = 31458
    isdatetime = True

@register(Crude_Oil_Prices)
class B6():
    # 'Crude_Oil_Prices'!B6
    value = 15.46
    formula = "='Input EIA Crude WTI'!B4"
    @eval_fn
    def B6():
        b4_1 = Input_EIA_Crude_WTI.B4()
        return b4_1

@register(Crude_Oil_Prices)
class A7():
    # 'Crude_Oil_Prices'!A7
    value = 31486
    isdatetime = True

@register(Crude_Oil_Prices)
class B7():
    # 'Crude_Oil_Prices'!B7
    value = 12.61
    formula = "='Input EIA Crude WTI'!B5"
    @eval_fn
    def B7():
        b5_1 = Input_EIA_Crude_WTI.B5()
        return b5_1

@register(Crude_Oil_Prices)
class A8():
    # 'Crude_Oil_Prices'!A8
    value = 31517
    isdatetime = True

@register(Crude_Oil_Prices)
class B8():
    # 'Crude_Oil_Prices'!B8
    value = 12.84
    formula = "='Input EIA Crude WTI'!B6"
    @eval_fn
    def B8():
        b6_1 = Input_EIA_Crude_WTI.B6()
        return b6_1

@register(Crude_Oil_Prices)
class A9():
    # 'Crude_Oil_Prices'!A9
    value = 31547
    isdatetime = True

@register(Crude_Oil_Prices)
class B9():
    # 'Crude_Oil_Prices'!B9
    value = 15.38
    formula = "='Input EIA Crude WTI'!B7"
    @eval_fn
    def B9():
        b7_1 = Input_EIA_Crude_WTI.B7()
        return b7_1

@register(Crude_Oil_Prices)
class A10():
    # 'Crude_Oil_Prices'!A10
    value = 31578
    isdatetime = True

@register(Crude_Oil_Prices)
class B10():
    # 'Crude_Oil_Prices'!B10
    value = 13.43
    formula = "='Input EIA Crude WTI'!B8"
    @eval_fn
    def B10():
        b8_1 = Input_EIA_Crude_WTI.B8()
        return b8_1

@register(Crude_Oil_Prices)
class A11():
    # 'Crude_Oil_Prices'!A11
    value = 31608
    isdatetime = True

@register(Crude_Oil_Prices)
class B11():
    # 'Crude_Oil_Prices'!B11
    value = 11.59
    formula = "='Input EIA Crude WTI'!B9"
    @eval_fn
    def B11():
        b9_1 = Input_EIA_Crude_WTI.B9()
        return b9_1

@register(Crude_Oil_Prices)
class A12():
    # 'Crude_Oil_Prices'!A12
    value = 31639
    isdatetime = True

@register(Crude_Oil_Prices)
class B12():
    # 'Crude_Oil_Prices'!B12
    value = 15.1
    formula = "='Input EIA Crude WTI'!B10"
    @eval_fn
    def B12():
        b10_1 = Input_EIA_Crude_WTI.B10()
        return b10_1

@register(Crude_Oil_Prices)
class A13():
    # 'Crude_Oil_Prices'!A13
    value = 31670
    isdatetime = True

@register(Crude_Oil_Prices)
class B13():
    # 'Crude_Oil_Prices'!B13
    value = 14.87
    formula = "='Input EIA Crude WTI'!B11"
    @eval_fn
    def B13():
        b11_1 = Input_EIA_Crude_WTI.B11()
        return b11_1

@register(Crude_Oil_Prices)
class A14():
    # 'Crude_Oil_Prices'!A14
    value = 31700
    isdatetime = True

@register(Crude_Oil_Prices)
class B14():
    # 'Crude_Oil_Prices'!B14
    value = 14.9
    formula = "='Input EIA Crude WTI'!B12"
    @eval_fn
    def B14():
        b12_1 = Input_EIA_Crude_WTI.B12()
        return b12_1

@register(Crude_Oil_Prices)
class A15():
    # 'Crude_Oil_Prices'!A15
    value = 31731
    isdatetime = True

@register(Crude_Oil_Prices)
class B15():
    # 'Crude_Oil_Prices'!B15
    value = 15.22
    formula = "='Input EIA Crude WTI'!B13"
    @eval_fn
    def B15():
        b13_1 = Input_EIA_Crude_WTI.B13()
        return b13_1

@register(Crude_Oil_Prices)
class A16():
    # 'Crude_Oil_Prices'!A16
    value = 31761
    isdatetime = True

@register(Crude_Oil_Prices)
class B16():
    # 'Crude_Oil_Prices'!B16
    value = 16.11
    formula = "='Input EIA Crude WTI'!B14"
    @eval_fn
    def B16():
        b14_1 = Input_EIA_Crude_WTI.B14()
        return b14_1

@register(Crude_Oil_Prices)
class A17():
    # 'Crude_Oil_Prices'!A17
    value = 31792
    isdatetime = True

@register(Crude_Oil_Prices)
class B17():
    # 'Crude_Oil_Prices'!B17
    value = 18.65
    formula = "='Input EIA Crude WTI'!B15"
    @eval_fn
    def B17():
        b15_1 = Input_EIA_Crude_WTI.B15()
        return b15_1

@register(Crude_Oil_Prices)
class A18():
    # 'Crude_Oil_Prices'!A18
    value = 31823
    isdatetime = True

@register(Crude_Oil_Prices)
class B18():
    # 'Crude_Oil_Prices'!B18
    value = 17.75
    formula = "='Input EIA Crude WTI'!B16"
    @eval_fn
    def B18():
        b16_1 = Input_EIA_Crude_WTI.B16()
        return b16_1

@register(Crude_Oil_Prices)
class A19():
    # 'Crude_Oil_Prices'!A19
    value = 31851
    isdatetime = True

@register(Crude_Oil_Prices)
class B19():
    # 'Crude_Oil_Prices'!B19
    value = 18.3
    formula = "='Input EIA Crude WTI'!B17"
    @eval_fn
    def B19():
        b17_1 = Input_EIA_Crude_WTI.B17()
        return b17_1

@register(Crude_Oil_Prices)
class A20():
    # 'Crude_Oil_Prices'!A20
    value = 31882
    isdatetime = True

@register(Crude_Oil_Prices)
class B20():
    # 'Crude_Oil_Prices'!B20
    value = 18.68
    formula = "='Input EIA Crude WTI'!B18"
    @eval_fn
    def B20():
        b18_1 = Input_EIA_Crude_WTI.B18()
        return b18_1

@register(Crude_Oil_Prices)
class A21():
    # 'Crude_Oil_Prices'!A21
    value = 31912
    isdatetime = True

@register(Crude_Oil_Prices)
class B21():
    # 'Crude_Oil_Prices'!B21
    value = 19.44
    formula = "='Input EIA Crude WTI'!B19"
    @eval_fn
    def B21():
        b19_1 = Input_EIA_Crude_WTI.B19()
        return b19_1

@register(Crude_Oil_Prices)
class C21():
    # 'Crude_Oil_Prices'!C21
    value = 18.58
    formula = "='Input EIA Crude Europe Brent'!B3"
    @eval_fn
    def C21():
        b3_1 = Input_EIA_Crude_Europe_Brent.B3()
        return b3_1

@register(Crude_Oil_Prices)
class A22():
    # 'Crude_Oil_Prices'!A22
    value = 31943
    isdatetime = True

@register(Crude_Oil_Prices)
class B22():
    # 'Crude_Oil_Prices'!B22
    value = 20.07
    formula = "='Input EIA Crude WTI'!B20"
    @eval_fn
    def B22():
        b20_1 = Input_EIA_Crude_WTI.B20()
        return b20_1

@register(Crude_Oil_Prices)
class C22():
    # 'Crude_Oil_Prices'!C22
    value = 18.86
    formula = "='Input EIA Crude Europe Brent'!B4"
    @eval_fn
    def C22():
        b4_1 = Input_EIA_Crude_Europe_Brent.B4()
        return b4_1

@register(Crude_Oil_Prices)
class A23():
    # 'Crude_Oil_Prices'!A23
    value = 31973
    isdatetime = True

@register(Crude_Oil_Prices)
class B23():
    # 'Crude_Oil_Prices'!B23
    value = 21.34
    formula = "='Input EIA Crude WTI'!B21"
    @eval_fn
    def B23():
        b21_1 = Input_EIA_Crude_WTI.B21()
        return b21_1

@register(Crude_Oil_Prices)
class C23():
    # 'Crude_Oil_Prices'!C23
    value = 19.86
    formula = "='Input EIA Crude Europe Brent'!B5"
    @eval_fn
    def C23():
        b5_1 = Input_EIA_Crude_Europe_Brent.B5()
        return b5_1

@register(Crude_Oil_Prices)
class A24():
    # 'Crude_Oil_Prices'!A24
    value = 32004
    isdatetime = True

@register(Crude_Oil_Prices)
class B24():
    # 'Crude_Oil_Prices'!B24
    value = 20.31
    formula = "='Input EIA Crude WTI'!B22"
    @eval_fn
    def B24():
        b22_1 = Input_EIA_Crude_WTI.B22()
        return b22_1

@register(Crude_Oil_Prices)
class C24():
    # 'Crude_Oil_Prices'!C24
    value = 18.98
    formula = "='Input EIA Crude Europe Brent'!B6"
    @eval_fn
    def C24():
        b6_1 = Input_EIA_Crude_Europe_Brent.B6()
        return b6_1

@register(Crude_Oil_Prices)
class A25():
    # 'Crude_Oil_Prices'!A25
    value = 32035
    isdatetime = True

@register(Crude_Oil_Prices)
class B25():
    # 'Crude_Oil_Prices'!B25
    value = 19.53
    formula = "='Input EIA Crude WTI'!B23"
    @eval_fn
    def B25():
        b23_1 = Input_EIA_Crude_WTI.B23()
        return b23_1

@register(Crude_Oil_Prices)
class C25():
    # 'Crude_Oil_Prices'!C25
    value = 18.31
    formula = "='Input EIA Crude Europe Brent'!B7"
    @eval_fn
    def C25():
        b7_1 = Input_EIA_Crude_Europe_Brent.B7()
        return b7_1

@register(Crude_Oil_Prices)
class A26():
    # 'Crude_Oil_Prices'!A26
    value = 32065
    isdatetime = True

@register(Crude_Oil_Prices)
class B26():
    # 'Crude_Oil_Prices'!B26
    value = 19.86
    formula = "='Input EIA Crude WTI'!B24"
    @eval_fn
    def B26():
        b24_1 = Input_EIA_Crude_WTI.B24()
        return b24_1

@register(Crude_Oil_Prices)
class C26():
    # 'Crude_Oil_Prices'!C26
    value = 18.76
    formula = "='Input EIA Crude Europe Brent'!B8"
    @eval_fn
    def C26():
        b8_1 = Input_EIA_Crude_Europe_Brent.B8()
        return b8_1

@register(Crude_Oil_Prices)
class A27():
    # 'Crude_Oil_Prices'!A27
    value = 32096
    isdatetime = True

@register(Crude_Oil_Prices)
class B27():
    # 'Crude_Oil_Prices'!B27
    value = 18.85
    formula = "='Input EIA Crude WTI'!B25"
    @eval_fn
    def B27():
        b25_1 = Input_EIA_Crude_WTI.B25()
        return b25_1

@register(Crude_Oil_Prices)
class C27():
    # 'Crude_Oil_Prices'!C27
    value = 17.78
    formula = "='Input EIA Crude Europe Brent'!B9"
    @eval_fn
    def C27():
        b9_1 = Input_EIA_Crude_Europe_Brent.B9()
        return b9_1

@register(Crude_Oil_Prices)
class A28():
    # 'Crude_Oil_Prices'!A28
    value = 32126
    isdatetime = True

@register(Crude_Oil_Prices)
class B28():
    # 'Crude_Oil_Prices'!B28
    value = 17.28
    formula = "='Input EIA Crude WTI'!B26"
    @eval_fn
    def B28():
        b26_1 = Input_EIA_Crude_WTI.B26()
        return b26_1

@register(Crude_Oil_Prices)
class C28():
    # 'Crude_Oil_Prices'!C28
    value = 17.05
    formula = "='Input EIA Crude Europe Brent'!B10"
    @eval_fn
    def C28():
        b10_1 = Input_EIA_Crude_Europe_Brent.B10()
        return b10_1

@register(Crude_Oil_Prices)
class A29():
    # 'Crude_Oil_Prices'!A29
    value = 32157
    isdatetime = True

@register(Crude_Oil_Prices)
class B29():
    # 'Crude_Oil_Prices'!B29
    value = 17.13
    formula = "='Input EIA Crude WTI'!B27"
    @eval_fn
    def B29():
        b27_1 = Input_EIA_Crude_WTI.B27()
        return b27_1

@register(Crude_Oil_Prices)
class C29():
    # 'Crude_Oil_Prices'!C29
    value = 16.75
    formula = "='Input EIA Crude Europe Brent'!B11"
    @eval_fn
    def C29():
        b11_1 = Input_EIA_Crude_Europe_Brent.B11()
        return b11_1

@register(Crude_Oil_Prices)
class A30():
    # 'Crude_Oil_Prices'!A30
    value = 32188
    isdatetime = True

@register(Crude_Oil_Prices)
class B30():
    # 'Crude_Oil_Prices'!B30
    value = 16.8
    formula = "='Input EIA Crude WTI'!B28"
    @eval_fn
    def B30():
        b28_1 = Input_EIA_Crude_WTI.B28()
        return b28_1

@register(Crude_Oil_Prices)
class C30():
    # 'Crude_Oil_Prices'!C30
    value = 15.73
    formula = "='Input EIA Crude Europe Brent'!B12"
    @eval_fn
    def C30():
        b12_1 = Input_EIA_Crude_Europe_Brent.B12()
        return b12_1

@register(Crude_Oil_Prices)
class A31():
    # 'Crude_Oil_Prices'!A31
    value = 32217
    isdatetime = True

@register(Crude_Oil_Prices)
class B31():
    # 'Crude_Oil_Prices'!B31
    value = 16.2
    formula = "='Input EIA Crude WTI'!B29"
    @eval_fn
    def B31():
        b29_1 = Input_EIA_Crude_WTI.B29()
        return b29_1

@register(Crude_Oil_Prices)
class C31():
    # 'Crude_Oil_Prices'!C31
    value = 14.73
    formula = "='Input EIA Crude Europe Brent'!B13"
    @eval_fn
    def C31():
        b13_1 = Input_EIA_Crude_Europe_Brent.B13()
        return b13_1

@register(Crude_Oil_Prices)
class A32():
    # 'Crude_Oil_Prices'!A32
    value = 32248
    isdatetime = True

@register(Crude_Oil_Prices)
class B32():
    # 'Crude_Oil_Prices'!B32
    value = 17.86
    formula = "='Input EIA Crude WTI'!B30"
    @eval_fn
    def B32():
        b30_1 = Input_EIA_Crude_WTI.B30()
        return b30_1

@register(Crude_Oil_Prices)
class C32():
    # 'Crude_Oil_Prices'!C32
    value = 16.6
    formula = "='Input EIA Crude Europe Brent'!B14"
    @eval_fn
    def C32():
        b14_1 = Input_EIA_Crude_Europe_Brent.B14()
        return b14_1

@register(Crude_Oil_Prices)
class A33():
    # 'Crude_Oil_Prices'!A33
    value = 32278
    isdatetime = True

@register(Crude_Oil_Prices)
class B33():
    # 'Crude_Oil_Prices'!B33
    value = 17.42
    formula = "='Input EIA Crude WTI'!B31"
    @eval_fn
    def B33():
        b31_1 = Input_EIA_Crude_WTI.B31()
        return b31_1

@register(Crude_Oil_Prices)
class C33():
    # 'Crude_Oil_Prices'!C33
    value = 16.31
    formula = "='Input EIA Crude Europe Brent'!B15"
    @eval_fn
    def C33():
        b15_1 = Input_EIA_Crude_Europe_Brent.B15()
        return b15_1

@register(Crude_Oil_Prices)
class A34():
    # 'Crude_Oil_Prices'!A34
    value = 32309
    isdatetime = True

@register(Crude_Oil_Prices)
class B34():
    # 'Crude_Oil_Prices'!B34
    value = 16.53
    formula = "='Input EIA Crude WTI'!B32"
    @eval_fn
    def B34():
        b32_1 = Input_EIA_Crude_WTI.B32()
        return b32_1

@register(Crude_Oil_Prices)
class C34():
    # 'Crude_Oil_Prices'!C34
    value = 15.54
    formula = "='Input EIA Crude Europe Brent'!B16"
    @eval_fn
    def C34():
        b16_1 = Input_EIA_Crude_Europe_Brent.B16()
        return b16_1

@register(Crude_Oil_Prices)
class A35():
    # 'Crude_Oil_Prices'!A35
    value = 32339
    isdatetime = True

@register(Crude_Oil_Prices)
class B35():
    # 'Crude_Oil_Prices'!B35
    value = 15.5
    formula = "='Input EIA Crude WTI'!B33"
    @eval_fn
    def B35():
        b33_1 = Input_EIA_Crude_WTI.B33()
        return b33_1

@register(Crude_Oil_Prices)
class C35():
    # 'Crude_Oil_Prices'!C35
    value = 14.91
    formula = "='Input EIA Crude Europe Brent'!B17"
    @eval_fn
    def C35():
        b17_1 = Input_EIA_Crude_Europe_Brent.B17()
        return b17_1

@register(Crude_Oil_Prices)
class A36():
    # 'Crude_Oil_Prices'!A36
    value = 32370
    isdatetime = True

@register(Crude_Oil_Prices)
class B36():
    # 'Crude_Oil_Prices'!B36
    value = 15.52
    formula = "='Input EIA Crude WTI'!B34"
    @eval_fn
    def B36():
        b34_1 = Input_EIA_Crude_WTI.B34()
        return b34_1

@register(Crude_Oil_Prices)
class C36():
    # 'Crude_Oil_Prices'!C36
    value = 14.89
    formula = "='Input EIA Crude Europe Brent'!B18"
    @eval_fn
    def C36():
        b18_1 = Input_EIA_Crude_Europe_Brent.B18()
        return b18_1

@register(Crude_Oil_Prices)
class A37():
    # 'Crude_Oil_Prices'!A37
    value = 32401
    isdatetime = True

@register(Crude_Oil_Prices)
class B37():
    # 'Crude_Oil_Prices'!B37
    value = 14.54
    formula = "='Input EIA Crude WTI'!B35"
    @eval_fn
    def B37():
        b35_1 = Input_EIA_Crude_WTI.B35()
        return b35_1

@register(Crude_Oil_Prices)
class C37():
    # 'Crude_Oil_Prices'!C37
    value = 13.18
    formula = "='Input EIA Crude Europe Brent'!B19"
    @eval_fn
    def C37():
        b19_1 = Input_EIA_Crude_Europe_Brent.B19()
        return b19_1

@register(Crude_Oil_Prices)
class A38():
    # 'Crude_Oil_Prices'!A38
    value = 32431
    isdatetime = True

@register(Crude_Oil_Prices)
class B38():
    # 'Crude_Oil_Prices'!B38
    value = 13.77
    formula = "='Input EIA Crude WTI'!B36"
    @eval_fn
    def B38():
        b36_1 = Input_EIA_Crude_WTI.B36()
        return b36_1

@register(Crude_Oil_Prices)
class C38():
    # 'Crude_Oil_Prices'!C38
    value = 12.41
    formula = "='Input EIA Crude Europe Brent'!B20"
    @eval_fn
    def C38():
        b20_1 = Input_EIA_Crude_Europe_Brent.B20()
        return b20_1

@register(Crude_Oil_Prices)
class A39():
    # 'Crude_Oil_Prices'!A39
    value = 32462
    isdatetime = True

@register(Crude_Oil_Prices)
class B39():
    # 'Crude_Oil_Prices'!B39
    value = 14.14
    formula = "='Input EIA Crude WTI'!B37"
    @eval_fn
    def B39():
        b37_1 = Input_EIA_Crude_WTI.B37()
        return b37_1

@register(Crude_Oil_Prices)
class C39():
    # 'Crude_Oil_Prices'!C39
    value = 13.02
    formula = "='Input EIA Crude Europe Brent'!B21"
    @eval_fn
    def C39():
        b21_1 = Input_EIA_Crude_Europe_Brent.B21()
        return b21_1

@register(Crude_Oil_Prices)
class A40():
    # 'Crude_Oil_Prices'!A40
    value = 32492
    isdatetime = True

@register(Crude_Oil_Prices)
class B40():
    # 'Crude_Oil_Prices'!B40
    value = 16.38
    formula = "='Input EIA Crude WTI'!B38"
    @eval_fn
    def B40():
        b38_1 = Input_EIA_Crude_WTI.B38()
        return b38_1

@register(Crude_Oil_Prices)
class C40():
    # 'Crude_Oil_Prices'!C40
    value = 15.31
    formula = "='Input EIA Crude Europe Brent'!B22"
    @eval_fn
    def C40():
        b22_1 = Input_EIA_Crude_Europe_Brent.B22()
        return b22_1

@register(Crude_Oil_Prices)
class A41():
    # 'Crude_Oil_Prices'!A41
    value = 32523
    isdatetime = True

@register(Crude_Oil_Prices)
class B41():
    # 'Crude_Oil_Prices'!B41
    value = 18.02
    formula = "='Input EIA Crude WTI'!B39"
    @eval_fn
    def B41():
        b39_1 = Input_EIA_Crude_WTI.B39()
        return b39_1

@register(Crude_Oil_Prices)
class C41():
    # 'Crude_Oil_Prices'!C41
    value = 17.17
    formula = "='Input EIA Crude Europe Brent'!B23"
    @eval_fn
    def C41():
        b23_1 = Input_EIA_Crude_Europe_Brent.B23()
        return b23_1

@register(Crude_Oil_Prices)
class A42():
    # 'Crude_Oil_Prices'!A42
    value = 32554
    isdatetime = True

@register(Crude_Oil_Prices)
class B42():
    # 'Crude_Oil_Prices'!B42
    value = 17.94
    formula = "='Input EIA Crude WTI'!B40"
    @eval_fn
    def B42():
        b40_1 = Input_EIA_Crude_WTI.B40()
        return b40_1

@register(Crude_Oil_Prices)
class C42():
    # 'Crude_Oil_Prices'!C42
    value = 16.89
    formula = "='Input EIA Crude Europe Brent'!B24"
    @eval_fn
    def C42():
        b24_1 = Input_EIA_Crude_Europe_Brent.B24()
        return b24_1

@register(Crude_Oil_Prices)
class A43():
    # 'Crude_Oil_Prices'!A43
    value = 32582
    isdatetime = True

@register(Crude_Oil_Prices)
class B43():
    # 'Crude_Oil_Prices'!B43
    value = 19.48
    formula = "='Input EIA Crude WTI'!B41"
    @eval_fn
    def B43():
        b41_1 = Input_EIA_Crude_WTI.B41()
        return b41_1

@register(Crude_Oil_Prices)
class C43():
    # 'Crude_Oil_Prices'!C43
    value = 18.7
    formula = "='Input EIA Crude Europe Brent'!B25"
    @eval_fn
    def C43():
        b25_1 = Input_EIA_Crude_Europe_Brent.B25()
        return b25_1

@register(Crude_Oil_Prices)
class A44():
    # 'Crude_Oil_Prices'!A44
    value = 32613
    isdatetime = True

@register(Crude_Oil_Prices)
class B44():
    # 'Crude_Oil_Prices'!B44
    value = 21.07
    formula = "='Input EIA Crude WTI'!B42"
    @eval_fn
    def B44():
        b42_1 = Input_EIA_Crude_WTI.B42()
        return b42_1

@register(Crude_Oil_Prices)
class C44():
    # 'Crude_Oil_Prices'!C44
    value = 20.32
    formula = "='Input EIA Crude Europe Brent'!B26"
    @eval_fn
    def C44():
        b26_1 = Input_EIA_Crude_Europe_Brent.B26()
        return b26_1

@register(Crude_Oil_Prices)
class A45():
    # 'Crude_Oil_Prices'!A45
    value = 32643
    isdatetime = True

@register(Crude_Oil_Prices)
class B45():
    # 'Crude_Oil_Prices'!B45
    value = 20.12
    formula = "='Input EIA Crude WTI'!B43"
    @eval_fn
    def B45():
        b43_1 = Input_EIA_Crude_WTI.B43()
        return b43_1

@register(Crude_Oil_Prices)
class C45():
    # 'Crude_Oil_Prices'!C45
    value = 18.63
    formula = "='Input EIA Crude Europe Brent'!B27"
    @eval_fn
    def C45():
        b27_1 = Input_EIA_Crude_Europe_Brent.B27()
        return b27_1

@register(Crude_Oil_Prices)
class A46():
    # 'Crude_Oil_Prices'!A46
    value = 32674
    isdatetime = True

@register(Crude_Oil_Prices)
class B46():
    # 'Crude_Oil_Prices'!B46
    value = 20.05
    formula = "='Input EIA Crude WTI'!B44"
    @eval_fn
    def B46():
        b44_1 = Input_EIA_Crude_WTI.B44()
        return b44_1

@register(Crude_Oil_Prices)
class C46():
    # 'Crude_Oil_Prices'!C46
    value = 17.67
    formula = "='Input EIA Crude Europe Brent'!B28"
    @eval_fn
    def C46():
        b28_1 = Input_EIA_Crude_Europe_Brent.B28()
        return b28_1

@register(Crude_Oil_Prices)
class A47():
    # 'Crude_Oil_Prices'!A47
    value = 32704
    isdatetime = True

@register(Crude_Oil_Prices)
class B47():
    # 'Crude_Oil_Prices'!B47
    value = 19.78
    formula = "='Input EIA Crude WTI'!B45"
    @eval_fn
    def B47():
        b45_1 = Input_EIA_Crude_WTI.B45()
        return b45_1

@register(Crude_Oil_Prices)
class C47():
    # 'Crude_Oil_Prices'!C47
    value = 17.62
    formula = "='Input EIA Crude Europe Brent'!B29"
    @eval_fn
    def C47():
        b29_1 = Input_EIA_Crude_Europe_Brent.B29()
        return b29_1

@register(Crude_Oil_Prices)
class A48():
    # 'Crude_Oil_Prices'!A48
    value = 32735
    isdatetime = True

@register(Crude_Oil_Prices)
class B48():
    # 'Crude_Oil_Prices'!B48
    value = 18.58
    formula = "='Input EIA Crude WTI'!B46"
    @eval_fn
    def B48():
        b46_1 = Input_EIA_Crude_WTI.B46()
        return b46_1

@register(Crude_Oil_Prices)
class C48():
    # 'Crude_Oil_Prices'!C48
    value = 16.77
    formula = "='Input EIA Crude Europe Brent'!B30"
    @eval_fn
    def C48():
        b30_1 = Input_EIA_Crude_Europe_Brent.B30()
        return b30_1

@register(Crude_Oil_Prices)
class A49():
    # 'Crude_Oil_Prices'!A49
    value = 32766
    isdatetime = True

@register(Crude_Oil_Prices)
class B49():
    # 'Crude_Oil_Prices'!B49
    value = 19.59
    formula = "='Input EIA Crude WTI'!B47"
    @eval_fn
    def B49():
        b47_1 = Input_EIA_Crude_WTI.B47()
        return b47_1

@register(Crude_Oil_Prices)
class C49():
    # 'Crude_Oil_Prices'!C49
    value = 17.77
    formula = "='Input EIA Crude Europe Brent'!B31"
    @eval_fn
    def C49():
        b31_1 = Input_EIA_Crude_Europe_Brent.B31()
        return b31_1

@register(Crude_Oil_Prices)
class A50():
    # 'Crude_Oil_Prices'!A50
    value = 32796
    isdatetime = True

@register(Crude_Oil_Prices)
class B50():
    # 'Crude_Oil_Prices'!B50
    value = 20.1
    formula = "='Input EIA Crude WTI'!B48"
    @eval_fn
    def B50():
        b48_1 = Input_EIA_Crude_WTI.B48()
        return b48_1

@register(Crude_Oil_Prices)
class C50():
    # 'Crude_Oil_Prices'!C50
    value = 18.91
    formula = "='Input EIA Crude Europe Brent'!B32"
    @eval_fn
    def C50():
        b32_1 = Input_EIA_Crude_Europe_Brent.B32()
        return b32_1

@register(Crude_Oil_Prices)
class A51():
    # 'Crude_Oil_Prices'!A51
    value = 32827
    isdatetime = True

@register(Crude_Oil_Prices)
class B51():
    # 'Crude_Oil_Prices'!B51
    value = 19.86
    formula = "='Input EIA Crude WTI'!B49"
    @eval_fn
    def B51():
        b49_1 = Input_EIA_Crude_WTI.B49()
        return b49_1

@register(Crude_Oil_Prices)
class C51():
    # 'Crude_Oil_Prices'!C51
    value = 18.73
    formula = "='Input EIA Crude Europe Brent'!B33"
    @eval_fn
    def C51():
        b33_1 = Input_EIA_Crude_Europe_Brent.B33()
        return b33_1

@register(Crude_Oil_Prices)
class A52():
    # 'Crude_Oil_Prices'!A52
    value = 32857
    isdatetime = True

@register(Crude_Oil_Prices)
class B52():
    # 'Crude_Oil_Prices'!B52
    value = 21.1
    formula = "='Input EIA Crude WTI'!B50"
    @eval_fn
    def B52():
        b50_1 = Input_EIA_Crude_WTI.B50()
        return b50_1

@register(Crude_Oil_Prices)
class C52():
    # 'Crude_Oil_Prices'!C52
    value = 19.84
    formula = "='Input EIA Crude Europe Brent'!B34"
    @eval_fn
    def C52():
        b34_1 = Input_EIA_Crude_Europe_Brent.B34()
        return b34_1

@register(Crude_Oil_Prices)
class A53():
    # 'Crude_Oil_Prices'!A53
    value = 32888
    isdatetime = True

@register(Crude_Oil_Prices)
class B53():
    # 'Crude_Oil_Prices'!B53
    value = 22.86
    formula = "='Input EIA Crude WTI'!B51"
    @eval_fn
    def B53():
        b51_1 = Input_EIA_Crude_WTI.B51()
        return b51_1

@register(Crude_Oil_Prices)
class C53():
    # 'Crude_Oil_Prices'!C53
    value = 21.25
    formula = "='Input EIA Crude Europe Brent'!B35"
    @eval_fn
    def C53():
        b35_1 = Input_EIA_Crude_Europe_Brent.B35()
        return b35_1

@register(Crude_Oil_Prices)
class A54():
    # 'Crude_Oil_Prices'!A54
    value = 32919
    isdatetime = True

@register(Crude_Oil_Prices)
class B54():
    # 'Crude_Oil_Prices'!B54
    value = 22.11
    formula = "='Input EIA Crude WTI'!B52"
    @eval_fn
    def B54():
        b52_1 = Input_EIA_Crude_WTI.B52()
        return b52_1

@register(Crude_Oil_Prices)
class C54():
    # 'Crude_Oil_Prices'!C54
    value = 19.81
    formula = "='Input EIA Crude Europe Brent'!B36"
    @eval_fn
    def C54():
        b36_1 = Input_EIA_Crude_Europe_Brent.B36()
        return b36_1

@register(Crude_Oil_Prices)
class A55():
    # 'Crude_Oil_Prices'!A55
    value = 32947
    isdatetime = True

@register(Crude_Oil_Prices)
class B55():
    # 'Crude_Oil_Prices'!B55
    value = 20.39
    formula = "='Input EIA Crude WTI'!B53"
    @eval_fn
    def B55():
        b53_1 = Input_EIA_Crude_WTI.B53()
        return b53_1

@register(Crude_Oil_Prices)
class C55():
    # 'Crude_Oil_Prices'!C55
    value = 18.39
    formula = "='Input EIA Crude Europe Brent'!B37"
    @eval_fn
    def C55():
        b37_1 = Input_EIA_Crude_Europe_Brent.B37()
        return b37_1

@register(Crude_Oil_Prices)
class A56():
    # 'Crude_Oil_Prices'!A56
    value = 32978
    isdatetime = True

@register(Crude_Oil_Prices)
class B56():
    # 'Crude_Oil_Prices'!B56
    value = 18.43
    formula = "='Input EIA Crude WTI'!B54"
    @eval_fn
    def B56():
        b54_1 = Input_EIA_Crude_WTI.B54()
        return b54_1

@register(Crude_Oil_Prices)
class C56():
    # 'Crude_Oil_Prices'!C56
    value = 16.61
    formula = "='Input EIA Crude Europe Brent'!B38"
    @eval_fn
    def C56():
        b38_1 = Input_EIA_Crude_Europe_Brent.B38()
        return b38_1

@register(Crude_Oil_Prices)
class A57():
    # 'Crude_Oil_Prices'!A57
    value = 33008
    isdatetime = True

@register(Crude_Oil_Prices)
class B57():
    # 'Crude_Oil_Prices'!B57
    value = 18.2
    formula = "='Input EIA Crude WTI'!B55"
    @eval_fn
    def B57():
        b55_1 = Input_EIA_Crude_WTI.B55()
        return b55_1

@register(Crude_Oil_Prices)
class C57():
    # 'Crude_Oil_Prices'!C57
    value = 16.35
    formula = "='Input EIA Crude Europe Brent'!B39"
    @eval_fn
    def C57():
        b39_1 = Input_EIA_Crude_Europe_Brent.B39()
        return b39_1

@register(Crude_Oil_Prices)
class A58():
    # 'Crude_Oil_Prices'!A58
    value = 33039
    isdatetime = True

@register(Crude_Oil_Prices)
class B58():
    # 'Crude_Oil_Prices'!B58
    value = 16.7
    formula = "='Input EIA Crude WTI'!B56"
    @eval_fn
    def B58():
        b56_1 = Input_EIA_Crude_WTI.B56()
        return b56_1

@register(Crude_Oil_Prices)
class C58():
    # 'Crude_Oil_Prices'!C58
    value = 15.1
    formula = "='Input EIA Crude Europe Brent'!B40"
    @eval_fn
    def C58():
        b40_1 = Input_EIA_Crude_Europe_Brent.B40()
        return b40_1

@register(Crude_Oil_Prices)
class A59():
    # 'Crude_Oil_Prices'!A59
    value = 33069
    isdatetime = True

@register(Crude_Oil_Prices)
class B59():
    # 'Crude_Oil_Prices'!B59
    value = 18.45
    formula = "='Input EIA Crude WTI'!B57"
    @eval_fn
    def B59():
        b57_1 = Input_EIA_Crude_WTI.B57()
        return b57_1

@register(Crude_Oil_Prices)
class C59():
    # 'Crude_Oil_Prices'!C59
    value = 17.17
    formula = "='Input EIA Crude Europe Brent'!B41"
    @eval_fn
    def C59():
        b41_1 = Input_EIA_Crude_Europe_Brent.B41()
        return b41_1

@register(Crude_Oil_Prices)
class A60():
    # 'Crude_Oil_Prices'!A60
    value = 33100
    isdatetime = True

@register(Crude_Oil_Prices)
class B60():
    # 'Crude_Oil_Prices'!B60
    value = 27.31
    formula = "='Input EIA Crude WTI'!B58"
    @eval_fn
    def B60():
        b58_1 = Input_EIA_Crude_WTI.B58()
        return b58_1

@register(Crude_Oil_Prices)
class C60():
    # 'Crude_Oil_Prices'!C60
    value = 27.17
    formula = "='Input EIA Crude Europe Brent'!B42"
    @eval_fn
    def C60():
        b42_1 = Input_EIA_Crude_Europe_Brent.B42()
        return b42_1

@register(Crude_Oil_Prices)
class A61():
    # 'Crude_Oil_Prices'!A61
    value = 33131
    isdatetime = True

@register(Crude_Oil_Prices)
class B61():
    # 'Crude_Oil_Prices'!B61
    value = 33.51
    formula = "='Input EIA Crude WTI'!B59"
    @eval_fn
    def B61():
        b59_1 = Input_EIA_Crude_WTI.B59()
        return b59_1

@register(Crude_Oil_Prices)
class C61():
    # 'Crude_Oil_Prices'!C61
    value = 34.9
    formula = "='Input EIA Crude Europe Brent'!B43"
    @eval_fn
    def C61():
        b43_1 = Input_EIA_Crude_Europe_Brent.B43()
        return b43_1

@register(Crude_Oil_Prices)
class A62():
    # 'Crude_Oil_Prices'!A62
    value = 33161
    isdatetime = True

@register(Crude_Oil_Prices)
class B62():
    # 'Crude_Oil_Prices'!B62
    value = 36.04
    formula = "='Input EIA Crude WTI'!B60"
    @eval_fn
    def B62():
        b60_1 = Input_EIA_Crude_WTI.B60()
        return b60_1

@register(Crude_Oil_Prices)
class C62():
    # 'Crude_Oil_Prices'!C62
    value = 36.02
    formula = "='Input EIA Crude Europe Brent'!B44"
    @eval_fn
    def C62():
        b44_1 = Input_EIA_Crude_Europe_Brent.B44()
        return b44_1

@register(Crude_Oil_Prices)
class A63():
    # 'Crude_Oil_Prices'!A63
    value = 33192
    isdatetime = True

@register(Crude_Oil_Prices)
class B63():
    # 'Crude_Oil_Prices'!B63
    value = 32.33
    formula = "='Input EIA Crude WTI'!B61"
    @eval_fn
    def B63():
        b61_1 = Input_EIA_Crude_WTI.B61()
        return b61_1

@register(Crude_Oil_Prices)
class C63():
    # 'Crude_Oil_Prices'!C63
    value = 33.07
    formula = "='Input EIA Crude Europe Brent'!B45"
    @eval_fn
    def C63():
        b45_1 = Input_EIA_Crude_Europe_Brent.B45()
        return b45_1

@register(Crude_Oil_Prices)
class A64():
    # 'Crude_Oil_Prices'!A64
    value = 33222
    isdatetime = True

@register(Crude_Oil_Prices)
class B64():
    # 'Crude_Oil_Prices'!B64
    value = 27.28
    formula = "='Input EIA Crude WTI'!B62"
    @eval_fn
    def B64():
        b62_1 = Input_EIA_Crude_WTI.B62()
        return b62_1

@register(Crude_Oil_Prices)
class C64():
    # 'Crude_Oil_Prices'!C64
    value = 28.27
    formula = "='Input EIA Crude Europe Brent'!B46"
    @eval_fn
    def C64():
        b46_1 = Input_EIA_Crude_Europe_Brent.B46()
        return b46_1

@register(Crude_Oil_Prices)
class A65():
    # 'Crude_Oil_Prices'!A65
    value = 33253
    isdatetime = True

@register(Crude_Oil_Prices)
class B65():
    # 'Crude_Oil_Prices'!B65
    value = 25.23
    formula = "='Input EIA Crude WTI'!B63"
    @eval_fn
    def B65():
        b63_1 = Input_EIA_Crude_WTI.B63()
        return b63_1

@register(Crude_Oil_Prices)
class C65():
    # 'Crude_Oil_Prices'!C65
    value = 23.57
    formula = "='Input EIA Crude Europe Brent'!B47"
    @eval_fn
    def C65():
        b47_1 = Input_EIA_Crude_Europe_Brent.B47()
        return b47_1

@register(Crude_Oil_Prices)
class A66():
    # 'Crude_Oil_Prices'!A66
    value = 33284
    isdatetime = True

@register(Crude_Oil_Prices)
class B66():
    # 'Crude_Oil_Prices'!B66
    value = 20.48
    formula = "='Input EIA Crude WTI'!B64"
    @eval_fn
    def B66():
        b64_1 = Input_EIA_Crude_WTI.B64()
        return b64_1

@register(Crude_Oil_Prices)
class C66():
    # 'Crude_Oil_Prices'!C66
    value = 19.54
    formula = "='Input EIA Crude Europe Brent'!B48"
    @eval_fn
    def C66():
        b48_1 = Input_EIA_Crude_Europe_Brent.B48()
        return b48_1

@register(Crude_Oil_Prices)
class A67():
    # 'Crude_Oil_Prices'!A67
    value = 33312
    isdatetime = True

@register(Crude_Oil_Prices)
class B67():
    # 'Crude_Oil_Prices'!B67
    value = 19.9
    formula = "='Input EIA Crude WTI'!B65"
    @eval_fn
    def B67():
        b65_1 = Input_EIA_Crude_WTI.B65()
        return b65_1

@register(Crude_Oil_Prices)
class C67():
    # 'Crude_Oil_Prices'!C67
    value = 19.08
    formula = "='Input EIA Crude Europe Brent'!B49"
    @eval_fn
    def C67():
        b49_1 = Input_EIA_Crude_Europe_Brent.B49()
        return b49_1

@register(Crude_Oil_Prices)
class A68():
    # 'Crude_Oil_Prices'!A68
    value = 33343
    isdatetime = True

@register(Crude_Oil_Prices)
class B68():
    # 'Crude_Oil_Prices'!B68
    value = 20.83
    formula = "='Input EIA Crude WTI'!B66"
    @eval_fn
    def B68():
        b66_1 = Input_EIA_Crude_WTI.B66()
        return b66_1

@register(Crude_Oil_Prices)
class C68():
    # 'Crude_Oil_Prices'!C68
    value = 19.18
    formula = "='Input EIA Crude Europe Brent'!B50"
    @eval_fn
    def C68():
        b50_1 = Input_EIA_Crude_Europe_Brent.B50()
        return b50_1

@register(Crude_Oil_Prices)
class A69():
    # 'Crude_Oil_Prices'!A69
    value = 33373
    isdatetime = True

@register(Crude_Oil_Prices)
class B69():
    # 'Crude_Oil_Prices'!B69
    value = 21.23
    formula = "='Input EIA Crude WTI'!B67"
    @eval_fn
    def B69():
        b67_1 = Input_EIA_Crude_WTI.B67()
        return b67_1

@register(Crude_Oil_Prices)
class C69():
    # 'Crude_Oil_Prices'!C69
    value = 19.19
    formula = "='Input EIA Crude Europe Brent'!B51"
    @eval_fn
    def C69():
        b51_1 = Input_EIA_Crude_Europe_Brent.B51()
        return b51_1

@register(Crude_Oil_Prices)
class A70():
    # 'Crude_Oil_Prices'!A70
    value = 33404
    isdatetime = True

@register(Crude_Oil_Prices)
class B70():
    # 'Crude_Oil_Prices'!B70
    value = 20.19
    formula = "='Input EIA Crude WTI'!B68"
    @eval_fn
    def B70():
        b68_1 = Input_EIA_Crude_WTI.B68()
        return b68_1

@register(Crude_Oil_Prices)
class C70():
    # 'Crude_Oil_Prices'!C70
    value = 18.17
    formula = "='Input EIA Crude Europe Brent'!B52"
    @eval_fn
    def C70():
        b52_1 = Input_EIA_Crude_Europe_Brent.B52()
        return b52_1

@register(Crude_Oil_Prices)
class A71():
    # 'Crude_Oil_Prices'!A71
    value = 33434
    isdatetime = True

@register(Crude_Oil_Prices)
class B71():
    # 'Crude_Oil_Prices'!B71
    value = 21.4
    formula = "='Input EIA Crude WTI'!B69"
    @eval_fn
    def B71():
        b69_1 = Input_EIA_Crude_WTI.B69()
        return b69_1

@register(Crude_Oil_Prices)
class C71():
    # 'Crude_Oil_Prices'!C71
    value = 19.4
    formula = "='Input EIA Crude Europe Brent'!B53"
    @eval_fn
    def C71():
        b53_1 = Input_EIA_Crude_Europe_Brent.B53()
        return b53_1

@register(Crude_Oil_Prices)
class A72():
    # 'Crude_Oil_Prices'!A72
    value = 33465
    isdatetime = True

@register(Crude_Oil_Prices)
class B72():
    # 'Crude_Oil_Prices'!B72
    value = 21.69
    formula = "='Input EIA Crude WTI'!B70"
    @eval_fn
    def B72():
        b70_1 = Input_EIA_Crude_WTI.B70()
        return b70_1

@register(Crude_Oil_Prices)
class C72():
    # 'Crude_Oil_Prices'!C72
    value = 19.77
    formula = "='Input EIA Crude Europe Brent'!B54"
    @eval_fn
    def C72():
        b54_1 = Input_EIA_Crude_Europe_Brent.B54()
        return b54_1

@register(Crude_Oil_Prices)
class A73():
    # 'Crude_Oil_Prices'!A73
    value = 33496
    isdatetime = True

@register(Crude_Oil_Prices)
class B73():
    # 'Crude_Oil_Prices'!B73
    value = 21.89
    formula = "='Input EIA Crude WTI'!B71"
    @eval_fn
    def B73():
        b71_1 = Input_EIA_Crude_WTI.B71()
        return b71_1

@register(Crude_Oil_Prices)
class C73():
    # 'Crude_Oil_Prices'!C73
    value = 20.5
    formula = "='Input EIA Crude Europe Brent'!B55"
    @eval_fn
    def C73():
        b55_1 = Input_EIA_Crude_Europe_Brent.B55()
        return b55_1

@register(Crude_Oil_Prices)
class A74():
    # 'Crude_Oil_Prices'!A74
    value = 33526
    isdatetime = True

@register(Crude_Oil_Prices)
class B74():
    # 'Crude_Oil_Prices'!B74
    value = 23.23
    formula = "='Input EIA Crude WTI'!B72"
    @eval_fn
    def B74():
        b72_1 = Input_EIA_Crude_WTI.B72()
        return b72_1

@register(Crude_Oil_Prices)
class C74():
    # 'Crude_Oil_Prices'!C74
    value = 22.21
    formula = "='Input EIA Crude Europe Brent'!B56"
    @eval_fn
    def C74():
        b56_1 = Input_EIA_Crude_Europe_Brent.B56()
        return b56_1

@register(Crude_Oil_Prices)
class A75():
    # 'Crude_Oil_Prices'!A75
    value = 33557
    isdatetime = True

@register(Crude_Oil_Prices)
class B75():
    # 'Crude_Oil_Prices'!B75
    value = 22.46
    formula = "='Input EIA Crude WTI'!B73"
    @eval_fn
    def B75():
        b73_1 = Input_EIA_Crude_WTI.B73()
        return b73_1

@register(Crude_Oil_Prices)
class C75():
    # 'Crude_Oil_Prices'!C75
    value = 21.11
    formula = "='Input EIA Crude Europe Brent'!B57"
    @eval_fn
    def C75():
        b57_1 = Input_EIA_Crude_Europe_Brent.B57()
        return b57_1

@register(Crude_Oil_Prices)
class A76():
    # 'Crude_Oil_Prices'!A76
    value = 33587
    isdatetime = True

@register(Crude_Oil_Prices)
class B76():
    # 'Crude_Oil_Prices'!B76
    value = 19.5
    formula = "='Input EIA Crude WTI'!B74"
    @eval_fn
    def B76():
        b74_1 = Input_EIA_Crude_WTI.B74()
        return b74_1

@register(Crude_Oil_Prices)
class C76():
    # 'Crude_Oil_Prices'!C76
    value = 18.41
    formula = "='Input EIA Crude Europe Brent'!B58"
    @eval_fn
    def C76():
        b58_1 = Input_EIA_Crude_Europe_Brent.B58()
        return b58_1

@register(Crude_Oil_Prices)
class A77():
    # 'Crude_Oil_Prices'!A77
    value = 33618
    isdatetime = True

@register(Crude_Oil_Prices)
class B77():
    # 'Crude_Oil_Prices'!B77
    value = 18.79
    formula = "='Input EIA Crude WTI'!B75"
    @eval_fn
    def B77():
        b75_1 = Input_EIA_Crude_WTI.B75()
        return b75_1

@register(Crude_Oil_Prices)
class C77():
    # 'Crude_Oil_Prices'!C77
    value = 18.16
    formula = "='Input EIA Crude Europe Brent'!B59"
    @eval_fn
    def C77():
        b59_1 = Input_EIA_Crude_Europe_Brent.B59()
        return b59_1

@register(Crude_Oil_Prices)
class A78():
    # 'Crude_Oil_Prices'!A78
    value = 33649
    isdatetime = True

@register(Crude_Oil_Prices)
class B78():
    # 'Crude_Oil_Prices'!B78
    value = 19.01
    formula = "='Input EIA Crude WTI'!B76"
    @eval_fn
    def B78():
        b76_1 = Input_EIA_Crude_WTI.B76()
        return b76_1

@register(Crude_Oil_Prices)
class C78():
    # 'Crude_Oil_Prices'!C78
    value = 18.05
    formula = "='Input EIA Crude Europe Brent'!B60"
    @eval_fn
    def C78():
        b60_1 = Input_EIA_Crude_Europe_Brent.B60()
        return b60_1

@register(Crude_Oil_Prices)
class A79():
    # 'Crude_Oil_Prices'!A79
    value = 33678
    isdatetime = True

@register(Crude_Oil_Prices)
class B79():
    # 'Crude_Oil_Prices'!B79
    value = 18.92
    formula = "='Input EIA Crude WTI'!B77"
    @eval_fn
    def B79():
        b77_1 = Input_EIA_Crude_WTI.B77()
        return b77_1

@register(Crude_Oil_Prices)
class C79():
    # 'Crude_Oil_Prices'!C79
    value = 17.63
    formula = "='Input EIA Crude Europe Brent'!B61"
    @eval_fn
    def C79():
        b61_1 = Input_EIA_Crude_Europe_Brent.B61()
        return b61_1

@register(Crude_Oil_Prices)
class A80():
    # 'Crude_Oil_Prices'!A80
    value = 33709
    isdatetime = True

@register(Crude_Oil_Prices)
class B80():
    # 'Crude_Oil_Prices'!B80
    value = 20.23
    formula = "='Input EIA Crude WTI'!B78"
    @eval_fn
    def B80():
        b78_1 = Input_EIA_Crude_WTI.B78()
        return b78_1

@register(Crude_Oil_Prices)
class C80():
    # 'Crude_Oil_Prices'!C80
    value = 18.92
    formula = "='Input EIA Crude Europe Brent'!B62"
    @eval_fn
    def C80():
        b62_1 = Input_EIA_Crude_Europe_Brent.B62()
        return b62_1

@register(Crude_Oil_Prices)
class A81():
    # 'Crude_Oil_Prices'!A81
    value = 33739
    isdatetime = True

@register(Crude_Oil_Prices)
class B81():
    # 'Crude_Oil_Prices'!B81
    value = 20.98
    formula = "='Input EIA Crude WTI'!B79"
    @eval_fn
    def B81():
        b79_1 = Input_EIA_Crude_WTI.B79()
        return b79_1

@register(Crude_Oil_Prices)
class C81():
    # 'Crude_Oil_Prices'!C81
    value = 19.89
    formula = "='Input EIA Crude Europe Brent'!B63"
    @eval_fn
    def C81():
        b63_1 = Input_EIA_Crude_Europe_Brent.B63()
        return b63_1

@register(Crude_Oil_Prices)
class A82():
    # 'Crude_Oil_Prices'!A82
    value = 33770
    isdatetime = True

@register(Crude_Oil_Prices)
class B82():
    # 'Crude_Oil_Prices'!B82
    value = 22.39
    formula = "='Input EIA Crude WTI'!B80"
    @eval_fn
    def B82():
        b80_1 = Input_EIA_Crude_WTI.B80()
        return b80_1

@register(Crude_Oil_Prices)
class C82():
    # 'Crude_Oil_Prices'!C82
    value = 21.16
    formula = "='Input EIA Crude Europe Brent'!B64"
    @eval_fn
    def C82():
        b64_1 = Input_EIA_Crude_Europe_Brent.B64()
        return b64_1

@register(Crude_Oil_Prices)
class A83():
    # 'Crude_Oil_Prices'!A83
    value = 33800
    isdatetime = True

@register(Crude_Oil_Prices)
class B83():
    # 'Crude_Oil_Prices'!B83
    value = 21.78
    formula = "='Input EIA Crude WTI'!B81"
    @eval_fn
    def B83():
        b81_1 = Input_EIA_Crude_WTI.B81()
        return b81_1

@register(Crude_Oil_Prices)
class C83():
    # 'Crude_Oil_Prices'!C83
    value = 20.24
    formula = "='Input EIA Crude Europe Brent'!B65"
    @eval_fn
    def C83():
        b65_1 = Input_EIA_Crude_Europe_Brent.B65()
        return b65_1

@register(Crude_Oil_Prices)
class A84():
    # 'Crude_Oil_Prices'!A84
    value = 33831
    isdatetime = True

@register(Crude_Oil_Prices)
class B84():
    # 'Crude_Oil_Prices'!B84
    value = 21.34
    formula = "='Input EIA Crude WTI'!B82"
    @eval_fn
    def B84():
        b82_1 = Input_EIA_Crude_WTI.B82()
        return b82_1

@register(Crude_Oil_Prices)
class C84():
    # 'Crude_Oil_Prices'!C84
    value = 19.74
    formula = "='Input EIA Crude Europe Brent'!B66"
    @eval_fn
    def C84():
        b66_1 = Input_EIA_Crude_Europe_Brent.B66()
        return b66_1

@register(Crude_Oil_Prices)
class A85():
    # 'Crude_Oil_Prices'!A85
    value = 33862
    isdatetime = True

@register(Crude_Oil_Prices)
class B85():
    # 'Crude_Oil_Prices'!B85
    value = 21.88
    formula = "='Input EIA Crude WTI'!B83"
    @eval_fn
    def B85():
        b83_1 = Input_EIA_Crude_WTI.B83()
        return b83_1

@register(Crude_Oil_Prices)
class C85():
    # 'Crude_Oil_Prices'!C85
    value = 20.27
    formula = "='Input EIA Crude Europe Brent'!B67"
    @eval_fn
    def C85():
        b67_1 = Input_EIA_Crude_Europe_Brent.B67()
        return b67_1

@register(Crude_Oil_Prices)
class A86():
    # 'Crude_Oil_Prices'!A86
    value = 33892
    isdatetime = True

@register(Crude_Oil_Prices)
class B86():
    # 'Crude_Oil_Prices'!B86
    value = 21.69
    formula = "='Input EIA Crude WTI'!B84"
    @eval_fn
    def B86():
        b84_1 = Input_EIA_Crude_WTI.B84()
        return b84_1

@register(Crude_Oil_Prices)
class C86():
    # 'Crude_Oil_Prices'!C86
    value = 20.26
    formula = "='Input EIA Crude Europe Brent'!B68"
    @eval_fn
    def C86():
        b68_1 = Input_EIA_Crude_Europe_Brent.B68()
        return b68_1

@register(Crude_Oil_Prices)
class A87():
    # 'Crude_Oil_Prices'!A87
    value = 33923
    isdatetime = True

@register(Crude_Oil_Prices)
class B87():
    # 'Crude_Oil_Prices'!B87
    value = 20.34
    formula = "='Input EIA Crude WTI'!B85"
    @eval_fn
    def B87():
        b85_1 = Input_EIA_Crude_WTI.B85()
        return b85_1

@register(Crude_Oil_Prices)
class C87():
    # 'Crude_Oil_Prices'!C87
    value = 19.21
    formula = "='Input EIA Crude Europe Brent'!B69"
    @eval_fn
    def C87():
        b69_1 = Input_EIA_Crude_Europe_Brent.B69()
        return b69_1

@register(Crude_Oil_Prices)
class A88():
    # 'Crude_Oil_Prices'!A88
    value = 33953
    isdatetime = True

@register(Crude_Oil_Prices)
class B88():
    # 'Crude_Oil_Prices'!B88
    value = 19.41
    formula = "='Input EIA Crude WTI'!B86"
    @eval_fn
    def B88():
        b86_1 = Input_EIA_Crude_WTI.B86()
        return b86_1

@register(Crude_Oil_Prices)
class C88():
    # 'Crude_Oil_Prices'!C88
    value = 18.14
    formula = "='Input EIA Crude Europe Brent'!B70"
    @eval_fn
    def C88():
        b70_1 = Input_EIA_Crude_Europe_Brent.B70()
        return b70_1

@register(Crude_Oil_Prices)
class A89():
    # 'Crude_Oil_Prices'!A89
    value = 33984
    isdatetime = True

@register(Crude_Oil_Prices)
class B89():
    # 'Crude_Oil_Prices'!B89
    value = 19.03
    formula = "='Input EIA Crude WTI'!B87"
    @eval_fn
    def B89():
        b87_1 = Input_EIA_Crude_WTI.B87()
        return b87_1

@register(Crude_Oil_Prices)
class C89():
    # 'Crude_Oil_Prices'!C89
    value = 17.39
    formula = "='Input EIA Crude Europe Brent'!B71"
    @eval_fn
    def C89():
        b71_1 = Input_EIA_Crude_Europe_Brent.B71()
        return b71_1

@register(Crude_Oil_Prices)
class A90():
    # 'Crude_Oil_Prices'!A90
    value = 34015
    isdatetime = True

@register(Crude_Oil_Prices)
class B90():
    # 'Crude_Oil_Prices'!B90
    value = 20.09
    formula = "='Input EIA Crude WTI'!B88"
    @eval_fn
    def B90():
        b88_1 = Input_EIA_Crude_WTI.B88()
        return b88_1

@register(Crude_Oil_Prices)
class C90():
    # 'Crude_Oil_Prices'!C90
    value = 18.47
    formula = "='Input EIA Crude Europe Brent'!B72"
    @eval_fn
    def C90():
        b72_1 = Input_EIA_Crude_Europe_Brent.B72()
        return b72_1

@register(Crude_Oil_Prices)
class A91():
    # 'Crude_Oil_Prices'!A91
    value = 34043
    isdatetime = True

@register(Crude_Oil_Prices)
class B91():
    # 'Crude_Oil_Prices'!B91
    value = 20.32
    formula = "='Input EIA Crude WTI'!B89"
    @eval_fn
    def B91():
        b89_1 = Input_EIA_Crude_WTI.B89()
        return b89_1

@register(Crude_Oil_Prices)
class C91():
    # 'Crude_Oil_Prices'!C91
    value = 18.79
    formula = "='Input EIA Crude Europe Brent'!B73"
    @eval_fn
    def C91():
        b73_1 = Input_EIA_Crude_Europe_Brent.B73()
        return b73_1

@register(Crude_Oil_Prices)
class A92():
    # 'Crude_Oil_Prices'!A92
    value = 34074
    isdatetime = True

@register(Crude_Oil_Prices)
class B92():
    # 'Crude_Oil_Prices'!B92
    value = 20.25
    formula = "='Input EIA Crude WTI'!B90"
    @eval_fn
    def B92():
        b90_1 = Input_EIA_Crude_WTI.B90()
        return b90_1

@register(Crude_Oil_Prices)
class C92():
    # 'Crude_Oil_Prices'!C92
    value = 18.67
    formula = "='Input EIA Crude Europe Brent'!B74"
    @eval_fn
    def C92():
        b74_1 = Input_EIA_Crude_Europe_Brent.B74()
        return b74_1

@register(Crude_Oil_Prices)
class A93():
    # 'Crude_Oil_Prices'!A93
    value = 34104
    isdatetime = True

@register(Crude_Oil_Prices)
class B93():
    # 'Crude_Oil_Prices'!B93
    value = 19.95
    formula = "='Input EIA Crude WTI'!B91"
    @eval_fn
    def B93():
        b91_1 = Input_EIA_Crude_WTI.B91()
        return b91_1

@register(Crude_Oil_Prices)
class C93():
    # 'Crude_Oil_Prices'!C93
    value = 18.51
    formula = "='Input EIA Crude Europe Brent'!B75"
    @eval_fn
    def C93():
        b75_1 = Input_EIA_Crude_Europe_Brent.B75()
        return b75_1

@register(Crude_Oil_Prices)
class A94():
    # 'Crude_Oil_Prices'!A94
    value = 34135
    isdatetime = True

@register(Crude_Oil_Prices)
class B94():
    # 'Crude_Oil_Prices'!B94
    value = 19.09
    formula = "='Input EIA Crude WTI'!B92"
    @eval_fn
    def B94():
        b92_1 = Input_EIA_Crude_WTI.B92()
        return b92_1

@register(Crude_Oil_Prices)
class C94():
    # 'Crude_Oil_Prices'!C94
    value = 17.65
    formula = "='Input EIA Crude Europe Brent'!B76"
    @eval_fn
    def C94():
        b76_1 = Input_EIA_Crude_Europe_Brent.B76()
        return b76_1

@register(Crude_Oil_Prices)
class A95():
    # 'Crude_Oil_Prices'!A95
    value = 34165
    isdatetime = True

@register(Crude_Oil_Prices)
class B95():
    # 'Crude_Oil_Prices'!B95
    value = 17.89
    formula = "='Input EIA Crude WTI'!B93"
    @eval_fn
    def B95():
        b93_1 = Input_EIA_Crude_WTI.B93()
        return b93_1

@register(Crude_Oil_Prices)
class C95():
    # 'Crude_Oil_Prices'!C95
    value = 16.78
    formula = "='Input EIA Crude Europe Brent'!B77"
    @eval_fn
    def C95():
        b77_1 = Input_EIA_Crude_Europe_Brent.B77()
        return b77_1

@register(Crude_Oil_Prices)
class A96():
    # 'Crude_Oil_Prices'!A96
    value = 34196
    isdatetime = True

@register(Crude_Oil_Prices)
class B96():
    # 'Crude_Oil_Prices'!B96
    value = 18.01
    formula = "='Input EIA Crude WTI'!B94"
    @eval_fn
    def B96():
        b94_1 = Input_EIA_Crude_WTI.B94()
        return b94_1

@register(Crude_Oil_Prices)
class C96():
    # 'Crude_Oil_Prices'!C96
    value = 16.7
    formula = "='Input EIA Crude Europe Brent'!B78"
    @eval_fn
    def C96():
        b78_1 = Input_EIA_Crude_Europe_Brent.B78()
        return b78_1

@register(Crude_Oil_Prices)
class A97():
    # 'Crude_Oil_Prices'!A97
    value = 34227
    isdatetime = True

@register(Crude_Oil_Prices)
class B97():
    # 'Crude_Oil_Prices'!B97
    value = 17.5
    formula = "='Input EIA Crude WTI'!B95"
    @eval_fn
    def B97():
        b95_1 = Input_EIA_Crude_WTI.B95()
        return b95_1

@register(Crude_Oil_Prices)
class C97():
    # 'Crude_Oil_Prices'!C97
    value = 16.01
    formula = "='Input EIA Crude Europe Brent'!B79"
    @eval_fn
    def C97():
        b79_1 = Input_EIA_Crude_Europe_Brent.B79()
        return b79_1

@register(Crude_Oil_Prices)
class A98():
    # 'Crude_Oil_Prices'!A98
    value = 34257
    isdatetime = True

@register(Crude_Oil_Prices)
class B98():
    # 'Crude_Oil_Prices'!B98
    value = 18.15
    formula = "='Input EIA Crude WTI'!B96"
    @eval_fn
    def B98():
        b96_1 = Input_EIA_Crude_WTI.B96()
        return b96_1

@register(Crude_Oil_Prices)
class C98():
    # 'Crude_Oil_Prices'!C98
    value = 16.61
    formula = "='Input EIA Crude Europe Brent'!B80"
    @eval_fn
    def C98():
        b80_1 = Input_EIA_Crude_Europe_Brent.B80()
        return b80_1

@register(Crude_Oil_Prices)
class A99():
    # 'Crude_Oil_Prices'!A99
    value = 34288
    isdatetime = True

@register(Crude_Oil_Prices)
class B99():
    # 'Crude_Oil_Prices'!B99
    value = 16.61
    formula = "='Input EIA Crude WTI'!B97"
    @eval_fn
    def B99():
        b97_1 = Input_EIA_Crude_WTI.B97()
        return b97_1

@register(Crude_Oil_Prices)
class C99():
    # 'Crude_Oil_Prices'!C99
    value = 15.2
    formula = "='Input EIA Crude Europe Brent'!B81"
    @eval_fn
    def C99():
        b81_1 = Input_EIA_Crude_Europe_Brent.B81()
        return b81_1

@register(Crude_Oil_Prices)
class A100():
    # 'Crude_Oil_Prices'!A100
    value = 34318
    isdatetime = True

@register(Crude_Oil_Prices)
class B100():
    # 'Crude_Oil_Prices'!B100
    value = 14.52
    formula = "='Input EIA Crude WTI'!B98"
    @eval_fn
    def B100():
        b98_1 = Input_EIA_Crude_WTI.B98()
        return b98_1

@register(Crude_Oil_Prices)
class C100():
    # 'Crude_Oil_Prices'!C100
    value = 13.73
    formula = "='Input EIA Crude Europe Brent'!B82"
    @eval_fn
    def C100():
        b82_1 = Input_EIA_Crude_Europe_Brent.B82()
        return b82_1

@register(Crude_Oil_Prices)
class A101():
    # 'Crude_Oil_Prices'!A101
    value = 34349
    isdatetime = True

@register(Crude_Oil_Prices)
class B101():
    # 'Crude_Oil_Prices'!B101
    value = 15.03
    formula = "='Input EIA Crude WTI'!B99"
    @eval_fn
    def B101():
        b99_1 = Input_EIA_Crude_WTI.B99()
        return b99_1

@register(Crude_Oil_Prices)
class C101():
    # 'Crude_Oil_Prices'!C101
    value = 14.29
    formula = "='Input EIA Crude Europe Brent'!B83"
    @eval_fn
    def C101():
        b83_1 = Input_EIA_Crude_Europe_Brent.B83()
        return b83_1

@register(Crude_Oil_Prices)
class A102():
    # 'Crude_Oil_Prices'!A102
    value = 34380
    isdatetime = True

@register(Crude_Oil_Prices)
class B102():
    # 'Crude_Oil_Prices'!B102
    value = 14.78
    formula = "='Input EIA Crude WTI'!B100"
    @eval_fn
    def B102():
        b100_1 = Input_EIA_Crude_WTI.B100()
        return b100_1

@register(Crude_Oil_Prices)
class C102():
    # 'Crude_Oil_Prices'!C102
    value = 13.8
    formula = "='Input EIA Crude Europe Brent'!B84"
    @eval_fn
    def C102():
        b84_1 = Input_EIA_Crude_Europe_Brent.B84()
        return b84_1

@register(Crude_Oil_Prices)
class A103():
    # 'Crude_Oil_Prices'!A103
    value = 34408
    isdatetime = True

@register(Crude_Oil_Prices)
class B103():
    # 'Crude_Oil_Prices'!B103
    value = 14.68
    formula = "='Input EIA Crude WTI'!B101"
    @eval_fn
    def B103():
        b101_1 = Input_EIA_Crude_WTI.B101()
        return b101_1

@register(Crude_Oil_Prices)
class C103():
    # 'Crude_Oil_Prices'!C103
    value = 13.82
    formula = "='Input EIA Crude Europe Brent'!B85"
    @eval_fn
    def C103():
        b85_1 = Input_EIA_Crude_Europe_Brent.B85()
        return b85_1

@register(Crude_Oil_Prices)
class A104():
    # 'Crude_Oil_Prices'!A104
    value = 34439
    isdatetime = True

@register(Crude_Oil_Prices)
class B104():
    # 'Crude_Oil_Prices'!B104
    value = 16.42
    formula = "='Input EIA Crude WTI'!B102"
    @eval_fn
    def B104():
        b102_1 = Input_EIA_Crude_WTI.B102()
        return b102_1

@register(Crude_Oil_Prices)
class C104():
    # 'Crude_Oil_Prices'!C104
    value = 15.23
    formula = "='Input EIA Crude Europe Brent'!B86"
    @eval_fn
    def C104():
        b86_1 = Input_EIA_Crude_Europe_Brent.B86()
        return b86_1

@register(Crude_Oil_Prices)
class A105():
    # 'Crude_Oil_Prices'!A105
    value = 34469
    isdatetime = True

@register(Crude_Oil_Prices)
class B105():
    # 'Crude_Oil_Prices'!B105
    value = 17.89
    formula = "='Input EIA Crude WTI'!B103"
    @eval_fn
    def B105():
        b103_1 = Input_EIA_Crude_WTI.B103()
        return b103_1

@register(Crude_Oil_Prices)
class C105():
    # 'Crude_Oil_Prices'!C105
    value = 16.19
    formula = "='Input EIA Crude Europe Brent'!B87"
    @eval_fn
    def C105():
        b87_1 = Input_EIA_Crude_Europe_Brent.B87()
        return b87_1

@register(Crude_Oil_Prices)
class A106():
    # 'Crude_Oil_Prices'!A106
    value = 34500
    isdatetime = True

@register(Crude_Oil_Prices)
class B106():
    # 'Crude_Oil_Prices'!B106
    value = 19.06
    formula = "='Input EIA Crude WTI'!B104"
    @eval_fn
    def B106():
        b104_1 = Input_EIA_Crude_WTI.B104()
        return b104_1

@register(Crude_Oil_Prices)
class C106():
    # 'Crude_Oil_Prices'!C106
    value = 16.76
    formula = "='Input EIA Crude Europe Brent'!B88"
    @eval_fn
    def C106():
        b88_1 = Input_EIA_Crude_Europe_Brent.B88()
        return b88_1

@register(Crude_Oil_Prices)
class A107():
    # 'Crude_Oil_Prices'!A107
    value = 34530
    isdatetime = True

@register(Crude_Oil_Prices)
class B107():
    # 'Crude_Oil_Prices'!B107
    value = 19.66
    formula = "='Input EIA Crude WTI'!B105"
    @eval_fn
    def B107():
        b105_1 = Input_EIA_Crude_WTI.B105()
        return b105_1

@register(Crude_Oil_Prices)
class C107():
    # 'Crude_Oil_Prices'!C107
    value = 17.6
    formula = "='Input EIA Crude Europe Brent'!B89"
    @eval_fn
    def C107():
        b89_1 = Input_EIA_Crude_Europe_Brent.B89()
        return b89_1

@register(Crude_Oil_Prices)
class A108():
    # 'Crude_Oil_Prices'!A108
    value = 34561
    isdatetime = True

@register(Crude_Oil_Prices)
class B108():
    # 'Crude_Oil_Prices'!B108
    value = 18.38
    formula = "='Input EIA Crude WTI'!B106"
    @eval_fn
    def B108():
        b106_1 = Input_EIA_Crude_WTI.B106()
        return b106_1

@register(Crude_Oil_Prices)
class C108():
    # 'Crude_Oil_Prices'!C108
    value = 16.89
    formula = "='Input EIA Crude Europe Brent'!B90"
    @eval_fn
    def C108():
        b90_1 = Input_EIA_Crude_Europe_Brent.B90()
        return b90_1

@register(Crude_Oil_Prices)
class A109():
    # 'Crude_Oil_Prices'!A109
    value = 34592
    isdatetime = True

@register(Crude_Oil_Prices)
class B109():
    # 'Crude_Oil_Prices'!B109
    value = 17.45
    formula = "='Input EIA Crude WTI'!B107"
    @eval_fn
    def B109():
        b107_1 = Input_EIA_Crude_WTI.B107()
        return b107_1

@register(Crude_Oil_Prices)
class C109():
    # 'Crude_Oil_Prices'!C109
    value = 15.9
    formula = "='Input EIA Crude Europe Brent'!B91"
    @eval_fn
    def C109():
        b91_1 = Input_EIA_Crude_Europe_Brent.B91()
        return b91_1

@register(Crude_Oil_Prices)
class A110():
    # 'Crude_Oil_Prices'!A110
    value = 34622
    isdatetime = True

@register(Crude_Oil_Prices)
class B110():
    # 'Crude_Oil_Prices'!B110
    value = 17.72
    formula = "='Input EIA Crude WTI'!B108"
    @eval_fn
    def B110():
        b108_1 = Input_EIA_Crude_WTI.B108()
        return b108_1

@register(Crude_Oil_Prices)
class C110():
    # 'Crude_Oil_Prices'!C110
    value = 16.49
    formula = "='Input EIA Crude Europe Brent'!B92"
    @eval_fn
    def C110():
        b92_1 = Input_EIA_Crude_Europe_Brent.B92()
        return b92_1

@register(Crude_Oil_Prices)
class A111():
    # 'Crude_Oil_Prices'!A111
    value = 34653
    isdatetime = True

@register(Crude_Oil_Prices)
class B111():
    # 'Crude_Oil_Prices'!B111
    value = 18.07
    formula = "='Input EIA Crude WTI'!B109"
    @eval_fn
    def B111():
        b109_1 = Input_EIA_Crude_WTI.B109()
        return b109_1

@register(Crude_Oil_Prices)
class C111():
    # 'Crude_Oil_Prices'!C111
    value = 17.19
    formula = "='Input EIA Crude Europe Brent'!B93"
    @eval_fn
    def C111():
        b93_1 = Input_EIA_Crude_Europe_Brent.B93()
        return b93_1

@register(Crude_Oil_Prices)
class A112():
    # 'Crude_Oil_Prices'!A112
    value = 34683
    isdatetime = True

@register(Crude_Oil_Prices)
class B112():
    # 'Crude_Oil_Prices'!B112
    value = 17.16
    formula = "='Input EIA Crude WTI'!B110"
    @eval_fn
    def B112():
        b110_1 = Input_EIA_Crude_WTI.B110()
        return b110_1

@register(Crude_Oil_Prices)
class C112():
    # 'Crude_Oil_Prices'!C112
    value = 15.93
    formula = "='Input EIA Crude Europe Brent'!B94"
    @eval_fn
    def C112():
        b94_1 = Input_EIA_Crude_Europe_Brent.B94()
        return b94_1

@register(Crude_Oil_Prices)
class A113():
    # 'Crude_Oil_Prices'!A113
    value = 34714
    isdatetime = True

@register(Crude_Oil_Prices)
class B113():
    # 'Crude_Oil_Prices'!B113
    value = 18.04
    formula = "='Input EIA Crude WTI'!B111"
    @eval_fn
    def B113():
        b111_1 = Input_EIA_Crude_WTI.B111()
        return b111_1

@register(Crude_Oil_Prices)
class C113():
    # 'Crude_Oil_Prices'!C113
    value = 16.55
    formula = "='Input EIA Crude Europe Brent'!B95"
    @eval_fn
    def C113():
        b95_1 = Input_EIA_Crude_Europe_Brent.B95()
        return b95_1

@register(Crude_Oil_Prices)
class A114():
    # 'Crude_Oil_Prices'!A114
    value = 34745
    isdatetime = True

@register(Crude_Oil_Prices)
class B114():
    # 'Crude_Oil_Prices'!B114
    value = 18.57
    formula = "='Input EIA Crude WTI'!B112"
    @eval_fn
    def B114():
        b112_1 = Input_EIA_Crude_WTI.B112()
        return b112_1

@register(Crude_Oil_Prices)
class C114():
    # 'Crude_Oil_Prices'!C114
    value = 17.11
    formula = "='Input EIA Crude Europe Brent'!B96"
    @eval_fn
    def C114():
        b96_1 = Input_EIA_Crude_Europe_Brent.B96()
        return b96_1

@register(Crude_Oil_Prices)
class A115():
    # 'Crude_Oil_Prices'!A115
    value = 34773
    isdatetime = True

@register(Crude_Oil_Prices)
class B115():
    # 'Crude_Oil_Prices'!B115
    value = 18.54
    formula = "='Input EIA Crude WTI'!B113"
    @eval_fn
    def B115():
        b113_1 = Input_EIA_Crude_WTI.B113()
        return b113_1

@register(Crude_Oil_Prices)
class C115():
    # 'Crude_Oil_Prices'!C115
    value = 17.01
    formula = "='Input EIA Crude Europe Brent'!B97"
    @eval_fn
    def C115():
        b97_1 = Input_EIA_Crude_Europe_Brent.B97()
        return b97_1

@register(Crude_Oil_Prices)
class A116():
    # 'Crude_Oil_Prices'!A116
    value = 34804
    isdatetime = True

@register(Crude_Oil_Prices)
class B116():
    # 'Crude_Oil_Prices'!B116
    value = 19.9
    formula = "='Input EIA Crude WTI'!B114"
    @eval_fn
    def B116():
        b114_1 = Input_EIA_Crude_WTI.B114()
        return b114_1

@register(Crude_Oil_Prices)
class C116():
    # 'Crude_Oil_Prices'!C116
    value = 18.65
    formula = "='Input EIA Crude Europe Brent'!B98"
    @eval_fn
    def C116():
        b98_1 = Input_EIA_Crude_Europe_Brent.B98()
        return b98_1

@register(Crude_Oil_Prices)
class A117():
    # 'Crude_Oil_Prices'!A117
    value = 34834
    isdatetime = True

@register(Crude_Oil_Prices)
class B117():
    # 'Crude_Oil_Prices'!B117
    value = 19.74
    formula = "='Input EIA Crude WTI'!B115"
    @eval_fn
    def B117():
        b115_1 = Input_EIA_Crude_WTI.B115()
        return b115_1

@register(Crude_Oil_Prices)
class C117():
    # 'Crude_Oil_Prices'!C117
    value = 18.35
    formula = "='Input EIA Crude Europe Brent'!B99"
    @eval_fn
    def C117():
        b99_1 = Input_EIA_Crude_Europe_Brent.B99()
        return b99_1

@register(Crude_Oil_Prices)
class A118():
    # 'Crude_Oil_Prices'!A118
    value = 34865
    isdatetime = True

@register(Crude_Oil_Prices)
class B118():
    # 'Crude_Oil_Prices'!B118
    value = 18.45
    formula = "='Input EIA Crude WTI'!B116"
    @eval_fn
    def B118():
        b116_1 = Input_EIA_Crude_WTI.B116()
        return b116_1

@register(Crude_Oil_Prices)
class C118():
    # 'Crude_Oil_Prices'!C118
    value = 17.31
    formula = "='Input EIA Crude Europe Brent'!B100"
    @eval_fn
    def C118():
        b100_1 = Input_EIA_Crude_Europe_Brent.B100()
        return b100_1

@register(Crude_Oil_Prices)
class A119():
    # 'Crude_Oil_Prices'!A119
    value = 34895
    isdatetime = True

@register(Crude_Oil_Prices)
class B119():
    # 'Crude_Oil_Prices'!B119
    value = 17.33
    formula = "='Input EIA Crude WTI'!B117"
    @eval_fn
    def B119():
        b117_1 = Input_EIA_Crude_WTI.B117()
        return b117_1

@register(Crude_Oil_Prices)
class C119():
    # 'Crude_Oil_Prices'!C119
    value = 15.85
    formula = "='Input EIA Crude Europe Brent'!B101"
    @eval_fn
    def C119():
        b101_1 = Input_EIA_Crude_Europe_Brent.B101()
        return b101_1

@register(Crude_Oil_Prices)
class A120():
    # 'Crude_Oil_Prices'!A120
    value = 34926
    isdatetime = True

@register(Crude_Oil_Prices)
class B120():
    # 'Crude_Oil_Prices'!B120
    value = 18.02
    formula = "='Input EIA Crude WTI'!B118"
    @eval_fn
    def B120():
        b118_1 = Input_EIA_Crude_WTI.B118()
        return b118_1

@register(Crude_Oil_Prices)
class C120():
    # 'Crude_Oil_Prices'!C120
    value = 16.1
    formula = "='Input EIA Crude Europe Brent'!B102"
    @eval_fn
    def C120():
        b102_1 = Input_EIA_Crude_Europe_Brent.B102()
        return b102_1

@register(Crude_Oil_Prices)
class A121():
    # 'Crude_Oil_Prices'!A121
    value = 34957
    isdatetime = True

@register(Crude_Oil_Prices)
class B121():
    # 'Crude_Oil_Prices'!B121
    value = 18.23
    formula = "='Input EIA Crude WTI'!B119"
    @eval_fn
    def B121():
        b119_1 = Input_EIA_Crude_WTI.B119()
        return b119_1

@register(Crude_Oil_Prices)
class C121():
    # 'Crude_Oil_Prices'!C121
    value = 16.7
    formula = "='Input EIA Crude Europe Brent'!B103"
    @eval_fn
    def C121():
        b103_1 = Input_EIA_Crude_Europe_Brent.B103()
        return b103_1

@register(Crude_Oil_Prices)
class A122():
    # 'Crude_Oil_Prices'!A122
    value = 34987
    isdatetime = True

@register(Crude_Oil_Prices)
class B122():
    # 'Crude_Oil_Prices'!B122
    value = 17.43
    formula = "='Input EIA Crude WTI'!B120"
    @eval_fn
    def B122():
        b120_1 = Input_EIA_Crude_WTI.B120()
        return b120_1

@register(Crude_Oil_Prices)
class C122():
    # 'Crude_Oil_Prices'!C122
    value = 16.11
    formula = "='Input EIA Crude Europe Brent'!B104"
    @eval_fn
    def C122():
        b104_1 = Input_EIA_Crude_Europe_Brent.B104()
        return b104_1

@register(Crude_Oil_Prices)
class A123():
    # 'Crude_Oil_Prices'!A123
    value = 35018
    isdatetime = True

@register(Crude_Oil_Prices)
class B123():
    # 'Crude_Oil_Prices'!B123
    value = 17.99
    formula = "='Input EIA Crude WTI'!B121"
    @eval_fn
    def B123():
        b121_1 = Input_EIA_Crude_WTI.B121()
        return b121_1

@register(Crude_Oil_Prices)
class C123():
    # 'Crude_Oil_Prices'!C123
    value = 16.86
    formula = "='Input EIA Crude Europe Brent'!B105"
    @eval_fn
    def C123():
        b105_1 = Input_EIA_Crude_Europe_Brent.B105()
        return b105_1

@register(Crude_Oil_Prices)
class A124():
    # 'Crude_Oil_Prices'!A124
    value = 35048
    isdatetime = True

@register(Crude_Oil_Prices)
class B124():
    # 'Crude_Oil_Prices'!B124
    value = 19.03
    formula = "='Input EIA Crude WTI'!B122"
    @eval_fn
    def B124():
        b122_1 = Input_EIA_Crude_WTI.B122()
        return b122_1

@register(Crude_Oil_Prices)
class C124():
    # 'Crude_Oil_Prices'!C124
    value = 17.93
    formula = "='Input EIA Crude Europe Brent'!B106"
    @eval_fn
    def C124():
        b106_1 = Input_EIA_Crude_Europe_Brent.B106()
        return b106_1

@register(Crude_Oil_Prices)
class A125():
    # 'Crude_Oil_Prices'!A125
    value = 35079
    isdatetime = True

@register(Crude_Oil_Prices)
class B125():
    # 'Crude_Oil_Prices'!B125
    value = 18.86
    formula = "='Input EIA Crude WTI'!B123"
    @eval_fn
    def B125():
        b123_1 = Input_EIA_Crude_WTI.B123()
        return b123_1

@register(Crude_Oil_Prices)
class C125():
    # 'Crude_Oil_Prices'!C125
    value = 17.85
    formula = "='Input EIA Crude Europe Brent'!B107"
    @eval_fn
    def C125():
        b107_1 = Input_EIA_Crude_Europe_Brent.B107()
        return b107_1

@register(Crude_Oil_Prices)
class A126():
    # 'Crude_Oil_Prices'!A126
    value = 35110
    isdatetime = True

@register(Crude_Oil_Prices)
class B126():
    # 'Crude_Oil_Prices'!B126
    value = 19.09
    formula = "='Input EIA Crude WTI'!B124"
    @eval_fn
    def B126():
        b124_1 = Input_EIA_Crude_WTI.B124()
        return b124_1

@register(Crude_Oil_Prices)
class C126():
    # 'Crude_Oil_Prices'!C126
    value = 18
    formula = "='Input EIA Crude Europe Brent'!B108"
    @eval_fn
    def C126():
        b108_1 = Input_EIA_Crude_Europe_Brent.B108()
        return b108_1

@register(Crude_Oil_Prices)
class A127():
    # 'Crude_Oil_Prices'!A127
    value = 35139
    isdatetime = True

@register(Crude_Oil_Prices)
class B127():
    # 'Crude_Oil_Prices'!B127
    value = 21.33
    formula = "='Input EIA Crude WTI'!B125"
    @eval_fn
    def B127():
        b125_1 = Input_EIA_Crude_WTI.B125()
        return b125_1

@register(Crude_Oil_Prices)
class C127():
    # 'Crude_Oil_Prices'!C127
    value = 19.85
    formula = "='Input EIA Crude Europe Brent'!B109"
    @eval_fn
    def C127():
        b109_1 = Input_EIA_Crude_Europe_Brent.B109()
        return b109_1

@register(Crude_Oil_Prices)
class A128():
    # 'Crude_Oil_Prices'!A128
    value = 35170
    isdatetime = True

@register(Crude_Oil_Prices)
class B128():
    # 'Crude_Oil_Prices'!B128
    value = 23.5
    formula = "='Input EIA Crude WTI'!B126"
    @eval_fn
    def B128():
        b126_1 = Input_EIA_Crude_WTI.B126()
        return b126_1

@register(Crude_Oil_Prices)
class C128():
    # 'Crude_Oil_Prices'!C128
    value = 20.9
    formula = "='Input EIA Crude Europe Brent'!B110"
    @eval_fn
    def C128():
        b110_1 = Input_EIA_Crude_Europe_Brent.B110()
        return b110_1

@register(Crude_Oil_Prices)
class A129():
    # 'Crude_Oil_Prices'!A129
    value = 35200
    isdatetime = True

@register(Crude_Oil_Prices)
class B129():
    # 'Crude_Oil_Prices'!B129
    value = 21.17
    formula = "='Input EIA Crude WTI'!B127"
    @eval_fn
    def B129():
        b127_1 = Input_EIA_Crude_WTI.B127()
        return b127_1

@register(Crude_Oil_Prices)
class C129():
    # 'Crude_Oil_Prices'!C129
    value = 19.15
    formula = "='Input EIA Crude Europe Brent'!B111"
    @eval_fn
    def C129():
        b111_1 = Input_EIA_Crude_Europe_Brent.B111()
        return b111_1

@register(Crude_Oil_Prices)
class A130():
    # 'Crude_Oil_Prices'!A130
    value = 35231
    isdatetime = True

@register(Crude_Oil_Prices)
class B130():
    # 'Crude_Oil_Prices'!B130
    value = 20.42
    formula = "='Input EIA Crude WTI'!B128"
    @eval_fn
    def B130():
        b128_1 = Input_EIA_Crude_WTI.B128()
        return b128_1

@register(Crude_Oil_Prices)
class C130():
    # 'Crude_Oil_Prices'!C130
    value = 18.46
    formula = "='Input EIA Crude Europe Brent'!B112"
    @eval_fn
    def C130():
        b112_1 = Input_EIA_Crude_Europe_Brent.B112()
        return b112_1

@register(Crude_Oil_Prices)
class A131():
    # 'Crude_Oil_Prices'!A131
    value = 35261
    isdatetime = True

@register(Crude_Oil_Prices)
class B131():
    # 'Crude_Oil_Prices'!B131
    value = 21.3
    formula = "='Input EIA Crude WTI'!B129"
    @eval_fn
    def B131():
        b129_1 = Input_EIA_Crude_WTI.B129()
        return b129_1

@register(Crude_Oil_Prices)
class C131():
    # 'Crude_Oil_Prices'!C131
    value = 19.57
    formula = "='Input EIA Crude Europe Brent'!B113"
    @eval_fn
    def C131():
        b113_1 = Input_EIA_Crude_Europe_Brent.B113()
        return b113_1

@register(Crude_Oil_Prices)
class A132():
    # 'Crude_Oil_Prices'!A132
    value = 35292
    isdatetime = True

@register(Crude_Oil_Prices)
class B132():
    # 'Crude_Oil_Prices'!B132
    value = 21.9
    formula = "='Input EIA Crude WTI'!B130"
    @eval_fn
    def B132():
        b130_1 = Input_EIA_Crude_WTI.B130()
        return b130_1

@register(Crude_Oil_Prices)
class C132():
    # 'Crude_Oil_Prices'!C132
    value = 20.51
    formula = "='Input EIA Crude Europe Brent'!B114"
    @eval_fn
    def C132():
        b114_1 = Input_EIA_Crude_Europe_Brent.B114()
        return b114_1

@register(Crude_Oil_Prices)
class A133():
    # 'Crude_Oil_Prices'!A133
    value = 35323
    isdatetime = True

@register(Crude_Oil_Prices)
class B133():
    # 'Crude_Oil_Prices'!B133
    value = 23.97
    formula = "='Input EIA Crude WTI'!B131"
    @eval_fn
    def B133():
        b131_1 = Input_EIA_Crude_WTI.B131()
        return b131_1

@register(Crude_Oil_Prices)
class C133():
    # 'Crude_Oil_Prices'!C133
    value = 22.63
    formula = "='Input EIA Crude Europe Brent'!B115"
    @eval_fn
    def C133():
        b115_1 = Input_EIA_Crude_Europe_Brent.B115()
        return b115_1

@register(Crude_Oil_Prices)
class A134():
    # 'Crude_Oil_Prices'!A134
    value = 35353
    isdatetime = True

@register(Crude_Oil_Prices)
class B134():
    # 'Crude_Oil_Prices'!B134
    value = 24.88
    formula = "='Input EIA Crude WTI'!B132"
    @eval_fn
    def B134():
        b132_1 = Input_EIA_Crude_WTI.B132()
        return b132_1

@register(Crude_Oil_Prices)
class C134():
    # 'Crude_Oil_Prices'!C134
    value = 24.16
    formula = "='Input EIA Crude Europe Brent'!B116"
    @eval_fn
    def C134():
        b116_1 = Input_EIA_Crude_Europe_Brent.B116()
        return b116_1

@register(Crude_Oil_Prices)
class A135():
    # 'Crude_Oil_Prices'!A135
    value = 35384
    isdatetime = True

@register(Crude_Oil_Prices)
class B135():
    # 'Crude_Oil_Prices'!B135
    value = 23.71
    formula = "='Input EIA Crude WTI'!B133"
    @eval_fn
    def B135():
        b133_1 = Input_EIA_Crude_WTI.B133()
        return b133_1

@register(Crude_Oil_Prices)
class C135():
    # 'Crude_Oil_Prices'!C135
    value = 22.76
    formula = "='Input EIA Crude Europe Brent'!B117"
    @eval_fn
    def C135():
        b117_1 = Input_EIA_Crude_Europe_Brent.B117()
        return b117_1

@register(Crude_Oil_Prices)
class A136():
    # 'Crude_Oil_Prices'!A136
    value = 35414
    isdatetime = True

@register(Crude_Oil_Prices)
class B136():
    # 'Crude_Oil_Prices'!B136
    value = 25.23
    formula = "='Input EIA Crude WTI'!B134"
    @eval_fn
    def B136():
        b134_1 = Input_EIA_Crude_WTI.B134()
        return b134_1

@register(Crude_Oil_Prices)
class C136():
    # 'Crude_Oil_Prices'!C136
    value = 23.78
    formula = "='Input EIA Crude Europe Brent'!B118"
    @eval_fn
    def C136():
        b118_1 = Input_EIA_Crude_Europe_Brent.B118()
        return b118_1

@register(Crude_Oil_Prices)
class A137():
    # 'Crude_Oil_Prices'!A137
    value = 35445
    isdatetime = True

@register(Crude_Oil_Prices)
class B137():
    # 'Crude_Oil_Prices'!B137
    value = 25.13
    formula = "='Input EIA Crude WTI'!B135"
    @eval_fn
    def B137():
        b135_1 = Input_EIA_Crude_WTI.B135()
        return b135_1

@register(Crude_Oil_Prices)
class C137():
    # 'Crude_Oil_Prices'!C137
    value = 23.54
    formula = "='Input EIA Crude Europe Brent'!B119"
    @eval_fn
    def C137():
        b119_1 = Input_EIA_Crude_Europe_Brent.B119()
        return b119_1

@register(Crude_Oil_Prices)
class A138():
    # 'Crude_Oil_Prices'!A138
    value = 35476
    isdatetime = True

@register(Crude_Oil_Prices)
class B138():
    # 'Crude_Oil_Prices'!B138
    value = 22.18
    formula = "='Input EIA Crude WTI'!B136"
    @eval_fn
    def B138():
        b136_1 = Input_EIA_Crude_WTI.B136()
        return b136_1

@register(Crude_Oil_Prices)
class C138():
    # 'Crude_Oil_Prices'!C138
    value = 20.85
    formula = "='Input EIA Crude Europe Brent'!B120"
    @eval_fn
    def C138():
        b120_1 = Input_EIA_Crude_Europe_Brent.B120()
        return b120_1

@register(Crude_Oil_Prices)
class A139():
    # 'Crude_Oil_Prices'!A139
    value = 35504
    isdatetime = True

@register(Crude_Oil_Prices)
class B139():
    # 'Crude_Oil_Prices'!B139
    value = 20.97
    formula = "='Input EIA Crude WTI'!B137"
    @eval_fn
    def B139():
        b137_1 = Input_EIA_Crude_WTI.B137()
        return b137_1

@register(Crude_Oil_Prices)
class C139():
    # 'Crude_Oil_Prices'!C139
    value = 19.13
    formula = "='Input EIA Crude Europe Brent'!B121"
    @eval_fn
    def C139():
        b121_1 = Input_EIA_Crude_Europe_Brent.B121()
        return b121_1

@register(Crude_Oil_Prices)
class A140():
    # 'Crude_Oil_Prices'!A140
    value = 35535
    isdatetime = True

@register(Crude_Oil_Prices)
class B140():
    # 'Crude_Oil_Prices'!B140
    value = 19.7
    formula = "='Input EIA Crude WTI'!B138"
    @eval_fn
    def B140():
        b138_1 = Input_EIA_Crude_WTI.B138()
        return b138_1

@register(Crude_Oil_Prices)
class C140():
    # 'Crude_Oil_Prices'!C140
    value = 17.56
    formula = "='Input EIA Crude Europe Brent'!B122"
    @eval_fn
    def C140():
        b122_1 = Input_EIA_Crude_Europe_Brent.B122()
        return b122_1

@register(Crude_Oil_Prices)
class A141():
    # 'Crude_Oil_Prices'!A141
    value = 35565
    isdatetime = True

@register(Crude_Oil_Prices)
class B141():
    # 'Crude_Oil_Prices'!B141
    value = 20.82
    formula = "='Input EIA Crude WTI'!B139"
    @eval_fn
    def B141():
        b139_1 = Input_EIA_Crude_WTI.B139()
        return b139_1

@register(Crude_Oil_Prices)
class C141():
    # 'Crude_Oil_Prices'!C141
    value = 19.02
    formula = "='Input EIA Crude Europe Brent'!B123"
    @eval_fn
    def C141():
        b123_1 = Input_EIA_Crude_Europe_Brent.B123()
        return b123_1

@register(Crude_Oil_Prices)
class A142():
    # 'Crude_Oil_Prices'!A142
    value = 35596
    isdatetime = True

@register(Crude_Oil_Prices)
class B142():
    # 'Crude_Oil_Prices'!B142
    value = 19.26
    formula = "='Input EIA Crude WTI'!B140"
    @eval_fn
    def B142():
        b140_1 = Input_EIA_Crude_WTI.B140()
        return b140_1

@register(Crude_Oil_Prices)
class C142():
    # 'Crude_Oil_Prices'!C142
    value = 17.58
    formula = "='Input EIA Crude Europe Brent'!B124"
    @eval_fn
    def C142():
        b124_1 = Input_EIA_Crude_Europe_Brent.B124()
        return b124_1

@register(Crude_Oil_Prices)
class A143():
    # 'Crude_Oil_Prices'!A143
    value = 35626
    isdatetime = True

@register(Crude_Oil_Prices)
class B143():
    # 'Crude_Oil_Prices'!B143
    value = 19.66
    formula = "='Input EIA Crude WTI'!B141"
    @eval_fn
    def B143():
        b141_1 = Input_EIA_Crude_WTI.B141()
        return b141_1

@register(Crude_Oil_Prices)
class C143():
    # 'Crude_Oil_Prices'!C143
    value = 18.46
    formula = "='Input EIA Crude Europe Brent'!B125"
    @eval_fn
    def C143():
        b125_1 = Input_EIA_Crude_Europe_Brent.B125()
        return b125_1

@register(Crude_Oil_Prices)
class A144():
    # 'Crude_Oil_Prices'!A144
    value = 35657
    isdatetime = True

@register(Crude_Oil_Prices)
class B144():
    # 'Crude_Oil_Prices'!B144
    value = 19.95
    formula = "='Input EIA Crude WTI'!B142"
    @eval_fn
    def B144():
        b142_1 = Input_EIA_Crude_WTI.B142()
        return b142_1

@register(Crude_Oil_Prices)
class C144():
    # 'Crude_Oil_Prices'!C144
    value = 18.6
    formula = "='Input EIA Crude Europe Brent'!B126"
    @eval_fn
    def C144():
        b126_1 = Input_EIA_Crude_Europe_Brent.B126()
        return b126_1

@register(Crude_Oil_Prices)
class A145():
    # 'Crude_Oil_Prices'!A145
    value = 35688
    isdatetime = True

@register(Crude_Oil_Prices)
class B145():
    # 'Crude_Oil_Prices'!B145
    value = 19.8
    formula = "='Input EIA Crude WTI'!B143"
    @eval_fn
    def B145():
        b143_1 = Input_EIA_Crude_WTI.B143()
        return b143_1

@register(Crude_Oil_Prices)
class C145():
    # 'Crude_Oil_Prices'!C145
    value = 18.46
    formula = "='Input EIA Crude Europe Brent'!B127"
    @eval_fn
    def C145():
        b127_1 = Input_EIA_Crude_Europe_Brent.B127()
        return b127_1

@register(Crude_Oil_Prices)
class A146():
    # 'Crude_Oil_Prices'!A146
    value = 35718
    isdatetime = True

@register(Crude_Oil_Prices)
class B146():
    # 'Crude_Oil_Prices'!B146
    value = 21.33
    formula = "='Input EIA Crude WTI'!B144"
    @eval_fn
    def B146():
        b144_1 = Input_EIA_Crude_WTI.B144()
        return b144_1

@register(Crude_Oil_Prices)
class C146():
    # 'Crude_Oil_Prices'!C146
    value = 19.87
    formula = "='Input EIA Crude Europe Brent'!B128"
    @eval_fn
    def C146():
        b128_1 = Input_EIA_Crude_Europe_Brent.B128()
        return b128_1

@register(Crude_Oil_Prices)
class A147():
    # 'Crude_Oil_Prices'!A147
    value = 35749
    isdatetime = True

@register(Crude_Oil_Prices)
class B147():
    # 'Crude_Oil_Prices'!B147
    value = 20.19
    formula = "='Input EIA Crude WTI'!B145"
    @eval_fn
    def B147():
        b145_1 = Input_EIA_Crude_WTI.B145()
        return b145_1

@register(Crude_Oil_Prices)
class C147():
    # 'Crude_Oil_Prices'!C147
    value = 19.17
    formula = "='Input EIA Crude Europe Brent'!B129"
    @eval_fn
    def C147():
        b129_1 = Input_EIA_Crude_Europe_Brent.B129()
        return b129_1

@register(Crude_Oil_Prices)
class A148():
    # 'Crude_Oil_Prices'!A148
    value = 35779
    isdatetime = True

@register(Crude_Oil_Prices)
class B148():
    # 'Crude_Oil_Prices'!B148
    value = 18.33
    formula = "='Input EIA Crude WTI'!B146"
    @eval_fn
    def B148():
        b146_1 = Input_EIA_Crude_WTI.B146()
        return b146_1

@register(Crude_Oil_Prices)
class C148():
    # 'Crude_Oil_Prices'!C148
    value = 17.18
    formula = "='Input EIA Crude Europe Brent'!B130"
    @eval_fn
    def C148():
        b130_1 = Input_EIA_Crude_Europe_Brent.B130()
        return b130_1

@register(Crude_Oil_Prices)
class A149():
    # 'Crude_Oil_Prices'!A149
    value = 35810
    isdatetime = True

@register(Crude_Oil_Prices)
class B149():
    # 'Crude_Oil_Prices'!B149
    value = 16.72
    formula = "='Input EIA Crude WTI'!B147"
    @eval_fn
    def B149():
        b147_1 = Input_EIA_Crude_WTI.B147()
        return b147_1

@register(Crude_Oil_Prices)
class C149():
    # 'Crude_Oil_Prices'!C149
    value = 15.19
    formula = "='Input EIA Crude Europe Brent'!B131"
    @eval_fn
    def C149():
        b131_1 = Input_EIA_Crude_Europe_Brent.B131()
        return b131_1

@register(Crude_Oil_Prices)
class A150():
    # 'Crude_Oil_Prices'!A150
    value = 35841
    isdatetime = True

@register(Crude_Oil_Prices)
class B150():
    # 'Crude_Oil_Prices'!B150
    value = 16.06
    formula = "='Input EIA Crude WTI'!B148"
    @eval_fn
    def B150():
        b148_1 = Input_EIA_Crude_WTI.B148()
        return b148_1

@register(Crude_Oil_Prices)
class C150():
    # 'Crude_Oil_Prices'!C150
    value = 14.07
    formula = "='Input EIA Crude Europe Brent'!B132"
    @eval_fn
    def C150():
        b132_1 = Input_EIA_Crude_Europe_Brent.B132()
        return b132_1

@register(Crude_Oil_Prices)
class A151():
    # 'Crude_Oil_Prices'!A151
    value = 35869
    isdatetime = True

@register(Crude_Oil_Prices)
class B151():
    # 'Crude_Oil_Prices'!B151
    value = 15.12
    formula = "='Input EIA Crude WTI'!B149"
    @eval_fn
    def B151():
        b149_1 = Input_EIA_Crude_WTI.B149()
        return b149_1

@register(Crude_Oil_Prices)
class C151():
    # 'Crude_Oil_Prices'!C151
    value = 13.1
    formula = "='Input EIA Crude Europe Brent'!B133"
    @eval_fn
    def C151():
        b133_1 = Input_EIA_Crude_Europe_Brent.B133()
        return b133_1

@register(Crude_Oil_Prices)
class A152():
    # 'Crude_Oil_Prices'!A152
    value = 35900
    isdatetime = True

@register(Crude_Oil_Prices)
class B152():
    # 'Crude_Oil_Prices'!B152
    value = 15.35
    formula = "='Input EIA Crude WTI'!B150"
    @eval_fn
    def B152():
        b150_1 = Input_EIA_Crude_WTI.B150()
        return b150_1

@register(Crude_Oil_Prices)
class C152():
    # 'Crude_Oil_Prices'!C152
    value = 13.53
    formula = "='Input EIA Crude Europe Brent'!B134"
    @eval_fn
    def C152():
        b134_1 = Input_EIA_Crude_Europe_Brent.B134()
        return b134_1

@register(Crude_Oil_Prices)
class A153():
    # 'Crude_Oil_Prices'!A153
    value = 35930
    isdatetime = True

@register(Crude_Oil_Prices)
class B153():
    # 'Crude_Oil_Prices'!B153
    value = 14.91
    formula = "='Input EIA Crude WTI'!B151"
    @eval_fn
    def B153():
        b151_1 = Input_EIA_Crude_WTI.B151()
        return b151_1

@register(Crude_Oil_Prices)
class C153():
    # 'Crude_Oil_Prices'!C153
    value = 14.36
    formula = "='Input EIA Crude Europe Brent'!B135"
    @eval_fn
    def C153():
        b135_1 = Input_EIA_Crude_Europe_Brent.B135()
        return b135_1

@register(Crude_Oil_Prices)
class A154():
    # 'Crude_Oil_Prices'!A154
    value = 35961
    isdatetime = True

@register(Crude_Oil_Prices)
class B154():
    # 'Crude_Oil_Prices'!B154
    value = 13.72
    formula = "='Input EIA Crude WTI'!B152"
    @eval_fn
    def B154():
        b152_1 = Input_EIA_Crude_WTI.B152()
        return b152_1

@register(Crude_Oil_Prices)
class C154():
    # 'Crude_Oil_Prices'!C154
    value = 12.21
    formula = "='Input EIA Crude Europe Brent'!B136"
    @eval_fn
    def C154():
        b136_1 = Input_EIA_Crude_Europe_Brent.B136()
        return b136_1

@register(Crude_Oil_Prices)
class A155():
    # 'Crude_Oil_Prices'!A155
    value = 35991
    isdatetime = True

@register(Crude_Oil_Prices)
class B155():
    # 'Crude_Oil_Prices'!B155
    value = 14.17
    formula = "='Input EIA Crude WTI'!B153"
    @eval_fn
    def B155():
        b153_1 = Input_EIA_Crude_WTI.B153()
        return b153_1

@register(Crude_Oil_Prices)
class C155():
    # 'Crude_Oil_Prices'!C155
    value = 12.08
    formula = "='Input EIA Crude Europe Brent'!B137"
    @eval_fn
    def C155():
        b137_1 = Input_EIA_Crude_Europe_Brent.B137()
        return b137_1

@register(Crude_Oil_Prices)
class A156():
    # 'Crude_Oil_Prices'!A156
    value = 36022
    isdatetime = True

@register(Crude_Oil_Prices)
class B156():
    # 'Crude_Oil_Prices'!B156
    value = 13.47
    formula = "='Input EIA Crude WTI'!B154"
    @eval_fn
    def B156():
        b154_1 = Input_EIA_Crude_WTI.B154()
        return b154_1

@register(Crude_Oil_Prices)
class C156():
    # 'Crude_Oil_Prices'!C156
    value = 11.91
    formula = "='Input EIA Crude Europe Brent'!B138"
    @eval_fn
    def C156():
        b138_1 = Input_EIA_Crude_Europe_Brent.B138()
        return b138_1

@register(Crude_Oil_Prices)
class A157():
    # 'Crude_Oil_Prices'!A157
    value = 36053
    isdatetime = True

@register(Crude_Oil_Prices)
class B157():
    # 'Crude_Oil_Prices'!B157
    value = 15.03
    formula = "='Input EIA Crude WTI'!B155"
    @eval_fn
    def B157():
        b155_1 = Input_EIA_Crude_WTI.B155()
        return b155_1

@register(Crude_Oil_Prices)
class C157():
    # 'Crude_Oil_Prices'!C157
    value = 13.34
    formula = "='Input EIA Crude Europe Brent'!B139"
    @eval_fn
    def C157():
        b139_1 = Input_EIA_Crude_Europe_Brent.B139()
        return b139_1

@register(Crude_Oil_Prices)
class A158():
    # 'Crude_Oil_Prices'!A158
    value = 36083
    isdatetime = True

@register(Crude_Oil_Prices)
class B158():
    # 'Crude_Oil_Prices'!B158
    value = 14.46
    formula = "='Input EIA Crude WTI'!B156"
    @eval_fn
    def B158():
        b156_1 = Input_EIA_Crude_WTI.B156()
        return b156_1

@register(Crude_Oil_Prices)
class C158():
    # 'Crude_Oil_Prices'!C158
    value = 12.7
    formula = "='Input EIA Crude Europe Brent'!B140"
    @eval_fn
    def C158():
        b140_1 = Input_EIA_Crude_Europe_Brent.B140()
        return b140_1

@register(Crude_Oil_Prices)
class A159():
    # 'Crude_Oil_Prices'!A159
    value = 36114
    isdatetime = True

@register(Crude_Oil_Prices)
class B159():
    # 'Crude_Oil_Prices'!B159
    value = 13
    formula = "='Input EIA Crude WTI'!B157"
    @eval_fn
    def B159():
        b157_1 = Input_EIA_Crude_WTI.B157()
        return b157_1

@register(Crude_Oil_Prices)
class C159():
    # 'Crude_Oil_Prices'!C159
    value = 11.04
    formula = "='Input EIA Crude Europe Brent'!B141"
    @eval_fn
    def C159():
        b141_1 = Input_EIA_Crude_Europe_Brent.B141()
        return b141_1

@register(Crude_Oil_Prices)
class A160():
    # 'Crude_Oil_Prices'!A160
    value = 36144
    isdatetime = True

@register(Crude_Oil_Prices)
class B160():
    # 'Crude_Oil_Prices'!B160
    value = 11.35
    formula = "='Input EIA Crude WTI'!B158"
    @eval_fn
    def B160():
        b158_1 = Input_EIA_Crude_WTI.B158()
        return b158_1

@register(Crude_Oil_Prices)
class C160():
    # 'Crude_Oil_Prices'!C160
    value = 9.82
    formula = "='Input EIA Crude Europe Brent'!B142"
    @eval_fn
    def C160():
        b142_1 = Input_EIA_Crude_Europe_Brent.B142()
        return b142_1

@register(Crude_Oil_Prices)
class A161():
    # 'Crude_Oil_Prices'!A161
    value = 36175
    isdatetime = True

@register(Crude_Oil_Prices)
class B161():
    # 'Crude_Oil_Prices'!B161
    value = 12.52
    formula = "='Input EIA Crude WTI'!B159"
    @eval_fn
    def B161():
        b159_1 = Input_EIA_Crude_WTI.B159()
        return b159_1

@register(Crude_Oil_Prices)
class C161():
    # 'Crude_Oil_Prices'!C161
    value = 11.11
    formula = "='Input EIA Crude Europe Brent'!B143"
    @eval_fn
    def C161():
        b143_1 = Input_EIA_Crude_Europe_Brent.B143()
        return b143_1

@register(Crude_Oil_Prices)
class A162():
    # 'Crude_Oil_Prices'!A162
    value = 36206
    isdatetime = True

@register(Crude_Oil_Prices)
class B162():
    # 'Crude_Oil_Prices'!B162
    value = 12.01
    formula = "='Input EIA Crude WTI'!B160"
    @eval_fn
    def B162():
        b160_1 = Input_EIA_Crude_WTI.B160()
        return b160_1

@register(Crude_Oil_Prices)
class C162():
    # 'Crude_Oil_Prices'!C162
    value = 10.27
    formula = "='Input EIA Crude Europe Brent'!B144"
    @eval_fn
    def C162():
        b144_1 = Input_EIA_Crude_Europe_Brent.B144()
        return b144_1

@register(Crude_Oil_Prices)
class A163():
    # 'Crude_Oil_Prices'!A163
    value = 36234
    isdatetime = True

@register(Crude_Oil_Prices)
class B163():
    # 'Crude_Oil_Prices'!B163
    value = 14.68
    formula = "='Input EIA Crude WTI'!B161"
    @eval_fn
    def B163():
        b161_1 = Input_EIA_Crude_WTI.B161()
        return b161_1

@register(Crude_Oil_Prices)
class C163():
    # 'Crude_Oil_Prices'!C163
    value = 12.51
    formula = "='Input EIA Crude Europe Brent'!B145"
    @eval_fn
    def C163():
        b145_1 = Input_EIA_Crude_Europe_Brent.B145()
        return b145_1

@register(Crude_Oil_Prices)
class A164():
    # 'Crude_Oil_Prices'!A164
    value = 36265
    isdatetime = True

@register(Crude_Oil_Prices)
class B164():
    # 'Crude_Oil_Prices'!B164
    value = 17.31
    formula = "='Input EIA Crude WTI'!B162"
    @eval_fn
    def B164():
        b162_1 = Input_EIA_Crude_WTI.B162()
        return b162_1

@register(Crude_Oil_Prices)
class C164():
    # 'Crude_Oil_Prices'!C164
    value = 15.29
    formula = "='Input EIA Crude Europe Brent'!B146"
    @eval_fn
    def C164():
        b146_1 = Input_EIA_Crude_Europe_Brent.B146()
        return b146_1

@register(Crude_Oil_Prices)
class A165():
    # 'Crude_Oil_Prices'!A165
    value = 36295
    isdatetime = True

@register(Crude_Oil_Prices)
class B165():
    # 'Crude_Oil_Prices'!B165
    value = 17.72
    formula = "='Input EIA Crude WTI'!B163"
    @eval_fn
    def B165():
        b163_1 = Input_EIA_Crude_WTI.B163()
        return b163_1

@register(Crude_Oil_Prices)
class C165():
    # 'Crude_Oil_Prices'!C165
    value = 15.23
    formula = "='Input EIA Crude Europe Brent'!B147"
    @eval_fn
    def C165():
        b147_1 = Input_EIA_Crude_Europe_Brent.B147()
        return b147_1

@register(Crude_Oil_Prices)
class A166():
    # 'Crude_Oil_Prices'!A166
    value = 36326
    isdatetime = True

@register(Crude_Oil_Prices)
class B166():
    # 'Crude_Oil_Prices'!B166
    value = 17.92
    formula = "='Input EIA Crude WTI'!B164"
    @eval_fn
    def B166():
        b164_1 = Input_EIA_Crude_WTI.B164()
        return b164_1

@register(Crude_Oil_Prices)
class C166():
    # 'Crude_Oil_Prices'!C166
    value = 15.86
    formula = "='Input EIA Crude Europe Brent'!B148"
    @eval_fn
    def C166():
        b148_1 = Input_EIA_Crude_Europe_Brent.B148()
        return b148_1

@register(Crude_Oil_Prices)
class A167():
    # 'Crude_Oil_Prices'!A167
    value = 36356
    isdatetime = True

@register(Crude_Oil_Prices)
class B167():
    # 'Crude_Oil_Prices'!B167
    value = 20.1
    formula = "='Input EIA Crude WTI'!B165"
    @eval_fn
    def B167():
        b165_1 = Input_EIA_Crude_WTI.B165()
        return b165_1

@register(Crude_Oil_Prices)
class C167():
    # 'Crude_Oil_Prices'!C167
    value = 19.08
    formula = "='Input EIA Crude Europe Brent'!B149"
    @eval_fn
    def C167():
        b149_1 = Input_EIA_Crude_Europe_Brent.B149()
        return b149_1

@register(Crude_Oil_Prices)
class A168():
    # 'Crude_Oil_Prices'!A168
    value = 36387
    isdatetime = True

@register(Crude_Oil_Prices)
class B168():
    # 'Crude_Oil_Prices'!B168
    value = 21.28
    formula = "='Input EIA Crude WTI'!B166"
    @eval_fn
    def B168():
        b166_1 = Input_EIA_Crude_WTI.B166()
        return b166_1

@register(Crude_Oil_Prices)
class C168():
    # 'Crude_Oil_Prices'!C168
    value = 20.22
    formula = "='Input EIA Crude Europe Brent'!B150"
    @eval_fn
    def C168():
        b150_1 = Input_EIA_Crude_Europe_Brent.B150()
        return b150_1

@register(Crude_Oil_Prices)
class A169():
    # 'Crude_Oil_Prices'!A169
    value = 36418
    isdatetime = True

@register(Crude_Oil_Prices)
class B169():
    # 'Crude_Oil_Prices'!B169
    value = 23.8
    formula = "='Input EIA Crude WTI'!B167"
    @eval_fn
    def B169():
        b167_1 = Input_EIA_Crude_WTI.B167()
        return b167_1

@register(Crude_Oil_Prices)
class C169():
    # 'Crude_Oil_Prices'!C169
    value = 22.54
    formula = "='Input EIA Crude Europe Brent'!B151"
    @eval_fn
    def C169():
        b151_1 = Input_EIA_Crude_Europe_Brent.B151()
        return b151_1

@register(Crude_Oil_Prices)
class A170():
    # 'Crude_Oil_Prices'!A170
    value = 36448
    isdatetime = True

@register(Crude_Oil_Prices)
class B170():
    # 'Crude_Oil_Prices'!B170
    value = 22.69
    formula = "='Input EIA Crude WTI'!B168"
    @eval_fn
    def B170():
        b168_1 = Input_EIA_Crude_WTI.B168()
        return b168_1

@register(Crude_Oil_Prices)
class C170():
    # 'Crude_Oil_Prices'!C170
    value = 22
    formula = "='Input EIA Crude Europe Brent'!B152"
    @eval_fn
    def C170():
        b152_1 = Input_EIA_Crude_Europe_Brent.B152()
        return b152_1

@register(Crude_Oil_Prices)
class A171():
    # 'Crude_Oil_Prices'!A171
    value = 36479
    isdatetime = True

@register(Crude_Oil_Prices)
class B171():
    # 'Crude_Oil_Prices'!B171
    value = 25
    formula = "='Input EIA Crude WTI'!B169"
    @eval_fn
    def B171():
        b169_1 = Input_EIA_Crude_WTI.B169()
        return b169_1

@register(Crude_Oil_Prices)
class C171():
    # 'Crude_Oil_Prices'!C171
    value = 24.58
    formula = "='Input EIA Crude Europe Brent'!B153"
    @eval_fn
    def C171():
        b153_1 = Input_EIA_Crude_Europe_Brent.B153()
        return b153_1

@register(Crude_Oil_Prices)
class A172():
    # 'Crude_Oil_Prices'!A172
    value = 36509
    isdatetime = True

@register(Crude_Oil_Prices)
class B172():
    # 'Crude_Oil_Prices'!B172
    value = 26.1
    formula = "='Input EIA Crude WTI'!B170"
    @eval_fn
    def B172():
        b170_1 = Input_EIA_Crude_WTI.B170()
        return b170_1

@register(Crude_Oil_Prices)
class C172():
    # 'Crude_Oil_Prices'!C172
    value = 25.47
    formula = "='Input EIA Crude Europe Brent'!B154"
    @eval_fn
    def C172():
        b154_1 = Input_EIA_Crude_Europe_Brent.B154()
        return b154_1

@register(Crude_Oil_Prices)
class A173():
    # 'Crude_Oil_Prices'!A173
    value = 36540
    isdatetime = True

@register(Crude_Oil_Prices)
class B173():
    # 'Crude_Oil_Prices'!B173
    value = 27.26
    formula = "='Input EIA Crude WTI'!B171"
    @eval_fn
    def B173():
        b171_1 = Input_EIA_Crude_WTI.B171()
        return b171_1

@register(Crude_Oil_Prices)
class C173():
    # 'Crude_Oil_Prices'!C173
    value = 25.51
    formula = "='Input EIA Crude Europe Brent'!B155"
    @eval_fn
    def C173():
        b155_1 = Input_EIA_Crude_Europe_Brent.B155()
        return b155_1

@register(Crude_Oil_Prices)
class A174():
    # 'Crude_Oil_Prices'!A174
    value = 36571
    isdatetime = True

@register(Crude_Oil_Prices)
class B174():
    # 'Crude_Oil_Prices'!B174
    value = 29.37
    formula = "='Input EIA Crude WTI'!B172"
    @eval_fn
    def B174():
        b172_1 = Input_EIA_Crude_WTI.B172()
        return b172_1

@register(Crude_Oil_Prices)
class C174():
    # 'Crude_Oil_Prices'!C174
    value = 27.78
    formula = "='Input EIA Crude Europe Brent'!B156"
    @eval_fn
    def C174():
        b156_1 = Input_EIA_Crude_Europe_Brent.B156()
        return b156_1

@register(Crude_Oil_Prices)
class A175():
    # 'Crude_Oil_Prices'!A175
    value = 36600
    isdatetime = True

@register(Crude_Oil_Prices)
class B175():
    # 'Crude_Oil_Prices'!B175
    value = 29.84
    formula = "='Input EIA Crude WTI'!B173"
    @eval_fn
    def B175():
        b173_1 = Input_EIA_Crude_WTI.B173()
        return b173_1

@register(Crude_Oil_Prices)
class C175():
    # 'Crude_Oil_Prices'!C175
    value = 27.49
    formula = "='Input EIA Crude Europe Brent'!B157"
    @eval_fn
    def C175():
        b157_1 = Input_EIA_Crude_Europe_Brent.B157()
        return b157_1

@register(Crude_Oil_Prices)
class A176():
    # 'Crude_Oil_Prices'!A176
    value = 36631
    isdatetime = True

@register(Crude_Oil_Prices)
class B176():
    # 'Crude_Oil_Prices'!B176
    value = 25.72
    formula = "='Input EIA Crude WTI'!B174"
    @eval_fn
    def B176():
        b174_1 = Input_EIA_Crude_WTI.B174()
        return b174_1

@register(Crude_Oil_Prices)
class C176():
    # 'Crude_Oil_Prices'!C176
    value = 22.76
    formula = "='Input EIA Crude Europe Brent'!B158"
    @eval_fn
    def C176():
        b158_1 = Input_EIA_Crude_Europe_Brent.B158()
        return b158_1

@register(Crude_Oil_Prices)
class A177():
    # 'Crude_Oil_Prices'!A177
    value = 36661
    isdatetime = True

@register(Crude_Oil_Prices)
class B177():
    # 'Crude_Oil_Prices'!B177
    value = 28.79
    formula = "='Input EIA Crude WTI'!B175"
    @eval_fn
    def B177():
        b175_1 = Input_EIA_Crude_WTI.B175()
        return b175_1

@register(Crude_Oil_Prices)
class C177():
    # 'Crude_Oil_Prices'!C177
    value = 27.74
    formula = "='Input EIA Crude Europe Brent'!B159"
    @eval_fn
    def C177():
        b159_1 = Input_EIA_Crude_Europe_Brent.B159()
        return b159_1

@register(Crude_Oil_Prices)
class A178():
    # 'Crude_Oil_Prices'!A178
    value = 36692
    isdatetime = True

@register(Crude_Oil_Prices)
class B178():
    # 'Crude_Oil_Prices'!B178
    value = 31.82
    formula = "='Input EIA Crude WTI'!B176"
    @eval_fn
    def B178():
        b176_1 = Input_EIA_Crude_WTI.B176()
        return b176_1

@register(Crude_Oil_Prices)
class C178():
    # 'Crude_Oil_Prices'!C178
    value = 29.8
    formula = "='Input EIA Crude Europe Brent'!B160"
    @eval_fn
    def C178():
        b160_1 = Input_EIA_Crude_Europe_Brent.B160()
        return b160_1

@register(Crude_Oil_Prices)
class A179():
    # 'Crude_Oil_Prices'!A179
    value = 36722
    isdatetime = True

@register(Crude_Oil_Prices)
class B179():
    # 'Crude_Oil_Prices'!B179
    value = 29.7
    formula = "='Input EIA Crude WTI'!B177"
    @eval_fn
    def B179():
        b177_1 = Input_EIA_Crude_WTI.B177()
        return b177_1

@register(Crude_Oil_Prices)
class C179():
    # 'Crude_Oil_Prices'!C179
    value = 28.68
    formula = "='Input EIA Crude Europe Brent'!B161"
    @eval_fn
    def C179():
        b161_1 = Input_EIA_Crude_Europe_Brent.B161()
        return b161_1

@register(Crude_Oil_Prices)
class A180():
    # 'Crude_Oil_Prices'!A180
    value = 36753
    isdatetime = True

@register(Crude_Oil_Prices)
class B180():
    # 'Crude_Oil_Prices'!B180
    value = 31.26
    formula = "='Input EIA Crude WTI'!B178"
    @eval_fn
    def B180():
        b178_1 = Input_EIA_Crude_WTI.B178()
        return b178_1

@register(Crude_Oil_Prices)
class C180():
    # 'Crude_Oil_Prices'!C180
    value = 30.2
    formula = "='Input EIA Crude Europe Brent'!B162"
    @eval_fn
    def C180():
        b162_1 = Input_EIA_Crude_Europe_Brent.B162()
        return b162_1

@register(Crude_Oil_Prices)
class A181():
    # 'Crude_Oil_Prices'!A181
    value = 36784
    isdatetime = True

@register(Crude_Oil_Prices)
class B181():
    # 'Crude_Oil_Prices'!B181
    value = 33.88
    formula = "='Input EIA Crude WTI'!B179"
    @eval_fn
    def B181():
        b179_1 = Input_EIA_Crude_WTI.B179()
        return b179_1

@register(Crude_Oil_Prices)
class C181():
    # 'Crude_Oil_Prices'!C181
    value = 33.14
    formula = "='Input EIA Crude Europe Brent'!B163"
    @eval_fn
    def C181():
        b163_1 = Input_EIA_Crude_Europe_Brent.B163()
        return b163_1

@register(Crude_Oil_Prices)
class A182():
    # 'Crude_Oil_Prices'!A182
    value = 36814
    isdatetime = True

@register(Crude_Oil_Prices)
class B182():
    # 'Crude_Oil_Prices'!B182
    value = 33.11
    formula = "='Input EIA Crude WTI'!B180"
    @eval_fn
    def B182():
        b180_1 = Input_EIA_Crude_WTI.B180()
        return b180_1

@register(Crude_Oil_Prices)
class C182():
    # 'Crude_Oil_Prices'!C182
    value = 30.96
    formula = "='Input EIA Crude Europe Brent'!B164"
    @eval_fn
    def C182():
        b164_1 = Input_EIA_Crude_Europe_Brent.B164()
        return b164_1

@register(Crude_Oil_Prices)
class A183():
    # 'Crude_Oil_Prices'!A183
    value = 36845
    isdatetime = True

@register(Crude_Oil_Prices)
class B183():
    # 'Crude_Oil_Prices'!B183
    value = 34.42
    formula = "='Input EIA Crude WTI'!B181"
    @eval_fn
    def B183():
        b181_1 = Input_EIA_Crude_WTI.B181()
        return b181_1

@register(Crude_Oil_Prices)
class C183():
    # 'Crude_Oil_Prices'!C183
    value = 32.55
    formula = "='Input EIA Crude Europe Brent'!B165"
    @eval_fn
    def C183():
        b165_1 = Input_EIA_Crude_Europe_Brent.B165()
        return b165_1

@register(Crude_Oil_Prices)
class A184():
    # 'Crude_Oil_Prices'!A184
    value = 36875
    isdatetime = True

@register(Crude_Oil_Prices)
class B184():
    # 'Crude_Oil_Prices'!B184
    value = 28.44
    formula = "='Input EIA Crude WTI'!B182"
    @eval_fn
    def B184():
        b182_1 = Input_EIA_Crude_WTI.B182()
        return b182_1

@register(Crude_Oil_Prices)
class C184():
    # 'Crude_Oil_Prices'!C184
    value = 25.66
    formula = "='Input EIA Crude Europe Brent'!B166"
    @eval_fn
    def C184():
        b166_1 = Input_EIA_Crude_Europe_Brent.B166()
        return b166_1

@register(Crude_Oil_Prices)
class A185():
    # 'Crude_Oil_Prices'!A185
    value = 36906
    isdatetime = True

@register(Crude_Oil_Prices)
class B185():
    # 'Crude_Oil_Prices'!B185
    value = 29.59
    formula = "='Input EIA Crude WTI'!B183"
    @eval_fn
    def B185():
        b183_1 = Input_EIA_Crude_WTI.B183()
        return b183_1

@register(Crude_Oil_Prices)
class C185():
    # 'Crude_Oil_Prices'!C185
    value = 25.62
    formula = "='Input EIA Crude Europe Brent'!B167"
    @eval_fn
    def C185():
        b167_1 = Input_EIA_Crude_Europe_Brent.B167()
        return b167_1

@register(Crude_Oil_Prices)
class A186():
    # 'Crude_Oil_Prices'!A186
    value = 36937
    isdatetime = True

@register(Crude_Oil_Prices)
class B186():
    # 'Crude_Oil_Prices'!B186
    value = 29.61
    formula = "='Input EIA Crude WTI'!B184"
    @eval_fn
    def B186():
        b184_1 = Input_EIA_Crude_WTI.B184()
        return b184_1

@register(Crude_Oil_Prices)
class C186():
    # 'Crude_Oil_Prices'!C186
    value = 27.5
    formula = "='Input EIA Crude Europe Brent'!B168"
    @eval_fn
    def C186():
        b168_1 = Input_EIA_Crude_Europe_Brent.B168()
        return b168_1

@register(Crude_Oil_Prices)
class A187():
    # 'Crude_Oil_Prices'!A187
    value = 36965
    isdatetime = True

@register(Crude_Oil_Prices)
class B187():
    # 'Crude_Oil_Prices'!B187
    value = 27.25
    formula = "='Input EIA Crude WTI'!B185"
    @eval_fn
    def B187():
        b185_1 = Input_EIA_Crude_WTI.B185()
        return b185_1

@register(Crude_Oil_Prices)
class C187():
    # 'Crude_Oil_Prices'!C187
    value = 24.5
    formula = "='Input EIA Crude Europe Brent'!B169"
    @eval_fn
    def C187():
        b169_1 = Input_EIA_Crude_Europe_Brent.B169()
        return b169_1

@register(Crude_Oil_Prices)
class A188():
    # 'Crude_Oil_Prices'!A188
    value = 36996
    isdatetime = True

@register(Crude_Oil_Prices)
class B188():
    # 'Crude_Oil_Prices'!B188
    value = 27.49
    formula = "='Input EIA Crude WTI'!B186"
    @eval_fn
    def B188():
        b186_1 = Input_EIA_Crude_WTI.B186()
        return b186_1

@register(Crude_Oil_Prices)
class C188():
    # 'Crude_Oil_Prices'!C188
    value = 25.66
    formula = "='Input EIA Crude Europe Brent'!B170"
    @eval_fn
    def C188():
        b170_1 = Input_EIA_Crude_Europe_Brent.B170()
        return b170_1

@register(Crude_Oil_Prices)
class A189():
    # 'Crude_Oil_Prices'!A189
    value = 37026
    isdatetime = True

@register(Crude_Oil_Prices)
class B189():
    # 'Crude_Oil_Prices'!B189
    value = 28.63
    formula = "='Input EIA Crude WTI'!B187"
    @eval_fn
    def B189():
        b187_1 = Input_EIA_Crude_WTI.B187()
        return b187_1

@register(Crude_Oil_Prices)
class C189():
    # 'Crude_Oil_Prices'!C189
    value = 28.31
    formula = "='Input EIA Crude Europe Brent'!B171"
    @eval_fn
    def C189():
        b171_1 = Input_EIA_Crude_Europe_Brent.B171()
        return b171_1

@register(Crude_Oil_Prices)
class A190():
    # 'Crude_Oil_Prices'!A190
    value = 37057
    isdatetime = True

@register(Crude_Oil_Prices)
class B190():
    # 'Crude_Oil_Prices'!B190
    value = 27.6
    formula = "='Input EIA Crude WTI'!B188"
    @eval_fn
    def B190():
        b188_1 = Input_EIA_Crude_WTI.B188()
        return b188_1

@register(Crude_Oil_Prices)
class C190():
    # 'Crude_Oil_Prices'!C190
    value = 27.85
    formula = "='Input EIA Crude Europe Brent'!B172"
    @eval_fn
    def C190():
        b172_1 = Input_EIA_Crude_Europe_Brent.B172()
        return b172_1

@register(Crude_Oil_Prices)
class A191():
    # 'Crude_Oil_Prices'!A191
    value = 37087
    isdatetime = True

@register(Crude_Oil_Prices)
class B191():
    # 'Crude_Oil_Prices'!B191
    value = 26.43
    formula = "='Input EIA Crude WTI'!B189"
    @eval_fn
    def B191():
        b189_1 = Input_EIA_Crude_WTI.B189()
        return b189_1

@register(Crude_Oil_Prices)
class C191():
    # 'Crude_Oil_Prices'!C191
    value = 24.61
    formula = "='Input EIA Crude Europe Brent'!B173"
    @eval_fn
    def C191():
        b173_1 = Input_EIA_Crude_Europe_Brent.B173()
        return b173_1

@register(Crude_Oil_Prices)
class A192():
    # 'Crude_Oil_Prices'!A192
    value = 37118
    isdatetime = True

@register(Crude_Oil_Prices)
class B192():
    # 'Crude_Oil_Prices'!B192
    value = 27.37
    formula = "='Input EIA Crude WTI'!B190"
    @eval_fn
    def B192():
        b190_1 = Input_EIA_Crude_WTI.B190()
        return b190_1

@register(Crude_Oil_Prices)
class C192():
    # 'Crude_Oil_Prices'!C192
    value = 25.68
    formula = "='Input EIA Crude Europe Brent'!B174"
    @eval_fn
    def C192():
        b174_1 = Input_EIA_Crude_Europe_Brent.B174()
        return b174_1

@register(Crude_Oil_Prices)
class A193():
    # 'Crude_Oil_Prices'!A193
    value = 37149
    isdatetime = True

@register(Crude_Oil_Prices)
class B193():
    # 'Crude_Oil_Prices'!B193
    value = 26.2
    formula = "='Input EIA Crude WTI'!B191"
    @eval_fn
    def B193():
        b191_1 = Input_EIA_Crude_WTI.B191()
        return b191_1

@register(Crude_Oil_Prices)
class C193():
    # 'Crude_Oil_Prices'!C193
    value = 25.62
    formula = "='Input EIA Crude Europe Brent'!B175"
    @eval_fn
    def C193():
        b175_1 = Input_EIA_Crude_Europe_Brent.B175()
        return b175_1

@register(Crude_Oil_Prices)
class A194():
    # 'Crude_Oil_Prices'!A194
    value = 37179
    isdatetime = True

@register(Crude_Oil_Prices)
class B194():
    # 'Crude_Oil_Prices'!B194
    value = 22.17
    formula = "='Input EIA Crude WTI'!B192"
    @eval_fn
    def B194():
        b192_1 = Input_EIA_Crude_WTI.B192()
        return b192_1

@register(Crude_Oil_Prices)
class C194():
    # 'Crude_Oil_Prices'!C194
    value = 20.54
    formula = "='Input EIA Crude Europe Brent'!B176"
    @eval_fn
    def C194():
        b176_1 = Input_EIA_Crude_Europe_Brent.B176()
        return b176_1

@register(Crude_Oil_Prices)
class A195():
    # 'Crude_Oil_Prices'!A195
    value = 37210
    isdatetime = True

@register(Crude_Oil_Prices)
class B195():
    # 'Crude_Oil_Prices'!B195
    value = 19.64
    formula = "='Input EIA Crude WTI'!B193"
    @eval_fn
    def B195():
        b193_1 = Input_EIA_Crude_WTI.B193()
        return b193_1

@register(Crude_Oil_Prices)
class C195():
    # 'Crude_Oil_Prices'!C195
    value = 18.8
    formula = "='Input EIA Crude Europe Brent'!B177"
    @eval_fn
    def C195():
        b177_1 = Input_EIA_Crude_Europe_Brent.B177()
        return b177_1

@register(Crude_Oil_Prices)
class A196():
    # 'Crude_Oil_Prices'!A196
    value = 37240
    isdatetime = True

@register(Crude_Oil_Prices)
class B196():
    # 'Crude_Oil_Prices'!B196
    value = 19.39
    formula = "='Input EIA Crude WTI'!B194"
    @eval_fn
    def B196():
        b194_1 = Input_EIA_Crude_WTI.B194()
        return b194_1

@register(Crude_Oil_Prices)
class C196():
    # 'Crude_Oil_Prices'!C196
    value = 18.71
    formula = "='Input EIA Crude Europe Brent'!B178"
    @eval_fn
    def C196():
        b178_1 = Input_EIA_Crude_Europe_Brent.B178()
        return b178_1

@register(Crude_Oil_Prices)
class A197():
    # 'Crude_Oil_Prices'!A197
    value = 37271
    isdatetime = True

@register(Crude_Oil_Prices)
class B197():
    # 'Crude_Oil_Prices'!B197
    value = 19.72
    formula = "='Input EIA Crude WTI'!B195"
    @eval_fn
    def B197():
        b195_1 = Input_EIA_Crude_WTI.B195()
        return b195_1

@register(Crude_Oil_Prices)
class C197():
    # 'Crude_Oil_Prices'!C197
    value = 19.42
    formula = "='Input EIA Crude Europe Brent'!B179"
    @eval_fn
    def C197():
        b179_1 = Input_EIA_Crude_Europe_Brent.B179()
        return b179_1

@register(Crude_Oil_Prices)
class A198():
    # 'Crude_Oil_Prices'!A198
    value = 37302
    isdatetime = True

@register(Crude_Oil_Prices)
class B198():
    # 'Crude_Oil_Prices'!B198
    value = 20.72
    formula = "='Input EIA Crude WTI'!B196"
    @eval_fn
    def B198():
        b196_1 = Input_EIA_Crude_WTI.B196()
        return b196_1

@register(Crude_Oil_Prices)
class C198():
    # 'Crude_Oil_Prices'!C198
    value = 20.28
    formula = "='Input EIA Crude Europe Brent'!B180"
    @eval_fn
    def C198():
        b180_1 = Input_EIA_Crude_Europe_Brent.B180()
        return b180_1

@register(Crude_Oil_Prices)
class A199():
    # 'Crude_Oil_Prices'!A199
    value = 37330
    isdatetime = True

@register(Crude_Oil_Prices)
class B199():
    # 'Crude_Oil_Prices'!B199
    value = 24.53
    formula = "='Input EIA Crude WTI'!B197"
    @eval_fn
    def B199():
        b197_1 = Input_EIA_Crude_WTI.B197()
        return b197_1

@register(Crude_Oil_Prices)
class C199():
    # 'Crude_Oil_Prices'!C199
    value = 23.7
    formula = "='Input EIA Crude Europe Brent'!B181"
    @eval_fn
    def C199():
        b181_1 = Input_EIA_Crude_Europe_Brent.B181()
        return b181_1

@register(Crude_Oil_Prices)
class A200():
    # 'Crude_Oil_Prices'!A200
    value = 37361
    isdatetime = True

@register(Crude_Oil_Prices)
class B200():
    # 'Crude_Oil_Prices'!B200
    value = 26.18
    formula = "='Input EIA Crude WTI'!B198"
    @eval_fn
    def B200():
        b198_1 = Input_EIA_Crude_WTI.B198()
        return b198_1

@register(Crude_Oil_Prices)
class C200():
    # 'Crude_Oil_Prices'!C200
    value = 25.73
    formula = "='Input EIA Crude Europe Brent'!B182"
    @eval_fn
    def C200():
        b182_1 = Input_EIA_Crude_Europe_Brent.B182()
        return b182_1

@register(Crude_Oil_Prices)
class A201():
    # 'Crude_Oil_Prices'!A201
    value = 37391
    isdatetime = True

@register(Crude_Oil_Prices)
class B201():
    # 'Crude_Oil_Prices'!B201
    value = 27.04
    formula = "='Input EIA Crude WTI'!B199"
    @eval_fn
    def B201():
        b199_1 = Input_EIA_Crude_WTI.B199()
        return b199_1

@register(Crude_Oil_Prices)
class C201():
    # 'Crude_Oil_Prices'!C201
    value = 25.35
    formula = "='Input EIA Crude Europe Brent'!B183"
    @eval_fn
    def C201():
        b183_1 = Input_EIA_Crude_Europe_Brent.B183()
        return b183_1

@register(Crude_Oil_Prices)
class A202():
    # 'Crude_Oil_Prices'!A202
    value = 37422
    isdatetime = True

@register(Crude_Oil_Prices)
class B202():
    # 'Crude_Oil_Prices'!B202
    value = 25.52
    formula = "='Input EIA Crude WTI'!B200"
    @eval_fn
    def B202():
        b200_1 = Input_EIA_Crude_WTI.B200()
        return b200_1

@register(Crude_Oil_Prices)
class C202():
    # 'Crude_Oil_Prices'!C202
    value = 24.08
    formula = "='Input EIA Crude Europe Brent'!B184"
    @eval_fn
    def C202():
        b184_1 = Input_EIA_Crude_Europe_Brent.B184()
        return b184_1

@register(Crude_Oil_Prices)
class A203():
    # 'Crude_Oil_Prices'!A203
    value = 37452
    isdatetime = True

@register(Crude_Oil_Prices)
class B203():
    # 'Crude_Oil_Prices'!B203
    value = 26.97
    formula = "='Input EIA Crude WTI'!B201"
    @eval_fn
    def B203():
        b201_1 = Input_EIA_Crude_WTI.B201()
        return b201_1

@register(Crude_Oil_Prices)
class C203():
    # 'Crude_Oil_Prices'!C203
    value = 25.74
    formula = "='Input EIA Crude Europe Brent'!B185"
    @eval_fn
    def C203():
        b185_1 = Input_EIA_Crude_Europe_Brent.B185()
        return b185_1

@register(Crude_Oil_Prices)
class A204():
    # 'Crude_Oil_Prices'!A204
    value = 37483
    isdatetime = True

@register(Crude_Oil_Prices)
class B204():
    # 'Crude_Oil_Prices'!B204
    value = 28.39
    formula = "='Input EIA Crude WTI'!B202"
    @eval_fn
    def B204():
        b202_1 = Input_EIA_Crude_WTI.B202()
        return b202_1

@register(Crude_Oil_Prices)
class C204():
    # 'Crude_Oil_Prices'!C204
    value = 26.65
    formula = "='Input EIA Crude Europe Brent'!B186"
    @eval_fn
    def C204():
        b186_1 = Input_EIA_Crude_Europe_Brent.B186()
        return b186_1

@register(Crude_Oil_Prices)
class A205():
    # 'Crude_Oil_Prices'!A205
    value = 37514
    isdatetime = True

@register(Crude_Oil_Prices)
class B205():
    # 'Crude_Oil_Prices'!B205
    value = 29.66
    formula = "='Input EIA Crude WTI'!B203"
    @eval_fn
    def B205():
        b203_1 = Input_EIA_Crude_WTI.B203()
        return b203_1

@register(Crude_Oil_Prices)
class C205():
    # 'Crude_Oil_Prices'!C205
    value = 28.4
    formula = "='Input EIA Crude Europe Brent'!B187"
    @eval_fn
    def C205():
        b187_1 = Input_EIA_Crude_Europe_Brent.B187()
        return b187_1

@register(Crude_Oil_Prices)
class A206():
    # 'Crude_Oil_Prices'!A206
    value = 37544
    isdatetime = True

@register(Crude_Oil_Prices)
class B206():
    # 'Crude_Oil_Prices'!B206
    value = 28.84
    formula = "='Input EIA Crude WTI'!B204"
    @eval_fn
    def B206():
        b204_1 = Input_EIA_Crude_WTI.B204()
        return b204_1

@register(Crude_Oil_Prices)
class C206():
    # 'Crude_Oil_Prices'!C206
    value = 27.54
    formula = "='Input EIA Crude Europe Brent'!B188"
    @eval_fn
    def C206():
        b188_1 = Input_EIA_Crude_Europe_Brent.B188()
        return b188_1

@register(Crude_Oil_Prices)
class A207():
    # 'Crude_Oil_Prices'!A207
    value = 37575
    isdatetime = True

@register(Crude_Oil_Prices)
class B207():
    # 'Crude_Oil_Prices'!B207
    value = 26.35
    formula = "='Input EIA Crude WTI'!B205"
    @eval_fn
    def B207():
        b205_1 = Input_EIA_Crude_WTI.B205()
        return b205_1

@register(Crude_Oil_Prices)
class C207():
    # 'Crude_Oil_Prices'!C207
    value = 24.34
    formula = "='Input EIA Crude Europe Brent'!B189"
    @eval_fn
    def C207():
        b189_1 = Input_EIA_Crude_Europe_Brent.B189()
        return b189_1

@register(Crude_Oil_Prices)
class A208():
    # 'Crude_Oil_Prices'!A208
    value = 37605
    isdatetime = True

@register(Crude_Oil_Prices)
class B208():
    # 'Crude_Oil_Prices'!B208
    value = 29.46
    formula = "='Input EIA Crude WTI'!B206"
    @eval_fn
    def B208():
        b206_1 = Input_EIA_Crude_WTI.B206()
        return b206_1

@register(Crude_Oil_Prices)
class C208():
    # 'Crude_Oil_Prices'!C208
    value = 28.33
    formula = "='Input EIA Crude Europe Brent'!B190"
    @eval_fn
    def C208():
        b190_1 = Input_EIA_Crude_Europe_Brent.B190()
        return b190_1

@register(Crude_Oil_Prices)
class A209():
    # 'Crude_Oil_Prices'!A209
    value = 37636
    isdatetime = True

@register(Crude_Oil_Prices)
class B209():
    # 'Crude_Oil_Prices'!B209
    value = 32.95
    formula = "='Input EIA Crude WTI'!B207"
    @eval_fn
    def B209():
        b207_1 = Input_EIA_Crude_WTI.B207()
        return b207_1

@register(Crude_Oil_Prices)
class C209():
    # 'Crude_Oil_Prices'!C209
    value = 31.18
    formula = "='Input EIA Crude Europe Brent'!B191"
    @eval_fn
    def C209():
        b191_1 = Input_EIA_Crude_Europe_Brent.B191()
        return b191_1

@register(Crude_Oil_Prices)
class A210():
    # 'Crude_Oil_Prices'!A210
    value = 37667
    isdatetime = True

@register(Crude_Oil_Prices)
class B210():
    # 'Crude_Oil_Prices'!B210
    value = 35.83
    formula = "='Input EIA Crude WTI'!B208"
    @eval_fn
    def B210():
        b208_1 = Input_EIA_Crude_WTI.B208()
        return b208_1

@register(Crude_Oil_Prices)
class C210():
    # 'Crude_Oil_Prices'!C210
    value = 32.77
    formula = "='Input EIA Crude Europe Brent'!B192"
    @eval_fn
    def C210():
        b192_1 = Input_EIA_Crude_Europe_Brent.B192()
        return b192_1

@register(Crude_Oil_Prices)
class A211():
    # 'Crude_Oil_Prices'!A211
    value = 37695
    isdatetime = True

@register(Crude_Oil_Prices)
class B211():
    # 'Crude_Oil_Prices'!B211
    value = 33.51
    formula = "='Input EIA Crude WTI'!B209"
    @eval_fn
    def B211():
        b209_1 = Input_EIA_Crude_WTI.B209()
        return b209_1

@register(Crude_Oil_Prices)
class C211():
    # 'Crude_Oil_Prices'!C211
    value = 30.61
    formula = "='Input EIA Crude Europe Brent'!B193"
    @eval_fn
    def C211():
        b193_1 = Input_EIA_Crude_Europe_Brent.B193()
        return b193_1

@register(Crude_Oil_Prices)
class A212():
    # 'Crude_Oil_Prices'!A212
    value = 37726
    isdatetime = True

@register(Crude_Oil_Prices)
class B212():
    # 'Crude_Oil_Prices'!B212
    value = 28.17
    formula = "='Input EIA Crude WTI'!B210"
    @eval_fn
    def B212():
        b210_1 = Input_EIA_Crude_WTI.B210()
        return b210_1

@register(Crude_Oil_Prices)
class C212():
    # 'Crude_Oil_Prices'!C212
    value = 25
    formula = "='Input EIA Crude Europe Brent'!B194"
    @eval_fn
    def C212():
        b194_1 = Input_EIA_Crude_Europe_Brent.B194()
        return b194_1

@register(Crude_Oil_Prices)
class A213():
    # 'Crude_Oil_Prices'!A213
    value = 37756
    isdatetime = True

@register(Crude_Oil_Prices)
class B213():
    # 'Crude_Oil_Prices'!B213
    value = 28.11
    formula = "='Input EIA Crude WTI'!B211"
    @eval_fn
    def B213():
        b211_1 = Input_EIA_Crude_WTI.B211()
        return b211_1

@register(Crude_Oil_Prices)
class C213():
    # 'Crude_Oil_Prices'!C213
    value = 25.86
    formula = "='Input EIA Crude Europe Brent'!B195"
    @eval_fn
    def C213():
        b195_1 = Input_EIA_Crude_Europe_Brent.B195()
        return b195_1

@register(Crude_Oil_Prices)
class A214():
    # 'Crude_Oil_Prices'!A214
    value = 37787
    isdatetime = True

@register(Crude_Oil_Prices)
class B214():
    # 'Crude_Oil_Prices'!B214
    value = 30.66
    formula = "='Input EIA Crude WTI'!B212"
    @eval_fn
    def B214():
        b212_1 = Input_EIA_Crude_WTI.B212()
        return b212_1

@register(Crude_Oil_Prices)
class C214():
    # 'Crude_Oil_Prices'!C214
    value = 27.65
    formula = "='Input EIA Crude Europe Brent'!B196"
    @eval_fn
    def C214():
        b196_1 = Input_EIA_Crude_Europe_Brent.B196()
        return b196_1

@register(Crude_Oil_Prices)
class A215():
    # 'Crude_Oil_Prices'!A215
    value = 37817
    isdatetime = True

@register(Crude_Oil_Prices)
class B215():
    # 'Crude_Oil_Prices'!B215
    value = 30.76
    formula = "='Input EIA Crude WTI'!B213"
    @eval_fn
    def B215():
        b213_1 = Input_EIA_Crude_WTI.B213()
        return b213_1

@register(Crude_Oil_Prices)
class C215():
    # 'Crude_Oil_Prices'!C215
    value = 28.35
    formula = "='Input EIA Crude Europe Brent'!B197"
    @eval_fn
    def C215():
        b197_1 = Input_EIA_Crude_Europe_Brent.B197()
        return b197_1

@register(Crude_Oil_Prices)
class A216():
    # 'Crude_Oil_Prices'!A216
    value = 37848
    isdatetime = True

@register(Crude_Oil_Prices)
class B216():
    # 'Crude_Oil_Prices'!B216
    value = 31.57
    formula = "='Input EIA Crude WTI'!B214"
    @eval_fn
    def B216():
        b214_1 = Input_EIA_Crude_WTI.B214()
        return b214_1

@register(Crude_Oil_Prices)
class C216():
    # 'Crude_Oil_Prices'!C216
    value = 29.89
    formula = "='Input EIA Crude Europe Brent'!B198"
    @eval_fn
    def C216():
        b198_1 = Input_EIA_Crude_Europe_Brent.B198()
        return b198_1

@register(Crude_Oil_Prices)
class A217():
    # 'Crude_Oil_Prices'!A217
    value = 37879
    isdatetime = True

@register(Crude_Oil_Prices)
class B217():
    # 'Crude_Oil_Prices'!B217
    value = 28.31
    formula = "='Input EIA Crude WTI'!B215"
    @eval_fn
    def B217():
        b215_1 = Input_EIA_Crude_WTI.B215()
        return b215_1

@register(Crude_Oil_Prices)
class C217():
    # 'Crude_Oil_Prices'!C217
    value = 27.11
    formula = "='Input EIA Crude Europe Brent'!B199"
    @eval_fn
    def C217():
        b199_1 = Input_EIA_Crude_Europe_Brent.B199()
        return b199_1

@register(Crude_Oil_Prices)
class A218():
    # 'Crude_Oil_Prices'!A218
    value = 37909
    isdatetime = True

@register(Crude_Oil_Prices)
class B218():
    # 'Crude_Oil_Prices'!B218
    value = 30.34
    formula = "='Input EIA Crude WTI'!B216"
    @eval_fn
    def B218():
        b216_1 = Input_EIA_Crude_WTI.B216()
        return b216_1

@register(Crude_Oil_Prices)
class C218():
    # 'Crude_Oil_Prices'!C218
    value = 29.61
    formula = "='Input EIA Crude Europe Brent'!B200"
    @eval_fn
    def C218():
        b200_1 = Input_EIA_Crude_Europe_Brent.B200()
        return b200_1

@register(Crude_Oil_Prices)
class A219():
    # 'Crude_Oil_Prices'!A219
    value = 37940
    isdatetime = True

@register(Crude_Oil_Prices)
class B219():
    # 'Crude_Oil_Prices'!B219
    value = 31.11
    formula = "='Input EIA Crude WTI'!B217"
    @eval_fn
    def B219():
        b217_1 = Input_EIA_Crude_WTI.B217()
        return b217_1

@register(Crude_Oil_Prices)
class C219():
    # 'Crude_Oil_Prices'!C219
    value = 28.75
    formula = "='Input EIA Crude Europe Brent'!B201"
    @eval_fn
    def C219():
        b201_1 = Input_EIA_Crude_Europe_Brent.B201()
        return b201_1

@register(Crude_Oil_Prices)
class A220():
    # 'Crude_Oil_Prices'!A220
    value = 37970
    isdatetime = True

@register(Crude_Oil_Prices)
class B220():
    # 'Crude_Oil_Prices'!B220
    value = 32.13
    formula = "='Input EIA Crude WTI'!B218"
    @eval_fn
    def B220():
        b218_1 = Input_EIA_Crude_WTI.B218()
        return b218_1

@register(Crude_Oil_Prices)
class C220():
    # 'Crude_Oil_Prices'!C220
    value = 29.81
    formula = "='Input EIA Crude Europe Brent'!B202"
    @eval_fn
    def C220():
        b202_1 = Input_EIA_Crude_Europe_Brent.B202()
        return b202_1

@register(Crude_Oil_Prices)
class A221():
    # 'Crude_Oil_Prices'!A221
    value = 38001
    isdatetime = True

@register(Crude_Oil_Prices)
class B221():
    # 'Crude_Oil_Prices'!B221
    value = 34.31
    formula = "='Input EIA Crude WTI'!B219"
    @eval_fn
    def B221():
        b219_1 = Input_EIA_Crude_WTI.B219()
        return b219_1

@register(Crude_Oil_Prices)
class C221():
    # 'Crude_Oil_Prices'!C221
    value = 31.28
    formula = "='Input EIA Crude Europe Brent'!B203"
    @eval_fn
    def C221():
        b203_1 = Input_EIA_Crude_Europe_Brent.B203()
        return b203_1

@register(Crude_Oil_Prices)
class A222():
    # 'Crude_Oil_Prices'!A222
    value = 38032
    isdatetime = True

@register(Crude_Oil_Prices)
class B222():
    # 'Crude_Oil_Prices'!B222
    value = 34.69
    formula = "='Input EIA Crude WTI'!B220"
    @eval_fn
    def B222():
        b220_1 = Input_EIA_Crude_WTI.B220()
        return b220_1

@register(Crude_Oil_Prices)
class C222():
    # 'Crude_Oil_Prices'!C222
    value = 30.86
    formula = "='Input EIA Crude Europe Brent'!B204"
    @eval_fn
    def C222():
        b204_1 = Input_EIA_Crude_Europe_Brent.B204()
        return b204_1

@register(Crude_Oil_Prices)
class A223():
    # 'Crude_Oil_Prices'!A223
    value = 38061
    isdatetime = True

@register(Crude_Oil_Prices)
class B223():
    # 'Crude_Oil_Prices'!B223
    value = 36.74
    formula = "='Input EIA Crude WTI'!B221"
    @eval_fn
    def B223():
        b221_1 = Input_EIA_Crude_WTI.B221()
        return b221_1

@register(Crude_Oil_Prices)
class C223():
    # 'Crude_Oil_Prices'!C223
    value = 33.63
    formula = "='Input EIA Crude Europe Brent'!B205"
    @eval_fn
    def C223():
        b205_1 = Input_EIA_Crude_Europe_Brent.B205()
        return b205_1

@register(Crude_Oil_Prices)
class A224():
    # 'Crude_Oil_Prices'!A224
    value = 38092
    isdatetime = True

@register(Crude_Oil_Prices)
class B224():
    # 'Crude_Oil_Prices'!B224
    value = 36.75
    formula = "='Input EIA Crude WTI'!B222"
    @eval_fn
    def B224():
        b222_1 = Input_EIA_Crude_WTI.B222()
        return b222_1

@register(Crude_Oil_Prices)
class C224():
    # 'Crude_Oil_Prices'!C224
    value = 33.59
    formula = "='Input EIA Crude Europe Brent'!B206"
    @eval_fn
    def C224():
        b206_1 = Input_EIA_Crude_Europe_Brent.B206()
        return b206_1

@register(Crude_Oil_Prices)
class A225():
    # 'Crude_Oil_Prices'!A225
    value = 38122
    isdatetime = True

@register(Crude_Oil_Prices)
class B225():
    # 'Crude_Oil_Prices'!B225
    value = 40.28
    formula = "='Input EIA Crude WTI'!B223"
    @eval_fn
    def B225():
        b223_1 = Input_EIA_Crude_WTI.B223()
        return b223_1

@register(Crude_Oil_Prices)
class C225():
    # 'Crude_Oil_Prices'!C225
    value = 37.57
    formula = "='Input EIA Crude Europe Brent'!B207"
    @eval_fn
    def C225():
        b207_1 = Input_EIA_Crude_Europe_Brent.B207()
        return b207_1

@register(Crude_Oil_Prices)
class A226():
    # 'Crude_Oil_Prices'!A226
    value = 38153
    isdatetime = True

@register(Crude_Oil_Prices)
class B226():
    # 'Crude_Oil_Prices'!B226
    value = 38.03
    formula = "='Input EIA Crude WTI'!B224"
    @eval_fn
    def B226():
        b224_1 = Input_EIA_Crude_WTI.B224()
        return b224_1

@register(Crude_Oil_Prices)
class C226():
    # 'Crude_Oil_Prices'!C226
    value = 35.18
    formula = "='Input EIA Crude Europe Brent'!B208"
    @eval_fn
    def C226():
        b208_1 = Input_EIA_Crude_Europe_Brent.B208()
        return b208_1

@register(Crude_Oil_Prices)
class A227():
    # 'Crude_Oil_Prices'!A227
    value = 38183
    isdatetime = True

@register(Crude_Oil_Prices)
class B227():
    # 'Crude_Oil_Prices'!B227
    value = 40.78
    formula = "='Input EIA Crude WTI'!B225"
    @eval_fn
    def B227():
        b225_1 = Input_EIA_Crude_WTI.B225()
        return b225_1

@register(Crude_Oil_Prices)
class C227():
    # 'Crude_Oil_Prices'!C227
    value = 38.22
    formula = "='Input EIA Crude Europe Brent'!B209"
    @eval_fn
    def C227():
        b209_1 = Input_EIA_Crude_Europe_Brent.B209()
        return b209_1

@register(Crude_Oil_Prices)
class A228():
    # 'Crude_Oil_Prices'!A228
    value = 38214
    isdatetime = True

@register(Crude_Oil_Prices)
class B228():
    # 'Crude_Oil_Prices'!B228
    value = 44.9
    formula = "='Input EIA Crude WTI'!B226"
    @eval_fn
    def B228():
        b226_1 = Input_EIA_Crude_WTI.B226()
        return b226_1

@register(Crude_Oil_Prices)
class C228():
    # 'Crude_Oil_Prices'!C228
    value = 42.74
    formula = "='Input EIA Crude Europe Brent'!B210"
    @eval_fn
    def C228():
        b210_1 = Input_EIA_Crude_Europe_Brent.B210()
        return b210_1

@register(Crude_Oil_Prices)
class A229():
    # 'Crude_Oil_Prices'!A229
    value = 38245
    isdatetime = True

@register(Crude_Oil_Prices)
class B229():
    # 'Crude_Oil_Prices'!B229
    value = 45.94
    formula = "='Input EIA Crude WTI'!B227"
    @eval_fn
    def B229():
        b227_1 = Input_EIA_Crude_WTI.B227()
        return b227_1

@register(Crude_Oil_Prices)
class C229():
    # 'Crude_Oil_Prices'!C229
    value = 43.2
    formula = "='Input EIA Crude Europe Brent'!B211"
    @eval_fn
    def C229():
        b211_1 = Input_EIA_Crude_Europe_Brent.B211()
        return b211_1

@register(Crude_Oil_Prices)
class A230():
    # 'Crude_Oil_Prices'!A230
    value = 38275
    isdatetime = True

@register(Crude_Oil_Prices)
class B230():
    # 'Crude_Oil_Prices'!B230
    value = 53.28
    formula = "='Input EIA Crude WTI'!B228"
    @eval_fn
    def B230():
        b228_1 = Input_EIA_Crude_WTI.B228()
        return b228_1

@register(Crude_Oil_Prices)
class C230():
    # 'Crude_Oil_Prices'!C230
    value = 49.78
    formula = "='Input EIA Crude Europe Brent'!B212"
    @eval_fn
    def C230():
        b212_1 = Input_EIA_Crude_Europe_Brent.B212()
        return b212_1

@register(Crude_Oil_Prices)
class A231():
    # 'Crude_Oil_Prices'!A231
    value = 38306
    isdatetime = True

@register(Crude_Oil_Prices)
class B231():
    # 'Crude_Oil_Prices'!B231
    value = 48.47
    formula = "='Input EIA Crude WTI'!B229"
    @eval_fn
    def B231():
        b229_1 = Input_EIA_Crude_WTI.B229()
        return b229_1

@register(Crude_Oil_Prices)
class C231():
    # 'Crude_Oil_Prices'!C231
    value = 43.11
    formula = "='Input EIA Crude Europe Brent'!B213"
    @eval_fn
    def C231():
        b213_1 = Input_EIA_Crude_Europe_Brent.B213()
        return b213_1

@register(Crude_Oil_Prices)
class A232():
    # 'Crude_Oil_Prices'!A232
    value = 38336
    isdatetime = True

@register(Crude_Oil_Prices)
class B232():
    # 'Crude_Oil_Prices'!B232
    value = 43.15
    formula = "='Input EIA Crude WTI'!B230"
    @eval_fn
    def B232():
        b230_1 = Input_EIA_Crude_WTI.B230()
        return b230_1

@register(Crude_Oil_Prices)
class C232():
    # 'Crude_Oil_Prices'!C232
    value = 39.6
    formula = "='Input EIA Crude Europe Brent'!B214"
    @eval_fn
    def C232():
        b214_1 = Input_EIA_Crude_Europe_Brent.B214()
        return b214_1

@register(Crude_Oil_Prices)
class A233():
    # 'Crude_Oil_Prices'!A233
    value = 38367
    isdatetime = True

@register(Crude_Oil_Prices)
class B233():
    # 'Crude_Oil_Prices'!B233
    value = 46.84
    formula = "='Input EIA Crude WTI'!B231"
    @eval_fn
    def B233():
        b231_1 = Input_EIA_Crude_WTI.B231()
        return b231_1

@register(Crude_Oil_Prices)
class C233():
    # 'Crude_Oil_Prices'!C233
    value = 44.51
    formula = "='Input EIA Crude Europe Brent'!B215"
    @eval_fn
    def C233():
        b215_1 = Input_EIA_Crude_Europe_Brent.B215()
        return b215_1

@register(Crude_Oil_Prices)
class A234():
    # 'Crude_Oil_Prices'!A234
    value = 38398
    isdatetime = True

@register(Crude_Oil_Prices)
class B234():
    # 'Crude_Oil_Prices'!B234
    value = 48.15
    formula = "='Input EIA Crude WTI'!B232"
    @eval_fn
    def B234():
        b232_1 = Input_EIA_Crude_WTI.B232()
        return b232_1

@register(Crude_Oil_Prices)
class C234():
    # 'Crude_Oil_Prices'!C234
    value = 45.48
    formula = "='Input EIA Crude Europe Brent'!B216"
    @eval_fn
    def C234():
        b216_1 = Input_EIA_Crude_Europe_Brent.B216()
        return b216_1

@register(Crude_Oil_Prices)
class A235():
    # 'Crude_Oil_Prices'!A235
    value = 38426
    isdatetime = True

@register(Crude_Oil_Prices)
class B235():
    # 'Crude_Oil_Prices'!B235
    value = 54.19
    formula = "='Input EIA Crude WTI'!B233"
    @eval_fn
    def B235():
        b233_1 = Input_EIA_Crude_WTI.B233()
        return b233_1

@register(Crude_Oil_Prices)
class C235():
    # 'Crude_Oil_Prices'!C235
    value = 53.1
    formula = "='Input EIA Crude Europe Brent'!B217"
    @eval_fn
    def C235():
        b217_1 = Input_EIA_Crude_Europe_Brent.B217()
        return b217_1

@register(Crude_Oil_Prices)
class A236():
    # 'Crude_Oil_Prices'!A236
    value = 38457
    isdatetime = True

@register(Crude_Oil_Prices)
class B236():
    # 'Crude_Oil_Prices'!B236
    value = 52.98
    formula = "='Input EIA Crude WTI'!B234"
    @eval_fn
    def B236():
        b234_1 = Input_EIA_Crude_WTI.B234()
        return b234_1

@register(Crude_Oil_Prices)
class C236():
    # 'Crude_Oil_Prices'!C236
    value = 51.88
    formula = "='Input EIA Crude Europe Brent'!B218"
    @eval_fn
    def C236():
        b218_1 = Input_EIA_Crude_Europe_Brent.B218()
        return b218_1

@register(Crude_Oil_Prices)
class A237():
    # 'Crude_Oil_Prices'!A237
    value = 38487
    isdatetime = True

@register(Crude_Oil_Prices)
class B237():
    # 'Crude_Oil_Prices'!B237
    value = 49.83
    formula = "='Input EIA Crude WTI'!B235"
    @eval_fn
    def B237():
        b235_1 = Input_EIA_Crude_WTI.B235()
        return b235_1

@register(Crude_Oil_Prices)
class C237():
    # 'Crude_Oil_Prices'!C237
    value = 48.65
    formula = "='Input EIA Crude Europe Brent'!B219"
    @eval_fn
    def C237():
        b219_1 = Input_EIA_Crude_Europe_Brent.B219()
        return b219_1

@register(Crude_Oil_Prices)
class A238():
    # 'Crude_Oil_Prices'!A238
    value = 38518
    isdatetime = True

@register(Crude_Oil_Prices)
class B238():
    # 'Crude_Oil_Prices'!B238
    value = 56.35
    formula = "='Input EIA Crude WTI'!B236"
    @eval_fn
    def B238():
        b236_1 = Input_EIA_Crude_WTI.B236()
        return b236_1

@register(Crude_Oil_Prices)
class C238():
    # 'Crude_Oil_Prices'!C238
    value = 54.35
    formula = "='Input EIA Crude Europe Brent'!B220"
    @eval_fn
    def C238():
        b220_1 = Input_EIA_Crude_Europe_Brent.B220()
        return b220_1

@register(Crude_Oil_Prices)
class A239():
    # 'Crude_Oil_Prices'!A239
    value = 38548
    isdatetime = True

@register(Crude_Oil_Prices)
class B239():
    # 'Crude_Oil_Prices'!B239
    value = 59
    formula = "='Input EIA Crude WTI'!B237"
    @eval_fn
    def B239():
        b237_1 = Input_EIA_Crude_WTI.B237()
        return b237_1

@register(Crude_Oil_Prices)
class C239():
    # 'Crude_Oil_Prices'!C239
    value = 57.52
    formula = "='Input EIA Crude Europe Brent'!B221"
    @eval_fn
    def C239():
        b221_1 = Input_EIA_Crude_Europe_Brent.B221()
        return b221_1

@register(Crude_Oil_Prices)
class A240():
    # 'Crude_Oil_Prices'!A240
    value = 38579
    isdatetime = True

@register(Crude_Oil_Prices)
class B240():
    # 'Crude_Oil_Prices'!B240
    value = 64.99
    formula = "='Input EIA Crude WTI'!B238"
    @eval_fn
    def B240():
        b238_1 = Input_EIA_Crude_WTI.B238()
        return b238_1

@register(Crude_Oil_Prices)
class C240():
    # 'Crude_Oil_Prices'!C240
    value = 63.98
    formula = "='Input EIA Crude Europe Brent'!B222"
    @eval_fn
    def C240():
        b222_1 = Input_EIA_Crude_Europe_Brent.B222()
        return b222_1

@register(Crude_Oil_Prices)
class A241():
    # 'Crude_Oil_Prices'!A241
    value = 38610
    isdatetime = True

@register(Crude_Oil_Prices)
class B241():
    # 'Crude_Oil_Prices'!B241
    value = 65.59
    formula = "='Input EIA Crude WTI'!B239"
    @eval_fn
    def B241():
        b239_1 = Input_EIA_Crude_WTI.B239()
        return b239_1

@register(Crude_Oil_Prices)
class C241():
    # 'Crude_Oil_Prices'!C241
    value = 62.91
    formula = "='Input EIA Crude Europe Brent'!B223"
    @eval_fn
    def C241():
        b223_1 = Input_EIA_Crude_Europe_Brent.B223()
        return b223_1

@register(Crude_Oil_Prices)
class A242():
    # 'Crude_Oil_Prices'!A242
    value = 38640
    isdatetime = True

@register(Crude_Oil_Prices)
class B242():
    # 'Crude_Oil_Prices'!B242
    value = 62.26
    formula = "='Input EIA Crude WTI'!B240"
    @eval_fn
    def B242():
        b240_1 = Input_EIA_Crude_WTI.B240()
        return b240_1

@register(Crude_Oil_Prices)
class C242():
    # 'Crude_Oil_Prices'!C242
    value = 58.54
    formula = "='Input EIA Crude Europe Brent'!B224"
    @eval_fn
    def C242():
        b224_1 = Input_EIA_Crude_Europe_Brent.B224()
        return b224_1

@register(Crude_Oil_Prices)
class A243():
    # 'Crude_Oil_Prices'!A243
    value = 38671
    isdatetime = True

@register(Crude_Oil_Prices)
class B243():
    # 'Crude_Oil_Prices'!B243
    value = 58.32
    formula = "='Input EIA Crude WTI'!B241"
    @eval_fn
    def B243():
        b241_1 = Input_EIA_Crude_WTI.B241()
        return b241_1

@register(Crude_Oil_Prices)
class C243():
    # 'Crude_Oil_Prices'!C243
    value = 55.24
    formula = "='Input EIA Crude Europe Brent'!B225"
    @eval_fn
    def C243():
        b225_1 = Input_EIA_Crude_Europe_Brent.B225()
        return b225_1

@register(Crude_Oil_Prices)
class A244():
    # 'Crude_Oil_Prices'!A244
    value = 38701
    isdatetime = True

@register(Crude_Oil_Prices)
class B244():
    # 'Crude_Oil_Prices'!B244
    value = 59.41
    formula = "='Input EIA Crude WTI'!B242"
    @eval_fn
    def B244():
        b242_1 = Input_EIA_Crude_WTI.B242()
        return b242_1

@register(Crude_Oil_Prices)
class C244():
    # 'Crude_Oil_Prices'!C244
    value = 56.86
    formula = "='Input EIA Crude Europe Brent'!B226"
    @eval_fn
    def C244():
        b226_1 = Input_EIA_Crude_Europe_Brent.B226()
        return b226_1

@register(Crude_Oil_Prices)
class A245():
    # 'Crude_Oil_Prices'!A245
    value = 38732
    isdatetime = True

@register(Crude_Oil_Prices)
class B245():
    # 'Crude_Oil_Prices'!B245
    value = 65.49
    formula = "='Input EIA Crude WTI'!B243"
    @eval_fn
    def B245():
        b243_1 = Input_EIA_Crude_WTI.B243()
        return b243_1

@register(Crude_Oil_Prices)
class C245():
    # 'Crude_Oil_Prices'!C245
    value = 62.99
    formula = "='Input EIA Crude Europe Brent'!B227"
    @eval_fn
    def C245():
        b227_1 = Input_EIA_Crude_Europe_Brent.B227()
        return b227_1

@register(Crude_Oil_Prices)
class A246():
    # 'Crude_Oil_Prices'!A246
    value = 38763
    isdatetime = True

@register(Crude_Oil_Prices)
class B246():
    # 'Crude_Oil_Prices'!B246
    value = 61.63
    formula = "='Input EIA Crude WTI'!B244"
    @eval_fn
    def B246():
        b244_1 = Input_EIA_Crude_WTI.B244()
        return b244_1

@register(Crude_Oil_Prices)
class C246():
    # 'Crude_Oil_Prices'!C246
    value = 60.21
    formula = "='Input EIA Crude Europe Brent'!B228"
    @eval_fn
    def C246():
        b228_1 = Input_EIA_Crude_Europe_Brent.B228()
        return b228_1

@register(Crude_Oil_Prices)
class A247():
    # 'Crude_Oil_Prices'!A247
    value = 38791
    isdatetime = True

@register(Crude_Oil_Prices)
class B247():
    # 'Crude_Oil_Prices'!B247
    value = 62.69
    formula = "='Input EIA Crude WTI'!B245"
    @eval_fn
    def B247():
        b245_1 = Input_EIA_Crude_WTI.B245()
        return b245_1

@register(Crude_Oil_Prices)
class C247():
    # 'Crude_Oil_Prices'!C247
    value = 62.06
    formula = "='Input EIA Crude Europe Brent'!B229"
    @eval_fn
    def C247():
        b229_1 = Input_EIA_Crude_Europe_Brent.B229()
        return b229_1

@register(Crude_Oil_Prices)
class A248():
    # 'Crude_Oil_Prices'!A248
    value = 38822
    isdatetime = True

@register(Crude_Oil_Prices)
class B248():
    # 'Crude_Oil_Prices'!B248
    value = 69.44
    formula = "='Input EIA Crude WTI'!B246"
    @eval_fn
    def B248():
        b246_1 = Input_EIA_Crude_WTI.B246()
        return b246_1

@register(Crude_Oil_Prices)
class C248():
    # 'Crude_Oil_Prices'!C248
    value = 70.26
    formula = "='Input EIA Crude Europe Brent'!B230"
    @eval_fn
    def C248():
        b230_1 = Input_EIA_Crude_Europe_Brent.B230()
        return b230_1

@register(Crude_Oil_Prices)
class A249():
    # 'Crude_Oil_Prices'!A249
    value = 38852
    isdatetime = True

@register(Crude_Oil_Prices)
class B249():
    # 'Crude_Oil_Prices'!B249
    value = 70.84
    formula = "='Input EIA Crude WTI'!B247"
    @eval_fn
    def B249():
        b247_1 = Input_EIA_Crude_WTI.B247()
        return b247_1

@register(Crude_Oil_Prices)
class C249():
    # 'Crude_Oil_Prices'!C249
    value = 69.78
    formula = "='Input EIA Crude Europe Brent'!B231"
    @eval_fn
    def C249():
        b231_1 = Input_EIA_Crude_Europe_Brent.B231()
        return b231_1

@register(Crude_Oil_Prices)
class A250():
    # 'Crude_Oil_Prices'!A250
    value = 38883
    isdatetime = True

@register(Crude_Oil_Prices)
class B250():
    # 'Crude_Oil_Prices'!B250
    value = 70.95
    formula = "='Input EIA Crude WTI'!B248"
    @eval_fn
    def B250():
        b248_1 = Input_EIA_Crude_WTI.B248()
        return b248_1

@register(Crude_Oil_Prices)
class C250():
    # 'Crude_Oil_Prices'!C250
    value = 68.56
    formula = "='Input EIA Crude Europe Brent'!B232"
    @eval_fn
    def C250():
        b232_1 = Input_EIA_Crude_Europe_Brent.B232()
        return b232_1

@register(Crude_Oil_Prices)
class A251():
    # 'Crude_Oil_Prices'!A251
    value = 38913
    isdatetime = True

@register(Crude_Oil_Prices)
class B251():
    # 'Crude_Oil_Prices'!B251
    value = 74.41
    formula = "='Input EIA Crude WTI'!B249"
    @eval_fn
    def B251():
        b249_1 = Input_EIA_Crude_WTI.B249()
        return b249_1

@register(Crude_Oil_Prices)
class C251():
    # 'Crude_Oil_Prices'!C251
    value = 73.67
    formula = "='Input EIA Crude Europe Brent'!B233"
    @eval_fn
    def C251():
        b233_1 = Input_EIA_Crude_Europe_Brent.B233()
        return b233_1

@register(Crude_Oil_Prices)
class A252():
    # 'Crude_Oil_Prices'!A252
    value = 38944
    isdatetime = True

@register(Crude_Oil_Prices)
class B252():
    # 'Crude_Oil_Prices'!B252
    value = 73.04
    formula = "='Input EIA Crude WTI'!B250"
    @eval_fn
    def B252():
        b250_1 = Input_EIA_Crude_WTI.B250()
        return b250_1

@register(Crude_Oil_Prices)
class C252():
    # 'Crude_Oil_Prices'!C252
    value = 73.23
    formula = "='Input EIA Crude Europe Brent'!B234"
    @eval_fn
    def C252():
        b234_1 = Input_EIA_Crude_Europe_Brent.B234()
        return b234_1

@register(Crude_Oil_Prices)
class A253():
    # 'Crude_Oil_Prices'!A253
    value = 38975
    isdatetime = True

@register(Crude_Oil_Prices)
class B253():
    # 'Crude_Oil_Prices'!B253
    value = 63.8
    formula = "='Input EIA Crude WTI'!B251"
    @eval_fn
    def B253():
        b251_1 = Input_EIA_Crude_WTI.B251()
        return b251_1

@register(Crude_Oil_Prices)
class C253():
    # 'Crude_Oil_Prices'!C253
    value = 61.96
    formula = "='Input EIA Crude Europe Brent'!B235"
    @eval_fn
    def C253():
        b235_1 = Input_EIA_Crude_Europe_Brent.B235()
        return b235_1

@register(Crude_Oil_Prices)
class A254():
    # 'Crude_Oil_Prices'!A254
    value = 39005
    isdatetime = True

@register(Crude_Oil_Prices)
class B254():
    # 'Crude_Oil_Prices'!B254
    value = 58.89
    formula = "='Input EIA Crude WTI'!B252"
    @eval_fn
    def B254():
        b252_1 = Input_EIA_Crude_WTI.B252()
        return b252_1

@register(Crude_Oil_Prices)
class C254():
    # 'Crude_Oil_Prices'!C254
    value = 57.81
    formula = "='Input EIA Crude Europe Brent'!B236"
    @eval_fn
    def C254():
        b236_1 = Input_EIA_Crude_Europe_Brent.B236()
        return b236_1

@register(Crude_Oil_Prices)
class A255():
    # 'Crude_Oil_Prices'!A255
    value = 39036
    isdatetime = True

@register(Crude_Oil_Prices)
class B255():
    # 'Crude_Oil_Prices'!B255
    value = 59.08
    formula = "='Input EIA Crude WTI'!B253"
    @eval_fn
    def B255():
        b253_1 = Input_EIA_Crude_WTI.B253()
        return b253_1

@register(Crude_Oil_Prices)
class C255():
    # 'Crude_Oil_Prices'!C255
    value = 58.76
    formula = "='Input EIA Crude Europe Brent'!B237"
    @eval_fn
    def C255():
        b237_1 = Input_EIA_Crude_Europe_Brent.B237()
        return b237_1

@register(Crude_Oil_Prices)
class A256():
    # 'Crude_Oil_Prices'!A256
    value = 39066
    isdatetime = True

@register(Crude_Oil_Prices)
class B256():
    # 'Crude_Oil_Prices'!B256
    value = 61.96
    formula = "='Input EIA Crude WTI'!B254"
    @eval_fn
    def B256():
        b254_1 = Input_EIA_Crude_WTI.B254()
        return b254_1

@register(Crude_Oil_Prices)
class C256():
    # 'Crude_Oil_Prices'!C256
    value = 62.47
    formula = "='Input EIA Crude Europe Brent'!B238"
    @eval_fn
    def C256():
        b238_1 = Input_EIA_Crude_Europe_Brent.B238()
        return b238_1

@register(Crude_Oil_Prices)
class A257():
    # 'Crude_Oil_Prices'!A257
    value = 39097
    isdatetime = True

@register(Crude_Oil_Prices)
class B257():
    # 'Crude_Oil_Prices'!B257
    value = 54.51
    formula = "='Input EIA Crude WTI'!B255"
    @eval_fn
    def B257():
        b255_1 = Input_EIA_Crude_WTI.B255()
        return b255_1

@register(Crude_Oil_Prices)
class C257():
    # 'Crude_Oil_Prices'!C257
    value = 53.68
    formula = "='Input EIA Crude Europe Brent'!B239"
    @eval_fn
    def C257():
        b239_1 = Input_EIA_Crude_Europe_Brent.B239()
        return b239_1

@register(Crude_Oil_Prices)
class A258():
    # 'Crude_Oil_Prices'!A258
    value = 39128
    isdatetime = True

@register(Crude_Oil_Prices)
class B258():
    # 'Crude_Oil_Prices'!B258
    value = 59.28
    formula = "='Input EIA Crude WTI'!B256"
    @eval_fn
    def B258():
        b256_1 = Input_EIA_Crude_WTI.B256()
        return b256_1

@register(Crude_Oil_Prices)
class C258():
    # 'Crude_Oil_Prices'!C258
    value = 57.56
    formula = "='Input EIA Crude Europe Brent'!B240"
    @eval_fn
    def C258():
        b240_1 = Input_EIA_Crude_Europe_Brent.B240()
        return b240_1

@register(Crude_Oil_Prices)
class A259():
    # 'Crude_Oil_Prices'!A259
    value = 39156
    isdatetime = True

@register(Crude_Oil_Prices)
class B259():
    # 'Crude_Oil_Prices'!B259
    value = 60.44
    formula = "='Input EIA Crude WTI'!B257"
    @eval_fn
    def B259():
        b257_1 = Input_EIA_Crude_WTI.B257()
        return b257_1

@register(Crude_Oil_Prices)
class C259():
    # 'Crude_Oil_Prices'!C259
    value = 62.05
    formula = "='Input EIA Crude Europe Brent'!B241"
    @eval_fn
    def C259():
        b241_1 = Input_EIA_Crude_Europe_Brent.B241()
        return b241_1

@register(Crude_Oil_Prices)
class A260():
    # 'Crude_Oil_Prices'!A260
    value = 39187
    isdatetime = True

@register(Crude_Oil_Prices)
class B260():
    # 'Crude_Oil_Prices'!B260
    value = 63.98
    formula = "='Input EIA Crude WTI'!B258"
    @eval_fn
    def B260():
        b258_1 = Input_EIA_Crude_WTI.B258()
        return b258_1

@register(Crude_Oil_Prices)
class C260():
    # 'Crude_Oil_Prices'!C260
    value = 67.49
    formula = "='Input EIA Crude Europe Brent'!B242"
    @eval_fn
    def C260():
        b242_1 = Input_EIA_Crude_Europe_Brent.B242()
        return b242_1

@register(Crude_Oil_Prices)
class A261():
    # 'Crude_Oil_Prices'!A261
    value = 39217
    isdatetime = True

@register(Crude_Oil_Prices)
class B261():
    # 'Crude_Oil_Prices'!B261
    value = 63.46
    formula = "='Input EIA Crude WTI'!B259"
    @eval_fn
    def B261():
        b259_1 = Input_EIA_Crude_WTI.B259()
        return b259_1

@register(Crude_Oil_Prices)
class C261():
    # 'Crude_Oil_Prices'!C261
    value = 67.21
    formula = "='Input EIA Crude Europe Brent'!B243"
    @eval_fn
    def C261():
        b243_1 = Input_EIA_Crude_Europe_Brent.B243()
        return b243_1

@register(Crude_Oil_Prices)
class A262():
    # 'Crude_Oil_Prices'!A262
    value = 39248
    isdatetime = True

@register(Crude_Oil_Prices)
class B262():
    # 'Crude_Oil_Prices'!B262
    value = 67.49
    formula = "='Input EIA Crude WTI'!B260"
    @eval_fn
    def B262():
        b260_1 = Input_EIA_Crude_WTI.B260()
        return b260_1

@register(Crude_Oil_Prices)
class C262():
    # 'Crude_Oil_Prices'!C262
    value = 71.05
    formula = "='Input EIA Crude Europe Brent'!B244"
    @eval_fn
    def C262():
        b244_1 = Input_EIA_Crude_Europe_Brent.B244()
        return b244_1

@register(Crude_Oil_Prices)
class A263():
    # 'Crude_Oil_Prices'!A263
    value = 39278
    isdatetime = True

@register(Crude_Oil_Prices)
class B263():
    # 'Crude_Oil_Prices'!B263
    value = 74.12
    formula = "='Input EIA Crude WTI'!B261"
    @eval_fn
    def B263():
        b261_1 = Input_EIA_Crude_WTI.B261()
        return b261_1

@register(Crude_Oil_Prices)
class C263():
    # 'Crude_Oil_Prices'!C263
    value = 76.93
    formula = "='Input EIA Crude Europe Brent'!B245"
    @eval_fn
    def C263():
        b245_1 = Input_EIA_Crude_Europe_Brent.B245()
        return b245_1

@register(Crude_Oil_Prices)
class A264():
    # 'Crude_Oil_Prices'!A264
    value = 39309
    isdatetime = True

@register(Crude_Oil_Prices)
class B264():
    # 'Crude_Oil_Prices'!B264
    value = 72.36
    formula = "='Input EIA Crude WTI'!B262"
    @eval_fn
    def B264():
        b262_1 = Input_EIA_Crude_WTI.B262()
        return b262_1

@register(Crude_Oil_Prices)
class C264():
    # 'Crude_Oil_Prices'!C264
    value = 70.76
    formula = "='Input EIA Crude Europe Brent'!B246"
    @eval_fn
    def C264():
        b246_1 = Input_EIA_Crude_Europe_Brent.B246()
        return b246_1

@register(Crude_Oil_Prices)
class A265():
    # 'Crude_Oil_Prices'!A265
    value = 39340
    isdatetime = True

@register(Crude_Oil_Prices)
class B265():
    # 'Crude_Oil_Prices'!B265
    value = 79.92
    formula = "='Input EIA Crude WTI'!B263"
    @eval_fn
    def B265():
        b263_1 = Input_EIA_Crude_WTI.B263()
        return b263_1

@register(Crude_Oil_Prices)
class C265():
    # 'Crude_Oil_Prices'!C265
    value = 77.17
    formula = "='Input EIA Crude Europe Brent'!B247"
    @eval_fn
    def C265():
        b247_1 = Input_EIA_Crude_Europe_Brent.B247()
        return b247_1

@register(Crude_Oil_Prices)
class A266():
    # 'Crude_Oil_Prices'!A266
    value = 39370
    isdatetime = True

@register(Crude_Oil_Prices)
class B266():
    # 'Crude_Oil_Prices'!B266
    value = 85.8
    formula = "='Input EIA Crude WTI'!B264"
    @eval_fn
    def B266():
        b264_1 = Input_EIA_Crude_WTI.B264()
        return b264_1

@register(Crude_Oil_Prices)
class C266():
    # 'Crude_Oil_Prices'!C266
    value = 82.34
    formula = "='Input EIA Crude Europe Brent'!B248"
    @eval_fn
    def C266():
        b248_1 = Input_EIA_Crude_Europe_Brent.B248()
        return b248_1

@register(Crude_Oil_Prices)
class A267():
    # 'Crude_Oil_Prices'!A267
    value = 39401
    isdatetime = True

@register(Crude_Oil_Prices)
class B267():
    # 'Crude_Oil_Prices'!B267
    value = 94.77
    formula = "='Input EIA Crude WTI'!B265"
    @eval_fn
    def B267():
        b265_1 = Input_EIA_Crude_WTI.B265()
        return b265_1

@register(Crude_Oil_Prices)
class C267():
    # 'Crude_Oil_Prices'!C267
    value = 92.41
    formula = "='Input EIA Crude Europe Brent'!B249"
    @eval_fn
    def C267():
        b249_1 = Input_EIA_Crude_Europe_Brent.B249()
        return b249_1

@register(Crude_Oil_Prices)
class A268():
    # 'Crude_Oil_Prices'!A268
    value = 39431
    isdatetime = True

@register(Crude_Oil_Prices)
class B268():
    # 'Crude_Oil_Prices'!B268
    value = 91.69
    formula = "='Input EIA Crude WTI'!B266"
    @eval_fn
    def B268():
        b266_1 = Input_EIA_Crude_WTI.B266()
        return b266_1

@register(Crude_Oil_Prices)
class C268():
    # 'Crude_Oil_Prices'!C268
    value = 90.93
    formula = "='Input EIA Crude Europe Brent'!B250"
    @eval_fn
    def C268():
        b250_1 = Input_EIA_Crude_Europe_Brent.B250()
        return b250_1

@register(Crude_Oil_Prices)
class A269():
    # 'Crude_Oil_Prices'!A269
    value = 39462
    isdatetime = True

@register(Crude_Oil_Prices)
class B269():
    # 'Crude_Oil_Prices'!B269
    value = 92.97
    formula = "='Input EIA Crude WTI'!B267"
    @eval_fn
    def B269():
        b267_1 = Input_EIA_Crude_WTI.B267()
        return b267_1

@register(Crude_Oil_Prices)
class C269():
    # 'Crude_Oil_Prices'!C269
    value = 92.18
    formula = "='Input EIA Crude Europe Brent'!B251"
    @eval_fn
    def C269():
        b251_1 = Input_EIA_Crude_Europe_Brent.B251()
        return b251_1

@register(Crude_Oil_Prices)
class A270():
    # 'Crude_Oil_Prices'!A270
    value = 39493
    isdatetime = True

@register(Crude_Oil_Prices)
class B270():
    # 'Crude_Oil_Prices'!B270
    value = 95.39
    formula = "='Input EIA Crude WTI'!B268"
    @eval_fn
    def B270():
        b268_1 = Input_EIA_Crude_WTI.B268()
        return b268_1

@register(Crude_Oil_Prices)
class C270():
    # 'Crude_Oil_Prices'!C270
    value = 94.99
    formula = "='Input EIA Crude Europe Brent'!B252"
    @eval_fn
    def C270():
        b252_1 = Input_EIA_Crude_Europe_Brent.B252()
        return b252_1

@register(Crude_Oil_Prices)
class A271():
    # 'Crude_Oil_Prices'!A271
    value = 39522
    isdatetime = True

@register(Crude_Oil_Prices)
class B271():
    # 'Crude_Oil_Prices'!B271
    value = 105.45
    formula = "='Input EIA Crude WTI'!B269"
    @eval_fn
    def B271():
        b269_1 = Input_EIA_Crude_WTI.B269()
        return b269_1

@register(Crude_Oil_Prices)
class C271():
    # 'Crude_Oil_Prices'!C271
    value = 103.64
    formula = "='Input EIA Crude Europe Brent'!B253"
    @eval_fn
    def C271():
        b253_1 = Input_EIA_Crude_Europe_Brent.B253()
        return b253_1

@register(Crude_Oil_Prices)
class A272():
    # 'Crude_Oil_Prices'!A272
    value = 39553
    isdatetime = True

@register(Crude_Oil_Prices)
class B272():
    # 'Crude_Oil_Prices'!B272
    value = 112.58
    formula = "='Input EIA Crude WTI'!B270"
    @eval_fn
    def B272():
        b270_1 = Input_EIA_Crude_WTI.B270()
        return b270_1

@register(Crude_Oil_Prices)
class C272():
    # 'Crude_Oil_Prices'!C272
    value = 109.07
    formula = "='Input EIA Crude Europe Brent'!B254"
    @eval_fn
    def C272():
        b254_1 = Input_EIA_Crude_Europe_Brent.B254()
        return b254_1

@register(Crude_Oil_Prices)
class A273():
    # 'Crude_Oil_Prices'!A273
    value = 39583
    isdatetime = True

@register(Crude_Oil_Prices)
class B273():
    # 'Crude_Oil_Prices'!B273
    value = 125.4
    formula = "='Input EIA Crude WTI'!B271"
    @eval_fn
    def B273():
        b271_1 = Input_EIA_Crude_WTI.B271()
        return b271_1

@register(Crude_Oil_Prices)
class C273():
    # 'Crude_Oil_Prices'!C273
    value = 122.8
    formula = "='Input EIA Crude Europe Brent'!B255"
    @eval_fn
    def C273():
        b255_1 = Input_EIA_Crude_Europe_Brent.B255()
        return b255_1

@register(Crude_Oil_Prices)
class A274():
    # 'Crude_Oil_Prices'!A274
    value = 39614
    isdatetime = True

@register(Crude_Oil_Prices)
class B274():
    # 'Crude_Oil_Prices'!B274
    value = 133.88
    formula = "='Input EIA Crude WTI'!B272"
    @eval_fn
    def B274():
        b272_1 = Input_EIA_Crude_WTI.B272()
        return b272_1

@register(Crude_Oil_Prices)
class C274():
    # 'Crude_Oil_Prices'!C274
    value = 132.32
    formula = "='Input EIA Crude Europe Brent'!B256"
    @eval_fn
    def C274():
        b256_1 = Input_EIA_Crude_Europe_Brent.B256()
        return b256_1

@register(Crude_Oil_Prices)
class A275():
    # 'Crude_Oil_Prices'!A275
    value = 39644
    isdatetime = True

@register(Crude_Oil_Prices)
class B275():
    # 'Crude_Oil_Prices'!B275
    value = 133.37
    formula = "='Input EIA Crude WTI'!B273"
    @eval_fn
    def B275():
        b273_1 = Input_EIA_Crude_WTI.B273()
        return b273_1

@register(Crude_Oil_Prices)
class C275():
    # 'Crude_Oil_Prices'!C275
    value = 132.72
    formula = "='Input EIA Crude Europe Brent'!B257"
    @eval_fn
    def C275():
        b257_1 = Input_EIA_Crude_Europe_Brent.B257()
        return b257_1

@register(Crude_Oil_Prices)
class A276():
    # 'Crude_Oil_Prices'!A276
    value = 39675
    isdatetime = True

@register(Crude_Oil_Prices)
class B276():
    # 'Crude_Oil_Prices'!B276
    value = 116.67
    formula = "='Input EIA Crude WTI'!B274"
    @eval_fn
    def B276():
        b274_1 = Input_EIA_Crude_WTI.B274()
        return b274_1

@register(Crude_Oil_Prices)
class C276():
    # 'Crude_Oil_Prices'!C276
    value = 113.24
    formula = "='Input EIA Crude Europe Brent'!B258"
    @eval_fn
    def C276():
        b258_1 = Input_EIA_Crude_Europe_Brent.B258()
        return b258_1

@register(Crude_Oil_Prices)
class A277():
    # 'Crude_Oil_Prices'!A277
    value = 39706
    isdatetime = True

@register(Crude_Oil_Prices)
class B277():
    # 'Crude_Oil_Prices'!B277
    value = 104.11
    formula = "='Input EIA Crude WTI'!B275"
    @eval_fn
    def B277():
        b275_1 = Input_EIA_Crude_WTI.B275()
        return b275_1

@register(Crude_Oil_Prices)
class C277():
    # 'Crude_Oil_Prices'!C277
    value = 97.23
    formula = "='Input EIA Crude Europe Brent'!B259"
    @eval_fn
    def C277():
        b259_1 = Input_EIA_Crude_Europe_Brent.B259()
        return b259_1

@register(Crude_Oil_Prices)
class A278():
    # 'Crude_Oil_Prices'!A278
    value = 39736
    isdatetime = True

@register(Crude_Oil_Prices)
class B278():
    # 'Crude_Oil_Prices'!B278
    value = 76.61
    formula = "='Input EIA Crude WTI'!B276"
    @eval_fn
    def B278():
        b276_1 = Input_EIA_Crude_WTI.B276()
        return b276_1

@register(Crude_Oil_Prices)
class C278():
    # 'Crude_Oil_Prices'!C278
    value = 71.58
    formula = "='Input EIA Crude Europe Brent'!B260"
    @eval_fn
    def C278():
        b260_1 = Input_EIA_Crude_Europe_Brent.B260()
        return b260_1

@register(Crude_Oil_Prices)
class A279():
    # 'Crude_Oil_Prices'!A279
    value = 39767
    isdatetime = True

@register(Crude_Oil_Prices)
class B279():
    # 'Crude_Oil_Prices'!B279
    value = 57.31
    formula = "='Input EIA Crude WTI'!B277"
    @eval_fn
    def B279():
        b277_1 = Input_EIA_Crude_WTI.B277()
        return b277_1

@register(Crude_Oil_Prices)
class C279():
    # 'Crude_Oil_Prices'!C279
    value = 52.45
    formula = "='Input EIA Crude Europe Brent'!B261"
    @eval_fn
    def C279():
        b261_1 = Input_EIA_Crude_Europe_Brent.B261()
        return b261_1

@register(Crude_Oil_Prices)
class A280():
    # 'Crude_Oil_Prices'!A280
    value = 39797
    isdatetime = True

@register(Crude_Oil_Prices)
class B280():
    # 'Crude_Oil_Prices'!B280
    value = 41.12
    formula = "='Input EIA Crude WTI'!B278"
    @eval_fn
    def B280():
        b278_1 = Input_EIA_Crude_WTI.B278()
        return b278_1

@register(Crude_Oil_Prices)
class C280():
    # 'Crude_Oil_Prices'!C280
    value = 39.95
    formula = "='Input EIA Crude Europe Brent'!B262"
    @eval_fn
    def C280():
        b262_1 = Input_EIA_Crude_Europe_Brent.B262()
        return b262_1

@register(Crude_Oil_Prices)
class A281():
    # 'Crude_Oil_Prices'!A281
    value = 39828
    isdatetime = True

@register(Crude_Oil_Prices)
class B281():
    # 'Crude_Oil_Prices'!B281
    value = 41.71
    formula = "='Input EIA Crude WTI'!B279"
    @eval_fn
    def B281():
        b279_1 = Input_EIA_Crude_WTI.B279()
        return b279_1

@register(Crude_Oil_Prices)
class C281():
    # 'Crude_Oil_Prices'!C281
    value = 43.44
    formula = "='Input EIA Crude Europe Brent'!B263"
    @eval_fn
    def C281():
        b263_1 = Input_EIA_Crude_Europe_Brent.B263()
        return b263_1

@register(Crude_Oil_Prices)
class A282():
    # 'Crude_Oil_Prices'!A282
    value = 39859
    isdatetime = True

@register(Crude_Oil_Prices)
class B282():
    # 'Crude_Oil_Prices'!B282
    value = 39.09
    formula = "='Input EIA Crude WTI'!B280"
    @eval_fn
    def B282():
        b280_1 = Input_EIA_Crude_WTI.B280()
        return b280_1

@register(Crude_Oil_Prices)
class C282():
    # 'Crude_Oil_Prices'!C282
    value = 43.32
    formula = "='Input EIA Crude Europe Brent'!B264"
    @eval_fn
    def C282():
        b264_1 = Input_EIA_Crude_Europe_Brent.B264()
        return b264_1

@register(Crude_Oil_Prices)
class A283():
    # 'Crude_Oil_Prices'!A283
    value = 39887
    isdatetime = True

@register(Crude_Oil_Prices)
class B283():
    # 'Crude_Oil_Prices'!B283
    value = 47.94
    formula = "='Input EIA Crude WTI'!B281"
    @eval_fn
    def B283():
        b281_1 = Input_EIA_Crude_WTI.B281()
        return b281_1

@register(Crude_Oil_Prices)
class C283():
    # 'Crude_Oil_Prices'!C283
    value = 46.54
    formula = "='Input EIA Crude Europe Brent'!B265"
    @eval_fn
    def C283():
        b265_1 = Input_EIA_Crude_Europe_Brent.B265()
        return b265_1

@register(Crude_Oil_Prices)
class A284():
    # 'Crude_Oil_Prices'!A284
    value = 39918
    isdatetime = True

@register(Crude_Oil_Prices)
class B284():
    # 'Crude_Oil_Prices'!B284
    value = 49.65
    formula = "='Input EIA Crude WTI'!B282"
    @eval_fn
    def B284():
        b282_1 = Input_EIA_Crude_WTI.B282()
        return b282_1

@register(Crude_Oil_Prices)
class C284():
    # 'Crude_Oil_Prices'!C284
    value = 50.18
    formula = "='Input EIA Crude Europe Brent'!B266"
    @eval_fn
    def C284():
        b266_1 = Input_EIA_Crude_Europe_Brent.B266()
        return b266_1

@register(Crude_Oil_Prices)
class A285():
    # 'Crude_Oil_Prices'!A285
    value = 39948
    isdatetime = True

@register(Crude_Oil_Prices)
class B285():
    # 'Crude_Oil_Prices'!B285
    value = 59.03
    formula = "='Input EIA Crude WTI'!B283"
    @eval_fn
    def B285():
        b283_1 = Input_EIA_Crude_WTI.B283()
        return b283_1

@register(Crude_Oil_Prices)
class C285():
    # 'Crude_Oil_Prices'!C285
    value = 57.3
    formula = "='Input EIA Crude Europe Brent'!B267"
    @eval_fn
    def C285():
        b267_1 = Input_EIA_Crude_Europe_Brent.B267()
        return b267_1

@register(Crude_Oil_Prices)
class A286():
    # 'Crude_Oil_Prices'!A286
    value = 39979
    isdatetime = True

@register(Crude_Oil_Prices)
class B286():
    # 'Crude_Oil_Prices'!B286
    value = 69.64
    formula = "='Input EIA Crude WTI'!B284"
    @eval_fn
    def B286():
        b284_1 = Input_EIA_Crude_WTI.B284()
        return b284_1

@register(Crude_Oil_Prices)
class C286():
    # 'Crude_Oil_Prices'!C286
    value = 68.61
    formula = "='Input EIA Crude Europe Brent'!B268"
    @eval_fn
    def C286():
        b268_1 = Input_EIA_Crude_Europe_Brent.B268()
        return b268_1

@register(Crude_Oil_Prices)
class A287():
    # 'Crude_Oil_Prices'!A287
    value = 40009
    isdatetime = True

@register(Crude_Oil_Prices)
class B287():
    # 'Crude_Oil_Prices'!B287
    value = 64.15
    formula = "='Input EIA Crude WTI'!B285"
    @eval_fn
    def B287():
        b285_1 = Input_EIA_Crude_WTI.B285()
        return b285_1

@register(Crude_Oil_Prices)
class C287():
    # 'Crude_Oil_Prices'!C287
    value = 64.44
    formula = "='Input EIA Crude Europe Brent'!B269"
    @eval_fn
    def C287():
        b269_1 = Input_EIA_Crude_Europe_Brent.B269()
        return b269_1

@register(Crude_Oil_Prices)
class A288():
    # 'Crude_Oil_Prices'!A288
    value = 40040
    isdatetime = True

@register(Crude_Oil_Prices)
class B288():
    # 'Crude_Oil_Prices'!B288
    value = 71.05
    formula = "='Input EIA Crude WTI'!B286"
    @eval_fn
    def B288():
        b286_1 = Input_EIA_Crude_WTI.B286()
        return b286_1

@register(Crude_Oil_Prices)
class C288():
    # 'Crude_Oil_Prices'!C288
    value = 72.51
    formula = "='Input EIA Crude Europe Brent'!B270"
    @eval_fn
    def C288():
        b270_1 = Input_EIA_Crude_Europe_Brent.B270()
        return b270_1

@register(Crude_Oil_Prices)
class A289():
    # 'Crude_Oil_Prices'!A289
    value = 40071
    isdatetime = True

@register(Crude_Oil_Prices)
class B289():
    # 'Crude_Oil_Prices'!B289
    value = 69.41
    formula = "='Input EIA Crude WTI'!B287"
    @eval_fn
    def B289():
        b287_1 = Input_EIA_Crude_WTI.B287()
        return b287_1

@register(Crude_Oil_Prices)
class C289():
    # 'Crude_Oil_Prices'!C289
    value = 67.65
    formula = "='Input EIA Crude Europe Brent'!B271"
    @eval_fn
    def C289():
        b271_1 = Input_EIA_Crude_Europe_Brent.B271()
        return b271_1

@register(Crude_Oil_Prices)
class A290():
    # 'Crude_Oil_Prices'!A290
    value = 40101
    isdatetime = True

@register(Crude_Oil_Prices)
class B290():
    # 'Crude_Oil_Prices'!B290
    value = 75.72
    formula = "='Input EIA Crude WTI'!B288"
    @eval_fn
    def B290():
        b288_1 = Input_EIA_Crude_WTI.B288()
        return b288_1

@register(Crude_Oil_Prices)
class C290():
    # 'Crude_Oil_Prices'!C290
    value = 72.77
    formula = "='Input EIA Crude Europe Brent'!B272"
    @eval_fn
    def C290():
        b272_1 = Input_EIA_Crude_Europe_Brent.B272()
        return b272_1

@register(Crude_Oil_Prices)
class A291():
    # 'Crude_Oil_Prices'!A291
    value = 40132
    isdatetime = True

@register(Crude_Oil_Prices)
class B291():
    # 'Crude_Oil_Prices'!B291
    value = 77.99
    formula = "='Input EIA Crude WTI'!B289"
    @eval_fn
    def B291():
        b289_1 = Input_EIA_Crude_WTI.B289()
        return b289_1

@register(Crude_Oil_Prices)
class C291():
    # 'Crude_Oil_Prices'!C291
    value = 76.66
    formula = "='Input EIA Crude Europe Brent'!B273"
    @eval_fn
    def C291():
        b273_1 = Input_EIA_Crude_Europe_Brent.B273()
        return b273_1

@register(Crude_Oil_Prices)
class A292():
    # 'Crude_Oil_Prices'!A292
    value = 40162
    isdatetime = True

@register(Crude_Oil_Prices)
class B292():
    # 'Crude_Oil_Prices'!B292
    value = 74.47
    formula = "='Input EIA Crude WTI'!B290"
    @eval_fn
    def B292():
        b290_1 = Input_EIA_Crude_WTI.B290()
        return b290_1

@register(Crude_Oil_Prices)
class C292():
    # 'Crude_Oil_Prices'!C292
    value = 74.46
    formula = "='Input EIA Crude Europe Brent'!B274"
    @eval_fn
    def C292():
        b274_1 = Input_EIA_Crude_Europe_Brent.B274()
        return b274_1

@register(Crude_Oil_Prices)
class A293():
    # 'Crude_Oil_Prices'!A293
    value = 40193
    isdatetime = True

@register(Crude_Oil_Prices)
class B293():
    # 'Crude_Oil_Prices'!B293
    value = 78.33
    formula = "='Input EIA Crude WTI'!B291"
    @eval_fn
    def B293():
        b291_1 = Input_EIA_Crude_WTI.B291()
        return b291_1

@register(Crude_Oil_Prices)
class C293():
    # 'Crude_Oil_Prices'!C293
    value = 76.17
    formula = "='Input EIA Crude Europe Brent'!B275"
    @eval_fn
    def C293():
        b275_1 = Input_EIA_Crude_Europe_Brent.B275()
        return b275_1

@register(Crude_Oil_Prices)
class A294():
    # 'Crude_Oil_Prices'!A294
    value = 40224
    isdatetime = True

@register(Crude_Oil_Prices)
class B294():
    # 'Crude_Oil_Prices'!B294
    value = 76.39
    formula = "='Input EIA Crude WTI'!B292"
    @eval_fn
    def B294():
        b292_1 = Input_EIA_Crude_WTI.B292()
        return b292_1

@register(Crude_Oil_Prices)
class C294():
    # 'Crude_Oil_Prices'!C294
    value = 73.75
    formula = "='Input EIA Crude Europe Brent'!B276"
    @eval_fn
    def C294():
        b276_1 = Input_EIA_Crude_Europe_Brent.B276()
        return b276_1

@register(Crude_Oil_Prices)
class A295():
    # 'Crude_Oil_Prices'!A295
    value = 40252
    isdatetime = True

@register(Crude_Oil_Prices)
class B295():
    # 'Crude_Oil_Prices'!B295
    value = 81.2
    formula = "='Input EIA Crude WTI'!B293"
    @eval_fn
    def B295():
        b293_1 = Input_EIA_Crude_WTI.B293()
        return b293_1

@register(Crude_Oil_Prices)
class C295():
    # 'Crude_Oil_Prices'!C295
    value = 78.83
    formula = "='Input EIA Crude Europe Brent'!B277"
    @eval_fn
    def C295():
        b277_1 = Input_EIA_Crude_Europe_Brent.B277()
        return b277_1

@register(Crude_Oil_Prices)
class A296():
    # 'Crude_Oil_Prices'!A296
    value = 40283
    isdatetime = True

@register(Crude_Oil_Prices)
class B296():
    # 'Crude_Oil_Prices'!B296
    value = 84.29
    formula = "='Input EIA Crude WTI'!B294"
    @eval_fn
    def B296():
        b294_1 = Input_EIA_Crude_WTI.B294()
        return b294_1

@register(Crude_Oil_Prices)
class C296():
    # 'Crude_Oil_Prices'!C296
    value = 84.82
    formula = "='Input EIA Crude Europe Brent'!B278"
    @eval_fn
    def C296():
        b278_1 = Input_EIA_Crude_Europe_Brent.B278()
        return b278_1

@register(Crude_Oil_Prices)
class A297():
    # 'Crude_Oil_Prices'!A297
    value = 40313
    isdatetime = True

@register(Crude_Oil_Prices)
class B297():
    # 'Crude_Oil_Prices'!B297
    value = 73.74
    formula = "='Input EIA Crude WTI'!B295"
    @eval_fn
    def B297():
        b295_1 = Input_EIA_Crude_WTI.B295()
        return b295_1

@register(Crude_Oil_Prices)
class C297():
    # 'Crude_Oil_Prices'!C297
    value = 75.95
    formula = "='Input EIA Crude Europe Brent'!B279"
    @eval_fn
    def C297():
        b279_1 = Input_EIA_Crude_Europe_Brent.B279()
        return b279_1

@register(Crude_Oil_Prices)
class A298():
    # 'Crude_Oil_Prices'!A298
    value = 40344
    isdatetime = True

@register(Crude_Oil_Prices)
class B298():
    # 'Crude_Oil_Prices'!B298
    value = 75.34
    formula = "='Input EIA Crude WTI'!B296"
    @eval_fn
    def B298():
        b296_1 = Input_EIA_Crude_WTI.B296()
        return b296_1

@register(Crude_Oil_Prices)
class C298():
    # 'Crude_Oil_Prices'!C298
    value = 74.76
    formula = "='Input EIA Crude Europe Brent'!B280"
    @eval_fn
    def C298():
        b280_1 = Input_EIA_Crude_Europe_Brent.B280()
        return b280_1

@register(Crude_Oil_Prices)
class A299():
    # 'Crude_Oil_Prices'!A299
    value = 40374
    isdatetime = True

@register(Crude_Oil_Prices)
class B299():
    # 'Crude_Oil_Prices'!B299
    value = 76.32
    formula = "='Input EIA Crude WTI'!B297"
    @eval_fn
    def B299():
        b297_1 = Input_EIA_Crude_WTI.B297()
        return b297_1

@register(Crude_Oil_Prices)
class C299():
    # 'Crude_Oil_Prices'!C299
    value = 75.58
    formula = "='Input EIA Crude Europe Brent'!B281"
    @eval_fn
    def C299():
        b281_1 = Input_EIA_Crude_Europe_Brent.B281()
        return b281_1

@register(Crude_Oil_Prices)
class A300():
    # 'Crude_Oil_Prices'!A300
    value = 40405
    isdatetime = True

@register(Crude_Oil_Prices)
class B300():
    # 'Crude_Oil_Prices'!B300
    value = 76.6
    formula = "='Input EIA Crude WTI'!B298"
    @eval_fn
    def B300():
        b298_1 = Input_EIA_Crude_WTI.B298()
        return b298_1

@register(Crude_Oil_Prices)
class C300():
    # 'Crude_Oil_Prices'!C300
    value = 77.04
    formula = "='Input EIA Crude Europe Brent'!B282"
    @eval_fn
    def C300():
        b282_1 = Input_EIA_Crude_Europe_Brent.B282()
        return b282_1

@register(Crude_Oil_Prices)
class A301():
    # 'Crude_Oil_Prices'!A301
    value = 40436
    isdatetime = True

@register(Crude_Oil_Prices)
class B301():
    # 'Crude_Oil_Prices'!B301
    value = 75.24
    formula = "='Input EIA Crude WTI'!B299"
    @eval_fn
    def B301():
        b299_1 = Input_EIA_Crude_WTI.B299()
        return b299_1

@register(Crude_Oil_Prices)
class C301():
    # 'Crude_Oil_Prices'!C301
    value = 77.84
    formula = "='Input EIA Crude Europe Brent'!B283"
    @eval_fn
    def C301():
        b283_1 = Input_EIA_Crude_Europe_Brent.B283()
        return b283_1

@register(Crude_Oil_Prices)
class A302():
    # 'Crude_Oil_Prices'!A302
    value = 40466
    isdatetime = True

@register(Crude_Oil_Prices)
class B302():
    # 'Crude_Oil_Prices'!B302
    value = 81.89
    formula = "='Input EIA Crude WTI'!B300"
    @eval_fn
    def B302():
        b300_1 = Input_EIA_Crude_WTI.B300()
        return b300_1

@register(Crude_Oil_Prices)
class C302():
    # 'Crude_Oil_Prices'!C302
    value = 82.67
    formula = "='Input EIA Crude Europe Brent'!B284"
    @eval_fn
    def C302():
        b284_1 = Input_EIA_Crude_Europe_Brent.B284()
        return b284_1

@register(Crude_Oil_Prices)
class A303():
    # 'Crude_Oil_Prices'!A303
    value = 40497
    isdatetime = True

@register(Crude_Oil_Prices)
class B303():
    # 'Crude_Oil_Prices'!B303
    value = 84.25
    formula = "='Input EIA Crude WTI'!B301"
    @eval_fn
    def B303():
        b301_1 = Input_EIA_Crude_WTI.B301()
        return b301_1

@register(Crude_Oil_Prices)
class C303():
    # 'Crude_Oil_Prices'!C303
    value = 85.28
    formula = "='Input EIA Crude Europe Brent'!B285"
    @eval_fn
    def C303():
        b285_1 = Input_EIA_Crude_Europe_Brent.B285()
        return b285_1

@register(Crude_Oil_Prices)
class A304():
    # 'Crude_Oil_Prices'!A304
    value = 40527
    isdatetime = True

@register(Crude_Oil_Prices)
class B304():
    # 'Crude_Oil_Prices'!B304
    value = 89.15
    formula = "='Input EIA Crude WTI'!B302"
    @eval_fn
    def B304():
        b302_1 = Input_EIA_Crude_WTI.B302()
        return b302_1

@register(Crude_Oil_Prices)
class C304():
    # 'Crude_Oil_Prices'!C304
    value = 91.45
    formula = "='Input EIA Crude Europe Brent'!B286"
    @eval_fn
    def C304():
        b286_1 = Input_EIA_Crude_Europe_Brent.B286()
        return b286_1

@register(Crude_Oil_Prices)
class A305():
    # 'Crude_Oil_Prices'!A305
    value = 40558
    isdatetime = True

@register(Crude_Oil_Prices)
class B305():
    # 'Crude_Oil_Prices'!B305
    value = 89.17
    formula = "='Input EIA Crude WTI'!B303"
    @eval_fn
    def B305():
        b303_1 = Input_EIA_Crude_WTI.B303()
        return b303_1

@register(Crude_Oil_Prices)
class C305():
    # 'Crude_Oil_Prices'!C305
    value = 96.52
    formula = "='Input EIA Crude Europe Brent'!B287"
    @eval_fn
    def C305():
        b287_1 = Input_EIA_Crude_Europe_Brent.B287()
        return b287_1

@register(Crude_Oil_Prices)
class A306():
    # 'Crude_Oil_Prices'!A306
    value = 40589
    isdatetime = True

@register(Crude_Oil_Prices)
class B306():
    # 'Crude_Oil_Prices'!B306
    value = 88.58
    formula = "='Input EIA Crude WTI'!B304"
    @eval_fn
    def B306():
        b304_1 = Input_EIA_Crude_WTI.B304()
        return b304_1

@register(Crude_Oil_Prices)
class C306():
    # 'Crude_Oil_Prices'!C306
    value = 103.72
    formula = "='Input EIA Crude Europe Brent'!B288"
    @eval_fn
    def C306():
        b288_1 = Input_EIA_Crude_Europe_Brent.B288()
        return b288_1

@register(Crude_Oil_Prices)
class A307():
    # 'Crude_Oil_Prices'!A307
    value = 40617
    isdatetime = True

@register(Crude_Oil_Prices)
class B307():
    # 'Crude_Oil_Prices'!B307
    value = 102.86
    formula = "='Input EIA Crude WTI'!B305"
    @eval_fn
    def B307():
        b305_1 = Input_EIA_Crude_WTI.B305()
        return b305_1

@register(Crude_Oil_Prices)
class C307():
    # 'Crude_Oil_Prices'!C307
    value = 114.64
    formula = "='Input EIA Crude Europe Brent'!B289"
    @eval_fn
    def C307():
        b289_1 = Input_EIA_Crude_Europe_Brent.B289()
        return b289_1

@register(Crude_Oil_Prices)
class A308():
    # 'Crude_Oil_Prices'!A308
    value = 40648
    isdatetime = True

@register(Crude_Oil_Prices)
class B308():
    # 'Crude_Oil_Prices'!B308
    value = 109.53
    formula = "='Input EIA Crude WTI'!B306"
    @eval_fn
    def B308():
        b306_1 = Input_EIA_Crude_WTI.B306()
        return b306_1

@register(Crude_Oil_Prices)
class C308():
    # 'Crude_Oil_Prices'!C308
    value = 123.26
    formula = "='Input EIA Crude Europe Brent'!B290"
    @eval_fn
    def C308():
        b290_1 = Input_EIA_Crude_Europe_Brent.B290()
        return b290_1

@register(Crude_Oil_Prices)
class A309():
    # 'Crude_Oil_Prices'!A309
    value = 40678
    isdatetime = True

@register(Crude_Oil_Prices)
class B309():
    # 'Crude_Oil_Prices'!B309
    value = 100.9
    formula = "='Input EIA Crude WTI'!B307"
    @eval_fn
    def B309():
        b307_1 = Input_EIA_Crude_WTI.B307()
        return b307_1

@register(Crude_Oil_Prices)
class C309():
    # 'Crude_Oil_Prices'!C309
    value = 114.99
    formula = "='Input EIA Crude Europe Brent'!B291"
    @eval_fn
    def C309():
        b291_1 = Input_EIA_Crude_Europe_Brent.B291()
        return b291_1

@register(Crude_Oil_Prices)
class A310():
    # 'Crude_Oil_Prices'!A310
    value = 40709
    isdatetime = True

@register(Crude_Oil_Prices)
class B310():
    # 'Crude_Oil_Prices'!B310
    value = 96.26
    formula = "='Input EIA Crude WTI'!B308"
    @eval_fn
    def B310():
        b308_1 = Input_EIA_Crude_WTI.B308()
        return b308_1

@register(Crude_Oil_Prices)
class C310():
    # 'Crude_Oil_Prices'!C310
    value = 113.83
    formula = "='Input EIA Crude Europe Brent'!B292"
    @eval_fn
    def C310():
        b292_1 = Input_EIA_Crude_Europe_Brent.B292()
        return b292_1

@register(Crude_Oil_Prices)
class A311():
    # 'Crude_Oil_Prices'!A311
    value = 40739
    isdatetime = True

@register(Crude_Oil_Prices)
class B311():
    # 'Crude_Oil_Prices'!B311
    value = 97.3
    formula = "='Input EIA Crude WTI'!B309"
    @eval_fn
    def B311():
        b309_1 = Input_EIA_Crude_WTI.B309()
        return b309_1

@register(Crude_Oil_Prices)
class C311():
    # 'Crude_Oil_Prices'!C311
    value = 116.97
    formula = "='Input EIA Crude Europe Brent'!B293"
    @eval_fn
    def C311():
        b293_1 = Input_EIA_Crude_Europe_Brent.B293()
        return b293_1

@register(Crude_Oil_Prices)
class A312():
    # 'Crude_Oil_Prices'!A312
    value = 40770
    isdatetime = True

@register(Crude_Oil_Prices)
class B312():
    # 'Crude_Oil_Prices'!B312
    value = 86.33
    formula = "='Input EIA Crude WTI'!B310"
    @eval_fn
    def B312():
        b310_1 = Input_EIA_Crude_WTI.B310()
        return b310_1

@register(Crude_Oil_Prices)
class C312():
    # 'Crude_Oil_Prices'!C312
    value = 110.22
    formula = "='Input EIA Crude Europe Brent'!B294"
    @eval_fn
    def C312():
        b294_1 = Input_EIA_Crude_Europe_Brent.B294()
        return b294_1

@register(Crude_Oil_Prices)
class A313():
    # 'Crude_Oil_Prices'!A313
    value = 40801
    isdatetime = True

@register(Crude_Oil_Prices)
class B313():
    # 'Crude_Oil_Prices'!B313
    value = 85.52
    formula = "='Input EIA Crude WTI'!B311"
    @eval_fn
    def B313():
        b311_1 = Input_EIA_Crude_WTI.B311()
        return b311_1

@register(Crude_Oil_Prices)
class C313():
    # 'Crude_Oil_Prices'!C313
    value = 112.83
    formula = "='Input EIA Crude Europe Brent'!B295"
    @eval_fn
    def C313():
        b295_1 = Input_EIA_Crude_Europe_Brent.B295()
        return b295_1

@register(Crude_Oil_Prices)
class A314():
    # 'Crude_Oil_Prices'!A314
    value = 40831
    isdatetime = True

@register(Crude_Oil_Prices)
class B314():
    # 'Crude_Oil_Prices'!B314
    value = 86.32
    formula = "='Input EIA Crude WTI'!B312"
    @eval_fn
    def B314():
        b312_1 = Input_EIA_Crude_WTI.B312()
        return b312_1

@register(Crude_Oil_Prices)
class C314():
    # 'Crude_Oil_Prices'!C314
    value = 109.55
    formula = "='Input EIA Crude Europe Brent'!B296"
    @eval_fn
    def C314():
        b296_1 = Input_EIA_Crude_Europe_Brent.B296()
        return b296_1

@register(Crude_Oil_Prices)
class A315():
    # 'Crude_Oil_Prices'!A315
    value = 40862
    isdatetime = True

@register(Crude_Oil_Prices)
class B315():
    # 'Crude_Oil_Prices'!B315
    value = 97.16
    formula = "='Input EIA Crude WTI'!B313"
    @eval_fn
    def B315():
        b313_1 = Input_EIA_Crude_WTI.B313()
        return b313_1

@register(Crude_Oil_Prices)
class C315():
    # 'Crude_Oil_Prices'!C315
    value = 110.77
    formula = "='Input EIA Crude Europe Brent'!B297"
    @eval_fn
    def C315():
        b297_1 = Input_EIA_Crude_Europe_Brent.B297()
        return b297_1

@register(Crude_Oil_Prices)
class A316():
    # 'Crude_Oil_Prices'!A316
    value = 40892
    isdatetime = True

@register(Crude_Oil_Prices)
class B316():
    # 'Crude_Oil_Prices'!B316
    value = 98.56
    formula = "='Input EIA Crude WTI'!B314"
    @eval_fn
    def B316():
        b314_1 = Input_EIA_Crude_WTI.B314()
        return b314_1

@register(Crude_Oil_Prices)
class C316():
    # 'Crude_Oil_Prices'!C316
    value = 107.87
    formula = "='Input EIA Crude Europe Brent'!B298"
    @eval_fn
    def C316():
        b298_1 = Input_EIA_Crude_Europe_Brent.B298()
        return b298_1

@register(Crude_Oil_Prices)
class A317():
    # 'Crude_Oil_Prices'!A317
    value = 40923
    isdatetime = True

@register(Crude_Oil_Prices)
class B317():
    # 'Crude_Oil_Prices'!B317
    value = 100.27
    formula = "='Input EIA Crude WTI'!B315"
    @eval_fn
    def B317():
        b315_1 = Input_EIA_Crude_WTI.B315()
        return b315_1

@register(Crude_Oil_Prices)
class C317():
    # 'Crude_Oil_Prices'!C317
    value = 110.69
    formula = "='Input EIA Crude Europe Brent'!B299"
    @eval_fn
    def C317():
        b299_1 = Input_EIA_Crude_Europe_Brent.B299()
        return b299_1

@register(Crude_Oil_Prices)
class A318():
    # 'Crude_Oil_Prices'!A318
    value = 40954
    isdatetime = True

@register(Crude_Oil_Prices)
class B318():
    # 'Crude_Oil_Prices'!B318
    value = 102.2
    formula = "='Input EIA Crude WTI'!B316"
    @eval_fn
    def B318():
        b316_1 = Input_EIA_Crude_WTI.B316()
        return b316_1

@register(Crude_Oil_Prices)
class C318():
    # 'Crude_Oil_Prices'!C318
    value = 119.33
    formula = "='Input EIA Crude Europe Brent'!B300"
    @eval_fn
    def C318():
        b300_1 = Input_EIA_Crude_Europe_Brent.B300()
        return b300_1

@register(Crude_Oil_Prices)
class A319():
    # 'Crude_Oil_Prices'!A319
    value = 40983
    isdatetime = True

@register(Crude_Oil_Prices)
class B319():
    # 'Crude_Oil_Prices'!B319
    value = 106.16
    formula = "='Input EIA Crude WTI'!B317"
    @eval_fn
    def B319():
        b317_1 = Input_EIA_Crude_WTI.B317()
        return b317_1

@register(Crude_Oil_Prices)
class C319():
    # 'Crude_Oil_Prices'!C319
    value = 125.45
    formula = "='Input EIA Crude Europe Brent'!B301"
    @eval_fn
    def C319():
        b301_1 = Input_EIA_Crude_Europe_Brent.B301()
        return b301_1

@register(Crude_Oil_Prices)
class A320():
    # 'Crude_Oil_Prices'!A320
    value = 41014
    isdatetime = True

@register(Crude_Oil_Prices)
class B320():
    # 'Crude_Oil_Prices'!B320
    value = 103.32
    formula = "='Input EIA Crude WTI'!B318"
    @eval_fn
    def B320():
        b318_1 = Input_EIA_Crude_WTI.B318()
        return b318_1

@register(Crude_Oil_Prices)
class C320():
    # 'Crude_Oil_Prices'!C320
    value = 119.75
    formula = "='Input EIA Crude Europe Brent'!B302"
    @eval_fn
    def C320():
        b302_1 = Input_EIA_Crude_Europe_Brent.B302()
        return b302_1

@register(Crude_Oil_Prices)
class A321():
    # 'Crude_Oil_Prices'!A321
    value = 41044
    isdatetime = True

@register(Crude_Oil_Prices)
class B321():
    # 'Crude_Oil_Prices'!B321
    value = 94.66
    formula = "='Input EIA Crude WTI'!B319"
    @eval_fn
    def B321():
        b319_1 = Input_EIA_Crude_WTI.B319()
        return b319_1

@register(Crude_Oil_Prices)
class C321():
    # 'Crude_Oil_Prices'!C321
    value = 110.34
    formula = "='Input EIA Crude Europe Brent'!B303"
    @eval_fn
    def C321():
        b303_1 = Input_EIA_Crude_Europe_Brent.B303()
        return b303_1

@register(Crude_Oil_Prices)
class A322():
    # 'Crude_Oil_Prices'!A322
    value = 41075
    isdatetime = True

@register(Crude_Oil_Prices)
class B322():
    # 'Crude_Oil_Prices'!B322
    value = 82.3
    formula = "='Input EIA Crude WTI'!B320"
    @eval_fn
    def B322():
        b320_1 = Input_EIA_Crude_WTI.B320()
        return b320_1

@register(Crude_Oil_Prices)
class C322():
    # 'Crude_Oil_Prices'!C322
    value = 95.16
    formula = "='Input EIA Crude Europe Brent'!B304"
    @eval_fn
    def C322():
        b304_1 = Input_EIA_Crude_Europe_Brent.B304()
        return b304_1

@register(Crude_Oil_Prices)
class A323():
    # 'Crude_Oil_Prices'!A323
    value = 41105
    isdatetime = True

@register(Crude_Oil_Prices)
class B323():
    # 'Crude_Oil_Prices'!B323
    value = 87.9
    formula = "='Input EIA Crude WTI'!B321"
    @eval_fn
    def B323():
        b321_1 = Input_EIA_Crude_WTI.B321()
        return b321_1

@register(Crude_Oil_Prices)
class C323():
    # 'Crude_Oil_Prices'!C323
    value = 102.62
    formula = "='Input EIA Crude Europe Brent'!B305"
    @eval_fn
    def C323():
        b305_1 = Input_EIA_Crude_Europe_Brent.B305()
        return b305_1

@register(Crude_Oil_Prices)
class A324():
    # 'Crude_Oil_Prices'!A324
    value = 41136
    isdatetime = True

@register(Crude_Oil_Prices)
class B324():
    # 'Crude_Oil_Prices'!B324
    value = 94.13
    formula = "='Input EIA Crude WTI'!B322"
    @eval_fn
    def B324():
        b322_1 = Input_EIA_Crude_WTI.B322()
        return b322_1

@register(Crude_Oil_Prices)
class C324():
    # 'Crude_Oil_Prices'!C324
    value = 113.36
    formula = "='Input EIA Crude Europe Brent'!B306"
    @eval_fn
    def C324():
        b306_1 = Input_EIA_Crude_Europe_Brent.B306()
        return b306_1

@register(Crude_Oil_Prices)
class A325():
    # 'Crude_Oil_Prices'!A325
    value = 41167
    isdatetime = True

@register(Crude_Oil_Prices)
class B325():
    # 'Crude_Oil_Prices'!B325
    value = 94.51
    formula = "='Input EIA Crude WTI'!B323"
    @eval_fn
    def B325():
        b323_1 = Input_EIA_Crude_WTI.B323()
        return b323_1

@register(Crude_Oil_Prices)
class C325():
    # 'Crude_Oil_Prices'!C325
    value = 112.86
    formula = "='Input EIA Crude Europe Brent'!B307"
    @eval_fn
    def C325():
        b307_1 = Input_EIA_Crude_Europe_Brent.B307()
        return b307_1

@register(Crude_Oil_Prices)
class A326():
    # 'Crude_Oil_Prices'!A326
    value = 41197
    isdatetime = True

@register(Crude_Oil_Prices)
class B326():
    # 'Crude_Oil_Prices'!B326
    value = 89.49
    formula = "='Input EIA Crude WTI'!B324"
    @eval_fn
    def B326():
        b324_1 = Input_EIA_Crude_WTI.B324()
        return b324_1

@register(Crude_Oil_Prices)
class C326():
    # 'Crude_Oil_Prices'!C326
    value = 111.71
    formula = "='Input EIA Crude Europe Brent'!B308"
    @eval_fn
    def C326():
        b308_1 = Input_EIA_Crude_Europe_Brent.B308()
        return b308_1

@register(Crude_Oil_Prices)
class A327():
    # 'Crude_Oil_Prices'!A327
    value = 41228
    isdatetime = True

@register(Crude_Oil_Prices)
class B327():
    # 'Crude_Oil_Prices'!B327
    value = 86.53
    formula = "='Input EIA Crude WTI'!B325"
    @eval_fn
    def B327():
        b325_1 = Input_EIA_Crude_WTI.B325()
        return b325_1

@register(Crude_Oil_Prices)
class C327():
    # 'Crude_Oil_Prices'!C327
    value = 109.06
    formula = "='Input EIA Crude Europe Brent'!B309"
    @eval_fn
    def C327():
        b309_1 = Input_EIA_Crude_Europe_Brent.B309()
        return b309_1

@register(Crude_Oil_Prices)
class A328():
    # 'Crude_Oil_Prices'!A328
    value = 41258
    isdatetime = True

@register(Crude_Oil_Prices)
class B328():
    # 'Crude_Oil_Prices'!B328
    value = 87.86
    formula = "='Input EIA Crude WTI'!B326"
    @eval_fn
    def B328():
        b326_1 = Input_EIA_Crude_WTI.B326()
        return b326_1

@register(Crude_Oil_Prices)
class C328():
    # 'Crude_Oil_Prices'!C328
    value = 109.49
    formula = "='Input EIA Crude Europe Brent'!B310"
    @eval_fn
    def C328():
        b310_1 = Input_EIA_Crude_Europe_Brent.B310()
        return b310_1

@register(Crude_Oil_Prices)
class A329():
    # 'Crude_Oil_Prices'!A329
    value = 41289
    isdatetime = True

@register(Crude_Oil_Prices)
class B329():
    # 'Crude_Oil_Prices'!B329
    value = 94.76
    formula = "='Input EIA Crude WTI'!B327"
    @eval_fn
    def B329():
        b327_1 = Input_EIA_Crude_WTI.B327()
        return b327_1

@register(Crude_Oil_Prices)
class C329():
    # 'Crude_Oil_Prices'!C329
    value = 112.96
    formula = "='Input EIA Crude Europe Brent'!B311"
    @eval_fn
    def C329():
        b311_1 = Input_EIA_Crude_Europe_Brent.B311()
        return b311_1

@register(Crude_Oil_Prices)
class A330():
    # 'Crude_Oil_Prices'!A330
    value = 41320
    isdatetime = True

@register(Crude_Oil_Prices)
class B330():
    # 'Crude_Oil_Prices'!B330
    value = 95.31
    formula = "='Input EIA Crude WTI'!B328"
    @eval_fn
    def B330():
        b328_1 = Input_EIA_Crude_WTI.B328()
        return b328_1

@register(Crude_Oil_Prices)
class C330():
    # 'Crude_Oil_Prices'!C330
    value = 116.05
    formula = "='Input EIA Crude Europe Brent'!B312"
    @eval_fn
    def C330():
        b312_1 = Input_EIA_Crude_Europe_Brent.B312()
        return b312_1

@register(Crude_Oil_Prices)
class A331():
    # 'Crude_Oil_Prices'!A331
    value = 41348
    isdatetime = True

@register(Crude_Oil_Prices)
class B331():
    # 'Crude_Oil_Prices'!B331
    value = 92.94
    formula = "='Input EIA Crude WTI'!B329"
    @eval_fn
    def B331():
        b329_1 = Input_EIA_Crude_WTI.B329()
        return b329_1

@register(Crude_Oil_Prices)
class C331():
    # 'Crude_Oil_Prices'!C331
    value = 108.47
    formula = "='Input EIA Crude Europe Brent'!B313"
    @eval_fn
    def C331():
        b313_1 = Input_EIA_Crude_Europe_Brent.B313()
        return b313_1

@register(Crude_Oil_Prices)
class A332():
    # 'Crude_Oil_Prices'!A332
    value = 41379
    isdatetime = True

@register(Crude_Oil_Prices)
class B332():
    # 'Crude_Oil_Prices'!B332
    value = 92.02
    formula = "='Input EIA Crude WTI'!B330"
    @eval_fn
    def B332():
        b330_1 = Input_EIA_Crude_WTI.B330()
        return b330_1

@register(Crude_Oil_Prices)
class C332():
    # 'Crude_Oil_Prices'!C332
    value = 102.25
    formula = "='Input EIA Crude Europe Brent'!B314"
    @eval_fn
    def C332():
        b314_1 = Input_EIA_Crude_Europe_Brent.B314()
        return b314_1

@register(Crude_Oil_Prices)
class A333():
    # 'Crude_Oil_Prices'!A333
    value = 41409
    isdatetime = True

@register(Crude_Oil_Prices)
class B333():
    # 'Crude_Oil_Prices'!B333
    value = 94.51
    formula = "='Input EIA Crude WTI'!B331"
    @eval_fn
    def B333():
        b331_1 = Input_EIA_Crude_WTI.B331()
        return b331_1

@register(Crude_Oil_Prices)
class C333():
    # 'Crude_Oil_Prices'!C333
    value = 102.56
    formula = "='Input EIA Crude Europe Brent'!B315"
    @eval_fn
    def C333():
        b315_1 = Input_EIA_Crude_Europe_Brent.B315()
        return b315_1

@register(Crude_Oil_Prices)
class A334():
    # 'Crude_Oil_Prices'!A334
    value = 41440
    isdatetime = True

@register(Crude_Oil_Prices)
class B334():
    # 'Crude_Oil_Prices'!B334
    value = 95.77
    formula = "='Input EIA Crude WTI'!B332"
    @eval_fn
    def B334():
        b332_1 = Input_EIA_Crude_WTI.B332()
        return b332_1

@register(Crude_Oil_Prices)
class C334():
    # 'Crude_Oil_Prices'!C334
    value = 102.92
    formula = "='Input EIA Crude Europe Brent'!B316"
    @eval_fn
    def C334():
        b316_1 = Input_EIA_Crude_Europe_Brent.B316()
        return b316_1

@register(Crude_Oil_Prices)
class A335():
    # 'Crude_Oil_Prices'!A335
    value = 41470
    isdatetime = True

@register(Crude_Oil_Prices)
class B335():
    # 'Crude_Oil_Prices'!B335
    value = 104.67
    formula = "='Input EIA Crude WTI'!B333"
    @eval_fn
    def B335():
        b333_1 = Input_EIA_Crude_WTI.B333()
        return b333_1

@register(Crude_Oil_Prices)
class C335():
    # 'Crude_Oil_Prices'!C335
    value = 107.93
    formula = "='Input EIA Crude Europe Brent'!B317"
    @eval_fn
    def C335():
        b317_1 = Input_EIA_Crude_Europe_Brent.B317()
        return b317_1

@register(Crude_Oil_Prices)
class A336():
    # 'Crude_Oil_Prices'!A336
    value = 41501
    isdatetime = True

@register(Crude_Oil_Prices)
class B336():
    # 'Crude_Oil_Prices'!B336
    value = 106.57
    formula = "='Input EIA Crude WTI'!B334"
    @eval_fn
    def B336():
        b334_1 = Input_EIA_Crude_WTI.B334()
        return b334_1

@register(Crude_Oil_Prices)
class C336():
    # 'Crude_Oil_Prices'!C336
    value = 111.28
    formula = "='Input EIA Crude Europe Brent'!B318"
    @eval_fn
    def C336():
        b318_1 = Input_EIA_Crude_Europe_Brent.B318()
        return b318_1

@register(Crude_Oil_Prices)
class A337():
    # 'Crude_Oil_Prices'!A337
    value = 41532
    isdatetime = True

@register(Crude_Oil_Prices)
class B337():
    # 'Crude_Oil_Prices'!B337
    value = 106.29
    formula = "='Input EIA Crude WTI'!B335"
    @eval_fn
    def B337():
        b335_1 = Input_EIA_Crude_WTI.B335()
        return b335_1

@register(Crude_Oil_Prices)
class C337():
    # 'Crude_Oil_Prices'!C337
    value = 111.6
    formula = "='Input EIA Crude Europe Brent'!B319"
    @eval_fn
    def C337():
        b319_1 = Input_EIA_Crude_Europe_Brent.B319()
        return b319_1

@register(Crude_Oil_Prices)
class A338():
    # 'Crude_Oil_Prices'!A338
    value = 41562
    isdatetime = True

@register(Crude_Oil_Prices)
class B338():
    # 'Crude_Oil_Prices'!B338
    value = 100.54
    formula = "='Input EIA Crude WTI'!B336"
    @eval_fn
    def B338():
        b336_1 = Input_EIA_Crude_WTI.B336()
        return b336_1

@register(Crude_Oil_Prices)
class C338():
    # 'Crude_Oil_Prices'!C338
    value = 109.08
    formula = "='Input EIA Crude Europe Brent'!B320"
    @eval_fn
    def C338():
        b320_1 = Input_EIA_Crude_Europe_Brent.B320()
        return b320_1

@register(Crude_Oil_Prices)
class A339():
    # 'Crude_Oil_Prices'!A339
    value = 41593
    isdatetime = True

@register(Crude_Oil_Prices)
class B339():
    # 'Crude_Oil_Prices'!B339
    value = 93.86
    formula = "='Input EIA Crude WTI'!B337"
    @eval_fn
    def B339():
        b337_1 = Input_EIA_Crude_WTI.B337()
        return b337_1

@register(Crude_Oil_Prices)
class C339():
    # 'Crude_Oil_Prices'!C339
    value = 107.79
    formula = "='Input EIA Crude Europe Brent'!B321"
    @eval_fn
    def C339():
        b321_1 = Input_EIA_Crude_Europe_Brent.B321()
        return b321_1

@register(Crude_Oil_Prices)
class A340():
    # 'Crude_Oil_Prices'!A340
    value = 41623
    isdatetime = True

@register(Crude_Oil_Prices)
class B340():
    # 'Crude_Oil_Prices'!B340
    value = 97.63
    formula = "='Input EIA Crude WTI'!B338"
    @eval_fn
    def B340():
        b338_1 = Input_EIA_Crude_WTI.B338()
        return b338_1

@register(Crude_Oil_Prices)
class C340():
    # 'Crude_Oil_Prices'!C340
    value = 110.76
    formula = "='Input EIA Crude Europe Brent'!B322"
    @eval_fn
    def C340():
        b322_1 = Input_EIA_Crude_Europe_Brent.B322()
        return b322_1

@register(Crude_Oil_Prices)
class A341():
    # 'Crude_Oil_Prices'!A341
    value = 41654
    isdatetime = True

@register(Crude_Oil_Prices)
class B341():
    # 'Crude_Oil_Prices'!B341
    value = 94.62
    formula = "='Input EIA Crude WTI'!B339"
    @eval_fn
    def B341():
        b339_1 = Input_EIA_Crude_WTI.B339()
        return b339_1

@register(Crude_Oil_Prices)
class C341():
    # 'Crude_Oil_Prices'!C341
    value = 108.12
    formula = "='Input EIA Crude Europe Brent'!B323"
    @eval_fn
    def C341():
        b323_1 = Input_EIA_Crude_Europe_Brent.B323()
        return b323_1

@register(Crude_Oil_Prices)
class A342():
    # 'Crude_Oil_Prices'!A342
    value = 41685
    isdatetime = True

@register(Crude_Oil_Prices)
class B342():
    # 'Crude_Oil_Prices'!B342
    value = 100.82
    formula = "='Input EIA Crude WTI'!B340"
    @eval_fn
    def B342():
        b340_1 = Input_EIA_Crude_WTI.B340()
        return b340_1

@register(Crude_Oil_Prices)
class C342():
    # 'Crude_Oil_Prices'!C342
    value = 108.9
    formula = "='Input EIA Crude Europe Brent'!B324"
    @eval_fn
    def C342():
        b324_1 = Input_EIA_Crude_Europe_Brent.B324()
        return b324_1

@register(Crude_Oil_Prices)
class A343():
    # 'Crude_Oil_Prices'!A343
    value = 41713
    isdatetime = True

@register(Crude_Oil_Prices)
class B343():
    # 'Crude_Oil_Prices'!B343
    value = 100.8
    formula = "='Input EIA Crude WTI'!B341"
    @eval_fn
    def B343():
        b341_1 = Input_EIA_Crude_WTI.B341()
        return b341_1

@register(Crude_Oil_Prices)
class C343():
    # 'Crude_Oil_Prices'!C343
    value = 107.48
    formula = "='Input EIA Crude Europe Brent'!B325"
    @eval_fn
    def C343():
        b325_1 = Input_EIA_Crude_Europe_Brent.B325()
        return b325_1

@register(Crude_Oil_Prices)
class A344():
    # 'Crude_Oil_Prices'!A344
    value = 41744
    isdatetime = True

@register(Crude_Oil_Prices)
class B344():
    # 'Crude_Oil_Prices'!B344
    value = 102.07
    formula = "='Input EIA Crude WTI'!B342"
    @eval_fn
    def B344():
        b342_1 = Input_EIA_Crude_WTI.B342()
        return b342_1

@register(Crude_Oil_Prices)
class C344():
    # 'Crude_Oil_Prices'!C344
    value = 107.76
    formula = "='Input EIA Crude Europe Brent'!B326"
    @eval_fn
    def C344():
        b326_1 = Input_EIA_Crude_Europe_Brent.B326()
        return b326_1

@register(Crude_Oil_Prices)
class A345():
    # 'Crude_Oil_Prices'!A345
    value = 41774
    isdatetime = True

@register(Crude_Oil_Prices)
class B345():
    # 'Crude_Oil_Prices'!B345
    value = 102.18
    formula = "='Input EIA Crude WTI'!B343"
    @eval_fn
    def B345():
        b343_1 = Input_EIA_Crude_WTI.B343()
        return b343_1

@register(Crude_Oil_Prices)
class C345():
    # 'Crude_Oil_Prices'!C345
    value = 109.54
    formula = "='Input EIA Crude Europe Brent'!B327"
    @eval_fn
    def C345():
        b327_1 = Input_EIA_Crude_Europe_Brent.B327()
        return b327_1

@register(Crude_Oil_Prices)
class A346():
    # 'Crude_Oil_Prices'!A346
    value = 41805
    isdatetime = True

@register(Crude_Oil_Prices)
class B346():
    # 'Crude_Oil_Prices'!B346
    value = 105.79
    formula = "='Input EIA Crude WTI'!B344"
    @eval_fn
    def B346():
        b344_1 = Input_EIA_Crude_WTI.B344()
        return b344_1

@register(Crude_Oil_Prices)
class C346():
    # 'Crude_Oil_Prices'!C346
    value = 111.8
    formula = "='Input EIA Crude Europe Brent'!B328"
    @eval_fn
    def C346():
        b328_1 = Input_EIA_Crude_Europe_Brent.B328()
        return b328_1

@register(Crude_Oil_Prices)
class A347():
    # 'Crude_Oil_Prices'!A347
    value = 41835
    isdatetime = True

@register(Crude_Oil_Prices)
class B347():
    # 'Crude_Oil_Prices'!B347
    value = 103.59
    formula = "='Input EIA Crude WTI'!B345"
    @eval_fn
    def B347():
        b345_1 = Input_EIA_Crude_WTI.B345()
        return b345_1

@register(Crude_Oil_Prices)
class C347():
    # 'Crude_Oil_Prices'!C347
    value = 106.77
    formula = "='Input EIA Crude Europe Brent'!B329"
    @eval_fn
    def C347():
        b329_1 = Input_EIA_Crude_Europe_Brent.B329()
        return b329_1

@register(Crude_Oil_Prices)
class A348():
    # 'Crude_Oil_Prices'!A348
    value = 41866
    isdatetime = True

@register(Crude_Oil_Prices)
class B348():
    # 'Crude_Oil_Prices'!B348
    value = 96.54
    formula = "='Input EIA Crude WTI'!B346"
    @eval_fn
    def B348():
        b346_1 = Input_EIA_Crude_WTI.B346()
        return b346_1

@register(Crude_Oil_Prices)
class C348():
    # 'Crude_Oil_Prices'!C348
    value = 101.61
    formula = "='Input EIA Crude Europe Brent'!B330"
    @eval_fn
    def C348():
        b330_1 = Input_EIA_Crude_Europe_Brent.B330()
        return b330_1

@register(Crude_Oil_Prices)
class A349():
    # 'Crude_Oil_Prices'!A349
    value = 41897
    isdatetime = True

@register(Crude_Oil_Prices)
class B349():
    # 'Crude_Oil_Prices'!B349
    value = 93.21
    formula = "='Input EIA Crude WTI'!B347"
    @eval_fn
    def B349():
        b347_1 = Input_EIA_Crude_WTI.B347()
        return b347_1

@register(Crude_Oil_Prices)
class C349():
    # 'Crude_Oil_Prices'!C349
    value = 97.09
    formula = "='Input EIA Crude Europe Brent'!B331"
    @eval_fn
    def C349():
        b331_1 = Input_EIA_Crude_Europe_Brent.B331()
        return b331_1

@register(Crude_Oil_Prices)
class A350():
    # 'Crude_Oil_Prices'!A350
    value = 41927
    isdatetime = True

@register(Crude_Oil_Prices)
class B350():
    # 'Crude_Oil_Prices'!B350
    value = 84.4
    formula = "='Input EIA Crude WTI'!B348"
    @eval_fn
    def B350():
        b348_1 = Input_EIA_Crude_WTI.B348()
        return b348_1

@register(Crude_Oil_Prices)
class C350():
    # 'Crude_Oil_Prices'!C350
    value = 87.43
    formula = "='Input EIA Crude Europe Brent'!B332"
    @eval_fn
    def C350():
        b332_1 = Input_EIA_Crude_Europe_Brent.B332()
        return b332_1

@register(Crude_Oil_Prices)
class A351():
    # 'Crude_Oil_Prices'!A351
    value = 41958
    isdatetime = True

@register(Crude_Oil_Prices)
class B351():
    # 'Crude_Oil_Prices'!B351
    value = 75.79
    formula = "='Input EIA Crude WTI'!B349"
    @eval_fn
    def B351():
        b349_1 = Input_EIA_Crude_WTI.B349()
        return b349_1

@register(Crude_Oil_Prices)
class C351():
    # 'Crude_Oil_Prices'!C351
    value = 79.44
    formula = "='Input EIA Crude Europe Brent'!B333"
    @eval_fn
    def C351():
        b333_1 = Input_EIA_Crude_Europe_Brent.B333()
        return b333_1

@register(Crude_Oil_Prices)
class A352():
    # 'Crude_Oil_Prices'!A352
    value = 41988
    isdatetime = True

@register(Crude_Oil_Prices)
class B352():
    # 'Crude_Oil_Prices'!B352
    value = 59.29
    formula = "='Input EIA Crude WTI'!B350"
    @eval_fn
    def B352():
        b350_1 = Input_EIA_Crude_WTI.B350()
        return b350_1

@register(Crude_Oil_Prices)
class C352():
    # 'Crude_Oil_Prices'!C352
    value = 62.34
    formula = "='Input EIA Crude Europe Brent'!B334"
    @eval_fn
    def C352():
        b334_1 = Input_EIA_Crude_Europe_Brent.B334()
        return b334_1

@register(Crude_Oil_Prices)
class A353():
    # 'Crude_Oil_Prices'!A353
    value = 42019
    isdatetime = True

@register(Crude_Oil_Prices)
class B353():
    # 'Crude_Oil_Prices'!B353
    value = 47.22
    formula = "='Input EIA Crude WTI'!B351"
    @eval_fn
    def B353():
        b351_1 = Input_EIA_Crude_WTI.B351()
        return b351_1

@register(Crude_Oil_Prices)
class C353():
    # 'Crude_Oil_Prices'!C353
    value = 47.76
    formula = "='Input EIA Crude Europe Brent'!B335"
    @eval_fn
    def C353():
        b335_1 = Input_EIA_Crude_Europe_Brent.B335()
        return b335_1

@register(Crude_Oil_Prices)
class A354():
    # 'Crude_Oil_Prices'!A354
    value = 42050
    isdatetime = True

@register(Crude_Oil_Prices)
class B354():
    # 'Crude_Oil_Prices'!B354
    value = 50.58
    formula = "='Input EIA Crude WTI'!B352"
    @eval_fn
    def B354():
        b352_1 = Input_EIA_Crude_WTI.B352()
        return b352_1

@register(Crude_Oil_Prices)
class C354():
    # 'Crude_Oil_Prices'!C354
    value = 58.1
    formula = "='Input EIA Crude Europe Brent'!B336"
    @eval_fn
    def C354():
        b336_1 = Input_EIA_Crude_Europe_Brent.B336()
        return b336_1

@register(Crude_Oil_Prices)
class A355():
    # 'Crude_Oil_Prices'!A355
    value = 42078
    isdatetime = True

@register(Crude_Oil_Prices)
class B355():
    # 'Crude_Oil_Prices'!B355
    value = 47.82
    formula = "='Input EIA Crude WTI'!B353"
    @eval_fn
    def B355():
        b353_1 = Input_EIA_Crude_WTI.B353()
        return b353_1

@register(Crude_Oil_Prices)
class C355():
    # 'Crude_Oil_Prices'!C355
    value = 55.89
    formula = "='Input EIA Crude Europe Brent'!B337"
    @eval_fn
    def C355():
        b337_1 = Input_EIA_Crude_Europe_Brent.B337()
        return b337_1

@register(Crude_Oil_Prices)
class A356():
    # 'Crude_Oil_Prices'!A356
    value = 42109
    isdatetime = True

@register(Crude_Oil_Prices)
class B356():
    # 'Crude_Oil_Prices'!B356
    value = 54.45
    formula = "='Input EIA Crude WTI'!B354"
    @eval_fn
    def B356():
        b354_1 = Input_EIA_Crude_WTI.B354()
        return b354_1

@register(Crude_Oil_Prices)
class C356():
    # 'Crude_Oil_Prices'!C356
    value = 59.52
    formula = "='Input EIA Crude Europe Brent'!B338"
    @eval_fn
    def C356():
        b338_1 = Input_EIA_Crude_Europe_Brent.B338()
        return b338_1

@register(Crude_Oil_Prices)
class A357():
    # 'Crude_Oil_Prices'!A357
    value = 42139
    isdatetime = True

@register(Crude_Oil_Prices)
class B357():
    # 'Crude_Oil_Prices'!B357
    value = 59.27
    formula = "='Input EIA Crude WTI'!B355"
    @eval_fn
    def B357():
        b355_1 = Input_EIA_Crude_WTI.B355()
        return b355_1

@register(Crude_Oil_Prices)
class C357():
    # 'Crude_Oil_Prices'!C357
    value = 64.08
    formula = "='Input EIA Crude Europe Brent'!B339"
    @eval_fn
    def C357():
        b339_1 = Input_EIA_Crude_Europe_Brent.B339()
        return b339_1

@register(Crude_Oil_Prices)
class A358():
    # 'Crude_Oil_Prices'!A358
    value = 42170
    isdatetime = True

@register(Crude_Oil_Prices)
class B358():
    # 'Crude_Oil_Prices'!B358
    value = 59.82
    formula = "='Input EIA Crude WTI'!B356"
    @eval_fn
    def B358():
        b356_1 = Input_EIA_Crude_WTI.B356()
        return b356_1

@register(Crude_Oil_Prices)
class C358():
    # 'Crude_Oil_Prices'!C358
    value = 61.48
    formula = "='Input EIA Crude Europe Brent'!B340"
    @eval_fn
    def C358():
        b340_1 = Input_EIA_Crude_Europe_Brent.B340()
        return b340_1

@register(Crude_Oil_Prices)
class A359():
    # 'Crude_Oil_Prices'!A359
    value = 42200
    isdatetime = True

@register(Crude_Oil_Prices)
class B359():
    # 'Crude_Oil_Prices'!B359
    value = 50.9
    formula = "='Input EIA Crude WTI'!B357"
    @eval_fn
    def B359():
        b357_1 = Input_EIA_Crude_WTI.B357()
        return b357_1

@register(Crude_Oil_Prices)
class C359():
    # 'Crude_Oil_Prices'!C359
    value = 56.56
    formula = "='Input EIA Crude Europe Brent'!B341"
    @eval_fn
    def C359():
        b341_1 = Input_EIA_Crude_Europe_Brent.B341()
        return b341_1

@register(Crude_Oil_Prices)
class A360():
    # 'Crude_Oil_Prices'!A360
    value = 42231
    isdatetime = True

@register(Crude_Oil_Prices)
class B360():
    # 'Crude_Oil_Prices'!B360
    value = 42.87
    formula = "='Input EIA Crude WTI'!B358"
    @eval_fn
    def B360():
        b358_1 = Input_EIA_Crude_WTI.B358()
        return b358_1

@register(Crude_Oil_Prices)
class C360():
    # 'Crude_Oil_Prices'!C360
    value = 46.52
    formula = "='Input EIA Crude Europe Brent'!B342"
    @eval_fn
    def C360():
        b342_1 = Input_EIA_Crude_Europe_Brent.B342()
        return b342_1

@register(Crude_Oil_Prices)
class A361():
    # 'Crude_Oil_Prices'!A361
    value = 42262
    isdatetime = True

@register(Crude_Oil_Prices)
class B361():
    # 'Crude_Oil_Prices'!B361
    value = 45.48
    formula = "='Input EIA Crude WTI'!B359"
    @eval_fn
    def B361():
        b359_1 = Input_EIA_Crude_WTI.B359()
        return b359_1

@register(Crude_Oil_Prices)
class C361():
    # 'Crude_Oil_Prices'!C361
    value = 47.62
    formula = "='Input EIA Crude Europe Brent'!B343"
    @eval_fn
    def C361():
        b343_1 = Input_EIA_Crude_Europe_Brent.B343()
        return b343_1

@register(Crude_Oil_Prices)
class A362():
    # 'Crude_Oil_Prices'!A362
    value = 42292
    isdatetime = True

@register(Crude_Oil_Prices)
class B362():
    # 'Crude_Oil_Prices'!B362
    value = 46.22
    formula = "='Input EIA Crude WTI'!B360"
    @eval_fn
    def B362():
        b360_1 = Input_EIA_Crude_WTI.B360()
        return b360_1

@register(Crude_Oil_Prices)
class C362():
    # 'Crude_Oil_Prices'!C362
    value = 48.43
    formula = "='Input EIA Crude Europe Brent'!B344"
    @eval_fn
    def C362():
        b344_1 = Input_EIA_Crude_Europe_Brent.B344()
        return b344_1

@register(Crude_Oil_Prices)
class A363():
    # 'Crude_Oil_Prices'!A363
    value = 42323
    isdatetime = True

@register(Crude_Oil_Prices)
class B363():
    # 'Crude_Oil_Prices'!B363
    value = 42.44
    formula = "='Input EIA Crude WTI'!B361"
    @eval_fn
    def B363():
        b361_1 = Input_EIA_Crude_WTI.B361()
        return b361_1

@register(Crude_Oil_Prices)
class C363():
    # 'Crude_Oil_Prices'!C363
    value = 44.27
    formula = "='Input EIA Crude Europe Brent'!B345"
    @eval_fn
    def C363():
        b345_1 = Input_EIA_Crude_Europe_Brent.B345()
        return b345_1

@register(Crude_Oil_Prices)
class A364():
    # 'Crude_Oil_Prices'!A364
    value = 42353
    isdatetime = True

@register(Crude_Oil_Prices)
class B364():
    # 'Crude_Oil_Prices'!B364
    value = 37.19
    formula = "='Input EIA Crude WTI'!B362"
    @eval_fn
    def B364():
        b362_1 = Input_EIA_Crude_WTI.B362()
        return b362_1

@register(Crude_Oil_Prices)
class C364():
    # 'Crude_Oil_Prices'!C364
    value = 38.01
    formula = "='Input EIA Crude Europe Brent'!B346"
    @eval_fn
    def C364():
        b346_1 = Input_EIA_Crude_Europe_Brent.B346()
        return b346_1

@register(Crude_Oil_Prices)
class A365():
    # 'Crude_Oil_Prices'!A365
    value = 42384
    isdatetime = True

@register(Crude_Oil_Prices)
class B365():
    # 'Crude_Oil_Prices'!B365
    value = 31.68
    formula = "='Input EIA Crude WTI'!B363"
    @eval_fn
    def B365():
        b363_1 = Input_EIA_Crude_WTI.B363()
        return b363_1

@register(Crude_Oil_Prices)
class C365():
    # 'Crude_Oil_Prices'!C365
    value = 30.7
    formula = "='Input EIA Crude Europe Brent'!B347"
    @eval_fn
    def C365():
        b347_1 = Input_EIA_Crude_Europe_Brent.B347()
        return b347_1

@register(Crude_Oil_Prices)
class A366():
    # 'Crude_Oil_Prices'!A366
    value = 42415
    isdatetime = True

@register(Crude_Oil_Prices)
class B366():
    # 'Crude_Oil_Prices'!B366
    value = 0
    formula = "='Input EIA Crude WTI'!B364"
    @eval_fn
    def B366():
        b364_1 = Input_EIA_Crude_WTI.B364()
        return b364_1

@register(Crude_Oil_Prices)
class C366():
    # 'Crude_Oil_Prices'!C366
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B348"
    @eval_fn
    def C366():
        b348_1 = Input_EIA_Crude_Europe_Brent.B348()
        return b348_1

@register(Crude_Oil_Prices)
class A367():
    # 'Crude_Oil_Prices'!A367
    value = 42444
    isdatetime = True

@register(Crude_Oil_Prices)
class B367():
    # 'Crude_Oil_Prices'!B367
    value = 0
    formula = "='Input EIA Crude WTI'!B365"
    @eval_fn
    def B367():
        b365_1 = Input_EIA_Crude_WTI.B365()
        return b365_1

@register(Crude_Oil_Prices)
class C367():
    # 'Crude_Oil_Prices'!C367
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B349"
    @eval_fn
    def C367():
        b349_1 = Input_EIA_Crude_Europe_Brent.B349()
        return b349_1

@register(Crude_Oil_Prices)
class A368():
    # 'Crude_Oil_Prices'!A368
    value = 42475
    isdatetime = True

@register(Crude_Oil_Prices)
class B368():
    # 'Crude_Oil_Prices'!B368
    value = 0
    formula = "='Input EIA Crude WTI'!B366"
    @eval_fn
    def B368():
        b366_1 = Input_EIA_Crude_WTI.B366()
        return b366_1

@register(Crude_Oil_Prices)
class C368():
    # 'Crude_Oil_Prices'!C368
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B350"
    @eval_fn
    def C368():
        b350_1 = Input_EIA_Crude_Europe_Brent.B350()
        return b350_1

@register(Crude_Oil_Prices)
class A369():
    # 'Crude_Oil_Prices'!A369
    value = 42505
    isdatetime = True

@register(Crude_Oil_Prices)
class B369():
    # 'Crude_Oil_Prices'!B369
    value = 0
    formula = "='Input EIA Crude WTI'!B367"
    @eval_fn
    def B369():
        b367_1 = Input_EIA_Crude_WTI.B367()
        return b367_1

@register(Crude_Oil_Prices)
class C369():
    # 'Crude_Oil_Prices'!C369
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B351"
    @eval_fn
    def C369():
        b351_1 = Input_EIA_Crude_Europe_Brent.B351()
        return b351_1

@register(Crude_Oil_Prices)
class A370():
    # 'Crude_Oil_Prices'!A370
    value = 42536
    isdatetime = True

@register(Crude_Oil_Prices)
class B370():
    # 'Crude_Oil_Prices'!B370
    value = 0
    formula = "='Input EIA Crude WTI'!B368"
    @eval_fn
    def B370():
        b368_1 = Input_EIA_Crude_WTI.B368()
        return b368_1

@register(Crude_Oil_Prices)
class C370():
    # 'Crude_Oil_Prices'!C370
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B352"
    @eval_fn
    def C370():
        b352_1 = Input_EIA_Crude_Europe_Brent.B352()
        return b352_1

@register(Crude_Oil_Prices)
class A371():
    # 'Crude_Oil_Prices'!A371
    value = 42566
    isdatetime = True

@register(Crude_Oil_Prices)
class B371():
    # 'Crude_Oil_Prices'!B371
    value = 0
    formula = "='Input EIA Crude WTI'!B369"
    @eval_fn
    def B371():
        b369_1 = Input_EIA_Crude_WTI.B369()
        return b369_1

@register(Crude_Oil_Prices)
class C371():
    # 'Crude_Oil_Prices'!C371
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B353"
    @eval_fn
    def C371():
        b353_1 = Input_EIA_Crude_Europe_Brent.B353()
        return b353_1

@register(Crude_Oil_Prices)
class A372():
    # 'Crude_Oil_Prices'!A372
    value = 42597
    isdatetime = True

@register(Crude_Oil_Prices)
class B372():
    # 'Crude_Oil_Prices'!B372
    value = 0
    formula = "='Input EIA Crude WTI'!B370"
    @eval_fn
    def B372():
        b370_1 = Input_EIA_Crude_WTI.B370()
        return b370_1

@register(Crude_Oil_Prices)
class C372():
    # 'Crude_Oil_Prices'!C372
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B354"
    @eval_fn
    def C372():
        b354_1 = Input_EIA_Crude_Europe_Brent.B354()
        return b354_1

@register(Crude_Oil_Prices)
class A373():
    # 'Crude_Oil_Prices'!A373
    value = 42628
    isdatetime = True

@register(Crude_Oil_Prices)
class B373():
    # 'Crude_Oil_Prices'!B373
    value = 0
    formula = "='Input EIA Crude WTI'!B371"
    @eval_fn
    def B373():
        b371_1 = Input_EIA_Crude_WTI.B371()
        return b371_1

@register(Crude_Oil_Prices)
class C373():
    # 'Crude_Oil_Prices'!C373
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B355"
    @eval_fn
    def C373():
        b355_1 = Input_EIA_Crude_Europe_Brent.B355()
        return b355_1

@register(Crude_Oil_Prices)
class A374():
    # 'Crude_Oil_Prices'!A374
    value = 42658
    isdatetime = True

@register(Crude_Oil_Prices)
class B374():
    # 'Crude_Oil_Prices'!B374
    value = 0
    formula = "='Input EIA Crude WTI'!B372"
    @eval_fn
    def B374():
        b372_1 = Input_EIA_Crude_WTI.B372()
        return b372_1

@register(Crude_Oil_Prices)
class C374():
    # 'Crude_Oil_Prices'!C374
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B356"
    @eval_fn
    def C374():
        b356_1 = Input_EIA_Crude_Europe_Brent.B356()
        return b356_1

@register(Crude_Oil_Prices)
class A375():
    # 'Crude_Oil_Prices'!A375
    value = 42689
    isdatetime = True

@register(Crude_Oil_Prices)
class B375():
    # 'Crude_Oil_Prices'!B375
    value = 0
    formula = "='Input EIA Crude WTI'!B373"
    @eval_fn
    def B375():
        b373_1 = Input_EIA_Crude_WTI.B373()
        return b373_1

@register(Crude_Oil_Prices)
class C375():
    # 'Crude_Oil_Prices'!C375
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B357"
    @eval_fn
    def C375():
        b357_1 = Input_EIA_Crude_Europe_Brent.B357()
        return b357_1

@register(Crude_Oil_Prices)
class A376():
    # 'Crude_Oil_Prices'!A376
    value = 42719
    isdatetime = True

@register(Crude_Oil_Prices)
class B376():
    # 'Crude_Oil_Prices'!B376
    value = 0
    formula = "='Input EIA Crude WTI'!B374"
    @eval_fn
    def B376():
        b374_1 = Input_EIA_Crude_WTI.B374()
        return b374_1

@register(Crude_Oil_Prices)
class C376():
    # 'Crude_Oil_Prices'!C376
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B358"
    @eval_fn
    def C376():
        b358_1 = Input_EIA_Crude_Europe_Brent.B358()
        return b358_1

@register(Crude_Oil_Prices)
class A377():
    # 'Crude_Oil_Prices'!A377
    value = 42750
    isdatetime = True

@register(Crude_Oil_Prices)
class B377():
    # 'Crude_Oil_Prices'!B377
    value = 0
    formula = "='Input EIA Crude WTI'!B375"
    @eval_fn
    def B377():
        b375_1 = Input_EIA_Crude_WTI.B375()
        return b375_1

@register(Crude_Oil_Prices)
class C377():
    # 'Crude_Oil_Prices'!C377
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B359"
    @eval_fn
    def C377():
        b359_1 = Input_EIA_Crude_Europe_Brent.B359()
        return b359_1

@register(Crude_Oil_Prices)
class A378():
    # 'Crude_Oil_Prices'!A378
    value = 42781
    isdatetime = True

@register(Crude_Oil_Prices)
class B378():
    # 'Crude_Oil_Prices'!B378
    value = 0
    formula = "='Input EIA Crude WTI'!B376"
    @eval_fn
    def B378():
        b376_1 = Input_EIA_Crude_WTI.B376()
        return b376_1

@register(Crude_Oil_Prices)
class C378():
    # 'Crude_Oil_Prices'!C378
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B360"
    @eval_fn
    def C378():
        b360_1 = Input_EIA_Crude_Europe_Brent.B360()
        return b360_1

@register(Crude_Oil_Prices)
class A379():
    # 'Crude_Oil_Prices'!A379
    value = 42809
    isdatetime = True

@register(Crude_Oil_Prices)
class B379():
    # 'Crude_Oil_Prices'!B379
    value = 0
    formula = "='Input EIA Crude WTI'!B377"
    @eval_fn
    def B379():
        b377_1 = Input_EIA_Crude_WTI.B377()
        return b377_1

@register(Crude_Oil_Prices)
class C379():
    # 'Crude_Oil_Prices'!C379
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B361"
    @eval_fn
    def C379():
        b361_1 = Input_EIA_Crude_Europe_Brent.B361()
        return b361_1

@register(Crude_Oil_Prices)
class A380():
    # 'Crude_Oil_Prices'!A380
    value = 42840
    isdatetime = True

@register(Crude_Oil_Prices)
class B380():
    # 'Crude_Oil_Prices'!B380
    value = 0
    formula = "='Input EIA Crude WTI'!B378"
    @eval_fn
    def B380():
        b378_1 = Input_EIA_Crude_WTI.B378()
        return b378_1

@register(Crude_Oil_Prices)
class C380():
    # 'Crude_Oil_Prices'!C380
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B362"
    @eval_fn
    def C380():
        b362_1 = Input_EIA_Crude_Europe_Brent.B362()
        return b362_1

@register(Crude_Oil_Prices)
class A381():
    # 'Crude_Oil_Prices'!A381
    value = 42870
    isdatetime = True

@register(Crude_Oil_Prices)
class B381():
    # 'Crude_Oil_Prices'!B381
    value = 0
    formula = "='Input EIA Crude WTI'!B379"
    @eval_fn
    def B381():
        b379_1 = Input_EIA_Crude_WTI.B379()
        return b379_1

@register(Crude_Oil_Prices)
class C381():
    # 'Crude_Oil_Prices'!C381
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B363"
    @eval_fn
    def C381():
        b363_1 = Input_EIA_Crude_Europe_Brent.B363()
        return b363_1

@register(Crude_Oil_Prices)
class A382():
    # 'Crude_Oil_Prices'!A382
    value = 42901
    isdatetime = True

@register(Crude_Oil_Prices)
class B382():
    # 'Crude_Oil_Prices'!B382
    value = 0
    formula = "='Input EIA Crude WTI'!B380"
    @eval_fn
    def B382():
        b380_1 = Input_EIA_Crude_WTI.B380()
        return b380_1

@register(Crude_Oil_Prices)
class C382():
    # 'Crude_Oil_Prices'!C382
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B364"
    @eval_fn
    def C382():
        b364_1 = Input_EIA_Crude_Europe_Brent.B364()
        return b364_1

@register(Crude_Oil_Prices)
class A383():
    # 'Crude_Oil_Prices'!A383
    value = 42931
    isdatetime = True

@register(Crude_Oil_Prices)
class B383():
    # 'Crude_Oil_Prices'!B383
    value = 0
    formula = "='Input EIA Crude WTI'!B381"
    @eval_fn
    def B383():
        b381_1 = Input_EIA_Crude_WTI.B381()
        return b381_1

@register(Crude_Oil_Prices)
class C383():
    # 'Crude_Oil_Prices'!C383
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B365"
    @eval_fn
    def C383():
        b365_1 = Input_EIA_Crude_Europe_Brent.B365()
        return b365_1

@register(Crude_Oil_Prices)
class A384():
    # 'Crude_Oil_Prices'!A384
    value = 42962
    isdatetime = True

@register(Crude_Oil_Prices)
class B384():
    # 'Crude_Oil_Prices'!B384
    value = 0
    formula = "='Input EIA Crude WTI'!B382"
    @eval_fn
    def B384():
        b382_1 = Input_EIA_Crude_WTI.B382()
        return b382_1

@register(Crude_Oil_Prices)
class C384():
    # 'Crude_Oil_Prices'!C384
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B366"
    @eval_fn
    def C384():
        b366_1 = Input_EIA_Crude_Europe_Brent.B366()
        return b366_1

@register(Crude_Oil_Prices)
class A385():
    # 'Crude_Oil_Prices'!A385
    value = 42993
    isdatetime = True

@register(Crude_Oil_Prices)
class B385():
    # 'Crude_Oil_Prices'!B385
    value = 0
    formula = "='Input EIA Crude WTI'!B383"
    @eval_fn
    def B385():
        b383_1 = Input_EIA_Crude_WTI.B383()
        return b383_1

@register(Crude_Oil_Prices)
class C385():
    # 'Crude_Oil_Prices'!C385
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B367"
    @eval_fn
    def C385():
        b367_1 = Input_EIA_Crude_Europe_Brent.B367()
        return b367_1

@register(Crude_Oil_Prices)
class A386():
    # 'Crude_Oil_Prices'!A386
    value = 43023
    isdatetime = True

@register(Crude_Oil_Prices)
class B386():
    # 'Crude_Oil_Prices'!B386
    value = 0
    formula = "='Input EIA Crude WTI'!B384"
    @eval_fn
    def B386():
        b384_1 = Input_EIA_Crude_WTI.B384()
        return b384_1

@register(Crude_Oil_Prices)
class C386():
    # 'Crude_Oil_Prices'!C386
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B368"
    @eval_fn
    def C386():
        b368_1 = Input_EIA_Crude_Europe_Brent.B368()
        return b368_1

@register(Crude_Oil_Prices)
class A387():
    # 'Crude_Oil_Prices'!A387
    value = 43054
    isdatetime = True

@register(Crude_Oil_Prices)
class B387():
    # 'Crude_Oil_Prices'!B387
    value = 0
    formula = "='Input EIA Crude WTI'!B385"
    @eval_fn
    def B387():
        b385_1 = Input_EIA_Crude_WTI.B385()
        return b385_1

@register(Crude_Oil_Prices)
class C387():
    # 'Crude_Oil_Prices'!C387
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B369"
    @eval_fn
    def C387():
        b369_1 = Input_EIA_Crude_Europe_Brent.B369()
        return b369_1

@register(Crude_Oil_Prices)
class A388():
    # 'Crude_Oil_Prices'!A388
    value = 43084
    isdatetime = True

@register(Crude_Oil_Prices)
class B388():
    # 'Crude_Oil_Prices'!B388
    value = 0
    formula = "='Input EIA Crude WTI'!B386"
    @eval_fn
    def B388():
        b386_1 = Input_EIA_Crude_WTI.B386()
        return b386_1

@register(Crude_Oil_Prices)
class C388():
    # 'Crude_Oil_Prices'!C388
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B370"
    @eval_fn
    def C388():
        b370_1 = Input_EIA_Crude_Europe_Brent.B370()
        return b370_1

@register(Crude_Oil_Prices)
class A389():
    # 'Crude_Oil_Prices'!A389
    value = 43115
    isdatetime = True

@register(Crude_Oil_Prices)
class B389():
    # 'Crude_Oil_Prices'!B389
    value = 0
    formula = "='Input EIA Crude WTI'!B387"
    @eval_fn
    def B389():
        b387_1 = Input_EIA_Crude_WTI.B387()
        return b387_1

@register(Crude_Oil_Prices)
class C389():
    # 'Crude_Oil_Prices'!C389
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B371"
    @eval_fn
    def C389():
        b371_1 = Input_EIA_Crude_Europe_Brent.B371()
        return b371_1

@register(Crude_Oil_Prices)
class A390():
    # 'Crude_Oil_Prices'!A390
    value = 43146
    isdatetime = True

@register(Crude_Oil_Prices)
class B390():
    # 'Crude_Oil_Prices'!B390
    value = 0
    formula = "='Input EIA Crude WTI'!B388"
    @eval_fn
    def B390():
        b388_1 = Input_EIA_Crude_WTI.B388()
        return b388_1

@register(Crude_Oil_Prices)
class C390():
    # 'Crude_Oil_Prices'!C390
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B372"
    @eval_fn
    def C390():
        b372_1 = Input_EIA_Crude_Europe_Brent.B372()
        return b372_1

@register(Crude_Oil_Prices)
class A391():
    # 'Crude_Oil_Prices'!A391
    value = 43174
    isdatetime = True

@register(Crude_Oil_Prices)
class B391():
    # 'Crude_Oil_Prices'!B391
    value = 0
    formula = "='Input EIA Crude WTI'!B389"
    @eval_fn
    def B391():
        b389_1 = Input_EIA_Crude_WTI.B389()
        return b389_1

@register(Crude_Oil_Prices)
class C391():
    # 'Crude_Oil_Prices'!C391
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B373"
    @eval_fn
    def C391():
        b373_1 = Input_EIA_Crude_Europe_Brent.B373()
        return b373_1

@register(Crude_Oil_Prices)
class A392():
    # 'Crude_Oil_Prices'!A392
    value = 43205
    isdatetime = True

@register(Crude_Oil_Prices)
class B392():
    # 'Crude_Oil_Prices'!B392
    value = 0
    formula = "='Input EIA Crude WTI'!B390"
    @eval_fn
    def B392():
        b390_1 = Input_EIA_Crude_WTI.B390()
        return b390_1

@register(Crude_Oil_Prices)
class C392():
    # 'Crude_Oil_Prices'!C392
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B374"
    @eval_fn
    def C392():
        b374_1 = Input_EIA_Crude_Europe_Brent.B374()
        return b374_1

@register(Crude_Oil_Prices)
class A393():
    # 'Crude_Oil_Prices'!A393
    value = 43235
    isdatetime = True

@register(Crude_Oil_Prices)
class B393():
    # 'Crude_Oil_Prices'!B393
    value = 0
    formula = "='Input EIA Crude WTI'!B391"
    @eval_fn
    def B393():
        b391_1 = Input_EIA_Crude_WTI.B391()
        return b391_1

@register(Crude_Oil_Prices)
class C393():
    # 'Crude_Oil_Prices'!C393
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B375"
    @eval_fn
    def C393():
        b375_1 = Input_EIA_Crude_Europe_Brent.B375()
        return b375_1

@register(Crude_Oil_Prices)
class A394():
    # 'Crude_Oil_Prices'!A394
    value = 43266
    isdatetime = True

@register(Crude_Oil_Prices)
class B394():
    # 'Crude_Oil_Prices'!B394
    value = 0
    formula = "='Input EIA Crude WTI'!B392"
    @eval_fn
    def B394():
        b392_1 = Input_EIA_Crude_WTI.B392()
        return b392_1

@register(Crude_Oil_Prices)
class C394():
    # 'Crude_Oil_Prices'!C394
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B376"
    @eval_fn
    def C394():
        b376_1 = Input_EIA_Crude_Europe_Brent.B376()
        return b376_1

@register(Crude_Oil_Prices)
class A395():
    # 'Crude_Oil_Prices'!A395
    value = 43296
    isdatetime = True

@register(Crude_Oil_Prices)
class B395():
    # 'Crude_Oil_Prices'!B395
    value = 0
    formula = "='Input EIA Crude WTI'!B393"
    @eval_fn
    def B395():
        b393_1 = Input_EIA_Crude_WTI.B393()
        return b393_1

@register(Crude_Oil_Prices)
class C395():
    # 'Crude_Oil_Prices'!C395
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B377"
    @eval_fn
    def C395():
        b377_1 = Input_EIA_Crude_Europe_Brent.B377()
        return b377_1

@register(Crude_Oil_Prices)
class A396():
    # 'Crude_Oil_Prices'!A396
    value = 43327
    isdatetime = True

@register(Crude_Oil_Prices)
class B396():
    # 'Crude_Oil_Prices'!B396
    value = 0
    formula = "='Input EIA Crude WTI'!B394"
    @eval_fn
    def B396():
        b394_1 = Input_EIA_Crude_WTI.B394()
        return b394_1

@register(Crude_Oil_Prices)
class C396():
    # 'Crude_Oil_Prices'!C396
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B378"
    @eval_fn
    def C396():
        b378_1 = Input_EIA_Crude_Europe_Brent.B378()
        return b378_1

@register(Crude_Oil_Prices)
class A397():
    # 'Crude_Oil_Prices'!A397
    value = 43358
    isdatetime = True

@register(Crude_Oil_Prices)
class B397():
    # 'Crude_Oil_Prices'!B397
    value = 0
    formula = "='Input EIA Crude WTI'!B395"
    @eval_fn
    def B397():
        b395_1 = Input_EIA_Crude_WTI.B395()
        return b395_1

@register(Crude_Oil_Prices)
class C397():
    # 'Crude_Oil_Prices'!C397
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B379"
    @eval_fn
    def C397():
        b379_1 = Input_EIA_Crude_Europe_Brent.B379()
        return b379_1

@register(Crude_Oil_Prices)
class A398():
    # 'Crude_Oil_Prices'!A398
    value = 43388
    isdatetime = True

@register(Crude_Oil_Prices)
class B398():
    # 'Crude_Oil_Prices'!B398
    value = 0
    formula = "='Input EIA Crude WTI'!B396"
    @eval_fn
    def B398():
        b396_1 = Input_EIA_Crude_WTI.B396()
        return b396_1

@register(Crude_Oil_Prices)
class C398():
    # 'Crude_Oil_Prices'!C398
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B380"
    @eval_fn
    def C398():
        b380_1 = Input_EIA_Crude_Europe_Brent.B380()
        return b380_1

@register(Crude_Oil_Prices)
class A399():
    # 'Crude_Oil_Prices'!A399
    value = 43419
    isdatetime = True

@register(Crude_Oil_Prices)
class B399():
    # 'Crude_Oil_Prices'!B399
    value = 0
    formula = "='Input EIA Crude WTI'!B397"
    @eval_fn
    def B399():
        b397_1 = Input_EIA_Crude_WTI.B397()
        return b397_1

@register(Crude_Oil_Prices)
class C399():
    # 'Crude_Oil_Prices'!C399
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B381"
    @eval_fn
    def C399():
        b381_1 = Input_EIA_Crude_Europe_Brent.B381()
        return b381_1

@register(Crude_Oil_Prices)
class A400():
    # 'Crude_Oil_Prices'!A400
    value = 43449
    isdatetime = True

@register(Crude_Oil_Prices)
class B400():
    # 'Crude_Oil_Prices'!B400
    value = 0
    formula = "='Input EIA Crude WTI'!B398"
    @eval_fn
    def B400():
        b398_1 = Input_EIA_Crude_WTI.B398()
        return b398_1

@register(Crude_Oil_Prices)
class C400():
    # 'Crude_Oil_Prices'!C400
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B382"
    @eval_fn
    def C400():
        b382_1 = Input_EIA_Crude_Europe_Brent.B382()
        return b382_1

@register(Crude_Oil_Prices)
class A401():
    # 'Crude_Oil_Prices'!A401
    value = 43480
    isdatetime = True

@register(Crude_Oil_Prices)
class B401():
    # 'Crude_Oil_Prices'!B401
    value = 0
    formula = "='Input EIA Crude WTI'!B399"
    @eval_fn
    def B401():
        b399_1 = Input_EIA_Crude_WTI.B399()
        return b399_1

@register(Crude_Oil_Prices)
class C401():
    # 'Crude_Oil_Prices'!C401
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B383"
    @eval_fn
    def C401():
        b383_1 = Input_EIA_Crude_Europe_Brent.B383()
        return b383_1

@register(Crude_Oil_Prices)
class A402():
    # 'Crude_Oil_Prices'!A402
    value = 43511
    isdatetime = True

@register(Crude_Oil_Prices)
class B402():
    # 'Crude_Oil_Prices'!B402
    value = 0
    formula = "='Input EIA Crude WTI'!B400"
    @eval_fn
    def B402():
        b400_1 = Input_EIA_Crude_WTI.B400()
        return b400_1

@register(Crude_Oil_Prices)
class C402():
    # 'Crude_Oil_Prices'!C402
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B384"
    @eval_fn
    def C402():
        b384_1 = Input_EIA_Crude_Europe_Brent.B384()
        return b384_1

@register(Crude_Oil_Prices)
class A403():
    # 'Crude_Oil_Prices'!A403
    value = 43539
    isdatetime = True

@register(Crude_Oil_Prices)
class B403():
    # 'Crude_Oil_Prices'!B403
    value = 0
    formula = "='Input EIA Crude WTI'!B401"
    @eval_fn
    def B403():
        b401_1 = Input_EIA_Crude_WTI.B401()
        return b401_1

@register(Crude_Oil_Prices)
class C403():
    # 'Crude_Oil_Prices'!C403
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B385"
    @eval_fn
    def C403():
        b385_1 = Input_EIA_Crude_Europe_Brent.B385()
        return b385_1

@register(Crude_Oil_Prices)
class A404():
    # 'Crude_Oil_Prices'!A404
    value = 43570
    isdatetime = True

@register(Crude_Oil_Prices)
class B404():
    # 'Crude_Oil_Prices'!B404
    value = 0
    formula = "='Input EIA Crude WTI'!B402"
    @eval_fn
    def B404():
        b402_1 = Input_EIA_Crude_WTI.B402()
        return b402_1

@register(Crude_Oil_Prices)
class C404():
    # 'Crude_Oil_Prices'!C404
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B386"
    @eval_fn
    def C404():
        b386_1 = Input_EIA_Crude_Europe_Brent.B386()
        return b386_1

@register(Crude_Oil_Prices)
class A405():
    # 'Crude_Oil_Prices'!A405
    value = 43600
    isdatetime = True

@register(Crude_Oil_Prices)
class B405():
    # 'Crude_Oil_Prices'!B405
    value = 0
    formula = "='Input EIA Crude WTI'!B403"
    @eval_fn
    def B405():
        b403_1 = Input_EIA_Crude_WTI.B403()
        return b403_1

@register(Crude_Oil_Prices)
class C405():
    # 'Crude_Oil_Prices'!C405
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B387"
    @eval_fn
    def C405():
        b387_1 = Input_EIA_Crude_Europe_Brent.B387()
        return b387_1

@register(Crude_Oil_Prices)
class A406():
    # 'Crude_Oil_Prices'!A406
    value = 43631
    isdatetime = True

@register(Crude_Oil_Prices)
class B406():
    # 'Crude_Oil_Prices'!B406
    value = 0
    formula = "='Input EIA Crude WTI'!B404"
    @eval_fn
    def B406():
        b404_1 = Input_EIA_Crude_WTI.B404()
        return b404_1

@register(Crude_Oil_Prices)
class C406():
    # 'Crude_Oil_Prices'!C406
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B388"
    @eval_fn
    def C406():
        b388_1 = Input_EIA_Crude_Europe_Brent.B388()
        return b388_1

@register(Crude_Oil_Prices)
class A407():
    # 'Crude_Oil_Prices'!A407
    value = 43661
    isdatetime = True

@register(Crude_Oil_Prices)
class B407():
    # 'Crude_Oil_Prices'!B407
    value = 0
    formula = "='Input EIA Crude WTI'!B405"
    @eval_fn
    def B407():
        b405_1 = Input_EIA_Crude_WTI.B405()
        return b405_1

@register(Crude_Oil_Prices)
class C407():
    # 'Crude_Oil_Prices'!C407
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B389"
    @eval_fn
    def C407():
        b389_1 = Input_EIA_Crude_Europe_Brent.B389()
        return b389_1

@register(Crude_Oil_Prices)
class A408():
    # 'Crude_Oil_Prices'!A408
    value = 43692
    isdatetime = True

@register(Crude_Oil_Prices)
class B408():
    # 'Crude_Oil_Prices'!B408
    value = 0
    formula = "='Input EIA Crude WTI'!B406"
    @eval_fn
    def B408():
        b406_1 = Input_EIA_Crude_WTI.B406()
        return b406_1

@register(Crude_Oil_Prices)
class C408():
    # 'Crude_Oil_Prices'!C408
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B390"
    @eval_fn
    def C408():
        b390_1 = Input_EIA_Crude_Europe_Brent.B390()
        return b390_1

@register(Crude_Oil_Prices)
class A409():
    # 'Crude_Oil_Prices'!A409
    value = 43723
    isdatetime = True

@register(Crude_Oil_Prices)
class B409():
    # 'Crude_Oil_Prices'!B409
    value = 0
    formula = "='Input EIA Crude WTI'!B407"
    @eval_fn
    def B409():
        b407_1 = Input_EIA_Crude_WTI.B407()
        return b407_1

@register(Crude_Oil_Prices)
class C409():
    # 'Crude_Oil_Prices'!C409
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B391"
    @eval_fn
    def C409():
        b391_1 = Input_EIA_Crude_Europe_Brent.B391()
        return b391_1

@register(Crude_Oil_Prices)
class A410():
    # 'Crude_Oil_Prices'!A410
    value = 43753
    isdatetime = True

@register(Crude_Oil_Prices)
class B410():
    # 'Crude_Oil_Prices'!B410
    value = 0
    formula = "='Input EIA Crude WTI'!B408"
    @eval_fn
    def B410():
        b408_1 = Input_EIA_Crude_WTI.B408()
        return b408_1

@register(Crude_Oil_Prices)
class C410():
    # 'Crude_Oil_Prices'!C410
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B392"
    @eval_fn
    def C410():
        b392_1 = Input_EIA_Crude_Europe_Brent.B392()
        return b392_1

@register(Crude_Oil_Prices)
class A411():
    # 'Crude_Oil_Prices'!A411
    value = 43784
    isdatetime = True

@register(Crude_Oil_Prices)
class B411():
    # 'Crude_Oil_Prices'!B411
    value = 0
    formula = "='Input EIA Crude WTI'!B409"
    @eval_fn
    def B411():
        b409_1 = Input_EIA_Crude_WTI.B409()
        return b409_1

@register(Crude_Oil_Prices)
class C411():
    # 'Crude_Oil_Prices'!C411
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B393"
    @eval_fn
    def C411():
        b393_1 = Input_EIA_Crude_Europe_Brent.B393()
        return b393_1

@register(Crude_Oil_Prices)
class A412():
    # 'Crude_Oil_Prices'!A412
    value = 43814
    isdatetime = True

@register(Crude_Oil_Prices)
class B412():
    # 'Crude_Oil_Prices'!B412
    value = 0
    formula = "='Input EIA Crude WTI'!B410"
    @eval_fn
    def B412():
        b410_1 = Input_EIA_Crude_WTI.B410()
        return b410_1

@register(Crude_Oil_Prices)
class C412():
    # 'Crude_Oil_Prices'!C412
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B394"
    @eval_fn
    def C412():
        b394_1 = Input_EIA_Crude_Europe_Brent.B394()
        return b394_1

@register(Crude_Oil_Prices)
class A413():
    # 'Crude_Oil_Prices'!A413
    value = 43845
    isdatetime = True

@register(Crude_Oil_Prices)
class B413():
    # 'Crude_Oil_Prices'!B413
    value = 0
    formula = "='Input EIA Crude WTI'!B411"
    @eval_fn
    def B413():
        b411_1 = Input_EIA_Crude_WTI.B411()
        return b411_1

@register(Crude_Oil_Prices)
class C413():
    # 'Crude_Oil_Prices'!C413
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B395"
    @eval_fn
    def C413():
        b395_1 = Input_EIA_Crude_Europe_Brent.B395()
        return b395_1

@register(Crude_Oil_Prices)
class A414():
    # 'Crude_Oil_Prices'!A414
    value = 43876
    isdatetime = True

@register(Crude_Oil_Prices)
class B414():
    # 'Crude_Oil_Prices'!B414
    value = 0
    formula = "='Input EIA Crude WTI'!B412"
    @eval_fn
    def B414():
        b412_1 = Input_EIA_Crude_WTI.B412()
        return b412_1

@register(Crude_Oil_Prices)
class C414():
    # 'Crude_Oil_Prices'!C414
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B396"
    @eval_fn
    def C414():
        b396_1 = Input_EIA_Crude_Europe_Brent.B396()
        return b396_1

@register(Crude_Oil_Prices)
class A415():
    # 'Crude_Oil_Prices'!A415
    value = 43905
    isdatetime = True

@register(Crude_Oil_Prices)
class B415():
    # 'Crude_Oil_Prices'!B415
    value = 0
    formula = "='Input EIA Crude WTI'!B413"
    @eval_fn
    def B415():
        b413_1 = Input_EIA_Crude_WTI.B413()
        return b413_1

@register(Crude_Oil_Prices)
class C415():
    # 'Crude_Oil_Prices'!C415
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B397"
    @eval_fn
    def C415():
        b397_1 = Input_EIA_Crude_Europe_Brent.B397()
        return b397_1

@register(Crude_Oil_Prices)
class A416():
    # 'Crude_Oil_Prices'!A416
    value = 43936
    isdatetime = True

@register(Crude_Oil_Prices)
class B416():
    # 'Crude_Oil_Prices'!B416
    value = 0
    formula = "='Input EIA Crude WTI'!B414"
    @eval_fn
    def B416():
        b414_1 = Input_EIA_Crude_WTI.B414()
        return b414_1

@register(Crude_Oil_Prices)
class C416():
    # 'Crude_Oil_Prices'!C416
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B398"
    @eval_fn
    def C416():
        b398_1 = Input_EIA_Crude_Europe_Brent.B398()
        return b398_1

@register(Crude_Oil_Prices)
class A417():
    # 'Crude_Oil_Prices'!A417
    value = 43966
    isdatetime = True

@register(Crude_Oil_Prices)
class B417():
    # 'Crude_Oil_Prices'!B417
    value = 0
    formula = "='Input EIA Crude WTI'!B415"
    @eval_fn
    def B417():
        b415_1 = Input_EIA_Crude_WTI.B415()
        return b415_1

@register(Crude_Oil_Prices)
class C417():
    # 'Crude_Oil_Prices'!C417
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B399"
    @eval_fn
    def C417():
        b399_1 = Input_EIA_Crude_Europe_Brent.B399()
        return b399_1

@register(Crude_Oil_Prices)
class A418():
    # 'Crude_Oil_Prices'!A418
    value = 43997
    isdatetime = True

@register(Crude_Oil_Prices)
class B418():
    # 'Crude_Oil_Prices'!B418
    value = 0
    formula = "='Input EIA Crude WTI'!B416"
    @eval_fn
    def B418():
        b416_1 = Input_EIA_Crude_WTI.B416()
        return b416_1

@register(Crude_Oil_Prices)
class C418():
    # 'Crude_Oil_Prices'!C418
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B400"
    @eval_fn
    def C418():
        b400_1 = Input_EIA_Crude_Europe_Brent.B400()
        return b400_1

@register(Crude_Oil_Prices)
class A419():
    # 'Crude_Oil_Prices'!A419
    value = 44027
    isdatetime = True

@register(Crude_Oil_Prices)
class B419():
    # 'Crude_Oil_Prices'!B419
    value = 0
    formula = "='Input EIA Crude WTI'!B417"
    @eval_fn
    def B419():
        b417_1 = Input_EIA_Crude_WTI.B417()
        return b417_1

@register(Crude_Oil_Prices)
class C419():
    # 'Crude_Oil_Prices'!C419
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B401"
    @eval_fn
    def C419():
        b401_1 = Input_EIA_Crude_Europe_Brent.B401()
        return b401_1

@register(Crude_Oil_Prices)
class A420():
    # 'Crude_Oil_Prices'!A420
    value = 44058
    isdatetime = True

@register(Crude_Oil_Prices)
class B420():
    # 'Crude_Oil_Prices'!B420
    value = 0
    formula = "='Input EIA Crude WTI'!B418"
    @eval_fn
    def B420():
        b418_1 = Input_EIA_Crude_WTI.B418()
        return b418_1

@register(Crude_Oil_Prices)
class C420():
    # 'Crude_Oil_Prices'!C420
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B402"
    @eval_fn
    def C420():
        b402_1 = Input_EIA_Crude_Europe_Brent.B402()
        return b402_1

@register(Crude_Oil_Prices)
class A421():
    # 'Crude_Oil_Prices'!A421
    value = 44089
    isdatetime = True

@register(Crude_Oil_Prices)
class B421():
    # 'Crude_Oil_Prices'!B421
    value = 0
    formula = "='Input EIA Crude WTI'!B419"
    @eval_fn
    def B421():
        b419_1 = Input_EIA_Crude_WTI.B419()
        return b419_1

@register(Crude_Oil_Prices)
class C421():
    # 'Crude_Oil_Prices'!C421
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B403"
    @eval_fn
    def C421():
        b403_1 = Input_EIA_Crude_Europe_Brent.B403()
        return b403_1

@register(Crude_Oil_Prices)
class A422():
    # 'Crude_Oil_Prices'!A422
    value = 44119
    isdatetime = True

@register(Crude_Oil_Prices)
class B422():
    # 'Crude_Oil_Prices'!B422
    value = 0
    formula = "='Input EIA Crude WTI'!B420"
    @eval_fn
    def B422():
        b420_1 = Input_EIA_Crude_WTI.B420()
        return b420_1

@register(Crude_Oil_Prices)
class C422():
    # 'Crude_Oil_Prices'!C422
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B404"
    @eval_fn
    def C422():
        b404_1 = Input_EIA_Crude_Europe_Brent.B404()
        return b404_1

@register(Crude_Oil_Prices)
class A423():
    # 'Crude_Oil_Prices'!A423
    value = 44150
    isdatetime = True

@register(Crude_Oil_Prices)
class B423():
    # 'Crude_Oil_Prices'!B423
    value = 0
    formula = "='Input EIA Crude WTI'!B421"
    @eval_fn
    def B423():
        b421_1 = Input_EIA_Crude_WTI.B421()
        return b421_1

@register(Crude_Oil_Prices)
class C423():
    # 'Crude_Oil_Prices'!C423
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B405"
    @eval_fn
    def C423():
        b405_1 = Input_EIA_Crude_Europe_Brent.B405()
        return b405_1

@register(Crude_Oil_Prices)
class A424():
    # 'Crude_Oil_Prices'!A424
    value = 44180
    isdatetime = True

@register(Crude_Oil_Prices)
class B424():
    # 'Crude_Oil_Prices'!B424
    value = 0
    formula = "='Input EIA Crude WTI'!B422"
    @eval_fn
    def B424():
        b422_1 = Input_EIA_Crude_WTI.B422()
        return b422_1

@register(Crude_Oil_Prices)
class C424():
    # 'Crude_Oil_Prices'!C424
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B406"
    @eval_fn
    def C424():
        b406_1 = Input_EIA_Crude_Europe_Brent.B406()
        return b406_1

@register(Crude_Oil_Prices)
class A425():
    # 'Crude_Oil_Prices'!A425
    value = 44211
    isdatetime = True

@register(Crude_Oil_Prices)
class B425():
    # 'Crude_Oil_Prices'!B425
    value = 0
    formula = "='Input EIA Crude WTI'!B423"
    @eval_fn
    def B425():
        b423_1 = Input_EIA_Crude_WTI.B423()
        return b423_1

@register(Crude_Oil_Prices)
class C425():
    # 'Crude_Oil_Prices'!C425
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B407"
    @eval_fn
    def C425():
        b407_1 = Input_EIA_Crude_Europe_Brent.B407()
        return b407_1

@register(Crude_Oil_Prices)
class A426():
    # 'Crude_Oil_Prices'!A426
    value = 44242
    isdatetime = True

@register(Crude_Oil_Prices)
class B426():
    # 'Crude_Oil_Prices'!B426
    value = 0
    formula = "='Input EIA Crude WTI'!B424"
    @eval_fn
    def B426():
        b424_1 = Input_EIA_Crude_WTI.B424()
        return b424_1

@register(Crude_Oil_Prices)
class C426():
    # 'Crude_Oil_Prices'!C426
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B408"
    @eval_fn
    def C426():
        b408_1 = Input_EIA_Crude_Europe_Brent.B408()
        return b408_1

@register(Crude_Oil_Prices)
class A427():
    # 'Crude_Oil_Prices'!A427
    value = 44270
    isdatetime = True

@register(Crude_Oil_Prices)
class B427():
    # 'Crude_Oil_Prices'!B427
    value = 0
    formula = "='Input EIA Crude WTI'!B425"
    @eval_fn
    def B427():
        b425_1 = Input_EIA_Crude_WTI.B425()
        return b425_1

@register(Crude_Oil_Prices)
class C427():
    # 'Crude_Oil_Prices'!C427
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B409"
    @eval_fn
    def C427():
        b409_1 = Input_EIA_Crude_Europe_Brent.B409()
        return b409_1

@register(Crude_Oil_Prices)
class A428():
    # 'Crude_Oil_Prices'!A428
    value = 44301
    isdatetime = True

@register(Crude_Oil_Prices)
class B428():
    # 'Crude_Oil_Prices'!B428
    value = 0
    formula = "='Input EIA Crude WTI'!B426"
    @eval_fn
    def B428():
        b426_1 = Input_EIA_Crude_WTI.B426()
        return b426_1

@register(Crude_Oil_Prices)
class C428():
    # 'Crude_Oil_Prices'!C428
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B410"
    @eval_fn
    def C428():
        b410_1 = Input_EIA_Crude_Europe_Brent.B410()
        return b410_1

@register(Crude_Oil_Prices)
class A429():
    # 'Crude_Oil_Prices'!A429
    value = 44331
    isdatetime = True

@register(Crude_Oil_Prices)
class B429():
    # 'Crude_Oil_Prices'!B429
    value = 0
    formula = "='Input EIA Crude WTI'!B427"
    @eval_fn
    def B429():
        b427_1 = Input_EIA_Crude_WTI.B427()
        return b427_1

@register(Crude_Oil_Prices)
class C429():
    # 'Crude_Oil_Prices'!C429
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B411"
    @eval_fn
    def C429():
        b411_1 = Input_EIA_Crude_Europe_Brent.B411()
        return b411_1

@register(Crude_Oil_Prices)
class A430():
    # 'Crude_Oil_Prices'!A430
    value = 44362
    isdatetime = True

@register(Crude_Oil_Prices)
class B430():
    # 'Crude_Oil_Prices'!B430
    value = 0
    formula = "='Input EIA Crude WTI'!B428"
    @eval_fn
    def B430():
        b428_1 = Input_EIA_Crude_WTI.B428()
        return b428_1

@register(Crude_Oil_Prices)
class C430():
    # 'Crude_Oil_Prices'!C430
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B412"
    @eval_fn
    def C430():
        b412_1 = Input_EIA_Crude_Europe_Brent.B412()
        return b412_1

@register(Crude_Oil_Prices)
class A431():
    # 'Crude_Oil_Prices'!A431
    value = 44392
    isdatetime = True

@register(Crude_Oil_Prices)
class B431():
    # 'Crude_Oil_Prices'!B431
    value = 0
    formula = "='Input EIA Crude WTI'!B429"
    @eval_fn
    def B431():
        b429_1 = Input_EIA_Crude_WTI.B429()
        return b429_1

@register(Crude_Oil_Prices)
class C431():
    # 'Crude_Oil_Prices'!C431
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B413"
    @eval_fn
    def C431():
        b413_1 = Input_EIA_Crude_Europe_Brent.B413()
        return b413_1

@register(Crude_Oil_Prices)
class A432():
    # 'Crude_Oil_Prices'!A432
    value = 44423
    isdatetime = True

@register(Crude_Oil_Prices)
class B432():
    # 'Crude_Oil_Prices'!B432
    value = 0
    formula = "='Input EIA Crude WTI'!B430"
    @eval_fn
    def B432():
        b430_1 = Input_EIA_Crude_WTI.B430()
        return b430_1

@register(Crude_Oil_Prices)
class C432():
    # 'Crude_Oil_Prices'!C432
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B414"
    @eval_fn
    def C432():
        b414_1 = Input_EIA_Crude_Europe_Brent.B414()
        return b414_1

@register(Crude_Oil_Prices)
class A433():
    # 'Crude_Oil_Prices'!A433
    value = 44454
    isdatetime = True

@register(Crude_Oil_Prices)
class B433():
    # 'Crude_Oil_Prices'!B433
    value = 0
    formula = "='Input EIA Crude WTI'!B431"
    @eval_fn
    def B433():
        b431_1 = Input_EIA_Crude_WTI.B431()
        return b431_1

@register(Crude_Oil_Prices)
class C433():
    # 'Crude_Oil_Prices'!C433
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B415"
    @eval_fn
    def C433():
        b415_1 = Input_EIA_Crude_Europe_Brent.B415()
        return b415_1

@register(Crude_Oil_Prices)
class A434():
    # 'Crude_Oil_Prices'!A434
    value = 44484
    isdatetime = True

@register(Crude_Oil_Prices)
class B434():
    # 'Crude_Oil_Prices'!B434
    value = 0
    formula = "='Input EIA Crude WTI'!B432"
    @eval_fn
    def B434():
        b432_1 = Input_EIA_Crude_WTI.B432()
        return b432_1

@register(Crude_Oil_Prices)
class C434():
    # 'Crude_Oil_Prices'!C434
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B416"
    @eval_fn
    def C434():
        b416_1 = Input_EIA_Crude_Europe_Brent.B416()
        return b416_1

@register(Crude_Oil_Prices)
class A435():
    # 'Crude_Oil_Prices'!A435
    value = 44515
    isdatetime = True

@register(Crude_Oil_Prices)
class B435():
    # 'Crude_Oil_Prices'!B435
    value = 0
    formula = "='Input EIA Crude WTI'!B433"
    @eval_fn
    def B435():
        b433_1 = Input_EIA_Crude_WTI.B433()
        return b433_1

@register(Crude_Oil_Prices)
class C435():
    # 'Crude_Oil_Prices'!C435
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B417"
    @eval_fn
    def C435():
        b417_1 = Input_EIA_Crude_Europe_Brent.B417()
        return b417_1

@register(Crude_Oil_Prices)
class A436():
    # 'Crude_Oil_Prices'!A436
    value = 44545
    isdatetime = True

@register(Crude_Oil_Prices)
class B436():
    # 'Crude_Oil_Prices'!B436
    value = 0
    formula = "='Input EIA Crude WTI'!B434"
    @eval_fn
    def B436():
        b434_1 = Input_EIA_Crude_WTI.B434()
        return b434_1

@register(Crude_Oil_Prices)
class C436():
    # 'Crude_Oil_Prices'!C436
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B418"
    @eval_fn
    def C436():
        b418_1 = Input_EIA_Crude_Europe_Brent.B418()
        return b418_1

@register(Crude_Oil_Prices)
class A437():
    # 'Crude_Oil_Prices'!A437
    value = 44576
    isdatetime = True

@register(Crude_Oil_Prices)
class B437():
    # 'Crude_Oil_Prices'!B437
    value = 0
    formula = "='Input EIA Crude WTI'!B435"
    @eval_fn
    def B437():
        b435_1 = Input_EIA_Crude_WTI.B435()
        return b435_1

@register(Crude_Oil_Prices)
class C437():
    # 'Crude_Oil_Prices'!C437
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B419"
    @eval_fn
    def C437():
        b419_1 = Input_EIA_Crude_Europe_Brent.B419()
        return b419_1

@register(Crude_Oil_Prices)
class A438():
    # 'Crude_Oil_Prices'!A438
    value = 44607
    isdatetime = True

@register(Crude_Oil_Prices)
class B438():
    # 'Crude_Oil_Prices'!B438
    value = 0
    formula = "='Input EIA Crude WTI'!B436"
    @eval_fn
    def B438():
        b436_1 = Input_EIA_Crude_WTI.B436()
        return b436_1

@register(Crude_Oil_Prices)
class C438():
    # 'Crude_Oil_Prices'!C438
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B420"
    @eval_fn
    def C438():
        b420_1 = Input_EIA_Crude_Europe_Brent.B420()
        return b420_1

@register(Crude_Oil_Prices)
class A439():
    # 'Crude_Oil_Prices'!A439
    value = 44635
    isdatetime = True

@register(Crude_Oil_Prices)
class B439():
    # 'Crude_Oil_Prices'!B439
    value = 0
    formula = "='Input EIA Crude WTI'!B437"
    @eval_fn
    def B439():
        b437_1 = Input_EIA_Crude_WTI.B437()
        return b437_1

@register(Crude_Oil_Prices)
class C439():
    # 'Crude_Oil_Prices'!C439
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B421"
    @eval_fn
    def C439():
        b421_1 = Input_EIA_Crude_Europe_Brent.B421()
        return b421_1

@register(Crude_Oil_Prices)
class A440():
    # 'Crude_Oil_Prices'!A440
    value = 44666
    isdatetime = True

@register(Crude_Oil_Prices)
class B440():
    # 'Crude_Oil_Prices'!B440
    value = 0
    formula = "='Input EIA Crude WTI'!B438"
    @eval_fn
    def B440():
        b438_1 = Input_EIA_Crude_WTI.B438()
        return b438_1

@register(Crude_Oil_Prices)
class C440():
    # 'Crude_Oil_Prices'!C440
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B422"
    @eval_fn
    def C440():
        b422_1 = Input_EIA_Crude_Europe_Brent.B422()
        return b422_1

@register(Crude_Oil_Prices)
class A441():
    # 'Crude_Oil_Prices'!A441
    value = 44696
    isdatetime = True

@register(Crude_Oil_Prices)
class B441():
    # 'Crude_Oil_Prices'!B441
    value = 0
    formula = "='Input EIA Crude WTI'!B439"
    @eval_fn
    def B441():
        b439_1 = Input_EIA_Crude_WTI.B439()
        return b439_1

@register(Crude_Oil_Prices)
class C441():
    # 'Crude_Oil_Prices'!C441
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B423"
    @eval_fn
    def C441():
        b423_1 = Input_EIA_Crude_Europe_Brent.B423()
        return b423_1

@register(Crude_Oil_Prices)
class A442():
    # 'Crude_Oil_Prices'!A442
    value = 44727
    isdatetime = True

@register(Crude_Oil_Prices)
class B442():
    # 'Crude_Oil_Prices'!B442
    value = 0
    formula = "='Input EIA Crude WTI'!B440"
    @eval_fn
    def B442():
        b440_1 = Input_EIA_Crude_WTI.B440()
        return b440_1

@register(Crude_Oil_Prices)
class C442():
    # 'Crude_Oil_Prices'!C442
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B424"
    @eval_fn
    def C442():
        b424_1 = Input_EIA_Crude_Europe_Brent.B424()
        return b424_1

@register(Crude_Oil_Prices)
class A443():
    # 'Crude_Oil_Prices'!A443
    value = 44757
    isdatetime = True

@register(Crude_Oil_Prices)
class B443():
    # 'Crude_Oil_Prices'!B443
    value = 0
    formula = "='Input EIA Crude WTI'!B441"
    @eval_fn
    def B443():
        b441_1 = Input_EIA_Crude_WTI.B441()
        return b441_1

@register(Crude_Oil_Prices)
class C443():
    # 'Crude_Oil_Prices'!C443
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B425"
    @eval_fn
    def C443():
        b425_1 = Input_EIA_Crude_Europe_Brent.B425()
        return b425_1

@register(Crude_Oil_Prices)
class A444():
    # 'Crude_Oil_Prices'!A444
    value = 44788
    isdatetime = True

@register(Crude_Oil_Prices)
class B444():
    # 'Crude_Oil_Prices'!B444
    value = 0
    formula = "='Input EIA Crude WTI'!B442"
    @eval_fn
    def B444():
        b442_1 = Input_EIA_Crude_WTI.B442()
        return b442_1

@register(Crude_Oil_Prices)
class C444():
    # 'Crude_Oil_Prices'!C444
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B426"
    @eval_fn
    def C444():
        b426_1 = Input_EIA_Crude_Europe_Brent.B426()
        return b426_1

@register(Crude_Oil_Prices)
class A445():
    # 'Crude_Oil_Prices'!A445
    value = 44819
    isdatetime = True

@register(Crude_Oil_Prices)
class B445():
    # 'Crude_Oil_Prices'!B445
    value = 0
    formula = "='Input EIA Crude WTI'!B443"
    @eval_fn
    def B445():
        b443_1 = Input_EIA_Crude_WTI.B443()
        return b443_1

@register(Crude_Oil_Prices)
class C445():
    # 'Crude_Oil_Prices'!C445
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B427"
    @eval_fn
    def C445():
        b427_1 = Input_EIA_Crude_Europe_Brent.B427()
        return b427_1

@register(Crude_Oil_Prices)
class A446():
    # 'Crude_Oil_Prices'!A446
    value = 44849
    isdatetime = True

@register(Crude_Oil_Prices)
class B446():
    # 'Crude_Oil_Prices'!B446
    value = 0
    formula = "='Input EIA Crude WTI'!B444"
    @eval_fn
    def B446():
        b444_1 = Input_EIA_Crude_WTI.B444()
        return b444_1

@register(Crude_Oil_Prices)
class C446():
    # 'Crude_Oil_Prices'!C446
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B428"
    @eval_fn
    def C446():
        b428_1 = Input_EIA_Crude_Europe_Brent.B428()
        return b428_1

@register(Crude_Oil_Prices)
class A447():
    # 'Crude_Oil_Prices'!A447
    value = 44880
    isdatetime = True

@register(Crude_Oil_Prices)
class B447():
    # 'Crude_Oil_Prices'!B447
    value = 0
    formula = "='Input EIA Crude WTI'!B445"
    @eval_fn
    def B447():
        b445_1 = Input_EIA_Crude_WTI.B445()
        return b445_1

@register(Crude_Oil_Prices)
class C447():
    # 'Crude_Oil_Prices'!C447
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B429"
    @eval_fn
    def C447():
        b429_1 = Input_EIA_Crude_Europe_Brent.B429()
        return b429_1

@register(Crude_Oil_Prices)
class A448():
    # 'Crude_Oil_Prices'!A448
    value = 44910
    isdatetime = True

@register(Crude_Oil_Prices)
class B448():
    # 'Crude_Oil_Prices'!B448
    value = 0
    formula = "='Input EIA Crude WTI'!B446"
    @eval_fn
    def B448():
        b446_1 = Input_EIA_Crude_WTI.B446()
        return b446_1

@register(Crude_Oil_Prices)
class C448():
    # 'Crude_Oil_Prices'!C448
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B430"
    @eval_fn
    def C448():
        b430_1 = Input_EIA_Crude_Europe_Brent.B430()
        return b430_1

@register(Crude_Oil_Prices)
class A449():
    # 'Crude_Oil_Prices'!A449
    value = 44941
    isdatetime = True

@register(Crude_Oil_Prices)
class B449():
    # 'Crude_Oil_Prices'!B449
    value = 0
    formula = "='Input EIA Crude WTI'!B447"
    @eval_fn
    def B449():
        b447_1 = Input_EIA_Crude_WTI.B447()
        return b447_1

@register(Crude_Oil_Prices)
class C449():
    # 'Crude_Oil_Prices'!C449
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B431"
    @eval_fn
    def C449():
        b431_1 = Input_EIA_Crude_Europe_Brent.B431()
        return b431_1

@register(Crude_Oil_Prices)
class A450():
    # 'Crude_Oil_Prices'!A450
    value = 44972
    isdatetime = True

@register(Crude_Oil_Prices)
class B450():
    # 'Crude_Oil_Prices'!B450
    value = 0
    formula = "='Input EIA Crude WTI'!B448"
    @eval_fn
    def B450():
        b448_1 = Input_EIA_Crude_WTI.B448()
        return b448_1

@register(Crude_Oil_Prices)
class C450():
    # 'Crude_Oil_Prices'!C450
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B432"
    @eval_fn
    def C450():
        b432_1 = Input_EIA_Crude_Europe_Brent.B432()
        return b432_1

@register(Crude_Oil_Prices)
class A451():
    # 'Crude_Oil_Prices'!A451
    value = 45000
    isdatetime = True

@register(Crude_Oil_Prices)
class B451():
    # 'Crude_Oil_Prices'!B451
    value = 0
    formula = "='Input EIA Crude WTI'!B449"
    @eval_fn
    def B451():
        b449_1 = Input_EIA_Crude_WTI.B449()
        return b449_1

@register(Crude_Oil_Prices)
class C451():
    # 'Crude_Oil_Prices'!C451
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B433"
    @eval_fn
    def C451():
        b433_1 = Input_EIA_Crude_Europe_Brent.B433()
        return b433_1

@register(Crude_Oil_Prices)
class A452():
    # 'Crude_Oil_Prices'!A452
    value = 45031
    isdatetime = True

@register(Crude_Oil_Prices)
class B452():
    # 'Crude_Oil_Prices'!B452
    value = 0
    formula = "='Input EIA Crude WTI'!B450"
    @eval_fn
    def B452():
        b450_1 = Input_EIA_Crude_WTI.B450()
        return b450_1

@register(Crude_Oil_Prices)
class C452():
    # 'Crude_Oil_Prices'!C452
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B434"
    @eval_fn
    def C452():
        b434_1 = Input_EIA_Crude_Europe_Brent.B434()
        return b434_1

@register(Crude_Oil_Prices)
class A453():
    # 'Crude_Oil_Prices'!A453
    value = 45061
    isdatetime = True

@register(Crude_Oil_Prices)
class B453():
    # 'Crude_Oil_Prices'!B453
    value = 0
    formula = "='Input EIA Crude WTI'!B451"
    @eval_fn
    def B453():
        b451_1 = Input_EIA_Crude_WTI.B451()
        return b451_1

@register(Crude_Oil_Prices)
class C453():
    # 'Crude_Oil_Prices'!C453
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B435"
    @eval_fn
    def C453():
        b435_1 = Input_EIA_Crude_Europe_Brent.B435()
        return b435_1

@register(Crude_Oil_Prices)
class A454():
    # 'Crude_Oil_Prices'!A454
    value = 45092
    isdatetime = True

@register(Crude_Oil_Prices)
class B454():
    # 'Crude_Oil_Prices'!B454
    value = 0
    formula = "='Input EIA Crude WTI'!B452"
    @eval_fn
    def B454():
        b452_1 = Input_EIA_Crude_WTI.B452()
        return b452_1

@register(Crude_Oil_Prices)
class C454():
    # 'Crude_Oil_Prices'!C454
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B436"
    @eval_fn
    def C454():
        b436_1 = Input_EIA_Crude_Europe_Brent.B436()
        return b436_1

@register(Crude_Oil_Prices)
class A455():
    # 'Crude_Oil_Prices'!A455
    value = 45122
    isdatetime = True

@register(Crude_Oil_Prices)
class B455():
    # 'Crude_Oil_Prices'!B455
    value = 0
    formula = "='Input EIA Crude WTI'!B453"
    @eval_fn
    def B455():
        b453_1 = Input_EIA_Crude_WTI.B453()
        return b453_1

@register(Crude_Oil_Prices)
class C455():
    # 'Crude_Oil_Prices'!C455
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B437"
    @eval_fn
    def C455():
        b437_1 = Input_EIA_Crude_Europe_Brent.B437()
        return b437_1

@register(Crude_Oil_Prices)
class A456():
    # 'Crude_Oil_Prices'!A456
    value = 45153
    isdatetime = True

@register(Crude_Oil_Prices)
class B456():
    # 'Crude_Oil_Prices'!B456
    value = 0
    formula = "='Input EIA Crude WTI'!B454"
    @eval_fn
    def B456():
        b454_1 = Input_EIA_Crude_WTI.B454()
        return b454_1

@register(Crude_Oil_Prices)
class C456():
    # 'Crude_Oil_Prices'!C456
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B438"
    @eval_fn
    def C456():
        b438_1 = Input_EIA_Crude_Europe_Brent.B438()
        return b438_1

@register(Crude_Oil_Prices)
class A457():
    # 'Crude_Oil_Prices'!A457
    value = 45184
    isdatetime = True

@register(Crude_Oil_Prices)
class B457():
    # 'Crude_Oil_Prices'!B457
    value = 0
    formula = "='Input EIA Crude WTI'!B455"
    @eval_fn
    def B457():
        b455_1 = Input_EIA_Crude_WTI.B455()
        return b455_1

@register(Crude_Oil_Prices)
class C457():
    # 'Crude_Oil_Prices'!C457
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B439"
    @eval_fn
    def C457():
        b439_1 = Input_EIA_Crude_Europe_Brent.B439()
        return b439_1

@register(Crude_Oil_Prices)
class A458():
    # 'Crude_Oil_Prices'!A458
    value = 45214
    isdatetime = True

@register(Crude_Oil_Prices)
class B458():
    # 'Crude_Oil_Prices'!B458
    value = 0
    formula = "='Input EIA Crude WTI'!B456"
    @eval_fn
    def B458():
        b456_1 = Input_EIA_Crude_WTI.B456()
        return b456_1

@register(Crude_Oil_Prices)
class C458():
    # 'Crude_Oil_Prices'!C458
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B440"
    @eval_fn
    def C458():
        b440_1 = Input_EIA_Crude_Europe_Brent.B440()
        return b440_1

@register(Crude_Oil_Prices)
class A459():
    # 'Crude_Oil_Prices'!A459
    value = 45245
    isdatetime = True

@register(Crude_Oil_Prices)
class B459():
    # 'Crude_Oil_Prices'!B459
    value = 0
    formula = "='Input EIA Crude WTI'!B457"
    @eval_fn
    def B459():
        b457_1 = Input_EIA_Crude_WTI.B457()
        return b457_1

@register(Crude_Oil_Prices)
class C459():
    # 'Crude_Oil_Prices'!C459
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B441"
    @eval_fn
    def C459():
        b441_1 = Input_EIA_Crude_Europe_Brent.B441()
        return b441_1

@register(Crude_Oil_Prices)
class A460():
    # 'Crude_Oil_Prices'!A460
    value = 45275
    isdatetime = True

@register(Crude_Oil_Prices)
class B460():
    # 'Crude_Oil_Prices'!B460
    value = 0
    formula = "='Input EIA Crude WTI'!B458"
    @eval_fn
    def B460():
        b458_1 = Input_EIA_Crude_WTI.B458()
        return b458_1

@register(Crude_Oil_Prices)
class C460():
    # 'Crude_Oil_Prices'!C460
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B442"
    @eval_fn
    def C460():
        b442_1 = Input_EIA_Crude_Europe_Brent.B442()
        return b442_1

@register(Crude_Oil_Prices)
class A461():
    # 'Crude_Oil_Prices'!A461
    value = 45306
    isdatetime = True

@register(Crude_Oil_Prices)
class B461():
    # 'Crude_Oil_Prices'!B461
    value = 0
    formula = "='Input EIA Crude WTI'!B459"
    @eval_fn
    def B461():
        b459_1 = Input_EIA_Crude_WTI.B459()
        return b459_1

@register(Crude_Oil_Prices)
class C461():
    # 'Crude_Oil_Prices'!C461
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B443"
    @eval_fn
    def C461():
        b443_1 = Input_EIA_Crude_Europe_Brent.B443()
        return b443_1

@register(Crude_Oil_Prices)
class A462():
    # 'Crude_Oil_Prices'!A462
    value = 45337
    isdatetime = True

@register(Crude_Oil_Prices)
class B462():
    # 'Crude_Oil_Prices'!B462
    value = 0
    formula = "='Input EIA Crude WTI'!B460"
    @eval_fn
    def B462():
        b460_1 = Input_EIA_Crude_WTI.B460()
        return b460_1

@register(Crude_Oil_Prices)
class C462():
    # 'Crude_Oil_Prices'!C462
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B444"
    @eval_fn
    def C462():
        b444_1 = Input_EIA_Crude_Europe_Brent.B444()
        return b444_1

@register(Crude_Oil_Prices)
class A463():
    # 'Crude_Oil_Prices'!A463
    value = 45366
    isdatetime = True

@register(Crude_Oil_Prices)
class B463():
    # 'Crude_Oil_Prices'!B463
    value = 0
    formula = "='Input EIA Crude WTI'!B461"
    @eval_fn
    def B463():
        b461_1 = Input_EIA_Crude_WTI.B461()
        return b461_1

@register(Crude_Oil_Prices)
class C463():
    # 'Crude_Oil_Prices'!C463
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B445"
    @eval_fn
    def C463():
        b445_1 = Input_EIA_Crude_Europe_Brent.B445()
        return b445_1

@register(Crude_Oil_Prices)
class A464():
    # 'Crude_Oil_Prices'!A464
    value = 45397
    isdatetime = True

@register(Crude_Oil_Prices)
class B464():
    # 'Crude_Oil_Prices'!B464
    value = 0
    formula = "='Input EIA Crude WTI'!B462"
    @eval_fn
    def B464():
        b462_1 = Input_EIA_Crude_WTI.B462()
        return b462_1

@register(Crude_Oil_Prices)
class C464():
    # 'Crude_Oil_Prices'!C464
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B446"
    @eval_fn
    def C464():
        b446_1 = Input_EIA_Crude_Europe_Brent.B446()
        return b446_1

@register(Crude_Oil_Prices)
class A465():
    # 'Crude_Oil_Prices'!A465
    value = 45427
    isdatetime = True

@register(Crude_Oil_Prices)
class B465():
    # 'Crude_Oil_Prices'!B465
    value = 0
    formula = "='Input EIA Crude WTI'!B463"
    @eval_fn
    def B465():
        b463_1 = Input_EIA_Crude_WTI.B463()
        return b463_1

@register(Crude_Oil_Prices)
class C465():
    # 'Crude_Oil_Prices'!C465
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B447"
    @eval_fn
    def C465():
        b447_1 = Input_EIA_Crude_Europe_Brent.B447()
        return b447_1

@register(Crude_Oil_Prices)
class A466():
    # 'Crude_Oil_Prices'!A466
    value = 45458
    isdatetime = True

@register(Crude_Oil_Prices)
class B466():
    # 'Crude_Oil_Prices'!B466
    value = 0
    formula = "='Input EIA Crude WTI'!B464"
    @eval_fn
    def B466():
        b464_1 = Input_EIA_Crude_WTI.B464()
        return b464_1

@register(Crude_Oil_Prices)
class C466():
    # 'Crude_Oil_Prices'!C466
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B448"
    @eval_fn
    def C466():
        b448_1 = Input_EIA_Crude_Europe_Brent.B448()
        return b448_1

@register(Crude_Oil_Prices)
class A467():
    # 'Crude_Oil_Prices'!A467
    value = 45488
    isdatetime = True

@register(Crude_Oil_Prices)
class B467():
    # 'Crude_Oil_Prices'!B467
    value = 0
    formula = "='Input EIA Crude WTI'!B465"
    @eval_fn
    def B467():
        b465_1 = Input_EIA_Crude_WTI.B465()
        return b465_1

@register(Crude_Oil_Prices)
class C467():
    # 'Crude_Oil_Prices'!C467
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B449"
    @eval_fn
    def C467():
        b449_1 = Input_EIA_Crude_Europe_Brent.B449()
        return b449_1

@register(Crude_Oil_Prices)
class A468():
    # 'Crude_Oil_Prices'!A468
    value = 45519
    isdatetime = True

@register(Crude_Oil_Prices)
class B468():
    # 'Crude_Oil_Prices'!B468
    value = 0
    formula = "='Input EIA Crude WTI'!B466"
    @eval_fn
    def B468():
        b466_1 = Input_EIA_Crude_WTI.B466()
        return b466_1

@register(Crude_Oil_Prices)
class C468():
    # 'Crude_Oil_Prices'!C468
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B450"
    @eval_fn
    def C468():
        b450_1 = Input_EIA_Crude_Europe_Brent.B450()
        return b450_1

@register(Crude_Oil_Prices)
class A469():
    # 'Crude_Oil_Prices'!A469
    value = 45550
    isdatetime = True

@register(Crude_Oil_Prices)
class B469():
    # 'Crude_Oil_Prices'!B469
    value = 0
    formula = "='Input EIA Crude WTI'!B467"
    @eval_fn
    def B469():
        b467_1 = Input_EIA_Crude_WTI.B467()
        return b467_1

@register(Crude_Oil_Prices)
class C469():
    # 'Crude_Oil_Prices'!C469
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B451"
    @eval_fn
    def C469():
        b451_1 = Input_EIA_Crude_Europe_Brent.B451()
        return b451_1

@register(Crude_Oil_Prices)
class A470():
    # 'Crude_Oil_Prices'!A470
    value = 45580
    isdatetime = True

@register(Crude_Oil_Prices)
class B470():
    # 'Crude_Oil_Prices'!B470
    value = 0
    formula = "='Input EIA Crude WTI'!B468"
    @eval_fn
    def B470():
        b468_1 = Input_EIA_Crude_WTI.B468()
        return b468_1

@register(Crude_Oil_Prices)
class C470():
    # 'Crude_Oil_Prices'!C470
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B452"
    @eval_fn
    def C470():
        b452_1 = Input_EIA_Crude_Europe_Brent.B452()
        return b452_1

@register(Crude_Oil_Prices)
class A471():
    # 'Crude_Oil_Prices'!A471
    value = 45611
    isdatetime = True

@register(Crude_Oil_Prices)
class B471():
    # 'Crude_Oil_Prices'!B471
    value = 0
    formula = "='Input EIA Crude WTI'!B469"
    @eval_fn
    def B471():
        b469_1 = Input_EIA_Crude_WTI.B469()
        return b469_1

@register(Crude_Oil_Prices)
class C471():
    # 'Crude_Oil_Prices'!C471
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B453"
    @eval_fn
    def C471():
        b453_1 = Input_EIA_Crude_Europe_Brent.B453()
        return b453_1

@register(Crude_Oil_Prices)
class A472():
    # 'Crude_Oil_Prices'!A472
    value = 45641
    isdatetime = True

@register(Crude_Oil_Prices)
class B472():
    # 'Crude_Oil_Prices'!B472
    value = 0
    formula = "='Input EIA Crude WTI'!B470"
    @eval_fn
    def B472():
        b470_1 = Input_EIA_Crude_WTI.B470()
        return b470_1

@register(Crude_Oil_Prices)
class C472():
    # 'Crude_Oil_Prices'!C472
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B454"
    @eval_fn
    def C472():
        b454_1 = Input_EIA_Crude_Europe_Brent.B454()
        return b454_1

@register(Crude_Oil_Prices)
class A473():
    # 'Crude_Oil_Prices'!A473
    value = 45672
    isdatetime = True

@register(Crude_Oil_Prices)
class B473():
    # 'Crude_Oil_Prices'!B473
    value = 0
    formula = "='Input EIA Crude WTI'!B471"
    @eval_fn
    def B473():
        b471_1 = Input_EIA_Crude_WTI.B471()
        return b471_1

@register(Crude_Oil_Prices)
class C473():
    # 'Crude_Oil_Prices'!C473
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B455"
    @eval_fn
    def C473():
        b455_1 = Input_EIA_Crude_Europe_Brent.B455()
        return b455_1

@register(Crude_Oil_Prices)
class A474():
    # 'Crude_Oil_Prices'!A474
    value = 45703
    isdatetime = True

@register(Crude_Oil_Prices)
class B474():
    # 'Crude_Oil_Prices'!B474
    value = 0
    formula = "='Input EIA Crude WTI'!B472"
    @eval_fn
    def B474():
        b472_1 = Input_EIA_Crude_WTI.B472()
        return b472_1

@register(Crude_Oil_Prices)
class C474():
    # 'Crude_Oil_Prices'!C474
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B456"
    @eval_fn
    def C474():
        b456_1 = Input_EIA_Crude_Europe_Brent.B456()
        return b456_1

@register(Crude_Oil_Prices)
class A475():
    # 'Crude_Oil_Prices'!A475
    value = 45731
    isdatetime = True

@register(Crude_Oil_Prices)
class B475():
    # 'Crude_Oil_Prices'!B475
    value = 0
    formula = "='Input EIA Crude WTI'!B473"
    @eval_fn
    def B475():
        b473_1 = Input_EIA_Crude_WTI.B473()
        return b473_1

@register(Crude_Oil_Prices)
class C475():
    # 'Crude_Oil_Prices'!C475
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B457"
    @eval_fn
    def C475():
        b457_1 = Input_EIA_Crude_Europe_Brent.B457()
        return b457_1

@register(Crude_Oil_Prices)
class A476():
    # 'Crude_Oil_Prices'!A476
    value = 45762
    isdatetime = True

@register(Crude_Oil_Prices)
class B476():
    # 'Crude_Oil_Prices'!B476
    value = 0
    formula = "='Input EIA Crude WTI'!B474"
    @eval_fn
    def B476():
        b474_1 = Input_EIA_Crude_WTI.B474()
        return b474_1

@register(Crude_Oil_Prices)
class C476():
    # 'Crude_Oil_Prices'!C476
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B458"
    @eval_fn
    def C476():
        b458_1 = Input_EIA_Crude_Europe_Brent.B458()
        return b458_1

@register(Crude_Oil_Prices)
class A477():
    # 'Crude_Oil_Prices'!A477
    value = 45792
    isdatetime = True

@register(Crude_Oil_Prices)
class B477():
    # 'Crude_Oil_Prices'!B477
    value = 0
    formula = "='Input EIA Crude WTI'!B475"
    @eval_fn
    def B477():
        b475_1 = Input_EIA_Crude_WTI.B475()
        return b475_1

@register(Crude_Oil_Prices)
class C477():
    # 'Crude_Oil_Prices'!C477
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B459"
    @eval_fn
    def C477():
        b459_1 = Input_EIA_Crude_Europe_Brent.B459()
        return b459_1

@register(Crude_Oil_Prices)
class A478():
    # 'Crude_Oil_Prices'!A478
    value = 45823
    isdatetime = True

@register(Crude_Oil_Prices)
class B478():
    # 'Crude_Oil_Prices'!B478
    value = 0
    formula = "='Input EIA Crude WTI'!B476"
    @eval_fn
    def B478():
        b476_1 = Input_EIA_Crude_WTI.B476()
        return b476_1

@register(Crude_Oil_Prices)
class C478():
    # 'Crude_Oil_Prices'!C478
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B460"
    @eval_fn
    def C478():
        b460_1 = Input_EIA_Crude_Europe_Brent.B460()
        return b460_1

@register(Crude_Oil_Prices)
class A479():
    # 'Crude_Oil_Prices'!A479
    value = 45853
    isdatetime = True

@register(Crude_Oil_Prices)
class B479():
    # 'Crude_Oil_Prices'!B479
    value = 0
    formula = "='Input EIA Crude WTI'!B477"
    @eval_fn
    def B479():
        b477_1 = Input_EIA_Crude_WTI.B477()
        return b477_1

@register(Crude_Oil_Prices)
class C479():
    # 'Crude_Oil_Prices'!C479
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B461"
    @eval_fn
    def C479():
        b461_1 = Input_EIA_Crude_Europe_Brent.B461()
        return b461_1

@register(Crude_Oil_Prices)
class A480():
    # 'Crude_Oil_Prices'!A480
    value = 45884
    isdatetime = True

@register(Crude_Oil_Prices)
class B480():
    # 'Crude_Oil_Prices'!B480
    value = 0
    formula = "='Input EIA Crude WTI'!B478"
    @eval_fn
    def B480():
        b478_1 = Input_EIA_Crude_WTI.B478()
        return b478_1

@register(Crude_Oil_Prices)
class C480():
    # 'Crude_Oil_Prices'!C480
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B462"
    @eval_fn
    def C480():
        b462_1 = Input_EIA_Crude_Europe_Brent.B462()
        return b462_1

@register(Crude_Oil_Prices)
class A481():
    # 'Crude_Oil_Prices'!A481
    value = 45915
    isdatetime = True

@register(Crude_Oil_Prices)
class B481():
    # 'Crude_Oil_Prices'!B481
    value = 0
    formula = "='Input EIA Crude WTI'!B479"
    @eval_fn
    def B481():
        b479_1 = Input_EIA_Crude_WTI.B479()
        return b479_1

@register(Crude_Oil_Prices)
class C481():
    # 'Crude_Oil_Prices'!C481
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B463"
    @eval_fn
    def C481():
        b463_1 = Input_EIA_Crude_Europe_Brent.B463()
        return b463_1

@register(Crude_Oil_Prices)
class A482():
    # 'Crude_Oil_Prices'!A482
    value = 45945
    isdatetime = True

@register(Crude_Oil_Prices)
class B482():
    # 'Crude_Oil_Prices'!B482
    value = 0
    formula = "='Input EIA Crude WTI'!B480"
    @eval_fn
    def B482():
        b480_1 = Input_EIA_Crude_WTI.B480()
        return b480_1

@register(Crude_Oil_Prices)
class C482():
    # 'Crude_Oil_Prices'!C482
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B464"
    @eval_fn
    def C482():
        b464_1 = Input_EIA_Crude_Europe_Brent.B464()
        return b464_1

@register(Crude_Oil_Prices)
class A483():
    # 'Crude_Oil_Prices'!A483
    value = 45976
    isdatetime = True

@register(Crude_Oil_Prices)
class B483():
    # 'Crude_Oil_Prices'!B483
    value = 0
    formula = "='Input EIA Crude WTI'!B481"
    @eval_fn
    def B483():
        b481_1 = Input_EIA_Crude_WTI.B481()
        return b481_1

@register(Crude_Oil_Prices)
class C483():
    # 'Crude_Oil_Prices'!C483
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B465"
    @eval_fn
    def C483():
        b465_1 = Input_EIA_Crude_Europe_Brent.B465()
        return b465_1

@register(Crude_Oil_Prices)
class A484():
    # 'Crude_Oil_Prices'!A484
    value = 46006
    isdatetime = True

@register(Crude_Oil_Prices)
class B484():
    # 'Crude_Oil_Prices'!B484
    value = 0
    formula = "='Input EIA Crude WTI'!B482"
    @eval_fn
    def B484():
        b482_1 = Input_EIA_Crude_WTI.B482()
        return b482_1

@register(Crude_Oil_Prices)
class C484():
    # 'Crude_Oil_Prices'!C484
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B466"
    @eval_fn
    def C484():
        b466_1 = Input_EIA_Crude_Europe_Brent.B466()
        return b466_1

@register(Crude_Oil_Prices)
class A485():
    # 'Crude_Oil_Prices'!A485
    value = 46037
    isdatetime = True

@register(Crude_Oil_Prices)
class B485():
    # 'Crude_Oil_Prices'!B485
    value = 0
    formula = "='Input EIA Crude WTI'!B483"
    @eval_fn
    def B485():
        b483_1 = Input_EIA_Crude_WTI.B483()
        return b483_1

@register(Crude_Oil_Prices)
class C485():
    # 'Crude_Oil_Prices'!C485
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B467"
    @eval_fn
    def C485():
        b467_1 = Input_EIA_Crude_Europe_Brent.B467()
        return b467_1

@register(Crude_Oil_Prices)
class A486():
    # 'Crude_Oil_Prices'!A486
    value = 46068
    isdatetime = True

@register(Crude_Oil_Prices)
class B486():
    # 'Crude_Oil_Prices'!B486
    value = 0
    formula = "='Input EIA Crude WTI'!B484"
    @eval_fn
    def B486():
        b484_1 = Input_EIA_Crude_WTI.B484()
        return b484_1

@register(Crude_Oil_Prices)
class C486():
    # 'Crude_Oil_Prices'!C486
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B468"
    @eval_fn
    def C486():
        b468_1 = Input_EIA_Crude_Europe_Brent.B468()
        return b468_1

@register(Crude_Oil_Prices)
class A487():
    # 'Crude_Oil_Prices'!A487
    value = 46096
    isdatetime = True

@register(Crude_Oil_Prices)
class B487():
    # 'Crude_Oil_Prices'!B487
    value = 0
    formula = "='Input EIA Crude WTI'!B485"
    @eval_fn
    def B487():
        b485_1 = Input_EIA_Crude_WTI.B485()
        return b485_1

@register(Crude_Oil_Prices)
class C487():
    # 'Crude_Oil_Prices'!C487
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B469"
    @eval_fn
    def C487():
        b469_1 = Input_EIA_Crude_Europe_Brent.B469()
        return b469_1

@register(Crude_Oil_Prices)
class A488():
    # 'Crude_Oil_Prices'!A488
    value = 46127
    isdatetime = True

@register(Crude_Oil_Prices)
class B488():
    # 'Crude_Oil_Prices'!B488
    value = 0
    formula = "='Input EIA Crude WTI'!B486"
    @eval_fn
    def B488():
        b486_1 = Input_EIA_Crude_WTI.B486()
        return b486_1

@register(Crude_Oil_Prices)
class C488():
    # 'Crude_Oil_Prices'!C488
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B470"
    @eval_fn
    def C488():
        b470_1 = Input_EIA_Crude_Europe_Brent.B470()
        return b470_1

@register(Crude_Oil_Prices)
class A489():
    # 'Crude_Oil_Prices'!A489
    value = 46157
    isdatetime = True

@register(Crude_Oil_Prices)
class B489():
    # 'Crude_Oil_Prices'!B489
    value = 0
    formula = "='Input EIA Crude WTI'!B487"
    @eval_fn
    def B489():
        b487_1 = Input_EIA_Crude_WTI.B487()
        return b487_1

@register(Crude_Oil_Prices)
class C489():
    # 'Crude_Oil_Prices'!C489
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B471"
    @eval_fn
    def C489():
        b471_1 = Input_EIA_Crude_Europe_Brent.B471()
        return b471_1

@register(Crude_Oil_Prices)
class A490():
    # 'Crude_Oil_Prices'!A490
    value = 46188
    isdatetime = True

@register(Crude_Oil_Prices)
class B490():
    # 'Crude_Oil_Prices'!B490
    value = 0
    formula = "='Input EIA Crude WTI'!B488"
    @eval_fn
    def B490():
        b488_1 = Input_EIA_Crude_WTI.B488()
        return b488_1

@register(Crude_Oil_Prices)
class C490():
    # 'Crude_Oil_Prices'!C490
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B472"
    @eval_fn
    def C490():
        b472_1 = Input_EIA_Crude_Europe_Brent.B472()
        return b472_1

@register(Crude_Oil_Prices)
class A491():
    # 'Crude_Oil_Prices'!A491
    value = 46218
    isdatetime = True

@register(Crude_Oil_Prices)
class B491():
    # 'Crude_Oil_Prices'!B491
    value = 0
    formula = "='Input EIA Crude WTI'!B489"
    @eval_fn
    def B491():
        b489_1 = Input_EIA_Crude_WTI.B489()
        return b489_1

@register(Crude_Oil_Prices)
class C491():
    # 'Crude_Oil_Prices'!C491
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B473"
    @eval_fn
    def C491():
        b473_1 = Input_EIA_Crude_Europe_Brent.B473()
        return b473_1

@register(Crude_Oil_Prices)
class A492():
    # 'Crude_Oil_Prices'!A492
    value = 46249
    isdatetime = True

@register(Crude_Oil_Prices)
class B492():
    # 'Crude_Oil_Prices'!B492
    value = 0
    formula = "='Input EIA Crude WTI'!B490"
    @eval_fn
    def B492():
        b490_1 = Input_EIA_Crude_WTI.B490()
        return b490_1

@register(Crude_Oil_Prices)
class C492():
    # 'Crude_Oil_Prices'!C492
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B474"
    @eval_fn
    def C492():
        b474_1 = Input_EIA_Crude_Europe_Brent.B474()
        return b474_1

@register(Crude_Oil_Prices)
class A493():
    # 'Crude_Oil_Prices'!A493
    value = 46280
    isdatetime = True

@register(Crude_Oil_Prices)
class B493():
    # 'Crude_Oil_Prices'!B493
    value = 0
    formula = "='Input EIA Crude WTI'!B491"
    @eval_fn
    def B493():
        b491_1 = Input_EIA_Crude_WTI.B491()
        return b491_1

@register(Crude_Oil_Prices)
class C493():
    # 'Crude_Oil_Prices'!C493
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B475"
    @eval_fn
    def C493():
        b475_1 = Input_EIA_Crude_Europe_Brent.B475()
        return b475_1

@register(Crude_Oil_Prices)
class A494():
    # 'Crude_Oil_Prices'!A494
    value = 46310
    isdatetime = True

@register(Crude_Oil_Prices)
class B494():
    # 'Crude_Oil_Prices'!B494
    value = 0
    formula = "='Input EIA Crude WTI'!B492"
    @eval_fn
    def B494():
        b492_1 = Input_EIA_Crude_WTI.B492()
        return b492_1

@register(Crude_Oil_Prices)
class C494():
    # 'Crude_Oil_Prices'!C494
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B476"
    @eval_fn
    def C494():
        b476_1 = Input_EIA_Crude_Europe_Brent.B476()
        return b476_1

@register(Crude_Oil_Prices)
class A495():
    # 'Crude_Oil_Prices'!A495
    value = 46341
    isdatetime = True

@register(Crude_Oil_Prices)
class B495():
    # 'Crude_Oil_Prices'!B495
    value = 0
    formula = "='Input EIA Crude WTI'!B493"
    @eval_fn
    def B495():
        b493_1 = Input_EIA_Crude_WTI.B493()
        return b493_1

@register(Crude_Oil_Prices)
class C495():
    # 'Crude_Oil_Prices'!C495
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B477"
    @eval_fn
    def C495():
        b477_1 = Input_EIA_Crude_Europe_Brent.B477()
        return b477_1

@register(Crude_Oil_Prices)
class A496():
    # 'Crude_Oil_Prices'!A496
    value = 46371
    isdatetime = True

@register(Crude_Oil_Prices)
class B496():
    # 'Crude_Oil_Prices'!B496
    value = 0
    formula = "='Input EIA Crude WTI'!B494"
    @eval_fn
    def B496():
        b494_1 = Input_EIA_Crude_WTI.B494()
        return b494_1

@register(Crude_Oil_Prices)
class C496():
    # 'Crude_Oil_Prices'!C496
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B478"
    @eval_fn
    def C496():
        b478_1 = Input_EIA_Crude_Europe_Brent.B478()
        return b478_1

@register(Crude_Oil_Prices)
class A497():
    # 'Crude_Oil_Prices'!A497
    value = 46402
    isdatetime = True

@register(Crude_Oil_Prices)
class B497():
    # 'Crude_Oil_Prices'!B497
    value = 0
    formula = "='Input EIA Crude WTI'!B495"
    @eval_fn
    def B497():
        b495_1 = Input_EIA_Crude_WTI.B495()
        return b495_1

@register(Crude_Oil_Prices)
class C497():
    # 'Crude_Oil_Prices'!C497
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B479"
    @eval_fn
    def C497():
        b479_1 = Input_EIA_Crude_Europe_Brent.B479()
        return b479_1

@register(Crude_Oil_Prices)
class A498():
    # 'Crude_Oil_Prices'!A498
    value = 46433
    isdatetime = True

@register(Crude_Oil_Prices)
class B498():
    # 'Crude_Oil_Prices'!B498
    value = 0
    formula = "='Input EIA Crude WTI'!B496"
    @eval_fn
    def B498():
        b496_1 = Input_EIA_Crude_WTI.B496()
        return b496_1

@register(Crude_Oil_Prices)
class C498():
    # 'Crude_Oil_Prices'!C498
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B480"
    @eval_fn
    def C498():
        b480_1 = Input_EIA_Crude_Europe_Brent.B480()
        return b480_1

@register(Crude_Oil_Prices)
class A499():
    # 'Crude_Oil_Prices'!A499
    value = 46461
    isdatetime = True

@register(Crude_Oil_Prices)
class B499():
    # 'Crude_Oil_Prices'!B499
    value = 0
    formula = "='Input EIA Crude WTI'!B497"
    @eval_fn
    def B499():
        b497_1 = Input_EIA_Crude_WTI.B497()
        return b497_1

@register(Crude_Oil_Prices)
class C499():
    # 'Crude_Oil_Prices'!C499
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B481"
    @eval_fn
    def C499():
        b481_1 = Input_EIA_Crude_Europe_Brent.B481()
        return b481_1

@register(Crude_Oil_Prices)
class A500():
    # 'Crude_Oil_Prices'!A500
    value = 46492
    isdatetime = True

@register(Crude_Oil_Prices)
class B500():
    # 'Crude_Oil_Prices'!B500
    value = 0
    formula = "='Input EIA Crude WTI'!B498"
    @eval_fn
    def B500():
        b498_1 = Input_EIA_Crude_WTI.B498()
        return b498_1

@register(Crude_Oil_Prices)
class C500():
    # 'Crude_Oil_Prices'!C500
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B482"
    @eval_fn
    def C500():
        b482_1 = Input_EIA_Crude_Europe_Brent.B482()
        return b482_1

@register(Crude_Oil_Prices)
class A501():
    # 'Crude_Oil_Prices'!A501
    value = 46522
    isdatetime = True

@register(Crude_Oil_Prices)
class B501():
    # 'Crude_Oil_Prices'!B501
    value = 0
    formula = "='Input EIA Crude WTI'!B499"
    @eval_fn
    def B501():
        b499_1 = Input_EIA_Crude_WTI.B499()
        return b499_1

@register(Crude_Oil_Prices)
class C501():
    # 'Crude_Oil_Prices'!C501
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B483"
    @eval_fn
    def C501():
        b483_1 = Input_EIA_Crude_Europe_Brent.B483()
        return b483_1

@register(Crude_Oil_Prices)
class A502():
    # 'Crude_Oil_Prices'!A502
    value = 46553
    isdatetime = True

@register(Crude_Oil_Prices)
class B502():
    # 'Crude_Oil_Prices'!B502
    value = 0
    formula = "='Input EIA Crude WTI'!B500"
    @eval_fn
    def B502():
        b500_1 = Input_EIA_Crude_WTI.B500()
        return b500_1

@register(Crude_Oil_Prices)
class C502():
    # 'Crude_Oil_Prices'!C502
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B484"
    @eval_fn
    def C502():
        b484_1 = Input_EIA_Crude_Europe_Brent.B484()
        return b484_1

@register(Crude_Oil_Prices)
class A503():
    # 'Crude_Oil_Prices'!A503
    value = 46583
    isdatetime = True

@register(Crude_Oil_Prices)
class B503():
    # 'Crude_Oil_Prices'!B503
    value = 0
    formula = "='Input EIA Crude WTI'!B501"
    @eval_fn
    def B503():
        b501_1 = Input_EIA_Crude_WTI.B501()
        return b501_1

@register(Crude_Oil_Prices)
class C503():
    # 'Crude_Oil_Prices'!C503
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B485"
    @eval_fn
    def C503():
        b485_1 = Input_EIA_Crude_Europe_Brent.B485()
        return b485_1

@register(Crude_Oil_Prices)
class A504():
    # 'Crude_Oil_Prices'!A504
    value = 46614
    isdatetime = True

@register(Crude_Oil_Prices)
class B504():
    # 'Crude_Oil_Prices'!B504
    value = 0
    formula = "='Input EIA Crude WTI'!B502"
    @eval_fn
    def B504():
        b502_1 = Input_EIA_Crude_WTI.B502()
        return b502_1

@register(Crude_Oil_Prices)
class C504():
    # 'Crude_Oil_Prices'!C504
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B486"
    @eval_fn
    def C504():
        b486_1 = Input_EIA_Crude_Europe_Brent.B486()
        return b486_1

@register(Crude_Oil_Prices)
class A505():
    # 'Crude_Oil_Prices'!A505
    value = 46645
    isdatetime = True

@register(Crude_Oil_Prices)
class B505():
    # 'Crude_Oil_Prices'!B505
    value = 0
    formula = "='Input EIA Crude WTI'!B503"
    @eval_fn
    def B505():
        b503_1 = Input_EIA_Crude_WTI.B503()
        return b503_1

@register(Crude_Oil_Prices)
class C505():
    # 'Crude_Oil_Prices'!C505
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B487"
    @eval_fn
    def C505():
        b487_1 = Input_EIA_Crude_Europe_Brent.B487()
        return b487_1

@register(Crude_Oil_Prices)
class A506():
    # 'Crude_Oil_Prices'!A506
    value = 46675
    isdatetime = True

@register(Crude_Oil_Prices)
class B506():
    # 'Crude_Oil_Prices'!B506
    value = 0
    formula = "='Input EIA Crude WTI'!B504"
    @eval_fn
    def B506():
        b504_1 = Input_EIA_Crude_WTI.B504()
        return b504_1

@register(Crude_Oil_Prices)
class C506():
    # 'Crude_Oil_Prices'!C506
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B488"
    @eval_fn
    def C506():
        b488_1 = Input_EIA_Crude_Europe_Brent.B488()
        return b488_1

@register(Crude_Oil_Prices)
class A507():
    # 'Crude_Oil_Prices'!A507
    value = 46706
    isdatetime = True

@register(Crude_Oil_Prices)
class B507():
    # 'Crude_Oil_Prices'!B507
    value = 0
    formula = "='Input EIA Crude WTI'!B505"
    @eval_fn
    def B507():
        b505_1 = Input_EIA_Crude_WTI.B505()
        return b505_1

@register(Crude_Oil_Prices)
class C507():
    # 'Crude_Oil_Prices'!C507
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B489"
    @eval_fn
    def C507():
        b489_1 = Input_EIA_Crude_Europe_Brent.B489()
        return b489_1

@register(Crude_Oil_Prices)
class A508():
    # 'Crude_Oil_Prices'!A508
    value = 46736
    isdatetime = True

@register(Crude_Oil_Prices)
class B508():
    # 'Crude_Oil_Prices'!B508
    value = 0
    formula = "='Input EIA Crude WTI'!B506"
    @eval_fn
    def B508():
        b506_1 = Input_EIA_Crude_WTI.B506()
        return b506_1

@register(Crude_Oil_Prices)
class C508():
    # 'Crude_Oil_Prices'!C508
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B490"
    @eval_fn
    def C508():
        b490_1 = Input_EIA_Crude_Europe_Brent.B490()
        return b490_1

@register(Crude_Oil_Prices)
class A509():
    # 'Crude_Oil_Prices'!A509
    value = 46767
    isdatetime = True

@register(Crude_Oil_Prices)
class B509():
    # 'Crude_Oil_Prices'!B509
    value = 0
    formula = "='Input EIA Crude WTI'!B507"
    @eval_fn
    def B509():
        b507_1 = Input_EIA_Crude_WTI.B507()
        return b507_1

@register(Crude_Oil_Prices)
class C509():
    # 'Crude_Oil_Prices'!C509
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B491"
    @eval_fn
    def C509():
        b491_1 = Input_EIA_Crude_Europe_Brent.B491()
        return b491_1

@register(Crude_Oil_Prices)
class A510():
    # 'Crude_Oil_Prices'!A510
    value = 46798
    isdatetime = True

@register(Crude_Oil_Prices)
class B510():
    # 'Crude_Oil_Prices'!B510
    value = 0
    formula = "='Input EIA Crude WTI'!B508"
    @eval_fn
    def B510():
        b508_1 = Input_EIA_Crude_WTI.B508()
        return b508_1

@register(Crude_Oil_Prices)
class C510():
    # 'Crude_Oil_Prices'!C510
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B492"
    @eval_fn
    def C510():
        b492_1 = Input_EIA_Crude_Europe_Brent.B492()
        return b492_1

@register(Crude_Oil_Prices)
class A511():
    # 'Crude_Oil_Prices'!A511
    value = 46827
    isdatetime = True

@register(Crude_Oil_Prices)
class B511():
    # 'Crude_Oil_Prices'!B511
    value = 0
    formula = "='Input EIA Crude WTI'!B509"
    @eval_fn
    def B511():
        b509_1 = Input_EIA_Crude_WTI.B509()
        return b509_1

@register(Crude_Oil_Prices)
class C511():
    # 'Crude_Oil_Prices'!C511
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B493"
    @eval_fn
    def C511():
        b493_1 = Input_EIA_Crude_Europe_Brent.B493()
        return b493_1

@register(Crude_Oil_Prices)
class A512():
    # 'Crude_Oil_Prices'!A512
    value = 46858
    isdatetime = True

@register(Crude_Oil_Prices)
class B512():
    # 'Crude_Oil_Prices'!B512
    value = 0
    formula = "='Input EIA Crude WTI'!B510"
    @eval_fn
    def B512():
        b510_1 = Input_EIA_Crude_WTI.B510()
        return b510_1

@register(Crude_Oil_Prices)
class C512():
    # 'Crude_Oil_Prices'!C512
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B494"
    @eval_fn
    def C512():
        b494_1 = Input_EIA_Crude_Europe_Brent.B494()
        return b494_1

@register(Crude_Oil_Prices)
class A513():
    # 'Crude_Oil_Prices'!A513
    value = 46888
    isdatetime = True

@register(Crude_Oil_Prices)
class B513():
    # 'Crude_Oil_Prices'!B513
    value = 0
    formula = "='Input EIA Crude WTI'!B511"
    @eval_fn
    def B513():
        b511_1 = Input_EIA_Crude_WTI.B511()
        return b511_1

@register(Crude_Oil_Prices)
class C513():
    # 'Crude_Oil_Prices'!C513
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B495"
    @eval_fn
    def C513():
        b495_1 = Input_EIA_Crude_Europe_Brent.B495()
        return b495_1

@register(Crude_Oil_Prices)
class A514():
    # 'Crude_Oil_Prices'!A514
    value = 46919
    isdatetime = True

@register(Crude_Oil_Prices)
class B514():
    # 'Crude_Oil_Prices'!B514
    value = 0
    formula = "='Input EIA Crude WTI'!B512"
    @eval_fn
    def B514():
        b512_1 = Input_EIA_Crude_WTI.B512()
        return b512_1

@register(Crude_Oil_Prices)
class C514():
    # 'Crude_Oil_Prices'!C514
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B496"
    @eval_fn
    def C514():
        b496_1 = Input_EIA_Crude_Europe_Brent.B496()
        return b496_1

@register(Crude_Oil_Prices)
class A515():
    # 'Crude_Oil_Prices'!A515
    value = 46949
    isdatetime = True

@register(Crude_Oil_Prices)
class B515():
    # 'Crude_Oil_Prices'!B515
    value = 0
    formula = "='Input EIA Crude WTI'!B513"
    @eval_fn
    def B515():
        b513_1 = Input_EIA_Crude_WTI.B513()
        return b513_1

@register(Crude_Oil_Prices)
class C515():
    # 'Crude_Oil_Prices'!C515
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B497"
    @eval_fn
    def C515():
        b497_1 = Input_EIA_Crude_Europe_Brent.B497()
        return b497_1

@register(Crude_Oil_Prices)
class A516():
    # 'Crude_Oil_Prices'!A516
    value = 46980
    isdatetime = True

@register(Crude_Oil_Prices)
class B516():
    # 'Crude_Oil_Prices'!B516
    value = 0
    formula = "='Input EIA Crude WTI'!B514"
    @eval_fn
    def B516():
        b514_1 = Input_EIA_Crude_WTI.B514()
        return b514_1

@register(Crude_Oil_Prices)
class C516():
    # 'Crude_Oil_Prices'!C516
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B498"
    @eval_fn
    def C516():
        b498_1 = Input_EIA_Crude_Europe_Brent.B498()
        return b498_1

@register(Crude_Oil_Prices)
class A517():
    # 'Crude_Oil_Prices'!A517
    value = 47011
    isdatetime = True

@register(Crude_Oil_Prices)
class B517():
    # 'Crude_Oil_Prices'!B517
    value = 0
    formula = "='Input EIA Crude WTI'!B515"
    @eval_fn
    def B517():
        b515_1 = Input_EIA_Crude_WTI.B515()
        return b515_1

@register(Crude_Oil_Prices)
class C517():
    # 'Crude_Oil_Prices'!C517
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B499"
    @eval_fn
    def C517():
        b499_1 = Input_EIA_Crude_Europe_Brent.B499()
        return b499_1

@register(Crude_Oil_Prices)
class A518():
    # 'Crude_Oil_Prices'!A518
    value = 47041
    isdatetime = True

@register(Crude_Oil_Prices)
class B518():
    # 'Crude_Oil_Prices'!B518
    value = 0
    formula = "='Input EIA Crude WTI'!B516"
    @eval_fn
    def B518():
        b516_1 = Input_EIA_Crude_WTI.B516()
        return b516_1

@register(Crude_Oil_Prices)
class C518():
    # 'Crude_Oil_Prices'!C518
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B500"
    @eval_fn
    def C518():
        b500_1 = Input_EIA_Crude_Europe_Brent.B500()
        return b500_1

@register(Crude_Oil_Prices)
class A519():
    # 'Crude_Oil_Prices'!A519
    value = 47072
    isdatetime = True

@register(Crude_Oil_Prices)
class B519():
    # 'Crude_Oil_Prices'!B519
    value = 0
    formula = "='Input EIA Crude WTI'!B517"
    @eval_fn
    def B519():
        b517_1 = Input_EIA_Crude_WTI.B517()
        return b517_1

@register(Crude_Oil_Prices)
class C519():
    # 'Crude_Oil_Prices'!C519
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B501"
    @eval_fn
    def C519():
        b501_1 = Input_EIA_Crude_Europe_Brent.B501()
        return b501_1

@register(Crude_Oil_Prices)
class A520():
    # 'Crude_Oil_Prices'!A520
    value = 47102
    isdatetime = True

@register(Crude_Oil_Prices)
class B520():
    # 'Crude_Oil_Prices'!B520
    value = 0
    formula = "='Input EIA Crude WTI'!B518"
    @eval_fn
    def B520():
        b518_1 = Input_EIA_Crude_WTI.B518()
        return b518_1

@register(Crude_Oil_Prices)
class C520():
    # 'Crude_Oil_Prices'!C520
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B502"
    @eval_fn
    def C520():
        b502_1 = Input_EIA_Crude_Europe_Brent.B502()
        return b502_1

@register(Crude_Oil_Prices)
class A521():
    # 'Crude_Oil_Prices'!A521
    value = 47133
    isdatetime = True

@register(Crude_Oil_Prices)
class B521():
    # 'Crude_Oil_Prices'!B521
    value = 0
    formula = "='Input EIA Crude WTI'!B519"
    @eval_fn
    def B521():
        b519_1 = Input_EIA_Crude_WTI.B519()
        return b519_1

@register(Crude_Oil_Prices)
class C521():
    # 'Crude_Oil_Prices'!C521
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B503"
    @eval_fn
    def C521():
        b503_1 = Input_EIA_Crude_Europe_Brent.B503()
        return b503_1

@register(Crude_Oil_Prices)
class A522():
    # 'Crude_Oil_Prices'!A522
    value = 47164
    isdatetime = True

@register(Crude_Oil_Prices)
class B522():
    # 'Crude_Oil_Prices'!B522
    value = 0
    formula = "='Input EIA Crude WTI'!B520"
    @eval_fn
    def B522():
        b520_1 = Input_EIA_Crude_WTI.B520()
        return b520_1

@register(Crude_Oil_Prices)
class C522():
    # 'Crude_Oil_Prices'!C522
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B504"
    @eval_fn
    def C522():
        b504_1 = Input_EIA_Crude_Europe_Brent.B504()
        return b504_1

@register(Crude_Oil_Prices)
class A523():
    # 'Crude_Oil_Prices'!A523
    value = 47192
    isdatetime = True

@register(Crude_Oil_Prices)
class B523():
    # 'Crude_Oil_Prices'!B523
    value = 0
    formula = "='Input EIA Crude WTI'!B521"
    @eval_fn
    def B523():
        b521_1 = Input_EIA_Crude_WTI.B521()
        return b521_1

@register(Crude_Oil_Prices)
class C523():
    # 'Crude_Oil_Prices'!C523
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B505"
    @eval_fn
    def C523():
        b505_1 = Input_EIA_Crude_Europe_Brent.B505()
        return b505_1

@register(Crude_Oil_Prices)
class A524():
    # 'Crude_Oil_Prices'!A524
    value = 47223
    isdatetime = True

@register(Crude_Oil_Prices)
class B524():
    # 'Crude_Oil_Prices'!B524
    value = 0
    formula = "='Input EIA Crude WTI'!B522"
    @eval_fn
    def B524():
        b522_1 = Input_EIA_Crude_WTI.B522()
        return b522_1

@register(Crude_Oil_Prices)
class C524():
    # 'Crude_Oil_Prices'!C524
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B506"
    @eval_fn
    def C524():
        b506_1 = Input_EIA_Crude_Europe_Brent.B506()
        return b506_1

@register(Crude_Oil_Prices)
class A525():
    # 'Crude_Oil_Prices'!A525
    value = 47253
    isdatetime = True

@register(Crude_Oil_Prices)
class B525():
    # 'Crude_Oil_Prices'!B525
    value = 0
    formula = "='Input EIA Crude WTI'!B523"
    @eval_fn
    def B525():
        b523_1 = Input_EIA_Crude_WTI.B523()
        return b523_1

@register(Crude_Oil_Prices)
class C525():
    # 'Crude_Oil_Prices'!C525
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B507"
    @eval_fn
    def C525():
        b507_1 = Input_EIA_Crude_Europe_Brent.B507()
        return b507_1

@register(Crude_Oil_Prices)
class A526():
    # 'Crude_Oil_Prices'!A526
    value = 47284
    isdatetime = True

@register(Crude_Oil_Prices)
class B526():
    # 'Crude_Oil_Prices'!B526
    value = 0
    formula = "='Input EIA Crude WTI'!B524"
    @eval_fn
    def B526():
        b524_1 = Input_EIA_Crude_WTI.B524()
        return b524_1

@register(Crude_Oil_Prices)
class C526():
    # 'Crude_Oil_Prices'!C526
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B508"
    @eval_fn
    def C526():
        b508_1 = Input_EIA_Crude_Europe_Brent.B508()
        return b508_1

@register(Crude_Oil_Prices)
class A527():
    # 'Crude_Oil_Prices'!A527
    value = 47314
    isdatetime = True

@register(Crude_Oil_Prices)
class B527():
    # 'Crude_Oil_Prices'!B527
    value = 0
    formula = "='Input EIA Crude WTI'!B525"
    @eval_fn
    def B527():
        b525_1 = Input_EIA_Crude_WTI.B525()
        return b525_1

@register(Crude_Oil_Prices)
class C527():
    # 'Crude_Oil_Prices'!C527
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B509"
    @eval_fn
    def C527():
        b509_1 = Input_EIA_Crude_Europe_Brent.B509()
        return b509_1

@register(Crude_Oil_Prices)
class A528():
    # 'Crude_Oil_Prices'!A528
    value = 47345
    isdatetime = True

@register(Crude_Oil_Prices)
class B528():
    # 'Crude_Oil_Prices'!B528
    value = 0
    formula = "='Input EIA Crude WTI'!B526"
    @eval_fn
    def B528():
        b526_1 = Input_EIA_Crude_WTI.B526()
        return b526_1

@register(Crude_Oil_Prices)
class C528():
    # 'Crude_Oil_Prices'!C528
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B510"
    @eval_fn
    def C528():
        b510_1 = Input_EIA_Crude_Europe_Brent.B510()
        return b510_1

@register(Crude_Oil_Prices)
class A529():
    # 'Crude_Oil_Prices'!A529
    value = 47376
    isdatetime = True

@register(Crude_Oil_Prices)
class B529():
    # 'Crude_Oil_Prices'!B529
    value = 0
    formula = "='Input EIA Crude WTI'!B527"
    @eval_fn
    def B529():
        b527_1 = Input_EIA_Crude_WTI.B527()
        return b527_1

@register(Crude_Oil_Prices)
class C529():
    # 'Crude_Oil_Prices'!C529
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B511"
    @eval_fn
    def C529():
        b511_1 = Input_EIA_Crude_Europe_Brent.B511()
        return b511_1

@register(Crude_Oil_Prices)
class A530():
    # 'Crude_Oil_Prices'!A530
    value = 47406
    isdatetime = True

@register(Crude_Oil_Prices)
class B530():
    # 'Crude_Oil_Prices'!B530
    value = 0
    formula = "='Input EIA Crude WTI'!B528"
    @eval_fn
    def B530():
        b528_1 = Input_EIA_Crude_WTI.B528()
        return b528_1

@register(Crude_Oil_Prices)
class C530():
    # 'Crude_Oil_Prices'!C530
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B512"
    @eval_fn
    def C530():
        b512_1 = Input_EIA_Crude_Europe_Brent.B512()
        return b512_1

@register(Crude_Oil_Prices)
class A531():
    # 'Crude_Oil_Prices'!A531
    value = 47437
    isdatetime = True

@register(Crude_Oil_Prices)
class B531():
    # 'Crude_Oil_Prices'!B531
    value = 0
    formula = "='Input EIA Crude WTI'!B529"
    @eval_fn
    def B531():
        b529_1 = Input_EIA_Crude_WTI.B529()
        return b529_1

@register(Crude_Oil_Prices)
class C531():
    # 'Crude_Oil_Prices'!C531
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B513"
    @eval_fn
    def C531():
        b513_1 = Input_EIA_Crude_Europe_Brent.B513()
        return b513_1

@register(Crude_Oil_Prices)
class A532():
    # 'Crude_Oil_Prices'!A532
    value = 47467
    isdatetime = True

@register(Crude_Oil_Prices)
class B532():
    # 'Crude_Oil_Prices'!B532
    value = 0
    formula = "='Input EIA Crude WTI'!B530"
    @eval_fn
    def B532():
        b530_1 = Input_EIA_Crude_WTI.B530()
        return b530_1

@register(Crude_Oil_Prices)
class C532():
    # 'Crude_Oil_Prices'!C532
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B514"
    @eval_fn
    def C532():
        b514_1 = Input_EIA_Crude_Europe_Brent.B514()
        return b514_1

@register(Crude_Oil_Prices)
class A533():
    # 'Crude_Oil_Prices'!A533
    value = 47498
    isdatetime = True

@register(Crude_Oil_Prices)
class B533():
    # 'Crude_Oil_Prices'!B533
    value = 0
    formula = "='Input EIA Crude WTI'!B531"
    @eval_fn
    def B533():
        b531_1 = Input_EIA_Crude_WTI.B531()
        return b531_1

@register(Crude_Oil_Prices)
class C533():
    # 'Crude_Oil_Prices'!C533
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B515"
    @eval_fn
    def C533():
        b515_1 = Input_EIA_Crude_Europe_Brent.B515()
        return b515_1

@register(Crude_Oil_Prices)
class A534():
    # 'Crude_Oil_Prices'!A534
    value = 47529
    isdatetime = True

@register(Crude_Oil_Prices)
class B534():
    # 'Crude_Oil_Prices'!B534
    value = 0
    formula = "='Input EIA Crude WTI'!B532"
    @eval_fn
    def B534():
        b532_1 = Input_EIA_Crude_WTI.B532()
        return b532_1

@register(Crude_Oil_Prices)
class C534():
    # 'Crude_Oil_Prices'!C534
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B516"
    @eval_fn
    def C534():
        b516_1 = Input_EIA_Crude_Europe_Brent.B516()
        return b516_1

@register(Crude_Oil_Prices)
class A535():
    # 'Crude_Oil_Prices'!A535
    value = 47557
    isdatetime = True

@register(Crude_Oil_Prices)
class B535():
    # 'Crude_Oil_Prices'!B535
    value = 0
    formula = "='Input EIA Crude WTI'!B533"
    @eval_fn
    def B535():
        b533_1 = Input_EIA_Crude_WTI.B533()
        return b533_1

@register(Crude_Oil_Prices)
class C535():
    # 'Crude_Oil_Prices'!C535
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B517"
    @eval_fn
    def C535():
        b517_1 = Input_EIA_Crude_Europe_Brent.B517()
        return b517_1

@register(Crude_Oil_Prices)
class A536():
    # 'Crude_Oil_Prices'!A536
    value = 47588
    isdatetime = True

@register(Crude_Oil_Prices)
class B536():
    # 'Crude_Oil_Prices'!B536
    value = 0
    formula = "='Input EIA Crude WTI'!B534"
    @eval_fn
    def B536():
        b534_1 = Input_EIA_Crude_WTI.B534()
        return b534_1

@register(Crude_Oil_Prices)
class C536():
    # 'Crude_Oil_Prices'!C536
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B518"
    @eval_fn
    def C536():
        b518_1 = Input_EIA_Crude_Europe_Brent.B518()
        return b518_1

@register(Crude_Oil_Prices)
class A537():
    # 'Crude_Oil_Prices'!A537
    value = 47618
    isdatetime = True

@register(Crude_Oil_Prices)
class B537():
    # 'Crude_Oil_Prices'!B537
    value = 0
    formula = "='Input EIA Crude WTI'!B535"
    @eval_fn
    def B537():
        b535_1 = Input_EIA_Crude_WTI.B535()
        return b535_1

@register(Crude_Oil_Prices)
class C537():
    # 'Crude_Oil_Prices'!C537
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B519"
    @eval_fn
    def C537():
        b519_1 = Input_EIA_Crude_Europe_Brent.B519()
        return b519_1

@register(Crude_Oil_Prices)
class A538():
    # 'Crude_Oil_Prices'!A538
    value = 47649
    isdatetime = True

@register(Crude_Oil_Prices)
class B538():
    # 'Crude_Oil_Prices'!B538
    value = 0
    formula = "='Input EIA Crude WTI'!B536"
    @eval_fn
    def B538():
        b536_1 = Input_EIA_Crude_WTI.B536()
        return b536_1

@register(Crude_Oil_Prices)
class C538():
    # 'Crude_Oil_Prices'!C538
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B520"
    @eval_fn
    def C538():
        b520_1 = Input_EIA_Crude_Europe_Brent.B520()
        return b520_1

@register(Crude_Oil_Prices)
class A539():
    # 'Crude_Oil_Prices'!A539
    value = 47679
    isdatetime = True

@register(Crude_Oil_Prices)
class B539():
    # 'Crude_Oil_Prices'!B539
    value = 0
    formula = "='Input EIA Crude WTI'!B537"
    @eval_fn
    def B539():
        b537_1 = Input_EIA_Crude_WTI.B537()
        return b537_1

@register(Crude_Oil_Prices)
class C539():
    # 'Crude_Oil_Prices'!C539
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B521"
    @eval_fn
    def C539():
        b521_1 = Input_EIA_Crude_Europe_Brent.B521()
        return b521_1

@register(Crude_Oil_Prices)
class A540():
    # 'Crude_Oil_Prices'!A540
    value = 47710
    isdatetime = True

@register(Crude_Oil_Prices)
class B540():
    # 'Crude_Oil_Prices'!B540
    value = 0
    formula = "='Input EIA Crude WTI'!B538"
    @eval_fn
    def B540():
        b538_1 = Input_EIA_Crude_WTI.B538()
        return b538_1

@register(Crude_Oil_Prices)
class C540():
    # 'Crude_Oil_Prices'!C540
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B522"
    @eval_fn
    def C540():
        b522_1 = Input_EIA_Crude_Europe_Brent.B522()
        return b522_1

@register(Crude_Oil_Prices)
class A541():
    # 'Crude_Oil_Prices'!A541
    value = 47741
    isdatetime = True

@register(Crude_Oil_Prices)
class B541():
    # 'Crude_Oil_Prices'!B541
    value = 0
    formula = "='Input EIA Crude WTI'!B539"
    @eval_fn
    def B541():
        b539_1 = Input_EIA_Crude_WTI.B539()
        return b539_1

@register(Crude_Oil_Prices)
class C541():
    # 'Crude_Oil_Prices'!C541
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B523"
    @eval_fn
    def C541():
        b523_1 = Input_EIA_Crude_Europe_Brent.B523()
        return b523_1

@register(Crude_Oil_Prices)
class A542():
    # 'Crude_Oil_Prices'!A542
    value = 47771
    isdatetime = True

@register(Crude_Oil_Prices)
class B542():
    # 'Crude_Oil_Prices'!B542
    value = 0
    formula = "='Input EIA Crude WTI'!B540"
    @eval_fn
    def B542():
        b540_1 = Input_EIA_Crude_WTI.B540()
        return b540_1

@register(Crude_Oil_Prices)
class C542():
    # 'Crude_Oil_Prices'!C542
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B524"
    @eval_fn
    def C542():
        b524_1 = Input_EIA_Crude_Europe_Brent.B524()
        return b524_1

@register(Crude_Oil_Prices)
class A543():
    # 'Crude_Oil_Prices'!A543
    value = 47802
    isdatetime = True

@register(Crude_Oil_Prices)
class B543():
    # 'Crude_Oil_Prices'!B543
    value = 0
    formula = "='Input EIA Crude WTI'!B541"
    @eval_fn
    def B543():
        b541_1 = Input_EIA_Crude_WTI.B541()
        return b541_1

@register(Crude_Oil_Prices)
class C543():
    # 'Crude_Oil_Prices'!C543
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B525"
    @eval_fn
    def C543():
        b525_1 = Input_EIA_Crude_Europe_Brent.B525()
        return b525_1

@register(Crude_Oil_Prices)
class A544():
    # 'Crude_Oil_Prices'!A544
    value = 47832
    isdatetime = True

@register(Crude_Oil_Prices)
class B544():
    # 'Crude_Oil_Prices'!B544
    value = 0
    formula = "='Input EIA Crude WTI'!B542"
    @eval_fn
    def B544():
        b542_1 = Input_EIA_Crude_WTI.B542()
        return b542_1

@register(Crude_Oil_Prices)
class C544():
    # 'Crude_Oil_Prices'!C544
    value = 0
    formula = "='Input EIA Crude Europe Brent'!B526"
    @eval_fn
    def C544():
        b526_1 = Input_EIA_Crude_Europe_Brent.B526()
        return b526_1