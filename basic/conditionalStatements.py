# IF else statement

# a = 21

# if a > 21:
#     print("A is geater than 21")

# else:
#     print("A is less than 21")


# money = int(input("Enter money: "))

# if money == 10:
#     print("Buy Icecream")
# elif money == 20:
#     print("Buy Cone")
# else:
#     print("Buy Candy")


# num1 = int(input("Enter number One "))
# num2 = int(input("Enter Number Two "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both numbers are same")

# gen = input("Please provide your gender as (M or F) F = ")

# if gen == "M" or gen == 'm':
#     print("Good Morning SIR")
# elif gen == "F" or gen == "f":
#     print("Good Morning MAM")
# else:
#     print("Unidentified Gender")

# num = int(input("Enter a number : "))

# if num%2 == 0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# year = int(input("Enter a year : "))

# if year % 100 == 0 and year % 400 == 0:
#     print("It is a leap year")
# elif year % 100 != 0 and year % 4 == 0:
#     print("It is a leap year")
# else:
#     print("It is a normal year")

temp = int(input("Enter a Temperature : "))

if temp <= 0:
    print("Freezing Cold")
    
elif temp > 0 and temp < 10:
    print("Very Cold")
elif temp >= 10 and temp < 20:
    print("Cold")
elif temp >= 20 and temp < 30:
    print("Pleasant")
elif temp >= 30 and temp < 40:
    print("Hot")
else:
    print("Very Hot")
    