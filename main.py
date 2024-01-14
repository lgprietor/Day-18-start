from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")

# tim.color("DarkBlue")


# for i in range(0, 4):
#     tim.forward(100)
#     tim.right(90)
#
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3 - Polygon Drawing from 3 to 10 sides

# def polygon(number_of_sides):
#     length_of_side = 100
#     angle = 360 / number_of_sides
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     tim.color(red,green,blue)
#
#     for i in range(number_of_sides):
#         tim.forward(length_of_side)
#         tim.right(angle)

# screen = Screen()
# screen.colormode(255)
#
# for i in range(3, 11):
#     polygon(i)
#
# screen.exitonclick()

# Challenge 4 - Random walk

# pace_length = 25
# tim.pensize(5)
# tim.forward(50)

# movements = ["forward", "backward", "left", "right"]

# def random_walk():
#
#     # Defining turtle color:
#     tim.speed(0)
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#
#     tim.color(red,green,blue)
#
#     random_movement = random.choice(movements)
#
#     if random_movement == "left":
#         tim.left(90)
#         random_movement = movements[random.randint(0, 1)]
#
#     elif random_movement == "right":
#         tim.right(90)
#         random_movement = movements[random.randint(0, 1)]
#
#     if random_movement == "forward":
#         tim.forward(pace_length)
#     elif random_movement == "backward":
#         tim.backward(pace_length)
#
# screen = Screen()
# screen.colormode(255)
#
# for i in range (0, 201):
#     random_walk()
#
# screen.exitonclick()


# Challenge 5 - Drawing a spirograph with circles:

def spirograph_circle(pace_length):
    tim.pensize(1)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    tim.color(red,green,blue)

    tim.circle(pace_length)

def polygon_spirograph(number_of_sides):
    length = 200
    angle = 360 / number_of_sides
    # red = random.randint(0, 255)
    # green = random.randint(0, 255)
    # blue = random.randint(0, 255)
    # tim.color(red, green, blue)

    for i in range(0, number_of_sides):
        tim.forward(length)
        tim.right(angle)


# polygon_spirograph(3)

screen = Screen()
screen.colormode(255)


tim.speed("fastest")

# # Spirograph with circles full

# step_size = 15
#
# for i in range(0, 361, step_size):
#
#     tim.left(step_size)
#     spirograph_circle(100)
#     print(tim.heading())


## Spirograph with step size:
# Spirograph with polygons:

step_size = 1


for i in range (0, 361, step_size):
    polygon_spirograph(6)
    tim.left(step_size)

screen.exitonclick()

