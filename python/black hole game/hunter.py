# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model
from blackhole import Black_Hole, eaten
class Hunter(Pulsator, Mobile_Simulton):  
    speed = 5
    radius = 10
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y, Hunter.radius, Hunter.radius)
        Mobile_Simulton.__init__(self,x,y,Hunter.radius,Hunter.radius,0,Hunter.speed)
        self.randomize_angle()
        self.counter = 0
        
    def update(self):
        x,y = self.get_location()
        self.counter+=1
        the_prey = model.find(Prey)
        min = 1000   
        for i in the_prey:
            if abs(self.distance(i.get_location())- self.radius) <200:
                next_prey = self.distance((abs(i.get_location()[0]), abs(i.get_location()[1])))
                if next_prey < min:
                    closest = i
                    min = next_prey
        if min != 1000:
            self.set_angle(atan2(closest.get_location()[1]-y, closest.get_location()[0]-x)) #
            if self.contains(closest.get_location()):
                eaten.add(i)
                model.simulton.remove(closest)
                self.radius +=1
                self.counter = 0
        if self.radius > 1:
            if self.counter == 30:
                self.radius-=1
                self.counter = 0
        else:
            model.simulton.remove(self)  
        self.move()  
        self.wall_bounce()
        
    #closest = min([self.distance((abs(i.get_location()[0]-x), abs(i.get_location()[0]-x)))-self.radius for i in the_prey])
