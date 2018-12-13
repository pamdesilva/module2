# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:48:17 2018

@author: pamde
"""

my_favourite_fruits = ['apple', 'orange', 'banana']
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
x = ['aha', 'zsb', 'csa' 'hdf', 'abw']
y = ['aeb', 'csr', 'hdb' 'yww', 'zsr']
z = ['zsn', 'yww', 'hde' 'csa', 'abe']

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

arranged = sorted(x2, key=lambda s:s[2][1])

print(arranged)

z[0] = 'pd'
y[-2] = 'cw'

x3 = [('d', 9, z), ('c', 6, y), ('r', 5, x)]

print(sorted(x3, key=lambda s:s[2][1][-3]))
