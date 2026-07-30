from turtle import Turtle , Screen
from random import randint
screen = Screen()
screen.setup(width = 500 , height = 400)
user_bet = screen.textinput(title = "make your bet", 
                            prompt = "which Turtle will win the race?"
                            "enter a color:"
                            )
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

#create turtles
for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions [turtle_index])
    all_turtles.append(new_turtle)

#start race if user entered a bet
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:

#check if turtle  reach finish line
     if turtle.xcor() >230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bet .lower():
           print(f"You've won! The {winning_color} turtle is winner!")
        else:
           print(f"You've lost! The {winning_color} turtle is winner!")

# move turtle by a random distance
    random_distance = randint(0,10)
    turtle.forward(random_distance)

screen.exitonclick()  