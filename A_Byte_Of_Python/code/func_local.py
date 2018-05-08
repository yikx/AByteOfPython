# -*- coding: utf-8 -*-
# filename:func_local.py

def func(x):
    print("x is", x )
    x = 2         #函数内部定义一个局部变量x=2
    print("Changed local x to", x) #
x = 50 # 在函数外部顶一个全局变量 x=50
func(x)
print("the glbal x is:", x) # 全局变量x并没有改变
