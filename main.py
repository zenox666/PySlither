from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"Left")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"Down")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"Right")
screen.onkey(snake.right,"d")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        snake.increase_parts()
        food.refresh()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>270 or snake.head.ycor()<-290:
        is_game_on = False
        score.game_over()

    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
