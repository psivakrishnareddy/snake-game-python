
import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('green')
        self.refresh_food()

    def refresh_food(self):
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        self.goto(x,y)    
