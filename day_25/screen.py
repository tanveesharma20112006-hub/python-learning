import turtle as t
from turtle import Screen
shapes = input(" arrow , square , triangle, circle, classic , turtle \n")

#shape = screen.textinput("arrow" , "square" , "triangle" , "circle" , "classic" , "turtle" )
screen = Screen()
if shapes in ["arrow","square","triangle","circle","classic","turtle"]:
    t.shape(shapes)
else:
    print("invalid input")
screen.exitonclick()   