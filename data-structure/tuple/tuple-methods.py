tupleData = (1, 2, 3, 4, 5,21,3,4,5,2,3,5,1)

index = tupleData.index(3)
print("index = ", index)

count_5 = tupleData.count(5)
print("count_5 = ", count_5)

a,b,c,d = (1,2,3,4)  # Tuple unpacking
print(a)
print(b)
print(c)
print(d)

a = (1)

print(type(a)) # It is not a tuple, it is an integer

a = (1,)

print(type(a)) # Now it is a tuple, because of the comma after 1.