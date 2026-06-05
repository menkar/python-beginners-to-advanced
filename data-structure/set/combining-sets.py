a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}

c = a.union(b)
d = a | b

# print(c)
# print(d)

e = a.intersection(b)
f = a & b

# print(e)
# print(f)

g = a.difference(b)
h = b.difference(a)
i = a - b
j = b - a

# print(g)
# print(h)
# print(i)
# print(j)

k = a.symmetric_difference(b)
l = b.symmetric_difference(a)
m = a ^ b
n = b ^ a

# print(k)
# print(l)
# print(m)
# print(n)

# Compound Operator
b -= a
print(b)

