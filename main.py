import turtle

from clock import Clock

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Timer")
screen.tracer(0)

clock = Clock() 

screen.exitonclick()
