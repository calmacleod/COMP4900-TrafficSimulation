from TrafficLight import *
import CONSTANTS
class TrafficControl:
    def __init__(self):
        self.lights = [[],[]]
        self.time = 0

        self.RED_TIME = CONSTANTS.RED_TIME
        self.YELLOW_TIME = CONSTANTS.YELLOW_TIME

        self.red_light_timer = self.RED_TIME
        
        self.current_light = 0
        self.priority_requested = False

    def add_light_2(self,light_1,light_2):
        light_1.control = self
        light_2.control = self

        self.lights[0].append(light_1)
        self.lights[1].append(light_2)

    def add_light_4(self,light_1,light_2,light_3,light_4):
        light_1.control = self
        light_2.control = self
        light_3.control = self
        light_4.control = self

        self.lights[0].append(light_1)
        self.lights[1].append(light_2)

        self.lights[0].append(light_3)
        self.lights[1].append(light_4)

    def add_light(self,traffic_light: TrafficLight):
        traffic_light.control = self
        self.lights.append(traffic_light)

    def prep_intersection(self):
        # Set all red
        for light_set in self.lights:
            for light in light_set:
                light.set_state(LIGHT_COLOR.RED)

        # Arbitrary first one green
        for light in self.lights[self.current_light]:
            light.set_state(LIGHT_COLOR.GREEN)

    def change_yellow(self):
        for light in self.lights[self.current_light]:
            light.set_state(LIGHT_COLOR.AMBER)

    def switch_lights(self):
        self.current_light = (self.current_light + 1) % 2

        for light_set in self.lights:
            for light in light_set:
                light.set_state(LIGHT_COLOR.RED)

        # Arbitrary first one green
        for light in self.lights[self.current_light]:
            light.set_state(LIGHT_COLOR.GREEN)

        self.reset_timers()

    def reset_timers(self):
        self.red_light_timer = self.RED_TIME

    def request_priority(self,light):
        if(self.red_light_timer > CONSTANTS.BUS_PRIORITY or self.priority_requested or self.red_light_timer <= self.YELLOW_TIME):
            return

        self.red_light_timer = self.YELLOW_TIME+1
        self.priority_requested = True

    def update(self):
        self.time += 1

        self.red_light_timer -= 1

        if(self.red_light_timer == self.YELLOW_TIME):
            self.change_yellow()

        if(self.red_light_timer == 0):
            self.switch_lights()
            if(self.priority_requested):
                self.priority_requested = False
        return 0