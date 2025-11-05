from abc import ABC, abstractmethod

class  Vehicle:
    def __init__(self, max_speed:int):
        self.max_speed = max_speed
    def __str__(self):
        return f'This vehicle max_speed is: {self.max_speed}'
    def drive(self):
        return  f'This vehicle max_speed is: {self.max_speed}'
        
        
    
class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass
# t = Motorcycle(35)
# print(t.drive())



class Employee:
    def __init__(self, name:str, salary:int):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def manage(self):
        return f'{self.name} is a manager, and is salery ia: {self.salary}'
class Developer(Employee):
    def write_code(self):
        return f'{self.name} is an employee, how is writes code on e salary of: {self.salary}'

# c = Developer('dan',180)
# print(c.write_code())



class Shapes_Area(ABC):
    @abstractmethod
    def area(self):
        return 'hahaha'
    
    
class Rectangle(Shapes_Area):
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
        
# r =  Rectangle(15,2) 
# print(r.area())
        
class Circle(Shapes_Area):
    def __init__(self, radius:int):
        self.radius = radius
    def area(self):
        pi:int = 3.141
        return (self.radius ** 2) * pi
# c = Circle(8)
# print(c.area())


class Square(Shapes_Area): 
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
class Payment():
    def __init__(self,method_name:str):
        self.method_name = method_name
class CreditCardPayment(Payment):
    def pay(self,amount:int):
        return f'{self.method_name} payed: {amount} on the credit card payment.'
    
class PayPalPayment(Payment):
    def pay(self,amount:int):
        return f'{self.method_name} payed: {amount} on the PayPal payment.'
# x = PayPalPayment('bla')
# print(x.pay(15))

class Engine:
    def __init__(self,horsepower:int):
        self.horsepower = horsepower
class Car2:
    def __init__(self, brand:str
                 , engine:Engine )