from mathlib import *
from dataclasses import dataclass

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Light(object):
  def __init__(self, position=V3(0,0,0), intensity=1):
    self.position = position
    self.intensity = intensity

class Material(object):
  def __init__(self, diffuse=WHITE, albedo=(1, 0, 0, 0), spec=0, refractive_index = 1):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refractive_index = refractive_index

class Intersect(object):
  def __init__(self, distance, point, normal):
    self.distance = distance
    self.point = point
    self.normal = normal

#materiales
gray = Material(diffuse=color(184, 182, 179), albedo=(0.6, 0.3, 0, 0, 0), spec=10)
coffee = Material(diffuse=color(71, 51, 10), albedo=(0.6,  0.3, 0, 0, 0), spec=10)
green = Material(diffuse=color(28, 110, 47), albedo=(0.9,  0.9, 0, 0), spec=60)
yellow = Material(diffuse=color(230, 225, 60), albedo=(0.8,  0.8, 0, 0), spec=55)
lightGreen = Material(diffuse=color(0, 255, 0), albedo=(0.9,  0.9, 0, 0), spec=60, refractive_index=0.2)
