import CONSTANTS
from TrafficLight import *
from Bus import Bus
class Road:
    def __init__(self, direction, offset):
        self.direction = direction
        self.offset = offset
        self.travelled = 0
        self.vehicles = []
        self.lights   = []
        if self.direction == 1:
            self.length = CONSTANTS.SCREEN_WIDTH
        elif self.direction == 2:
            self.length = CONSTANTS.SCREEN_HEIGHT


    #TODO Implement
    def update(self):
        for v in self.vehicles:
            if(isinstance(v,Bus)):
                if v in self.first_three_vehicles(self.lights[0]) and self.lights[0].state == LIGHT_COLOR.RED:
                    self.lights[0].request_priority()

            v.update()

            if(v.should_delete()):
                self.vehicle_finished(v)

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def get_last_vehicle(self):
        if(self.vehicles == []):
            return None
        return self.vehicles[-1]

    def add_traffic_light(self, light):
        self.lights.append(light)

    def can_create_car(self):
        for v in self.vehicles:
            if(v.pos < v.l):
                return False
        return True

    def vehicle_finished(self, vehicle):
        self.travelled += vehicle.capacity
        self.vehicles.remove(vehicle)
        if(len(self.vehicles) > 0):
            self.vehicles[0].lead = None
        del vehicle

    def first_three_vehicles(self,traffic_light):
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