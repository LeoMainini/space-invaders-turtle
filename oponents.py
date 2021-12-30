from turtle import Turtle, shape
from bullet import Bullet
import random
X_COORDS = (-250, 250)
Y_COORDS = (200, 50)


class Oponent(Turtle):

    def __init__(self, bullet_shape):
        super().__init__()
        self.bullet_shape = bullet_shape
        self.type = "oponent"
        self.is_alive = True

    def shoot(self):
        Bullet(shape=self.bullet_shape, pos=(
            self.xcor(), self.ycor()-10), heading=270)


class OponentField:

    def __init__(self, shape, bullet_shape):
        self.bullet_shape = bullet_shape
        self.oponents: list[Oponent] = []
        field_generating = True
        x_pos = X_COORDS[0]
        y_pos = Y_COORDS[0]
        while field_generating:
            if x_pos > X_COORDS[1]:
                x_pos = X_COORDS[0]
                y_pos -= 50
            if y_pos < Y_COORDS[1]:
                field_generating = False
                break
            oponent = Oponent(bullet_shape=self.bullet_shape)
            oponent.hideturtle()
            oponent.penup()
            oponent.setposition(x=x_pos, y=y_pos)
            oponent.shape(shape)
            oponent.showturtle()
            self.oponents.append(oponent)
            x_pos += 50

    def move(self):
        if self.oponents[-1].xcor() > 325:
            for oponent in self.oponents:
                oponent.setheading(180)
        elif self.oponents[0].xcor() < -325:
            for oponent in self.oponents:
                oponent.setheading(0)
        for oponent in self.oponents:
            alive_oponents = self.get_alive_oponents()
            oponent.forward(12.5)
            if len(alive_oponents) > 5 and oponent.is_alive:
                if random.randint(0, 2*len(self.oponents)) == 12:
                    oponent.shoot()
            elif oponent.is_alive:
                if random.randint(0, 6) == 3:
                    oponent.shoot()

    def get_alive_oponents(self):
        return [oponent for oponent in self.oponents if oponent.is_alive]