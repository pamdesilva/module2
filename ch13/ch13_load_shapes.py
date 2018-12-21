# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:02:36 2018

@author: pamde
"""

from Shapes import *

frame = Frame()
s1 = Shape('square', 100)
s1.goto(200, 100)

s2 = Shape('circle', 100)
s2.goto(200, 100)

x = 0
y = 0

for i in range(100):
    s1.goto(x, y)
    x = x + 5
    y = y + 5
