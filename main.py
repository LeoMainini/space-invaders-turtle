from turtle import Screen, Shape, resizemode
from tkinter import PhotoImage
from oponents import OponentField
from player import Player
import time

from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=800, height=600)
sc.cv._rootwindow.resizable(False, False)
sc.tracer(0)
sc.bgcolor("black")
sc.title("Space Invaders")
small_ship = PhotoImage(file="resources/ship.png").subsample(32, 32)
sc.addshape("small_ship", Shape("image", small_ship))
oponent = PhotoImage(file="resources/oponent.png").subsample(24, 24)
sc.addshape("oponent", Shape("image", oponent))
torpedo = PhotoImage(file="resources/torpedo.png").subsample(32, 32)
sc.addshape("torpedo", Shape("image", torpedo))
bullet = PhotoImage(file="resources/bullet.png")
sc.addshape("bullet", Shape("image", bullet))
speed = 0.050

pt = Player(shape="small_ship", bullet_shape="bullet")
oponent_field = OponentField(shape="oponent", bullet_shape="torpedo")
sb = Scoreboard(pt.score, pt.lives)
sc.listen()
sc.onkeypress(fun=pt.move_left, key="Left")
sc.onkeypress(fun=pt.move_right, key="Right")
sc.onkey(fun=pt.shoot, key="space")
cycles = 0
start_time = time.time()
game_over = False
while pt.lives > 0 and (len(oponent_field.get_alive_oponents()) > 0):
    cycles += 1
    if cycles == 5:
        cycles = 0
        oponent_field.move()
    for turtle in sc.turtles():
        if turtle.type == "bullet":
            turtle.move()
            turtle.detect_collisions(oponent_field.oponents, pt)
    sb.update_sb(pt.score, pt.lives)
    sc.update()
    time.sleep(speed)

end_time = time.time()
timedelta = round(end_time-start_time, 3)
sb.game_over(timedelta)
sc.update()

sc.exitonclick()
