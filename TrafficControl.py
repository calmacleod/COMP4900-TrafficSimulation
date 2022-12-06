from TrafficLight import *
class TrafficControl:
    def __init__(self):
        self.lights = []
        self.time = 0

        self.red_light_timer = 300
        self.yellow_light_timer = 100
        self.current_light = 0

    def add_light(self,traffic_light: TrafficLight):
        self.lights.append(traffic_light)

    def prep_intersection(self):
        # Set all red
        for light in self.lights:
            light.set_state(LIGHT_COLOR.RED)

        # Arbitrary first one green
        self.lights[self.current_light].set_state(LIGHT_COLOR.GREEN)

    def change_yellow(self):
        self.lights[self.current_light].set_state(LIGHT_COLOR.AMBER)

    def switch_lights(self):
        self.current_light = (self.current_light + 1) % 2

        for light in self.lights:
            light.set_state(LIGHT_COLOR.RED)

        # Arbitrary first one green
        self.lights[self.current_light].set_state(LIGHT_COLOR.GREEN)

        self.reset_timers()


    def reset_timers(self):
        self.red_light_timer = 300

    def update(self):
        self.time += 1

        self.red_light_timer -= 1

        if(self.red_light_timer == self.yellow_light_timer):
            self.change_yellow()

        if(self.red_light_timer == 0):
            self.switch_lights()
        return 0