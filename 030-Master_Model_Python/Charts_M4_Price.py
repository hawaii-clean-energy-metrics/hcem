# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Charts_M4_Price = Worksheet('Charts_M4_Price', 10, 10)



@register(Charts_M4_Price)
class B2():
    # 'Charts_M4_Price'!B2
    value = True

@register(Charts_M4_Price)
class D2():
    # 'Charts_M4_Price'!D2
    value = "Metric 4: Hawaii energy portfolio price volatility"

@register(Charts_M4_Price)
class B3():
    # 'Charts_M4_Price'!B3
    value = True

@register(Charts_M4_Price)
class B4():
    # 'Charts_M4_Price'!B4
    value = True

@register(Charts_M4_Price)
class B5():
    # 'Charts_M4_Price'!B5
    value = True

@register(Charts_M4_Price)
class H5():
    # 'Charts_M4_Price'!H5
    value = 2006

@register(Charts_M4_Price)
class I5():
    # 'Charts_M4_Price'!I5
    value = 2007

@register(Charts_M4_Price)
class J5():
    # 'Charts_M4_Price'!J5
    value = 2008

@register(Charts_M4_Price)
class K5():
    # 'Charts_M4_Price'!K5
    value = 2009

@register(Charts_M4_Price)
class L5():
    # 'Charts_M4_Price'!L5
    value = 2010

@register(Charts_M4_Price)
class M5():
    # 'Charts_M4_Price'!M5
    value = 2011

@register(Charts_M4_Price)
class N5():
    # 'Charts_M4_Price'!N5
    value = 2012

@register(Charts_M4_Price)
class O5():
    # 'Charts_M4_Price'!O5
    value = 2013

@register(Charts_M4_Price)
class R5():
    # 'Charts_M4_Price'!R5
    value = "Note: Fuel consumption of the power sector is accounted for indirectly in each sector's electricity rates. Power sector direct fuel consumption is therefore not included in this metric. Similarly, refinery fuel consumption is accounted for indirectly in sector-level fuel consumption. Therefore, direct fuel consumption of refineries, usually counted in the industrial sector, is excluded from this metric."

@register(Charts_M4_Price)
class B6():
    # 'Charts_M4_Price'!B6
    value = True

@register(Charts_M4_Price)
class E6():
    # 'Charts_M4_Price'!E6
    value = "Residential"
    formula = "='Charts Data M4 Price'!B2"
    @eval_fn
    def E6():
        b2_1 = Charts_Data_M4_Price.B2()
        return b2_1

@register(Charts_M4_Price)
class H6():
    # 'Charts_M4_Price'!H6
    value = 6.95872707244
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA87,"")'''
    @eval_fn
    def H6():
        ba87_1 = Dashboard_M4_Price_Annual.BA87()
        var_1 = IFERROR(ba87_1, "")
        return var_1

@register(Charts_M4_Price)
class I6():
    # 'Charts_M4_Price'!I6
    value = 17.9005877397
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB87,"")'''
    @eval_fn
    def I6():
        bb87_1 = Dashboard_M4_Price_Annual.BB87()
        var_1 = IFERROR(bb87_1, "")
        return var_1

@register(Charts_M4_Price)
class J6():
    # 'Charts_M4_Price'!J6
    value = 22.6815030407
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC87,"")'''
    @eval_fn
    def J6():
        bc87_1 = Dashboard_M4_Price_Annual.BC87()
        var_1 = IFERROR(bc87_1, "")
        return var_1

@register(Charts_M4_Price)
class K6():
    # 'Charts_M4_Price'!K6
    value = 15.5912398601
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD87,"")'''
    @eval_fn
    def K6():
        bd87_1 = Dashboard_M4_Price_Annual.BD87()
        var_1 = IFERROR(bd87_1, "")
        return var_1

