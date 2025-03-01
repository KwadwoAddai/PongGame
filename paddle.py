from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(xpos, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_dn(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
