
i = 0
while i < 6:
  print(i)
  i += 1

for i in range(6):
    print(i)


#SECTION While loop

while True:
    print('Hello') # infinity loop

N = int(input("Enter Number : "))
riddle = 1
while N > 1:
    riddle *= N;
    N-=1




i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i > 6")

                                        #SECTION For Loops

#range(start:end:step)
#by Default range: start = 0, step = 1
#stop before end
for i in range(5): 
    pass

for i in range(1, 5, 2):
    print(i)

s = "PIXELS"
for c in s:
    if c == 'S':
        break
    print(c)

for x in range(6):
  print("*"*i )
else:
  print("Finally finished!")

    
#SECTION Recursion

#What Happen If Function Call It Self?
#When To Stop?
#! BASE CASE

def power(a, b) :
  if b == 0 : return 1
  elif a == 0 : return 0
  else :
    return a * power(a, b - 1)

#TODO:  fib(n)
def fib(N) :
  if(N == 0 or N == 1) : return N
  return fib(n - 1) + fib(n - 2)