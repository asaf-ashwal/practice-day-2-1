class Book:
    def __init__(self,title:str, author:str, content:str):
        self.title = title
        self.author = author
        self.content = content
    def __str__(self):
        return f'title: {self.title} \nauthor: {self.author} \ncontent: {self.content}'
        
class Books_list:
    
    def __init__(self):
        self.books_list = []
        
    def save_to_list(self, filename):
        if filename not in self.books_list:
            self.books_list.append(filename)
            # print(filename)
        else: print('this book all raddy egsist')
    def printed(self):
        for i in self.books_list:
            print(i)
        # print( self.books_list)
            
class Student:
    def __init__(self, name:str, grades:list[int]):
        self.name = name
        self.grades = grades
        
        
class Calculates_grades:
    def __init__(self):
        pass
    @staticmethod
    def clac_avg(grades):
        return sum(grades) / len(grades)
    
# student1 = Student('asaf',[100,90])
# calc = Calculates_grades()
# print(calc.clac_avg(student1.grades))
     
     
     
class Order:
    def __init__(self, items:list ,total_price:int):
        self.items = items
        self.total_price = total_price
    def __str__(self):
        return f
class Order_printer:
    def __init__(self):
        pass
    @staticmethod
    def print_invoice(ord:Order):
        # print(ord.items)
        
        print( f'catomer bay {ord.items} with cost of {ord.total_price}')
    
    
# ords = Order(['milk','ckockus'],42)
# printer = Order_printer()
# printer.print_invoice(ords)



