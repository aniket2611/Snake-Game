from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
from border import Border
import time

# for better experience 500 <= SCREEN_WIDTH <= 1000 and 500 <= SCREEN_HEIGHT <= 700
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650

# screen setup
screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

# screen body setup
food = Food(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)
score = Score(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)
border = Border(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)
snake = Snake(border_half_height=border.border_half_height, border_half_width=border.border_half_width)

screen.update()

# snake movement handle
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

# game on
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.segments[0].distance(food) < 10:
        food.reallocate()
        score.update_score()
        snake.increase_length()

    # wall collision
    if snake.is_collided_with_wall():
        score.game_over()
        snake.reset()

    # tail collision
    for segment in snake.segments[1:]:
        if segment.distance(snake.segments[0]) < 5:
            score.game_over()
            snake.reset()

screen.exitonclick()
