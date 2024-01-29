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

rand_int = random.randint(0, 100)
attempts = 0
max_attempts = 5
print(rand_int)

# game loop
while attempts < max_attempts:
    attempts += 1

    print(f"Attempt: {attempts} of {max_attempts}")
    guess = int(input("Enter a guess: "))

    if attempts >= max_attempts:
        print(f"Too many attempts! {rand_int} was the number.")
    elif guess < rand_int:
        print(f"Higher than {guess}! Guess again!")
    else:
        print(f"Lower than {guess}! Guess again!")

