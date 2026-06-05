class Animal:
    name = "lion" # Class attribute

    def __init__(self, age):
        self.age = age # instance attribute
    
    def show(self): # instance method
        print(f"Youe age is {self.age}")

    @classmethod
    def hello(cls): # Access to class
        print("How are you...")

    @staticmethod
    def static():
        print("How are you...static")

obj = Animal(21)
obj.show()

obj.hello()
obj.static()

