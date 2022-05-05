user_info = ["PIXELS", "HELWAN", True ,19, 10j]

print(type(user_info))  #<class 'list'>

print(user_info)        #['PIXELS', 'HELWAN', True, 19, 10j]

print(len(user_info))   #5

#SECTION Access/Change same as string
                                    #*Access

print(user_info[2:5])     #[True, 19, 10j]
print(user_info[:5])      #['PIXELS', 'HELWAN', True, 19, 10j]
print(user_info[2:])      #[True, 19, 10j]
print(user_info[-5:-2])   #['PIXELS', 'HELWAN', True]
print(user_info[::-1])    #[10j, 19, True, 'HELWAN', 'PIXELS']
print(user_info[0:5:2])   #['PIXELS', True, 10j]

if "PIXELS" in user_info : print("HOLA")    

odd = [2, 4, 6, 8]
                            #*change
odd[0] = 1          #?change one item
odd[1:] = [3, 5, 7] #?change muliple items
print(odd)                      #[1, 3, 5, 7]

#SECTION Add List Elements
odd = [1, 3, 5, 7]
                            #*Add
#Repeat list
print(odd * 2)                  #[1, 3, 5, 7, 1, 3, 5, 7]

odd.append(9)            #?add one value at the end
odd.extend([11, 13, 15]) #?add multiple values at the end
print(odd)                      #[1, 3, 5, 7, 9, 11, 13, 15]

#insert(index, value)  
odd.insert(1, 2)      #?add one value at certain index
odd[2:2] = [4, 5, 6]  #?add one value at certain index
print(odd)                      #[1, 2, 4, 5, 6, 3, 5, 7, 9, 11, 13, 15]
                            #*Methods
num = [2, 1, 8, 6, 2]
for i in num: 
    print(i)
num.reverse();print(num)            #[2, 6, 8, 1, 2]
num.sort();print(num)               #[1, 2, 2, 6, 8]
print(num.count(2))                 #2
print(num.index(2))                 #2
print(num.index(10))                #!Error







#SECTION Delete/Methods List Elements
                            #*Delete
fruits = ["apple", "banana", "cherry", "mango", "guava", "kiwi", "peach"]
#? to remove by vale
fruits.remove("banana")
#? to remove by index
#pop remove from list and return the removed value
print(fruits.pop())     #peach
print(fruits.pop(2))    #mango

print(fruits)           #['apple', 'cherry', 'guava', 'kiwi']

#? Between del & clear
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)           #[]

fruits = ["apple", "banana", "cherry"]
del fruits
print(fruits)           #!Error
