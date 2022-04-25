#? 1 - Write a Python program to calculate a dog's age in dog's years :
#Note: For the first two years, a dog year is equal to 10.5 human years. 
#After that, each dog year equals 4 human years.

years =  float(input("Enter Dog Year : "))

if years <= 2 :
    years *= 10.5
else :
    years = (2 * 10.5) + (years - 2) * 4

print(f"Dog Year in Human Years = {years}")


#2 - Write a Python program to check a triangle is equilateral, isosceles or scalene.

x = int(input("Enter Side 1 :"))
y = int(input("Enter Side 2 :"))
z = int(input("Enter Side 3 :"))

#x,y,z = [int(x) for x in input().split()]

if x == y and x == z : print("Equilateral")
elif x == y or x == z or y == z : print("Isosceles")
else : print("Scalene")