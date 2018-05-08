# -*- coding: utf-8 -*-
#filename:str_method.py

name = "Swaroop"

if name.startswith('Swa'): # 判断字符串是否以"Swa:"开头
    print("Yes, the String starts with 'Swa'")
if 'a' in name:
    print("Yes,it contains the string 'a'")
if name.find('war') !=-1:
    print("Yes, it contains the string 'war'")

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print (delimiter.join(mylist))

