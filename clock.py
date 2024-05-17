import turtle
import time

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")
win.title("Timer")

# Create a turtle to draw the timer
timer = turtle.Turtle()
timer.speed(0)
timer.color("black")
timer.hideturtle()

# Function to draw the timer
def draw_timer(t):
    timer.clear()
    timer.penup()
    timer.goto(0, 0)
    timer.pendown()
    timer.write(f"Time: {t:02d} seconds", align="center", font=("Arial", 24, "normal"))

# Function to countdown
def countdown(t):
    while t:
        draw_timer(t)
        time.sleep(1)
        t -= 1
    timer.write("Time Up!!", align="center", font=("Arial", 24, "normal"))


# Get the time from the user
t = int(input("Enter the time in seconds: "))

# Start the countdown
countdown(t)

# Keep the window open
turtle.done()
