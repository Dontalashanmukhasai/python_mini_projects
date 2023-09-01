import turtle as turtle_module
import random
from turtle import Screen

screen = Screen()
tim = turtle_module.Turtle()
def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def turn_left():
    new_heading = tim.heading() +10
    tim.left(new_heading)
    
def turn_right():
    new_heading = tim.heading() -10
    tim.right(new_heading)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(move_forward ,"f")
screen.onkey(move_backward ,"b")
screen.onkey(turn_left ,"l")
screen.onkey(turn_right ,"r")
screen.onkey(clear_screen,"c")


screen.exitonclick()

