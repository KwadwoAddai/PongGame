import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)


ball = Ball()
score = Score()
rt_paddle = Paddle(370)
lt_paddle = Paddle(-370)

screen.listen()
screen.onkey(rt_paddle.go_up, 'Up')
screen.onkey(rt_paddle.go_dn, 'Down')
screen.onkey(lt_paddle.go_up, 'w')
screen.onkey(lt_paddle.go_dn, 's')

game_on = True
while game_on:
    time.sleep(ball.move_pace)
    screen.update()
    ball.move()

#Detect top and bottom wal collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#Detect left and right paddle collision
    if ball.distance(rt_paddle) < 50 and ball.xcor() > 340 or ball.distance(lt_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
#Detect left and right wall collision
    if ball.xcor() > 380:
        ball.reset()
        score.l_points()

    if ball.xcor() < -380:
        ball.reset()
        score.r_points()

screen.exitonclick()