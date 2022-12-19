from Simulation.Vehicle import Vehicle
import random
import Simulation.CONSTANTS as CONSTANTS

class Bus(Vehicle):
    def __init__(self, road, lead = None):
        super().__init__(road,lead)
        self.l = CONSTANTS.BUS_LENGTH
        self.capacity = random.randrange(CONSTANTS.BUS_CAPACITY_RANGE[0],CONSTANTS.BUS_CAPACITY_RANGE[1])
        