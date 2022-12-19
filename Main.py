from Simulation.World import World
from Interface.Window import Window
from Interface.Data_Entry import Data_Entry
import SaveStats

Data_Entry().data_entry()

w = World()

#Generates 4-way interection centered around coordinates
w.add_4_way(465,365)

#Generates 2-way intersection centered around coordinates
#w.add_2_way(450,350)

window = Window(w)

window.loop()

SaveStats.get_output(w)
