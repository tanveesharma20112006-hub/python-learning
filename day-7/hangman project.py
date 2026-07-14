import random
word_list = ["camel", "horse", "rabbit","tiger"]
#create a variable called'lives' to keep track of the number of lives left.
#set 'lives' to equal 6.
lives = 6
#randomly choose a word from word_list and assign it to the variable called choosen_word. then print it.
chosen_word = random.choice(word_list)
#create a placeholder with the same number of blanks as the chosen_word
placeholder =""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters=[]
# ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
guess = input("guess a letter:").lower()
#create a "display" that puts the guess letter in the right positions and _ in non guessed letter
display =""
for letter in chosen_word:
    if letter == guess:
        display +=letter
        correct_letters.append(guess)
    elif letter in correct_letters :
        display += letter
    else:
        display +="_"

    print (display)

#if lives goes down to 0 then the game should stop and it should print "you lose."
if  guess not in chosen_word:
    lives -= 1
    if lives == 0:
        game_over =True
        print ("You lose.")

#if guess is not a letter in chosen_word, then reduce 'lives' by 1.
# if lives goes down to 0 then the game should stop and it should print "you lose"
if"_" not in display:
    game_over =True
    print("You Win.")


#check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is ,"Wrong", if it is not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

    print(stages[lives])


