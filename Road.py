from TrafficLight import TrafficLight
class Road:
    def __init__(self, direction, offset):
        self.direction = direction
        self.offset = offset
        self.vehicles = []
        self.lights   = []

    #TODO Implement
    def update(self):
        return 0

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def get_last_vehicle(self):
        if(self.vehicles == []):
            return None
        return self.vehicles[-1]

    def add_traffic_light(self, light):
        self.lights.append(light)