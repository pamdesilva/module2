# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:46:15 2018

@author: pamde

"""
###############################################

#CHAPTER 03 - FUNCTIONS AND IMPORTING MODULES

###############################################

#---------------------------------------
#TASK 1: Function that prints 'Hello world'
#---------------------------------------

def print_hello_world():
    return 'Hello world'

#--------------------------------------------------------------
#TASK 2: Function that adds two numbers and returns the result
#--------------------------------------------------------------

def addition(num1, num2):
    sum = num1 + num2
    print(str(sum))
    return sum

#---------------------------------------------------------------------------
#TASK 3: Function which converts 'miles' to 'km' and returns the 'km' value
#---------------------------------------------------------------------------
    
def convert_distance(miles):
    kilometers = round(miles * 1.609, 2)
    print ("Converting distance in miles to kilometers")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    return kilometers
    
#-----------------------------------------------------------------------------------------------------------
#TASK 4: Function which converts 'centigrade' to 'fahrenheit' and 'kelvin' and returns the calculated values
#-----------------------------------------------------------------------------------------------------------

def c_to_f_formula(c):
    return c * 9.0 / 5.0 + 32
   
def c_to_k_formula(c):
    return c + 273.15

def convert_temp(temp, type):
    if type == "f":
        convertedTemp = c_to_f_formula(temp)
        print(temp, "Celsius is", convertedTemp, "Fahrenheit"  )
        return convertedTemp
    elif type == "k":
        convertedTemp = c_to_k_formula(temp)
        print(temp, "Celsius is", convertedTemp, "Kelvin")
        return convertedTemp
    else:
        return 'Unrecognised conversion'
        
       