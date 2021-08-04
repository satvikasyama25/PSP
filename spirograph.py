import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
    for colours in ["blue", "red", "silver", "green", "yellow", "white", "gold"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
