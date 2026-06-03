# a = 256

# while a > 0:
#     print(a % 10)
#     a = a // 10  

# num = int(input("Enter a number : "))

# while num > 0:
#     print( num % 10)
#     num = num // 10

# Reverse value 

# num = int(input("Enter a number : "))
# rev = 0
# originalNum = num

# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10

# print(f"Original Number is = {originalNum}\nReverse Number is = {rev}")

# Palindrom

num = int(input("Enter a number : "))
orgNum = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if orgNum == rev:
    print("Number is a Palindorm")
else:
    print("Number is not a Palindorm")
