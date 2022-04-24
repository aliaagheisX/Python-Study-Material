# SECTION :Operators
x = 5
y = 2
                # Arithmetic Operators & Assignment Operators

x + y;   x+= y  #7
x - y;   x-= y  #3
x * y;   x*= y  #10
x ** y;  x**=y  #25 
x / y;   x/= y  #2.5
x //y;   x//= y #2
x % y;   x%= y  #1 =(1 + 4) / 2 = 1/2+ 2

                # Comparison Operators
x = 5

x == 5  #True
x != 2  #True
x > 2   #True
x >= 5  #True
x < 5   #False
x <= 5  #True
                # Logical Operators
x = 5              
x > 2 and x < 3 #False
x > 2 or x < 3  #True
not x == 4      #True

                # Identity Operators
x = ['P', 'I']
y = ['P', 'I']
z = x
x is z          #True
x is y          #False
x is not y      #True
x == y          #Tue

                # Membership Operators
x = ['P', 'I']
'P' in x        #True
'P' not in x    #False