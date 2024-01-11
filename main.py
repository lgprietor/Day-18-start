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
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    tim.color(red,green,blue)

    for i in range(number_of_sides):
        tim.forward(length_of_side)
        tim.right(angle)


screen = Screen()
screen.colormode(255)

for i in range(3,11):
    polygon(i)

screen.exitonclick()

