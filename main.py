from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake_game=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake_game.up,"Up") 
screen.onkey(snake_game.down,"Down") 
screen.onkey(snake_game.left,"Left") 
screen.onkey(snake_game.right,"Right") 

game_still_on=True
while game_still_on:
    screen.update()
    time.sleep(0.1)

    snake_game.move()
    
    #food
    if snake_game.head.distance(food) < 15 :
        food.refresh()
        score.increase()
        snake_game.increase()

    #collision with wall
    if snake_game.head.xcor() > 295 or snake_game.head.xcor() < -295 or snake_game.head.ycor() > 295 or snake_game.head.ycor() < -295 :
        game_still_on=False
        score.end_game()

    #collision With body
    for seg in snake_game.segment[1::1]:
        # if seg == snake_game.head:
        #     pass
        if snake_game.head.distance(seg) < 10:
            score.end_game()
            game_still_on=False
    


screen.exitonclick()