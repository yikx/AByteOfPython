#!/usr/bin/env python
#filename:objvar.py

class Person():
    """Represents a person."""
    population = 0

    def __init__(self, name):
        '''Initalizes the person's data.'''
        self.name = name
        print("(Initializing {})".format(self.name))
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
        
    def __del__(self):    #当对象被删除时候Python会自动调用该方法
        '''I am dying'''
        print("{} says bye.".format(self.name))

        Person.population -= 1

        if Person.population == 0:
            print("I am the last one.")
        else:
            print("There are still {} people left.".format(Person.population))
            
    def sayHi(self):
        '''
            Greeting by the person
            Really, that's all it does.

        '''
        print("Hi, my name is {}".format(self.name))

    def howMany(self):
        '''Prints the current population'''
        if Person.population == 1:
            print("I am the only person here.")
        else:
            print("We have {} persons here.".format(Person.population))

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()


kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

del swaroop #原文采用的是Python的自动回收机制，
            #但是自己测试时无法获得一样结果且
            #无法知道Python自动回收具体时间，因此采用手动删除

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()
                  

        
