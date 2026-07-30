import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (239, 243, 245), (236, 234, 240), (225, 231, 227),
    (224, 154, 102), (47, 95, 145), (155, 76, 51),
    (224, 219, 76), (131, 34, 20), (222, 77, 106),
    (144, 177, 208), (132, 167, 142), (46, 122, 86),
    (13, 98, 71), (173, 153, 40), (168, 19, 32),
    (144, 30, 45), (224, 176, 168), (1, 76, 105),
    (106, 67, 85), (30, 58, 111), (17, 86, 91),
    (182, 97, 109), (107, 127, 157), (176, 192, 209)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()