
from turtle import Turtle, xcor, ycor


class Paddle(Turtle):
    def __init__(self, pos=(xcor, ycor)):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color('white')
        self.goto(pos)

    def up(self):
        self.fd(70)
        if self.ycor() > 240:
            self.goto(self.xcor(), 245)

    def down(self):
        self.bk(70)
        if self.ycor() < -240:
            self.goto(self.xcor(), -235)
