from turtle import Turtle
from random import randint
import time


class Food(Turtle):
    def __init__(self, s_width, s_height):
        super().__init__()
        self.screen_half_width = s_width / 2
        self.screen_half_height = s_height / 2
        self.max_x_cor = self.screen_half_width - 90
        self.max_y_cor = self.screen_half_height - 90
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow", "yellow")
        self.penup()
        self.reallocate()

    def reallocate(self):
        self.goto(x=randint(-self.max_x_cor, self.max_x_cor), y=randint(-self.max_y_cor, self.max_y_cor))
        # self.goto(x=-260, y=260)
