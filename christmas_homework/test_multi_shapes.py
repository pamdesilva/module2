# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:53:06 2018

@author: pamde
"""

from MovingShapes import *

frame = Frame()
numshapes = 3
shapes = []
size = 60

for i in range(numshapes):
    shapes.append(Square(frame, size))
    shapes.append(Circle(frame, size))
    shapes.append(Diamond(frame, size))
    
for i in range(100):
    for shape in shapes:
        shape.moveTick()
        