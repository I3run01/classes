class Student:
    def __init__(self, name, age):
        self._name = name #protected
        self._age = age #protected

    @property #call the attribute
    def name(self):
        return self._name

    @name.setter #I can give a new name
    def name(self, v):
        self._name = v
    
p1 = Student('Paola', 27)
p1.name = 'Ana'
print(p1.name)

p1._name  = 'Carla' #I can access a protected attribute
print(p1.name)