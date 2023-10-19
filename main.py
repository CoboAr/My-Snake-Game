from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# When "Escape" key is pressed game over function will be called, stopping the game
def game_over():
    global game_is_on
    game_is_on = False
    scoreboard.game_over ()

# Instances of Snake, Food, and ScoreBoard classes
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# Event handler functions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(screen.bye, "Escape")
screen.onkey (game_over, "Escape")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance (segment) <10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
