import controller
import model   # Calls to update in update_all are passed a reference to model

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special
from simulton import Simulton



# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
simulton = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simulton
    running = False
    cycle_count = 0
    simulton = set()
    
    


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, simulton, running
    running = False
    cycle_count+=1
    controller.the_progress.config(text=str(len(simulton))+" simulton/"+str(cycle_count)+" cycles")
    for s in simulton:
        s.update()


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global name
    name = kind
    

#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if name == 'Ball':
        simulton.add(Ball(x,y))
    elif name == 'Floater':
        simulton.add(Floater(x,y))
    elif name == 'Black_Hole':
        simulton.add(Black_Hole(x,y,Black_Hole.radius,Black_Hole.radius))
    elif name == 'Pulsator':
        simulton.add(Pulsator(x,y,Pulsator.radius, Pulsator.radius))
    elif name == 'Hunter':
        simulton.add(Hunter(x,y))
    elif name == 'Special':
        simulton.add(Special(x,y))
    elif name == 'Remove':
        remove((x,y))


#add simulton s to the simulation
def add(s):
    global simulton
    simulton.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simulton
    for i in simulton.copy():
        if abs(i.get_location()[0]-s[0])< 15 and abs(i.get_location()[1]-s[1])< 15:
            simulton.remove(i)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    s = set()
    for i in simulton:
        if isinstance(i,p):
            s.add(i)
    return s
        


# for each simulton in this simulation, call update (passing model to it) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for s in simulton.copy():
            s.update()

#How to animate: 1st: delete all simultons on the canvas; 2nd: call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; 3rd: update the label defined in the controller for progress 
#  this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    global cycle_count
    global simulton
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simulton:
        s.display(controller.the_canvas)
    
    

    controller.the_progress.config(text=str(len(simulton))+" simulton/"+str(cycle_count)+" cycles")
