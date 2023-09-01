import turtle as turtle_module
import random
from turtle import Screen


screen = Screen()
screen.setup(width = 500 , height = 400)
user = screen.textinput(title ='make your bet', prompt = 'which turtle willl win the race? Enter the color:')
turtle_colors = ["red","blue","orange","green","yellow","black"]
y_postion =[-100,-70,-40,-10,20,50]
turtles = []


for turtle_index in range(0,6):
    tim = turtle_module.Turtle(shape="turtle")
    tim.color(turtle_colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y = y_postion[turtle_index])
    turtles.append(tim)


if user:
    is_race_on = True
    
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user:
                print(f"you won! The {winning_color} turtle is the winner")
            else:
                print(f"ypu have lost! The {winning_color} is the winner")
    
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()