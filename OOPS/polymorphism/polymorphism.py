class Animal:
    def show(self):
        print("Hello, this is animal show")

class Human(Animal):
    def show(self):
        print("Hello, this is human show")

obj = Human();

obj.show()

# In python not having method overloading
# Example:
# class Animal:
#     def show(self):
#         print("Hello, this is animal show")

#     def show(self, material):
#         print("Method overloading")

