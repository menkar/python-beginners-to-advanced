# mutable, unordered, no duplicate elements and semi heterogeneous data structure
# set is implemented using hash table   
# s = {1,2,3,4,5,6,7,8,9,10}

# print(s)
# print(type(s))

# s1 = {}
# print(type(s1)) # It is a dictionary, not a set

# Hashing is used to store the elements in a set, so the order of elements is not guaranteed
# a = hash("Hello")
# print(a)

# c = hash((1,2,3,4,5))
# print(c)

data = {1,2,3,4,5,6,7,8,9,10}
print(data)

data1 = {1,2,7,8,9,11,3,4,5,6}
print(data1) 

a = {1,2,3,4,5,"Hello",8, 6,5,7,10} # depend on hash value of elements, the order may change and duplicate elements are not allowed
print(a) # No duplicate elements, so 5 is only printed once}