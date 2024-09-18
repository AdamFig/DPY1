import os
os.system('clear')

# Problem Set 1

fruits = ["apple", "banana", "mango", "kiwi", "strawberry"]
print(fruits[0], fruits[4])
fruits.append("grape")
print(fruits)
fruits[1] = "blueberry"
print(fruits)
fruits.pop(5)
print(fruits)

# Problem Set 2 (Easy-Medium)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integers[2], integers[5])
sliced_integers = integers[3:7]
print(sliced_integers)
integers.append(11)
print(integers)
integers.pop(0)
print(integers)

# Problem Set 3 (Medium)

# mixed_list = ["apple", 1, 0.5, True]
# print(mixed_list)
# mixed_list.append(2)
# print(mixed_list)
# mixed_list.insert(0,"banana")
# print(mixed_list)


# for i in mixed_list:
#     if type(i) == bool:
#         print(i)
#         index_of_bool = mixed_list.index(i)
#         mixed_list.pop(index_of_bool)
# print(mixed_list)

#Troubleshoot above code


# Problem Set 4 (Medium-Hard)

integer_list = [1, 7, 4, 5, 3, 2, 4, 6, 8, 7, 9, 10]

sorted_integer_list = sorted(integer_list)
print(sorted_integer_list)

even_integer_list = []
for i in integer_list:
    if i % 2 == 0:
        even_integer_list.append(i)
print(even_integer_list)

sum_of_integer_list = sum(integer_list)
print(sum_of_integer_list)

no_duplicate_integer_list = []
for i in sorted_integer_list:
    if i not in no_duplicate_integer_list:
        no_duplicate_integer_list.append(i)
print(no_duplicate_integer_list)



# Problem Set 5 (Hard)


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists[2][1])

list_of_lists[0][0:3] = "a" "b" "c" # Is there a way to make VSCode happy and not show an error underline?
print(list_of_lists)

flattened_list = []
for sublist in list_of_lists:
    for i in sublist:
        if type(i) == int:
            flattened_list.append(i)
print(flattened_list)


# Messing around with nested lists below

list_of_lists_of_lists = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]], [[13,14,15], [16,17,18]], [[19,20,21], [22,23,24]]]
print(list_of_lists_of_lists[0][1][2]) # - first list index 0 = [1,2,3], second list index 1 = [4,5,6], third list index 2 = 6

# Messing around with nested lists above
