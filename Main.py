from World import World
from Window import Window


w = World()

r1 = w.add_road(1,350)
r2 = w.add_road(2,500)

w.add_intersection(r1,r2)

window = Window(w)

window.loop()

