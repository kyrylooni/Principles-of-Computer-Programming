# Hit The Taget Game 

# Note: In order to stop an execution of the program, please click once on the “Python Turtle Graphics” window. 

import turtle
from turtle import Screen 
import random


# Named constants
SCREEN_WIDTH = 600       # Screen width 
SCREEN_HEIGHT = 600      # Screen height 
TARGET_LLEFT_X = 100     # Target's lower-left X
TARGET_LLEFT_Y = 250     # Target's lower-left Y
TARGET_WIDTH = 25        # Width of the target
FORCE_FACTOR = 30        # Arbitrary force factor
PROJECTILE_SPEED = 1     # Projectile's animation speed
NORTH = 90               # Angle of north dirrection 
SOUTH = 270              # Angle of south dirrection
EAST = 0                 # Angle of east dirrection
WEST = 180               # Angle of west dirrection

# Setup the window. 
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# screen object in order to establish color mode of the window, so that the program 
# will randomly choose an intager in rnge from 0 to 255 (max RGB value)
screen = Screen()
screen.colormode(255)

# Draw the target .
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center thee turtle. 
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()

turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))

# Calculate the distance. 
distance = force * FORCE_FACTOR

# Set the heading. 
turtle.setheading(angle)

#random color every time turtle starts
R = random.randint(0, 255) # RED  
G = random.randint(0, 255) # GREEN 
B = random.randint(0, 255) # BLUE

# Launch the projectile. 
turtle.pendown()
turtle.pencolor(R, G, B)  # every execution -- new color 
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        turtle.pencolor("black")
        turtle.write("Hit!")
        turtle.bgcolor("green") # when turtle hits background is green 
        print("Target hit!")
else:
    turtle.pencolor("black")
    turtle.write("Missed!")
    turtle.bgcolor("red") # when turtle  misses the target, background is red 
    print("You missed the target")

# Note: In order to stop an execution of the program, please click once on the “Python Turtle Graphics” window. 
print("Click once on the turtle window to stop the execution")
screen.exitonclick()
print("Thank you!")
