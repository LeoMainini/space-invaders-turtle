from turtle import Turtle, distance


class Bullet(Turtle):
    def __init__(self, shape, pos, heading):
        super().__init__()
        self.type = "bullet"
        self.hideturtle()
        self.penup()
        self.shape(shape)
        self.setheading(heading)
        self.setposition(x=pos[0], y=pos[1])
        self.showturtle()

    def move(self):

        if self.ycor() > 320 or self.ycor() < -320 and self.isvisible():
            self.clear_turtle()
        else:
            self.forward(5)

    def clear_turtle(self):
        self.hideturtle()

    def detect_monster_colision(self, oponent_field: list[Turtle]):
        if self.heading() != 90:
            return False
        for oponent in oponent_field:
            if self.distance(oponent) < 12 and oponent.is_alive:
                self.setposition(600, 600)
                oponent.is_alive = False
                oponent.hideturtle()
                return True

    def detect_player_collision(self, player: Turtle):
        if self.heading() != 270:
            return False
        if self.distance(player) < 15 and player.lives > 0:
            self.setposition(600, 600)
            player.lives -= 1
            return True

    def detect_collisions(self, oponents, player):
        if self.detect_monster_colision(oponents):
            player.score += 20
        self.detect_player_collision(player)
