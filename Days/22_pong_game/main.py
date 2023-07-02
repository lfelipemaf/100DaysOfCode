from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.listen()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)


#create another paddle
#create the ball and make it move
#detecet collision with wall and bounce
#detect collition with paddle
#detect when paddle misses
#keep score
screen.exitonclick()