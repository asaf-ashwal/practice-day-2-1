class Vahicles:
    def __init__(self, brand, modle):
        self.brand = brand
        self.modle = modle
    def move(self):
        print('The vehicle is moving')
        
class Car(Vahicles):
    def move(self):
        print('The car is drives')
    
class Plane(Vahicles):
    def move(self):
        print('The plane is flies')
        
# x = Vahicles('bla','xla')
# x.move()
# toyota = Car('toyota','camary')
# toyota.move()
# plane = Plane('boing',707)
# plane.move()



class Animal:
    def __init__(self, type):
        self.type = type
    def sound(self):
         return f'The {self.type} sound is: '
        
class Dog(Animal):
    def __init__(self,type, sou):
        super().__init__(type)
        self.sou = sou        
    def sound(self):
        return super().sound() + self.sou

class Cat(Animal):
    def __init__(self,type, sou):
        super().__init__(type)
        self.sou = sou        
    def sound(self):
        return super().sound() + self.sou      
        
# chumba = Dog('dog',"woof")
# print(chumba.sound())


class Shape:
    def area(self):
        raise  NotImplementedError
class Rectangle(Shape):
    def __init__(self,width, height):
        super().__init__()
        self.height = height
        self.width = width
    
    def area(self):
        # super().area()
        return self.height * self.width
    
class Circle(Shape):
    def __init__(self,rad):
        super().__init__()
        self.rad = rad
    
    def radius(self):
        # super().radius()
        return self.rad * 3.14
x = Circle(2)
print(x.radius())