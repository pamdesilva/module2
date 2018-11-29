# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:15 2018

@author: pamde
"""

##################################### userInput

"""
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

"""

##################################### functions

##############Task2


def print_user_info():
    print('What\'s your name?')
    name = input()
    
    print('Enter a number')
    num_one = input()
    
    print('Enter another number')
    num_two = input()
    
    print("Hello " + name.title() + "!" + " Your lucky number is " + addition(int(num_one), int(num_two)))

def addition(num1, num2):
    return(str(num1 + num2))

def hello_world():
    print_user_info()
    
hello_world()


##############Task2_2
"""
def hello_world_4args(a, b, c, d): 
    print("{} {} {} {}".format(a,b,c,d))
    
arg1 = 'purple'
arg2 = 'unicorns'
arg3 = 'drink'
arg4 = 'apple juice'

hello_world_4args(arg1, arg2, arg3, arg4)

"""

##############Task3

"""
def add_two_numbers():
    print(4 + 2)
    

def add_two_numbers_from_args(a, b):
    print(a + b)
    
add_two_numbers()
add_two_numbers_from_args(5, 3)
add_two_numbers_from_args(3, 4)

"""