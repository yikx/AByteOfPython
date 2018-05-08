# -*- coding: utf-8 -*-
#filename:reference.py

print("Simple Assignmet")

shoplist = ['apple','mango','carrot', 'banana']
mylist = shoplist  
print("The id of mylist is ",id(mylist))
print("The id of shoplist is ",id(shoplist))
del shoplist[0]
print("shoplist is ", shoplist)
print("my list is ", mylist)

print("copy by making a full slice")
mylist = shoplist[:] # 内存中备份一份shoplist的内容，然后mylist指向改地址，mylist和shoplist两个完全不同、
print("The id of mylist is ",id(mylist))
print("The id of shoplist is ",id(shoplist))
del mylist[0] 
print("shoplist is ", shoplist)
print("my list is ", mylist)