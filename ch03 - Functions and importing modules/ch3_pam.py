# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:15 2018

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
#EXTRAS
#---------------------------------------
"""

def addition(num1, num2):
    return(str(num1 + num2))

def print_user_info():
    print('What\'s your name?')
    name = input()
    
    print('Enter a number')
    num_one = input()
    
    print('Enter another number')
    num_two = input()
    
    print("Hello " + name.title() + "!" + " Your lucky number is " + addition(int(num_one), int(num_two)))

def hello_world():
    print_user_info()
    
hello_world()
"""

"""
def sentence_4args(a, b): 
    print("{} {}".format(a, b))
    
arg1 = 'purple'
arg2 = 'unicorns'
arg3 = 'drink'
arg4 = 'apple juice'

sentence_4args(arg2, arg3)

sentence_4args(arg1, arg4)
"""

"""
def add_two_numbers():
    print(4 + 2)
    

def add_two_numbers_from_args(a, b):
    print(a + b)
    
add_two_numbers()
add_two_numbers_from_args(5, 3)
add_two_numbers_from_args(3, 4)

"""

"""
print(range(10))
print(range(1, 10))
print(range(1, 10, 15))

def range_test():
    for i in range(5, 10):
        print(i)
        
range_test()

"""



