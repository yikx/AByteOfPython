#! usr/bin/env python
#filename:class_init.py

class Person():
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print("Hello, my name is ", self.name)

p = Person("zhangsan")
p.sayHi()
