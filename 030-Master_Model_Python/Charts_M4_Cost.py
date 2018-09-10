# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M4_Cost = Worksheet('Charts_M4_Cost', 10, 10)



@register(Charts_M4_Cost)
class B2():
    # 'Charts_M4_Cost'!B2
    value = True

@register(Charts_M4_Cost)
class D2():
    # 'Charts_M4_Cost'!D2
    value = "Metric 4: Hawaii energy portfolio Cost volatility"

@register(Charts_M4_Cost)
class B3():
    # 'Charts_M4_Cost'!B3
    value = True

@register(Charts_M4_Cost)
class B4():
    # 'Charts_M4_Cost'!B4
    value = True

@register(Charts_M4_Cost)
class B5():
    # 'Charts_M4_Cost'!B5
    value = True

@register(Charts_M4_Cost)
class G5():
    # 'Charts_M4_Cost'!G5
    value = 2006

@register(Charts_M4_Cost)
class H5():
    # 'Charts_M4_Cost'!H5
    value = 2007

@register(Charts_M4_Cost)
class I5():
    # 'Charts_M4_Cost'!I5
    value = 2008

@register(Charts_M4_Cost)
class J5():
    # 'Charts_M4_Cost'!J5
    value = 2009

@register(Charts_M4_Cost)
class K5():
    # 'Charts_M4_Cost'!K5
    value = 2010

@register(Charts_M4_Cost)
class L5():
    # 'Charts_M4_Cost'!L5
    value = 2011

@register(Charts_M4_Cost)
class M5():
    # 'Charts_M4_Cost'!M5
    value = 2012

@register(Charts_M4_Cost)
class N5():
    # 'Charts_M4_Cost'!N5
    value = 2013

@register(Charts_M4_Cost)
class S5():
    # 'Charts_M4_Cost'!S5
    value = "Note: Cost Volatility here is calculated as a standard deviation and therefore, the total variation for all fuels is not expected to equal the sum of the variations if individual fuels."

@register(Charts_M4_Cost)
class B6():
    # 'Charts_M4_Cost'!B6
    value = True

@register(Charts_M4_Cost)
class D6():
    # 'Charts_M4_Cost'!D6
    value = "Residential"
    formula = "='Dashboard M4 Cost Annual'!A157"
    @eval_fn
    def D6():
        a157_1 = Dashboard_M4_Cost_Annual.A157()
        return a157_1

