# a = range(1,21,1)

# for i in a:
#     print(i)

# for i in range(1,21,1):
#     print(i)

# for i in range(21):
#     print(i)

# for i in range(15, 51, 2):
#     print(i)

# for i in range(15, 1, -1):
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)

# Lets print a table of 5

# for i in range(5, 51, 5):
#     print(i)


# num = int(input("Enter number to generate table : "))

# for i in range(num,(num * 10) + 10, num):
#     print(i)


# Loops on strings

str = "Swapnil Menkar"

# for i in range(len(str)):
#     print(str[i])

# for i in str:
#     print(i)

# Break and Continue

# for i in range(1, 21):
#     if i == 11:
#         break
#     else :
#         print(i)

# for i in range(1, 21):
#     if i == 11:
#         continue
#     else :
#         print(i)

for i in range(1, 21):
    if i == 22:
        print("Break Statement is executed")
        break
    print(i)

else:
    print("Break statement is not executed")