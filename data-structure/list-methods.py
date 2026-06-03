# print(dir(list))

# help(list)

l = [1,3,4,5,5,6,4,7,4,5,3,5,6,7,5]

# l.append(6)
# l.insert(1, 2)
l.extend([20,25,27])
l.remove(5)
popped_item = l.pop(3)

print("popped_item", popped_item)

index = l.index(3)
print("index", index)

count_5 = l.count(5)
print("count_5", count_5)

l.sort()
l.reverse()

new_l = l.copy()
print("new_l", new_l)

l.clear()

print(l)