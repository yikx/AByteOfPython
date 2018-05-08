# -*- coding: utf-8 -*-
#filename:sys_module.py
import sys

print("The commadnd line arguments are: ")
for i in sys.argv:# 打印sys.argv的参数列表
    print(i)
print("\n\nThe PYTHONPATH is:", sys.path,"\n")

