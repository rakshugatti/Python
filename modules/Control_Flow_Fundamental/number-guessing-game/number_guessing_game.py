import random


def play_number_guessing_game() -> None:
    """
    Runs the number guessing game using a while loop.
    """

    # Generate random number between 1 and 100
    target_number = random.randint(1, 100)

    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    # Game loop using while
    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < target_number:
                print("Too Low. Try again.\n")

            elif user_guess > target_number:
                print("Too High. Try again.\n")

            else:
                guessed_correctly = True
                print("\nCongratulations! You guessed the correct number.")
                print(f"Total Attempts: {attempts}")

        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


if __name__ == "__main__":
    play_number_guessing_game()