from TrafficLight import TrafficLight
from TrafficControl import *

class Intersection:
    def __init__(self,road_1,road_2,road_3=None,road_4=None):
        if(road_3 is None and road_4 is None):
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

            road_1_light = TrafficLight(xPos)
            road_2_light = TrafficLight(yPos)

            road_1.add_traffic_light(road_1_light)
            road_2.add_traffic_light(road_2_light)

            self.control = TrafficControl()
            self.control.add_light_2(road_1_light,road_2_light)
            self.control.prep_intersection()
        else:
            r_1_pos = road_1.offset
            r_2_pos = road_2.offset
            r_3_pos = road_3.offset
            r_4_pos = road_4.offset

            l_1_pos = r_4_pos
            l_2_pos = r_1_pos
            l_3_pos = CONSTANTS.SCREEN_WIDTH - r_2_pos
            l_4_pos = CONSTANTS.SCREEN_HEIGHT - r_3_pos

            r_1_light = TrafficLight(l_1_pos,True)
            r_2_light = TrafficLight(l_2_pos,True)
            r_3_light = TrafficLight(l_3_pos,True)
            r_4_light = TrafficLight(l_4_pos,True)

            road_1.add_traffic_light(r_1_light)
            road_2.add_traffic_light(r_2_light)
            road_3.add_traffic_light(r_3_light)
            road_4.add_traffic_light(r_4_light)

            self.control = TrafficControl()
            self.control.add_light_4(r_1_light,r_2_light,r_3_light,r_4_light)
            self.control.prep_intersection()

    def update(self):
        self.control.update()
            