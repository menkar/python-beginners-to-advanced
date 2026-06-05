# addition = lambda a, b : a + b
# print("Addition is : ", addition(12,21))

# isEvenorOdd = lambda a: "even" if a % 2 == 0 else "odd"

# print("Is Even or Odd : ", isEvenorOdd(21))


# map operator

arr = [1,2,3,4,5,6]

# square = map(lambda x : x * 2, arr)

# print(list(square))

# def double(a):
#     return a * 2

# square = map(double, arr)

# print(list(square))

# filter operator

# def even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False


# res = filter(even, arr)

# print("Filter Result : ", list(res))


res = filter(lambda x : True if x % 2 == 0 else "odd",arr)
print(list(res))