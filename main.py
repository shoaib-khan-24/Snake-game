from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun= snake.move_up, key="Up")
screen.onkey(fun= snake.move_down, key="Down")
screen.onkey(fun= snake.move_right, key="Right")
screen.onkey(fun= snake.move_left, key="Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_score()
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        snake.snake_dead()
        screen.update()
        game_on = False

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False
            snake.snake_dead()
            screen.update()

screen.exitonclick()