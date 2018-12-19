# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:19:02 2018

@author: pamde
"""

####### Change user input to int. Input values are strings by default
#userInput = input('Please give me a number')
#result = int(userInput) - 2
#
#print(type(userInput))


####### Using breakpoints for debugging

userInput = input('Please give me a number')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2
result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)