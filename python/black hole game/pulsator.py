# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole, eaten
from prey import Prey
import model

class Pulsator(Black_Hole): 
    def __init__(self,x,y, width, height):
        radius = 10
        Black_Hole.__init__(self,x,y, Pulsator.radius, Pulsator.radius)
        self.counter = 0
    def update(self):
        global eaten
        self.counter+=1
        if self.radius > 1:
            if self.counter == 30:
                self.radius-=1
                self.counter = 0
            the_prey = model.find(Prey)
            for i in the_prey:
                if self.contains(i.get_location()):
                    eaten.add(i)
                    model.simulton.remove(i)
                    self.radius +=1
                    self.counter = 0
        else:
            model.simulton.remove(self)
            
            