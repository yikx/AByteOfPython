# -*- coding: utf-8 -*-
# filenamne:using_list.py

#This is my shopping list
shoplist = ['apple', 'mango','carrot', 'banana']

print("I have ", len(shoplist),'items to purchase')

for item in shoplist:
    print(item, end=',')
print("\nI also have tyo buy rise.")
shoplist.append("rise")
print("My shopping list is now:", shoplist)

print("I will sort my list now")
shoplist.sort()
print("Sorted shoppling list is:", shoplist)

print("The first item I will buy is:" , shoplist[0])

olditem = shoplist[0]
del shoplist[0]
print("I bought the", olditem)
print("My shoplist is now", shoplist)
