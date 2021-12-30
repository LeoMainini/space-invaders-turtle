from turtle import Turtle
from bullet import Bullet
import time

class Player(Turtle):
    def __init__(self, shape, bullet_shape):
        self.type = "player"
        self.score = 0
        self.lives = 3
        self.last_shot = 0
        super().__init__()
        self.bullet_shape = bullet_shape
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape(shape)
        self.shapesize(1)
        self.setpos(x=0, y=-220)
        self.showturtle()

    def move_left(self):
        self.setheading(180)
        if self.xcor() > -325:
            self.forward(10)

    def move_right(self):
        self.setheading(0)
        if self.xcor() < 325:
            self.forward(10)

    def shoot(self):
        if time.time() - self.last_shot > 0.66:
            self.last_shot = time.time()
            Bullet(shape=self.bullet_shape, pos=(
                self.xcor(), self.ycor()+10), heading=90)
