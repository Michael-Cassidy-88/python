
# Guess the Random Number Function

import random # imports random library 

def play_game():
    number = random.randint(1, 10) 
    while True:
        guess = int(input("Guess the Number: "))
        if guess > number:
            print("The number you have guessed is too high. Please try again")
        elif guess < number:
            print("The number you have guessed is too low. Please try again.")
        elif guess == number:
            print("You guessed it!")
            break
play_game() 