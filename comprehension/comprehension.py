# a = 21
# print("even") if a % 2 == 0 else print("odd")


# l = []

# for i in range(1, 21): 
#     if i % 2 == 0:
#         l.append(i)

# print("Even numbers are : ", l)

# comprehension

# l = [i for i in range(1,21) if i % 2 == 0]
# print("Comprehension : ", l)

l = { i: i ** 2 for i in range(1,10)}

print("Dict : ", l)