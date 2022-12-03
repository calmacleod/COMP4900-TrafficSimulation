from enum import Enum

class TrafficLight:
    def __init__(self):
        self.state = LIGHT_COLOR.GREEN

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state


class LIGHT_COLOR(Enum):
    RED    = 1
    AMBERT = 2
    GREEN  = 3
