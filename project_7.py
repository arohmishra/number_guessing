#number guessing

import random

# Introduction
print("Let me think of a number between 1 and 50...")
num = random.randint(1, 50)

# Difficulty selection
diff = input("Choose level of difficulty.. type 'easy' or 'hard': ").lower()

if diff == 'easy':
    attempts = 8
    print("You have 8 attempts to guess the number!")
elif diff == 'hard':
    attempts = 5
    print("You have 5 attempts to guess the number!")
else:
    print("Invalid difficulty level. Please restart the game and type 'easy' or 'hard'.")
    exit()  # Exit the program if an invalid difficulty is entered

# Game logic
while attempts > 0:
    guess_num = int(input("Make a guess: "))
    if guess_num == num:
       print("Congratulations, you guessed the number!")
       break
    elif guess_num < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1

    if attempts == 0:
        print(f"You ran out of attempts! The correct number was {num}.")
        break
    else:
        print(f"You have {attempts} attempts remaining.")
