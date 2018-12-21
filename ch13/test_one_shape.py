# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:35:49 2018

@author: pamde
"""

from MovingShapes import *

frame = Frame(300, 300)
shape1 = Square(frame, 100)
shape2 = Circle(frame, 100)

for i in range(100):
    shape1.moveTick()
    
