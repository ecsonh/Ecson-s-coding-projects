# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey): 
    radius  = 5
    speed = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,Floater.radius,Floater.radius,0,Floater.speed)
        
        
    def update(self):
        y = random.randint(0,100)
        if 0 <= y <= 30:
            self.randomize_angle()
            angle = self.get_angle()
            x = random.randint(-5,5) * 0.1
            while Floater.speed + x > 7 or Floater.speed + x < 3:
                x = random.randint(-5,5) *0.1
            newspeed = Floater.speed+x
            self.set_velocity(newspeed, angle)
            
        self.wall_bounce()
        self.move()
        
        
    def display(self,canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Floater.radius      , y-Floater.radius,
                                x+Floater.radius, y+Floater.radius,
                                fill='red')