@register(Charts_M4_Cost)
class G6():
    # 'Charts_M4_Cost'!G6
    value = 7.91657124131
    formula = "='Dashboard M4 Cost Annual'!BA158/1000000"
    @eval_fn
    def G6():
        ba158_1 = Dashboard_M4_Cost_Annual.BA158()
        var_1 = divide(ba158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H6():
    # 'Charts_M4_Cost'!H6
    value = 22.1292339542
    formula = "='Dashboard M4 Cost Annual'!BB158/1000000"
    @eval_fn
    def H6():
        bb158_1 = Dashboard_M4_Cost_Annual.BB158()
        var_1 = divide(bb158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I6():
    # 'Charts_M4_Cost'!I6
    value = 28.0347742398
    formula = "='Dashboard M4 Cost Annual'!BC158/1000000"
    @eval_fn
    def I6():
        bc158_1 = Dashboard_M4_Cost_Annual.BC158()
        var_1 = divide(bc158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J6():
    # 'Charts_M4_Cost'!J6
    value = 26.1793999022
    formula = "='Dashboard M4 Cost Annual'!BD158/1000000"
    @eval_fn
    def J6():
        bd158_1 = Dashboard_M4_Cost_Annual.BD158()
        var_1 = divide(bd158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K6():
    # 'Charts_M4_Cost'!K6
    value = 10.4836813868
    formula = "='Dashboard M4 Cost Annual'!BE158/1000000"
    @eval_fn
    def K6():
        be158_1 = Dashboard_M4_Cost_Annual.BE158()
        var_1 = divide(be158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L6():
    # 'Charts_M4_Cost'!L6
    value = 25.7670319096
    formula = "='Dashboard M4 Cost Annual'!BF158/1000000"
    @eval_fn
    def L6():
        bf158_1 = Dashboard_M4_Cost_Annual.BF158()
        var_1 = divide(bf158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M6():
    # 'Charts_M4_Cost'!M6
    value = 17.9608675021
    formula = "='Dashboard M4 Cost Annual'!BG158/1000000"
    @eval_fn
    def M6():
        bg158_1 = Dashboard_M4_Cost_Annual.BG158()
        var_1 = divide(bg158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N6():
    # 'Charts_M4_Cost'!N6
    value = 21.9340782686
    formula = "='Dashboard M4 Cost Annual'!BH158/1000000"
    @eval_fn
    def N6():
        bh158_1 = Dashboard_M4_Cost_Annual.BH158()
        var_1 = divide(bh158_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B7():
    # 'Charts_M4_Cost'!B7
    value = True

@register(Charts_M4_Cost)
class D7():
    # 'Charts_M4_Cost'!D7
    value = "Commercial"
    formula = "='Dashboard M4 Cost Annual'!A159"
    @eval_fn
    def D7():
        a159_1 = Dashboard_M4_Cost_Annual.A159()
        return a159_1

@register(Charts_M4_Cost)
class G7():
    # 'Charts_M4_Cost'!G7
    value = 10.415319466
    formula = "='Dashboard M4 Cost Annual'!BA160/1000000"
    @eval_fn
    def G7():
        ba160_1 = Dashboard_M4_Cost_Annual.BA160()
        var_1 = divide(ba160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H7():
    # 'Charts_M4_Cost'!H7
    value = 27.9570301102
    formula = "='Dashboard M4 Cost Annual'!BB160/1000000"
    @eval_fn
    def H7():
        bb160_1 = Dashboard_M4_Cost_Annual.BB160()
        var_1 = divide(bb160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I7():
    # 'Charts_M4_Cost'!I7
    value = 38.0187780674
    formula = "='Dashboard M4 Cost Annual'!BC160/1000000"
    @eval_fn
    def I7():
        bc160_1 = Dashboard_M4_Cost_Annual.BC160()
        var_1 = divide(bc160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J7():
    # 'Charts_M4_Cost'!J7
    value = 36.4326780906
    formula = "='Dashboard M4 Cost Annual'!BD160/1000000"
    @eval_fn
    def J7():
        bd160_1 = Dashboard_M4_Cost_Annual.BD160()
        var_1 = divide(bd160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K7():
    # 'Charts_M4_Cost'!K7
    value = 13.0824501668
    formula = "='Dashboard M4 Cost Annual'!BE160/1000000"
    @eval_fn
    def K7():
        be160_1 = Dashboard_M4_Cost_Annual.BE160()
        var_1 = divide(be160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L7():
    # 'Charts_M4_Cost'!L7
    value = 36.1455219366
    formula = "='Dashboard M4 Cost Annual'!BF160/1000000"
    @eval_fn
    def L7():
        bf160_1 = Dashboard_M4_Cost_Annual.BF160()
        var_1 = divide(bf160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M7():
    # 'Charts_M4_Cost'!M7
    value = 22.2725985141
    formula = "='Dashboard M4 Cost Annual'!BG160/1000000"
    @eval_fn
    def M7():
        bg160_1 = Dashboard_M4_Cost_Annual.BG160()
        var_1 = divide(bg160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N7():
    # 'Charts_M4_Cost'!N7
    value = 27.9629154511
    formula = "='Dashboard M4 Cost Annual'!BH160/1000000"
    @eval_fn
    def N7():
        bh160_1 = Dashboard_M4_Cost_Annual.BH160()
        var_1 = divide(bh160_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B8():
    # 'Charts_M4_Cost'!B8
    value = True

@register(Charts_M4_Cost)
class D8():
    # 'Charts_M4_Cost'!D8
    value = "Industrial (Excl. Refineries)"
    formula = "='Dashboard M4 Cost Annual'!A161"
    @eval_fn
    def D8():
        a161_1 = Dashboard_M4_Cost_Annual.A161()
        return a161_1

@register(Charts_M4_Cost)
class G8():
    # 'Charts_M4_Cost'!G8
    value = 10.7244473095
    formula = "='Dashboard M4 Cost Annual'!BA162/1000000"
    @eval_fn
    def G8():
        ba162_1 = Dashboard_M4_Cost_Annual.BA162()
        var_1 = divide(ba162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H8():
    # 'Charts_M4_Cost'!H8
    value = 27.6761347706
    formula = "='Dashboard M4 Cost Annual'!BB162/1000000"
    @eval_fn
    def H8():
        bb162_1 = Dashboard_M4_Cost_Annual.BB162()
        var_1 = divide(bb162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I8():
    # 'Charts_M4_Cost'!I8
    value = 36.6510075005
    formula = "='Dashboard M4 Cost Annual'!BC162/1000000"
    @eval_fn
    def I8():
        bc162_1 = Dashboard_M4_Cost_Annual.BC162()
        var_1 = divide(bc162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J8():
    # 'Charts_M4_Cost'!J8
    value = 32.6524711039
    formula = "='Dashboard M4 Cost Annual'!BD162/1000000"
    @eval_fn
    def J8():
        bd162_1 = Dashboard_M4_Cost_Annual.BD162()
        var_1 = divide(bd162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K8():
    # 'Charts_M4_Cost'!K8
    value = 12.559276632
    formula = "='Dashboard M4 Cost Annual'!BE162/1000000"
    @eval_fn
    def K8():
        be162_1 = Dashboard_M4_Cost_Annual.BE162()
        var_1 = divide(be162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L8():
    # 'Charts_M4_Cost'!L8
    value = 32.0788295069
    formula = "='Dashboard M4 Cost Annual'!BF162/1000000"
    @eval_fn
    def L8():
        bf162_1 = Dashboard_M4_Cost_Annual.BF162()
        var_1 = divide(bf162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M8():
    # 'Charts_M4_Cost'!M8
    value = 22.3931600926
    formula = "='Dashboard M4 Cost Annual'!BG162/1000000"
    @eval_fn
    def M8():
        bg162_1 = Dashboard_M4_Cost_Annual.BG162()
        var_1 = divide(bg162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N8():
    # 'Charts_M4_Cost'!N8
    value = 29.7363887338
    formula = "='Dashboard M4 Cost Annual'!BH162/1000000"
    @eval_fn
    def N8():
        bh162_1 = Dashboard_M4_Cost_Annual.BH162()
        var_1 = divide(bh162_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class D9():
    # 'Charts_M4_Cost'!D9
    value = "Ground and Water Transportation"
    formula = "='Dashboard M4 Cost Annual'!A163"
    @eval_fn
    def D9():
        a163_1 = Dashboard_M4_Cost_Annual.A163()
        return a163_1

@register(Charts_M4_Cost)
class G9():
    # 'Charts_M4_Cost'!G9
    value = 85.283592777
    formula = "='Dashboard M4 Cost Annual'!BA164/1000000"
    @eval_fn
    def G9():
        ba164_1 = Dashboard_M4_Cost_Annual.BA164()
        var_1 = divide(ba164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H9():
    # 'Charts_M4_Cost'!H9
    value = 114.544555931
    formula = "='Dashboard M4 Cost Annual'!BB164/1000000"
    @eval_fn
    def H9():
        bb164_1 = Dashboard_M4_Cost_Annual.BB164()
        var_1 = divide(bb164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I9():
    # 'Charts_M4_Cost'!I9
    value = 169.95567622
    formula = "='Dashboard M4 Cost Annual'!BC164/1000000"
    @eval_fn
    def I9():
        bc164_1 = Dashboard_M4_Cost_Annual.BC164()
        var_1 = divide(bc164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J9():
    # 'Charts_M4_Cost'!J9
    value = 159.563489301
    formula = "='Dashboard M4 Cost Annual'!BD164/1000000"
    @eval_fn
    def J9():
        bd164_1 = Dashboard_M4_Cost_Annual.BD164()
        var_1 = divide(bd164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K9():
    # 'Charts_M4_Cost'!K9
    value = 47.8216771407
    formula = "='Dashboard M4 Cost Annual'!BE164/1000000"
    @eval_fn
    def K9():
        be164_1 = Dashboard_M4_Cost_Annual.BE164()
        var_1 = divide(be164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L9():
    # 'Charts_M4_Cost'!L9
    value = 127.65359851
    formula = "='Dashboard M4 Cost Annual'!BF164/1000000"
    @eval_fn
    def L9():
        bf164_1 = Dashboard_M4_Cost_Annual.BF164()
        var_1 = divide(bf164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M9():
    # 'Charts_M4_Cost'!M9
    value = 61.9470631224
    formula = "='Dashboard M4 Cost Annual'!BG164/1000000"
    @eval_fn
    def M9():
        bg164_1 = Dashboard_M4_Cost_Annual.BG164()
        var_1 = divide(bg164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N9():
    # 'Charts_M4_Cost'!N9
    value = 25.6869797713
    formula = "='Dashboard M4 Cost Annual'!BH164/1000000"
    @eval_fn
    def N9():
        bh164_1 = Dashboard_M4_Cost_Annual.BH164()
        var_1 = divide(bh164_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class D10():
    # 'Charts_M4_Cost'!D10
    value = "Air Transportation"
    formula = "='Dashboard M4 Cost Annual'!A165"
    @eval_fn
    def D10():
        a165_1 = Dashboard_M4_Cost_Annual.A165()
        return a165_1

@register(Charts_M4_Cost)
class G10():
    # 'Charts_M4_Cost'!G10
    value = 53.0465895249
    formula = "='Dashboard M4 Cost Annual'!BA166/1000000"
    @eval_fn
    def G10():
        ba166_1 = Dashboard_M4_Cost_Annual.BA166()
        var_1 = divide(ba166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H10():
    # 'Charts_M4_Cost'!H10
    value = 97.6588725884
    formula = "='Dashboard M4 Cost Annual'!BB166/1000000"
    @eval_fn
    def H10():
        bb166_1 = Dashboard_M4_Cost_Annual.BB166()
        var_1 = divide(bb166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I10():
    # 'Charts_M4_Cost'!I10
    value = 138.310857373
    formula = "='Dashboard M4 Cost Annual'!BC166/1000000"
    @eval_fn
    def I10():
        bc166_1 = Dashboard_M4_Cost_Annual.BC166()
        var_1 = divide(bc166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J10():
    # 'Charts_M4_Cost'!J10
    value = 73.5530812988
    formula = "='Dashboard M4 Cost Annual'!BD166/1000000"
    @eval_fn
    def J10():
        bd166_1 = Dashboard_M4_Cost_Annual.BD166()
        var_1 = divide(bd166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K10():
    # 'Charts_M4_Cost'!K10
    value = 30.1640739985
    formula = "='Dashboard M4 Cost Annual'!BE166/1000000"
    @eval_fn
    def K10():
        be166_1 = Dashboard_M4_Cost_Annual.BE166()
        var_1 = divide(be166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L10():
    # 'Charts_M4_Cost'!L10
    value = 66.0801915234
    formula = "='Dashboard M4 Cost Annual'!BF166/1000000"
    @eval_fn
    def L10():
        bf166_1 = Dashboard_M4_Cost_Annual.BF166()
        var_1 = divide(bf166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M10():
    # 'Charts_M4_Cost'!M10
    value = 27.2277128703
    formula = "='Dashboard M4 Cost Annual'!BG166/1000000"
    @eval_fn
    def M10():
        bg166_1 = Dashboard_M4_Cost_Annual.BG166()
        var_1 = divide(bg166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N10():
    # 'Charts_M4_Cost'!N10
    value = 23.2862953088
    formula = "='Dashboard M4 Cost Annual'!BH166/1000000"
    @eval_fn
    def N10():
        bh166_1 = Dashboard_M4_Cost_Annual.BH166()
        var_1 = divide(bh166_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class D11():
    # 'Charts_M4_Cost'!D11
    value = "All Sectors"
    formula = "='Dashboard M4 Cost Annual'!A169"
    @eval_fn
    def D11():
        a169_1 = Dashboard_M4_Cost_Annual.A169()
        return a169_1

@register(Charts_M4_Cost)
class G11():
    # 'Charts_M4_Cost'!G11
    value = 157.797948029
    formula = "='Dashboard M4 Cost Annual'!BA170/1000000"
    @eval_fn
    def G11():
        ba170_1 = Dashboard_M4_Cost_Annual.BA170()
        var_1 = divide(ba170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H11():
    # 'Charts_M4_Cost'!H11
    value = 281.339979709
    formula = "='Dashboard M4 Cost Annual'!BB170/1000000"
    @eval_fn
    def H11():
        bb170_1 = Dashboard_M4_Cost_Annual.BB170()
        var_1 = divide(bb170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I11():
    # 'Charts_M4_Cost'!I11
    value = 385.102664394
    formula = "='Dashboard M4 Cost Annual'!BC170/1000000"
    @eval_fn
    def I11():
        bc170_1 = Dashboard_M4_Cost_Annual.BC170()
        var_1 = divide(bc170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J11():
    # 'Charts_M4_Cost'!J11
    value = 318.796616241
    formula = "='Dashboard M4 Cost Annual'!BD170/1000000"
    @eval_fn
    def J11():
        bd170_1 = Dashboard_M4_Cost_Annual.BD170()
        var_1 = divide(bd170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K11():
    # 'Charts_M4_Cost'!K11
    value = 102.23603033
    formula = "='Dashboard M4 Cost Annual'!BE170/1000000"
    @eval_fn
    def K11():
        be170_1 = Dashboard_M4_Cost_Annual.BE170()
        var_1 = divide(be170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L11():
    # 'Charts_M4_Cost'!L11
    value = 272.707196632
    formula = "='Dashboard M4 Cost Annual'!BF170/1000000"
    @eval_fn
    def L11():
        bf170_1 = Dashboard_M4_Cost_Annual.BF170()
        var_1 = divide(bf170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M11():
    # 'Charts_M4_Cost'!M11
    value = 121.344692841
    formula = "='Dashboard M4 Cost Annual'!BG170/1000000"
    @eval_fn
    def M11():
        bg170_1 = Dashboard_M4_Cost_Annual.BG170()
        var_1 = divide(bg170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N11():
    # 'Charts_M4_Cost'!N11
    value = 80.5410237803
    formula = "='Dashboard M4 Cost Annual'!BH170/1000000"
    @eval_fn
    def N11():
        bh170_1 = Dashboard_M4_Cost_Annual.BH170()
        var_1 = divide(bh170_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class S11():
    # 'Charts_M4_Cost'!S11
    value = "Note: Fuel consumption of the power sector is accounted for indirectly in each sector's electricity rates. Power sector direct fuel consumption is therefore not included in this metric. Similarly, refinery fuel consumption is accounted for indirectly in sector-level fuel consumption. Therefore, direct fuel consumption of refineries, usually counted in the industrial sector, is excluded from this metric."

@register(Charts_M4_Cost)
class B14():
    # 'Charts_M4_Cost'!B14
    value = "Annual Energy Cost Volatility by Sector"

@register(Charts_M4_Cost)
class S23():
    # 'Charts_M4_Cost'!S23
    value = "Scroll Down to compare by fuel"

@register(Charts_M4_Cost)
class B36():
    # 'Charts_M4_Cost'!B36
    value = True

@register(Charts_M4_Cost)
class B37():
    # 'Charts_M4_Cost'!B37
    value = True

@register(Charts_M4_Cost)
class G37():
    # 'Charts_M4_Cost'!G37
    value = 2006

@register(Charts_M4_Cost)
class H37():
    # 'Charts_M4_Cost'!H37
    value = 2007

@register(Charts_M4_Cost)
class I37():
    # 'Charts_M4_Cost'!I37
    value = 2008

@register(Charts_M4_Cost)
class J37():
    # 'Charts_M4_Cost'!J37
    value = 2009

@register(Charts_M4_Cost)
class K37():
    # 'Charts_M4_Cost'!K37
    value = 2010

@register(Charts_M4_Cost)
class L37():
    # 'Charts_M4_Cost'!L37
    value = 2011

@register(Charts_M4_Cost)
class M37():
    # 'Charts_M4_Cost'!M37
    value = 2012

@register(Charts_M4_Cost)
class N37():
    # 'Charts_M4_Cost'!N37
    value = 2013

@register(Charts_M4_Cost)
class S37():
    # 'Charts_M4_Cost'!S37
    value = "Note: Biodiesel data are obtained through DEBDT. Data begin in October, 2010, are listed as 0 in November, 2010, and present again in December, 2010 and forward. As such, variability in 2010 is extraordinarily high and is removed from this analysis. Analysis on biodiesel begins in 2011, but because consumption data for those years are not yet available, comparisons cannot yet be made."

@register(Charts_M4_Cost)
class B38():
    # 'Charts_M4_Cost'!B38
    value = True

@register(Charts_M4_Cost)
class D38():
    # 'Charts_M4_Cost'!D38
    value = "Electricity"
    formula = "='Dashboard M4 Cost Annual'!B145"
    @eval_fn
    def D38():
        b145_1 = Dashboard_M4_Cost_Annual.B145()
        return b145_1

@register(Charts_M4_Cost)
class G38():
    # 'Charts_M4_Cost'!G38
    value = 23.5070958589
    formula = "='Dashboard M4 Cost Annual'!BA145/1000000"
    @eval_fn
    def G38():
        ba145_1 = Dashboard_M4_Cost_Annual.BA145()
        var_1 = divide(ba145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H38():
    # 'Charts_M4_Cost'!H38
    value = 66.0083137321
    formula = "='Dashboard M4 Cost Annual'!BB145/1000000"
    @eval_fn
    def H38():
        bb145_1 = Dashboard_M4_Cost_Annual.BB145()
        var_1 = divide(bb145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I38():
    # 'Charts_M4_Cost'!I38
    value = 81.3462340129
    formula = "='Dashboard M4 Cost Annual'!BC145/1000000"
    @eval_fn
    def I38():
        bc145_1 = Dashboard_M4_Cost_Annual.BC145()
        var_1 = divide(bc145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J38():
    # 'Charts_M4_Cost'!J38
    value = 74.5719817038
    formula = "='Dashboard M4 Cost Annual'!BD145/1000000"
    @eval_fn
    def J38():
        bd145_1 = Dashboard_M4_Cost_Annual.BD145()
        var_1 = divide(bd145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K38():
    # 'Charts_M4_Cost'!K38
    value = 32.8735982288
    formula = "='Dashboard M4 Cost Annual'!BE145/1000000"
    @eval_fn
    def K38():
        be145_1 = Dashboard_M4_Cost_Annual.BE145()
        var_1 = divide(be145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L38():
    # 'Charts_M4_Cost'!L38
    value = 79.2144837243
    formula = "='Dashboard M4 Cost Annual'!BF145/1000000"
    @eval_fn
    def L38():
        bf145_1 = Dashboard_M4_Cost_Annual.BF145()
        var_1 = divide(bf145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M38():
    # 'Charts_M4_Cost'!M38
    value = 58.9670442728
    formula = "='Dashboard M4 Cost Annual'!BG145/1000000"
    @eval_fn
    def M38():
        bg145_1 = Dashboard_M4_Cost_Annual.BG145()
        var_1 = divide(bg145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N38():
    # 'Charts_M4_Cost'!N38
    value = 78.9903292133
    formula = "='Dashboard M4 Cost Annual'!BH145/1000000"
    @eval_fn
    def N38():
        bh145_1 = Dashboard_M4_Cost_Annual.BH145()
        var_1 = divide(bh145_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B39():
    # 'Charts_M4_Cost'!B39
    value = True

@register(Charts_M4_Cost)
class D39():
    # 'Charts_M4_Cost'!D39
    value = "Gasoline"
    formula = "='Dashboard M4 Cost Annual'!B146"
    @eval_fn
    def D39():
        b146_1 = Dashboard_M4_Cost_Annual.B146()
        return b146_1

@register(Charts_M4_Cost)
class G39():
    # 'Charts_M4_Cost'!G39
    value = 57.7400135535
    formula = "='Dashboard M4 Cost Annual'!BA146/1000000"
    @eval_fn
    def G39():
        ba146_1 = Dashboard_M4_Cost_Annual.BA146()
        var_1 = divide(ba146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H39():
    # 'Charts_M4_Cost'!H39
    value = 73.0765475046
    formula = "='Dashboard M4 Cost Annual'!BB146/1000000"
    @eval_fn
    def H39():
        bb146_1 = Dashboard_M4_Cost_Annual.BB146()
        var_1 = divide(bb146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I39():
    # 'Charts_M4_Cost'!I39
    value = 134.870470996
    formula = "='Dashboard M4 Cost Annual'!BC146/1000000"
    @eval_fn
    def I39():
        bc146_1 = Dashboard_M4_Cost_Annual.BC146()
        var_1 = divide(bc146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J39():
    # 'Charts_M4_Cost'!J39
    value = 121.709415906
    formula = "='Dashboard M4 Cost Annual'!BD146/1000000"
    @eval_fn
    def J39():
        bd146_1 = Dashboard_M4_Cost_Annual.BD146()
        var_1 = divide(bd146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K39():
    # 'Charts_M4_Cost'!K39
    value = 27.2084222805
    formula = "='Dashboard M4 Cost Annual'!BE146/1000000"
    @eval_fn
    def K39():
        be146_1 = Dashboard_M4_Cost_Annual.BE146()
        var_1 = divide(be146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L39():
    # 'Charts_M4_Cost'!L39
    value = 83.8605615783
    formula = "='Dashboard M4 Cost Annual'!BF146/1000000"
    @eval_fn
    def L39():
        bf146_1 = Dashboard_M4_Cost_Annual.BF146()
        var_1 = divide(bf146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M39():
    # 'Charts_M4_Cost'!M39
    value = 43.0271392272
    formula = "='Dashboard M4 Cost Annual'!BG146/1000000"
    @eval_fn
    def M39():
        bg146_1 = Dashboard_M4_Cost_Annual.BG146()
        var_1 = divide(bg146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N39():
    # 'Charts_M4_Cost'!N39
    value = 17.4367121036
    formula = "='Dashboard M4 Cost Annual'!BH146/1000000"
    @eval_fn
    def N39():
        bh146_1 = Dashboard_M4_Cost_Annual.BH146()
        var_1 = divide(bh146_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B40():
    # 'Charts_M4_Cost'!B40
    value = True

@register(Charts_M4_Cost)
class D40():
    # 'Charts_M4_Cost'!D40
    value = "Jet Fuel"
    formula = "='Dashboard M4 Cost Annual'!B147"
    @eval_fn
    def D40():
        b147_1 = Dashboard_M4_Cost_Annual.B147()
        return b147_1

@register(Charts_M4_Cost)
class G40():
    # 'Charts_M4_Cost'!G40
    value = 53.0465895249
    formula = "='Dashboard M4 Cost Annual'!BA147/1000000"
    @eval_fn
    def G40():
        ba147_1 = Dashboard_M4_Cost_Annual.BA147()
        var_1 = divide(ba147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H40():
    # 'Charts_M4_Cost'!H40
    value = 97.6588725884
    formula = "='Dashboard M4 Cost Annual'!BB147/1000000"
    @eval_fn
    def H40():
        bb147_1 = Dashboard_M4_Cost_Annual.BB147()
        var_1 = divide(bb147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I40():
    # 'Charts_M4_Cost'!I40
    value = 138.310857373
    formula = "='Dashboard M4 Cost Annual'!BC147/1000000"
    @eval_fn
    def I40():
        bc147_1 = Dashboard_M4_Cost_Annual.BC147()
        var_1 = divide(bc147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J40():
    # 'Charts_M4_Cost'!J40
    value = 73.5530812988
    formula = "='Dashboard M4 Cost Annual'!BD147/1000000"
    @eval_fn
    def J40():
        bd147_1 = Dashboard_M4_Cost_Annual.BD147()
        var_1 = divide(bd147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K40():
    # 'Charts_M4_Cost'!K40
    value = 30.1640739985
    formula = "='Dashboard M4 Cost Annual'!BE147/1000000"
    @eval_fn
    def K40():
        be147_1 = Dashboard_M4_Cost_Annual.BE147()
        var_1 = divide(be147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L40():
    # 'Charts_M4_Cost'!L40
    value = 66.0801915234
    formula = "='Dashboard M4 Cost Annual'!BF147/1000000"
    @eval_fn
    def L40():
        bf147_1 = Dashboard_M4_Cost_Annual.BF147()
        var_1 = divide(bf147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M40():
    # 'Charts_M4_Cost'!M40
    value = 27.2277128703
    formula = "='Dashboard M4 Cost Annual'!BG147/1000000"
    @eval_fn
    def M40():
        bg147_1 = Dashboard_M4_Cost_Annual.BG147()
        var_1 = divide(bg147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N40():
    # 'Charts_M4_Cost'!N40
    value = 23.2862953088
    formula = "='Dashboard M4 Cost Annual'!BH147/1000000"
    @eval_fn
    def N40():
        bh147_1 = Dashboard_M4_Cost_Annual.BH147()
        var_1 = divide(bh147_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B41():
    # 'Charts_M4_Cost'!B41
    value = True

@register(Charts_M4_Cost)
class D41():
    # 'Charts_M4_Cost'!D41
    value = "Diesel"
    formula = "='Dashboard M4 Cost Annual'!B148"
    @eval_fn
    def D41():
        b148_1 = Dashboard_M4_Cost_Annual.B148()
        return b148_1

@register(Charts_M4_Cost)
class G41():
    # 'Charts_M4_Cost'!G41
    value = 13.6708574836
    formula = "='Dashboard M4 Cost Annual'!BA148/1000000"
    @eval_fn
    def G41():
        ba148_1 = Dashboard_M4_Cost_Annual.BA148()
        var_1 = divide(ba148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H41():
    # 'Charts_M4_Cost'!H41
    value = 45.8639514099
    formula = "='Dashboard M4 Cost Annual'!BB148/1000000"
    @eval_fn
    def H41():
        bb148_1 = Dashboard_M4_Cost_Annual.BB148()
        var_1 = divide(bb148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I41():
    # 'Charts_M4_Cost'!I41
    value = 50.179968021
    formula = "='Dashboard M4 Cost Annual'!BC148/1000000"
    @eval_fn
    def I41():
        bc148_1 = Dashboard_M4_Cost_Annual.BC148()
        var_1 = divide(bc148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J41():
    # 'Charts_M4_Cost'!J41
    value = 38.1646470396
    formula = "='Dashboard M4 Cost Annual'!BD148/1000000"
    @eval_fn
    def J41():
        bd148_1 = Dashboard_M4_Cost_Annual.BD148()
        var_1 = divide(bd148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K41():
    # 'Charts_M4_Cost'!K41
    value = 14.1635869327
    formula = "='Dashboard M4 Cost Annual'!BE148/1000000"
    @eval_fn
    def K41():
        be148_1 = Dashboard_M4_Cost_Annual.BE148()
        var_1 = divide(be148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L41():
    # 'Charts_M4_Cost'!L41
    value = 37.1238494299
    formula = "='Dashboard M4 Cost Annual'!BF148/1000000"
    @eval_fn
    def L41():
        bf148_1 = Dashboard_M4_Cost_Annual.BF148()
        var_1 = divide(bf148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M41():
    # 'Charts_M4_Cost'!M41
    value = 11.2230999906
    formula = "='Dashboard M4 Cost Annual'!BG148/1000000"
    @eval_fn
    def M41():
        bg148_1 = Dashboard_M4_Cost_Annual.BG148()
        var_1 = divide(bg148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N41():
    # 'Charts_M4_Cost'!N41
    value = 5.54942568835
    formula = "='Dashboard M4 Cost Annual'!BH148/1000000"
    @eval_fn
    def N41():
        bh148_1 = Dashboard_M4_Cost_Annual.BH148()
        var_1 = divide(bh148_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B42():
    # 'Charts_M4_Cost'!B42
    value = True

@register(Charts_M4_Cost)
class D42():
    # 'Charts_M4_Cost'!D42
    value = "Fuel Oil"
    formula = "='Dashboard M4 Cost Annual'!B149"
    @eval_fn
    def D42():
        b149_1 = Dashboard_M4_Cost_Annual.B149()
        return b149_1

@register(Charts_M4_Cost)
class G42():
    # 'Charts_M4_Cost'!G42
    value = 20.5507387641
    formula = "='Dashboard M4 Cost Annual'!BA149/1000000"
    @eval_fn
    def G42():
        ba149_1 = Dashboard_M4_Cost_Annual.BA149()
        var_1 = divide(ba149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H42():
    # 'Charts_M4_Cost'!H42
    value = 18.1084571437
    formula = "='Dashboard M4 Cost Annual'!BB149/1000000"
    @eval_fn
    def H42():
        bb149_1 = Dashboard_M4_Cost_Annual.BB149()
        var_1 = divide(bb149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I42():
    # 'Charts_M4_Cost'!I42
    value = 29.331747115
    formula = "='Dashboard M4 Cost Annual'!BC149/1000000"
    @eval_fn
    def I42():
        bc149_1 = Dashboard_M4_Cost_Annual.BC149()
        var_1 = divide(bc149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J42():
    # 'Charts_M4_Cost'!J42
    value = 5.13568060675
    formula = "='Dashboard M4 Cost Annual'!BD149/1000000"
    @eval_fn
    def J42():
        bd149_1 = Dashboard_M4_Cost_Annual.BD149()
        var_1 = divide(bd149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K42():
    # 'Charts_M4_Cost'!K42
    value = 10.5089538996
    formula = "='Dashboard M4 Cost Annual'!BE149/1000000"
    @eval_fn
    def K42():
        be149_1 = Dashboard_M4_Cost_Annual.BE149()
        var_1 = divide(be149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L42():
    # 'Charts_M4_Cost'!L42
    value = 13.339463576
    formula = "='Dashboard M4 Cost Annual'!BF149/1000000"
    @eval_fn
    def L42():
        bf149_1 = Dashboard_M4_Cost_Annual.BF149()
        var_1 = divide(bf149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M42():
    # 'Charts_M4_Cost'!M42
    value = 9.08743261265
    formula = "='Dashboard M4 Cost Annual'!BG149/1000000"
    @eval_fn
    def M42():
        bg149_1 = Dashboard_M4_Cost_Annual.BG149()
        var_1 = divide(bg149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N42():
    # 'Charts_M4_Cost'!N42
    value = 10.5696540124
    formula = "='Dashboard M4 Cost Annual'!BH149/1000000"
    @eval_fn
    def N42():
        bh149_1 = Dashboard_M4_Cost_Annual.BH149()
        var_1 = divide(bh149_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B43():
    # 'Charts_M4_Cost'!B43
    value = True

@register(Charts_M4_Cost)
class D43():
    # 'Charts_M4_Cost'!D43
    value = "LPG"
    formula = "='Dashboard M4 Cost Annual'!B150"
    @eval_fn
    def D43():
        b150_1 = Dashboard_M4_Cost_Annual.B150()
        return b150_1

@register(Charts_M4_Cost)
class G43():
    # 'Charts_M4_Cost'!G43
    value = 2.17348381291
    formula = "='Dashboard M4 Cost Annual'!BA150/1000000"
    @eval_fn
    def G43():
        ba150_1 = Dashboard_M4_Cost_Annual.BA150()
        var_1 = divide(ba150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H43():
    # 'Charts_M4_Cost'!H43
    value = 4.8225733894
    formula = "='Dashboard M4 Cost Annual'!BB150/1000000"
    @eval_fn
    def H43():
        bb150_1 = Dashboard_M4_Cost_Annual.BB150()
        var_1 = divide(bb150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I43():
    # 'Charts_M4_Cost'!I43
    value = 10.8347803653
    formula = "='Dashboard M4 Cost Annual'!BC150/1000000"
    @eval_fn
    def I43():
        bc150_1 = Dashboard_M4_Cost_Annual.BC150()
        var_1 = divide(bc150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J43():
    # 'Charts_M4_Cost'!J43
    value = 10.1865926743
    formula = "='Dashboard M4 Cost Annual'!BD150/1000000"
    @eval_fn
    def J43():
        bd150_1 = Dashboard_M4_Cost_Annual.BD150()
        var_1 = divide(bd150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K43():
    # 'Charts_M4_Cost'!K43
    value = 3.00000936639
    formula = "='Dashboard M4 Cost Annual'!BE150/1000000"
    @eval_fn
    def K43():
        be150_1 = Dashboard_M4_Cost_Annual.BE150()
        var_1 = divide(be150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L43():
    # 'Charts_M4_Cost'!L43
    value = 7.8027407162
    formula = "='Dashboard M4 Cost Annual'!BF150/1000000"
    @eval_fn
    def L43():
        bf150_1 = Dashboard_M4_Cost_Annual.BF150()
        var_1 = divide(bf150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M43():
    # 'Charts_M4_Cost'!M43
    value = 5.73721233006
    formula = "='Dashboard M4 Cost Annual'!BG150/1000000"
    @eval_fn
    def M43():
        bg150_1 = Dashboard_M4_Cost_Annual.BG150()
        var_1 = divide(bg150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N43():
    # 'Charts_M4_Cost'!N43
    value = 4.7965391552
    formula = "='Dashboard M4 Cost Annual'!BH150/1000000"
    @eval_fn
    def N43():
        bh150_1 = Dashboard_M4_Cost_Annual.BH150()
        var_1 = divide(bh150_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B44():
    # 'Charts_M4_Cost'!B44
    value = True

@register(Charts_M4_Cost)
class D44():
    # 'Charts_M4_Cost'!D44
    value = "SNG"
    formula = "='Dashboard M4 Cost Annual'!B151"
    @eval_fn
    def D44():
        b151_1 = Dashboard_M4_Cost_Annual.B151()
        return b151_1

@register(Charts_M4_Cost)
class G44():
    # 'Charts_M4_Cost'!G44
    value = 1.21538951858
    formula = "='Dashboard M4 Cost Annual'!BA151/1000000"
    @eval_fn
    def G44():
        ba151_1 = Dashboard_M4_Cost_Annual.BA151()
        var_1 = divide(ba151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H44():
    # 'Charts_M4_Cost'!H44
    value = 2.53189450585
    formula = "='Dashboard M4 Cost Annual'!BB151/1000000"
    @eval_fn
    def H44():
        bb151_1 = Dashboard_M4_Cost_Annual.BB151()
        var_1 = divide(bb151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I44():
    # 'Charts_M4_Cost'!I44
    value = 4.70145296828
    formula = "='Dashboard M4 Cost Annual'!BC151/1000000"
    @eval_fn
    def I44():
        bc151_1 = Dashboard_M4_Cost_Annual.BC151()
        var_1 = divide(bc151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J44():
    # 'Charts_M4_Cost'!J44
    value = 4.33186063479
    formula = "='Dashboard M4 Cost Annual'!BD151/1000000"
    @eval_fn
    def J44():
        bd151_1 = Dashboard_M4_Cost_Annual.BD151()
        var_1 = divide(bd151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K44():
    # 'Charts_M4_Cost'!K44
    value = 1.40882730901
    formula = "='Dashboard M4 Cost Annual'!BE151/1000000"
    @eval_fn
    def K44():
        be151_1 = Dashboard_M4_Cost_Annual.BE151()
        var_1 = divide(be151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L44():
    # 'Charts_M4_Cost'!L44
    value = 3.95083513664
    formula = "='Dashboard M4 Cost Annual'!BF151/1000000"
    @eval_fn
    def L44():
        bf151_1 = Dashboard_M4_Cost_Annual.BF151()
        var_1 = divide(bf151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M44():
    # 'Charts_M4_Cost'!M44
    value = 1.6951839232
    formula = "='Dashboard M4 Cost Annual'!BG151/1000000"
    @eval_fn
    def M44():
        bg151_1 = Dashboard_M4_Cost_Annual.BG151()
        var_1 = divide(bg151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N44():
    # 'Charts_M4_Cost'!N44
    value = 0.914969123388
    formula = "='Dashboard M4 Cost Annual'!BH151/1000000"
    @eval_fn
    def N44():
        bh151_1 = Dashboard_M4_Cost_Annual.BH151()
        var_1 = divide(bh151_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B45():
    # 'Charts_M4_Cost'!B45
    value = True

@register(Charts_M4_Cost)
class D45():
    # 'Charts_M4_Cost'!D45
    value = "Biodiesel"
    formula = "='Dashboard M4 Cost Annual'!B152"
    @eval_fn
    def D45():
        b152_1 = Dashboard_M4_Cost_Annual.B152()
        return b152_1

@register(Charts_M4_Cost)
class G45():
    # 'Charts_M4_Cost'!G45
    value = 0
    formula = "='Dashboard M4 Cost Annual'!BA152/1000000"
    @eval_fn
    def G45():
        ba152_1 = Dashboard_M4_Cost_Annual.BA152()
        var_1 = divide(ba152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H45():
    # 'Charts_M4_Cost'!H45
    value = 0
    formula = "='Dashboard M4 Cost Annual'!BB152/1000000"
    @eval_fn
    def H45():
        bb152_1 = Dashboard_M4_Cost_Annual.BB152()
        var_1 = divide(bb152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I45():
    # 'Charts_M4_Cost'!I45
    value = 0
    formula = "='Dashboard M4 Cost Annual'!BC152/1000000"
    @eval_fn
    def I45():
        bc152_1 = Dashboard_M4_Cost_Annual.BC152()
        var_1 = divide(bc152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J45():
    # 'Charts_M4_Cost'!J45
    value = 0
    formula = "='Dashboard M4 Cost Annual'!BD152/1000000"
    @eval_fn
    def J45():
        bd152_1 = Dashboard_M4_Cost_Annual.BD152()
        var_1 = divide(bd152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K45():
    # 'Charts_M4_Cost'!K45
    value = 0
    formula = "='Dashboard M4 Cost Annual'!BE152/1000000"
    @eval_fn
    def K45():
        be152_1 = Dashboard_M4_Cost_Annual.BE152()
        var_1 = divide(be152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L45():
    # 'Charts_M4_Cost'!L45
    value = 1.63896086275
    formula = "='Dashboard M4 Cost Annual'!BF152/1000000"
    @eval_fn
    def L45():
        bf152_1 = Dashboard_M4_Cost_Annual.BF152()
        var_1 = divide(bf152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M45():
    # 'Charts_M4_Cost'!M45
    value = 2.60254427131
    formula = "='Dashboard M4 Cost Annual'!BG152/1000000"
    @eval_fn
    def M45():
        bg152_1 = Dashboard_M4_Cost_Annual.BG152()
        var_1 = divide(bg152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N45():
    # 'Charts_M4_Cost'!N45
    value = 1.60059946285
    formula = "='Dashboard M4 Cost Annual'!BH152/1000000"
    @eval_fn
    def N45():
        bh152_1 = Dashboard_M4_Cost_Annual.BH152()
        var_1 = divide(bh152_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class D46():
    # 'Charts_M4_Cost'!D46
    value = "Ethanol"
    formula = "='Dashboard M4 Cost Annual'!B153"
    @eval_fn
    def D46():
        b153_1 = Dashboard_M4_Cost_Annual.B153()
        return b153_1

@register(Charts_M4_Cost)
class G46():
    # 'Charts_M4_Cost'!G46
    value = 1.61967665333
    formula = "='Dashboard M4 Cost Annual'!BA153/1000000"
    @eval_fn
    def G46():
        ba153_1 = Dashboard_M4_Cost_Annual.BA153()
        var_1 = divide(ba153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H46():
    # 'Charts_M4_Cost'!H46
    value = 2.79901749181
    formula = "='Dashboard M4 Cost Annual'!BB153/1000000"
    @eval_fn
    def H46():
        bb153_1 = Dashboard_M4_Cost_Annual.BB153()
        var_1 = divide(bb153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I46():
    # 'Charts_M4_Cost'!I46
    value = 7.2310654988
    formula = "='Dashboard M4 Cost Annual'!BC153/1000000"
    @eval_fn
    def I46():
        bc153_1 = Dashboard_M4_Cost_Annual.BC153()
        var_1 = divide(bc153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J46():
    # 'Charts_M4_Cost'!J46
    value = 7.43826553006
    formula = "='Dashboard M4 Cost Annual'!BD153/1000000"
    @eval_fn
    def J46():
        bd153_1 = Dashboard_M4_Cost_Annual.BD153()
        var_1 = divide(bd153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K46():
    # 'Charts_M4_Cost'!K46
    value = 3.21808106486
    formula = "='Dashboard M4 Cost Annual'!BE153/1000000"
    @eval_fn
    def K46():
        be153_1 = Dashboard_M4_Cost_Annual.BE153()
        var_1 = divide(be153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L46():
    # 'Charts_M4_Cost'!L46
    value = 6.27663553835
    formula = "='Dashboard M4 Cost Annual'!BF153/1000000"
    @eval_fn
    def L46():
        bf153_1 = Dashboard_M4_Cost_Annual.BF153()
        var_1 = divide(bf153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M46():
    # 'Charts_M4_Cost'!M46
    value = 2.16678681089
    formula = "='Dashboard M4 Cost Annual'!BG153/1000000"
    @eval_fn
    def M46():
        bg153_1 = Dashboard_M4_Cost_Annual.BG153()
        var_1 = divide(bg153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N46():
    # 'Charts_M4_Cost'!N46
    value = 1.23843741146
    formula = "='Dashboard M4 Cost Annual'!BH153/1000000"
    @eval_fn
    def N46():
        bh153_1 = Dashboard_M4_Cost_Annual.BH153()
        var_1 = divide(bh153_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class D47():
    # 'Charts_M4_Cost'!D47
    value = "All Fuels"
    formula = "='Dashboard M4 Cost Annual'!B154"
    @eval_fn
    def D47():
        b154_1 = Dashboard_M4_Cost_Annual.B154()
        return b154_1

@register(Charts_M4_Cost)
class G47():
    # 'Charts_M4_Cost'!G47
    value = 157.797948029
    formula = "='Dashboard M4 Cost Annual'!BA154/1000000"
    @eval_fn
    def G47():
        ba154_1 = Dashboard_M4_Cost_Annual.BA154()
        var_1 = divide(ba154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class H47():
    # 'Charts_M4_Cost'!H47
    value = 281.339979709
    formula = "='Dashboard M4 Cost Annual'!BB154/1000000"
    @eval_fn
    def H47():
        bb154_1 = Dashboard_M4_Cost_Annual.BB154()
        var_1 = divide(bb154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class I47():
    # 'Charts_M4_Cost'!I47
    value = 385.102664394
    formula = "='Dashboard M4 Cost Annual'!BC154/1000000"
    @eval_fn
    def I47():
        bc154_1 = Dashboard_M4_Cost_Annual.BC154()
        var_1 = divide(bc154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class J47():
    # 'Charts_M4_Cost'!J47
    value = 318.796616241
    formula = "='Dashboard M4 Cost Annual'!BD154/1000000"
    @eval_fn
    def J47():
        bd154_1 = Dashboard_M4_Cost_Annual.BD154()
        var_1 = divide(bd154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class K47():
    # 'Charts_M4_Cost'!K47
    value = 102.23603033
    formula = "='Dashboard M4 Cost Annual'!BE154/1000000"
    @eval_fn
    def K47():
        be154_1 = Dashboard_M4_Cost_Annual.BE154()
        var_1 = divide(be154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class L47():
    # 'Charts_M4_Cost'!L47
    value = 272.707196632
    formula = "='Dashboard M4 Cost Annual'!BF154/1000000"
    @eval_fn
    def L47():
        bf154_1 = Dashboard_M4_Cost_Annual.BF154()
        var_1 = divide(bf154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class M47():
    # 'Charts_M4_Cost'!M47
    value = 121.344692841
    formula = "='Dashboard M4 Cost Annual'!BG154/1000000"
    @eval_fn
    def M47():
        bg154_1 = Dashboard_M4_Cost_Annual.BG154()
        var_1 = divide(bg154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class N47():
    # 'Charts_M4_Cost'!N47
    value = 80.5410237803
    formula = "='Dashboard M4 Cost Annual'!BH154/1000000"
    @eval_fn
    def N47():
        bh154_1 = Dashboard_M4_Cost_Annual.BH154()
        var_1 = divide(bh154_1, 1000000)
        return var_1

@register(Charts_M4_Cost)
class B51():
    # 'Charts_M4_Cost'!B51
    value = "Annual Energy Cost Volatility by Fuel"