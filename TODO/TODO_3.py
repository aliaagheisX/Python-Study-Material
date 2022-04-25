#1 - Write a program to check the number is even or odd by using function.
def Even_or_Odd(x):
    if(x % 2 == 0): print("even")
    else : print("odd")

#2- Write a program to calculate the factorial of any number by using function.
def fact(n):
    if(n < 0) : return -1;
    if(n == 0 or n == 1) : return 1
    else : return n * fact(n - 1)

#3 - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(s):
    stuart_score = 0
    kevin_score = 0

    for i in range(len(s)) :
        if s[i] in "AEIOU" : kevin_score += len(s) - i
        else : stuart_score += len(s) - i
    
    if stuart_score > kevin_score : print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score : print(f"Kevin {kevin_score}")
    else : print("Draw")
