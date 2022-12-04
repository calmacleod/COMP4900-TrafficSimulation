from World import World
from Window import Window


w = World()

r1 = w.add_road(1,250)
#r2 = w.add_road(2,500)

window = Window(w)

window.loop()

