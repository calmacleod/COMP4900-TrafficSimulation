from os import listdir
from os.path import isfile, join
import glob
import os

subfolders = [ f.path for f in os.scandir("./results") if f.is_dir() ]


for folder in subfolders:
    road_1_car = 0
    road_1_bus = 0

    road_1_car_pass = 0
    road_1_bus_pass = 0

    road_2_car = 0
    road_2_car_pass = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        f = open(path,"r")
        var = f.read()
        f.close()
        var = var.splitlines()
        var = list(filter(None, var))
        keep = ["Road ID ","Travelled","Passengers",]
        key_info = []
        for string in var:
            for key_word in keep:
                if key_word in string:
                    key_info.append(string)
                    continue

        key_info = [int(item.split(" ")[-1]) for item in key_info]
            
        road_1_car += key_info[1]
        road_1_car_pass += key_info[2]
        road_1_bus += key_info[3]
        road_1_bus_pass += key_info[4]
        road_2_car += key_info[6]
        road_2_car_pass += key_info[7]
    print(folder)
    print("Road 1 Cars:            ",road_1_car // len(os.listdir(folder)))
    print("Road 1 Cars Passengers: ",road_1_car_pass // len(os.listdir(folder)))
    print("Road 1 Bus:             ",road_1_bus // len(os.listdir(folder)))
    print("Road 1 Bus Passengers:  ",road_1_bus_pass // len(os.listdir(folder)))
    print("Road 2 Cars:            ",road_2_car // len(os.listdir(folder)))
    print("Road 2 Cars Passengers: ",road_2_car_pass // len(os.listdir(folder)))

    print("----------------")


