# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 

import random
from prey import Prey


class Ball(Prey): 
    radius  = 5
    speed = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,Ball.radius,Ball.radius,0,Ball.speed)
        self.randomize_angle()
        
    def update(self):
        self.wall_bounce()
        self.move()
        
    
    def display(self,canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Ball.radius      , y-Ball.radius,
                                x+Ball.radius, y+Ball.radius,
                                fill='blue')
