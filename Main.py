import math
import time
import turtle

import VectorMath as vm
from FieldObject import FieldObject as fo
from Environment import Environment as e

environment = e(.1)

environment.add_object(5, vm.Vector([1, 0]))
environment.add_object(5, vm.Vector([-1, 0]))

for i in range(100):
    environment.update()
    print(environment.objects[0].position.x)