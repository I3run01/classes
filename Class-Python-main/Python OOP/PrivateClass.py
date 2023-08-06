class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property #call the attribute
    def name(self):
        return self.__name

    @name.setter #I can give a new name
    def name(self, v):
        self.__name = v
    
p1 = Student('Paola', 27)
p1.__name = 'Ana'  #Will not set
print(p1.name)

p1.name = 'Carla'  #I have a function to set e another one to get
print(p1.name)

p1._Student__name = 'julia' #I can set or get even a private attribute
print(p1.name) 