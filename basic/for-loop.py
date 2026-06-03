# num = int(input("Enter a number : "))

# for i in range(num):
#     print("Hello World!")

# num = int(input("Enter a number : "))
# for i in range(1, num + 1):
#     print(i)

# num = int(input("Enter a number :"))
# for i in range(num, 0, -1 ):
#     print(i)


# num = int(input("Which table you want :"))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

# num = int(input("Enter a number for sum :"))

# sum = 0

# for i in range(1, num + 1):
#     sum = sum + i


# print(f" Sum is {sum}")


# num = int(input("Enter a number for factorial :"))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i


# print(f"Factorial is {fact}")

# num = int(input("Enter a number :"))
# even = 0
# odd = 0

# for i in range(1, num + 1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i


# print(f"Sum of Even number is {even} and Sum of odd number is {odd}")

# Factors

# num = int(input("Enter a Number : "))

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

# Perfect Number 

# num = int(input("Enter a number : "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum = sum + i

# if sum == num:
#     print("Your number is perfect")
# else:
#     print("Your number is not perfect")

# Prime or not

# num = int(input("Enter a number : "))
# count = 0

# for i in range(1, num+1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print("Your number is prime")
# else:
#     print("Your number is not prime")

# reverse string

# str = "Swapnil Menkar"

# print(str[::-1])

# str = "Swapnil Menkar"
# reverseStr = ''
# strLength = len(str)
# for i in range(strLength - 1, -1, -1):
#     reverseStr += str[i]

# print(f"Reverse String is {reverseStr}")

# palindrom

# str = input("Enter a string : ")
# reverseStr = ''

# for i in range(len(str)-1, -1, -1):
#     reverseStr += str[i]

# if reverseStr == str:
#     print("String is Palindrom")
# else:
#     print("String is not a Palindrom")

# Count char, digit and splchars

mixedStr = input("Enter mixed string : ")
digit = 0
char = 0
splChar = 0

for i in mixedStr:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        splChar += 1

print(f"Digit = {digit}\nCharacters = {char}\nSpecial Characters = {splChar}") 
