# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

# create a nested list
original_list = [1, 2, [3, 4], 5]

# shallow copy the list
shallow_copy = copy.copy(original_list)

# deep copy the list
deep_copy = copy.deepcopy(original_list)

# modify the nested list in the shallow copy
shallow_copy[2][0] = 6

# modify the nested list in the deep copy
deep_copy[2][0] = 7

# print the original list and the copies
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
