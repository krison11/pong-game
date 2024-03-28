
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('PONG GAME')
screen.listen()
screen.tracer(0)  # turn off the animations


p_right = Paddle((350, 0))
p_left = Paddle((-350, 0))
ball = Ball()
board = ScoreBoard()


screen.onkey(key='Up', fun=p_right.up)
screen.onkey(key='Down', fun=p_right.down)
screen.onkey(key='w', fun=p_left.up)
screen.onkey(key='s', fun=p_left.down)


game_is_on = True

while game_is_on:
    screen.update()
    ball.fd(1)

    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(p_right) < 50 and ball.xcor() > 330 or ball.distance(p_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        board.increase_score_left()
        ball.new_ball()
    elif ball.xcor() < -400:
        board.increase_score_right()
        ball.new_ball()
    if board.p_l == 10 or board.p_r == 10:
        game_is_on = False

board.goto(0, 0)
board.write('Game over!', align='center', font=('Arial', 40, 'bold'))
screen.exitonclick()
