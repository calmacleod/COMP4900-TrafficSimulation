from Vehicle import Vehicle
import random

class Car(Vehicle):
    def __init__(self, road, lead = None):
        super().__init__(road,lead)
        self.l = 40
        self.capacity = random.randrange(1,5)