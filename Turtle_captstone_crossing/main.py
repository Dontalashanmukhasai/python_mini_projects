import turtle as turtle_module
from turtle import Screen
import time
from challenger import Challenger
from cars import Cars
from scoreboard import Scoreboard


screen = Screen()
turtle = turtle_module.Turtle()
cars = Cars()
challenger = Challenger()
scoreboard = Scoreboard()

screen.setup(width = 800 , height= 600)
screen.bgcolor("white")
screen.title("Turtle Capstone Crossing")
screen.tracer(0)
screen.listen()
screen.onkey(challenger.go_up,"e")



is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(challenger) < 20:
            is_game_on = False
            scoreboard.game_over()
    
    
    if challenger.goal():
        challenger.goto_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()