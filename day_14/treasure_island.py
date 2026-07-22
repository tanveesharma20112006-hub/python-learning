print("Welcome to the Treasure Island")
print("Find the treasure.\n")
way = input ("Left or Right?"). lower()
if way == "left":
    lake= input("Swim or wait?") . lower()
    if lake == "wait":
        door = input("Red, Blue or yellow ?") . lower()

        if door == "yellow":
            print("CONGRATULATIONS!, you found the treasure . You win")
        else:
            print("You lose. GAME OVER !!!")
    else:
        print("You Drowned ! , GAME OVER!!!")
else:
    print(" you fell into the hole. GAME OVER!!!")
