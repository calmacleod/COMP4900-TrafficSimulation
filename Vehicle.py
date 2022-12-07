import math
import CONSTANTS
from TrafficLight import LIGHT_COLOR

class Vehicle:
    def __init__(self, road, lead = None):
        self.first_car = (lead == None)
        self.road = road

        if not self.first_car:
            self.lead = lead
        
        self.pos = 0
        self.delta = 2
        self.x = 0
        self.l = 40
        
        self.s0 = 90
        self.v_max = 5
        self.v = self.v_max

        if not self.first_car:
            self.s = self.pos - lead.pos - self.l
            self.diff_v = self.v - lead.v
        else:
            self.s = 1000
            self.diff_v = 0

        self.T = 1
        self.a = 10
        self.b = 10

        self.root_constant = math.sqrt(2 * self.a * self.b)
    
    def update_acceleration(self):
        # - Update based on lead car
        if not self.first_car:
            self.s = self.lead.pos - self.pos -  - self.l
            self.diff_v = self.v - self.lead.v
        else:
            self.s = 1000
            self.diff_v = 0

        # If (Light yellow & V^2 / 2b > distance to light):
        if (self.road.lights[0].get_state() == LIGHT_COLOR.AMBER and self.pos < self.road.lights[0].position):
            if (self.v**2 / 2*self.b) > (self.road.lights[0].position - self.pos):
                self.s = self.road.lights[0].position - self.pos - self.l
                self.diff_v = self.v

        if (self.road.lights[0].get_state() == LIGHT_COLOR.RED and self.pos < self.road.lights[0].position):
            if self.first_car:
                self.s = self.road.lights[0].position - self.pos - 5
                self.diff_v = self.v
            elif (self.road.lights[0].position - self.pos) < (self.lead.pos - self.pos):
                self.s = self.road.lights[0].position - self.pos - 5
                self.diff_v = self.v



        #Perform accleration calculation
        sStar = self.s0 + (self.v * self.T) + ((self.v * self.diff_v) / self.root_constant)

        a_free_road = self.a * (1- (self.v / self.v_max)**self.delta)
        a_interatcion = -self.a * (sStar / self.s)**2

        acc = a_free_road + a_interatcion
        
        return acc
    
    def should_delete(self):
        return self.pos > self.road.length
        
    def update(self):
        if(not self.first_car and self.lead is None):
            self.first_car = True

        accel = self.update_acceleration()
        
        self.v += accel

        if(self.v <= 0):
            self.v = 0

        self.pos += self.v
