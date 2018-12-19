# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:54:34 2018

@author: pamde
"""
###############################################

#CHAPTER 03 - FUNCTIONS AND IMPORTING MODULES

###############################################

#---------------------------------------
#TASK 1: Input from user
#---------------------------------------

print('What\'s your name?')
name = input().title()

#name
#print("Hello {}!".format(name.title()))

#age
print('What\'s your age?')
age = input()

#location
print('Where do you come from?')
location= input()

print("Hello " + name + "! You are " + age +  ' years old. You come from ' + location + '.' )

#---------------------------------------
#Importing functions from an external file
#---------------------------------------

import ch3_pam_function as helpers

helpers.convert_temp(80, 'k')
helpers.convert_temp(29, 'f')
helpers.convert_temp(80, 'a')

helpers.convert_distance(15)

helpers.addition(2, 6)

