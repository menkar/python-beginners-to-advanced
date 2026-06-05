#a = int(input("Enter a number : "))

#print(10/a)


# print("Start")
# print(10/0) # Zero Division Error
# print("End") # Not executed

# try: 
#     print(10/a)
# #except ZeroDivisionError: # only for zero division error
# except Exception as err: # Any type of exception / error
#     print(f"Sorry, there is an error as {err}")

# else:
#     print("Good there is no exception")

# finally:
#     print("I will run no matter what")
    
# print("I have done the division")

# If exception / error wants to custom raise

age = int(input("Enter a age : "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
        print(f"Error occurred as {err}")

print("The club will start soon")
