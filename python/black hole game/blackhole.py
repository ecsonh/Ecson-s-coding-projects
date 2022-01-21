# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model
eaten = set()
class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y,width,height):
        Simulton.__init__(self,x,y,width,height)
        
        
    def contains(self, xy):
        if self.distance(xy) < self.radius:
            return True 
        else:
            return False

    def display(self,canvas):
        x,y = self.get_location()
        canvas.create_oval(x -self.radius      , y-self.radius,
                                x+self.radius, y+self.radius,
                                fill='black')
    def update(self):
        global eaten
        the_prey = model.find(Prey)
        for i in the_prey:
            if self.contains(i.get_location()):
                eaten.add(i)
                model.simulton.remove(i)
                
        
        
    
            
    
    
