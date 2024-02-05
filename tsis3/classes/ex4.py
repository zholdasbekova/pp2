import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(3, 4)
point2 = Point(1, 2)

point1.show()
point2.show()

point1.move(2, 3)
point1.show()

distance = point1.dist(point2)
print(f"Distance between the points: {distance}")
