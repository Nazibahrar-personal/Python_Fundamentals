

import random

name=input("Enter your name : ")
print(f"Good luck {name}")


words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


choice=random.choice(words)

attempt=len(choice)
print(f"I'm thinking about a {attempt} letter word. So you've {attempt} attempts to guess the word. Note that a right guess won't cost you an attempt!")


guesses="_"*len(choice)

while attempt>0:
  guess=input("guess a character : ")
  if guess in choice:
    for i in range (len(choice)):
      if choice[i]==guess:
        guesses=guesses[:i]+guess+guesses[i+1:]
      else:
        continue
    print(guesses)
  
  else:
    
    attempt-=1
    print(f"Wrong guess . Attempt remains: {attempt}")
  if guesses==choice :
    print("You've successfully guessed the word!")
    break
  else:
    continue

if guesses!=choice  and attempt==0:
  print("sorry you've failed to guess the word")
elif guesses==choice and attempt==0:
  print("You've successfully guessed the word!")
        
            










    