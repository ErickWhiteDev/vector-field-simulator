import math

class Vector:
    position = [0,0]
    x, y = 0, 0
    magnitude = 0
    angle = 0

    def __init__(self, position):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        self.angle = math.atan2(self.y, self.x)

    def modify_by_magnitude(self, factor):
        self.x *= factor
        self.y *= factor
        self.magnitude *= factor
        self.angle = math.atan2(self.y, self.x)
    
    def modify_by_components(self, x_factor, y_factor):
        self.x += x_factor
        self.y += y_factor
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        self.angle = math.atan2(self.y, self.x)

def calc_distance(vector_1, vector_2):
    x = vector_2.x - vector_1.x
    y = vector_2.y - vector_1.y

    return x ** 2 + y ** 2

def calc_angle(vector_1, vector_2):
    if vector_1.x == vector_2.x:
        if vector_2.y > vector_1.y:
            return math.pi
        else:
            return 0 - math.pi
    else:
        return math.atan2(vector_2.y - vector_1.y, vector_2.x - vector_1.x)
