word = input("Enter a word")
rev_word =(word[::1])
if word == rev_word:
    print("This is an palindrome!")
else:
    print("Not an palindrome!")