from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7 , stretch_len=0.7)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()
    def refresh_food(self):
        random_x_cor = random.randint(-280, 280)
        random_y_cor = random.randint(-280, 280)
        self.goto(random_x_cor, random_y_cor)



