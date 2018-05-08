#_*_ coding:utf-8 _*_
#filename:list_comprehension.py

listone = [2,3,4]
listtwo = [ 2*i for i in listone if i > 2]
print(listtwo)  # [6,8]
