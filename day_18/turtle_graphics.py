#importing Turtle
from turtle import Turtle, Screen
#Turtle :- Creates the Turtle(pen)
# Screen :- Creates the drawing window

#creating a Turtle
from turtle import Turtle
tim = Turtle()
# here tim is Turtle object

#Creating a screen
from turtle import Screen
screen = Screen()
#here exitonclick keep the window open until you click on it .

#basic movement
#move forward
tim.forward(100)
#move backward
tim.backward(100)
#turn left
tim.left(90)
#turn right
tim.right(90)

#Drawing a Square
for _ in range(4):
    tim. forward(100)
    tim.right(90)

#pen control
#lift the pen (move without drawing)
tim.penup()
#put the pen down
tim.pendown()

#changing speed
tim.speed("fastest")
#options:(slowest, slow, normal, fast, fastest)

#changing color
tim.color("green")

#changing shape
tim.shape("turtle")
#options: "arrow", "circle", "square", "triangle","classic"

#Drawing a Dot
tim.dot(20)
#draw a dot with a diametre of 20 pixel

#heading(direction)
tim.setheading(90)
#directions: 0(east/ right), 90(north/ up) , 180 (west/ left), 270 (south/ down)

#moving to a position 
tim.goto(100,50)
#moves the turtle to the coordinate(100,50)

#screen methods
screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("white")
screen.title("My Turtle program")

#keeping the window open
screen.exitonclick()
