from plane import Plane
from mathlib import *
from materials import *

class Pyramid(object):
  def __init__(self, arrayV3, material):
    self.arrayV3 = arrayV3
    self.material = material

  def side(self, v0, v1, v2, origin, direction):
    v0v1 = sub(v1, v0)
    v0v2 = sub(v2, v0)

    N = mul(cross(v0v1, v0v2),1)

    raydirection = dot(N, direction)

    if abs(raydirection) < 0.0001:
        return None
    
    d = dot(N, v0)
    t = (dot(N, origin) + d)/raydirection
    
    
    
    if t < 0:
      return None

    P = sum(origin, mul(direction, t))
    U, V, W = barycentric(v0, v1, v2, P)

    if U<0 or V<0 or W<0:
      return None
    else: 
      return Intersect(distance = d,
                      point = P,
                      normal = norm(N))
    edge0 = sub(v1, v0)
    vp0 = sub(P, v0)

    C = cross(edge0, vp0)

    nc = dot(N, C)
    if nc < 0:
      return None

    edge1 = sub(v2, v1)
    vp1 = sub(P, v1)

    C = cross(edge1, vp1)

    if dot(N, C) < 0:
      return None

    edge2 = sub(v0, v2)
    vp2 = sub(P, v2)

    C = cross(edge2, vp2)

    if dot(N, C) < 0:
      return None

    return Intersect(distance = (t / raydirection),
                     point = P,
                     normal = norm(N))


  def ray_intersect(self, origin, direction):
    v0, v1, v2, v3 = self.arrayV3
    planes = [
    self.side(v0, v3, v2, origin, direction),
    self.side(v0, v1, v2, origin, direction),
    self.side(v1, v3, v2, origin, direction),
    self.side(v0, v1, v3, origin, direction)
    ]


    t = float('inf')
    intersect = None

    for plane in planes:
        if plane is not None:
            if plane.distance < t:
                t = plane.distance
                intersect = plane

    if intersect is None:
        return None

    return Intersect(distance = intersect.distance,
                     point = intersect.point,
                     normal = intersect.normal)