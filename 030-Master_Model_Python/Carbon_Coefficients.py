# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Carbon_Coefficients = Worksheet('Carbon_Coefficients', 10, 10)



@register(Carbon_Coefficients)
class A1():
    # 'Carbon_Coefficients'!A1
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class A3():
    # 'Carbon_Coefficients'!A3
    value = "Natural Gas"

@register(Carbon_Coefficients)
class A4():
    # 'Carbon_Coefficients'!A4
    value = "Carbon Content Coefficient (kgCarbon/MMBtu)"

@register(Carbon_Coefficients)
class A5():
    # 'Carbon_Coefficients'!A5
    value = "pipelin natural gas"

@register(Carbon_Coefficients)
class B5():
    # 'Carbon_Coefficients'!B5
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C5():
    # 'Carbon_Coefficients'!C5
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D5():
    # 'Carbon_Coefficients'!D5
    value = 14.45

@register(Carbon_Coefficients)
class E5():
    # 'Carbon_Coefficients'!E5
    value = 52.9833333333
    formula = "=D5*(44/12)"
    @eval_fn
    def E5():
        d5_1 = Carbon_Coefficients.D5()
        var_1 = divide(44, 12)
        var_2 = mult(d5_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A6():
    # 'Carbon_Coefficients'!A6
    value = "flare gas"

@register(Carbon_Coefficients)
class B6():
    # 'Carbon_Coefficients'!B6
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C6():
    # 'Carbon_Coefficients'!C6
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D6():
    # 'Carbon_Coefficients'!D6
    value = 15.31

@register(Carbon_Coefficients)
class A7():
    # 'Carbon_Coefficients'!A7
    value = "Nat Gas, Weighted National Average (1029  Btu/scf)"

@register(Carbon_Coefficients)
class B7():
    # 'Carbon_Coefficients'!B7
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class C7():
    # 'Carbon_Coefficients'!C7
    value = "http://www.eia.gov/oiaf/1605/excel/Fuel%20Emission%20Factors.xls "

@register(Carbon_Coefficients)
class D7():
    # 'Carbon_Coefficients'!D7
    value = 53.06

@register(Carbon_Coefficients)
class A8():
    # 'Carbon_Coefficients'!A8
    value = "Upstream Emissions, Average LNG "

@register(Carbon_Coefficients)
class B8():
    # 'Carbon_Coefficients'!B8
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class C8():
    # 'Carbon_Coefficients'!C8
    value = "Slide 26. http://www.netl.doe.gov/energy-analyses/pubs/LCA_coal&NG_plants.pdf"

@register(Carbon_Coefficients)
class D8():
    # 'Carbon_Coefficients'!D8
    value = 39.9

@register(Carbon_Coefficients)
class A9():
    # 'Carbon_Coefficients'!A9
    value = "Total WTW Emission"

@register(Carbon_Coefficients)
class B9():
    # 'Carbon_Coefficients'!B9
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class C9():
    # 'Carbon_Coefficients'!C9
    value = "Combined sources above"

@register(Carbon_Coefficients)
class D9():
    # 'Carbon_Coefficients'!D9
    value = 92.96
    formula = "=D8+D7"
    @eval_fn
    def D9():
        d8_1 = Carbon_Coefficients.D8()
        d7_1 = Carbon_Coefficients.D7()
        var_1 = add(d8_1, d7_1)
        return var_1

@register(Carbon_Coefficients)
class A10():
    # 'Carbon_Coefficients'!A10
    value = "LCEF"

@register(Carbon_Coefficients)
class B10():
    # 'Carbon_Coefficients'!B10
    value = "Percentage"

@register(Carbon_Coefficients)
class D10():
    # 'Carbon_Coefficients'!D10
    value = 0.751978891821
    formula = "=D8/D7"
    @eval_fn
    def D10():
        d8_1 = Carbon_Coefficients.D8()
        d7_1 = Carbon_Coefficients.D7()
        var_1 = divide(d8_1, d7_1)
        return var_1

@register(Carbon_Coefficients)
class A12():
    # 'Carbon_Coefficients'!A12
    value = "Coal"

@register(Carbon_Coefficients)
class A13():
    # 'Carbon_Coefficients'!A13
    value = "Carbon Content Coefficient (kgCarbon/MMBtu)"

@register(Carbon_Coefficients)
class A14():
    # 'Carbon_Coefficients'!A14
    value = "Residential coal"

@register(Carbon_Coefficients)
class B14():
    # 'Carbon_Coefficients'!B14
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C14():
    # 'Carbon_Coefficients'!C14
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D14():
    # 'Carbon_Coefficients'!D14
    value = 25.71

@register(Carbon_Coefficients)
class A15():
    # 'Carbon_Coefficients'!A15
    value = "Commercial"

@register(Carbon_Coefficients)
class B15():
    # 'Carbon_Coefficients'!B15
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C15():
    # 'Carbon_Coefficients'!C15
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D15():
    # 'Carbon_Coefficients'!D15
    value = 25.71

@register(Carbon_Coefficients)
class A16():
    # 'Carbon_Coefficients'!A16
    value = "Industrial Coking"

@register(Carbon_Coefficients)
class B16():
    # 'Carbon_Coefficients'!B16
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C16():
    # 'Carbon_Coefficients'!C16
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D16():
    # 'Carbon_Coefficients'!D16
    value = 25.61

@register(Carbon_Coefficients)
class A17():
    # 'Carbon_Coefficients'!A17
    value = "industrial Other"

@register(Carbon_Coefficients)
class B17():
    # 'Carbon_Coefficients'!B17
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C17():
    # 'Carbon_Coefficients'!C17
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D17():
    # 'Carbon_Coefficients'!D17
    value = 25.82

@register(Carbon_Coefficients)
class A18():
    # 'Carbon_Coefficients'!A18
    value = "Utility Coal"

@register(Carbon_Coefficients)
class B18():
    # 'Carbon_Coefficients'!B18
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C18():
    # 'Carbon_Coefficients'!C18
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D18():
    # 'Carbon_Coefficients'!D18
    value = 26.05

@register(Carbon_Coefficients)
class A19():
    # 'Carbon_Coefficients'!A19
    value = "Average Coal"

@register(Carbon_Coefficients)
class B19():
    # 'Carbon_Coefficients'!B19
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C19():
    # 'Carbon_Coefficients'!C19
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D19():
    # 'Carbon_Coefficients'!D19
    value = 25.78
    formula = "=SUM(D14:D18)/COUNT(D14:D18)"
    @eval_fn
    def D19():
        range_1 = Carbon_Coefficients(4, 14, 4, 18)
        var_1 = SUM(range_1)
        range_2 = Carbon_Coefficients(4, 14, 4, 18)
        var_2 = COUNT(range_2)
        var_3 = divide(var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A20():
    # 'Carbon_Coefficients'!A20
    value = "Average Coal"

@register(Carbon_Coefficients)
class B20():
    # 'Carbon_Coefficients'!B20
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class C20():
    # 'Carbon_Coefficients'!C20
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D20():
    # 'Carbon_Coefficients'!D20
    value = 94.5266666667
    formula = "=D19*(44/12)"
    @eval_fn
    def D20():
        d19_1 = Carbon_Coefficients.D19()
        var_1 = divide(44, 12)
        var_2 = mult(d19_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A21():
    # 'Carbon_Coefficients'!A21
    value = "Upstream Emissions, Average Coal, "

@register(Carbon_Coefficients)
class B21():
    # 'Carbon_Coefficients'!B21
    value = "(kgCO2/MMBtu)"

@register(Carbon_Coefficients)
class C21():
    # 'Carbon_Coefficients'!C21
    value = "Slide 26. This is underrepresentative because it assumes unit train instead of overseaas shipping, http://www.netl.doe.gov/energy-analyses/pubs/LCA_coal&NG_plants.pdf"

@register(Carbon_Coefficients)
class D21():
    # 'Carbon_Coefficients'!D21
    value = 9.2

@register(Carbon_Coefficients)
class A22():
    # 'Carbon_Coefficients'!A22
    value = "Total WTT Emission"

@register(Carbon_Coefficients)
class B22():
    # 'Carbon_Coefficients'!B22
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class C22():
    # 'Carbon_Coefficients'!C22
    value = "Combined sources above"

@register(Carbon_Coefficients)
class D22():
    # 'Carbon_Coefficients'!D22
    value = 103.726666667
    formula = "=D21+D20"
    @eval_fn
    def D22():
        d21_1 = Carbon_Coefficients.D21()
        d20_1 = Carbon_Coefficients.D20()
        var_1 = add(d21_1, d20_1)
        return var_1

@register(Carbon_Coefficients)
class A23():
    # 'Carbon_Coefficients'!A23
    value = "LCEF"

@register(Carbon_Coefficients)
class B23():
    # 'Carbon_Coefficients'!B23
    value = "Percentage"

@register(Carbon_Coefficients)
class D23():
    # 'Carbon_Coefficients'!D23
    value = 0.097327032936
    formula = "=D21/D20"
    @eval_fn
    def D23():
        d21_1 = Carbon_Coefficients.D21()
        d20_1 = Carbon_Coefficients.D20()
        var_1 = divide(d21_1, d20_1)
        return var_1

@register(Carbon_Coefficients)
class A25():
    # 'Carbon_Coefficients'!A25
    value = "Ethanol"

@register(Carbon_Coefficients)
class A26():
    # 'Carbon_Coefficients'!A26
    value = "Carbon Content Coefficient (kgCarbon/MMBtu)"

@register(Carbon_Coefficients)
class A27():
    # 'Carbon_Coefficients'!A27
    value = "Ethanol"

@register(Carbon_Coefficients)
class B27():
    # 'Carbon_Coefficients'!B27
    value = "kgCO2/mmbtu"

@register(Carbon_Coefficients)
class D27():
    # 'Carbon_Coefficients'!D27
    value = 76.0548523207
    formula = "='LCEF by Fuel Type'!AC24"
    @eval_fn
    def D27():
        ac24_1 = LCEF_by_Fuel_Type.AC24()
        return ac24_1

@register(Carbon_Coefficients)
class A29():
    # 'Carbon_Coefficients'!A29
    value = "Petroleum"

@register(Carbon_Coefficients)
class A30():
    # 'Carbon_Coefficients'!A30
    value = "Carbon Content Coefficient (kgCarbon/MMBtu)"

@register(Carbon_Coefficients)
class A31():
    # 'Carbon_Coefficients'!A31
    value = "asphalt"

@register(Carbon_Coefficients)
class B31():
    # 'Carbon_Coefficients'!B31
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C31():
    # 'Carbon_Coefficients'!C31
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D31():
    # 'Carbon_Coefficients'!D31
    value = 20.55

@register(Carbon_Coefficients)
class A32():
    # 'Carbon_Coefficients'!A32
    value = "aviation"

@register(Carbon_Coefficients)
class B32():
    # 'Carbon_Coefficients'!B32
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C32():
    # 'Carbon_Coefficients'!C32
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D32():
    # 'Carbon_Coefficients'!D32
    value = 18.86

@register(Carbon_Coefficients)
class A33():
    # 'Carbon_Coefficients'!A33
    value = "distil 1"

@register(Carbon_Coefficients)
class B33():
    # 'Carbon_Coefficients'!B33
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C33():
    # 'Carbon_Coefficients'!C33
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D33():
    # 'Carbon_Coefficients'!D33
    value = 19.98

@register(Carbon_Coefficients)
class A34():
    # 'Carbon_Coefficients'!A34
    value = "distil2"

@register(Carbon_Coefficients)
class B34():
    # 'Carbon_Coefficients'!B34
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C34():
    # 'Carbon_Coefficients'!C34
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D34():
    # 'Carbon_Coefficients'!D34
    value = 20.17

@register(Carbon_Coefficients)
class A35():
    # 'Carbon_Coefficients'!A35
    value = "distil4"

@register(Carbon_Coefficients)
class B35():
    # 'Carbon_Coefficients'!B35
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C35():
    # 'Carbon_Coefficients'!C35
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D35():
    # 'Carbon_Coefficients'!D35
    value = 20.47

@register(Carbon_Coefficients)
class A36():
    # 'Carbon_Coefficients'!A36
    value = "jet"

@register(Carbon_Coefficients)
class B36():
    # 'Carbon_Coefficients'!B36
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C36():
    # 'Carbon_Coefficients'!C36
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D36():
    # 'Carbon_Coefficients'!D36
    value = 19.7

@register(Carbon_Coefficients)
class A37():
    # 'Carbon_Coefficients'!A37
    value = "kero"

@register(Carbon_Coefficients)
class B37():
    # 'Carbon_Coefficients'!B37
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C37():
    # 'Carbon_Coefficients'!C37
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D37():
    # 'Carbon_Coefficients'!D37
    value = 19.96

@register(Carbon_Coefficients)
class A38():
    # 'Carbon_Coefficients'!A38
    value = "lpg"

@register(Carbon_Coefficients)
class B38():
    # 'Carbon_Coefficients'!B38
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C38():
    # 'Carbon_Coefficients'!C38
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D38():
    # 'Carbon_Coefficients'!D38
    value = 16.83

@register(Carbon_Coefficients)
class A39():
    # 'Carbon_Coefficients'!A39
    value = "lpg"

@register(Carbon_Coefficients)
class B39():
    # 'Carbon_Coefficients'!B39
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C39():
    # 'Carbon_Coefficients'!C39
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D39():
    # 'Carbon_Coefficients'!D39
    value = 17.06

@register(Carbon_Coefficients)
class A40():
    # 'Carbon_Coefficients'!A40
    value = "lubri"

@register(Carbon_Coefficients)
class B40():
    # 'Carbon_Coefficients'!B40
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C40():
    # 'Carbon_Coefficients'!C40
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D40():
    # 'Carbon_Coefficients'!D40
    value = 20.2

@register(Carbon_Coefficients)
class A41():
    # 'Carbon_Coefficients'!A41
    value = "gasoline"

@register(Carbon_Coefficients)
class B41():
    # 'Carbon_Coefficients'!B41
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C41():
    # 'Carbon_Coefficients'!C41
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D41():
    # 'Carbon_Coefficients'!D41
    value = 19.46

@register(Carbon_Coefficients)
class A42():
    # 'Carbon_Coefficients'!A42
    value = "res 5"

@register(Carbon_Coefficients)
class B42():
    # 'Carbon_Coefficients'!B42
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C42():
    # 'Carbon_Coefficients'!C42
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D42():
    # 'Carbon_Coefficients'!D42
    value = 19.89

@register(Carbon_Coefficients)
class A43():
    # 'Carbon_Coefficients'!A43
    value = "res 6"

@register(Carbon_Coefficients)
class B43():
    # 'Carbon_Coefficients'!B43
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class C43():
    # 'Carbon_Coefficients'!C43
    value = "http://www.epa.gov/climatechange/Downloads/ghgemissions/US-GHG-Inventory-2010-Annexes.pdf"

@register(Carbon_Coefficients)
class D43():
    # 'Carbon_Coefficients'!D43
    value = 20.48

@register(Carbon_Coefficients)
class A45():
    # 'Carbon_Coefficients'!A45
    value = "CO2 Content Coefficient (kgCO2/MMBtu)"

@register(Carbon_Coefficients)
class A46():
    # 'Carbon_Coefficients'!A46
    value = "asphalt"

@register(Carbon_Coefficients)
class B46():
    # 'Carbon_Coefficients'!B46
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D46():
    # 'Carbon_Coefficients'!D46
    value = 75.35
    formula = "=D31*(44/12)"
    @eval_fn
    def D46():
        d31_1 = Carbon_Coefficients.D31()
        var_1 = divide(44, 12)
        var_2 = mult(d31_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A47():
    # 'Carbon_Coefficients'!A47
    value = "aviation"

@register(Carbon_Coefficients)
class B47():
    # 'Carbon_Coefficients'!B47
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D47():
    # 'Carbon_Coefficients'!D47
    value = 69.1533333333
    formula = "=D32*(44/12)"
    @eval_fn
    def D47():
        d32_1 = Carbon_Coefficients.D32()
        var_1 = divide(44, 12)
        var_2 = mult(d32_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A48():
    # 'Carbon_Coefficients'!A48
    value = "distil 1"

@register(Carbon_Coefficients)
class B48():
    # 'Carbon_Coefficients'!B48
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D48():
    # 'Carbon_Coefficients'!D48
    value = 73.26
    formula = "=D33*(44/12)"
    @eval_fn
    def D48():
        d33_1 = Carbon_Coefficients.D33()
        var_1 = divide(44, 12)
        var_2 = mult(d33_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A49():
    # 'Carbon_Coefficients'!A49
    value = "distil2"

@register(Carbon_Coefficients)
class B49():
    # 'Carbon_Coefficients'!B49
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D49():
    # 'Carbon_Coefficients'!D49
    value = 73.9566666667
    formula = "=D34*(44/12)"
    @eval_fn
    def D49():
        d34_1 = Carbon_Coefficients.D34()
        var_1 = divide(44, 12)
        var_2 = mult(d34_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A50():
    # 'Carbon_Coefficients'!A50
    value = "distil4"

@register(Carbon_Coefficients)
class B50():
    # 'Carbon_Coefficients'!B50
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D50():
    # 'Carbon_Coefficients'!D50
    value = 75.0566666667
    formula = "=D35*(44/12)"
    @eval_fn
    def D50():
        d35_1 = Carbon_Coefficients.D35()
        var_1 = divide(44, 12)
        var_2 = mult(d35_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A51():
    # 'Carbon_Coefficients'!A51
    value = "jet"

@register(Carbon_Coefficients)
class B51():
    # 'Carbon_Coefficients'!B51
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D51():
    # 'Carbon_Coefficients'!D51
    value = 72.2333333333
    formula = "=D36*(44/12)"
    @eval_fn
    def D51():
        d36_1 = Carbon_Coefficients.D36()
        var_1 = divide(44, 12)
        var_2 = mult(d36_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A52():
    # 'Carbon_Coefficients'!A52
    value = "kero"

@register(Carbon_Coefficients)
class B52():
    # 'Carbon_Coefficients'!B52
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D52():
    # 'Carbon_Coefficients'!D52
    value = 73.1866666667
    formula = "=D37*(44/12)"
    @eval_fn
    def D52():
        d37_1 = Carbon_Coefficients.D37()
        var_1 = divide(44, 12)
        var_2 = mult(d37_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A53():
    # 'Carbon_Coefficients'!A53
    value = "lpg"

@register(Carbon_Coefficients)
class B53():
    # 'Carbon_Coefficients'!B53
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D53():
    # 'Carbon_Coefficients'!D53
    value = 61.71
    formula = "=D38*(44/12)"
    @eval_fn
    def D53():
        d38_1 = Carbon_Coefficients.D38()
        var_1 = divide(44, 12)
        var_2 = mult(d38_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A54():
    # 'Carbon_Coefficients'!A54
    value = "lpg"

@register(Carbon_Coefficients)
class B54():
    # 'Carbon_Coefficients'!B54
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D54():
    # 'Carbon_Coefficients'!D54
    value = 62.5533333333
    formula = "=D39*(44/12)"
    @eval_fn
    def D54():
        d39_1 = Carbon_Coefficients.D39()
        var_1 = divide(44, 12)
        var_2 = mult(d39_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A55():
    # 'Carbon_Coefficients'!A55
    value = "lubri"

@register(Carbon_Coefficients)
class B55():
    # 'Carbon_Coefficients'!B55
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D55():
    # 'Carbon_Coefficients'!D55
    value = 74.0666666667
    formula = "=D40*(44/12)"
    @eval_fn
    def D55():
        d40_1 = Carbon_Coefficients.D40()
        var_1 = divide(44, 12)
        var_2 = mult(d40_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A56():
    # 'Carbon_Coefficients'!A56
    value = "gasoline"

@register(Carbon_Coefficients)
class B56():
    # 'Carbon_Coefficients'!B56
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D56():
    # 'Carbon_Coefficients'!D56
    value = 71.3533333333
    formula = "=D41*(44/12)"
    @eval_fn
    def D56():
        d41_1 = Carbon_Coefficients.D41()
        var_1 = divide(44, 12)
        var_2 = mult(d41_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A57():
    # 'Carbon_Coefficients'!A57
    value = "res 5"

@register(Carbon_Coefficients)
class B57():
    # 'Carbon_Coefficients'!B57
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D57():
    # 'Carbon_Coefficients'!D57
    value = 72.93
    formula = "=D42*(44/12)"
    @eval_fn
    def D57():
        d42_1 = Carbon_Coefficients.D42()
        var_1 = divide(44, 12)
        var_2 = mult(d42_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class A58():
    # 'Carbon_Coefficients'!A58
    value = "res 6"

@register(Carbon_Coefficients)
class B58():
    # 'Carbon_Coefficients'!B58
    value = "kgCO2/MMBtu"

@register(Carbon_Coefficients)
class D58():
    # 'Carbon_Coefficients'!D58
    value = 75.0933333333
    formula = "=D43*(44/12)"
    @eval_fn
    def D58():
        d43_1 = Carbon_Coefficients.D43()
        var_1 = divide(44, 12)
        var_2 = mult(d43_1, var_1)
        return var_2

@register(Carbon_Coefficients)
class D60():
    # 'Carbon_Coefficients'!D60
    value = "All Years"

@register(Carbon_Coefficients)
class E60():
    # 'Carbon_Coefficients'!E60
    value = 1987

@register(Carbon_Coefficients)
class F60():
    # 'Carbon_Coefficients'!F60
    value = 1988

@register(Carbon_Coefficients)
class G60():
    # 'Carbon_Coefficients'!G60
    value = 1989

@register(Carbon_Coefficients)
class H60():
    # 'Carbon_Coefficients'!H60
    value = 1990

@register(Carbon_Coefficients)
class I60():
    # 'Carbon_Coefficients'!I60
    value = 1991

@register(Carbon_Coefficients)
class J60():
    # 'Carbon_Coefficients'!J60
    value = 1992

@register(Carbon_Coefficients)
class K60():
    # 'Carbon_Coefficients'!K60
    value = 1993

@register(Carbon_Coefficients)
class L60():
    # 'Carbon_Coefficients'!L60
    value = 1994

@register(Carbon_Coefficients)
class M60():
    # 'Carbon_Coefficients'!M60
    value = 1995

@register(Carbon_Coefficients)
class N60():
    # 'Carbon_Coefficients'!N60
    value = 1996

@register(Carbon_Coefficients)
class O60():
    # 'Carbon_Coefficients'!O60
    value = 1997

@register(Carbon_Coefficients)
class P60():
    # 'Carbon_Coefficients'!P60
    value = 1998

@register(Carbon_Coefficients)
class Q60():
    # 'Carbon_Coefficients'!Q60
    value = 1999

@register(Carbon_Coefficients)
class R60():
    # 'Carbon_Coefficients'!R60
    value = 2000

@register(Carbon_Coefficients)
class S60():
    # 'Carbon_Coefficients'!S60
    value = 2001

@register(Carbon_Coefficients)
class T60():
    # 'Carbon_Coefficients'!T60
    value = 2002

@register(Carbon_Coefficients)
class U60():
    # 'Carbon_Coefficients'!U60
    value = 2003

@register(Carbon_Coefficients)
class V60():
    # 'Carbon_Coefficients'!V60
    value = 2004

@register(Carbon_Coefficients)
class W60():
    # 'Carbon_Coefficients'!W60
    value = 2005

@register(Carbon_Coefficients)
class X60():
    # 'Carbon_Coefficients'!X60
    value = 2006

@register(Carbon_Coefficients)
class Y60():
    # 'Carbon_Coefficients'!Y60
    value = 2007

@register(Carbon_Coefficients)
class Z60():
    # 'Carbon_Coefficients'!Z60
    value = 2008

@register(Carbon_Coefficients)
class AA60():
    # 'Carbon_Coefficients'!AA60
    value = 2009

@register(Carbon_Coefficients)
class AB60():
    # 'Carbon_Coefficients'!AB60
    value = 2010

@register(Carbon_Coefficients)
class AC60():
    # 'Carbon_Coefficients'!AC60
    value = 2011

@register(Carbon_Coefficients)
class AD60():
    # 'Carbon_Coefficients'!AD60
    value = 2012

@register(Carbon_Coefficients)
class AE60():
    # 'Carbon_Coefficients'!AE60
    value = 2013

@register(Carbon_Coefficients)
class AF60():
    # 'Carbon_Coefficients'!AF60
    value = 2014

@register(Carbon_Coefficients)
class AG60():
    # 'Carbon_Coefficients'!AG60
    value = 2015

@register(Carbon_Coefficients)
class AH60():
    # 'Carbon_Coefficients'!AH60
    value = 2016

@register(Carbon_Coefficients)
class AI60():
    # 'Carbon_Coefficients'!AI60
    value = 2017

@register(Carbon_Coefficients)
class AJ60():
    # 'Carbon_Coefficients'!AJ60
    value = 2018

@register(Carbon_Coefficients)
class AK60():
    # 'Carbon_Coefficients'!AK60
    value = 2019

@register(Carbon_Coefficients)
class AL60():
    # 'Carbon_Coefficients'!AL60
    value = 2020

@register(Carbon_Coefficients)
class AM60():
    # 'Carbon_Coefficients'!AM60
    value = 2021

@register(Carbon_Coefficients)
class AN60():
    # 'Carbon_Coefficients'!AN60
    value = 2022

@register(Carbon_Coefficients)
class AO60():
    # 'Carbon_Coefficients'!AO60
    value = 2023

@register(Carbon_Coefficients)
class AP60():
    # 'Carbon_Coefficients'!AP60
    value = 2024

@register(Carbon_Coefficients)
class AQ60():
    # 'Carbon_Coefficients'!AQ60
    value = 2025

@register(Carbon_Coefficients)
class AR60():
    # 'Carbon_Coefficients'!AR60
    value = 2026

@register(Carbon_Coefficients)
class AS60():
    # 'Carbon_Coefficients'!AS60
    value = 2027

@register(Carbon_Coefficients)
class AT60():
    # 'Carbon_Coefficients'!AT60
    value = 2028

@register(Carbon_Coefficients)
class AU60():
    # 'Carbon_Coefficients'!AU60
    value = 2029

@register(Carbon_Coefficients)
class AV60():
    # 'Carbon_Coefficients'!AV60
    value = 2030

@register(Carbon_Coefficients)
class A61():
    # 'Carbon_Coefficients'!A61
    value = "Consumption by Petroleum Type (MMBtu)"

@register(Carbon_Coefficients)
class A62():
    # 'Carbon_Coefficients'!A62
    value = "Asphat"

@register(Carbon_Coefficients)
class B62():
    # 'Carbon_Coefficients'!B62
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C62():
    # 'Carbon_Coefficients'!C62
    value = "ARTCb"

@register(Carbon_Coefficients)
class E62():
    # 'Carbon_Coefficients'!E62
    value = 2636
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F62():
    # 'Carbon_Coefficients'!F62
    value = 2332
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G62():
    # 'Carbon_Coefficients'!G62
    value = 1966
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H62():
    # 'Carbon_Coefficients'!H62
    value = 2530
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I62():
    # 'Carbon_Coefficients'!I62
    value = 2543
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J62():
    # 'Carbon_Coefficients'!J62
    value = 2858
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K62():
    # 'Carbon_Coefficients'!K62
    value = 2946
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L62():
    # 'Carbon_Coefficients'!L62
    value = 2699
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M62():
    # 'Carbon_Coefficients'!M62
    value = 2907
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N62():
    # 'Carbon_Coefficients'!N62
    value = 2663
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O62():
    # 'Carbon_Coefficients'!O62
    value = 2630
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P62():
    # 'Carbon_Coefficients'!P62
    value = 2138
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q62():
    # 'Carbon_Coefficients'!Q62
    value = 2340
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R62():
    # 'Carbon_Coefficients'!R62
    value = 4009
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S62():
    # 'Carbon_Coefficients'!S62
    value = 2271
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T62():
    # 'Carbon_Coefficients'!T62
    value = 710
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U62():
    # 'Carbon_Coefficients'!U62
    value = 732
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V62():
    # 'Carbon_Coefficients'!V62
    value = 799
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W62():
    # 'Carbon_Coefficients'!W62
    value = 1319
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X62():
    # 'Carbon_Coefficients'!X62
    value = 21
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y62():
    # 'Carbon_Coefficients'!Y62
    value = 19
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z62():
    # 'Carbon_Coefficients'!Z62
    value = 16
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA62():
    # 'Carbon_Coefficients'!AA62
    value = 882
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB62():
    # 'Carbon_Coefficients'!AB62
    value = 887
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC62():
    # 'Carbon_Coefficients'!AC62
    value = 868
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD62():
    # 'Carbon_Coefficients'!AD62
    value = 835
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE62():
    # 'Carbon_Coefficients'!AE62
    value = 791
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF62():
    # 'Carbon_Coefficients'!AF62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG62():
    # 'Carbon_Coefficients'!AG62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH62():
    # 'Carbon_Coefficients'!AH62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI62():
    # 'Carbon_Coefficients'!AI62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ62():
    # 'Carbon_Coefficients'!AJ62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK62():
    # 'Carbon_Coefficients'!AK62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL62():
    # 'Carbon_Coefficients'!AL62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM62():
    # 'Carbon_Coefficients'!AM62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN62():
    # 'Carbon_Coefficients'!AN62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO62():
    # 'Carbon_Coefficients'!AO62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP62():
    # 'Carbon_Coefficients'!AP62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ62():
    # 'Carbon_Coefficients'!AQ62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR62():
    # 'Carbon_Coefficients'!AR62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS62():
    # 'Carbon_Coefficients'!AS62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT62():
    # 'Carbon_Coefficients'!AT62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU62():
    # 'Carbon_Coefficients'!AU62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV62():
    # 'Carbon_Coefficients'!AV62
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C62,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV62():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c62_1 = Carbon_Coefficients.C62()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c62_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A63():
    # 'Carbon_Coefficients'!A63
    value = "Aviation"

@register(Carbon_Coefficients)
class B63():
    # 'Carbon_Coefficients'!B63
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C63():
    # 'Carbon_Coefficients'!C63
    value = "AVTCb"

@register(Carbon_Coefficients)
class E63():
    # 'Carbon_Coefficients'!E63
    value = 1259
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F63():
    # 'Carbon_Coefficients'!F63
    value = 1420
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G63():
    # 'Carbon_Coefficients'!G63
    value = 1449
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H63():
    # 'Carbon_Coefficients'!H63
    value = 1375
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I63():
    # 'Carbon_Coefficients'!I63
    value = 1320
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J63():
    # 'Carbon_Coefficients'!J63
    value = 1229
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K63():
    # 'Carbon_Coefficients'!K63
    value = 1002
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L63():
    # 'Carbon_Coefficients'!L63
    value = 1061
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M63():
    # 'Carbon_Coefficients'!M63
    value = 1100
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N63():
    # 'Carbon_Coefficients'!N63
    value = 833
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O63():
    # 'Carbon_Coefficients'!O63
    value = 609
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P63():
    # 'Carbon_Coefficients'!P63
    value = 540
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q63():
    # 'Carbon_Coefficients'!Q63
    value = 294
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R63():
    # 'Carbon_Coefficients'!R63
    value = 226
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S63():
    # 'Carbon_Coefficients'!S63
    value = 244
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T63():
    # 'Carbon_Coefficients'!T63
    value = 89
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U63():
    # 'Carbon_Coefficients'!U63
    value = 77
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V63():
    # 'Carbon_Coefficients'!V63
    value = 197
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W63():
    # 'Carbon_Coefficients'!W63
    value = 224
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X63():
    # 'Carbon_Coefficients'!X63
    value = 208
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y63():
    # 'Carbon_Coefficients'!Y63
    value = 206
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z63():
    # 'Carbon_Coefficients'!Z63
    value = 140
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA63():
    # 'Carbon_Coefficients'!AA63
    value = 149
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB63():
    # 'Carbon_Coefficients'!AB63
    value = 188
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC63():
    # 'Carbon_Coefficients'!AC63
    value = 176
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD63():
    # 'Carbon_Coefficients'!AD63
    value = 155
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE63():
    # 'Carbon_Coefficients'!AE63
    value = 136
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF63():
    # 'Carbon_Coefficients'!AF63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG63():
    # 'Carbon_Coefficients'!AG63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH63():
    # 'Carbon_Coefficients'!AH63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI63():
    # 'Carbon_Coefficients'!AI63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ63():
    # 'Carbon_Coefficients'!AJ63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK63():
    # 'Carbon_Coefficients'!AK63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL63():
    # 'Carbon_Coefficients'!AL63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM63():
    # 'Carbon_Coefficients'!AM63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN63():
    # 'Carbon_Coefficients'!AN63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO63():
    # 'Carbon_Coefficients'!AO63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP63():
    # 'Carbon_Coefficients'!AP63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ63():
    # 'Carbon_Coefficients'!AQ63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR63():
    # 'Carbon_Coefficients'!AR63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS63():
    # 'Carbon_Coefficients'!AS63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT63():
    # 'Carbon_Coefficients'!AT63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU63():
    # 'Carbon_Coefficients'!AU63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV63():
    # 'Carbon_Coefficients'!AV63
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C63,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV63():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c63_1 = Carbon_Coefficients.C63()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c63_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A64():
    # 'Carbon_Coefficients'!A64
    value = "Distllate"

@register(Carbon_Coefficients)
class B64():
    # 'Carbon_Coefficients'!B64
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C64():
    # 'Carbon_Coefficients'!C64
    value = "DFTCb"

@register(Carbon_Coefficients)
class E64():
    # 'Carbon_Coefficients'!E64
    value = 21464
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F64():
    # 'Carbon_Coefficients'!F64
    value = 32802
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G64():
    # 'Carbon_Coefficients'!G64
    value = 33465
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H64():
    # 'Carbon_Coefficients'!H64
    value = 37796
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I64():
    # 'Carbon_Coefficients'!I64
    value = 41999
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J64():
    # 'Carbon_Coefficients'!J64
    value = 36224
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K64():
    # 'Carbon_Coefficients'!K64
    value = 34539
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L64():
    # 'Carbon_Coefficients'!L64
    value = 36822
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M64():
    # 'Carbon_Coefficients'!M64
    value = 33711
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N64():
    # 'Carbon_Coefficients'!N64
    value = 28833
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O64():
    # 'Carbon_Coefficients'!O64
    value = 27026
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P64():
    # 'Carbon_Coefficients'!P64
    value = 25925
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q64():
    # 'Carbon_Coefficients'!Q64
    value = 30951
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R64():
    # 'Carbon_Coefficients'!R64
    value = 29672
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S64():
    # 'Carbon_Coefficients'!S64
    value = 35180
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T64():
    # 'Carbon_Coefficients'!T64
    value = 47100
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U64():
    # 'Carbon_Coefficients'!U64
    value = 47797
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V64():
    # 'Carbon_Coefficients'!V64
    value = 50294
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W64():
    # 'Carbon_Coefficients'!W64
    value = 42565
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X64():
    # 'Carbon_Coefficients'!X64
    value = 38977
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y64():
    # 'Carbon_Coefficients'!Y64
    value = 54138
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z64():
    # 'Carbon_Coefficients'!Z64
    value = 32042
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA64():
    # 'Carbon_Coefficients'!AA64
    value = 35255
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB64():
    # 'Carbon_Coefficients'!AB64
    value = 39947
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC64():
    # 'Carbon_Coefficients'!AC64
    value = 36779
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD64():
    # 'Carbon_Coefficients'!AD64
    value = 35217
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE64():
    # 'Carbon_Coefficients'!AE64
    value = 33020
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF64():
    # 'Carbon_Coefficients'!AF64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG64():
    # 'Carbon_Coefficients'!AG64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH64():
    # 'Carbon_Coefficients'!AH64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI64():
    # 'Carbon_Coefficients'!AI64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ64():
    # 'Carbon_Coefficients'!AJ64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK64():
    # 'Carbon_Coefficients'!AK64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL64():
    # 'Carbon_Coefficients'!AL64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM64():
    # 'Carbon_Coefficients'!AM64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN64():
    # 'Carbon_Coefficients'!AN64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO64():
    # 'Carbon_Coefficients'!AO64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP64():
    # 'Carbon_Coefficients'!AP64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ64():
    # 'Carbon_Coefficients'!AQ64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR64():
    # 'Carbon_Coefficients'!AR64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS64():
    # 'Carbon_Coefficients'!AS64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT64():
    # 'Carbon_Coefficients'!AT64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU64():
    # 'Carbon_Coefficients'!AU64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV64():
    # 'Carbon_Coefficients'!AV64
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C64,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV64():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c64_1 = Carbon_Coefficients.C64()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c64_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A65():
    # 'Carbon_Coefficients'!A65
    value = "Jet Fuel"

@register(Carbon_Coefficients)
class B65():
    # 'Carbon_Coefficients'!B65
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C65():
    # 'Carbon_Coefficients'!C65
    value = "JFTCb"

@register(Carbon_Coefficients)
class E65():
    # 'Carbon_Coefficients'!E65
    value = 64386
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F65():
    # 'Carbon_Coefficients'!F65
    value = 67174
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G65():
    # 'Carbon_Coefficients'!G65
    value = 74414
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H65():
    # 'Carbon_Coefficients'!H65
    value = 71051
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I65():
    # 'Carbon_Coefficients'!I65
    value = 62557
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J65():
    # 'Carbon_Coefficients'!J65
    value = 56501
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K65():
    # 'Carbon_Coefficients'!K65
    value = 50409
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L65():
    # 'Carbon_Coefficients'!L65
    value = 53705
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M65():
    # 'Carbon_Coefficients'!M65
    value = 56358
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N65():
    # 'Carbon_Coefficients'!N65
    value = 57194
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O65():
    # 'Carbon_Coefficients'!O65
    value = 57955
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P65():
    # 'Carbon_Coefficients'!P65
    value = 56695
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q65():
    # 'Carbon_Coefficients'!Q65
    value = 53720
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R65():
    # 'Carbon_Coefficients'!R65
    value = 53511
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S65():
    # 'Carbon_Coefficients'!S65
    value = 50437
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T65():
    # 'Carbon_Coefficients'!T65
    value = 57774
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U65():
    # 'Carbon_Coefficients'!U65
    value = 72056
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V65():
    # 'Carbon_Coefficients'!V65
    value = 75861
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W65():
    # 'Carbon_Coefficients'!W65
    value = 92831
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X65():
    # 'Carbon_Coefficients'!X65
    value = 86945
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y65():
    # 'Carbon_Coefficients'!Y65
    value = 72329
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z65():
    # 'Carbon_Coefficients'!Z65
    value = 60679
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA65():
    # 'Carbon_Coefficients'!AA65
    value = 52748
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB65():
    # 'Carbon_Coefficients'!AB65
    value = 55775
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC65():
    # 'Carbon_Coefficients'!AC65
    value = 62077
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD65():
    # 'Carbon_Coefficients'!AD65
    value = 64135
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE65():
    # 'Carbon_Coefficients'!AE65
    value = 64201
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF65():
    # 'Carbon_Coefficients'!AF65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG65():
    # 'Carbon_Coefficients'!AG65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH65():
    # 'Carbon_Coefficients'!AH65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI65():
    # 'Carbon_Coefficients'!AI65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ65():
    # 'Carbon_Coefficients'!AJ65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK65():
    # 'Carbon_Coefficients'!AK65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL65():
    # 'Carbon_Coefficients'!AL65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM65():
    # 'Carbon_Coefficients'!AM65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN65():
    # 'Carbon_Coefficients'!AN65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO65():
    # 'Carbon_Coefficients'!AO65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP65():
    # 'Carbon_Coefficients'!AP65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ65():
    # 'Carbon_Coefficients'!AQ65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR65():
    # 'Carbon_Coefficients'!AR65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS65():
    # 'Carbon_Coefficients'!AS65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT65():
    # 'Carbon_Coefficients'!AT65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU65():
    # 'Carbon_Coefficients'!AU65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV65():
    # 'Carbon_Coefficients'!AV65
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C65,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV65():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c65_1 = Carbon_Coefficients.C65()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c65_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A66():
    # 'Carbon_Coefficients'!A66
    value = "Kerosene"

@register(Carbon_Coefficients)
class B66():
    # 'Carbon_Coefficients'!B66
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C66():
    # 'Carbon_Coefficients'!C66
    value = "KSTCb"

@register(Carbon_Coefficients)
class E66():
    # 'Carbon_Coefficients'!E66
    value = 11
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F66():
    # 'Carbon_Coefficients'!F66
    value = 2
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G66():
    # 'Carbon_Coefficients'!G66
    value = 2
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H66():
    # 'Carbon_Coefficients'!H66
    value = 2
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I66():
    # 'Carbon_Coefficients'!I66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J66():
    # 'Carbon_Coefficients'!J66
    value = 2
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K66():
    # 'Carbon_Coefficients'!K66
    value = 6
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L66():
    # 'Carbon_Coefficients'!L66
    value = 4
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M66():
    # 'Carbon_Coefficients'!M66
    value = 3
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N66():
    # 'Carbon_Coefficients'!N66
    value = 3
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O66():
    # 'Carbon_Coefficients'!O66
    value = 3
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P66():
    # 'Carbon_Coefficients'!P66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q66():
    # 'Carbon_Coefficients'!Q66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R66():
    # 'Carbon_Coefficients'!R66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S66():
    # 'Carbon_Coefficients'!S66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T66():
    # 'Carbon_Coefficients'!T66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U66():
    # 'Carbon_Coefficients'!U66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V66():
    # 'Carbon_Coefficients'!V66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W66():
    # 'Carbon_Coefficients'!W66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X66():
    # 'Carbon_Coefficients'!X66
    value = 1
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y66():
    # 'Carbon_Coefficients'!Y66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z66():
    # 'Carbon_Coefficients'!Z66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA66():
    # 'Carbon_Coefficients'!AA66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB66():
    # 'Carbon_Coefficients'!AB66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC66():
    # 'Carbon_Coefficients'!AC66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD66():
    # 'Carbon_Coefficients'!AD66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE66():
    # 'Carbon_Coefficients'!AE66
    value = 0
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF66():
    # 'Carbon_Coefficients'!AF66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG66():
    # 'Carbon_Coefficients'!AG66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH66():
    # 'Carbon_Coefficients'!AH66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI66():
    # 'Carbon_Coefficients'!AI66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ66():
    # 'Carbon_Coefficients'!AJ66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK66():
    # 'Carbon_Coefficients'!AK66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL66():
    # 'Carbon_Coefficients'!AL66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM66():
    # 'Carbon_Coefficients'!AM66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN66():
    # 'Carbon_Coefficients'!AN66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO66():
    # 'Carbon_Coefficients'!AO66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP66():
    # 'Carbon_Coefficients'!AP66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ66():
    # 'Carbon_Coefficients'!AQ66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR66():
    # 'Carbon_Coefficients'!AR66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS66():
    # 'Carbon_Coefficients'!AS66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT66():
    # 'Carbon_Coefficients'!AT66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU66():
    # 'Carbon_Coefficients'!AU66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV66():
    # 'Carbon_Coefficients'!AV66
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C66,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV66():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c66_1 = Carbon_Coefficients.C66()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c66_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A67():
    # 'Carbon_Coefficients'!A67
    value = "LPG"

@register(Carbon_Coefficients)
class B67():
    # 'Carbon_Coefficients'!B67
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C67():
    # 'Carbon_Coefficients'!C67
    value = "LGTCb"

@register(Carbon_Coefficients)
class E67():
    # 'Carbon_Coefficients'!E67
    value = 600
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F67():
    # 'Carbon_Coefficients'!F67
    value = 681
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G67():
    # 'Carbon_Coefficients'!G67
    value = 711
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H67():
    # 'Carbon_Coefficients'!H67
    value = 679
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I67():
    # 'Carbon_Coefficients'!I67
    value = 806
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J67():
    # 'Carbon_Coefficients'!J67
    value = 2462
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K67():
    # 'Carbon_Coefficients'!K67
    value = 3165
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L67():
    # 'Carbon_Coefficients'!L67
    value = 5835
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M67():
    # 'Carbon_Coefficients'!M67
    value = 4730
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N67():
    # 'Carbon_Coefficients'!N67
    value = 4722
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O67():
    # 'Carbon_Coefficients'!O67
    value = 922
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P67():
    # 'Carbon_Coefficients'!P67
    value = 3187
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q67():
    # 'Carbon_Coefficients'!Q67
    value = 1441
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R67():
    # 'Carbon_Coefficients'!R67
    value = 2142
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S67():
    # 'Carbon_Coefficients'!S67
    value = 2214
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T67():
    # 'Carbon_Coefficients'!T67
    value = 2883
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U67():
    # 'Carbon_Coefficients'!U67
    value = 1863
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V67():
    # 'Carbon_Coefficients'!V67
    value = 1755
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W67():
    # 'Carbon_Coefficients'!W67
    value = 1652
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X67():
    # 'Carbon_Coefficients'!X67
    value = 1793
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y67():
    # 'Carbon_Coefficients'!Y67
    value = 1588
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z67():
    # 'Carbon_Coefficients'!Z67
    value = 2584
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA67():
    # 'Carbon_Coefficients'!AA67
    value = 3128
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB67():
    # 'Carbon_Coefficients'!AB67
    value = 3155
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC67():
    # 'Carbon_Coefficients'!AC67
    value = 3447
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD67():
    # 'Carbon_Coefficients'!AD67
    value = 3441
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE67():
    # 'Carbon_Coefficients'!AE67
    value = 3211
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF67():
    # 'Carbon_Coefficients'!AF67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG67():
    # 'Carbon_Coefficients'!AG67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH67():
    # 'Carbon_Coefficients'!AH67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI67():
    # 'Carbon_Coefficients'!AI67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ67():
    # 'Carbon_Coefficients'!AJ67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK67():
    # 'Carbon_Coefficients'!AK67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL67():
    # 'Carbon_Coefficients'!AL67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM67():
    # 'Carbon_Coefficients'!AM67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN67():
    # 'Carbon_Coefficients'!AN67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO67():
    # 'Carbon_Coefficients'!AO67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP67():
    # 'Carbon_Coefficients'!AP67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ67():
    # 'Carbon_Coefficients'!AQ67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR67():
    # 'Carbon_Coefficients'!AR67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS67():
    # 'Carbon_Coefficients'!AS67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT67():
    # 'Carbon_Coefficients'!AT67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU67():
    # 'Carbon_Coefficients'!AU67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV67():
    # 'Carbon_Coefficients'!AV67
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C67,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV67():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c67_1 = Carbon_Coefficients.C67()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c67_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A68():
    # 'Carbon_Coefficients'!A68
    value = "Lubricants"

@register(Carbon_Coefficients)
class B68():
    # 'Carbon_Coefficients'!B68
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C68():
    # 'Carbon_Coefficients'!C68
    value = "LUTCb"

@register(Carbon_Coefficients)
class E68():
    # 'Carbon_Coefficients'!E68
    value = 574
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F68():
    # 'Carbon_Coefficients'!F68
    value = 554
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G68():
    # 'Carbon_Coefficients'!G68
    value = 568
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H68():
    # 'Carbon_Coefficients'!H68
    value = 585
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I68():
    # 'Carbon_Coefficients'!I68
    value = 523
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J68():
    # 'Carbon_Coefficients'!J68
    value = 533
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K68():
    # 'Carbon_Coefficients'!K68
    value = 543
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L68():
    # 'Carbon_Coefficients'!L68
    value = 567
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M68():
    # 'Carbon_Coefficients'!M68
    value = 558
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N68():
    # 'Carbon_Coefficients'!N68
    value = 541
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O68():
    # 'Carbon_Coefficients'!O68
    value = 572
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P68():
    # 'Carbon_Coefficients'!P68
    value = 599
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q68():
    # 'Carbon_Coefficients'!Q68
    value = 605
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R68():
    # 'Carbon_Coefficients'!R68
    value = 596
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S68():
    # 'Carbon_Coefficients'!S68
    value = 546
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T68():
    # 'Carbon_Coefficients'!T68
    value = 539
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U68():
    # 'Carbon_Coefficients'!U68
    value = 499
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V68():
    # 'Carbon_Coefficients'!V68
    value = 505
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W68():
    # 'Carbon_Coefficients'!W68
    value = 503
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X68():
    # 'Carbon_Coefficients'!X68
    value = 490
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y68():
    # 'Carbon_Coefficients'!Y68
    value = 506
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z68():
    # 'Carbon_Coefficients'!Z68
    value = 469
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA68():
    # 'Carbon_Coefficients'!AA68
    value = 422
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB68():
    # 'Carbon_Coefficients'!AB68
    value = 469
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC68():
    # 'Carbon_Coefficients'!AC68
    value = 445
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD68():
    # 'Carbon_Coefficients'!AD68
    value = 409
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE68():
    # 'Carbon_Coefficients'!AE68
    value = 433
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF68():
    # 'Carbon_Coefficients'!AF68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG68():
    # 'Carbon_Coefficients'!AG68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH68():
    # 'Carbon_Coefficients'!AH68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI68():
    # 'Carbon_Coefficients'!AI68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ68():
    # 'Carbon_Coefficients'!AJ68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK68():
    # 'Carbon_Coefficients'!AK68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL68():
    # 'Carbon_Coefficients'!AL68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM68():
    # 'Carbon_Coefficients'!AM68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN68():
    # 'Carbon_Coefficients'!AN68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO68():
    # 'Carbon_Coefficients'!AO68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP68():
    # 'Carbon_Coefficients'!AP68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ68():
    # 'Carbon_Coefficients'!AQ68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR68():
    # 'Carbon_Coefficients'!AR68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS68():
    # 'Carbon_Coefficients'!AS68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT68():
    # 'Carbon_Coefficients'!AT68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU68():
    # 'Carbon_Coefficients'!AU68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV68():
    # 'Carbon_Coefficients'!AV68
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C68,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV68():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c68_1 = Carbon_Coefficients.C68()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c68_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A69():
    # 'Carbon_Coefficients'!A69
    value = "Motor Gasoline"

@register(Carbon_Coefficients)
class B69():
    # 'Carbon_Coefficients'!B69
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C69():
    # 'Carbon_Coefficients'!C69
    value = "MGTCb"

@register(Carbon_Coefficients)
class E69():
    # 'Carbon_Coefficients'!E69
    value = 42998
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F69():
    # 'Carbon_Coefficients'!F69
    value = 44525
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G69():
    # 'Carbon_Coefficients'!G69
    value = 45985
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H69():
    # 'Carbon_Coefficients'!H69
    value = 45543
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I69():
    # 'Carbon_Coefficients'!I69
    value = 47120
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J69():
    # 'Carbon_Coefficients'!J69
    value = 46593
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K69():
    # 'Carbon_Coefficients'!K69
    value = 47590
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L69():
    # 'Carbon_Coefficients'!L69
    value = 48865
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M69():
    # 'Carbon_Coefficients'!M69
    value = 49103
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N69():
    # 'Carbon_Coefficients'!N69
    value = 48892
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O69():
    # 'Carbon_Coefficients'!O69
    value = 48781
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P69():
    # 'Carbon_Coefficients'!P69
    value = 48692
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q69():
    # 'Carbon_Coefficients'!Q69
    value = 46654
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R69():
    # 'Carbon_Coefficients'!R69
    value = 48398
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S69():
    # 'Carbon_Coefficients'!S69
    value = 50587
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T69():
    # 'Carbon_Coefficients'!T69
    value = 54261
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U69():
    # 'Carbon_Coefficients'!U69
    value = 55177
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V69():
    # 'Carbon_Coefficients'!V69
    value = 56014
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W69():
    # 'Carbon_Coefficients'!W69
    value = 57283
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X69():
    # 'Carbon_Coefficients'!X69
    value = 60177
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y69():
    # 'Carbon_Coefficients'!Y69
    value = 59224
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z69():
    # 'Carbon_Coefficients'!Z69
    value = 55704
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA69():
    # 'Carbon_Coefficients'!AA69
    value = 56531
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB69():
    # 'Carbon_Coefficients'!AB69
    value = 52142
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC69():
    # 'Carbon_Coefficients'!AC69
    value = 58154
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD69():
    # 'Carbon_Coefficients'!AD69
    value = 53599
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE69():
    # 'Carbon_Coefficients'!AE69
    value = 54045
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF69():
    # 'Carbon_Coefficients'!AF69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG69():
    # 'Carbon_Coefficients'!AG69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH69():
    # 'Carbon_Coefficients'!AH69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI69():
    # 'Carbon_Coefficients'!AI69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ69():
    # 'Carbon_Coefficients'!AJ69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK69():
    # 'Carbon_Coefficients'!AK69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL69():
    # 'Carbon_Coefficients'!AL69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM69():
    # 'Carbon_Coefficients'!AM69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN69():
    # 'Carbon_Coefficients'!AN69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO69():
    # 'Carbon_Coefficients'!AO69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP69():
    # 'Carbon_Coefficients'!AP69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ69():
    # 'Carbon_Coefficients'!AQ69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR69():
    # 'Carbon_Coefficients'!AR69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS69():
    # 'Carbon_Coefficients'!AS69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT69():
    # 'Carbon_Coefficients'!AT69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU69():
    # 'Carbon_Coefficients'!AU69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV69():
    # 'Carbon_Coefficients'!AV69
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C69,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV69():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c69_1 = Carbon_Coefficients.C69()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c69_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A70():
    # 'Carbon_Coefficients'!A70
    value = "Residual Fuel Oil"

@register(Carbon_Coefficients)
class B70():
    # 'Carbon_Coefficients'!B70
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C70():
    # 'Carbon_Coefficients'!C70
    value = "RFTCb"

@register(Carbon_Coefficients)
class E70():
    # 'Carbon_Coefficients'!E70
    value = 85469
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F70():
    # 'Carbon_Coefficients'!F70
    value = 106471
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G70():
    # 'Carbon_Coefficients'!G70
    value = 109113
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H70():
    # 'Carbon_Coefficients'!H70
    value = 119871
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I70():
    # 'Carbon_Coefficients'!I70
    value = 98072
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J70():
    # 'Carbon_Coefficients'!J70
    value = 112261
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K70():
    # 'Carbon_Coefficients'!K70
    value = 87047
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L70():
    # 'Carbon_Coefficients'!L70
    value = 95060
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M70():
    # 'Carbon_Coefficients'!M70
    value = 90994
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N70():
    # 'Carbon_Coefficients'!N70
    value = 79639
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O70():
    # 'Carbon_Coefficients'!O70
    value = 76812
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P70():
    # 'Carbon_Coefficients'!P70
    value = 83261
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q70():
    # 'Carbon_Coefficients'!Q70
    value = 81383
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R70():
    # 'Carbon_Coefficients'!R70
    value = 85001
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S70():
    # 'Carbon_Coefficients'!S70
    value = 83518
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T70():
    # 'Carbon_Coefficients'!T70
    value = 80086
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U70():
    # 'Carbon_Coefficients'!U70
    value = 75939
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V70():
    # 'Carbon_Coefficients'!V70
    value = 82423
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W70():
    # 'Carbon_Coefficients'!W70
    value = 83048
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X70():
    # 'Carbon_Coefficients'!X70
    value = 92336
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y70():
    # 'Carbon_Coefficients'!Y70
    value = 102594
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z70():
    # 'Carbon_Coefficients'!Z70
    value = 78093
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA70():
    # 'Carbon_Coefficients'!AA70
    value = 77860
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB70():
    # 'Carbon_Coefficients'!AB70
    value = 74747
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC70():
    # 'Carbon_Coefficients'!AC70
    value = 73623
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD70():
    # 'Carbon_Coefficients'!AD70
    value = 67437
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE70():
    # 'Carbon_Coefficients'!AE70
    value = 65250
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF70():
    # 'Carbon_Coefficients'!AF70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG70():
    # 'Carbon_Coefficients'!AG70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH70():
    # 'Carbon_Coefficients'!AH70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI70():
    # 'Carbon_Coefficients'!AI70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ70():
    # 'Carbon_Coefficients'!AJ70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK70():
    # 'Carbon_Coefficients'!AK70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL70():
    # 'Carbon_Coefficients'!AL70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM70():
    # 'Carbon_Coefficients'!AM70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN70():
    # 'Carbon_Coefficients'!AN70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO70():
    # 'Carbon_Coefficients'!AO70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP70():
    # 'Carbon_Coefficients'!AP70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ70():
    # 'Carbon_Coefficients'!AQ70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR70():
    # 'Carbon_Coefficients'!AR70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS70():
    # 'Carbon_Coefficients'!AS70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT70():
    # 'Carbon_Coefficients'!AT70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU70():
    # 'Carbon_Coefficients'!AU70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV70():
    # 'Carbon_Coefficients'!AV70
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C70,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV70():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c70_1 = Carbon_Coefficients.C70()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c70_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A71():
    # 'Carbon_Coefficients'!A71
    value = "Other Petrol Products"

@register(Carbon_Coefficients)
class B71():
    # 'Carbon_Coefficients'!B71
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C71():
    # 'Carbon_Coefficients'!C71
    value = "POTCb"

@register(Carbon_Coefficients)
class E71():
    # 'Carbon_Coefficients'!E71
    value = 9497
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F71():
    # 'Carbon_Coefficients'!F71
    value = 12062
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G71():
    # 'Carbon_Coefficients'!G71
    value = 12425
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H71():
    # 'Carbon_Coefficients'!H71
    value = 13331
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I71():
    # 'Carbon_Coefficients'!I71
    value = 11633
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J71():
    # 'Carbon_Coefficients'!J71
    value = 13829
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K71():
    # 'Carbon_Coefficients'!K71
    value = 12419
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L71():
    # 'Carbon_Coefficients'!L71
    value = 13609
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M71():
    # 'Carbon_Coefficients'!M71
    value = 13053
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N71():
    # 'Carbon_Coefficients'!N71
    value = 15489
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O71():
    # 'Carbon_Coefficients'!O71
    value = 15257
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P71():
    # 'Carbon_Coefficients'!P71
    value = 12595
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q71():
    # 'Carbon_Coefficients'!Q71
    value = 12615
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R71():
    # 'Carbon_Coefficients'!R71
    value = 11752
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S71():
    # 'Carbon_Coefficients'!S71
    value = 14948
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T71():
    # 'Carbon_Coefficients'!T71
    value = 14168
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U71():
    # 'Carbon_Coefficients'!U71
    value = 15439
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V71():
    # 'Carbon_Coefficients'!V71
    value = 15184
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W71():
    # 'Carbon_Coefficients'!W71
    value = 15848
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X71():
    # 'Carbon_Coefficients'!X71
    value = 16323
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y71():
    # 'Carbon_Coefficients'!Y71
    value = 15842
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z71():
    # 'Carbon_Coefficients'!Z71
    value = 13913
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA71():
    # 'Carbon_Coefficients'!AA71
    value = 13803
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB71():
    # 'Carbon_Coefficients'!AB71
    value = 14638
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC71():
    # 'Carbon_Coefficients'!AC71
    value = 15092
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD71():
    # 'Carbon_Coefficients'!AD71
    value = 15606
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE71():
    # 'Carbon_Coefficients'!AE71
    value = 14941
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF71():
    # 'Carbon_Coefficients'!AF71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG71():
    # 'Carbon_Coefficients'!AG71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH71():
    # 'Carbon_Coefficients'!AH71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI71():
    # 'Carbon_Coefficients'!AI71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ71():
    # 'Carbon_Coefficients'!AJ71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK71():
    # 'Carbon_Coefficients'!AK71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL71():
    # 'Carbon_Coefficients'!AL71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM71():
    # 'Carbon_Coefficients'!AM71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN71():
    # 'Carbon_Coefficients'!AN71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO71():
    # 'Carbon_Coefficients'!AO71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP71():
    # 'Carbon_Coefficients'!AP71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ71():
    # 'Carbon_Coefficients'!AQ71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR71():
    # 'Carbon_Coefficients'!AR71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS71():
    # 'Carbon_Coefficients'!AS71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT71():
    # 'Carbon_Coefficients'!AT71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU71():
    # 'Carbon_Coefficients'!AU71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV71():
    # 'Carbon_Coefficients'!AV71
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C71,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV71():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c71_1 = Carbon_Coefficients.C71()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c71_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A72():
    # 'Carbon_Coefficients'!A72
    value = "Total Petroleum"

@register(Carbon_Coefficients)
class B72():
    # 'Carbon_Coefficients'!B72
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C72():
    # 'Carbon_Coefficients'!C72
    value = "PATCb"

@register(Carbon_Coefficients)
class E72():
    # 'Carbon_Coefficients'!E72
    value = 228895
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!E$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def E72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        e60_1 = Carbon_Coefficients.E60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(e60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class F72():
    # 'Carbon_Coefficients'!F72
    value = 268024
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!F$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def F72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        f60_1 = Carbon_Coefficients.F60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(f60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class G72():
    # 'Carbon_Coefficients'!G72
    value = 280098
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!G$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def G72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        g60_1 = Carbon_Coefficients.G60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(g60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class H72():
    # 'Carbon_Coefficients'!H72
    value = 292763
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!H$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def H72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        h60_1 = Carbon_Coefficients.H60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(h60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class I72():
    # 'Carbon_Coefficients'!I72
    value = 266575
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!I$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def I72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        i60_1 = Carbon_Coefficients.I60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(i60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class J72():
    # 'Carbon_Coefficients'!J72
    value = 272492
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!J$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def J72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        j60_1 = Carbon_Coefficients.J60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(j60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class K72():
    # 'Carbon_Coefficients'!K72
    value = 239665
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!K$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def K72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        k60_1 = Carbon_Coefficients.K60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(k60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class L72():
    # 'Carbon_Coefficients'!L72
    value = 258227
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!L$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def L72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        l60_1 = Carbon_Coefficients.L60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(l60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class M72():
    # 'Carbon_Coefficients'!M72
    value = 252516
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!M$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def M72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        m60_1 = Carbon_Coefficients.M60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(m60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class N72():
    # 'Carbon_Coefficients'!N72
    value = 238809
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!N$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def N72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        n60_1 = Carbon_Coefficients.N60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(n60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class O72():
    # 'Carbon_Coefficients'!O72
    value = 230566
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!O$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def O72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        o60_1 = Carbon_Coefficients.O60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(o60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class P72():
    # 'Carbon_Coefficients'!P72
    value = 233635
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!P$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def P72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        p60_1 = Carbon_Coefficients.P60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(p60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Q72():
    # 'Carbon_Coefficients'!Q72
    value = 230004
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Q$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Q72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        q60_1 = Carbon_Coefficients.Q60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(q60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class R72():
    # 'Carbon_Coefficients'!R72
    value = 235308
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!R$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def R72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        r60_1 = Carbon_Coefficients.R60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(r60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class S72():
    # 'Carbon_Coefficients'!S72
    value = 239946
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!S$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def S72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        s60_1 = Carbon_Coefficients.S60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(s60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class T72():
    # 'Carbon_Coefficients'!T72
    value = 257610
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!T$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def T72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        t60_1 = Carbon_Coefficients.T60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(t60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class U72():
    # 'Carbon_Coefficients'!U72
    value = 269578
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!U$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def U72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        u60_1 = Carbon_Coefficients.U60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(u60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class V72():
    # 'Carbon_Coefficients'!V72
    value = 283032
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!V$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def V72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        v60_1 = Carbon_Coefficients.V60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(v60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class W72():
    # 'Carbon_Coefficients'!W72
    value = 295275
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!W$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def W72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        w60_1 = Carbon_Coefficients.W60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(w60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class X72():
    # 'Carbon_Coefficients'!X72
    value = 297270
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!X$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def X72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        x60_1 = Carbon_Coefficients.X60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(x60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Y72():
    # 'Carbon_Coefficients'!Y72
    value = 306445
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Y$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Y72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        y60_1 = Carbon_Coefficients.Y60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(y60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class Z72():
    # 'Carbon_Coefficients'!Z72
    value = 243641
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!Z$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def Z72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        z60_1 = Carbon_Coefficients.Z60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(z60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AA72():
    # 'Carbon_Coefficients'!AA72
    value = 240778
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AA$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AA72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        aa60_1 = Carbon_Coefficients.AA60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aa60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AB72():
    # 'Carbon_Coefficients'!AB72
    value = 241947
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AB$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AB72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ab60_1 = Carbon_Coefficients.AB60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ab60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AC72():
    # 'Carbon_Coefficients'!AC72
    value = 250661
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AC$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AC72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ac60_1 = Carbon_Coefficients.AC60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ac60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AD72():
    # 'Carbon_Coefficients'!AD72
    value = 240835
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AD$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AD72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ad60_1 = Carbon_Coefficients.AD60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ad60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AE72():
    # 'Carbon_Coefficients'!AE72
    value = 236027
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AE$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AE72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ae60_1 = Carbon_Coefficients.AE60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ae60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AF72():
    # 'Carbon_Coefficients'!AF72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AF$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AF72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        af60_1 = Carbon_Coefficients.AF60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(af60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AG72():
    # 'Carbon_Coefficients'!AG72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AG$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AG72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ag60_1 = Carbon_Coefficients.AG60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ag60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AH72():
    # 'Carbon_Coefficients'!AH72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AH$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AH72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ah60_1 = Carbon_Coefficients.AH60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ah60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AI72():
    # 'Carbon_Coefficients'!AI72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AI$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AI72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ai60_1 = Carbon_Coefficients.AI60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ai60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AJ72():
    # 'Carbon_Coefficients'!AJ72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AJ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AJ72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        aj60_1 = Carbon_Coefficients.AJ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aj60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AK72():
    # 'Carbon_Coefficients'!AK72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AK$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AK72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ak60_1 = Carbon_Coefficients.AK60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ak60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AL72():
    # 'Carbon_Coefficients'!AL72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AL$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AL72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        al60_1 = Carbon_Coefficients.AL60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(al60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AM72():
    # 'Carbon_Coefficients'!AM72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AM$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AM72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        am60_1 = Carbon_Coefficients.AM60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(am60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AN72():
    # 'Carbon_Coefficients'!AN72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AN$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AN72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        an60_1 = Carbon_Coefficients.AN60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(an60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AO72():
    # 'Carbon_Coefficients'!AO72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AO$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AO72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ao60_1 = Carbon_Coefficients.AO60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ao60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AP72():
    # 'Carbon_Coefficients'!AP72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AP$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AP72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ap60_1 = Carbon_Coefficients.AP60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ap60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AQ72():
    # 'Carbon_Coefficients'!AQ72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AQ$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AQ72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        aq60_1 = Carbon_Coefficients.AQ60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(aq60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AR72():
    # 'Carbon_Coefficients'!AR72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AR$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AR72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        ar60_1 = Carbon_Coefficients.AR60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(ar60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AS72():
    # 'Carbon_Coefficients'!AS72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AS$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AS72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        as60_1 = Carbon_Coefficients.AS60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(as60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AT72():
    # 'Carbon_Coefficients'!AT72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AT$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AT72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        at60_1 = Carbon_Coefficients.AT60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(at60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AU72():
    # 'Carbon_Coefficients'!AU72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AU$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AU72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        au60_1 = Carbon_Coefficients.AU60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(au60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class AV72():
    # 'Carbon_Coefficients'!AV72
    value = "#N/A"
    formula = "=INDEX('EIA Consumption'!$A$1:$CD$2765,MATCH('Carbon Coefficients'!$C72,'EIA Consumption'!$C$1:$C$765,0),MATCH('Carbon Coefficients'!AV$60,'EIA Consumption'!$A$2:$CD$2,0))"
    @eval_fn
    def AV72():
        range_1 = EIA_Consumption(1, 1, 82, 2765)
        c72_1 = Carbon_Coefficients.C72()
        range_2 = EIA_Consumption(3, 1, 3, 765)
        var_1 = MATCH(c72_1, range_2, 0)
        av60_1 = Carbon_Coefficients.AV60()
        range_3 = EIA_Consumption(1, 2, 82, 2)
        var_2 = MATCH(av60_1, range_3, 0)
        var_3 = INDEX(range_1, var_1, var_2)
        return var_3

@register(Carbon_Coefficients)
class A74():
    # 'Carbon_Coefficients'!A74
    value = "Consumption Weights"

@register(Carbon_Coefficients)
class A75():
    # 'Carbon_Coefficients'!A75
    value = "Asphat"

@register(Carbon_Coefficients)
class B75():
    # 'Carbon_Coefficients'!B75
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C75():
    # 'Carbon_Coefficients'!C75
    value = "ARTCb"

@register(Carbon_Coefficients)
class E75():
    # 'Carbon_Coefficients'!E75
    value = 0.0115161973831
    formula = "=E62/E$72"
    @eval_fn
    def E75():
        e62_1 = Carbon_Coefficients.E62()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e62_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F75():
    # 'Carbon_Coefficients'!F75
    value = 0.00870071336895
    formula = "=F62/F$72"
    @eval_fn
    def F75():
        f62_1 = Carbon_Coefficients.F62()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f62_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G75():
    # 'Carbon_Coefficients'!G75
    value = 0.00701897193125
    formula = "=G62/G$72"
    @eval_fn
    def G75():
        g62_1 = Carbon_Coefficients.G62()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g62_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H75():
    # 'Carbon_Coefficients'!H75
    value = 0.00864180241356
    formula = "=H62/H$72"
    @eval_fn
    def H75():
        h62_1 = Carbon_Coefficients.H62()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h62_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I75():
    # 'Carbon_Coefficients'!I75
    value = 0.00953952921317
    formula = "=I62/I$72"
    @eval_fn
    def I75():
        i62_1 = Carbon_Coefficients.I62()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i62_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J75():
    # 'Carbon_Coefficients'!J75
    value = 0.0104883813103
    formula = "=J62/J$72"
    @eval_fn
    def J75():
        j62_1 = Carbon_Coefficients.J62()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j62_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K75():
    # 'Carbon_Coefficients'!K75
    value = 0.0122921578036
    formula = "=K62/K$72"
    @eval_fn
    def K75():
        k62_1 = Carbon_Coefficients.K62()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k62_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L75():
    # 'Carbon_Coefficients'!L75
    value = 0.0104520441317
    formula = "=L62/L$72"
    @eval_fn
    def L75():
        l62_1 = Carbon_Coefficients.L62()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l62_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M75():
    # 'Carbon_Coefficients'!M75
    value = 0.0115121418049
    formula = "=M62/M$72"
    @eval_fn
    def M75():
        m62_1 = Carbon_Coefficients.M62()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m62_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N75():
    # 'Carbon_Coefficients'!N75
    value = 0.0111511710195
    formula = "=N62/N$72"
    @eval_fn
    def N75():
        n62_1 = Carbon_Coefficients.N62()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n62_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O75():
    # 'Carbon_Coefficients'!O75
    value = 0.0114067121779
    formula = "=O62/O$72"
    @eval_fn
    def O75():
        o62_1 = Carbon_Coefficients.O62()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o62_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P75():
    # 'Carbon_Coefficients'!P75
    value = 0.0091510261733
    formula = "=P62/P$72"
    @eval_fn
    def P75():
        p62_1 = Carbon_Coefficients.P62()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p62_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q75():
    # 'Carbon_Coefficients'!Q75
    value = 0.0101737361089
    formula = "=Q62/Q$72"
    @eval_fn
    def Q75():
        q62_1 = Carbon_Coefficients.Q62()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q62_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R75():
    # 'Carbon_Coefficients'!R75
    value = 0.0170372448026
    formula = "=R62/R$72"
    @eval_fn
    def R75():
        r62_1 = Carbon_Coefficients.R62()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r62_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S75():
    # 'Carbon_Coefficients'!S75
    value = 0.00946462954165
    formula = "=S62/S$72"
    @eval_fn
    def S75():
        s62_1 = Carbon_Coefficients.S62()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s62_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T75():
    # 'Carbon_Coefficients'!T75
    value = 0.0027561041885
    formula = "=T62/T$72"
    @eval_fn
    def T75():
        t62_1 = Carbon_Coefficients.T62()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t62_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U75():
    # 'Carbon_Coefficients'!U75
    value = 0.00271535511058
    formula = "=U62/U$72"
    @eval_fn
    def U75():
        u62_1 = Carbon_Coefficients.U62()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u62_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V75():
    # 'Carbon_Coefficients'!V75
    value = 0.00282300234602
    formula = "=V62/V$72"
    @eval_fn
    def V75():
        v62_1 = Carbon_Coefficients.V62()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v62_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W75():
    # 'Carbon_Coefficients'!W75
    value = 0.00446702226738
    formula = "=W62/W$72"
    @eval_fn
    def W75():
        w62_1 = Carbon_Coefficients.W62()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w62_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X75():
    # 'Carbon_Coefficients'!X75
    value = 7.06428499344e-05
    formula = "=X62/X$72"
    @eval_fn
    def X75():
        x62_1 = Carbon_Coefficients.X62()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x62_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y75():
    # 'Carbon_Coefficients'!Y75
    value = 6.20013379236e-05
    formula = "=Y62/Y$72"
    @eval_fn
    def Y75():
        y62_1 = Carbon_Coefficients.Y62()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y62_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z75():
    # 'Carbon_Coefficients'!Z75
    value = 6.56703920933e-05
    formula = "=Z62/Z$72"
    @eval_fn
    def Z75():
        z62_1 = Carbon_Coefficients.Z62()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z62_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA75():
    # 'Carbon_Coefficients'!AA75
    value = 0.0036631253686
    formula = "=AA62/AA$72"
    @eval_fn
    def AA75():
        aa62_1 = Carbon_Coefficients.AA62()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa62_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB75():
    # 'Carbon_Coefficients'!AB75
    value = 0.00366609216068
    formula = "=AB62/AB$72"
    @eval_fn
    def AB75():
        ab62_1 = Carbon_Coefficients.AB62()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab62_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC75():
    # 'Carbon_Coefficients'!AC75
    value = 0.00346284423983
    formula = "=AC62/AC$72"
    @eval_fn
    def AC75():
        ac62_1 = Carbon_Coefficients.AC62()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac62_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD75():
    # 'Carbon_Coefficients'!AD75
    value = 0.00346710403388
    formula = "=AD62/AD$72"
    @eval_fn
    def AD75():
        ad62_1 = Carbon_Coefficients.AD62()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad62_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE75():
    # 'Carbon_Coefficients'!AE75
    value = 0.0033513115025
    formula = "=AE62/AE$72"
    @eval_fn
    def AE75():
        ae62_1 = Carbon_Coefficients.AE62()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae62_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF75():
    # 'Carbon_Coefficients'!AF75
    value = "#N/A"
    formula = "=AF62/AF$72"
    @eval_fn
    def AF75():
        af62_1 = Carbon_Coefficients.AF62()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af62_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG75():
    # 'Carbon_Coefficients'!AG75
    value = "#N/A"
    formula = "=AG62/AG$72"
    @eval_fn
    def AG75():
        ag62_1 = Carbon_Coefficients.AG62()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag62_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH75():
    # 'Carbon_Coefficients'!AH75
    value = "#N/A"
    formula = "=AH62/AH$72"
    @eval_fn
    def AH75():
        ah62_1 = Carbon_Coefficients.AH62()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah62_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI75():
    # 'Carbon_Coefficients'!AI75
    value = "#N/A"
    formula = "=AI62/AI$72"
    @eval_fn
    def AI75():
        ai62_1 = Carbon_Coefficients.AI62()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai62_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ75():
    # 'Carbon_Coefficients'!AJ75
    value = "#N/A"
    formula = "=AJ62/AJ$72"
    @eval_fn
    def AJ75():
        aj62_1 = Carbon_Coefficients.AJ62()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj62_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK75():
    # 'Carbon_Coefficients'!AK75
    value = "#N/A"
    formula = "=AK62/AK$72"
    @eval_fn
    def AK75():
        ak62_1 = Carbon_Coefficients.AK62()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak62_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL75():
    # 'Carbon_Coefficients'!AL75
    value = "#N/A"
    formula = "=AL62/AL$72"
    @eval_fn
    def AL75():
        al62_1 = Carbon_Coefficients.AL62()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al62_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM75():
    # 'Carbon_Coefficients'!AM75
    value = "#N/A"
    formula = "=AM62/AM$72"
    @eval_fn
    def AM75():
        am62_1 = Carbon_Coefficients.AM62()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am62_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN75():
    # 'Carbon_Coefficients'!AN75
    value = "#N/A"
    formula = "=AN62/AN$72"
    @eval_fn
    def AN75():
        an62_1 = Carbon_Coefficients.AN62()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an62_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO75():
    # 'Carbon_Coefficients'!AO75
    value = "#N/A"
    formula = "=AO62/AO$72"
    @eval_fn
    def AO75():
        ao62_1 = Carbon_Coefficients.AO62()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao62_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP75():
    # 'Carbon_Coefficients'!AP75
    value = "#N/A"
    formula = "=AP62/AP$72"
    @eval_fn
    def AP75():
        ap62_1 = Carbon_Coefficients.AP62()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap62_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ75():
    # 'Carbon_Coefficients'!AQ75
    value = "#N/A"
    formula = "=AQ62/AQ$72"
    @eval_fn
    def AQ75():
        aq62_1 = Carbon_Coefficients.AQ62()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq62_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR75():
    # 'Carbon_Coefficients'!AR75
    value = "#N/A"
    formula = "=AR62/AR$72"
    @eval_fn
    def AR75():
        ar62_1 = Carbon_Coefficients.AR62()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar62_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS75():
    # 'Carbon_Coefficients'!AS75
    value = "#N/A"
    formula = "=AS62/AS$72"
    @eval_fn
    def AS75():
        as62_1 = Carbon_Coefficients.AS62()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as62_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT75():
    # 'Carbon_Coefficients'!AT75
    value = "#N/A"
    formula = "=AT62/AT$72"
    @eval_fn
    def AT75():
        at62_1 = Carbon_Coefficients.AT62()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at62_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU75():
    # 'Carbon_Coefficients'!AU75
    value = "#N/A"
    formula = "=AU62/AU$72"
    @eval_fn
    def AU75():
        au62_1 = Carbon_Coefficients.AU62()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au62_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV75():
    # 'Carbon_Coefficients'!AV75
    value = "#N/A"
    formula = "=AV62/AV$72"
    @eval_fn
    def AV75():
        av62_1 = Carbon_Coefficients.AV62()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av62_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A76():
    # 'Carbon_Coefficients'!A76
    value = "Aviation"

@register(Carbon_Coefficients)
class B76():
    # 'Carbon_Coefficients'!B76
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C76():
    # 'Carbon_Coefficients'!C76
    value = "AVTCb"

@register(Carbon_Coefficients)
class E76():
    # 'Carbon_Coefficients'!E76
    value = 0.00550033858319
    formula = "=E63/E$72"
    @eval_fn
    def E76():
        e63_1 = Carbon_Coefficients.E63()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e63_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F76():
    # 'Carbon_Coefficients'!F76
    value = 0.00529803301197
    formula = "=F63/F$72"
    @eval_fn
    def F76():
        f63_1 = Carbon_Coefficients.F63()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f63_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G76():
    # 'Carbon_Coefficients'!G76
    value = 0.00517318938372
    formula = "=G63/G$72"
    @eval_fn
    def G76():
        g63_1 = Carbon_Coefficients.G63()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g63_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H76():
    # 'Carbon_Coefficients'!H76
    value = 0.0046966317465
    formula = "=H63/H$72"
    @eval_fn
    def H76():
        h63_1 = Carbon_Coefficients.H63()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h63_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I76():
    # 'Carbon_Coefficients'!I76
    value = 0.00495170214761
    formula = "=I63/I$72"
    @eval_fn
    def I76():
        i63_1 = Carbon_Coefficients.I63()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i63_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J76():
    # 'Carbon_Coefficients'!J76
    value = 0.00451022415337
    formula = "=J63/J$72"
    @eval_fn
    def J76():
        j63_1 = Carbon_Coefficients.J63()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j63_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K76():
    # 'Carbon_Coefficients'!K76
    value = 0.0041808357499
    formula = "=K63/K$72"
    @eval_fn
    def K76():
        k63_1 = Carbon_Coefficients.K63()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k63_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L76():
    # 'Carbon_Coefficients'!L76
    value = 0.00410878800435
    formula = "=L63/L$72"
    @eval_fn
    def L76():
        l63_1 = Carbon_Coefficients.L63()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l63_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M76():
    # 'Carbon_Coefficients'!M76
    value = 0.00435615960969
    formula = "=M63/M$72"
    @eval_fn
    def M76():
        m63_1 = Carbon_Coefficients.M63()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m63_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N76():
    # 'Carbon_Coefficients'!N76
    value = 0.00348814324418
    formula = "=N63/N$72"
    @eval_fn
    def N76():
        n63_1 = Carbon_Coefficients.N63()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n63_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O76():
    # 'Carbon_Coefficients'!O76
    value = 0.00264132612788
    formula = "=O63/O$72"
    @eval_fn
    def O76():
        o63_1 = Carbon_Coefficients.O63()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o63_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P76():
    # 'Carbon_Coefficients'!P76
    value = 0.00231129753676
    formula = "=P63/P$72"
    @eval_fn
    def P76():
        p63_1 = Carbon_Coefficients.P63()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p63_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q76():
    # 'Carbon_Coefficients'!Q76
    value = 0.00127823863933
    formula = "=Q63/Q$72"
    @eval_fn
    def Q76():
        q63_1 = Carbon_Coefficients.Q63()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q63_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R76():
    # 'Carbon_Coefficients'!R76
    value = 0.000960443333843
    formula = "=R63/R$72"
    @eval_fn
    def R76():
        r63_1 = Carbon_Coefficients.R63()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r63_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S76():
    # 'Carbon_Coefficients'!S76
    value = 0.00101689546815
    formula = "=S63/S$72"
    @eval_fn
    def S76():
        s63_1 = Carbon_Coefficients.S63()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s63_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T76():
    # 'Carbon_Coefficients'!T76
    value = 0.000345483482784
    formula = "=T63/T$72"
    @eval_fn
    def T76():
        t63_1 = Carbon_Coefficients.T63()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t63_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U76():
    # 'Carbon_Coefficients'!U76
    value = 0.000285631616823
    formula = "=U63/U$72"
    @eval_fn
    def U76():
        u63_1 = Carbon_Coefficients.U63()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u63_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V76():
    # 'Carbon_Coefficients'!V76
    value = 0.000696034370672
    formula = "=V63/V$72"
    @eval_fn
    def V76():
        v63_1 = Carbon_Coefficients.V63()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v63_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W76():
    # 'Carbon_Coefficients'!W76
    value = 0.000758614850563
    formula = "=W63/W$72"
    @eval_fn
    def W76():
        w63_1 = Carbon_Coefficients.W63()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w63_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X76():
    # 'Carbon_Coefficients'!X76
    value = 0.000699700608874
    formula = "=X63/X$72"
    @eval_fn
    def X76():
        x63_1 = Carbon_Coefficients.X63()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x63_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y76():
    # 'Carbon_Coefficients'!Y76
    value = 0.000672225032224
    formula = "=Y63/Y$72"
    @eval_fn
    def Y76():
        y63_1 = Carbon_Coefficients.Y63()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y63_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z76():
    # 'Carbon_Coefficients'!Z76
    value = 0.000574615930816
    formula = "=Z63/Z$72"
    @eval_fn
    def Z76():
        z63_1 = Carbon_Coefficients.Z63()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z63_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA76():
    # 'Carbon_Coefficients'!AA76
    value = 0.000618827301498
    formula = "=AA63/AA$72"
    @eval_fn
    def AA76():
        aa63_1 = Carbon_Coefficients.AA63()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa63_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB76():
    # 'Carbon_Coefficients'!AB76
    value = 0.000777029680054
    formula = "=AB63/AB$72"
    @eval_fn
    def AB76():
        ab63_1 = Carbon_Coefficients.AB63()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab63_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC76():
    # 'Carbon_Coefficients'!AC76
    value = 0.0007021435325
    formula = "=AC63/AC$72"
    @eval_fn
    def AC76():
        ac63_1 = Carbon_Coefficients.AC63()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac63_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD76():
    # 'Carbon_Coefficients'!AD76
    value = 0.000643594161978
    formula = "=AD63/AD$72"
    @eval_fn
    def AD76():
        ad63_1 = Carbon_Coefficients.AD63()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad63_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE76():
    # 'Carbon_Coefficients'!AE76
    value = 0.000576205264652
    formula = "=AE63/AE$72"
    @eval_fn
    def AE76():
        ae63_1 = Carbon_Coefficients.AE63()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae63_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF76():
    # 'Carbon_Coefficients'!AF76
    value = "#N/A"
    formula = "=AF63/AF$72"
    @eval_fn
    def AF76():
        af63_1 = Carbon_Coefficients.AF63()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af63_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG76():
    # 'Carbon_Coefficients'!AG76
    value = "#N/A"
    formula = "=AG63/AG$72"
    @eval_fn
    def AG76():
        ag63_1 = Carbon_Coefficients.AG63()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag63_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH76():
    # 'Carbon_Coefficients'!AH76
    value = "#N/A"
    formula = "=AH63/AH$72"
    @eval_fn
    def AH76():
        ah63_1 = Carbon_Coefficients.AH63()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah63_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI76():
    # 'Carbon_Coefficients'!AI76
    value = "#N/A"
    formula = "=AI63/AI$72"
    @eval_fn
    def AI76():
        ai63_1 = Carbon_Coefficients.AI63()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai63_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ76():
    # 'Carbon_Coefficients'!AJ76
    value = "#N/A"
    formula = "=AJ63/AJ$72"
    @eval_fn
    def AJ76():
        aj63_1 = Carbon_Coefficients.AJ63()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj63_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK76():
    # 'Carbon_Coefficients'!AK76
    value = "#N/A"
    formula = "=AK63/AK$72"
    @eval_fn
    def AK76():
        ak63_1 = Carbon_Coefficients.AK63()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak63_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL76():
    # 'Carbon_Coefficients'!AL76
    value = "#N/A"
    formula = "=AL63/AL$72"
    @eval_fn
    def AL76():
        al63_1 = Carbon_Coefficients.AL63()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al63_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM76():
    # 'Carbon_Coefficients'!AM76
    value = "#N/A"
    formula = "=AM63/AM$72"
    @eval_fn
    def AM76():
        am63_1 = Carbon_Coefficients.AM63()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am63_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN76():
    # 'Carbon_Coefficients'!AN76
    value = "#N/A"
    formula = "=AN63/AN$72"
    @eval_fn
    def AN76():
        an63_1 = Carbon_Coefficients.AN63()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an63_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO76():
    # 'Carbon_Coefficients'!AO76
    value = "#N/A"
    formula = "=AO63/AO$72"
    @eval_fn
    def AO76():
        ao63_1 = Carbon_Coefficients.AO63()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao63_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP76():
    # 'Carbon_Coefficients'!AP76
    value = "#N/A"
    formula = "=AP63/AP$72"
    @eval_fn
    def AP76():
        ap63_1 = Carbon_Coefficients.AP63()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap63_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ76():
    # 'Carbon_Coefficients'!AQ76
    value = "#N/A"
    formula = "=AQ63/AQ$72"
    @eval_fn
    def AQ76():
        aq63_1 = Carbon_Coefficients.AQ63()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq63_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR76():
    # 'Carbon_Coefficients'!AR76
    value = "#N/A"
    formula = "=AR63/AR$72"
    @eval_fn
    def AR76():
        ar63_1 = Carbon_Coefficients.AR63()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar63_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS76():
    # 'Carbon_Coefficients'!AS76
    value = "#N/A"
    formula = "=AS63/AS$72"
    @eval_fn
    def AS76():
        as63_1 = Carbon_Coefficients.AS63()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as63_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT76():
    # 'Carbon_Coefficients'!AT76
    value = "#N/A"
    formula = "=AT63/AT$72"
    @eval_fn
    def AT76():
        at63_1 = Carbon_Coefficients.AT63()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at63_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU76():
    # 'Carbon_Coefficients'!AU76
    value = "#N/A"
    formula = "=AU63/AU$72"
    @eval_fn
    def AU76():
        au63_1 = Carbon_Coefficients.AU63()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au63_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV76():
    # 'Carbon_Coefficients'!AV76
    value = "#N/A"
    formula = "=AV63/AV$72"
    @eval_fn
    def AV76():
        av63_1 = Carbon_Coefficients.AV63()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av63_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A77():
    # 'Carbon_Coefficients'!A77
    value = "Distllate"

@register(Carbon_Coefficients)
class B77():
    # 'Carbon_Coefficients'!B77
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C77():
    # 'Carbon_Coefficients'!C77
    value = "DFTCb"

@register(Carbon_Coefficients)
class E77():
    # 'Carbon_Coefficients'!E77
    value = 0.0937722536534
    formula = "=E64/E$72"
    @eval_fn
    def E77():
        e64_1 = Carbon_Coefficients.E64()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e64_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F77():
    # 'Carbon_Coefficients'!F77
    value = 0.122384562576
    formula = "=F64/F$72"
    @eval_fn
    def F77():
        f64_1 = Carbon_Coefficients.F64()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f64_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G77():
    # 'Carbon_Coefficients'!G77
    value = 0.119476040529
    formula = "=G64/G$72"
    @eval_fn
    def G77():
        g64_1 = Carbon_Coefficients.G64()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g64_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H77():
    # 'Carbon_Coefficients'!H77
    value = 0.129101013448
    formula = "=H64/H$72"
    @eval_fn
    def H77():
        h64_1 = Carbon_Coefficients.H64()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h64_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I77():
    # 'Carbon_Coefficients'!I77
    value = 0.157550407953
    formula = "=I64/I$72"
    @eval_fn
    def I77():
        i64_1 = Carbon_Coefficients.I64()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i64_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J77():
    # 'Carbon_Coefficients'!J77
    value = 0.1329360128
    formula = "=J64/J$72"
    @eval_fn
    def J77():
        j64_1 = Carbon_Coefficients.J64()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j64_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K77():
    # 'Carbon_Coefficients'!K77
    value = 0.144113658649
    formula = "=K64/K$72"
    @eval_fn
    def K77():
        k64_1 = Carbon_Coefficients.K64()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k64_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L77():
    # 'Carbon_Coefficients'!L77
    value = 0.142595468328
    formula = "=L64/L$72"
    @eval_fn
    def L77():
        l64_1 = Carbon_Coefficients.L64()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l64_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M77():
    # 'Carbon_Coefficients'!M77
    value = 0.133500451457
    formula = "=M64/M$72"
    @eval_fn
    def M77():
        m64_1 = Carbon_Coefficients.M64()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m64_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N77():
    # 'Carbon_Coefficients'!N77
    value = 0.120736655654
    formula = "=N64/N$72"
    @eval_fn
    def N77():
        n64_1 = Carbon_Coefficients.N64()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n64_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O77():
    # 'Carbon_Coefficients'!O77
    value = 0.117215894798
    formula = "=O64/O$72"
    @eval_fn
    def O77():
        o64_1 = Carbon_Coefficients.O64()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o64_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P77():
    # 'Carbon_Coefficients'!P77
    value = 0.110963682667
    formula = "=P64/P$72"
    @eval_fn
    def P77():
        p64_1 = Carbon_Coefficients.P64()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p64_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q77():
    # 'Carbon_Coefficients'!Q77
    value = 0.134567224918
    formula = "=Q64/Q$72"
    @eval_fn
    def Q77():
        q64_1 = Carbon_Coefficients.Q64()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q64_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R77():
    # 'Carbon_Coefficients'!R77
    value = 0.126098560185
    formula = "=R64/R$72"
    @eval_fn
    def R77():
        r64_1 = Carbon_Coefficients.R64()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r64_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S77():
    # 'Carbon_Coefficients'!S77
    value = 0.146616322006
    formula = "=S64/S$72"
    @eval_fn
    def S77():
        s64_1 = Carbon_Coefficients.S64()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s64_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T77():
    # 'Carbon_Coefficients'!T77
    value = 0.182834517294
    formula = "=T64/T$72"
    @eval_fn
    def T77():
        t64_1 = Carbon_Coefficients.T64()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t64_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U77():
    # 'Carbon_Coefficients'!U77
    value = 0.177303044017
    formula = "=U64/U$72"
    @eval_fn
    def U77():
        u64_1 = Carbon_Coefficients.U64()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u64_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V77():
    # 'Carbon_Coefficients'!V77
    value = 0.177697221516
    formula = "=V64/V$72"
    @eval_fn
    def V77():
        v64_1 = Carbon_Coefficients.V64()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v64_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W77():
    # 'Carbon_Coefficients'!W77
    value = 0.144153754974
    formula = "=W64/W$72"
    @eval_fn
    def W77():
        w64_1 = Carbon_Coefficients.W64()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w64_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X77():
    # 'Carbon_Coefficients'!X77
    value = 0.131116493423
    formula = "=X64/X$72"
    @eval_fn
    def X77():
        x64_1 = Carbon_Coefficients.X64()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x64_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y77():
    # 'Carbon_Coefficients'!Y77
    value = 0.176664654343
    formula = "=Y64/Y$72"
    @eval_fn
    def Y77():
        y64_1 = Carbon_Coefficients.Y64()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y64_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z77():
    # 'Carbon_Coefficients'!Z77
    value = 0.131513168966
    formula = "=Z64/Z$72"
    @eval_fn
    def Z77():
        z64_1 = Carbon_Coefficients.Z64()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z64_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA77():
    # 'Carbon_Coefficients'!AA77
    value = 0.14642118466
    formula = "=AA64/AA$72"
    @eval_fn
    def AA77():
        aa64_1 = Carbon_Coefficients.AA64()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa64_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB77():
    # 'Carbon_Coefficients'!AB77
    value = 0.165106407602
    formula = "=AB64/AB$72"
    @eval_fn
    def AB77():
        ab64_1 = Carbon_Coefficients.AB64()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab64_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC77():
    # 'Carbon_Coefficients'!AC77
    value = 0.146728051033
    formula = "=AC64/AC$72"
    @eval_fn
    def AC77():
        ac64_1 = Carbon_Coefficients.AC64()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac64_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD77():
    # 'Carbon_Coefficients'!AD77
    value = 0.146228745822
    formula = "=AD64/AD$72"
    @eval_fn
    def AD77():
        ad64_1 = Carbon_Coefficients.AD64()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad64_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE77():
    # 'Carbon_Coefficients'!AE77
    value = 0.139899248815
    formula = "=AE64/AE$72"
    @eval_fn
    def AE77():
        ae64_1 = Carbon_Coefficients.AE64()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae64_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF77():
    # 'Carbon_Coefficients'!AF77
    value = "#N/A"
    formula = "=AF64/AF$72"
    @eval_fn
    def AF77():
        af64_1 = Carbon_Coefficients.AF64()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af64_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG77():
    # 'Carbon_Coefficients'!AG77
    value = "#N/A"
    formula = "=AG64/AG$72"
    @eval_fn
    def AG77():
        ag64_1 = Carbon_Coefficients.AG64()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag64_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH77():
    # 'Carbon_Coefficients'!AH77
    value = "#N/A"
    formula = "=AH64/AH$72"
    @eval_fn
    def AH77():
        ah64_1 = Carbon_Coefficients.AH64()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah64_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI77():
    # 'Carbon_Coefficients'!AI77
    value = "#N/A"
    formula = "=AI64/AI$72"
    @eval_fn
    def AI77():
        ai64_1 = Carbon_Coefficients.AI64()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai64_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ77():
    # 'Carbon_Coefficients'!AJ77
    value = "#N/A"
    formula = "=AJ64/AJ$72"
    @eval_fn
    def AJ77():
        aj64_1 = Carbon_Coefficients.AJ64()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj64_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK77():
    # 'Carbon_Coefficients'!AK77
    value = "#N/A"
    formula = "=AK64/AK$72"
    @eval_fn
    def AK77():
        ak64_1 = Carbon_Coefficients.AK64()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak64_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL77():
    # 'Carbon_Coefficients'!AL77
    value = "#N/A"
    formula = "=AL64/AL$72"
    @eval_fn
    def AL77():
        al64_1 = Carbon_Coefficients.AL64()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al64_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM77():
    # 'Carbon_Coefficients'!AM77
    value = "#N/A"
    formula = "=AM64/AM$72"
    @eval_fn
    def AM77():
        am64_1 = Carbon_Coefficients.AM64()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am64_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN77():
    # 'Carbon_Coefficients'!AN77
    value = "#N/A"
    formula = "=AN64/AN$72"
    @eval_fn
    def AN77():
        an64_1 = Carbon_Coefficients.AN64()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an64_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO77():
    # 'Carbon_Coefficients'!AO77
    value = "#N/A"
    formula = "=AO64/AO$72"
    @eval_fn
    def AO77():
        ao64_1 = Carbon_Coefficients.AO64()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao64_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP77():
    # 'Carbon_Coefficients'!AP77
    value = "#N/A"
    formula = "=AP64/AP$72"
    @eval_fn
    def AP77():
        ap64_1 = Carbon_Coefficients.AP64()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap64_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ77():
    # 'Carbon_Coefficients'!AQ77
    value = "#N/A"
    formula = "=AQ64/AQ$72"
    @eval_fn
    def AQ77():
        aq64_1 = Carbon_Coefficients.AQ64()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq64_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR77():
    # 'Carbon_Coefficients'!AR77
    value = "#N/A"
    formula = "=AR64/AR$72"
    @eval_fn
    def AR77():
        ar64_1 = Carbon_Coefficients.AR64()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar64_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS77():
    # 'Carbon_Coefficients'!AS77
    value = "#N/A"
    formula = "=AS64/AS$72"
    @eval_fn
    def AS77():
        as64_1 = Carbon_Coefficients.AS64()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as64_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT77():
    # 'Carbon_Coefficients'!AT77
    value = "#N/A"
    formula = "=AT64/AT$72"
    @eval_fn
    def AT77():
        at64_1 = Carbon_Coefficients.AT64()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at64_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU77():
    # 'Carbon_Coefficients'!AU77
    value = "#N/A"
    formula = "=AU64/AU$72"
    @eval_fn
    def AU77():
        au64_1 = Carbon_Coefficients.AU64()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au64_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV77():
    # 'Carbon_Coefficients'!AV77
    value = "#N/A"
    formula = "=AV64/AV$72"
    @eval_fn
    def AV77():
        av64_1 = Carbon_Coefficients.AV64()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av64_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A78():
    # 'Carbon_Coefficients'!A78
    value = "Jet Fuel"

@register(Carbon_Coefficients)
class B78():
    # 'Carbon_Coefficients'!B78
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C78():
    # 'Carbon_Coefficients'!C78
    value = "JFTCb"

@register(Carbon_Coefficients)
class E78():
    # 'Carbon_Coefficients'!E78
    value = 0.281290548068
    formula = "=E65/E$72"
    @eval_fn
    def E78():
        e65_1 = Carbon_Coefficients.E65()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e65_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F78():
    # 'Carbon_Coefficients'!F78
    value = 0.250626809539
    formula = "=F65/F$72"
    @eval_fn
    def F78():
        f65_1 = Carbon_Coefficients.F65()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f65_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G78():
    # 'Carbon_Coefficients'!G78
    value = 0.265671300759
    formula = "=G65/G$72"
    @eval_fn
    def G78():
        g65_1 = Carbon_Coefficients.G65()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g65_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H78():
    # 'Carbon_Coefficients'!H78
    value = 0.242691187069
    formula = "=H65/H$72"
    @eval_fn
    def H78():
        h65_1 = Carbon_Coefficients.H65()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h65_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I78():
    # 'Carbon_Coefficients'!I78
    value = 0.234669417612
    formula = "=I65/I$72"
    @eval_fn
    def I78():
        i65_1 = Carbon_Coefficients.I65()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i65_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J78():
    # 'Carbon_Coefficients'!J78
    value = 0.207349206582
    formula = "=J65/J$72"
    @eval_fn
    def J78():
        j65_1 = Carbon_Coefficients.J65()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j65_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K78():
    # 'Carbon_Coefficients'!K78
    value = 0.210331087142
    formula = "=K65/K$72"
    @eval_fn
    def K78():
        k65_1 = Carbon_Coefficients.K65()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k65_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L78():
    # 'Carbon_Coefficients'!L78
    value = 0.207975928156
    formula = "=L65/L$72"
    @eval_fn
    def L78():
        l65_1 = Carbon_Coefficients.L65()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l65_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M78():
    # 'Carbon_Coefficients'!M78
    value = 0.22318585753
    formula = "=M65/M$72"
    @eval_fn
    def M78():
        m65_1 = Carbon_Coefficients.M65()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m65_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N78():
    # 'Carbon_Coefficients'!N78
    value = 0.239496836384
    formula = "=N65/N$72"
    @eval_fn
    def N78():
        n65_1 = Carbon_Coefficients.N65()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n65_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O78():
    # 'Carbon_Coefficients'!O78
    value = 0.25135969744
    formula = "=O65/O$72"
    @eval_fn
    def O78():
        o65_1 = Carbon_Coefficients.O65()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o65_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P78():
    # 'Carbon_Coefficients'!P78
    value = 0.242664840456
    formula = "=P65/P$72"
    @eval_fn
    def P78():
        p65_1 = Carbon_Coefficients.P65()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p65_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q78():
    # 'Carbon_Coefficients'!Q78
    value = 0.233561155458
    formula = "=Q65/Q$72"
    @eval_fn
    def Q78():
        q65_1 = Carbon_Coefficients.Q65()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q65_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R78():
    # 'Carbon_Coefficients'!R78
    value = 0.227408332908
    formula = "=R65/R$72"
    @eval_fn
    def R78():
        r65_1 = Carbon_Coefficients.R65()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r65_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S78():
    # 'Carbon_Coefficients'!S78
    value = 0.210201461996
    formula = "=S65/S$72"
    @eval_fn
    def S78():
        s65_1 = Carbon_Coefficients.S65()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s65_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T78():
    # 'Carbon_Coefficients'!T78
    value = 0.224269244206
    formula = "=T65/T$72"
    @eval_fn
    def T78():
        t65_1 = Carbon_Coefficients.T65()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t65_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U78():
    # 'Carbon_Coefficients'!U78
    value = 0.267291841322
    formula = "=U65/U$72"
    @eval_fn
    def U78():
        u65_1 = Carbon_Coefficients.U65()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u65_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V78():
    # 'Carbon_Coefficients'!V78
    value = 0.268029763419
    formula = "=V65/V$72"
    @eval_fn
    def V78():
        v65_1 = Carbon_Coefficients.V65()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v65_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W78():
    # 'Carbon_Coefficients'!W78
    value = 0.31438828211
    formula = "=W65/W$72"
    @eval_fn
    def W78():
        w65_1 = Carbon_Coefficients.W65()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w65_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X78():
    # 'Carbon_Coefficients'!X78
    value = 0.292478218455
    formula = "=X65/X$72"
    @eval_fn
    def X78():
        x65_1 = Carbon_Coefficients.X65()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x65_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y78():
    # 'Carbon_Coefficients'!Y78
    value = 0.236026040562
    formula = "=Y65/Y$72"
    @eval_fn
    def Y78():
        y65_1 = Carbon_Coefficients.Y65()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y65_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z78():
    # 'Carbon_Coefficients'!Z78
    value = 0.249050857614
    formula = "=Z65/Z$72"
    @eval_fn
    def Z78():
        z65_1 = Carbon_Coefficients.Z65()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z65_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA78():
    # 'Carbon_Coefficients'!AA78
    value = 0.219073171137
    formula = "=AA65/AA$72"
    @eval_fn
    def AA78():
        aa65_1 = Carbon_Coefficients.AA65()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa65_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB78():
    # 'Carbon_Coefficients'!AB78
    value = 0.230525693644
    formula = "=AB65/AB$72"
    @eval_fn
    def AB78():
        ab65_1 = Carbon_Coefficients.AB65()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab65_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC78():
    # 'Carbon_Coefficients'!AC78
    value = 0.247653204926
    formula = "=AC65/AC$72"
    @eval_fn
    def AC78():
        ac65_1 = Carbon_Coefficients.AC65()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac65_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD78():
    # 'Carbon_Coefficients'!AD78
    value = 0.266302655345
    formula = "=AD65/AD$72"
    @eval_fn
    def AD78():
        ad65_1 = Carbon_Coefficients.AD65()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad65_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE78():
    # 'Carbon_Coefficients'!AE78
    value = 0.272007016146
    formula = "=AE65/AE$72"
    @eval_fn
    def AE78():
        ae65_1 = Carbon_Coefficients.AE65()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae65_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF78():
    # 'Carbon_Coefficients'!AF78
    value = "#N/A"
    formula = "=AF65/AF$72"
    @eval_fn
    def AF78():
        af65_1 = Carbon_Coefficients.AF65()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af65_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG78():
    # 'Carbon_Coefficients'!AG78
    value = "#N/A"
    formula = "=AG65/AG$72"
    @eval_fn
    def AG78():
        ag65_1 = Carbon_Coefficients.AG65()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag65_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH78():
    # 'Carbon_Coefficients'!AH78
    value = "#N/A"
    formula = "=AH65/AH$72"
    @eval_fn
    def AH78():
        ah65_1 = Carbon_Coefficients.AH65()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah65_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI78():
    # 'Carbon_Coefficients'!AI78
    value = "#N/A"
    formula = "=AI65/AI$72"
    @eval_fn
    def AI78():
        ai65_1 = Carbon_Coefficients.AI65()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai65_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ78():
    # 'Carbon_Coefficients'!AJ78
    value = "#N/A"
    formula = "=AJ65/AJ$72"
    @eval_fn
    def AJ78():
        aj65_1 = Carbon_Coefficients.AJ65()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj65_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK78():
    # 'Carbon_Coefficients'!AK78
    value = "#N/A"
    formula = "=AK65/AK$72"
    @eval_fn
    def AK78():
        ak65_1 = Carbon_Coefficients.AK65()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak65_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL78():
    # 'Carbon_Coefficients'!AL78
    value = "#N/A"
    formula = "=AL65/AL$72"
    @eval_fn
    def AL78():
        al65_1 = Carbon_Coefficients.AL65()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al65_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM78():
    # 'Carbon_Coefficients'!AM78
    value = "#N/A"
    formula = "=AM65/AM$72"
    @eval_fn
    def AM78():
        am65_1 = Carbon_Coefficients.AM65()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am65_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN78():
    # 'Carbon_Coefficients'!AN78
    value = "#N/A"
    formula = "=AN65/AN$72"
    @eval_fn
    def AN78():
        an65_1 = Carbon_Coefficients.AN65()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an65_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO78():
    # 'Carbon_Coefficients'!AO78
    value = "#N/A"
    formula = "=AO65/AO$72"
    @eval_fn
    def AO78():
        ao65_1 = Carbon_Coefficients.AO65()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao65_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP78():
    # 'Carbon_Coefficients'!AP78
    value = "#N/A"
    formula = "=AP65/AP$72"
    @eval_fn
    def AP78():
        ap65_1 = Carbon_Coefficients.AP65()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap65_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ78():
    # 'Carbon_Coefficients'!AQ78
    value = "#N/A"
    formula = "=AQ65/AQ$72"
    @eval_fn
    def AQ78():
        aq65_1 = Carbon_Coefficients.AQ65()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq65_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR78():
    # 'Carbon_Coefficients'!AR78
    value = "#N/A"
    formula = "=AR65/AR$72"
    @eval_fn
    def AR78():
        ar65_1 = Carbon_Coefficients.AR65()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar65_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS78():
    # 'Carbon_Coefficients'!AS78
    value = "#N/A"
    formula = "=AS65/AS$72"
    @eval_fn
    def AS78():
        as65_1 = Carbon_Coefficients.AS65()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as65_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT78():
    # 'Carbon_Coefficients'!AT78
    value = "#N/A"
    formula = "=AT65/AT$72"
    @eval_fn
    def AT78():
        at65_1 = Carbon_Coefficients.AT65()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at65_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU78():
    # 'Carbon_Coefficients'!AU78
    value = "#N/A"
    formula = "=AU65/AU$72"
    @eval_fn
    def AU78():
        au65_1 = Carbon_Coefficients.AU65()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au65_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV78():
    # 'Carbon_Coefficients'!AV78
    value = "#N/A"
    formula = "=AV65/AV$72"
    @eval_fn
    def AV78():
        av65_1 = Carbon_Coefficients.AV65()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av65_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A79():
    # 'Carbon_Coefficients'!A79
    value = "Kerosene"

@register(Carbon_Coefficients)
class B79():
    # 'Carbon_Coefficients'!B79
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C79():
    # 'Carbon_Coefficients'!C79
    value = "KSTCb"

@register(Carbon_Coefficients)
class E79():
    # 'Carbon_Coefficients'!E79
    value = 4.80569693528e-05
    formula = "=E66/E$72"
    @eval_fn
    def E79():
        e66_1 = Carbon_Coefficients.E66()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e66_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F79():
    # 'Carbon_Coefficients'!F79
    value = 7.46201832672e-06
    formula = "=F66/F$72"
    @eval_fn
    def F79():
        f66_1 = Carbon_Coefficients.F66()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f66_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G79():
    # 'Carbon_Coefficients'!G79
    value = 7.14035801755e-06
    formula = "=G66/G$72"
    @eval_fn
    def G79():
        g66_1 = Carbon_Coefficients.G66()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g66_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H79():
    # 'Carbon_Coefficients'!H79
    value = 6.83146435854e-06
    formula = "=H66/H$72"
    @eval_fn
    def H79():
        h66_1 = Carbon_Coefficients.H66()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h66_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I79():
    # 'Carbon_Coefficients'!I79
    value = 3.75128950577e-06
    formula = "=I66/I$72"
    @eval_fn
    def I79():
        i66_1 = Carbon_Coefficients.I66()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i66_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J79():
    # 'Carbon_Coefficients'!J79
    value = 7.33966501769e-06
    formula = "=J66/J$72"
    @eval_fn
    def J79():
        j66_1 = Carbon_Coefficients.J66()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j66_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K79():
    # 'Carbon_Coefficients'!K79
    value = 2.50349446102e-05
    formula = "=K66/K$72"
    @eval_fn
    def K79():
        k66_1 = Carbon_Coefficients.K66()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k66_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L79():
    # 'Carbon_Coefficients'!L79
    value = 1.54902469533e-05
    formula = "=L66/L$72"
    @eval_fn
    def L79():
        l66_1 = Carbon_Coefficients.L66()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l66_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M79():
    # 'Carbon_Coefficients'!M79
    value = 1.18804352991e-05
    formula = "=M66/M$72"
    @eval_fn
    def M79():
        m66_1 = Carbon_Coefficients.M66()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m66_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N79():
    # 'Carbon_Coefficients'!N79
    value = 1.25623406153e-05
    formula = "=N66/N$72"
    @eval_fn
    def N79():
        n66_1 = Carbon_Coefficients.N66()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n66_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O79():
    # 'Carbon_Coefficients'!O79
    value = 1.3011458758e-05
    formula = "=O66/O$72"
    @eval_fn
    def O79():
        o66_1 = Carbon_Coefficients.O66()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o66_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P79():
    # 'Carbon_Coefficients'!P79
    value = 4.28018062362e-06
    formula = "=P66/P$72"
    @eval_fn
    def P79():
        p66_1 = Carbon_Coefficients.P66()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p66_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q79():
    # 'Carbon_Coefficients'!Q79
    value = 4.3477504739e-06
    formula = "=Q66/Q$72"
    @eval_fn
    def Q79():
        q66_1 = Carbon_Coefficients.Q66()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q66_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R79():
    # 'Carbon_Coefficients'!R79
    value = 4.24974926479e-06
    formula = "=R66/R$72"
    @eval_fn
    def R79():
        r66_1 = Carbon_Coefficients.R66()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r66_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S79():
    # 'Carbon_Coefficients'!S79
    value = 4.16760437765e-06
    formula = "=S66/S$72"
    @eval_fn
    def S79():
        s66_1 = Carbon_Coefficients.S66()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s66_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T79():
    # 'Carbon_Coefficients'!T79
    value = 3.88183688521e-06
    formula = "=T66/T$72"
    @eval_fn
    def T79():
        t66_1 = Carbon_Coefficients.T66()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t66_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U79():
    # 'Carbon_Coefficients'!U79
    value = 3.70950151719e-06
    formula = "=U66/U$72"
    @eval_fn
    def U79():
        u66_1 = Carbon_Coefficients.U66()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u66_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V79():
    # 'Carbon_Coefficients'!V79
    value = 3.53316939427e-06
    formula = "=V66/V$72"
    @eval_fn
    def V79():
        v66_1 = Carbon_Coefficients.V66()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v66_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W79():
    # 'Carbon_Coefficients'!W79
    value = 3.38667344001e-06
    formula = "=W66/W$72"
    @eval_fn
    def W79():
        w66_1 = Carbon_Coefficients.W66()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w66_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X79():
    # 'Carbon_Coefficients'!X79
    value = 3.36394523497e-06
    formula = "=X66/X$72"
    @eval_fn
    def X79():
        x66_1 = Carbon_Coefficients.X66()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x66_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y79():
    # 'Carbon_Coefficients'!Y79
    value = 0
    formula = "=Y66/Y$72"
    @eval_fn
    def Y79():
        y66_1 = Carbon_Coefficients.Y66()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y66_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z79():
    # 'Carbon_Coefficients'!Z79
    value = 0
    formula = "=Z66/Z$72"
    @eval_fn
    def Z79():
        z66_1 = Carbon_Coefficients.Z66()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z66_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA79():
    # 'Carbon_Coefficients'!AA79
    value = 0
    formula = "=AA66/AA$72"
    @eval_fn
    def AA79():
        aa66_1 = Carbon_Coefficients.AA66()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa66_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB79():
    # 'Carbon_Coefficients'!AB79
    value = 0
    formula = "=AB66/AB$72"
    @eval_fn
    def AB79():
        ab66_1 = Carbon_Coefficients.AB66()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab66_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC79():
    # 'Carbon_Coefficients'!AC79
    value = 0
    formula = "=AC66/AC$72"
    @eval_fn
    def AC79():
        ac66_1 = Carbon_Coefficients.AC66()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac66_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD79():
    # 'Carbon_Coefficients'!AD79
    value = 0
    formula = "=AD66/AD$72"
    @eval_fn
    def AD79():
        ad66_1 = Carbon_Coefficients.AD66()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad66_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE79():
    # 'Carbon_Coefficients'!AE79
    value = 0
    formula = "=AE66/AE$72"
    @eval_fn
    def AE79():
        ae66_1 = Carbon_Coefficients.AE66()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae66_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF79():
    # 'Carbon_Coefficients'!AF79
    value = "#N/A"
    formula = "=AF66/AF$72"
    @eval_fn
    def AF79():
        af66_1 = Carbon_Coefficients.AF66()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af66_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG79():
    # 'Carbon_Coefficients'!AG79
    value = "#N/A"
    formula = "=AG66/AG$72"
    @eval_fn
    def AG79():
        ag66_1 = Carbon_Coefficients.AG66()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag66_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH79():
    # 'Carbon_Coefficients'!AH79
    value = "#N/A"
    formula = "=AH66/AH$72"
    @eval_fn
    def AH79():
        ah66_1 = Carbon_Coefficients.AH66()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah66_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI79():
    # 'Carbon_Coefficients'!AI79
    value = "#N/A"
    formula = "=AI66/AI$72"
    @eval_fn
    def AI79():
        ai66_1 = Carbon_Coefficients.AI66()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai66_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ79():
    # 'Carbon_Coefficients'!AJ79
    value = "#N/A"
    formula = "=AJ66/AJ$72"
    @eval_fn
    def AJ79():
        aj66_1 = Carbon_Coefficients.AJ66()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj66_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK79():
    # 'Carbon_Coefficients'!AK79
    value = "#N/A"
    formula = "=AK66/AK$72"
    @eval_fn
    def AK79():
        ak66_1 = Carbon_Coefficients.AK66()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak66_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL79():
    # 'Carbon_Coefficients'!AL79
    value = "#N/A"
    formula = "=AL66/AL$72"
    @eval_fn
    def AL79():
        al66_1 = Carbon_Coefficients.AL66()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al66_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM79():
    # 'Carbon_Coefficients'!AM79
    value = "#N/A"
    formula = "=AM66/AM$72"
    @eval_fn
    def AM79():
        am66_1 = Carbon_Coefficients.AM66()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am66_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN79():
    # 'Carbon_Coefficients'!AN79
    value = "#N/A"
    formula = "=AN66/AN$72"
    @eval_fn
    def AN79():
        an66_1 = Carbon_Coefficients.AN66()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an66_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO79():
    # 'Carbon_Coefficients'!AO79
    value = "#N/A"
    formula = "=AO66/AO$72"
    @eval_fn
    def AO79():
        ao66_1 = Carbon_Coefficients.AO66()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao66_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP79():
    # 'Carbon_Coefficients'!AP79
    value = "#N/A"
    formula = "=AP66/AP$72"
    @eval_fn
    def AP79():
        ap66_1 = Carbon_Coefficients.AP66()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap66_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ79():
    # 'Carbon_Coefficients'!AQ79
    value = "#N/A"
    formula = "=AQ66/AQ$72"
    @eval_fn
    def AQ79():
        aq66_1 = Carbon_Coefficients.AQ66()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq66_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR79():
    # 'Carbon_Coefficients'!AR79
    value = "#N/A"
    formula = "=AR66/AR$72"
    @eval_fn
    def AR79():
        ar66_1 = Carbon_Coefficients.AR66()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar66_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS79():
    # 'Carbon_Coefficients'!AS79
    value = "#N/A"
    formula = "=AS66/AS$72"
    @eval_fn
    def AS79():
        as66_1 = Carbon_Coefficients.AS66()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as66_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT79():
    # 'Carbon_Coefficients'!AT79
    value = "#N/A"
    formula = "=AT66/AT$72"
    @eval_fn
    def AT79():
        at66_1 = Carbon_Coefficients.AT66()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at66_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU79():
    # 'Carbon_Coefficients'!AU79
    value = "#N/A"
    formula = "=AU66/AU$72"
    @eval_fn
    def AU79():
        au66_1 = Carbon_Coefficients.AU66()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au66_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV79():
    # 'Carbon_Coefficients'!AV79
    value = "#N/A"
    formula = "=AV66/AV$72"
    @eval_fn
    def AV79():
        av66_1 = Carbon_Coefficients.AV66()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av66_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A80():
    # 'Carbon_Coefficients'!A80
    value = "LPG"

@register(Carbon_Coefficients)
class B80():
    # 'Carbon_Coefficients'!B80
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C80():
    # 'Carbon_Coefficients'!C80
    value = "LGTCb"

@register(Carbon_Coefficients)
class E80():
    # 'Carbon_Coefficients'!E80
    value = 0.00262128923742
    formula = "=E67/E$72"
    @eval_fn
    def E80():
        e67_1 = Carbon_Coefficients.E67()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e67_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F80():
    # 'Carbon_Coefficients'!F80
    value = 0.00254081724025
    formula = "=F67/F$72"
    @eval_fn
    def F80():
        f67_1 = Carbon_Coefficients.F67()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f67_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G80():
    # 'Carbon_Coefficients'!G80
    value = 0.00253839727524
    formula = "=G67/G$72"
    @eval_fn
    def G80():
        g67_1 = Carbon_Coefficients.G67()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g67_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H80():
    # 'Carbon_Coefficients'!H80
    value = 0.00231928214973
    formula = "=H67/H$72"
    @eval_fn
    def H80():
        h67_1 = Carbon_Coefficients.H67()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h67_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I80():
    # 'Carbon_Coefficients'!I80
    value = 0.00302353934165
    formula = "=I67/I$72"
    @eval_fn
    def I80():
        i67_1 = Carbon_Coefficients.I67()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i67_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J80():
    # 'Carbon_Coefficients'!J80
    value = 0.00903512763677
    formula = "=J67/J$72"
    @eval_fn
    def J80():
        j67_1 = Carbon_Coefficients.J67()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j67_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K80():
    # 'Carbon_Coefficients'!K80
    value = 0.0132059332819
    formula = "=K67/K$72"
    @eval_fn
    def K80():
        k67_1 = Carbon_Coefficients.K67()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k67_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L80():
    # 'Carbon_Coefficients'!L80
    value = 0.0225963977431
    formula = "=L67/L$72"
    @eval_fn
    def L80():
        l67_1 = Carbon_Coefficients.L67()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l67_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M80():
    # 'Carbon_Coefficients'!M80
    value = 0.0187314863217
    formula = "=M67/M$72"
    @eval_fn
    def M80():
        m67_1 = Carbon_Coefficients.M67()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m67_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N80():
    # 'Carbon_Coefficients'!N80
    value = 0.0197731241285
    formula = "=N67/N$72"
    @eval_fn
    def N80():
        n67_1 = Carbon_Coefficients.N67()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n67_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O80():
    # 'Carbon_Coefficients'!O80
    value = 0.00399885499163
    formula = "=O67/O$72"
    @eval_fn
    def O80():
        o67_1 = Carbon_Coefficients.O67()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o67_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P80():
    # 'Carbon_Coefficients'!P80
    value = 0.0136409356475
    formula = "=P67/P$72"
    @eval_fn
    def P80():
        p67_1 = Carbon_Coefficients.P67()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p67_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q80():
    # 'Carbon_Coefficients'!Q80
    value = 0.0062651084329
    formula = "=Q67/Q$72"
    @eval_fn
    def Q80():
        q67_1 = Carbon_Coefficients.Q67()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q67_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R80():
    # 'Carbon_Coefficients'!R80
    value = 0.00910296292519
    formula = "=R67/R$72"
    @eval_fn
    def R80():
        r67_1 = Carbon_Coefficients.R67()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r67_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S80():
    # 'Carbon_Coefficients'!S80
    value = 0.00922707609212
    formula = "=S67/S$72"
    @eval_fn
    def S80():
        s67_1 = Carbon_Coefficients.S67()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s67_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T80():
    # 'Carbon_Coefficients'!T80
    value = 0.0111913357401
    formula = "=T67/T$72"
    @eval_fn
    def T80():
        t67_1 = Carbon_Coefficients.T67()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t67_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U80():
    # 'Carbon_Coefficients'!U80
    value = 0.00691080132652
    formula = "=U67/U$72"
    @eval_fn
    def U80():
        u67_1 = Carbon_Coefficients.U67()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u67_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V80():
    # 'Carbon_Coefficients'!V80
    value = 0.00620071228695
    formula = "=V67/V$72"
    @eval_fn
    def V80():
        v67_1 = Carbon_Coefficients.V67()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v67_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W80():
    # 'Carbon_Coefficients'!W80
    value = 0.0055947845229
    formula = "=W67/W$72"
    @eval_fn
    def W80():
        w67_1 = Carbon_Coefficients.W67()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w67_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X80():
    # 'Carbon_Coefficients'!X80
    value = 0.0060315538063
    formula = "=X67/X$72"
    @eval_fn
    def X80():
        x67_1 = Carbon_Coefficients.X67()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x67_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y80():
    # 'Carbon_Coefficients'!Y80
    value = 0.00518200655909
    formula = "=Y67/Y$72"
    @eval_fn
    def Y80():
        y67_1 = Carbon_Coefficients.Y67()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y67_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z80():
    # 'Carbon_Coefficients'!Z80
    value = 0.0106057683231
    formula = "=Z67/Z$72"
    @eval_fn
    def Z80():
        z67_1 = Carbon_Coefficients.Z67()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z67_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA80():
    # 'Carbon_Coefficients'!AA80
    value = 0.0129912201281
    formula = "=AA67/AA$72"
    @eval_fn
    def AA80():
        aa67_1 = Carbon_Coefficients.AA67()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa67_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB80():
    # 'Carbon_Coefficients'!AB80
    value = 0.0130400459605
    formula = "=AB67/AB$72"
    @eval_fn
    def AB80():
        ab67_1 = Carbon_Coefficients.AB67()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab67_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC80():
    # 'Carbon_Coefficients'!AC80
    value = 0.0137516406621
    formula = "=AC67/AC$72"
    @eval_fn
    def AC80():
        ac67_1 = Carbon_Coefficients.AC67()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac67_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD80():
    # 'Carbon_Coefficients'!AD80
    value = 0.0142877903959
    formula = "=AD67/AD$72"
    @eval_fn
    def AD80():
        ad67_1 = Carbon_Coefficients.AD67()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad67_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE80():
    # 'Carbon_Coefficients'!AE80
    value = 0.0136043757706
    formula = "=AE67/AE$72"
    @eval_fn
    def AE80():
        ae67_1 = Carbon_Coefficients.AE67()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae67_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF80():
    # 'Carbon_Coefficients'!AF80
    value = "#N/A"
    formula = "=AF67/AF$72"
    @eval_fn
    def AF80():
        af67_1 = Carbon_Coefficients.AF67()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af67_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG80():
    # 'Carbon_Coefficients'!AG80
    value = "#N/A"
    formula = "=AG67/AG$72"
    @eval_fn
    def AG80():
        ag67_1 = Carbon_Coefficients.AG67()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag67_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH80():
    # 'Carbon_Coefficients'!AH80
    value = "#N/A"
    formula = "=AH67/AH$72"
    @eval_fn
    def AH80():
        ah67_1 = Carbon_Coefficients.AH67()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah67_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI80():
    # 'Carbon_Coefficients'!AI80
    value = "#N/A"
    formula = "=AI67/AI$72"
    @eval_fn
    def AI80():
        ai67_1 = Carbon_Coefficients.AI67()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai67_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ80():
    # 'Carbon_Coefficients'!AJ80
    value = "#N/A"
    formula = "=AJ67/AJ$72"
    @eval_fn
    def AJ80():
        aj67_1 = Carbon_Coefficients.AJ67()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj67_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK80():
    # 'Carbon_Coefficients'!AK80
    value = "#N/A"
    formula = "=AK67/AK$72"
    @eval_fn
    def AK80():
        ak67_1 = Carbon_Coefficients.AK67()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak67_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL80():
    # 'Carbon_Coefficients'!AL80
    value = "#N/A"
    formula = "=AL67/AL$72"
    @eval_fn
    def AL80():
        al67_1 = Carbon_Coefficients.AL67()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al67_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM80():
    # 'Carbon_Coefficients'!AM80
    value = "#N/A"
    formula = "=AM67/AM$72"
    @eval_fn
    def AM80():
        am67_1 = Carbon_Coefficients.AM67()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am67_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN80():
    # 'Carbon_Coefficients'!AN80
    value = "#N/A"
    formula = "=AN67/AN$72"
    @eval_fn
    def AN80():
        an67_1 = Carbon_Coefficients.AN67()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an67_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO80():
    # 'Carbon_Coefficients'!AO80
    value = "#N/A"
    formula = "=AO67/AO$72"
    @eval_fn
    def AO80():
        ao67_1 = Carbon_Coefficients.AO67()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao67_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP80():
    # 'Carbon_Coefficients'!AP80
    value = "#N/A"
    formula = "=AP67/AP$72"
    @eval_fn
    def AP80():
        ap67_1 = Carbon_Coefficients.AP67()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap67_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ80():
    # 'Carbon_Coefficients'!AQ80
    value = "#N/A"
    formula = "=AQ67/AQ$72"
    @eval_fn
    def AQ80():
        aq67_1 = Carbon_Coefficients.AQ67()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq67_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR80():
    # 'Carbon_Coefficients'!AR80
    value = "#N/A"
    formula = "=AR67/AR$72"
    @eval_fn
    def AR80():
        ar67_1 = Carbon_Coefficients.AR67()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar67_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS80():
    # 'Carbon_Coefficients'!AS80
    value = "#N/A"
    formula = "=AS67/AS$72"
    @eval_fn
    def AS80():
        as67_1 = Carbon_Coefficients.AS67()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as67_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT80():
    # 'Carbon_Coefficients'!AT80
    value = "#N/A"
    formula = "=AT67/AT$72"
    @eval_fn
    def AT80():
        at67_1 = Carbon_Coefficients.AT67()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at67_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU80():
    # 'Carbon_Coefficients'!AU80
    value = "#N/A"
    formula = "=AU67/AU$72"
    @eval_fn
    def AU80():
        au67_1 = Carbon_Coefficients.AU67()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au67_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV80():
    # 'Carbon_Coefficients'!AV80
    value = "#N/A"
    formula = "=AV67/AV$72"
    @eval_fn
    def AV80():
        av67_1 = Carbon_Coefficients.AV67()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av67_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A81():
    # 'Carbon_Coefficients'!A81
    value = "Lubricants"

@register(Carbon_Coefficients)
class B81():
    # 'Carbon_Coefficients'!B81
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C81():
    # 'Carbon_Coefficients'!C81
    value = "LUTCb"

@register(Carbon_Coefficients)
class E81():
    # 'Carbon_Coefficients'!E81
    value = 0.00250770003713
    formula = "=E68/E$72"
    @eval_fn
    def E81():
        e68_1 = Carbon_Coefficients.E68()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e68_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F81():
    # 'Carbon_Coefficients'!F81
    value = 0.0020669790765
    formula = "=F68/F$72"
    @eval_fn
    def F81():
        f68_1 = Carbon_Coefficients.F68()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f68_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G81():
    # 'Carbon_Coefficients'!G81
    value = 0.00202786167698
    formula = "=G68/G$72"
    @eval_fn
    def G81():
        g68_1 = Carbon_Coefficients.G68()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g68_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H81():
    # 'Carbon_Coefficients'!H81
    value = 0.00199820332487
    formula = "=H68/H$72"
    @eval_fn
    def H81():
        h68_1 = Carbon_Coefficients.H68()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h68_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I81():
    # 'Carbon_Coefficients'!I81
    value = 0.00196192441152
    formula = "=I68/I$72"
    @eval_fn
    def I81():
        i68_1 = Carbon_Coefficients.I68()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i68_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J81():
    # 'Carbon_Coefficients'!J81
    value = 0.00195602072721
    formula = "=J68/J$72"
    @eval_fn
    def J81():
        j68_1 = Carbon_Coefficients.J68()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j68_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K81():
    # 'Carbon_Coefficients'!K81
    value = 0.00226566248722
    formula = "=K68/K$72"
    @eval_fn
    def K81():
        k68_1 = Carbon_Coefficients.K68()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k68_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L81():
    # 'Carbon_Coefficients'!L81
    value = 0.00219574250562
    formula = "=L68/L$72"
    @eval_fn
    def L81():
        l68_1 = Carbon_Coefficients.L68()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l68_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M81():
    # 'Carbon_Coefficients'!M81
    value = 0.00220976096564
    formula = "=M68/M$72"
    @eval_fn
    def M81():
        m68_1 = Carbon_Coefficients.M68()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m68_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N81():
    # 'Carbon_Coefficients'!N81
    value = 0.00226540875763
    formula = "=N68/N$72"
    @eval_fn
    def N81():
        n68_1 = Carbon_Coefficients.N68()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n68_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O81():
    # 'Carbon_Coefficients'!O81
    value = 0.00248085146986
    formula = "=O68/O$72"
    @eval_fn
    def O81():
        o68_1 = Carbon_Coefficients.O68()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o68_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P81():
    # 'Carbon_Coefficients'!P81
    value = 0.00256382819355
    formula = "=P68/P$72"
    @eval_fn
    def P81():
        p68_1 = Carbon_Coefficients.P68()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p68_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q81():
    # 'Carbon_Coefficients'!Q81
    value = 0.00263038903671
    formula = "=Q68/Q$72"
    @eval_fn
    def Q81():
        q68_1 = Carbon_Coefficients.Q68()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q68_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R81():
    # 'Carbon_Coefficients'!R81
    value = 0.00253285056182
    formula = "=R68/R$72"
    @eval_fn
    def R81():
        r68_1 = Carbon_Coefficients.R68()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r68_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S81():
    # 'Carbon_Coefficients'!S81
    value = 0.0022755119902
    formula = "=S68/S$72"
    @eval_fn
    def S81():
        s68_1 = Carbon_Coefficients.S68()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s68_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T81():
    # 'Carbon_Coefficients'!T81
    value = 0.00209231008113
    formula = "=T68/T$72"
    @eval_fn
    def T81():
        t68_1 = Carbon_Coefficients.T68()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t68_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U81():
    # 'Carbon_Coefficients'!U81
    value = 0.00185104125708
    formula = "=U68/U$72"
    @eval_fn
    def U81():
        u68_1 = Carbon_Coefficients.U68()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u68_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V81():
    # 'Carbon_Coefficients'!V81
    value = 0.00178425054411
    formula = "=V68/V$72"
    @eval_fn
    def V81():
        v68_1 = Carbon_Coefficients.V68()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v68_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W81():
    # 'Carbon_Coefficients'!W81
    value = 0.00170349674033
    formula = "=W68/W$72"
    @eval_fn
    def W81():
        w68_1 = Carbon_Coefficients.W68()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w68_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X81():
    # 'Carbon_Coefficients'!X81
    value = 0.00164833316514
    formula = "=X68/X$72"
    @eval_fn
    def X81():
        x68_1 = Carbon_Coefficients.X68()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x68_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y81():
    # 'Carbon_Coefficients'!Y81
    value = 0.00165119352576
    formula = "=Y68/Y$72"
    @eval_fn
    def Y81():
        y68_1 = Carbon_Coefficients.Y68()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y68_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z81():
    # 'Carbon_Coefficients'!Z81
    value = 0.00192496336823
    formula = "=Z68/Z$72"
    @eval_fn
    def Z81():
        z68_1 = Carbon_Coefficients.Z68()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z68_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA81():
    # 'Carbon_Coefficients'!AA81
    value = 0.00175265182035
    formula = "=AA68/AA$72"
    @eval_fn
    def AA81():
        aa68_1 = Carbon_Coefficients.AA68()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa68_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB81():
    # 'Carbon_Coefficients'!AB81
    value = 0.00193844106354
    formula = "=AB68/AB$72"
    @eval_fn
    def AB81():
        ab68_1 = Carbon_Coefficients.AB68()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab68_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC81():
    # 'Carbon_Coefficients'!AC81
    value = 0.0017753060907
    formula = "=AC68/AC$72"
    @eval_fn
    def AC81():
        ac68_1 = Carbon_Coefficients.AC68()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac68_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD81():
    # 'Carbon_Coefficients'!AD81
    value = 0.00169825814354
    formula = "=AD68/AD$72"
    @eval_fn
    def AD81():
        ad68_1 = Carbon_Coefficients.AD68()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad68_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE81():
    # 'Carbon_Coefficients'!AE81
    value = 0.00183453587937
    formula = "=AE68/AE$72"
    @eval_fn
    def AE81():
        ae68_1 = Carbon_Coefficients.AE68()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae68_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF81():
    # 'Carbon_Coefficients'!AF81
    value = "#N/A"
    formula = "=AF68/AF$72"
    @eval_fn
    def AF81():
        af68_1 = Carbon_Coefficients.AF68()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af68_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG81():
    # 'Carbon_Coefficients'!AG81
    value = "#N/A"
    formula = "=AG68/AG$72"
    @eval_fn
    def AG81():
        ag68_1 = Carbon_Coefficients.AG68()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag68_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH81():
    # 'Carbon_Coefficients'!AH81
    value = "#N/A"
    formula = "=AH68/AH$72"
    @eval_fn
    def AH81():
        ah68_1 = Carbon_Coefficients.AH68()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah68_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI81():
    # 'Carbon_Coefficients'!AI81
    value = "#N/A"
    formula = "=AI68/AI$72"
    @eval_fn
    def AI81():
        ai68_1 = Carbon_Coefficients.AI68()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai68_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ81():
    # 'Carbon_Coefficients'!AJ81
    value = "#N/A"
    formula = "=AJ68/AJ$72"
    @eval_fn
    def AJ81():
        aj68_1 = Carbon_Coefficients.AJ68()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj68_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK81():
    # 'Carbon_Coefficients'!AK81
    value = "#N/A"
    formula = "=AK68/AK$72"
    @eval_fn
    def AK81():
        ak68_1 = Carbon_Coefficients.AK68()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak68_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL81():
    # 'Carbon_Coefficients'!AL81
    value = "#N/A"
    formula = "=AL68/AL$72"
    @eval_fn
    def AL81():
        al68_1 = Carbon_Coefficients.AL68()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al68_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM81():
    # 'Carbon_Coefficients'!AM81
    value = "#N/A"
    formula = "=AM68/AM$72"
    @eval_fn
    def AM81():
        am68_1 = Carbon_Coefficients.AM68()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am68_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN81():
    # 'Carbon_Coefficients'!AN81
    value = "#N/A"
    formula = "=AN68/AN$72"
    @eval_fn
    def AN81():
        an68_1 = Carbon_Coefficients.AN68()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an68_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO81():
    # 'Carbon_Coefficients'!AO81
    value = "#N/A"
    formula = "=AO68/AO$72"
    @eval_fn
    def AO81():
        ao68_1 = Carbon_Coefficients.AO68()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao68_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP81():
    # 'Carbon_Coefficients'!AP81
    value = "#N/A"
    formula = "=AP68/AP$72"
    @eval_fn
    def AP81():
        ap68_1 = Carbon_Coefficients.AP68()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap68_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ81():
    # 'Carbon_Coefficients'!AQ81
    value = "#N/A"
    formula = "=AQ68/AQ$72"
    @eval_fn
    def AQ81():
        aq68_1 = Carbon_Coefficients.AQ68()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq68_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR81():
    # 'Carbon_Coefficients'!AR81
    value = "#N/A"
    formula = "=AR68/AR$72"
    @eval_fn
    def AR81():
        ar68_1 = Carbon_Coefficients.AR68()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar68_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS81():
    # 'Carbon_Coefficients'!AS81
    value = "#N/A"
    formula = "=AS68/AS$72"
    @eval_fn
    def AS81():
        as68_1 = Carbon_Coefficients.AS68()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as68_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT81():
    # 'Carbon_Coefficients'!AT81
    value = "#N/A"
    formula = "=AT68/AT$72"
    @eval_fn
    def AT81():
        at68_1 = Carbon_Coefficients.AT68()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at68_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU81():
    # 'Carbon_Coefficients'!AU81
    value = "#N/A"
    formula = "=AU68/AU$72"
    @eval_fn
    def AU81():
        au68_1 = Carbon_Coefficients.AU68()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au68_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV81():
    # 'Carbon_Coefficients'!AV81
    value = "#N/A"
    formula = "=AV68/AV$72"
    @eval_fn
    def AV81():
        av68_1 = Carbon_Coefficients.AV68()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av68_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A82():
    # 'Carbon_Coefficients'!A82
    value = "Motor Gasoline"

@register(Carbon_Coefficients)
class B82():
    # 'Carbon_Coefficients'!B82
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C82():
    # 'Carbon_Coefficients'!C82
    value = "MGTCb"

@register(Carbon_Coefficients)
class E82():
    # 'Carbon_Coefficients'!E82
    value = 0.187850324385
    formula = "=E69/E$72"
    @eval_fn
    def E82():
        e69_1 = Carbon_Coefficients.E69()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e69_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F82():
    # 'Carbon_Coefficients'!F82
    value = 0.166123182999
    formula = "=F69/F$72"
    @eval_fn
    def F82():
        f69_1 = Carbon_Coefficients.F69()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f69_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G82():
    # 'Carbon_Coefficients'!G82
    value = 0.164174681719
    formula = "=G69/G$72"
    @eval_fn
    def G82():
        g69_1 = Carbon_Coefficients.G69()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g69_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H82():
    # 'Carbon_Coefficients'!H82
    value = 0.155562690641
    formula = "=H69/H$72"
    @eval_fn
    def H82():
        h69_1 = Carbon_Coefficients.H69()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h69_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I82():
    # 'Carbon_Coefficients'!I82
    value = 0.176760761512
    formula = "=I69/I$72"
    @eval_fn
    def I82():
        i69_1 = Carbon_Coefficients.I69()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i69_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J82():
    # 'Carbon_Coefficients'!J82
    value = 0.170988506085
    formula = "=J69/J$72"
    @eval_fn
    def J82():
        j69_1 = Carbon_Coefficients.J69()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j69_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K82():
    # 'Carbon_Coefficients'!K82
    value = 0.198568835666
    formula = "=K69/K$72"
    @eval_fn
    def K82():
        k69_1 = Carbon_Coefficients.K69()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k69_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L82():
    # 'Carbon_Coefficients'!L82
    value = 0.189232729343
    formula = "=L69/L$72"
    @eval_fn
    def L82():
        l69_1 = Carbon_Coefficients.L69()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l69_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M82():
    # 'Carbon_Coefficients'!M82
    value = 0.194455004831
    formula = "=M69/M$72"
    @eval_fn
    def M82():
        m69_1 = Carbon_Coefficients.M69()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m69_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N82():
    # 'Carbon_Coefficients'!N82
    value = 0.204732652454
    formula = "=N69/N$72"
    @eval_fn
    def N82():
        n69_1 = Carbon_Coefficients.N69()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n69_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O82():
    # 'Carbon_Coefficients'!O82
    value = 0.211570656558
    formula = "=O69/O$72"
    @eval_fn
    def O82():
        o69_1 = Carbon_Coefficients.O69()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o69_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P82():
    # 'Carbon_Coefficients'!P82
    value = 0.208410554925
    formula = "=P69/P$72"
    @eval_fn
    def P82():
        p69_1 = Carbon_Coefficients.P69()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p69_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q82():
    # 'Carbon_Coefficients'!Q82
    value = 0.20283995061
    formula = "=Q69/Q$72"
    @eval_fn
    def Q82():
        q69_1 = Carbon_Coefficients.Q69()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q69_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R82():
    # 'Carbon_Coefficients'!R82
    value = 0.205679364917
    formula = "=R69/R$72"
    @eval_fn
    def R82():
        r69_1 = Carbon_Coefficients.R69()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r69_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S82():
    # 'Carbon_Coefficients'!S82
    value = 0.210826602652
    formula = "=S69/S$72"
    @eval_fn
    def S82():
        s69_1 = Carbon_Coefficients.S69()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s69_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T82():
    # 'Carbon_Coefficients'!T82
    value = 0.210632351229
    formula = "=T69/T$72"
    @eval_fn
    def T82():
        t69_1 = Carbon_Coefficients.T69()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t69_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U82():
    # 'Carbon_Coefficients'!U82
    value = 0.204679165214
    formula = "=U69/U$72"
    @eval_fn
    def U82():
        u69_1 = Carbon_Coefficients.U69()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u69_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V82():
    # 'Carbon_Coefficients'!V82
    value = 0.197906950451
    formula = "=V69/V$72"
    @eval_fn
    def V82():
        v69_1 = Carbon_Coefficients.V69()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v69_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W82():
    # 'Carbon_Coefficients'!W82
    value = 0.193998814664
    formula = "=W69/W$72"
    @eval_fn
    def W82():
        w69_1 = Carbon_Coefficients.W69()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w69_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X82():
    # 'Carbon_Coefficients'!X82
    value = 0.202432132405
    formula = "=X69/X$72"
    @eval_fn
    def X82():
        x69_1 = Carbon_Coefficients.X69()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x69_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y82():
    # 'Carbon_Coefficients'!Y82
    value = 0.193261433536
    formula = "=Y69/Y$72"
    @eval_fn
    def Y82():
        y69_1 = Carbon_Coefficients.Y69()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y69_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z82():
    # 'Carbon_Coefficients'!Z82
    value = 0.228631470073
    formula = "=Z69/Z$72"
    @eval_fn
    def Z82():
        z69_1 = Carbon_Coefficients.Z69()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z69_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA82():
    # 'Carbon_Coefficients'!AA82
    value = 0.23478473947
    formula = "=AA69/AA$72"
    @eval_fn
    def AA82():
        aa69_1 = Carbon_Coefficients.AA69()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa69_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB82():
    # 'Carbon_Coefficients'!AB82
    value = 0.21551000839
    formula = "=AB69/AB$72"
    @eval_fn
    def AB82():
        ab69_1 = Carbon_Coefficients.AB69()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab69_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC82():
    # 'Carbon_Coefficients'!AC82
    value = 0.232002585165
    formula = "=AC69/AC$72"
    @eval_fn
    def AC82():
        ac69_1 = Carbon_Coefficients.AC69()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac69_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD82():
    # 'Carbon_Coefficients'!AD82
    value = 0.222554861212
    formula = "=AD69/AD$72"
    @eval_fn
    def AD82():
        ad69_1 = Carbon_Coefficients.AD69()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad69_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE82():
    # 'Carbon_Coefficients'!AE82
    value = 0.228978040648
    formula = "=AE69/AE$72"
    @eval_fn
    def AE82():
        ae69_1 = Carbon_Coefficients.AE69()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae69_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF82():
    # 'Carbon_Coefficients'!AF82
    value = "#N/A"
    formula = "=AF69/AF$72"
    @eval_fn
    def AF82():
        af69_1 = Carbon_Coefficients.AF69()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af69_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG82():
    # 'Carbon_Coefficients'!AG82
    value = "#N/A"
    formula = "=AG69/AG$72"
    @eval_fn
    def AG82():
        ag69_1 = Carbon_Coefficients.AG69()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag69_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH82():
    # 'Carbon_Coefficients'!AH82
    value = "#N/A"
    formula = "=AH69/AH$72"
    @eval_fn
    def AH82():
        ah69_1 = Carbon_Coefficients.AH69()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah69_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI82():
    # 'Carbon_Coefficients'!AI82
    value = "#N/A"
    formula = "=AI69/AI$72"
    @eval_fn
    def AI82():
        ai69_1 = Carbon_Coefficients.AI69()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai69_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ82():
    # 'Carbon_Coefficients'!AJ82
    value = "#N/A"
    formula = "=AJ69/AJ$72"
    @eval_fn
    def AJ82():
        aj69_1 = Carbon_Coefficients.AJ69()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj69_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK82():
    # 'Carbon_Coefficients'!AK82
    value = "#N/A"
    formula = "=AK69/AK$72"
    @eval_fn
    def AK82():
        ak69_1 = Carbon_Coefficients.AK69()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak69_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL82():
    # 'Carbon_Coefficients'!AL82
    value = "#N/A"
    formula = "=AL69/AL$72"
    @eval_fn
    def AL82():
        al69_1 = Carbon_Coefficients.AL69()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al69_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM82():
    # 'Carbon_Coefficients'!AM82
    value = "#N/A"
    formula = "=AM69/AM$72"
    @eval_fn
    def AM82():
        am69_1 = Carbon_Coefficients.AM69()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am69_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN82():
    # 'Carbon_Coefficients'!AN82
    value = "#N/A"
    formula = "=AN69/AN$72"
    @eval_fn
    def AN82():
        an69_1 = Carbon_Coefficients.AN69()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an69_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO82():
    # 'Carbon_Coefficients'!AO82
    value = "#N/A"
    formula = "=AO69/AO$72"
    @eval_fn
    def AO82():
        ao69_1 = Carbon_Coefficients.AO69()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao69_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP82():
    # 'Carbon_Coefficients'!AP82
    value = "#N/A"
    formula = "=AP69/AP$72"
    @eval_fn
    def AP82():
        ap69_1 = Carbon_Coefficients.AP69()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap69_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ82():
    # 'Carbon_Coefficients'!AQ82
    value = "#N/A"
    formula = "=AQ69/AQ$72"
    @eval_fn
    def AQ82():
        aq69_1 = Carbon_Coefficients.AQ69()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq69_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR82():
    # 'Carbon_Coefficients'!AR82
    value = "#N/A"
    formula = "=AR69/AR$72"
    @eval_fn
    def AR82():
        ar69_1 = Carbon_Coefficients.AR69()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar69_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS82():
    # 'Carbon_Coefficients'!AS82
    value = "#N/A"
    formula = "=AS69/AS$72"
    @eval_fn
    def AS82():
        as69_1 = Carbon_Coefficients.AS69()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as69_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT82():
    # 'Carbon_Coefficients'!AT82
    value = "#N/A"
    formula = "=AT69/AT$72"
    @eval_fn
    def AT82():
        at69_1 = Carbon_Coefficients.AT69()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at69_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU82():
    # 'Carbon_Coefficients'!AU82
    value = "#N/A"
    formula = "=AU69/AU$72"
    @eval_fn
    def AU82():
        au69_1 = Carbon_Coefficients.AU69()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au69_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV82():
    # 'Carbon_Coefficients'!AV82
    value = "#N/A"
    formula = "=AV69/AV$72"
    @eval_fn
    def AV82():
        av69_1 = Carbon_Coefficients.AV69()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av69_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A83():
    # 'Carbon_Coefficients'!A83
    value = "Residual Fuel Oil"

@register(Carbon_Coefficients)
class B83():
    # 'Carbon_Coefficients'!B83
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C83():
    # 'Carbon_Coefficients'!C83
    value = "RFTCb"

@register(Carbon_Coefficients)
class E83():
    # 'Carbon_Coefficients'!E83
    value = 0.373398283056
    formula = "=E70/E$72"
    @eval_fn
    def E83():
        e70_1 = Carbon_Coefficients.E70()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e70_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F83():
    # 'Carbon_Coefficients'!F83
    value = 0.397244276632
    formula = "=F70/F$72"
    @eval_fn
    def F83():
        f70_1 = Carbon_Coefficients.F70()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f70_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G83():
    # 'Carbon_Coefficients'!G83
    value = 0.389552942185
    formula = "=G70/G$72"
    @eval_fn
    def G83():
        g70_1 = Carbon_Coefficients.G70()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g70_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H83():
    # 'Carbon_Coefficients'!H83
    value = 0.409447232061
    formula = "=H70/H$72"
    @eval_fn
    def H83():
        h70_1 = Carbon_Coefficients.H70()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h70_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I83():
    # 'Carbon_Coefficients'!I83
    value = 0.36789646441
    formula = "=I70/I$72"
    @eval_fn
    def I83():
        i70_1 = Carbon_Coefficients.I70()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i70_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J83():
    # 'Carbon_Coefficients'!J83
    value = 0.411979067275
    formula = "=J70/J$72"
    @eval_fn
    def J83():
        j70_1 = Carbon_Coefficients.J70()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j70_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K83():
    # 'Carbon_Coefficients'!K83
    value = 0.363202803914
    formula = "=K70/K$72"
    @eval_fn
    def K83():
        k70_1 = Carbon_Coefficients.K70()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k70_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L83():
    # 'Carbon_Coefficients'!L83
    value = 0.368125718844
    formula = "=L70/L$72"
    @eval_fn
    def L83():
        l70_1 = Carbon_Coefficients.L70()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l70_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M83():
    # 'Carbon_Coefficients'!M83
    value = 0.360349443204
    formula = "=M70/M$72"
    @eval_fn
    def M83():
        m70_1 = Carbon_Coefficients.M70()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m70_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N83():
    # 'Carbon_Coefficients'!N83
    value = 0.333484081421
    formula = "=N70/N$72"
    @eval_fn
    def N83():
        n70_1 = Carbon_Coefficients.N70()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n70_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O83():
    # 'Carbon_Coefficients'!O83
    value = 0.33314539004
    formula = "=O70/O$72"
    @eval_fn
    def O83():
        o70_1 = Carbon_Coefficients.O70()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o70_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P83():
    # 'Carbon_Coefficients'!P83
    value = 0.356372118903
    formula = "=P70/P$72"
    @eval_fn
    def P83():
        p70_1 = Carbon_Coefficients.P70()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p70_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q83():
    # 'Carbon_Coefficients'!Q83
    value = 0.353832976818
    formula = "=Q70/Q$72"
    @eval_fn
    def Q83():
        q70_1 = Carbon_Coefficients.Q70()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q70_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R83():
    # 'Carbon_Coefficients'!R83
    value = 0.361232937257
    formula = "=R70/R$72"
    @eval_fn
    def R83():
        r70_1 = Carbon_Coefficients.R70()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r70_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S83():
    # 'Carbon_Coefficients'!S83
    value = 0.348069982413
    formula = "=S70/S$72"
    @eval_fn
    def S83():
        s70_1 = Carbon_Coefficients.S70()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s70_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T83():
    # 'Carbon_Coefficients'!T83
    value = 0.310880788789
    formula = "=T70/T$72"
    @eval_fn
    def T83():
        t70_1 = Carbon_Coefficients.T70()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t70_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U83():
    # 'Carbon_Coefficients'!U83
    value = 0.281695835714
    formula = "=U70/U$72"
    @eval_fn
    def U83():
        u70_1 = Carbon_Coefficients.U70()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u70_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V83():
    # 'Carbon_Coefficients'!V83
    value = 0.291214420984
    formula = "=V70/V$72"
    @eval_fn
    def V83():
        v70_1 = Carbon_Coefficients.V70()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v70_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W83():
    # 'Carbon_Coefficients'!W83
    value = 0.281256455846
    formula = "=W70/W$72"
    @eval_fn
    def W83():
        w70_1 = Carbon_Coefficients.W70()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w70_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X83():
    # 'Carbon_Coefficients'!X83
    value = 0.310613247216
    formula = "=X70/X$72"
    @eval_fn
    def X83():
        x70_1 = Carbon_Coefficients.X70()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x70_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y83():
    # 'Carbon_Coefficients'!Y83
    value = 0.334787645418
    formula = "=Y70/Y$72"
    @eval_fn
    def Y83():
        y70_1 = Carbon_Coefficients.Y70()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y70_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z83():
    # 'Carbon_Coefficients'!Z83
    value = 0.320524870609
    formula = "=Z70/Z$72"
    @eval_fn
    def Z83():
        z70_1 = Carbon_Coefficients.Z70()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z70_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA83():
    # 'Carbon_Coefficients'!AA83
    value = 0.323368414058
    formula = "=AA70/AA$72"
    @eval_fn
    def AA83():
        aa70_1 = Carbon_Coefficients.AA70()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa70_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB83():
    # 'Carbon_Coefficients'!AB83
    value = 0.308939561144
    formula = "=AB70/AB$72"
    @eval_fn
    def AB83():
        ab70_1 = Carbon_Coefficients.AB70()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab70_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC83():
    # 'Carbon_Coefficients'!AC83
    value = 0.293715416439
    formula = "=AC70/AC$72"
    @eval_fn
    def AC83():
        ac70_1 = Carbon_Coefficients.AC70()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac70_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD83():
    # 'Carbon_Coefficients'!AD83
    value = 0.280013287105
    formula = "=AD70/AD$72"
    @eval_fn
    def AD83():
        ad70_1 = Carbon_Coefficients.AD70()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad70_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE83():
    # 'Carbon_Coefficients'!AE83
    value = 0.27645142293
    formula = "=AE70/AE$72"
    @eval_fn
    def AE83():
        ae70_1 = Carbon_Coefficients.AE70()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae70_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF83():
    # 'Carbon_Coefficients'!AF83
    value = "#N/A"
    formula = "=AF70/AF$72"
    @eval_fn
    def AF83():
        af70_1 = Carbon_Coefficients.AF70()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af70_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG83():
    # 'Carbon_Coefficients'!AG83
    value = "#N/A"
    formula = "=AG70/AG$72"
    @eval_fn
    def AG83():
        ag70_1 = Carbon_Coefficients.AG70()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag70_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH83():
    # 'Carbon_Coefficients'!AH83
    value = "#N/A"
    formula = "=AH70/AH$72"
    @eval_fn
    def AH83():
        ah70_1 = Carbon_Coefficients.AH70()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah70_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI83():
    # 'Carbon_Coefficients'!AI83
    value = "#N/A"
    formula = "=AI70/AI$72"
    @eval_fn
    def AI83():
        ai70_1 = Carbon_Coefficients.AI70()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai70_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ83():
    # 'Carbon_Coefficients'!AJ83
    value = "#N/A"
    formula = "=AJ70/AJ$72"
    @eval_fn
    def AJ83():
        aj70_1 = Carbon_Coefficients.AJ70()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj70_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK83():
    # 'Carbon_Coefficients'!AK83
    value = "#N/A"
    formula = "=AK70/AK$72"
    @eval_fn
    def AK83():
        ak70_1 = Carbon_Coefficients.AK70()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak70_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL83():
    # 'Carbon_Coefficients'!AL83
    value = "#N/A"
    formula = "=AL70/AL$72"
    @eval_fn
    def AL83():
        al70_1 = Carbon_Coefficients.AL70()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al70_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM83():
    # 'Carbon_Coefficients'!AM83
    value = "#N/A"
    formula = "=AM70/AM$72"
    @eval_fn
    def AM83():
        am70_1 = Carbon_Coefficients.AM70()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am70_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN83():
    # 'Carbon_Coefficients'!AN83
    value = "#N/A"
    formula = "=AN70/AN$72"
    @eval_fn
    def AN83():
        an70_1 = Carbon_Coefficients.AN70()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an70_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO83():
    # 'Carbon_Coefficients'!AO83
    value = "#N/A"
    formula = "=AO70/AO$72"
    @eval_fn
    def AO83():
        ao70_1 = Carbon_Coefficients.AO70()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao70_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP83():
    # 'Carbon_Coefficients'!AP83
    value = "#N/A"
    formula = "=AP70/AP$72"
    @eval_fn
    def AP83():
        ap70_1 = Carbon_Coefficients.AP70()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap70_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ83():
    # 'Carbon_Coefficients'!AQ83
    value = "#N/A"
    formula = "=AQ70/AQ$72"
    @eval_fn
    def AQ83():
        aq70_1 = Carbon_Coefficients.AQ70()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq70_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR83():
    # 'Carbon_Coefficients'!AR83
    value = "#N/A"
    formula = "=AR70/AR$72"
    @eval_fn
    def AR83():
        ar70_1 = Carbon_Coefficients.AR70()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar70_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS83():
    # 'Carbon_Coefficients'!AS83
    value = "#N/A"
    formula = "=AS70/AS$72"
    @eval_fn
    def AS83():
        as70_1 = Carbon_Coefficients.AS70()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as70_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT83():
    # 'Carbon_Coefficients'!AT83
    value = "#N/A"
    formula = "=AT70/AT$72"
    @eval_fn
    def AT83():
        at70_1 = Carbon_Coefficients.AT70()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at70_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU83():
    # 'Carbon_Coefficients'!AU83
    value = "#N/A"
    formula = "=AU70/AU$72"
    @eval_fn
    def AU83():
        au70_1 = Carbon_Coefficients.AU70()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au70_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV83():
    # 'Carbon_Coefficients'!AV83
    value = "#N/A"
    formula = "=AV70/AV$72"
    @eval_fn
    def AV83():
        av70_1 = Carbon_Coefficients.AV70()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av70_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A84():
    # 'Carbon_Coefficients'!A84
    value = "Other Petrol Products"

@register(Carbon_Coefficients)
class B84():
    # 'Carbon_Coefficients'!B84
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C84():
    # 'Carbon_Coefficients'!C84
    value = "POTCb"

@register(Carbon_Coefficients)
class E84():
    # 'Carbon_Coefficients'!E84
    value = 0.041490639813
    formula = "=E71/E$72"
    @eval_fn
    def E84():
        e71_1 = Carbon_Coefficients.E71()
        e72_1 = Carbon_Coefficients.E72()
        var_1 = divide(e71_1, e72_1)
        return var_1

@register(Carbon_Coefficients)
class F84():
    # 'Carbon_Coefficients'!F84
    value = 0.0450034325284
    formula = "=F71/F$72"
    @eval_fn
    def F84():
        f71_1 = Carbon_Coefficients.F71()
        f72_1 = Carbon_Coefficients.F72()
        var_1 = divide(f71_1, f72_1)
        return var_1

@register(Carbon_Coefficients)
class G84():
    # 'Carbon_Coefficients'!G84
    value = 0.044359474184
    formula = "=G71/G$72"
    @eval_fn
    def G84():
        g71_1 = Carbon_Coefficients.G71()
        g72_1 = Carbon_Coefficients.G72()
        var_1 = divide(g71_1, g72_1)
        return var_1

@register(Carbon_Coefficients)
class H84():
    # 'Carbon_Coefficients'!H84
    value = 0.0455351256819
    formula = "=H71/H$72"
    @eval_fn
    def H84():
        h71_1 = Carbon_Coefficients.H71()
        h72_1 = Carbon_Coefficients.H72()
        var_1 = divide(h71_1, h72_1)
        return var_1

@register(Carbon_Coefficients)
class I84():
    # 'Carbon_Coefficients'!I84
    value = 0.0436387508206
    formula = "=I71/I$72"
    @eval_fn
    def I84():
        i71_1 = Carbon_Coefficients.I71()
        i72_1 = Carbon_Coefficients.I72()
        var_1 = divide(i71_1, i72_1)
        return var_1

@register(Carbon_Coefficients)
class J84():
    # 'Carbon_Coefficients'!J84
    value = 0.0507501137648
    formula = "=J71/J$72"
    @eval_fn
    def J84():
        j71_1 = Carbon_Coefficients.J71()
        j72_1 = Carbon_Coefficients.J72()
        var_1 = divide(j71_1, j72_1)
        return var_1

@register(Carbon_Coefficients)
class K84():
    # 'Carbon_Coefficients'!K84
    value = 0.0518181628523
    formula = "=K71/K$72"
    @eval_fn
    def K84():
        k71_1 = Carbon_Coefficients.K71()
        k72_1 = Carbon_Coefficients.K72()
        var_1 = divide(k71_1, k72_1)
        return var_1

@register(Carbon_Coefficients)
class L84():
    # 'Carbon_Coefficients'!L84
    value = 0.0527016926967
    formula = "=L71/L$72"
    @eval_fn
    def L84():
        l71_1 = Carbon_Coefficients.L71()
        l72_1 = Carbon_Coefficients.L72()
        var_1 = divide(l71_1, l72_1)
        return var_1

@register(Carbon_Coefficients)
class M84():
    # 'Carbon_Coefficients'!M84
    value = 0.0516917739866
    formula = "=M71/M$72"
    @eval_fn
    def M84():
        m71_1 = Carbon_Coefficients.M71()
        m72_1 = Carbon_Coefficients.M72()
        var_1 = divide(m71_1, m72_1)
        return var_1

@register(Carbon_Coefficients)
class N84():
    # 'Carbon_Coefficients'!N84
    value = 0.0648593645968
    formula = "=N71/N$72"
    @eval_fn
    def N84():
        n71_1 = Carbon_Coefficients.N71()
        n72_1 = Carbon_Coefficients.N72()
        var_1 = divide(n71_1, n72_1)
        return var_1

@register(Carbon_Coefficients)
class O84():
    # 'Carbon_Coefficients'!O84
    value = 0.0661719420903
    formula = "=O71/O$72"
    @eval_fn
    def O84():
        o71_1 = Carbon_Coefficients.O71()
        o72_1 = Carbon_Coefficients.O72()
        var_1 = divide(o71_1, o72_1)
        return var_1

@register(Carbon_Coefficients)
class P84():
    # 'Carbon_Coefficients'!P84
    value = 0.0539088749545
    formula = "=P71/P$72"
    @eval_fn
    def P84():
        p71_1 = Carbon_Coefficients.P71()
        p72_1 = Carbon_Coefficients.P72()
        var_1 = divide(p71_1, p72_1)
        return var_1

@register(Carbon_Coefficients)
class Q84():
    # 'Carbon_Coefficients'!Q84
    value = 0.0548468722283
    formula = "=Q71/Q$72"
    @eval_fn
    def Q84():
        q71_1 = Carbon_Coefficients.Q71()
        q72_1 = Carbon_Coefficients.Q72()
        var_1 = divide(q71_1, q72_1)
        return var_1

@register(Carbon_Coefficients)
class R84():
    # 'Carbon_Coefficients'!R84
    value = 0.0499430533599
    formula = "=R71/R$72"
    @eval_fn
    def R84():
        r71_1 = Carbon_Coefficients.R71()
        r72_1 = Carbon_Coefficients.R72()
        var_1 = divide(r71_1, r72_1)
        return var_1

@register(Carbon_Coefficients)
class S84():
    # 'Carbon_Coefficients'!S84
    value = 0.0622973502371
    formula = "=S71/S$72"
    @eval_fn
    def S84():
        s71_1 = Carbon_Coefficients.S71()
        s72_1 = Carbon_Coefficients.S72()
        var_1 = divide(s71_1, s72_1)
        return var_1

@register(Carbon_Coefficients)
class T84():
    # 'Carbon_Coefficients'!T84
    value = 0.0549978649897
    formula = "=T71/T$72"
    @eval_fn
    def T84():
        t71_1 = Carbon_Coefficients.T71()
        t72_1 = Carbon_Coefficients.T72()
        var_1 = divide(t71_1, t72_1)
        return var_1

@register(Carbon_Coefficients)
class U84():
    # 'Carbon_Coefficients'!U84
    value = 0.0572709939238
    formula = "=U71/U$72"
    @eval_fn
    def U84():
        u71_1 = Carbon_Coefficients.U71()
        u72_1 = Carbon_Coefficients.U72()
        var_1 = divide(u71_1, u72_1)
        return var_1

@register(Carbon_Coefficients)
class V84():
    # 'Carbon_Coefficients'!V84
    value = 0.0536476440826
    formula = "=V71/V$72"
    @eval_fn
    def V84():
        v71_1 = Carbon_Coefficients.V71()
        v72_1 = Carbon_Coefficients.V72()
        var_1 = divide(v71_1, v72_1)
        return var_1

@register(Carbon_Coefficients)
class W84():
    # 'Carbon_Coefficients'!W84
    value = 0.0536720006773
    formula = "=W71/W$72"
    @eval_fn
    def W84():
        w71_1 = Carbon_Coefficients.W71()
        w72_1 = Carbon_Coefficients.W72()
        var_1 = divide(w71_1, w72_1)
        return var_1

@register(Carbon_Coefficients)
class X84():
    # 'Carbon_Coefficients'!X84
    value = 0.0549096780704
    formula = "=X71/X$72"
    @eval_fn
    def X84():
        x71_1 = Carbon_Coefficients.X71()
        x72_1 = Carbon_Coefficients.X72()
        var_1 = divide(x71_1, x72_1)
        return var_1

@register(Carbon_Coefficients)
class Y84():
    # 'Carbon_Coefficients'!Y84
    value = 0.051696062915
    formula = "=Y71/Y$72"
    @eval_fn
    def Y84():
        y71_1 = Carbon_Coefficients.Y71()
        y72_1 = Carbon_Coefficients.Y72()
        var_1 = divide(y71_1, y72_1)
        return var_1

@register(Carbon_Coefficients)
class Z84():
    # 'Carbon_Coefficients'!Z84
    value = 0.0571045103246
    formula = "=Z71/Z$72"
    @eval_fn
    def Z84():
        z71_1 = Carbon_Coefficients.Z71()
        z72_1 = Carbon_Coefficients.Z72()
        var_1 = divide(z71_1, z72_1)
        return var_1

@register(Carbon_Coefficients)
class AA84():
    # 'Carbon_Coefficients'!AA84
    value = 0.0573266660575
    formula = "=AA71/AA$72"
    @eval_fn
    def AA84():
        aa71_1 = Carbon_Coefficients.AA71()
        aa72_1 = Carbon_Coefficients.AA72()
        var_1 = divide(aa71_1, aa72_1)
        return var_1

@register(Carbon_Coefficients)
class AB84():
    # 'Carbon_Coefficients'!AB84
    value = 0.0605008534927
    formula = "=AB71/AB$72"
    @eval_fn
    def AB84():
        ab71_1 = Carbon_Coefficients.AB71()
        ab72_1 = Carbon_Coefficients.AB72()
        var_1 = divide(ab71_1, ab72_1)
        return var_1

@register(Carbon_Coefficients)
class AC84():
    # 'Carbon_Coefficients'!AC84
    value = 0.0602088079119
    formula = "=AC71/AC$72"
    @eval_fn
    def AC84():
        ac71_1 = Carbon_Coefficients.AC71()
        ac72_1 = Carbon_Coefficients.AC72()
        var_1 = divide(ac71_1, ac72_1)
        return var_1

@register(Carbon_Coefficients)
class AD84():
    # 'Carbon_Coefficients'!AD84
    value = 0.0647995515602
    formula = "=AD71/AD$72"
    @eval_fn
    def AD84():
        ad71_1 = Carbon_Coefficients.AD71()
        ad72_1 = Carbon_Coefficients.AD72()
        var_1 = divide(ad71_1, ad72_1)
        return var_1

@register(Carbon_Coefficients)
class AE84():
    # 'Carbon_Coefficients'!AE84
    value = 0.0633020798468
    formula = "=AE71/AE$72"
    @eval_fn
    def AE84():
        ae71_1 = Carbon_Coefficients.AE71()
        ae72_1 = Carbon_Coefficients.AE72()
        var_1 = divide(ae71_1, ae72_1)
        return var_1

@register(Carbon_Coefficients)
class AF84():
    # 'Carbon_Coefficients'!AF84
    value = "#N/A"
    formula = "=AF71/AF$72"
    @eval_fn
    def AF84():
        af71_1 = Carbon_Coefficients.AF71()
        af72_1 = Carbon_Coefficients.AF72()
        var_1 = divide(af71_1, af72_1)
        return var_1

@register(Carbon_Coefficients)
class AG84():
    # 'Carbon_Coefficients'!AG84
    value = "#N/A"
    formula = "=AG71/AG$72"
    @eval_fn
    def AG84():
        ag71_1 = Carbon_Coefficients.AG71()
        ag72_1 = Carbon_Coefficients.AG72()
        var_1 = divide(ag71_1, ag72_1)
        return var_1

@register(Carbon_Coefficients)
class AH84():
    # 'Carbon_Coefficients'!AH84
    value = "#N/A"
    formula = "=AH71/AH$72"
    @eval_fn
    def AH84():
        ah71_1 = Carbon_Coefficients.AH71()
        ah72_1 = Carbon_Coefficients.AH72()
        var_1 = divide(ah71_1, ah72_1)
        return var_1

@register(Carbon_Coefficients)
class AI84():
    # 'Carbon_Coefficients'!AI84
    value = "#N/A"
    formula = "=AI71/AI$72"
    @eval_fn
    def AI84():
        ai71_1 = Carbon_Coefficients.AI71()
        ai72_1 = Carbon_Coefficients.AI72()
        var_1 = divide(ai71_1, ai72_1)
        return var_1

@register(Carbon_Coefficients)
class AJ84():
    # 'Carbon_Coefficients'!AJ84
    value = "#N/A"
    formula = "=AJ71/AJ$72"
    @eval_fn
    def AJ84():
        aj71_1 = Carbon_Coefficients.AJ71()
        aj72_1 = Carbon_Coefficients.AJ72()
        var_1 = divide(aj71_1, aj72_1)
        return var_1

@register(Carbon_Coefficients)
class AK84():
    # 'Carbon_Coefficients'!AK84
    value = "#N/A"
    formula = "=AK71/AK$72"
    @eval_fn
    def AK84():
        ak71_1 = Carbon_Coefficients.AK71()
        ak72_1 = Carbon_Coefficients.AK72()
        var_1 = divide(ak71_1, ak72_1)
        return var_1

@register(Carbon_Coefficients)
class AL84():
    # 'Carbon_Coefficients'!AL84
    value = "#N/A"
    formula = "=AL71/AL$72"
    @eval_fn
    def AL84():
        al71_1 = Carbon_Coefficients.AL71()
        al72_1 = Carbon_Coefficients.AL72()
        var_1 = divide(al71_1, al72_1)
        return var_1

@register(Carbon_Coefficients)
class AM84():
    # 'Carbon_Coefficients'!AM84
    value = "#N/A"
    formula = "=AM71/AM$72"
    @eval_fn
    def AM84():
        am71_1 = Carbon_Coefficients.AM71()
        am72_1 = Carbon_Coefficients.AM72()
        var_1 = divide(am71_1, am72_1)
        return var_1

@register(Carbon_Coefficients)
class AN84():
    # 'Carbon_Coefficients'!AN84
    value = "#N/A"
    formula = "=AN71/AN$72"
    @eval_fn
    def AN84():
        an71_1 = Carbon_Coefficients.AN71()
        an72_1 = Carbon_Coefficients.AN72()
        var_1 = divide(an71_1, an72_1)
        return var_1

@register(Carbon_Coefficients)
class AO84():
    # 'Carbon_Coefficients'!AO84
    value = "#N/A"
    formula = "=AO71/AO$72"
    @eval_fn
    def AO84():
        ao71_1 = Carbon_Coefficients.AO71()
        ao72_1 = Carbon_Coefficients.AO72()
        var_1 = divide(ao71_1, ao72_1)
        return var_1

@register(Carbon_Coefficients)
class AP84():
    # 'Carbon_Coefficients'!AP84
    value = "#N/A"
    formula = "=AP71/AP$72"
    @eval_fn
    def AP84():
        ap71_1 = Carbon_Coefficients.AP71()
        ap72_1 = Carbon_Coefficients.AP72()
        var_1 = divide(ap71_1, ap72_1)
        return var_1

@register(Carbon_Coefficients)
class AQ84():
    # 'Carbon_Coefficients'!AQ84
    value = "#N/A"
    formula = "=AQ71/AQ$72"
    @eval_fn
    def AQ84():
        aq71_1 = Carbon_Coefficients.AQ71()
        aq72_1 = Carbon_Coefficients.AQ72()
        var_1 = divide(aq71_1, aq72_1)
        return var_1

@register(Carbon_Coefficients)
class AR84():
    # 'Carbon_Coefficients'!AR84
    value = "#N/A"
    formula = "=AR71/AR$72"
    @eval_fn
    def AR84():
        ar71_1 = Carbon_Coefficients.AR71()
        ar72_1 = Carbon_Coefficients.AR72()
        var_1 = divide(ar71_1, ar72_1)
        return var_1

@register(Carbon_Coefficients)
class AS84():
    # 'Carbon_Coefficients'!AS84
    value = "#N/A"
    formula = "=AS71/AS$72"
    @eval_fn
    def AS84():
        as71_1 = Carbon_Coefficients.AS71()
        as72_1 = Carbon_Coefficients.AS72()
        var_1 = divide(as71_1, as72_1)
        return var_1

@register(Carbon_Coefficients)
class AT84():
    # 'Carbon_Coefficients'!AT84
    value = "#N/A"
    formula = "=AT71/AT$72"
    @eval_fn
    def AT84():
        at71_1 = Carbon_Coefficients.AT71()
        at72_1 = Carbon_Coefficients.AT72()
        var_1 = divide(at71_1, at72_1)
        return var_1

@register(Carbon_Coefficients)
class AU84():
    # 'Carbon_Coefficients'!AU84
    value = "#N/A"
    formula = "=AU71/AU$72"
    @eval_fn
    def AU84():
        au71_1 = Carbon_Coefficients.AU71()
        au72_1 = Carbon_Coefficients.AU72()
        var_1 = divide(au71_1, au72_1)
        return var_1

@register(Carbon_Coefficients)
class AV84():
    # 'Carbon_Coefficients'!AV84
    value = "#N/A"
    formula = "=AV71/AV$72"
    @eval_fn
    def AV84():
        av71_1 = Carbon_Coefficients.AV71()
        av72_1 = Carbon_Coefficients.AV72()
        var_1 = divide(av71_1, av72_1)
        return var_1

@register(Carbon_Coefficients)
class A85():
    # 'Carbon_Coefficients'!A85
    value = "Total Petroleum"

@register(Carbon_Coefficients)
class B85():
    # 'Carbon_Coefficients'!B85
    value = "EIA State Energy Data 2010: consumption Table TN3. Summary of Petroleum Products in the State Energy Data System"

@register(Carbon_Coefficients)
class C85():
    # 'Carbon_Coefficients'!C85
    value = "PATCb"

@register(Carbon_Coefficients)
class A88():
    # 'Carbon_Coefficients'!A88
    value = "Asphat"

@register(Carbon_Coefficients)
class B88():
    # 'Carbon_Coefficients'!B88
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D88():
    # 'Carbon_Coefficients'!D88
    value = 75.35
    formula = "=$D46"
    @eval_fn
    def D88():
        d46_1 = Carbon_Coefficients.D46()
        return d46_1

@register(Carbon_Coefficients)
class A89():
    # 'Carbon_Coefficients'!A89
    value = "Aviation"

@register(Carbon_Coefficients)
class B89():
    # 'Carbon_Coefficients'!B89
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D89():
    # 'Carbon_Coefficients'!D89
    value = 69.1533333333
    formula = "=$D47"
    @eval_fn
    def D89():
        d47_1 = Carbon_Coefficients.D47()
        return d47_1

@register(Carbon_Coefficients)
class A90():
    # 'Carbon_Coefficients'!A90
    value = "Distllate"

@register(Carbon_Coefficients)
class B90():
    # 'Carbon_Coefficients'!B90
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D90():
    # 'Carbon_Coefficients'!D90
    value = 74.0911111111
    formula = "=SUM($D48:$D50)/3"
    @eval_fn
    def D90():
        range_1 = Carbon_Coefficients(4, 48, 4, 50)
        var_1 = SUM(range_1)
        var_2 = divide(var_1, 3)
        return var_2

@register(Carbon_Coefficients)
class A91():
    # 'Carbon_Coefficients'!A91
    value = "Jet Fuel"

@register(Carbon_Coefficients)
class B91():
    # 'Carbon_Coefficients'!B91
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D91():
    # 'Carbon_Coefficients'!D91
    value = 72.2333333333
    formula = "=$D51"
    @eval_fn
    def D91():
        d51_1 = Carbon_Coefficients.D51()
        return d51_1

@register(Carbon_Coefficients)
class A92():
    # 'Carbon_Coefficients'!A92
    value = "Kerosene"

@register(Carbon_Coefficients)
class B92():
    # 'Carbon_Coefficients'!B92
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D92():
    # 'Carbon_Coefficients'!D92
    value = 73.1866666667
    formula = "=$D52"
    @eval_fn
    def D92():
        d52_1 = Carbon_Coefficients.D52()
        return d52_1

@register(Carbon_Coefficients)
class A93():
    # 'Carbon_Coefficients'!A93
    value = "LPG"

@register(Carbon_Coefficients)
class B93():
    # 'Carbon_Coefficients'!B93
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D93():
    # 'Carbon_Coefficients'!D93
    value = 62.1316666667
    formula = "=SUM($D53:D54)/2"
    @eval_fn
    def D93():
        range_1 = Carbon_Coefficients(4, 53, 4, 54)
        var_1 = SUM(range_1)
        var_2 = divide(var_1, 2)
        return var_2

@register(Carbon_Coefficients)
class A94():
    # 'Carbon_Coefficients'!A94
    value = "Lubricants"

@register(Carbon_Coefficients)
class B94():
    # 'Carbon_Coefficients'!B94
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D94():
    # 'Carbon_Coefficients'!D94
    value = 74.0666666667
    formula = "=D55"
    @eval_fn
    def D94():
        d55_1 = Carbon_Coefficients.D55()
        return d55_1

@register(Carbon_Coefficients)
class A95():
    # 'Carbon_Coefficients'!A95
    value = "Motor Gasoline"

@register(Carbon_Coefficients)
class B95():
    # 'Carbon_Coefficients'!B95
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D95():
    # 'Carbon_Coefficients'!D95
    value = 71.3533333333
    formula = "=D56"
    @eval_fn
    def D95():
        d56_1 = Carbon_Coefficients.D56()
        return d56_1

@register(Carbon_Coefficients)
class A96():
    # 'Carbon_Coefficients'!A96
    value = "Residual Fuel Oil"

@register(Carbon_Coefficients)
class B96():
    # 'Carbon_Coefficients'!B96
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D96():
    # 'Carbon_Coefficients'!D96
    value = 74.0116666667
    formula = "=SUM(D57:D58)/2"
    @eval_fn
    def D96():
        range_1 = Carbon_Coefficients(4, 57, 4, 58)
        var_1 = SUM(range_1)
        var_2 = divide(var_1, 2)
        return var_2

@register(Carbon_Coefficients)
class A97():
    # 'Carbon_Coefficients'!A97
    value = "Other Petrol Products"

@register(Carbon_Coefficients)
class B97():
    # 'Carbon_Coefficients'!B97
    value = "co2 coefficient"

@register(Carbon_Coefficients)
class D97():
    # 'Carbon_Coefficients'!D97
    value = 71.7308641975
    formula = "=AVERAGE(D88:D96)"
    @eval_fn
    def D97():
        range_1 = Carbon_Coefficients(4, 88, 4, 96)
        var_1 = AVERAGE(range_1)
        return var_1

@register(Carbon_Coefficients)
class E97():
    # 'Carbon_Coefficients'!E97
    value = "(Average Used)"

@register(Carbon_Coefficients)
class A99():
    # 'Carbon_Coefficients'!A99
    value = "Total Petroleum Average CO2 coefficient"

@register(Carbon_Coefficients)
class E99():
    # 'Carbon_Coefficients'!E99
    value = 72.8822113102
    formula = "=SUMPRODUCT(E75:E84,$D88:$D97)"
    @eval_fn
    def E99():
        range_1 = Carbon_Coefficients(5, 75, 5, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class F99():
    # 'Carbon_Coefficients'!F99
    value = 72.9869880208
    formula = "=SUMPRODUCT(F75:F84,$D88:$D97)"
    @eval_fn
    def F99():
        range_1 = Carbon_Coefficients(6, 75, 6, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class G99():
    # 'Carbon_Coefficients'!G99
    value = 72.965310145
    formula = "=SUMPRODUCT(G75:G84,$D88:$D97)"
    @eval_fn
    def G99():
        range_1 = Carbon_Coefficients(7, 75, 7, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class H99():
    # 'Carbon_Coefficients'!H99
    value = 73.0342420872
    formula = "=SUMPRODUCT(H75:H84,$D88:$D97)"
    @eval_fn
    def H99():
        range_1 = Carbon_Coefficients(8, 75, 8, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class I99():
    # 'Carbon_Coefficients'!I99
    value = 72.9900599035
    formula = "=SUMPRODUCT(I75:I84,$D88:$D97)"
    @eval_fn
    def I99():
        range_1 = Carbon_Coefficients(9, 75, 9, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class J99():
    # 'Carbon_Coefficients'!J99
    value = 72.9680852461
    formula = "=SUMPRODUCT(J75:J84,$D88:$D97)"
    @eval_fn
    def J99():
        range_1 = Carbon_Coefficients(10, 75, 10, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class K99():
    # 'Carbon_Coefficients'!K99
    value = 72.8426931584
    formula = "=SUMPRODUCT(K75:K84,$D88:$D97)"
    @eval_fn
    def K99():
        range_1 = Carbon_Coefficients(11, 75, 11, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class L99():
    # 'Carbon_Coefficients'!L99
    value = 72.7555879744
    formula = "=SUMPRODUCT(L75:L84,$D88:$D97)"
    @eval_fn
    def L99():
        range_1 = Carbon_Coefficients(12, 75, 12, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class M99():
    # 'Carbon_Coefficients'!M99
    value = 72.7626669216
    formula = "=SUMPRODUCT(M75:M84,$D88:$D97)"
    @eval_fn
    def M99():
        range_1 = Carbon_Coefficients(13, 75, 13, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class N99():
    # 'Carbon_Coefficients'!N99
    value = 72.6663612227
    formula = "=SUMPRODUCT(N75:N84,$D88:$D97)"
    @eval_fn
    def N99():
        range_1 = Carbon_Coefficients(14, 75, 14, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class O99():
    # 'Carbon_Coefficients'!O99
    value = 72.8160008875
    formula = "=SUMPRODUCT(O75:O84,$D88:$D97)"
    @eval_fn
    def O99():
        range_1 = Carbon_Coefficients(15, 75, 15, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class P99():
    # 'Carbon_Coefficients'!P99
    value = 72.7504305867
    formula = "=SUMPRODUCT(P75:P84,$D88:$D97)"
    @eval_fn
    def P99():
        range_1 = Carbon_Coefficients(16, 75, 16, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class Q99():
    # 'Carbon_Coefficients'!Q99
    value = 72.8758139504
    formula = "=SUMPRODUCT(Q75:Q84,$D88:$D97)"
    @eval_fn
    def Q99():
        range_1 = Carbon_Coefficients(17, 75, 17, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class R99():
    # 'Carbon_Coefficients'!R99
    value = 72.8667300868
    formula = "=SUMPRODUCT(R75:R84,$D88:$D97)"
    @eval_fn
    def R99():
        range_1 = Carbon_Coefficients(18, 75, 18, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class S99():
    # 'Carbon_Coefficients'!S99
    value = 72.8452013797
    formula = "=SUMPRODUCT(S75:S84,$D88:$D97)"
    @eval_fn
    def S99():
        range_1 = Carbon_Coefficients(19, 75, 19, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class T99():
    # 'Carbon_Coefficients'!T99
    value = 72.8114523334
    formula = "=SUMPRODUCT(T75:T84,$D88:$D97)"
    @eval_fn
    def T99():
        range_1 = Carbon_Coefficients(20, 75, 20, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class U99():
    # 'Carbon_Coefficients'!U99
    value = 72.7964830221
    formula = "=SUMPRODUCT(U75:U84,$D88:$D97)"
    @eval_fn
    def U99():
        range_1 = Carbon_Coefficients(21, 75, 21, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class V99():
    # 'Carbon_Coefficients'!V99
    value = 72.8277639426
    formula = "=SUMPRODUCT(V75:V84,$D88:$D97)"
    @eval_fn
    def V99():
        range_1 = Carbon_Coefficients(22, 75, 22, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class W99():
    # 'Carbon_Coefficients'!W99
    value = 72.7615699385
    formula = "=SUMPRODUCT(W75:W84,$D88:$D97)"
    @eval_fn
    def W99():
        range_1 = Carbon_Coefficients(23, 75, 23, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class X99():
    # 'Carbon_Coefficients'!X99
    value = 72.7639663238
    formula = "=SUMPRODUCT(X75:X84,$D88:$D97)"
    @eval_fn
    def X99():
        range_1 = Carbon_Coefficients(24, 75, 24, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class Y99():
    # 'Carbon_Coefficients'!Y99
    value = 72.9098940776
    formula = "=SUMPRODUCT(Y75:Y84,$D88:$D97)"
    @eval_fn
    def Y99():
        range_1 = Carbon_Coefficients(25, 75, 25, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class Z99():
    # 'Carbon_Coefficients'!Z99
    value = 72.7122982344
    formula = "=SUMPRODUCT(Z75:Z84,$D88:$D97)"
    @eval_fn
    def Z99():
        range_1 = Carbon_Coefficients(26, 75, 26, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AA99():
    # 'Carbon_Coefficients'!AA99
    value = 72.7264837073
    formula = "=SUMPRODUCT(AA75:AA84,$D88:$D97)"
    @eval_fn
    def AA99():
        range_1 = Carbon_Coefficients(27, 75, 27, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AB99():
    # 'Carbon_Coefficients'!AB99
    value = 72.750572146
    formula = "=SUMPRODUCT(AB75:AB84,$D88:$D97)"
    @eval_fn
    def AB99():
        range_1 = Carbon_Coefficients(28, 75, 28, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AC99():
    # 'Carbon_Coefficients'!AC99
    value = 72.6668001857
    formula = "=SUMPRODUCT(AC75:AC84,$D88:$D97)"
    @eval_fn
    def AC99():
        range_1 = Carbon_Coefficients(29, 75, 29, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AD99():
    # 'Carbon_Coefficients'!AD99
    value = 72.6418493436
    formula = "=SUMPRODUCT(AD75:AD84,$D88:$D97)"
    @eval_fn
    def AD99():
        range_1 = Carbon_Coefficients(30, 75, 30, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AE99():
    # 'Carbon_Coefficients'!AE99
    value = 72.6264625058
    formula = "=SUMPRODUCT(AE75:AE84,$D88:$D97)"
    @eval_fn
    def AE99():
        range_1 = Carbon_Coefficients(31, 75, 31, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AF99():
    # 'Carbon_Coefficients'!AF99
    value = "#N/A"
    formula = "=SUMPRODUCT(AF75:AF84,$D88:$D97)"
    @eval_fn
    def AF99():
        range_1 = Carbon_Coefficients(32, 75, 32, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AG99():
    # 'Carbon_Coefficients'!AG99
    value = "#N/A"
    formula = "=SUMPRODUCT(AG75:AG84,$D88:$D97)"
    @eval_fn
    def AG99():
        range_1 = Carbon_Coefficients(33, 75, 33, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AH99():
    # 'Carbon_Coefficients'!AH99
    value = "#N/A"
    formula = "=SUMPRODUCT(AH75:AH84,$D88:$D97)"
    @eval_fn
    def AH99():
        range_1 = Carbon_Coefficients(34, 75, 34, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AI99():
    # 'Carbon_Coefficients'!AI99
    value = "#N/A"
    formula = "=SUMPRODUCT(AI75:AI84,$D88:$D97)"
    @eval_fn
    def AI99():
        range_1 = Carbon_Coefficients(35, 75, 35, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AJ99():
    # 'Carbon_Coefficients'!AJ99
    value = "#N/A"
    formula = "=SUMPRODUCT(AJ75:AJ84,$D88:$D97)"
    @eval_fn
    def AJ99():
        range_1 = Carbon_Coefficients(36, 75, 36, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AK99():
    # 'Carbon_Coefficients'!AK99
    value = "#N/A"
    formula = "=SUMPRODUCT(AK75:AK84,$D88:$D97)"
    @eval_fn
    def AK99():
        range_1 = Carbon_Coefficients(37, 75, 37, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class AL99():
    # 'Carbon_Coefficients'!AL99
    value = "#N/A"
    formula = "=SUMPRODUCT(AL75:AL84,$D88:$D97)"
    @eval_fn
    def AL99():
        range_1 = Carbon_Coefficients(38, 75, 38, 84)
        range_2 = Carbon_Coefficients(4, 88, 4, 97)
        var_1 = SUMPRODUCT(range_1, range_2)
        return var_1

@register(Carbon_Coefficients)
class A112():
    # 'Carbon_Coefficients'!A112
    value = "Geothermal"

@register(Carbon_Coefficients)
class A113():
    # 'Carbon_Coefficients'!A113
    value = "Carbon Content Coefficient (kkgCarbon/MMBtu)"

@register(Carbon_Coefficients)
class B114():
    # 'Carbon_Coefficients'!B114
    value = "kgCarbon/mmbtu"

@register(Carbon_Coefficients)
class H114():
    # 'Carbon_Coefficients'!H114
    value = 2.05

@register(Carbon_Coefficients)
class I114():
    # 'Carbon_Coefficients'!I114
    value = 2.05

@register(Carbon_Coefficients)
class J114():
    # 'Carbon_Coefficients'!J114
    value = 2.05

@register(Carbon_Coefficients)
class K114():
    # 'Carbon_Coefficients'!K114
    value = 2.05

@register(Carbon_Coefficients)
class L114():
    # 'Carbon_Coefficients'!L114
    value = 2.05

@register(Carbon_Coefficients)
class M114():
    # 'Carbon_Coefficients'!M114
    value = 2.05

@register(Carbon_Coefficients)
class N114():
    # 'Carbon_Coefficients'!N114
    value = 2.05

@register(Carbon_Coefficients)
class O114():
    # 'Carbon_Coefficients'!O114
    value = 2.05

@register(Carbon_Coefficients)
class P114():
    # 'Carbon_Coefficients'!P114
    value = 2.05

@register(Carbon_Coefficients)
class Q114():
    # 'Carbon_Coefficients'!Q114
    value = 2.05

@register(Carbon_Coefficients)
class R114():
    # 'Carbon_Coefficients'!R114
    value = 2.05

@register(Carbon_Coefficients)
class S114():
    # 'Carbon_Coefficients'!S114
    value = 2.05

@register(Carbon_Coefficients)
class T114():
    # 'Carbon_Coefficients'!T114
    value = 2.05

@register(Carbon_Coefficients)
class U114():
    # 'Carbon_Coefficients'!U114
    value = 2.05

@register(Carbon_Coefficients)
class V114():
    # 'Carbon_Coefficients'!V114
    value = 2.05

@register(Carbon_Coefficients)
class W114():
    # 'Carbon_Coefficients'!W114
    value = 2.05

@register(Carbon_Coefficients)
class X114():
    # 'Carbon_Coefficients'!X114
    value = 2.05

@register(Carbon_Coefficients)
class Y114():
    # 'Carbon_Coefficients'!Y114
    value = 2.05

@register(Carbon_Coefficients)
class Z114():
    # 'Carbon_Coefficients'!Z114
    value = 2.05

@register(Carbon_Coefficients)
class A116():
    # 'Carbon_Coefficients'!A116
    value = "Notes"

@register(Carbon_Coefficients)
class A117():
    # 'Carbon_Coefficients'!A117
    value = "Coefficients for 1986-1989 are 1990 numbers as data was not provided for those years"