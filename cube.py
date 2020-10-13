from mathlib import *
from materials   import *
from plane import Plane 

class Cube(object):
  def __init__(self, position, size, material):
    self.position = position
    self.size = size
    self.material = material
    self.planes = []

    halfSize = size / 2
    #Se crean las 6 paredes del cubo con planos
    self.planes.append( Plane( sum(position, V3(halfSize,0,0)), V3(1,0,0), material))
    self.planes.append( Plane( sum(position, V3(-halfSize,0,0)), V3(-1,0,0), material))

    self.planes.append( Plane( sum(position, V3(0,halfSize,0)), V3(0,1,0), material))
    self.planes.append( Plane( sum(position, V3(0,-halfSize,0)), V3(0,-1,0), material))

    self.planes.append( Plane( sum(position, V3(0,0,halfSize)), V3(0,0,1), material))
    self.planes.append( Plane( sum(position, V3(0,0,-halfSize)), V3(0,0,-1), material))


  def ray_intersect(self, orig, direction):

    epsilon = 0.001
    
    #bbox
    minLimits = [0,0,0]
    maxLimits = [0,0,0]

    for i in range(3):
      minLimits[i] = self.position[i] - (epsilon + self.size / 2)
      maxLimits[i] = self.position[i] + (epsilon + self.size / 2)



    t = float('inf')
    intersect = None

    for plane in self.planes:
      intersectPlane = plane.ray_intersect(orig, direction)

      if intersectPlane is not None:
        if intersectPlane.point[0] >= minLimits[0] and intersectPlane.point[0] <= maxLimits[0]:
          if intersectPlane.point[1] >= minLimits[1] and intersectPlane.point[1] <= maxLimits[1]:
            if intersectPlane.point[2] >= minLimits[2] and intersectPlane.point[2] <= maxLimits[2]:
              if intersectPlane.distance < t:
                t = intersectPlane.distance
                intersect = intersectPlane

    if intersect is None:
      return None

    return Intersect(distance = intersect.distance,
                     point = intersect.point,
                     normal = intersect.normal)