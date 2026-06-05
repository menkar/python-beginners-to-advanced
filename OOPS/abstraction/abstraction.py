# class Square:
#     def __init__(self, side):
#         self.side = side;

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius


from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side;

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("This is added into abstract class - perimeter")

    def area(self):
         print("This is added into abstract class - area")

obj = Circle(5)
# obj2 = Square(4)
obj.perimeter()
obj.area()
# obj2.perimeter()
# obj2.area() 

