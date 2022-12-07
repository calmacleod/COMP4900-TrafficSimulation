import CONSTANTS
from TrafficLight import TrafficLight
class Road:
    def __init__(self, direction, offset):
        self.direction = direction
        self.offset = offset
        self.vehicles = []
        self.lights   = []
        if self.direction == 1:
            self.length = CONSTANTS.SCREEN_WIDTH
        elif self.direction == 2:
            self.length = CONSTANTS.SCREEN_HEIGHT


    #TODO Implement
    def update(self):
        for v in self.vehicles:
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

    def vehicle_finished(self, vehicle):
        self.vehicles.remove(vehicle)
        if(len(self.vehicles) > 0):
            self.vehicles[0].lead = None

        del vehicle

        
