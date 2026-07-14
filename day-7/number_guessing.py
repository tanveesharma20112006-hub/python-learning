import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1

    elif guess < answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {answer}.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

turns = set_difficulty()

guess = 0

while guess != answer:

    print(f"\nYou have {turns} attempts remaining.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)

    if guess != answer:

        if turns == 0:
            print("You've run out of guesses. You lose.")
            break

        else:
            print("Guess again.")