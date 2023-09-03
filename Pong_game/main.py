from turtle import Screen
import turtle as turtle_module
from paddles import paddle
from ball import Ball
import time
from scoreboard import score

turtle = turtle_module.Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800 , height = 600)
screen.title("Pong")
screen.tracer(0)

right_paddle = paddle((350,0))
left_paddle = paddle((-350,0))
ball = Ball()
scoreboard = score()

screen.listen()
screen.onkey(right_paddle.go_up,"o")
screen.onkey(right_paddle.go_down,"k")
screen.onkey(left_paddle.go_up,"e")
screen.onkey(left_paddle.go_down,"d")




is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(right_paddle) < 50 and ball.xcor() >  320 :
        ball.bounce_x()
        
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        
    if ball.xcor() < -380:
        ball.reset_position()   
        scoreboard.right_point()
    
screen.exitonclick()