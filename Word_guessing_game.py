"""
word guessing game in python
"""

import random


def word_guessing_game():
    # list of words for the game:
    words = ["python", "computer", "programming", "keyboard", "mouse", "algorithms", "system",
             "variable", "function", "loop"]

    # Select a random word from the list
    word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Number of attempts are allowed

    print("Welcome to the Word Guessing Game.")
    print("Guess a letter of word, You've only 6 attempts.")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
            print(display_word)

        guess = input("Guess the letter of word: ").lower()

        if len(guess) > 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter:")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1
            print("You've left: ", attempts)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! you have guessed the correct word: ", word)
            break

    if attempts == 0:
        print("you've run out of attempts, The word is ", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again != "no":
        word_guessing_game()
    else:
        print("Thank you for playing this game.")


word_guessing_game()
