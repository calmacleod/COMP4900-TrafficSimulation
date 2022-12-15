from World import World
from Data_Entry import Data_Entry
import SaveStats

Data_Entry().data_entry()

for i in range(10):
    w = World()

    r1 = w.add_road(1,500,True)
    r2 = w.add_road(2,500)

    w.add_intersection(r1,r2)

    while not w.done:
        w.update()

    SaveStats.get_output(w)
