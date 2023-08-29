import turtle as t
import random

tim = t.Turtle()
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
def draw_shape(no_of_sides):
    angle = 360/no_of_sides
    for i in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)


for diff_side in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(diff_side)