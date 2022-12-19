from Simulation.World import World
from Simulation.Car import *
from Simulation.Bus import *
from Simulation.Road import *
import time
from pathlib import Path
import Simulation.CONSTANTS as CONSTANTS
import os
import os.path


def get_book_variable_module_name(module_name):
    module = globals().get(module_name, None)
    book = {}
    if module:
        book = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
    return book

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path

def get_formatted(key, value):
    if(isinstance(value, tuple)):
        value = ",".join(map(str,value))
    return f'{key:<18}  {value:>8}\n'


def get_output(world: World):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    file_name = uniquify("results/results_"+timestr)

    f = open(file_name, "w")

    f.write("STATS: \n")

    f.write(get_formatted("Ticks",world.tick))
    
    f.write("\n")

    for r in world.roads:
        f.write(get_formatted("Road ID",r.id))
        f.write(get_formatted("Road Direction,",r.direction))
        f.write(get_formatted("Car Travelled",r.car_trav))
        f.write(get_formatted("Car Passengers",r.car_pass))
        f.write(get_formatted("Bus Travelled",r.bus_trav))
        f.write(get_formatted("Bus Passengers",r.bus_pass))
        f.write("\n")

    book = get_book_variable_module_name("CONSTANTS")

    f.write("Constants: \n")

    for key,value in book.items():
        f.write(get_formatted(key,value))

    f.close()




