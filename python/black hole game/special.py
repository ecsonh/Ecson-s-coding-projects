from prey import Prey
import tkinter as tk
import random
#The Special class work as a prey that moves in parallel direction.
#in bounce when it hits the wall and turn in the opposite direction
#this rectangle prey will be sparkling by chaning it's color every cycle.
# it will disappear if it's eaten by a blackhole, pulstor, or hunter.

class Special(Prey):
    radius  = 10
    speed = 15
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,Special.radius,Special.radius,0,Special.speed)
        self.set_angle(0)
        
    def update(self):
        self.wall_bounce()
        self.move()
        
    
    def display(self,canvas):
        colors = ["red", "orange", "yellow", "green", "blue", "violet", "white"]
        x, y = self.get_location()
        canvas.create_rectangle(x+Special.radius      , y+Special.radius,
                                x+Special.radius*2, y+Special.radius*2,
                                fill=random.choice(colors))

