import os
import statistics
import re


def calculate_diff(first,cur):
    return (cur-first)


#Set to path to results
f1 = r''

folder = f1
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
sorted_folder = sorted(subfolders)
file_name = [s.split("\\")[-1] for s in sorted_folder]
sf_priority = [int(re.search(r'\d+',s).group()) for s in file_name]

print(sf_priority)

print("---MEDIAN---")

first_val = None

bus_median = {}
nb_median  = {}


for folder_number,folder in enumerate(sorted(subfolders)):
    car_passengers = {}
    bus_passengers = {}
    
    for i in range(1,5):
        car_passengers[i] = []
        bus_passengers[i] = []
    
    for file in os.listdir(folder):
        car_by_road = {}
        bus_by_road = {}
        for i in range(1,5):
            car_by_road[i] = 0
            bus_by_road[i] = 0
                
        path = os.path.join(folder, file)
        f = open(path,"r")
        var = f.read()
        f.close()
        var = var.splitlines()
        for line_num,line in enumerate(var):
            if("Road ID" in line):
                road_data = []
                for i in range(6):
                    road_data.append(int(var[line_num+i].split(" ")[-1]))
                car_by_road[road_data[1]] += road_data[3]
                bus_by_road[road_data[1]] += road_data[5]
            elif("Constants" in line):
                break
                
        for i in range(1,5):
            car_passengers[i].append(car_by_road[i])
            bus_passengers[i].append(bus_by_road[i])
    
    for i in range (1,5):
        median_car = statistics.median(car_passengers[i])
        median_bus = statistics.median(bus_passengers[i])
        total = round(median_car+median_bus,2)
        if first_val is None:
            first_val = total
            
        pri = sf_priority[folder_number]
        if(i == 1 or i == 3):
            if pri not in bus_median.keys():
                bus_median[pri] = median_bus
            else:
                bus_median[pri] += median_bus
        
        #Replace i == X or i == Y with road direction you wish to measure cars for
        if(i == 2 or i == 4):
            if pri not in nb_median.keys():
                nb_median[pri] = median_car
            else:
                nb_median[pri] += median_car
            


# Bus & Car Mean
print("----BUS----")
[print(k,v) for k,v in bus_median.items()]

print("----CAR----")
[print(k,v) for k,v in nb_median.items()]


first_val = None
print("---MEAN---")   
for folder_number,folder in enumerate(sorted(subfolders)):
    important_values = {}
    
    car_passengers = 0
    bus_passengers = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        f = open(path,"r")
        var = f.read()
        f.close()
        var = var.splitlines()
        for line_num,line in enumerate(var):
            if("Road ID" in line):
                road_data = []
                for i in range(6):
                    road_data.append(int(var[line_num+i].split(" ")[-1]))

                if(road_data[1] not in important_values):
                    important_values[road_data[1]] = road_data
                else:
                    for i in range(2,6):
                        important_values[road_data[1]][i] += road_data[i]
            elif("Constants" in line):
                break
    
    
    for road in important_values.values():
        car_pass_val = round(road[3] / len(os.listdir(folder)),2)
        bus_pass_val = round(road[5] / len(os.listdir(folder)),2)
        
        car_passengers += car_pass_val
        bus_passengers += bus_pass_val
        
    r_car = round(car_passengers,2)
    r_bus = round(bus_passengers,2)
    r_tot = round(car_passengers+bus_passengers,2)
    
    if first_val is None:
        first_val = r_tot
    
    r_cha = round(calculate_diff(first_val,r_tot),2)
    
    print(sf_priority[folder_number],r_car,r_bus,r_tot,r_cha)
    important_values.clear()
    
print("\n")