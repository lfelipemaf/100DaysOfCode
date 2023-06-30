from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_down, "Down")
    screen.onkey(snake.turn_right, "Right")
    screen.listen()


#day 21
#TODO step 4: Detect collision with food

#TODO step 5: Create a scoreboard

#TODO step 6: Detect collision with wall

#TODO step 7: Detect collision with tail

screen.exitonclick()