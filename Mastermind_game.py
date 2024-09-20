"""
Mastermind game in python
"""
import random


def generate_code():
    colors = ["red", "blue", "green", "yellow", "black", "pink", "orange", "purple"]
    code = random.choice(colors, k=4)  # generating a random code of 4 colors.
    return code


def evaluate_guess(code, guess):
    correct_color_and_position = 0
    correct_color_only = 0

    for i in range(len(code)):
        if guess[i] == code[i]:
            correct_color_and_position += 1
        elif guess[i] in code:
            correct_color_only += 1

    return correct_color_and_position, correct_color_only


def mastermind():
    code = generate_code()
    max_turns = 8
    turns_taken = 0
    game_over = False

    print("Welcome to the mastermind game!")
    print("guess the 4 color code. The colors are:red, blue, green, yellow, black, pink, orange, purple ")
    print("You have", max_turns, "turns to guess the code.")

    while not game_over and turns_taken < max_turns:
        guess = input("Enter your guess(coma-separated colors): ").lower().replace(" ", "").split(",")

        if len(guess) != 4:
            print("Invalid input. Please enter exactly 4 colors.")
            continue

        turns_taken += 1

        correct_color_and_position, correct_color_only = evaluate_guess(code, guess)

        print("result:")
        print("Correct color and position:", correct_color_and_position)
        print("Correct color only:", correct_color_only)

        if correct_color_and_position == 4:
            print("Congratulations!~ You've guessed the code.", code)
            break
        else:
            print("Incorrect guess, turns left", max_turns - turns_taken)

    if not game_over and turns_taken == max_turns:
        print("\nOut of turns. The code was:", code)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        mastermind()
    else:
        print("Thanks for playing this game. Have a great day")


mastermind()
