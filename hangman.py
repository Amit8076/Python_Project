"""
Hangman game using python
"""
import random


def hangman():
    words = ["python", "computer", "programming", "keyboard", "mouse", "algorithms", "system",
             "variable", "functions", "loop"]
    secret_word = random.choice(words)
    max_attempts = 5
    guessed_letters = []
    word_length = len(secret_word)
    incorrect_guesses = 0
    game_over = False

    print("Welcome to the hangman game.")
    print("i am thinking of a word that has", word_length, "letters")

    while not game_over:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("incorrect guesses:", incorrect_guesses, "/", "max attempts:", max_attempts)

        if "_" not in display_word:
            print("\nCongratulations! you've guessed the correct word", secret_word)
            break

        guess = input("Guess the letters of the whole word: ").lower()

        if guess == secret_word:
            print("Congratulations! you've guessed the correct word", secret_word)
            break
        elif len(guess) == 1 or guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter")
            elif guess in secret_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                guessed_letters.append(guess)
                incorrect_guesses += 1

        else:
            print("Invalid input. Please enter single letter or whole word")

        if incorrect_guesses == max_attempts:
            print("\nOut of attempts. the word was", secret_word)
            break

    play_again = input("Do you want play again? (yes/no): ").lower()
    if play_again == "yes" or play_again != "no":
        hangman()
    else:
        print("Thanks for playing this game")


hangman()
