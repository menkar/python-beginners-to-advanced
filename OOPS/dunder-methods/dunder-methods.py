# class Animal:
#     def __init__(self, name):
#         self.name = name;

#     def __str__(self):
#         return f"Animal name is : {self.name}"

# obj = Animal("Lion")
# print(obj) # By default it will print the object reference but by using __str__ method


# class Animal:
#     def __init__(self, name, age):
#         self.name = name;
#         self.age = age; 

#     def __str__(self):
#         return f"Animal name is : {self.name}"
    
#     def __add__(self, other):
#         return f"You sum of ages is : {self.age + other.age}"

# obj = Animal("Lion", 19)
# obj2 = Animal("Tiger", 20)
# print(obj + obj2)

# class Animal:
#     def __init__(self, name, age):
#         self.name = name;
#         self.age = age; 

#     def __str__(self):
#         return f"Animal name is : {self.name}"
    
#     def __add__(self, other):
#         return f"You sum of ages is : {self.age + other.age}"

# obj = Animal("Lion", 19)
# obj2 = Animal("Tiger", 20)
# obj3 = Animal("Dolphin", 15)
# print(obj + obj2 + obj3) # Not working, throwing error

class Animal:
    def __init__(self, name, age):
        self.name = name;
        self.age = age; 

    def __str__(self):
        return f"Animal name is : {self.name}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age

        return f"You sum of ages is : {self.age + sum}"

obj = Animal("Lion", 19)
obj2 = Animal("Tiger", 20)
obj3 = Animal("Dolphin", 15)
print(obj + (obj2, obj3))  # Working with tuple




