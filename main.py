from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")

tim.color("DarkBlue")

# for i in range(0, 4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def polygon(number_of_sides):
    length_of_side = 100
    angle = 360 / number_of_sides

    for i in range(number_of_sides):
        tim.forward(length_of_side)
        tim.right(angle)
        # tim.pencolor(random.choice())

for i in range(3,11):
    polygon(i)


screen = Screen()

screen.exitonclick()

