# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Input_PV = Worksheet('Input_PV', 10, 10)



@register(Input_PV)
class A1():
    # 'Input_PV'!A1
    value = "http://www.heco.com/portal/site/heco/menuitem.20516707928314340b4c0610c510b1ca/?vgnextoid=3be8e20c52a1b310VgnVCM10000005041aacRCRD&vgnextfmt=default "

@register(Input_PV)
class A2():
    # 'Input_PV'!A2
    value = "KIUC numbers can be found in NEM Filing to PUC"

@register(Input_PV)
class A4():
    # 'Input_PV'!A4
    value = "In MW"

@register(Input_PV)
class O4():
    # 'Input_PV'!O4
    value = "Up to September 30th"

@register(Input_PV)
class B5():
    # 'Input_PV'!B5
    value = 2000

@register(Input_PV)
class C5():
    # 'Input_PV'!C5
    value = 2001

@register(Input_PV)
class D5():
    # 'Input_PV'!D5
    value = 2002

@register(Input_PV)
class E5():
    # 'Input_PV'!E5
    value = 2003

@register(Input_PV)
class F5():
    # 'Input_PV'!F5
    value = 2004

@register(Input_PV)
class G5():
    # 'Input_PV'!G5
    value = 2005

@register(Input_PV)
class H5():
    # 'Input_PV'!H5
    value = 2006

@register(Input_PV)
class I5():
    # 'Input_PV'!I5
    value = 2007

@register(Input_PV)
class J5():
    # 'Input_PV'!J5
    value = 2008

@register(Input_PV)
class K5():
    # 'Input_PV'!K5
    value = 2009

@register(Input_PV)
class L5():
    # 'Input_PV'!L5
    value = 2010

@register(Input_PV)
class M5():
    # 'Input_PV'!M5
    value = 2011

@register(Input_PV)
class N5():
    # 'Input_PV'!N5
    value = 2012

@register(Input_PV)
class O5():
    # 'Input_PV'!O5
    value = 2013

@register(Input_PV)
class P5():
    # 'Input_PV'!P5
    value = 2014

@register(Input_PV)
class Q5():
    # 'Input_PV'!Q5
    value = 2015

@register(Input_PV)
class R5():
    # 'Input_PV'!R5
    value = 2016

@register(Input_PV)
class S5():
    # 'Input_PV'!S5
    value = 2017

@register(Input_PV)
class T5():
    # 'Input_PV'!T5
    value = 2018

@register(Input_PV)
class U5():
    # 'Input_PV'!U5
    value = 2019

@register(Input_PV)
class V5():
    # 'Input_PV'!V5
    value = 2020

@register(Input_PV)
class W5():
    # 'Input_PV'!W5
    value = 2021

@register(Input_PV)
class X5():
    # 'Input_PV'!X5
    value = 2022

@register(Input_PV)
class Y5():
    # 'Input_PV'!Y5
    value = 2023

@register(Input_PV)
class Z5():
    # 'Input_PV'!Z5
    value = 2024

@register(Input_PV)
class AA5():
    # 'Input_PV'!AA5
    value = 2025

@register(Input_PV)
class AB5():
    # 'Input_PV'!AB5
    value = 2026

@register(Input_PV)
class AC5():
    # 'Input_PV'!AC5
    value = 2027

@register(Input_PV)
class AD5():
    # 'Input_PV'!AD5
    value = 2028

@register(Input_PV)
class AE5():
    # 'Input_PV'!AE5
    value = 2029

@register(Input_PV)
class AF5():
    # 'Input_PV'!AF5
    value = 2030

@register(Input_PV)
class A6():
    # 'Input_PV'!A6
    value = "HECO Companies"

@register(Input_PV)
class G6():
    # 'Input_PV'!G6
    value = 1.8

@register(Input_PV)
class H6():
    # 'Input_PV'!H6
    value = 2.4

@register(Input_PV)
class I6():
    # 'Input_PV'!I6
    value = 4.7

@register(Input_PV)
class J6():
    # 'Input_PV'!J6
    value = 12

@register(Input_PV)
class K6():
    # 'Input_PV'!K6
    value = 24

@register(Input_PV)
class L6():
    # 'Input_PV'!L6
    value = 40

@register(Input_PV)
class M6():
    # 'Input_PV'!M6
    value = 79

@register(Input_PV)
class N6():
    # 'Input_PV'!N6
    value = 172

@register(Input_PV)
class O6():
    # 'Input_PV'!O6
    value = 261

@register(Input_PV)
class A7():
    # 'Input_PV'!A7
    value = "KIUC"

@register(Input_PV)
class I7():
    # 'Input_PV'!I7
    value = 0.544

@register(Input_PV)
class J7():
    # 'Input_PV'!J7
    value = 1.169

@register(Input_PV)
class K7():
    # 'Input_PV'!K7
    value = 1.439

@register(Input_PV)
class L7():
    # 'Input_PV'!L7
    value = 1.605

@register(Input_PV)
class M7():
    # 'Input_PV'!M7
    value = 1.945

@register(Input_PV)
class N7():
    # 'Input_PV'!N7
    value = 2.197

@register(Input_PV)
class A8():
    # 'Input_PV'!A8
    value = "Total "

@register(Input_PV)
class G8():
    # 'Input_PV'!G8
    value = 1.8
    formula = "=SUM(G6:G7)"
    @eval_fn
    def G8():
        range_1 = Input_PV(7, 6, 7, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class H8():
    # 'Input_PV'!H8
    value = 2.4
    formula = "=SUM(H6:H7)"
    @eval_fn
    def H8():
        range_1 = Input_PV(8, 6, 8, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class I8():
    # 'Input_PV'!I8
    value = 5.244
    formula = "=SUM(I6:I7)"
    @eval_fn
    def I8():
        range_1 = Input_PV(9, 6, 9, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class J8():
    # 'Input_PV'!J8
    value = 13.169
    formula = "=SUM(J6:J7)"
    @eval_fn
    def J8():
        range_1 = Input_PV(10, 6, 10, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class K8():
    # 'Input_PV'!K8
    value = 25.439
    formula = "=SUM(K6:K7)"
    @eval_fn
    def K8():
        range_1 = Input_PV(11, 6, 11, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class L8():
    # 'Input_PV'!L8
    value = 41.605
    formula = "=SUM(L6:L7)"
    @eval_fn
    def L8():
        range_1 = Input_PV(12, 6, 12, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class M8():
    # 'Input_PV'!M8
    value = 80.945
    formula = "=SUM(M6:M7)"
    @eval_fn
    def M8():
        range_1 = Input_PV(13, 6, 13, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class N8():
    # 'Input_PV'!N8
    value = 174.197
    formula = "=SUM(N6:N7)"
    @eval_fn
    def N8():
        range_1 = Input_PV(14, 6, 14, 7)
        var_1 = SUM(range_1)
        return var_1

@register(Input_PV)
class O8():
    # 'Input_PV'!O8
    value = 261
    formula = "=SUM(O6:O7)"
    @eval_fn
    def O8():
        range_1 = Input_PV(15, 6, 15, 7)
        var_1 = SUM(range_1)
        return var_1