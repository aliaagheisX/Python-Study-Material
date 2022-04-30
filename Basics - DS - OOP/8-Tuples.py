user_info = ("PIXELS", "HELWAN", True ,19, 10j)
test = ("PI")
test1 = ("PI",)
print(type(user_info))   #<class 'tuple'>
print(type(test))        #<class 'str'>
print(type(test1))       #<class 'tuple'>
print(user_info)         #('PIXELS', 'HELWAN', True, 19, 10j)
print(len(user_info))    #5

#SECTION Access/Change same as string
                                    #*Access

print(user_info[2:5])     #(True, 19, 10j)
print(user_info[:5])      #('PIXELS', 'HELWAN', True, 19, 10j)
print(user_info[2:])      #(True, 19, 10j)
print(user_info[-5:-2])   #('PIXELS', 'HELWAN', True)
print(user_info[::-1])    #(10j, 19, True, 'HELWAN', 'PIXELS')
print(user_info[0:5:2])   #('PIXELS', True, 10j)

if "PIXELS" in user_info : print("HOLA")
evens = [2, 4, 6]
num1, num2, num3 = evens
print (num1)
print (num2)
print (num3)

                            #*Can't Change items But
nested_tuple = (1 , 2, [1, 2, 3], (1, 2, 3))
#?inside of it can change
nested_tuple[2][0] = 0
#? Can be reassigned
nested_tuple = (1 , 3)


#SECTION Add/Delete/Methods for  tuble
odd = (1, 3, 5, 7)
                            #*Add
#Repeat list
print(odd * 2)                  #(1, 3, 5, 7, 1, 3, 5, 7)

evens = (2, 4, 5)
odd += evens    #? can only add tuble at the end
print(odd)                      #(1, 3, 5, 7, 2, 4, 5)

                            #*Methods
num = (2, 1, 8, 6, 2)
for i in num: 
    print(i)
    
print(num.count(2))                 #2
print(num.index(2))                 #2
print(num.index(10))                #!Error

                            #*Delete
del num #?can only Delete List