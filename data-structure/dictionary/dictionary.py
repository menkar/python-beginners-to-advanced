# mutable, Duplicates (Keys unique, values duplicates), Order - Insertion order and Heterogeneous

# Hash map = Dictionary in Python

# d = {1,2,3}

# print(type(d))

# dict = { 1: "Hello", 2: "Swapnil", "City": "Pune"}

# print(dict)


dict = {10: 100, 20: 200, 30: 300, 40: 400}

print(dict[20]) # 200

dict[10] = 1000

print(dict)

dict.update({50: 500}) # Updating

dict[60] = 6000 # Inserted/Creating

print(dict)

del dict[60] # Deleting

print(dict)

