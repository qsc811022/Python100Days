import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.height


c = Cylinder(5, 10)
print("Volume:", c.volume())
print("Surface Area:", c.surface_area())


class Line:
    def __init__(self,coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        if x2 - x1 == 0:
            return float('inf')  # Infinite slope (vertical line)
        return (y2 - y1) / (x2 - x1)

line = Line((0, 0), (3, 4))
print("Distance:", line.distance())
    