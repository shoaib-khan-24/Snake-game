from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]
    def create_snake(self):
        for curr_pos in STARTING_POSITIONS:
            self.add_segment(curr_pos)
    def add_segment(self , position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for curr_seg in range(len(self.segments)-1, 0, -1):
            new_x_cor = self.segments[curr_seg-1].xcor()
            new_y_cor = self.segments[curr_seg-1].ycor()
            self.segments[curr_seg].goto(new_x_cor,new_y_cor)
        self.head.forward(MOVE_DISTANCE)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def snake_dead(self):
        for segment in self.segments:
            segment.color("grey")

