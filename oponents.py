from turtle import Turtle, xcor
X_COORDS =(-250,250)
Y_COORDS =(200, 50)

class OponentField:
    def __init__(self, shape, bullet_shape):
        self.bullet_shape = bullet_shape
        self.oponents: list[Turtle] = []
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
            oponent = Turtle()
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
            oponent.forward(25)