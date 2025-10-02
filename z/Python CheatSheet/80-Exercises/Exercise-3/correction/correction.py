import random

NUMBER_MIN = 1
NUMBER_MAX = 10
MAX_ATTEMPTS = 3


def play_game():
    secret_number = random.randint(NUMBER_MIN, NUMBER_MAX)
    attempts_left = MAX_ATTEMPTS

    print("\nWelcome to the Magic Number Game!")
    print(f"Guess the magic number between {NUMBER_MIN} and {NUMBER_MAX}.")
    print(f"You have {attempts_left} lives.\n")

    while attempts_left > 0:
        try:
            guessUser = int(input("Enter your guess: "))

            if guessUser < NUMBER_MIN or guessUser > NUMBER_MAX:
                print(f"Please enter a number between {NUMBER_MIN} and {NUMBER_MAX}.")
                continue

            if guessUser == secret_number:
                print("Congratulations! You found the magic number!")
                return 

            else:
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Wrong! You have {attempts_left} lives left.")
                else:
                    print(f"Sorry, you lost! The magic number was {secret_number}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def play_again():
    while True:
        response = input("\nDo you want to play again? (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please answer with 'y' or 'n'.")


while True:
    play_game()
    if not play_again():
        print("\nThanks for playing! Goodbye 👋")
        break
