# -*- coding: utf-8 -*-
#filename:inherit.py

class SchoolMember(object):
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember: {}".format(self.name))
    def tell(self):
        '''Tell my details.'''
        print("Name:{} Age {}".format(self.name, self.age))
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: {}".format(self.name))
        
    def tell(self):
        SchoolMember.tell(self) #调用了父类ShoolMember的tell方法
        print("Salary：{}".format(self.salary))
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized Student: {}".format(self.name))
    def tell(self):
        SchoolMember.tell(self) #调用了父类ShoolMember的tell方法
        print("Marks: {}".format(self.marks))        
        
t = Teacher('Mrs.zhang', 40, 30000)
s = Student('lisi',20,100)
print # print a blank line

members = [t,s]
for member in members:
    member.tell()   #works for both Teachers and Students