# -*- coding: utf-8 -*-
#filename:func_key.py

def func(a,b=2,c=3):
    print("a is ", a , " and b is ", b, "c is ", c)
func(1)    # ab使用的是默认值2，3
func(3,7)  # c使用的是默认值3
func(c=30,a=10) # b使用的是默认值2
