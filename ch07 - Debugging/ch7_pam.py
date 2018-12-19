# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:19:02 2018

@author: pamde
"""
###############################################

#CHAPTER 07 - DEBUGGING

###############################################

#---------------------------------------
#TASK 1: Debugging using 'print' function
#---------------------------------------

####### Change user input to int. Input values are strings by default
userInput = input('Please give me a number')
result = int(userInput) - 2

print(type(userInput))


#---------------------------------------
#TASK 2: Using breakpoints for debugging
#---------------------------------------

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

## debugging using breakpoints 
#1) double click next to the line number of your code to set up a breakpoint,a red circle should
#appear 
#2)you can now run your code in debug mode using debugging buttons on the toolbar
#  - first button is for you to start running your code until the break point.
#  - second button allows you to run your code line-by-line until the breakpoint.
#  - third one is for stepping into the sections (class and functions) 
#  - fourth button is for you to step out when you feel that the error is not related to the current section
#  - fifth button is for you to go to the next breakpoint
#  - last, square shaped button is for you to exit debugging mode and go back to normal coding mode.