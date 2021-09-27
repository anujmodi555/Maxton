sample_list = [1,1,1,1,3,2,7,6,4,5,6,7,8,8,7]

# Remove Duplicate elements from list
print(set(sample_list))

list_b = []
def remove_duplicate(list_a):
    for item in list_a:
        if item in list_b:
            pass
        else:
            list_b.append(item)
    print(list_b)

remove_duplicate(sorted(sample_list))

# print the  frequency of largest element
frequency = print(sample_list.count(max(sample_list)))

# Python program to find the
# frequency of largest element


L = [1, 2, 8, 5, 8, 7, 8]
d = {}

# find the largest element
largest = max(L)

for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d[largest])

# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the second last element
print("Second largest element is:", list1[-2])

