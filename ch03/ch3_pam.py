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

##############Task2_2

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

################ Range function

"""
print(range(10))
print(range(1, 10))
print(range(1, 10, 15))

def range_test():
    for i in range(5, 10):
        print(i)
        
range_test()

"""

################ Mid class challenge

"""
def convert_distance(miles):
    kilometers = (miles id* 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    
convert_distance(15)
"""

################ Task 4

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

convert_temp(80, 'k')
convert_temp(29, 'f')
convert_temp(80, 'a')

################ Task 5

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer

test = add_two_numbers_and_return_value()
print(test)


