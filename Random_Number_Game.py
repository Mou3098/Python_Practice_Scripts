import random


def guess_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    guess = None

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != random_number:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))

            # Give hints
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number correctly!")
        except ValueError:
            print("Please enter a valid number.")


# Start the game
guess_number()