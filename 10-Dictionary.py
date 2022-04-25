user_info = {
    "Name" : "Pixels",
    "Location" : "Helwan",
    5: 19
}

print(type(user_info))   #<class 'dict'>
print(user_info)         #{'Name': 'Pixels', 'Location': 'Helwan', 5: 19}
print(len(user_info))    #3

#SECTION Access/Change same as string

                                    #*Access

user_info = { "Name" : "Pixels", "Location" : "Helwan", "Age": 19}

print(user_info["Name"])    #Pixels
#print(user_info["sdf"])     #!ERROR
print(user_info.get("sdf")) #None

#? check for keys only                                  
if "Name" in user_info : print("HOLA")

                            #*Change & Add items items 
                            
user_info = { "Name" : "Pixels", "Location" : "Helwan"}

user_info["Location"] = "University"
print(user_info)            #{'Name': 'Pixels', 'Location': 'University'}
user_info["Age"] = 10
print(user_info)            #{'Name': 'Pixels', 'Location': 'University', 'Age': 10}

                            #*Delete
user_info = { "Name" : "Pixels", "Location" : "Helwan", "Age" : 8}

print(user_info.pop("Location"))    #Helwan
print(user_info.popitem())          #('Age', 8)
print(user_info)                    #{'Name': 'Pixels'}

user_info.clear()
del user_info


                            #*Methods
squares = {x : x*x for x in range(5)}
print(squares)  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

for i in squares:
    print(f"{i} ^ 2 = {squares[i]}")

x = squares.keys();print(x)         #dict_keys([0, 1, 2, 3, 4])
x = squares.values();print(x)       #dict_values([0, 1, 4, 9, 16])
x = squares.items();print(x)        #dict_items([(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)])

# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)


print(marks)                        #{'English': 0, 'Math': 0, 'Science': 0}

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))   #['English', 'Math', 'Science']