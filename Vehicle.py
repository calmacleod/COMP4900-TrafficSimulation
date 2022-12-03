class Vehicle:
    def __init__(self, road, lead):
        self.road = road
        self.lead = lead

        self.delta = 2
        self.x = 0
        self.l = 4
        self.s = self.x - lead.x - self.l
        self.s0 = 3
        self.v_max = 60
        self.v = self.v_max
        self.diff_v = self.v - lead.v
        self.T = 1
        self.a = 10
        self.b = 10
    
    def checkLights():
        return road.light

    def updatePosition(self):
        sStar = self.s0 + (self.v * self.T) + ((self.v * self.diff_v) / sqrt(2 * self.a * self.b))
        acc = self.a * (1- (self.v / self.diff_v)^delta - (sStar / self.s)^2)
        
        return acc
