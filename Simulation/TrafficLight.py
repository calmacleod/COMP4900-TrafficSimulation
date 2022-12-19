from enum import Enum
import Simulation.CONSTANTS as CONSTANTS

class TrafficLight:
    def __init__(self,position,extended=False):
        self.state = LIGHT_COLOR.GREEN
        self.position = position
        self.control = None
        self.extended = extended

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def get_stop_distance(self):
        if(self.extended):
            return self.position - CONSTANTS.ROAD_WIDTH//2 - CONSTANTS.ROAD_WIDTH
        else:
            return self.position - CONSTANTS.ROAD_WIDTH//2 

    def request_priority(self):
        self.control.request_priority(self)

    def get_rgb(self):
        if(self.state == LIGHT_COLOR.RED):
            return (207, 31, 19)
        elif(self.state == LIGHT_COLOR.AMBER):
            return (207, 163, 19)
        else:
            return (5, 135, 14)


class LIGHT_COLOR(Enum):
    RED    = 1
    AMBER = 2
    GREEN  = 3
