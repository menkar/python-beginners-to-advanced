dict = {10: 100, 20: 200, 30: 300, 40:400, 50:500}

# for i in dict:
#     print(i)

# for i in dict:
#     print(dict[i])

# for i in dict.values():
#     print(i)


# # Keys
# for i in dict.keys():
#     print(i)

# help(dict)


# num = {10: 100, 20: 200}
# print(num)

# num.clear()

# print("After Clear", num)


# Shallow and Deep Copy

# a = [10,12,3,4,6]

# b = a # Deep Copy

# b[0] = 1000
# print(a)

# a = [10,12,3,4,6]

# b = a.copy() # Shallow Copy

# b[0] = 1000
# print(a)
# print("Copied")
# print(b)

num = {10: 100, 20: 200}

# num1 = num.copy() # Shallow Copy
# print(num1)

d = num.get(20)

#print(d)
print(num.items())
