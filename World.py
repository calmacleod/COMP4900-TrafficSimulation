from Road import Road
from Vehicle import Vehicle
import random
class World:
    def __init__(self):
            self.vehicles = []
            self.done_vehicles = []
            self.roads    = []
            self.tick     = 0

    def add_road(self,start,end):
        r = Road(start,end)
        self.roads.append(r)
        return r

    def add_vehicle(self, road):
        self.vehicles.append(Vehicle(road))

    def update(self):
        self.tick += 1

        if(self.tick % 10 == 0):
            self.add_vehicle(random.choice(self.roads))

        for v in self.vehicles:
            #TODO - Implement update
            v.updatePosition()
    
    def get_finished(self):
        people = 0
        for v in self.done_vehicles:
            people += v.capacity
        return people 