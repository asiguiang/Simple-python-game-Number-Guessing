import random

print(
    "Hello! This is Isaeus Guiang, and this is a number guessing game. \n"
    "You have 5 chances to guess the number, or...\n"
    "you will die :)."
)

number_guess = random.randint(1, 100)  # Use randint to include 100 in the range

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input(f"Attempt {guess_counter}/{chances} - Your Guess :) -> "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        guess_counter -= 1  # Don't count invalid inputs as attempts
        continue

    if my_guess == number_guess:
        print(f"The number is {number_guess}, and you guessed it right in {guess_counter} attempt(s)!")
        break
    elif my_guess < number_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if guess_counter == chances:
        print(f"Oops, sorry, the number was {number_guess}. You are going to die :).")
