# class Animal:
#     def show(self):
#         print("This is an animal.")

# obj = Animal()
# obj.show()

# class Animal:
#     @property
#     def show(self):
#         print("This is an animal.")

# obj = Animal()
# obj.show # Access method  as property without parentheses

# Creating a decorator function

# def decorate(func):
#     def wrapper():
#         print("This is before the function call.")
#         func()
#         print("This is after the function call.")
#     return wrapper

# @decorate
# def hello():
#     print("Hello, Welcome to Python Decorators!")

# hello()

def decorate(func):
    def wrapper(a,b):
        print("Addition of a and b is : ", a + b)
        func(a,b)
        print("This is after the function call.")
    return wrapper

@decorate
def hello(a,b):
    print(f"Your total is : {a + b}")

hello(21,11)