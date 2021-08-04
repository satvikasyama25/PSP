'''
import turtle
turtle.begin_fill()
turtle.color('blue')
turtle.circle(70)
turtle.end_fill()
'''
import turtle

Riya = turtle.Turtle()
Riya.fillcolor("yellow")
Riya.begin_fill()
Riya.pendown()

for i in range(3):
    Riya.forward(300)
    Riya.left(120)
Riya.end_fill()


