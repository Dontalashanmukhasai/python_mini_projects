import turtle as turtle_module
START_POSITION = (0,-280)
class Challenger(turtle_module.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_start()
        self.setheading(90)        
        
          
        
    def go_up(self):
        self.forward(10)
        
    def goto_start(self):
        self.goto(START_POSITION)
        
    def goal(self):
        if self.ycor() > 280:
            return True
        else:
            False