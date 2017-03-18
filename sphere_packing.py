#!/home/justin/opt/blender-2.78c-linux-glibc219-x86_64/2.78/python/bin/python3.5m 
import sys
sys.path.append('.')
from mathutils import Vector
from mathutils import noise
import base

class Packer:

    GROWTH_RATE = 0.1

    def __init__(self, location):
        self.location = location
        self.radius = 0
        self.active = True

    def grow(self):
        if self.active:
            self.radius += self.GROWTH_RATE

    def check_collision(self, others):
        for other in others:
            distance = (self.location - other.location).magnitude \
                        - self.radius - other.radius
            if distance < 0 and not other is self:
                self.active = False

    def render(self):
        base.sphere(location=self.location,
                    size=self.radius)


class PackerManager():

    N = 1000

    def __init__(self):
        self.bodies = []
        for i in range(self.N):
            self.bodies.append(Packer(10*noise.random_unit_vector()))

    def run(self):
        for body in self.bodies:
            if not body.check_collision(self.bodies):
                body.grow()

    def still_active(self):
        return any([body.active for body in self.bodies])

if __name__ == '__main__':

    manager = PackerManager()

    while manager.still_active():
        print('running')
        manager.run()
        
    for body in manager.bodies:
        body.render()
