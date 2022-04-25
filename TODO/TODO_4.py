#1 -  Create a list by picking
# an odd-index items from the first list and even index items from the second
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
even = [my_list[i] for i in range(0,len(my_list), 2)]
odd = [my_list[i] for i in range(1,len(my_list), 2)]

print(my_list)
print(even)
print(odd)

#2 - Write a program to 
# remove the item present at index 4 and add it to the 2nd position and at the end of the list.
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
my_list.insert(2, my_list.pop(4))

print(my_list)


#3 - Slice list into 3 equal Lists and reverse each 
my_list = [1, 2, 3, 4, 5, 6]
step = int(len(my_list) / 3)

my_list = [my_list[i:i+step] for i in range(0, len(my_list) - step + 1, step)]
for i in my_list : i.reverse()
print(my_list)