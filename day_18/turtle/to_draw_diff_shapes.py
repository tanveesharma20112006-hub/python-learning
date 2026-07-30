import turtle as t #we didnt have to write turtle all the time t can also call the module
tim = t.Turtle()
num_sides = 5
for  _ in range(num_sides):
    angle = 360/(num_sides)
    tim.forward(100)
    tim.right(angle)
    #here we had drawn a pentagon .