d1 = {10:100, 20:200}
d2 = {30:300, 40:400, 50: 500}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# listNums = [1,2,3,4,5,6,7,8,9,92,5,4,4,5,3,2,1,2,3,5,4,3,4,3,1,1,1,2,3,4,5,5]

# charCount = {}

# for i in listNums:
#     if i in charCount.keys():
#         charCount[i] = charCount[i] + 1
#     else:
#         charCount[i] = 1

# print("charCount :", charCount)


d1 = {10: 100, 20: 200, 30: 300}
d2 = {30: 1000, 40: 400, 50: 500}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)