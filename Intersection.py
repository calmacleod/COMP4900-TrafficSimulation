from TrafficLight import TrafficLight
from TrafficControl import *

class Intersection:
    def __init__(self,road_1,road_2):
        if((road_1.direction == 1 or road_1.direction == 3) and (road_2.direction == 1 or road_2.direction == 3)):
            return #Both moving East-West
        elif((road_1.direction == 2 or road_1.direction == 4) and (road_2.direction == 2 or road_2.direction == 4)):
            return #Both moving North-South
        elif(road_1.direction == road_2.direction):
            return #Both in the same direction

        roads = [road_1,road_2]
        xPos = 0
        yPos = 0
        
        for road in roads:
            if(road.direction == 1 or road.direction == 3):
                xPos = road.offset
            if(road.direction == 2 or road.direction == 4):
                yPos = road.offset

        self.position = (xPos,yPos)

        road_1_light = TrafficLight(road_2.offset)
        road_2_light = TrafficLight(road_1.offset)

        road_1.add_traffic_light(road_1_light)
        road_2.add_traffic_light(road_2_light)

        self.control = TrafficControl()
        self.control.add_light(road_1_light)
        self.control.add_light(road_2_light)
        self.control.prep_intersection()

    def update(self):
        self.control.update()
            