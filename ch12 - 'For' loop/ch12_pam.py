# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:26:36 2018

@author: pamde
"""

###############################################

#CHAPTER 12 - THE 'FOR' LOOP

###############################################

#-----------------------------
#TASK 1: Loop through a list
#-----------------------------

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print(item)
    
#-----------------------------
#TASK 2: Update 'list' values
#-----------------------------

values = [875, 23, 451] 

for val in values:
    print('---->' + str(val + 50))
    

for val in values:
    print('---->', str(val * 2))
    
#----------------------------------------
#TASK 3: Create your own list and print
#----------------------------------------

for char in "Yes":
    print(list(char))
    
#----------------------------------------
#TASK 4: Loop through a string data type
#----------------------------------------
   
for char in "Yes and no".split():
    print(char)

#----------------------------------------
#TASK 5: Loop through tuple data type
#----------------------------------------

fruits = ('orange', 'banana', 'apple', 'kiwi', 'blueberries')
    
for item in fruits:
    print(item)
    
#-----------------------------------------------
#TASK 6 & 7: Loop through dictionary data type
#-----------------------------------------------

salaries = {'al': 20000, 'ced': 50000, 'bo': 1500}

employees = list(salaries.keys())

print(employees)

for employee in employees:
    print('{} = {}'.format(employee, salaries[employee]))    

products = {'iron' : (7.2, 0.93, 6000), 'gold': (19.3, 1.58, 26000), 'zinc': (6.5, 0.42, 15800), 'lead': (11.4, 0.75, 7300)}
metals = list(products.keys())

metals.sort()

for metal in metals:
    print('metal: {}, price: {}'.format(metal, products[metal][0]))

for k, v in sorted(products.items(), key = lambda kv:kv[1][1]):
    print(k, v[0])

#-------------------------------------------------------------------
#TASK 8: Combine counting loop and conditionals to filter out values
#-------------------------------------------------------------------
    
#print metals with densities larger than 8
    
for k, v in sorted(products.items(), key = lambda kv:kv[1][1]):
    if v[0] >= 8:
        print('Density larger than 8:', k, v[0])
    else:
        print('Density lower than 8:', k, v[0])
        
wishList = {'puppies': 3, 'kittens': 7, 'foxes': 2, 'lemurs': 8}

animals = list(wishList.keys())

for animal in animals:
    if wishList[animal] >= 3:
        print(animal, wishList[animal])
        
#------------------------------
#TASK 9: Design a sum function
#------------------------------

values = [3, 12, 9]
total = 0
for val in values:
    total += val
    print('TOTAL:' + str(total))
    
def sumValues(l):
    sumV = 0
    for item in l:
        sumV += item
    return sumV

print(sumValues(values))
    
#-------------------------------
#TASK 10: Loop with index values
#-------------------------------

def multiplyValues(m):
    for i in range(len(values)):
        values[i] = values[i] * m
    return values

print(multiplyValues(3))

    
#---------------------------------
#TASK 11: Loop with range function
#---------------------------------

def printRange(a, b, c):
    for i in range(a, b, c):
        print(i)    
    
printRange(1, 9, 3)
printRange(3, 10, 2)
printRange(4, 10, 2)

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for i in range(0, len(names), 3):
    print(names[i])

#---------------------------------
#TASK 12: Using 'break in for loops
#---------------------------------

nums = [2, 32, 65, 23, 123, 432, 3]  

for n in nums:
    if n > 100:
        print('found:', n)
        break   
    
for index in range(len(nums)):
    if nums[index] > 60:
        print('break at:', nums[index])
        break

#-----------------------------------------------
#TASK 13: Creating nested loops in a for loop
#-----------------------------------------------

outer_vals_list = [1, 2, 3]
inner_vals_list = ['A', 'B', 'C']
d = {}

for outer_val in outer_vals_list:
    print(outer_val)
    for inner_val in inner_vals_list:
        print(outer_val, inner_val)
        d[outer_val] = inner_val
print(d)


for i in range(1, 7):
    for j in range(1, 11):
        print('{0: > 3}'.format(i * j), end='')
    print('\n')

#---------------------------------------------
#TASK 14: Multiplication using a 'for' loop
#---------------------------------------------
    
for i in range(1, 11):
    for j in range(1, 11):
        print('{0: > 3}'.format(i * j), end='')
    print('\n')