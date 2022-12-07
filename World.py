from Road import Road
from Vehicle import Vehicle
from Intersection import Intersection
import CONSTANTS
import random
class World:
    def __init__(self):
            self.vehicles = []
            self.done_vehicles = []
            self.roads    = []
            self.intersections = []
            self.tick     = 0

    def add_road(self,start,end):
        r = Road(start,end)
        self.roads.append(r)
        return r

    def add_vehicle(self, road):
        v = Vehicle(road,road.get_last_vehicle())
        self.vehicles.append(v)
        road.add_vehicle(v)

    def add_intersection(self,road1,road2):
        intersection = Intersection(road1,road2)
        self.intersections.append(intersection)

    def get_finished(self):
        people = 0
        for v in self.done_vehicles:
            people += v.capacity
        return people 

    def update(self):
        self.tick += 1

        # '''
        if(self.tick == 1):
            self.add_vehicle(random.choice(self.roads))

        if(self.tick % 30 == 0):
            self.add_vehicle(random.choice(self.roads))
        # '''

        for i in self.intersections:
            i.update()

        for r in self.roads:
            r.update()
            r.clear_vehicles()

            

        
    
    

    