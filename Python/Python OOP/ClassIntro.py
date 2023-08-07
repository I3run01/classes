from lib2to3.pgen2.pgen import DFAState
from mimetypes import init


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(self):
        print(f'My name is {self.name}')

    def myage(self):
        print(f'I am {self.age}')

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation = year

    def welcome(self):
        print(f'Welcome {self.name}')




p1 = Student('Daniel', 18, 2020)
p1.welcome()