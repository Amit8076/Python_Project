# Exercise 22/12/2023
"""
Kaum Banega Karorepati Game
"""
import random


def display_questions(questions, options):
    print(questions)
    for i, options in enumerate(options, start=1):
        print(f"{i}. {options}")
    user_answer = int(input("Your choice (enter the number): "))
    return user_answer


def kbc_game():
    questions = [
        {
            "questions": "What is the Capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": 3
        },
        {
            "questions": "Which Planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "correct_answer": 1
        },
        {
            "questions": "who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct_answer": 2
        },
        {
            "questions": "What is the Capital of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
            "correct_answer": 3
        },
        {
            "questions": "Who painted the MonaLisa?",
            "options": ["Vincent van gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "correct_answer": 3
        },
        {
            "questions": "What is the largest ocean in the world?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_answer": 4
        },
        {
            "questions": "What is the currency of japan?",
            "options": ["Yen", "Euro", "Dollar", "Rupee"],
            "correct_answer": 1

        },
        {
            "questions": "Who is the of harry potter book series?",
            "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Dan Brown"],
            "correct_answer": 2
        },
        # Add more questions as needed
    ]

    # random.shuffle(questions)  # shuffle the questions for more dynamic experience
    score = 0

    for q in questions:
        user_choice = display_questions(q["questions"], q["options"])
        if user_choice == q["correct_answer"]:
            print("correct\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['options'][q['correct_answer'] - 1]}\n")
            break  # end the game if user gives a wrong answer

    prize_level = [0, 1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000]
    final_amount = prize_level[score]

    print(f"Congratulations! You won ${final_amount}!")


if __name__ == "__main__":
    print("Welcome to the KBC (Kaun Banega Karorepati)!")
    kbc_game()