@register(Charts_M4_Price)
class L6():
    # 'Charts_M4_Price'!L6
    value = 4.77226646786
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE87,"")'''
    @eval_fn
    def L6():
        be87_1 = Dashboard_M4_Price_Annual.BE87()
        var_1 = IFERROR(be87_1, "")
        return var_1

@register(Charts_M4_Price)
class M6():
    # 'Charts_M4_Price'!M6
    value = 20.4701213375
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF87,"")'''
    @eval_fn
    def M6():
        bf87_1 = Dashboard_M4_Price_Annual.BF87()
        var_1 = IFERROR(bf87_1, "")
        return var_1

@register(Charts_M4_Price)
class N6():
    # 'Charts_M4_Price'!N6
    value = 5.55732131777
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG87,"")'''
    @eval_fn
    def N6():
        bg87_1 = Dashboard_M4_Price_Annual.BG87()
        var_1 = IFERROR(bg87_1, "")
        return var_1

@register(Charts_M4_Price)
class O6():
    # 'Charts_M4_Price'!O6
    value = 7.24505063002
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH87,"")'''
    @eval_fn
    def O6():
        bh87_1 = Dashboard_M4_Price_Annual.BH87()
        var_1 = IFERROR(bh87_1, "")
        return var_1

@register(Charts_M4_Price)
class B7():
    # 'Charts_M4_Price'!B7
    value = False

@register(Charts_M4_Price)
class E7():
    # 'Charts_M4_Price'!E7
    value = "Commercial"
    formula = "='Charts Data M4 Price'!B3"
    @eval_fn
    def E7():
        b3_1 = Charts_Data_M4_Price.B3()
        return b3_1

@register(Charts_M4_Price)
class H7():
    # 'Charts_M4_Price'!H7
    value = 4.67007909812
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA89,"")'''
    @eval_fn
    def H7():
        ba89_1 = Dashboard_M4_Price_Annual.BA89()
        var_1 = IFERROR(ba89_1, "")
        return var_1

@register(Charts_M4_Price)
class I7():
    # 'Charts_M4_Price'!I7
    value = 13.3458819563
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB89,"")'''
    @eval_fn
    def I7():
        bb89_1 = Dashboard_M4_Price_Annual.BB89()
        var_1 = IFERROR(bb89_1, "")
        return var_1

@register(Charts_M4_Price)
class J7():
    # 'Charts_M4_Price'!J7
    value = 17.5030113071
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC89,"")'''
    @eval_fn
    def J7():
        bc89_1 = Dashboard_M4_Price_Annual.BC89()
        var_1 = IFERROR(bc89_1, "")
        return var_1

@register(Charts_M4_Price)
class K7():
    # 'Charts_M4_Price'!K7
    value = 10.5214521755
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD89,"")'''
    @eval_fn
    def K7():
        bd89_1 = Dashboard_M4_Price_Annual.BD89()
        var_1 = IFERROR(bd89_1, "")
        return var_1

@register(Charts_M4_Price)
class L7():
    # 'Charts_M4_Price'!L7
    value = 3.27340543164
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE89,"")'''
    @eval_fn
    def L7():
        be89_1 = Dashboard_M4_Price_Annual.BE89()
        var_1 = IFERROR(be89_1, "")
        return var_1

@register(Charts_M4_Price)
class M7():
    # 'Charts_M4_Price'!M7
    value = 13.2338444777
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF89,"")'''
    @eval_fn
    def M7():
        bf89_1 = Dashboard_M4_Price_Annual.BF89()
        var_1 = IFERROR(bf89_1, "")
        return var_1

@register(Charts_M4_Price)
class N7():
    # 'Charts_M4_Price'!N7
    value = 4.58416789746
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG89,"")'''
    @eval_fn
    def N7():
        bg89_1 = Dashboard_M4_Price_Annual.BG89()
        var_1 = IFERROR(bg89_1, "")
        return var_1

@register(Charts_M4_Price)
class O7():
    # 'Charts_M4_Price'!O7
    value = 6.91522399393
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH89,"")'''
    @eval_fn
    def O7():
        bh89_1 = Dashboard_M4_Price_Annual.BH89()
        var_1 = IFERROR(bh89_1, "")
        return var_1

