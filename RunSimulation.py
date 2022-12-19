from Simulation.World import World
from Interface.Data_Entry import Data_Entry
import SaveStats

Data_Entry().data_entry()

for i in range(1):
    w = World()

    w.add_4_way(465,365)

    while not w.done:
        w.update()

    SaveStats.get_output(w)
