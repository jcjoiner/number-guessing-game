""" 
    - Import random number and assign it to a variable
    - Have user guess a number (Validate)
        - No letters
        - No negatives
    - Provide feedback if number is high or low
    - Only allow x amount of guesses and keep track of them
    - Ask to play again after a win or a loss
"""
import random
import time
import os

# game loop
def game_loop():
    os.system("clear")
    rand_int = random.randint(0, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:

        attempts += 1

        print(f"Attempt: {attempts} of {max_attempts}")
       
        while True:
            try:
                guess = int(input("Enter a guess: "))
                if guess < 0:
                   print("Numbers cannot be less than 0. Try again.")
                else:
                    break
            except ValueError:
                print("Integers only. Try again.")

        print("========================================")
       
        if guess == rand_int:
            print(f"You win! {rand_int} was the number!")
            break
        elif attempts >= max_attempts:
            print(f"Too many attempts! {rand_int} was the number.")
            break
        elif guess < rand_int:
            print(f"Higher than {guess}! Guess again!")
        else:
            print(f"Lower than {guess}! Guess again!")

def main():

    while True:
        game_loop()

        choice = input("Would you like to play again? (Y/N)\n> ").upper()

        if choice != "Y":
            print("Thanks for playing!")
            time.sleep(1)
            os.system("clear")
            quit()

main()
