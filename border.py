from turtle import Turtle
from math import sqrt


class Border(Turtle):

    def __init__(self, s_width, s_height):
        super().__init__()
        self.screen_half_width = s_width / 2
        self.screen_half_height = s_height / 2
        self.hideturtle()
        self.color("red", "red")
        self.penup()
        self.border_half_height = (self.screen_half_height - 80)
        self.border_half_width = (self.screen_half_width - 80)
        self.goto(x=-self.border_half_width, y=-self.border_half_height)
        self.pendown()

        self.forward(2*self.border_half_width)
        self.left(90)
        self.forward(2*self.border_half_height)
        self.left(90)
        self.forward(2*self.border_half_width)
        self.left(90)
        self.forward(2 * self.border_half_height)

        # # self.pensize(5)
        # self.radius_square = self.border_half_height ** 2 + self.border_half_width ** 2
        # self.circle(sqrt(self.radius_square), 360, 4)
        # print(sqrt(self.radius_square))
