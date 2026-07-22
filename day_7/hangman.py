import random

word_list = ["apple", "banana", "orange", "mango", "grapes"]

chosen_word = random.choice(word_list)

display = []

for _ in chosen_word:
    display.append("_")

lives = 6
game_over = False

print("Welcome to Hangman!")

while not game_over:

    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed that letter.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")
        print("Lives left:", lives)

        if lives == 0:
            game_over = True
            print("You Lose!")
            print("The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("\nWord:", " ".join(display))
        print("Congratulations! You Win!")