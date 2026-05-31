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

num = int(input("Enter a number :"))
even = 0
odd = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i


print(f"Sum of Even number is {even} and Sum of odd number is {odd}")