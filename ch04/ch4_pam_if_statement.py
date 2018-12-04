# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:23:51 2018

@author: pamde
"""

number = input("Enter a number between 1 and 10")
number = int(number)

if number > 10:
    print("Too high!")

elif number <= 0:
    print("Too low!")

else:
    print("Thanks!")
    
age = 10
    
if age < 13:
    print('child')
elif age < 18:
    print('teen')
elif age < 65:
    print('adult')
else:
    print('pensioner')