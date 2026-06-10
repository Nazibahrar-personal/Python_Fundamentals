#Title: Number guessing game in Python
#Link:https://www.geeksforgeeks.org/python/number-guessing-game-in-python/


import random

lower=int(input("enter a low value : "))
higher=int(input("enter a high value : "))
system_guess=random.randint(lower,higher)
user_guess_count=0

while True:
    user_guess=int(input('enter your guessed integer: '))
    user_guess_count+=1
    if user_guess>system_guess:
        print('Guess lower!')
    elif user_guess<system_guess:
        print('Guess higher!')
    else:
        print("Correct guess!!")
        break
print(f"It took you {user_guess_count} attempts to guess the correct integer")
        