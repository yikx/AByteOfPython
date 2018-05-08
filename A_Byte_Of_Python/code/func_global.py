# -*- coding: utf-8 -*-
# filename:func_global.py

def func():
    global x  # 将x定义为全局变量
    print("x is", x )
    x = 2         #函数内部定义一个局部变量x=2
    print("Changed local x to", x) #
x = 50 # 在函数外部顶一个全局变量 x=50
func()
print("the global x is:", x) # 全局变量x别修改为2
