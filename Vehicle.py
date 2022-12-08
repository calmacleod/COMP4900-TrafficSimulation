import math
import CONSTANTS
from TrafficLight import LIGHT_COLOR

class Vehicle:
    def __init__(self, road, lead = None):
        self.first_car = (lead == None)
        self.road = road
        self.capacity = 4

        if not self.first_car:
            self.lead = lead
        
        self.pos = 0
        self.delta = 4
        self.x = 0
        self.l = 40
        
        self.s0 = 5
        self.v_max = 5
        self.v = self.v_max

        if not self.first_car:
            self.s = self.pos - lead.pos - self.l
            self.diff_v = self.v - lead.v
        else:
            self.s = 1000
            self.diff_v = 0

        self.T = 8
        self.a = 0.1
        self.b = 0.1

        self.root_constant = math.sqrt(2 * self.a * self.b)
    
    def update_acceleration(self):
        # - Update based on lead car
        if not self.first_car:
            self.s = self.lead.pos - (self.pos + self.l)
            self.diff_v = self.v - self.lead.v 
        else:
            self.s = 1000
            self.diff_v = 0

        light_state = self.road.lights[0].get_state()

        stop_line = self.road.lights[0].get_stop_distance()

        front_vehicle = self.pos + self.l
            
        if not self.first_car:
            distance_to_lead = self.lead.pos - (self.pos + self.l)

        # If (Light yellow & V^2 / 2b > distance to light):
        if (light_state == LIGHT_COLOR.AMBER and front_vehicle < stop_line):
            distance_to_light = stop_line - front_vehicle 
            if self.first_car:
                if self.calculate_can_stop(distance_to_light):
                    self.s = stop_line - front_vehicle
                    self.diff_v = self.v
            elif distance_to_light < distance_to_lead:
                if self.calculate_can_stop(distance_to_light):
                    self.s = stop_line - front_vehicle
                    self.diff_v = self.v

        if (light_state == LIGHT_COLOR.RED and front_vehicle < stop_line):
            distance_to_light = stop_line - front_vehicle 
            if self.first_car:
                self.s = stop_line - front_vehicle
                self.diff_v = self.v
            elif(distance_to_light < distance_to_lead):
                self.s = stop_line - front_vehicle
                self.diff_v = self.v



        #Perform accleration calculation
        sStar = self.s0 + (self.v * self.T) + ((self.v * self.diff_v) / self.root_constant)

        a_free_road = self.a * (1- (self.v / self.v_max)**self.delta)
        a_interatcion = -self.a * (sStar / self.s)**2

        acc = a_free_road + a_interatcion
        
        return acc
    
    def should_delete(self):
        return self.pos > self.road.length
        
    def calculate_can_stop(self,distance_to_light):
        sStar = self.s0 + (self.v * self.T) + ((self.v * self.v) / self.root_constant)

        a_free_road = self.a * (1- (self.v / self.v_max)**self.delta)
        a_interatcion = -self.a * (sStar / distance_to_light)**2

        return (a_free_road + a_interatcion) <= 0

    def update(self):
        if(not self.first_car and self.lead is None):
            self.first_car = True

        accel = self.update_acceleration()
        
        self.v += accel

        if(self.v <= 0):
            self.v = 0

        self.pos += self.v
