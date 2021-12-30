from turtle import Screen, Shape
from tkinter import PhotoImage
from oponents import OponentField
from player import Player
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.tracer(0)
sc.bgcolor("black")
sc.title("Space Invaders")
small_ship = PhotoImage(file="resources/ship.png").subsample(32, 32)
sc.addshape("small_ship", Shape("image", small_ship))
oponent = PhotoImage(file="resources/oponent.png").subsample(24,24)
sc.addshape("oponent",Shape("image", oponent))
torpedo = PhotoImage(file="resources/torpedo.png").subsample(64,64)
sc.addshape("torpedo", Shape("image", torpedo))
bullet = PhotoImage(file="resources/bullet.png")
sc.addshape("bullet", Shape("image", bullet))

speed = 0.050
pt = Player(shape="small_ship", bullet_shape="bullet")
oponents = OponentField(shape="oponent", bullet_shape="torpedo")
sc.update()
# bf = BlockField()
sc.listen()
sc.onkeypress(fun=pt.move_left,key= "Left")
sc.onkeypress(fun=pt.move_right, key= "Right")
sc.onkey(fun=pt.shoot, key="space")
cycles = 0
game_over = False
while not game_over:
    sc.update()
    cycles += 1
    if cycles == 10:
        cycles = 0
        oponents.move()
    time.sleep(speed)
    
    
    
    
sc.exitonclick()
    
    



