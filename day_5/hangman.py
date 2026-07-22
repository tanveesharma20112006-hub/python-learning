import random

words = ["apple", "mango", "tiger", "table"]

word = random.choice(words)

guess_word = "_" * len(word)

lives = 6

while lives > 0 and "_" in guess_word:
    print("Word:", guess_word)

    letter = input("Guess a letter: ")

    new_word = ""

    for ch in word:
        if ch == letter:
            new_word += letter
        else:
            index = word.index(ch)
            new_word += guess_word[index]

    if new_word == guess_word:
        lives -= 1
        print("Wrong Guess!")
        print("Lives Left:", lives)

    guess_word = new_word

if "_" not in guess_word:
    print("You Win!")
else:
    print("You Lose!")
    print("Word was:", word)