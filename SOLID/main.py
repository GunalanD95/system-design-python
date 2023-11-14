# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         # Calculate and return the area of the circle
#         pass

# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def calculate_area(self):
#         # Calculate and return the area of the square
#         pass

# class AreaCalculator:
#     def calculate_total_area(self, shapes):
#         # Calculate and return the total area of all shapes in the list
#         pass
    
    
# AFTER 
# from abc import ABC , abstractmethod
# class Shape(ABC):
#     def calculate_area(self):
#         # Calculate and return the area of this shape
#         pass
    
# class Square(Shape):
#     def __init__(self,radius) -> None:
#         self.radius =  radius
        
#     def calculate_area(self) -> int:
#         # Calculate and return the area of the square
#         return 4 * self.radius

# class Circle(Shape):
#     def __init__(self,side_length) -> None:
#         self.side_length =  side_length
        
#     def calculate_area(self):
#         return 10 * self.side_length
    
    
# class AreaCalculator:
#     def calculate_total_area(self, shapes):
#         # Calculate and return the total area of all shapes in the list
#         total = 0
#         for shape in shapes:
#             total += shape.calculate_area()
#         return total


# sqr = Square(10)
# crl = Circle(4)
# calc = AreaCalculator()

# res = calc.calculate_total_area([sqr,crl])

# print("ans",res)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class RegularEmployee(Employee):
    pass

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.salary += bonus
        
class SalaryCalculator:
    @classmethod
    def calculate_salary(self,employees) -> int:
        total_salary = 0
        for emp in employees:
            total_salary += emp.salary
        return total_salary
    
    
mgr = Manager('Gojo',100,5) 
rg1 = RegularEmployee('Guna',50)
rg2 = RegularEmployee('Guha',60)

res = SalaryCalculator.calculate_salary([mgr,rg1,rg2])
print("res",res)