@register(Charts_M4_Price)
class B8():
    # 'Charts_M4_Price'!B8
    value = True

@register(Charts_M4_Price)
class E8():
    # 'Charts_M4_Price'!E8
    value = "Industrial (Excl. Refineries)"
    formula = "='Charts Data M4 Price'!B4"
    @eval_fn
    def E8():
        b4_1 = Charts_Data_M4_Price.B4()
        return b4_1

@register(Charts_M4_Price)
class H8():
    # 'Charts_M4_Price'!H8
    value = 4.17564035271
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA91,"")'''
    @eval_fn
    def H8():
        ba91_1 = Dashboard_M4_Price_Annual.BA91()
        var_1 = IFERROR(ba91_1, "")
        return var_1

@register(Charts_M4_Price)
class I8():
    # 'Charts_M4_Price'!I8
    value = 12.8541800252
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB91,"")'''
    @eval_fn
    def I8():
        bb91_1 = Dashboard_M4_Price_Annual.BB91()
        var_1 = IFERROR(bb91_1, "")
        return var_1

@register(Charts_M4_Price)
class J8():
    # 'Charts_M4_Price'!J8
    value = 20.4518667101
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC91,"")'''
    @eval_fn
    def J8():
        bc91_1 = Dashboard_M4_Price_Annual.BC91()
        var_1 = IFERROR(bc91_1, "")
        return var_1

@register(Charts_M4_Price)
class K8():
    # 'Charts_M4_Price'!K8
    value = 11.0057538618
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD91,"")'''
    @eval_fn
    def K8():
        bd91_1 = Dashboard_M4_Price_Annual.BD91()
        var_1 = IFERROR(bd91_1, "")
        return var_1

@register(Charts_M4_Price)
class L8():
    # 'Charts_M4_Price'!L8
    value = 3.91279273563
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE91,"")'''
    @eval_fn
    def L8():
        be91_1 = Dashboard_M4_Price_Annual.BE91()
        var_1 = IFERROR(be91_1, "")
        return var_1

@register(Charts_M4_Price)
class M8():
    # 'Charts_M4_Price'!M8
    value = 16.6002387534
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF91,"")'''
    @eval_fn
    def M8():
        bf91_1 = Dashboard_M4_Price_Annual.BF91()
        var_1 = IFERROR(bf91_1, "")
        return var_1

@register(Charts_M4_Price)
class N8():
    # 'Charts_M4_Price'!N8
    value = 4.88347017712
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG91,"")'''
    @eval_fn
    def N8():
        bg91_1 = Dashboard_M4_Price_Annual.BG91()
        var_1 = IFERROR(bg91_1, "")
        return var_1

@register(Charts_M4_Price)
class O8():
    # 'Charts_M4_Price'!O8
    value = 7.33333226616
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH91,"")'''
    @eval_fn
    def O8():
        bh91_1 = Dashboard_M4_Price_Annual.BH91()
        var_1 = IFERROR(bh91_1, "")
        return var_1

@register(Charts_M4_Price)
class E9():
    # 'Charts_M4_Price'!E9
    value = "Ground and Water Transportation"
    formula = "='Charts Data M4 Price'!B5"
    @eval_fn
    def E9():
        b5_1 = Charts_Data_M4_Price.B5()
        return b5_1

@register(Charts_M4_Price)
class H9():
    # 'Charts_M4_Price'!H9
    value = 3.02944189468
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA93,"")'''
    @eval_fn
    def H9():
        ba93_1 = Dashboard_M4_Price_Annual.BA93()
        var_1 = IFERROR(ba93_1, "")
        return var_1

@register(Charts_M4_Price)
class I9():
    # 'Charts_M4_Price'!I9
    value = 7.25777400563
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB93,"")'''
    @eval_fn
    def I9():
        bb93_1 = Dashboard_M4_Price_Annual.BB93()
        var_1 = IFERROR(bb93_1, "")
        return var_1

