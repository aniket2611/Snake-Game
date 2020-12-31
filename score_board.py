import turtle

turtle.colormode(255)


class Score(turtle.Turtle):

    def __init__(self, s_width, s_height):
        super().__init__()
        self.screen_half_width = s_width/2
        self.screen_half_height = s_height/2
        self.hideturtle()
        self.color((197, 198, 118), "white")
        self.penup()
        self.goto(x=0, y=self.screen_half_height - 50)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Your score : {self.score}", move=False, align="center", font=("courier", 15, "bold"))

    def game_over(self):
        self.clear()
        self.write(arg=f"Game Over!! Your final score is {self.score}", move=False, align="center", font=("courier", 15, "bold"))
