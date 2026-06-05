arr = [1,3,5,7,10,1,-2,-4,2,-11]

# print("Positive numbers are: ")

# for i in arr:
#     if i >= 0:
#         print(i)

# print("\n Negative numbers are: ")

# for i in arr:
#     if i < 0:
#         print(i)

#mean
arr = [1,2,3,4,5,21,22,2,21,2,51,23]
# sum = 0

# for i in arr:
#     sum = sum + i

# print(sum/len(arr))

# Find largest number and index too

# largest = arr[0]
# index = 0

# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#         index = i

# print(f"Greatest Number is {largest} and inde is {index}")

# Find second largest number

# arr = [21, 25,32, 11, 12, 23, 43, 21, 14, 24, 40]

# largest = arr[0]
# sec_largest = arr[0]

# for i in arr:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(f"Largest number is {largest} and Second largest number is {sec_largest}")

# Check if list is sorted or not

arr = [11,12,13,14,18,16,17]

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")