@register(Charts_M4_Price)
class J9():
    # 'Charts_M4_Price'!J9
    value = 15.8235264666
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC93,"")'''
    @eval_fn
    def J9():
        bc93_1 = Dashboard_M4_Price_Annual.BC93()
        var_1 = IFERROR(bc93_1, "")
        return var_1

@register(Charts_M4_Price)
class K9():
    # 'Charts_M4_Price'!K9
    value = 9.26806421521
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD93,"")'''
    @eval_fn
    def K9():
        bd93_1 = Dashboard_M4_Price_Annual.BD93()
        var_1 = IFERROR(bd93_1, "")
        return var_1

@register(Charts_M4_Price)
class L9():
    # 'Charts_M4_Price'!L9
    value = 1.51785210063
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE93,"")'''
    @eval_fn
    def L9():
        be93_1 = Dashboard_M4_Price_Annual.BE93()
        var_1 = IFERROR(be93_1, "")
        return var_1

@register(Charts_M4_Price)
class M9():
    # 'Charts_M4_Price'!M9
    value = 5.4684812863
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF93,"")'''
    @eval_fn
    def M9():
        bf93_1 = Dashboard_M4_Price_Annual.BF93()
        var_1 = IFERROR(bf93_1, "")
        return var_1

@register(Charts_M4_Price)
class N9():
    # 'Charts_M4_Price'!N9
    value = 3.82958024021
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG93,"")'''
    @eval_fn
    def N9():
        bg93_1 = Dashboard_M4_Price_Annual.BG93()
        var_1 = IFERROR(bg93_1, "")
        return var_1

@register(Charts_M4_Price)
class O9():
    # 'Charts_M4_Price'!O9
    value = 2.54575148553
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH93,"")'''
    @eval_fn
    def O9():
        bh93_1 = Dashboard_M4_Price_Annual.BH93()
        var_1 = IFERROR(bh93_1, "")
        return var_1

@register(Charts_M4_Price)
class E10():
    # 'Charts_M4_Price'!E10
    value = "Air Transportation"
    formula = "='Charts Data M4 Price'!B6"
    @eval_fn
    def E10():
        b6_1 = Charts_Data_M4_Price.B6()
        return b6_1

@register(Charts_M4_Price)
class H10():
    # 'Charts_M4_Price'!H10
    value = 4.79876997762
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA95,"")'''
    @eval_fn
    def H10():
        ba95_1 = Dashboard_M4_Price_Annual.BA95()
        var_1 = IFERROR(ba95_1, "")
        return var_1

@register(Charts_M4_Price)
class I10():
    # 'Charts_M4_Price'!I10
    value = 9.00063397269
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB95,"")'''
    @eval_fn
    def I10():
        bb95_1 = Dashboard_M4_Price_Annual.BB95()
        var_1 = IFERROR(bb95_1, "")
        return var_1

@register(Charts_M4_Price)
class J10():
    # 'Charts_M4_Price'!J10
    value = 23.0705693513
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC95,"")'''
    @eval_fn
    def J10():
        bc95_1 = Dashboard_M4_Price_Annual.BC95()
        var_1 = IFERROR(bc95_1, "")
        return var_1

@register(Charts_M4_Price)
class K10():
    # 'Charts_M4_Price'!K10
    value = 7.94568497795
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD95,"")'''
    @eval_fn
    def K10():
        bd95_1 = Dashboard_M4_Price_Annual.BD95()
        var_1 = IFERROR(bd95_1, "")
        return var_1

@register(Charts_M4_Price)
class L10():
    # 'Charts_M4_Price'!L10
    value = 4.04184649021
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE95,"")'''
    @eval_fn
    def L10():
        be95_1 = Dashboard_M4_Price_Annual.BE95()
        var_1 = IFERROR(be95_1, "")
        return var_1

@register(Charts_M4_Price)
class M10():
    # 'Charts_M4_Price'!M10
    value = 4.8137194326
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF95,"")'''
    @eval_fn
    def M10():
        bf95_1 = Dashboard_M4_Price_Annual.BF95()
        var_1 = IFERROR(bf95_1, "")
        return var_1

