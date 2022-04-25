import math
from os import environ
import VectorMath as vm

class FieldObject:

    mass = 0
    radius = 0
    position = vm.Vector([0,0])
    velocity = vm.Vector([0,0])
    acceleration = vm.Vector([0,0])
    force = vm.Vector([0,0])

    def __init__(self, mass, position):
        self.mass = mass
        self.position = position
        self.radius = math.sqrt(mass)

    def calc_force(self, environment):
        x, y = 0, 0
        g = environment.g
        force = 0

        for i in environment.objects:
            target_vector = i.position
            target_mass = i.mass
            distance = vm.calc_distance(self.position, target_vector)

            if vm.calc_distance(self.position, target_vector) > .2:
                force += (g * self.mass * target_mass) / distance ** 2

                x += force * math.cos(vm.calc_angle(self.position, target_vector))
                y += force * math.sin(vm.calc_angle(self.position, target_vector))
            else:
                self.mass += target_mass
                self.radius = math.sqrt(self.mass)
                self.position.modify_by_components(target_vector.x - self.position.x, target_vector.y - self.position.y)
                environment.objects.remove(i)
        
        return vm.Vector([x, y])
    
    def move(self, environment):
        self.force = self.calc_force(environment)
        self.acceleration = self.force
        self.acceleration.modify_by_magnitude(1 / self.mass)
        self.velocity.modify_by_components(self.acceleration.x, self.acceleration.y)
        self.position.modify_by_components(self.velocity.x, self.velocity.y)
