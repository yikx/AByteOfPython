# -*- coding: utf-8 -*-
#filename:function2.py

def printMax(a,b):
    if a > b:
        print(a,"is maximum")
    else:
        print(b,"is maximum")
        
printMax(3,4) #直接调用函数
x = 4
y = 5
printMax(x,y) # 给定变量作为参数