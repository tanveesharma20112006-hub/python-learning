import turtle as t
import random
tim = t.Turtle()
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepskyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0,90,180,270]
tim.pensize(15)# this pen_size can change the size of pen. it can be wider and thinner.
tim.speed("fast")# this can change the speed 
for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))