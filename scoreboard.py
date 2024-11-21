from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(arg=f"score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial",20,"bold"))