@register(Charts_M4_Price)
class N10():
    # 'Charts_M4_Price'!N10
    value = 4.94237888448
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG95,"")'''
    @eval_fn
    def N10():
        bg95_1 = Dashboard_M4_Price_Annual.BG95()
        var_1 = IFERROR(bg95_1, "")
        return var_1

@register(Charts_M4_Price)
class O10():
    # 'Charts_M4_Price'!O10
    value = 4.003429333
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH95,"")'''
    @eval_fn
    def O10():
        bh95_1 = Dashboard_M4_Price_Annual.BH95()
        var_1 = IFERROR(bh95_1, "")
        return var_1

@register(Charts_M4_Price)
class E11():
    # 'Charts_M4_Price'!E11
    value = "All Sectors"
    formula = "='Charts Data M4 Price'!B8"
    @eval_fn
    def E11():
        b8_1 = Charts_Data_M4_Price.B8()
        return b8_1

@register(Charts_M4_Price)
class H11():
    # 'Charts_M4_Price'!H11
    value = 2.94216499129
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BA108,"")'''
    @eval_fn
    def H11():
        ba108_1 = Dashboard_M4_Price_Annual.BA108()
        var_1 = IFERROR(ba108_1, "")
        return var_1

@register(Charts_M4_Price)
class I11():
    # 'Charts_M4_Price'!I11
    value = 7.82841838123
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BB108,"")'''
    @eval_fn
    def I11():
        bb108_1 = Dashboard_M4_Price_Annual.BB108()
        var_1 = IFERROR(bb108_1, "")
        return var_1

@register(Charts_M4_Price)
class J11():
    # 'Charts_M4_Price'!J11
    value = 16.8976812311
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BC108,"")'''
    @eval_fn
    def J11():
        bc108_1 = Dashboard_M4_Price_Annual.BC108()
        var_1 = IFERROR(bc108_1, "")
        return var_1

@register(Charts_M4_Price)
class K11():
    # 'Charts_M4_Price'!K11
    value = 6.67536892777
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BD108,"")'''
    @eval_fn
    def K11():
        bd108_1 = Dashboard_M4_Price_Annual.BD108()
        var_1 = IFERROR(bd108_1, "")
        return var_1

@register(Charts_M4_Price)
class L11():
    # 'Charts_M4_Price'!L11
    value = 1.92767671388
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BE108,"")'''
    @eval_fn
    def L11():
        be108_1 = Dashboard_M4_Price_Annual.BE108()
        var_1 = IFERROR(be108_1, "")
        return var_1

@register(Charts_M4_Price)
class M11():
    # 'Charts_M4_Price'!M11
    value = 4.55813844338
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BF108,"")'''
    @eval_fn
    def M11():
        bf108_1 = Dashboard_M4_Price_Annual.BF108()
        var_1 = IFERROR(bf108_1, "")
        return var_1

@register(Charts_M4_Price)
class N11():
    # 'Charts_M4_Price'!N11
    value = 3.99811262042
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BG108,"")'''
    @eval_fn
    def N11():
        bg108_1 = Dashboard_M4_Price_Annual.BG108()
        var_1 = IFERROR(bg108_1, "")
        return var_1

@register(Charts_M4_Price)
class O11():
    # 'Charts_M4_Price'!O11
    value = 3.35844308954
    formula = '''=IFERROR('Dashboard M4 Price Annual'!BH108,"")'''
    @eval_fn
    def O11():
        bh108_1 = Dashboard_M4_Price_Annual.BH108()
        var_1 = IFERROR(bh108_1, "")
        return var_1

@register(Charts_M4_Price)
class B13():
    # 'Charts_M4_Price'!B13
    value = "Annual Energy Price Volatility by Sector"

@register(Charts_M4_Price)
class B37():
    # 'Charts_M4_Price'!B37
    value = "Annual Energy Price Volatility by Sector (as percent of sector annual fuel price)"