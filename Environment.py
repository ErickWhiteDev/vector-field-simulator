from FieldObject import FieldObject as fo

class Environment:

    g = 0
    mass = 0

    objects = []

    def __init__(self, g):
        self.g = g
    
    def add_object(self, mass, position):
        field_object = fo(mass, position)
        self.objects.append(field_object)
        self.mass += mass
    
    def update(self):
        for i in self.objects:
            i.move(self)