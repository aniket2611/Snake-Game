from turtle import Turtle

X_COR_HEAD = 0
DISTANCE_TO_MOVE = 10


def create():
    segments = []
    x_cor = X_COR_HEAD
    for i in range(5):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("red", "white")
        new_turtle.goto(x_cor, 0)
        if i == 0:
            new_turtle.shape("circle")
            new_turtle.shapesize(stretch_wid=0.6, stretch_len=0.6)
        else:
            new_turtle.shape("square")
            new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x_cor -= 10
        segments.append(new_turtle)
    return segments


class Snake:

    def __init__(self, border_half_height, border_half_width):
        self.max_x_cor = border_half_width - 5
        self.max_y_cor = border_half_height - 5
        self.segments = create()

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments = create()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].setx(self.segments[i - 1].xcor())
            self.segments[i].sety(self.segments[i - 1].ycor())
        self.segments[0].forward(DISTANCE_TO_MOVE)

    def is_collided_with_wall(self):
        x_cor = self.segments[0].xcor()
        y_cor = self.segments[0].ycor()
        if x_cor > self.max_x_cor or x_cor < -self.max_x_cor or y_cor < -self.max_y_cor or y_cor > self.max_y_cor:
            return True

    def increase_length(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("red", "white")
        new_turtle.goto(self.segments[-1].position())
        new_turtle.shape("square")
        new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.segments.append(new_turtle)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

