import turtle as turtle_module
FONT = ("Arial",14,"normal")




class Scoreboard(turtle_module.Turtle):
    def __init__(self):
        super().__init__()  
        self.level = 1   
        self.hideturtle()
        self.penup()
        self.goto(-380,280)
        self.write(f"Level: {self.level}",align = "left",font=FONT)
        
        
        
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",align = "left",font=FONT)
        
        
    def game_over(self):
        self.goto(-100,0)
        self.write("GAME OVER",align = "left",font=FONT)
        