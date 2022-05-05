#1 -  Convert two lists into a dictionary
key_list = ["Physics", "Math", "Electronics"]
value_list = [1, 5, 0]

my_dict = dict(zip(key_list, value_list))

print(my_dict)
#2 - Rename key of a dictionary
my_dict = {0:0, 1:1, 2:4, 3:9, 4:16}
old_key = 2
new_key = "two"
my_dict[new_key] = my_dict.pop(old_key)

print(my_dict)

#3 -  Get the key of a minimum value from the following dictionary
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
min_value = min(sample_dict.values())
for key in sample_dict : 
    if sample_dict[key] == min_value : print(key)

#4 - Return a set of elements present in Set A or B, but not both

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = (A | B) - (A & B)
print(C)

#5 - Update set1 by adding items from set2, except common items
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A.update(B)
print(A)