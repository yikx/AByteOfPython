# -*- coding: utf-8 -*-
#filemane:using_tuple.py
zoo = ('wolf','elephant','penguin')
print("Number of animals in the zoo is:", len(zoo))

new_zoo = ('Monkey','Dolphin',zoo) #元祖中包含另外一个元祖
print("Numbers of the animals in  the new zoo is:", len(new_zoo))
print("All animals in new zoo are:", new_zoo)
print("Animals brought from old zoo are", new_zoo[2])
print("Last  animals brougth from old zoo is:", new_zoo[2][2]) #二维

