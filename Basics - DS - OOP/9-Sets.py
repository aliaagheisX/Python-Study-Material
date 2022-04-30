user_info = {"PIXELS", "HELWAN", True ,19, 19}

print(type(user_info))   #<class 'set'>
print(user_info)         #{True, 19, 'PIXELS', 'HELWAN'}
print(len(user_info))    #4

#SECTION Access/Change same as string

                                    #*Access
if "PIXELS" in user_info : print("HOLA")
                            #*Can't Change items 
                            #*Add
my_set = {1, 3, 5, 7}
#Repeat list

my_set.add(2)   #? to add item

#? to add multiple items
my_set.update((3, "Pixels", "name"))
my_set.update({3, "Pixels", "name"})
my_set.update([3, "Pixels", "name"])
print(my_set)   #{1, 2, 3, 'Pixels', 5, 7, 'name'}

                            #*Delete
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana") #error if not fount
fruits.discard("banana")#NO error if not fount
fruits.pop()#remove randomly
fruits.clear()


                            #*Methods
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)            #{1, 2, 3, 4, 5, 6, 7, 8}
A.union(B)
B.union(A)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)            #{4, 5}
A.intersection(B)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)            #{1, 2, 3}
A.difference(B) # A - B
B.difference(A) # B - A