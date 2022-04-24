def func(s):
    print(f"Hello, {s}")

func("Aliaa")
func("PIXELS")
func("WORLD")
func("Python")
func("Function")
func(5)
func(823)


#SECTION SYNTAX
#   def function_name(arguments): 
#       CODE 
#       return

#SECTION Arguments

#it could be multiple
def triangle_area(b, h) :
    return 0.5 * b * h
print(triangle_area(4, 4))

#you can set a default value to parameter
def print_name(fname,lname = "Pixels") :
    print(f"Hello {fname}, {lname}")

print_name("Aliaa")             #Hello Aliaa, Pixels
print_name("Aliaa", "Gheis")    #Hello Aliaa, Gheis

#If you do not know how many arguments that will be passed into your function
def sum_all(*numbers) :
    sum = 0
    for i in numbers:
        sum += i
    return sum
print(sum_all(5, 4, 5, 2, 0, 1, -4))
