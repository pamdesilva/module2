# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:26:17 2018

@author: pamde
"""

def f_to_c_formula(temp):
    return (int(temp) - 32) * 9/5

def convert_f_to_c(temp):
    convertedTemp = f_to_c_formula(temp)
    
    print(temp, "Fahrenheit is", convertedTemp, "Celsius")
    

def c_to_k_formula(temp):
    return temp + 273.15
    
def convert_c_to_k(temp):
    convertedTemp = c_to_k_formula(temp)
    
    print(temp, "Celsius is", convertedTemp, "Kelvin")
    
convert_f_to_c(70)
convert_c_to_k(32)