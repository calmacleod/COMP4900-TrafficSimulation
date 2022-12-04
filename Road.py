from TrafficLight import TrafficLight
class Road:
    def __init__(self, direction, offset):
        self.direction = direction
        self.offset = offset
        self.vehicles = []

    #TODO Implement
    def update(self):
        return 0

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

