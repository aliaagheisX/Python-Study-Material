x = int(input("Enter X : "))

print(type(x))
print("==============================")
# SECTION String Manipulation
msg = "pixels student activity"

print(msg[0])   #p

                # SECTION 1 String Slicing

print(msg[2:5])     #xel
print(msg[:5])      #pixel
print(msg[2:])      #xels student activity
print(msg[-5:-2])   #ivi
print(msg[::-1])    #ytivitca tneduts slexip
print(msg[0:5:2])   #pxl
print("==============================")

                    # SECTION 2 methods
msg = "PIXELS's student activity"

print(msg.lower())              #pixels's student activity
print(msg.upper())              #PIXELS'S STUDENT ACTIVITY
print(msg.title())              #Pixels'S Student Activity
print(msg.replace("s", "H"))    #PIXELS'H Htudent activity
print(msg.split(" "))           #["PIXELS's", 'student', 'activity']
print(msg.count("s"))           #2
print(msg.find("s"))            #7
print(msg.isalnum())            #False
print(msg.isalpha())            #False
print("==============================")

                       # SECTION 3 Format
age = 18
money = 5

print("I'm " + age + "years old And I have" + money + "dollars")
#ERROR
print("I'm {} years old And I have {} dollars".format(age, money))
#I'm 18 years old And I have 5 dollars
print("I'm {1} years old And I have {0} dollars".format(age, money))
#I'm 5 years old And I have 18 dollars
print(f"I'm {age} years old And I have {money} dollars")
#I'm 18 years old And I have 5 dollars