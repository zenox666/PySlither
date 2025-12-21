from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("")
screen.tracer(0)

snake = Snake()

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



screen.exitonclick()
