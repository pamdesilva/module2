# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:27:57 2018

@author: pamde
"""

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.x = 0
        self.y = 0
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        self.goto(self.x, self.y)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
        
    def moveTick(self):
        self.x += self.dx
        self.y += self.dy
        self.figure.goto(self.x, self.y)
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        
