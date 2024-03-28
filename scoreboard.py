
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        self.p_l = 0
        self.p_r = 0
        self.line = Turtle()
        self.line.hideturtle()
        self.line.setheading(90)
        self.line.color('#D3D3D3')
        self.line.pensize(2)
        self.line.penup()
        self.line.goto(0, -280)
        self.board_line()
        super().__init__()
        self.hideturtle()
        self.color('#D3D3D3')
        self.penup()
        self.goto(0, 250)
        self.display_score()

    def display_score(self):
        self.write(f'{self.p_l}             {self.p_r}',
                   align='center', font=('Arial', 40, 'bold'))

    def increase_score_left(self):
        self.clear()
        self.p_l += 1
        self.display_score()

    def increase_score_right(self):
        self.clear()
        self.p_r += 1
        self.display_score()

    def board_line(self):
        for _ in range(31):
            self.line.pendown()
            self.line.fd(25)
            self.line.penup()
            self.line.fd(25)
