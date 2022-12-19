import Simulation.CONSTANTS as CONSTANTS
from Simulation.TrafficLight import *
from Simulation.Vehicle import Vehicle
from Simulation.Bus import Bus
from Simulation.Car import Car
import itertools
import random

class Road:
    id_obj = itertools.count()
    
    def __init__(self, direction, offset,make_bus = False):
        self.id = next(Road.id_obj)

        self.direction = direction
        self.offset = offset
        self.make_bus = make_bus

        self.bus_trav = 0
        self.car_trav = 0
        
        self.bus_pass = 0
        self.car_pass = 0

        self.vehicles = []
        self.lights   = []
        
        if self.direction == 1 or self.direction == 3:
            self.length = CONSTANTS.SCREEN_WIDTH
        elif self.direction == 2 or self.direction == 4:
            self.length = CONSTANTS.SCREEN_HEIGHT

    def update(self, tick):
        if(tick % 50 == 0):
            if(len(self.vehicles) < 90):
                self.add_vehicle_ignore_distance()

        for v in self.vehicles:
            if(isinstance(v,Bus)):
                if v in self.first_n_vehicles(self.lights[0]) and self.lights[0].state == LIGHT_COLOR.RED:
                    self.lights[0].request_priority()

            v.update()

            if(v.should_delete()):
                self.vehicle_finished(v)

    def add_vehicle_ignore_distance(self):
        v = None
        if(self.make_bus):
            if random.random() < CONSTANTS.BUS_PROB:
                v = Bus(self,self.get_last_vehicle())
            else:
                v = Car(self,self.get_last_vehicle())
                v.assign_type()
        else:
            v = Car(self,self.get_last_vehicle())
            v.assign_type()

        if((x := self.get_last_vehicle()) is not None):
            #Can create car immediately
            if x.pos > (v.s0):
                v.pos = -v.l
            else:
                v.pos = x.pos - (v.l + v.s0 + 1)

        self.vehicles.append(v)

    def get_last_vehicle(self):
        if(self.vehicles == []):
            return None
        return self.vehicles[-1]

    def add_traffic_light(self, light):
        self.lights.append(light)
        self.lights.sort(key=lambda x: x.position)

    def can_create_car(self,length):
        if(len(self.vehicles) > 0):
            return self.vehicles[-1].pos > length + 5
        return True

    def vehicle_finished(self, vehicle):
        if(isinstance(vehicle,Bus)):
            self.bus_trav += 1
            self.bus_pass += vehicle.capacity
        else:
            self.car_trav += 1
            self.car_pass += vehicle.capacity

        self.vehicles.remove(vehicle)

        if(len(self.vehicles) > 0):
            self.vehicles[0].lead = None
        del vehicle

    def get_light(self, vehicle: Vehicle):
        for light in self.lights:
            if(vehicle.pos < light.position + CONSTANTS.ROAD_WIDTH//2):
                return light
        return None

    def first_n_vehicles(self,traffic_light):
        light_pos = traffic_light.get_stop_distance()
        end_index = -1

        for i in range(len(self.vehicles)):
            if(self.vehicles[i].pos < light_pos):
                end_index = i
                break

        #Handle if no cars or all past light
        if(end_index == -1):
            return []

        last_car = min(end_index + 5, len(self.vehicles)+1)

        if (end_index == last_car):
            return []

        return self.vehicles[end_index:last_car]