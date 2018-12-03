# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:46:15 2018

@author: pamde

"""


def convert_distance(miles):
    kilometers = round(miles * 1.609, 2)
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)


def c_to_f_formula(c):
    return c * 9.0 / 5.0 + 32
   
def c_to_k_formula(c):
    return c + 273.15

def convert_temp(temp, type):
    if type == "f":
        convertedTemp = c_to_f_formula(temp)
        print(temp, "Celsius is", convertedTemp, "Fahrenheit"  )
    elif type == "k":
        convertedTemp = c_to_k_formula(temp)
        print(temp, "Celsius is", convertedTemp, "Kelvin")
    else:
        print('Unrecognised conversion')
        
        
def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print(answer)
       