a = {1,2,3,4,5}
a.add(6)
print("Add = ", a)

a.remove(3)
print("Remove = ", a)

a.discard(4)
print("Discard = ", a)

a.discard(10) # No error, because discard does not raise an error if the element is not found
print("Discard 10 = ", a)

popped = a.pop() # Removes and returns an arbitrary element from the set
print("Pop = ", a)
print("Popped element = ", popped)

a.clear() # Removes all elements from the set
print("Clear = ", a)