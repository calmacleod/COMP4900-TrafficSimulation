from Simulation.Vehicle import Vehicle
import random
import Simulation.CONSTANTS as CONSTANTS

class Car(Vehicle):
    def __init__(self, road, lead = None):
        super().__init__(road,lead)
        self.l = CONSTANTS.CAR_LENGTH
        self.capacity = random.randrange(CONSTANTS.CAR_CAPACITY_RANGE[0],CONSTANTS.CAR_CAPACITY_RANGE[1])