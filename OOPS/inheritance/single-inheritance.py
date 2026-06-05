# class FactoryMumbai: # Parent / Super Class
#     a = "I am an attribute, mentioned inside in factory"

#     def hello(self):
#         print("I am a method, mentioned in factory")

# class FactoryPune(FactoryMumbai): # Child Class / Sub Class
#     pass

# obj = FactoryMumbai()

# print(obj.a)
# obj.hello()

# obj1 = FactoryPune()

# print(obj1.a)
# obj1.hello()


# class Animal():
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"Name is {self.name}")

# class Human(Animal):
#     pass

# animal1 = Animal("Lion")
# person1 = Human("Swapnil")

# animal1.show()
# person1.show()

class Animal():
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Your name is {self.name} and age is {self.age}")

animal1 = Animal("Lion")
person1 = Human("Swapnil", 21)

animal1.show()
person1.show()





