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

    important_values = {}

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        f = open(path,"r")
        var = f.read()
        f.close()
        var = var.splitlines()
        #print(var)

        for line_num,line in enumerate(var):
            if("Road ID" in line):
                road_data = []
                for i in range(6):
                    road_data.append(int(var[line_num+i].split(" ")[-1]))

                if(road_data[0] not in important_values):
                    important_values[road_data[0]] = road_data
                else:
                    for i in range(2,6):
                        important_values[road_data[0]][i] += road_data[i]
            elif("Constants" in line):
                break
    
    print(folder)
    print("Averages over",len(os.listdir(folder)),"simulations:")
    print("----------------")
    for road in important_values.values():
        print(f"Road {road[0]} Direction        ",road[1])
        print(f"Road {road[0]} Cars:            ",road[2] // len(os.listdir(folder)))
        print(f"Road {road[0]} Cars Passengers: ",road[3] // len(os.listdir(folder)))
        print(f"Road {road[0]} Bus:             ",road[4] // len(os.listdir(folder)))
        print(f"Road {road[0]} Bus Passengers:  ",road[5] // len(os.listdir(folder)))
        print("----------------")


