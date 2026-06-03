# # print("Hello, I am inbuilt functions")

# def hello():
#     print("Hello, I am user defined function")

# hello()

# def sum(a, b):  # positional arguments
#     return a + b

# sumOfTwoNum = sum(10, 20) 
# print(f"Sum of two number is {sumOfTwoNum}")


# # Ordered and Keyword Arguments
# def person(name, age):
#     print(f"Name of person is {name} and age is {age}")

# person("Swapnil", 22) #Ordered Arguments
# person(age = 22, name = "Swapnil") #Keyword Arguments

# # Default Arguments

# def defaultSum(a, b = 10):
#     return a + b

# sumOfTwo = defaultSum(10) # Here we are passing only one argument and other is taking default value which is 10
# print(f"Sum of two number is {sumOfTwo}")


def isPalindrom(str):
    rev = ""
    for i in range(len(str) -1, -1, -1):
        rev = rev + str[i]


    if rev == str:
        print("Provided string is Palindrom")
    else:
        print("Provided string is not a Palindrom")


isPalindrom("madam")
isPalindrom("Madam")