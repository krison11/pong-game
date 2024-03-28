
import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.penup()
        self.color('white')
        # self.color('#D8F000')
        self.new_ball()

    def new_ball(self):
        if self.xcor() > 400:
            self.setheading(170)
            self.goto(0, random.randint(-100, 100))
        elif self.xcor() < -400:
            self.setheading(10)
            self.goto(0, random.randint(-100, 100))
        else:
            self.setheading(random.choice([10, 170]))
            self.goto(0, random.randint(-100, 100))

    def bounce_y(self):
        self.setheading(360-self.heading())

    def bounce_x(self):
        x = random.randint(170, 190)
        self.setheading(x-self.heading())
        self.fd(20)
