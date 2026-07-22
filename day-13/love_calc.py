name1 = input ("your name :").lower()
name2 = input ("partner name:"). lower()
combined = name1 + name2
true_score = (
    combined.count("t")
    + combined.count("r")
    + combined . count("u")
    + combined . count("e")
)
love_score = (
    combined.count("l")
    + combined.count("o")
    + combined. count("v")
    + combined . count ("e")
)
score = int(str(true_score)+ str(love_score))
if score < 10 or score > 90:
    print(f"Your Score is {score}, you go together like coke and mentos!!")
elif 40<= score <=50:
    print(f"Your Score is {score}. You are alright together. ")
else:
    print(f"your score is{score}.")
