from Simulation.World import World
from Interface.Data_Entry import Data_Entry
import Simulation.CONSTANTS
import SaveStats
import os
import shutil

#Constant
Simulation.CONSTANTS.MAX_TICK   = 60_000
Simulation.CONSTANTS.RED_TIME   = 700
Simulation.CONSTANTS.BUS_PROB   = 0.05

priority_range = [100,150,200,250,300,350,400,450,500]

for prio in priority_range:
    Simulation.CONSTANTS.BUS_PRIORITY = prio
    for i in range(15):
        w = World()
        w.add_4_way(465,365)
        while not w.done:
            w.update()
        SaveStats.get_output(w)
    # Make new direction to save results 
    folder_name = f"{prio}_priority_results"
    newpath = r'./results/'+folder_name
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    # Move all results to said directory
    for f in os.scandir(r'./results'):
        if os.path.isfile(f):
            file_path = f.path
            destination_path = os.path.join(newpath,f.name)
            shutil.move(file_path,destination_path)
