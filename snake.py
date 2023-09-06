from turtle import Turtle

POSITION=[(0,0),(-20,0),(-40,0)]
MOVEDISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self) :
        self.segment=[]
        self.create()
        self.head=self.segment[0]

    def create(self):
        for pos in POSITION:
            self.new_segment(pos)

    def new_segment(self,pos):
        snake=Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segment.append(snake)

    def increase(self):
        self.new_segment(self.segment[-1].position())
        

    def move(self):
        for seg in range (len(self.segment)-1,0,-1):
            x_new=self.segment[seg-1].xcor()
            y_new=self.segment[seg-1].ycor()
            self.segment[seg].goto(x_new,y_new)
        self.segment[0].forward(MOVEDISTANCE)

    def up(self):
        # self.move()
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # self.move()
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # self.move()
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        # self.move()
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

