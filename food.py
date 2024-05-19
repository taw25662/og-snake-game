from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape("circle")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 260)
        self.goto(new_x, new_y)




