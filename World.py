from Road import Road
from Vehicle import Vehicle
from Bus import Bus
from Car import Car
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
            self.max_tick = CONSTANTS.MAX_TICK
            self.done = False

    def add_road(self,start,end,make_bus = False):
        r = Road(start,end,make_bus)
        self.roads.append(r)
        return r

    def add_vehicle(self, road):
        #Chance of bus
        makeBus = random.random() < CONSTANTS.BUS_PROB
        #Hardwire not great
        hypoLength = CONSTANTS.BUS_LENGTH if makeBus else CONSTANTS.CAR_LENGTH
        if(road.can_create_car(hypoLength)):
            if(makeBus):
                v = Bus(road,road.get_last_vehicle())
            else:
                v = Car(road,road.get_last_vehicle())
            self.vehicles.append(v)
            road.add_vehicle(v)

    def add_vehicle_queue(self):
        if(bool(random.getrandbits(1))):
            self.roads[0].add_vehicle_queue(random.random() < CONSTANTS.BUS_PROB)
        else:
            self.roads[1].add_vehicle_queue(False)

    def add_intersection(self,road1,road2):
        intersection = Intersection(road1,road2)
        self.intersections.append(intersection)

    def get_finished(self):
        people = 0
        for v in self.done_vehicles:
            people += v.capacity
        return people 

    def update(self):
        for i in self.intersections:
            i.update()

        for r in self.roads:
            r.update(self.tick)

        self.tick += 1

        if(self.tick == self.max_tick):
            self.done = True

            

        
    
    

    