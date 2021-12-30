from turtle import Turtle

class Bullet(Turtle):
    def __init__(self,shape, pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape(shape)
        self.setheading(90)
        self.setposition(x=pos[0], y=pos[1])
        self.showturtle()
        self.forward(100)