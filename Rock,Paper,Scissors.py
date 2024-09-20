import random


def get_user_choice():
    while True:
        user_choice = input("Choose: Rock, Paper or Scissor: ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissor"]:
            return user_choice
        else:
            print("Invalid choice")


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissor"])


def Determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie"
    elif (
            (user_choice == "Rock" and computer_choice == "Scissor") or
            (user_choice == "Scissor" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        print("Computer Wins")


def play_game():
    print("Lets play Rock, Paper and Scissor game:")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"computer chose: {computer_choice}")

        result = Determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again (yes/no): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    play_game()
