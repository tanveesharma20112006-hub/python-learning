word = input("Enter a word")
rev_word =(word[::2])
print(rev_word)
if word == rev_word:
    print("This is an palindrome!")
else:
    print("Not an palindrome!")