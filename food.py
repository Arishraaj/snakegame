from turtle import Turtle
import random

SIZE=[0.5,1,1.5]
COLOR=["red","blue","yellow","brown"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        #self.shapesize(stretch_len=0.5,stretch_wid=random.choice(SIZE))
        self.refresh()
        self.food_create()

    def food_create(self):
        rand_size=random.choice(SIZE)
        rand_color=random.choice(COLOR)
        self.color(rand_color)
        self.shapesize(stretch_len=rand_size,stretch_wid=rand_size)

    def refresh(self):
        self.food_create()
        x_new=random.randint(-280,280)
        y_new=random.randint(-280,280)
        self.goto(x_new,y_new)
        