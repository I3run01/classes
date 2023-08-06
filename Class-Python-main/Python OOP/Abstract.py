from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @abstractclassmethod
    def fullname(self):
        print('test')

    
    
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def fullname(self):
        return (f'{self.fname} {self.lname}')

p1 = Student('john', 'Cannor', 2020)
print(p1.fullname())
    