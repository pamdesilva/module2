# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:48 2018

@author: pamde
"""

###############################################

#CHAPTER 09 - LISTS & TUPLES

###############################################

#---------------------------------------
#TASK 1: Create a list
#---------------------------------------

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]

print(x[0])
print(x[1])
print(x[3][0])
print(x[-1])
print(x[-1][-2])
print(x[-2][-3])

#---------------------------------------
#TASK 2: Modify the list
#---------------------------------------

x.remove(my_favourite_fruits)
print(x)

x[1] = 'and'
print(x)

x.append('again')
print(x)

x.append('muffins')
print(x)

y = x
print(y)

y = x.append('cupcakes')
print(y)
print(x)

#---------------------------------------
#TASK 3: Slicing the list
#---------------------------------------

x = ['the', 'cat', 'sat', 'directly']
y = ['on', 'the', 'wet', 'mat']
z = x + y
print(x[0:3])
print(y[1:4])
print(z)
print(x)
print(z[-1])

#---------------------------------------
#TASK 4: Sorting the list
#---------------------------------------

######## List operations: sort

x = ['the', 'cat', 'sat', 'directly']
y = ['on', 'the', 'wet', 'mat']
z = sorted(x)
print(z)
print(x)

t = y.sort()
print(t)
print(y)


######## List operations: reverse sort

x = [7, 11, 3, 9, 2]
print(sorted(x))

print(sorted(x, reverse=True))

print(x)

y = [9, 4, 10, 29, 12]

z = y.sort()
print('now z is: ', z)
print('now y is: ', y)
y.sort(reverse=True)
print('now y is: ',y)

#-----------------------------------------------------
#TASK 5: Create a tuple and compare tuples with lists
#-----------------------------------------------------

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#del a[3]
#print(a)
#a[3] = 50
#print(a)
#a.append('z')
#print(a)

######## Tuples : immutable
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
##print(type(b))
##del b[3]
##print(b)
##b[3] = 50
##print(b)
#print('b is: ', b)
#c = list(b)
#print('c is now: ', c)


#-----------------------------------------------------
#TASK 6: Using lambda functions to sort a list
#-----------------------------------------------------

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

#---------------------------------------
#EXTRAS
#---------------------------------------

######## List operations: + *

z = ['zs', 'yw', 'hd' 'cs', 'ab']
#x = ['the', 'cat', 'sat']
#y = ['on', 'the', 'mat']
#z = x + y
#print(z)
#z = x * 3
#print(z)
#print(type(z))
#a = set(x + y)
#print(a)
#print(type(a))
#print(x)
#print(y)
