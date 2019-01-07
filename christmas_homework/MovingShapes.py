# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:27:57 2018

@author: pamde
"""

from Shapes import *
import random
import math

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.frame = frame
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.minxy = self.diameter/2
        self.maxx = self.frame.width - self.minxy
        self.maxy = self.frame.height - self.minxy
        self.x = random.randrange(self.minxy, self.maxx + 1)
        self.y = random.randrange(self.minxy, self.maxy + 1)
        self.dx = 1 + 10 * random.random()
        self.dy = 1 + 10 * random.random()
        self.goto(self.x, self.y)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
        
    def moveTick(self):
        if self.x > self.maxx:
            self.dx = (1 - 10) * random.random()
        elif self.x < self.minxy:
            self.dx = (1 + 10) * random.random()
        else:
            pass       
        
        self.x += self.dx
        
        if self.y > self.maxy:
            self.dy = (1 - 10) * random.random()
        elif self.y < self.minxy:
            self.dy = (1 + 10) * random.random()
        else:
            pass
        
        self.y += self.dy
        
        self.figure.goto(self.x, self.y)
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        self.minxy = self.diameter * math.sqrt(2) / 2
        self.maxx = self.frame.width - self.minxy
        self.maxy = self.frame.height - self.minxy
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        
