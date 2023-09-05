import turtle as turtle_module
import random
colors = ["blue","green","orange","red","yellow"]
START_DISTANCE = 5

class Cars(turtle_module.Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = START_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = turtle_module.Turtle("square")
            new_car.shapesize(stretch_wid = 1,stretch_len = 2)
            new_car.penup()
            new_car.color(random.choice(colors))
            y = random.randint(-250,250)
            new_car.goto(300,y)
            self.all_cars.append(new_car)
        
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
            
    
    def level_up(self):
        self.speed += 10