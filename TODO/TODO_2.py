#1 - Write a Python program to print pattern

for i in range(1,6) :
    for i in range(1, i+1):
        print(i,end=' ')
    print()

#2 - print prime numbers in certain range
l = int(input("Enter Start of Range : "))
r = int(input("Enter End of Range : "))
for i in range(l, r+1) :
    isPrime = True
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0: 
            isPrime = False
            break
    if isPrime : print(i)
