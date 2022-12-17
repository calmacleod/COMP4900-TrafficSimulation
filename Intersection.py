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

        #Assume road_1 = 1 or 3 and road_2 = 2 or 4
        if(road_1.direction == 1):
            xPos = road_2.offset
        elif(road_1.direction == 3):
            xPos = CONSTANTS.SCREEN_WIDTH - road_2.offset

        if(road_2.direction == 2):
            yPos = road_1.offset
        elif(road_2.direction == 4):
            yPos = CONSTANTS.SCREEN_HEIGHT - road_1.offset

        self.position = (xPos,yPos)

        road_1_light = TrafficLight(xPos)
        road_2_light = TrafficLight(yPos)

        road_1.add_traffic_light(road_1_light)
        road_2.add_traffic_light(road_2_light)

        self.control = TrafficControl()
        self.control.add_light(road_1_light)
        self.control.add_light(road_2_light)
        self.control.prep_intersection()

    def update(self):
        self.control.update()
            