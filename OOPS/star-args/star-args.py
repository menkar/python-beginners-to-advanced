# def addition(a,b):
#     print("Addition is : ", a + b)

# addition(10,20)

# def addition(*args):
#     sum = 0
#     print("Arguments are : ", args) # Tuple of arguments

#     for i in args:
#         sum = sum + i

#     print("Addition is : ", sum)

# addition(10,20,30,40,50)

def addition(**kwargs):
    print("Keyword Arguments are : ", kwargs) # Dictionary of keyword arguments
    sum = 0
    
    for i in kwargs.values():
        sum = sum + i

    print("Addition is : ", sum)

addition(a=10, b=20, c=30, d=40, e=50)
