from turtle import Turtle
from bullet import Bullet
class Player(Turtle):
    def __init__(self, shape, bullet_shape):
        super().__init__()
        self.bullet_shape = bullet_shape
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape(shape)
        self.shapesize(1)
        self.setpos(x=0,y=-220)
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
        bullet = Bullet(shape=self.bullet_shape, pos=(self.xcor(), self.ycor()))