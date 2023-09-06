from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score : {self.score }',align=ALIGNMENT,font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.update()

    def end_game(self):
        self.goto(0,0)
        self.write(f'Game Over',align=ALIGNMENT,font=FONT)
        