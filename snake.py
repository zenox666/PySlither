from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_part(i)

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.parts.append(new_part)

    def increase_parts(self):
        self.add_part(self.parts[-1].position())

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            x = self.parts[part_num - 1].xcor()
            y = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
