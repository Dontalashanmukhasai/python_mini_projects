import turtle as t
import random

tim = t.Turtle()
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
directions = [0,90,180,270]
tim.pensize(6)
tim.speed("fastest")
for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(100)
    tim.setheading(random.choice(directions))
    
    
#Random walk with RGB colors:
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
    
directions = [0,90,180,270]
tim.pensize(6)
tim.speed("fastest")
for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))