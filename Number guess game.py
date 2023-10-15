#making changes to see if they appear in git
from random import randint
import random
num = randint(1,100)
print(num)

print("Welcome to the game.")

level = input("Choose a level: 1 for Easy, 2 is Hard\n")#1 is easy, 2 is med, 3 is hard

Guesses = 10

#keep_playing = y

#while keep_playing == y:
if level == 1:
    Guesses = 10
    
elif level == 2:
    Guesses = 5
    
print(f"You have {Guesses} guesses.")

def user_guess(guess):
    guess = input("choose your first number: ")
    if guess > num:
        print("too high")
        return Guesses +- 1
    elif guess < num:
        print("too lowo")
        return Guesses +- 1
    elif guess == num:
        print("You win")
        return Guesses +- Guesses

