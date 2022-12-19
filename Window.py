import pygame
import CONSTANTS
from World import World
from Road  import Road
class Window:
    def __init__(self,world: World):
        self.default_config()
        self.world = world
        self.width = CONSTANTS.SCREEN_WIDTH
        self.height = CONSTANTS.SCREEN_HEIGHT
        self.road_width = CONSTANTS.ROAD_WIDTH

    def default_config(self):
        self.bg_colors = (255,255,255)

        self.fps  = 60
        self.zoom = 5
        self.offset = (0,0)

        self.mouse_last = (0,0)
        self.mouse_down = False

    def loop(self):
        self.screen = pygame.display.set_mode((self.width,self.height))

        pygame.display.flip()

        clock = pygame.time.Clock()

        pygame.font.init()
        self.text_font = pygame.font.SysFont('Lucida Console', 16)
        self.draw_background()

        running = True

        while running:
            #Update Simulation
            self.draw()

            pygame.display.update()
            #clock.tick(self.fps)
            clock.tick(60)

            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.QUIT:
                    running = False;

            if(self.world.done):
                running = False

    def draw_background(self):
        self.screen.fill(self.bg_colors)

    def draw_roads(self):
        width = self.road_width

        for r in self.world.roads:
            # Road to the right
            if(r.direction == 1 or r.direction == 3):
                xPos = 0
                yPos = r.offset - width//2
                length = self.width
                roadRect = pygame.Rect(xPos,yPos,length,width)

            elif(r.direction == 2 or r.direction == 4):
                xPos = r.offset - width//2
                yPos = 0
                length = self.height
                roadRect = pygame.Rect(xPos,yPos,width,length)

            pygame.draw.rect(self.screen,pygame.Color(115, 125, 118), roadRect)

    def draw_cars(self):
        width = self.road_width

        vehicles = []

        for road in self.world.roads:
            vehicles = vehicles + road.vehicles


        for v in vehicles:
            if(v.road.direction == 1):
                xPos = v.pos
                yPos = v.road.offset - width//2
                length = v.l
                #Spawn off screen vehicles
                if(xPos + length < 0):
                    continue  
                vehicleRect = pygame.Rect(xPos,yPos,length,self.road_width)
            elif(v.road.direction == 2):
                xPos = v.road.offset - width//2
                yPos = v.pos
                length = v.l
                vehicleRect = pygame.Rect(xPos,yPos,self.road_width,length)
            elif(v.road.direction == 3):
                length = v.l
                yPos = v.road.offset - width//2
                xPos = CONSTANTS.SCREEN_WIDTH - (v.pos+length)

                if(xPos > CONSTANTS.SCREEN_WIDTH):
                    continue

                vehicleRect = pygame.Rect(xPos,yPos,length,self.road_width)
            elif(v.road.direction == 4):
                xPos = v.road.offset - width//2 
                yPos = CONSTANTS.SCREEN_HEIGHT - v.pos - v.l
                length = v.l
                vehicleRect = pygame.Rect(xPos,yPos,self.road_width,length)

            if(v.first_car):
                color = pygame.Color(18, 39, 148)
            else:
                if(v.type == 1):
                    color = pygame.Color(173, 150, 59)
                elif(v.type == 2):
                    color = pygame.Color(59, 173, 95)
                else:
                    color = pygame.Color(235, 52, 82)
            pygame.draw.rect(self.screen,color, vehicleRect)

    def draw_stats(self):
        ticks = self.world.tick
        pplDone = self.world.get_finished()

        out_string = "Ticks: " + str(ticks)
        
        text = self.text_font.render(out_string,False, (0,0,0)) 

        text_rect = text.get_rect()

        text_rect.topleft = (0,0)

        self.screen.blit(text,text_rect)

    def draw_lights(self):
        width = self.road_width
        light_size = 10
        for r in self.world.roads:
            for light in r.lights:
                if(r.direction == 1):
                    xPos = light.position + width//2
                    yPos = r.offset - width//2
                    length = light_size
                    light_rect = pygame.Rect(xPos,yPos,length,width)
                    pygame.draw.rect(self.screen,pygame.Color(light.get_rgb()), light_rect)
                elif(r.direction == 2):
                    yPos = light.position + width//2
                    xPos = r.offset - width//2
                    length = light_size
                    light_rect = pygame.Rect(xPos,yPos,width,length)
                    pygame.draw.rect(self.screen,pygame.Color(light.get_rgb()), light_rect)
                elif(r.direction == 3):
                    xPos = (CONSTANTS.SCREEN_WIDTH - light.position) - (width//2 + light_size)
                    yPos = r.offset - width//2
                    length = light_size
                    light_rect = pygame.Rect(xPos,yPos,length,width)
                    pygame.draw.rect(self.screen,pygame.Color(light.get_rgb()), light_rect)
                elif(r.direction == 4):
                    yPos = (CONSTANTS.SCREEN_HEIGHT - light.position) - (width//2 + light_size)
                    xPos = r.offset - width//2
                    length = light_size
                    light_rect = pygame.Rect(xPos,yPos,width,length)
                    pygame.draw.rect(self.screen,pygame.Color(light.get_rgb()), light_rect)
    
    def draw(self):
        self.draw_background()
        # Draw roads
        self.world.update()

        self.draw_stats()

        self.draw_roads()

        self.draw_lights()

        self.draw_cars()

        
