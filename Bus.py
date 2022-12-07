from Vehicle import Vehicle
import random

class Bus(Vehicle):
    def __init__(self, road, lead = None):
        super().__init__(road,lead)
        self.l = 80
        self.capacity = random.randrange(75,100)
        