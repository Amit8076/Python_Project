
import random


def number_guessing_game():
    print("Welcome to the number guessing game. ")
    print("Think a number between 1 to 100. ")

    # Generate a random number between 1 to 100.
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your numbers: "))
        attempts += 1

        if guess < secret_number:
            print("Too low, Try a higher number.")
        elif guess > secret_number:
            print("Too high, Try a lower number.")
        else:
            print("Congratulations! you guessed the number in", attempts, "attempts!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "no":
            break


number_guessing_game()
