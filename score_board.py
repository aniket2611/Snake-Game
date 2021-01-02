import turtle

turtle.colormode(255)


class Score(turtle.Turtle):

    def __init__(self, s_width, s_height):
        super().__init__()
        self.screen_half_width = s_width / 2
        self.screen_half_height = s_height / 2
        self.hideturtle()
        self.color((197, 198, 118), "white")
        self.penup()
        self.goto(x=0, y=self.screen_half_height - 50)
        self.score = -1
        file = open("high_score.txt")
        self.high_score = int(file.read())
        file.close()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score.txt", mode="w")
            file.write(f"{self.high_score}")
            file.close()
        self.write(arg=f"Your score : {self.score}      High score : {self.high_score}", move=False, align="center",
                   font=("courier", 15, "bold"))

    def game_over(self):
        self.clear()
        self.score = 0
        file = open("high_score.txt", mode="w")
        file.write(f"{self.high_score}")
        file.close()
        self.write(arg=f"Your score : {self.score}      High score : {self.high_score}", move=False, align="center",
                   font=("courier", 15, "bold"))
