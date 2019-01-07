# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:13:04 2019

@author: pamde
"""

###############################################

#CHAPTER 13 - MORE ON OOP

###############################################

#------------------------------------
#TASK 1: Initialise the person class
#------------------------------------

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised!')
            
    def greetingInformal(self):
        print('Hi', self.name)
    
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.name)
        else:
            print('Welcome, Ms', self.name)

#--------------------------
#TASK 3: A greeting filter
#--------------------------
            
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young', self.name)
        elif self.age > 60:
            print('Welcome, venerable', self.name)
        else:
            self.greetingFormal()


p1 = Person('John', 44, 'm')
print(p1.name)
print(p1.isMale)

p1.greetingAgeBased()

#----------------------------------------------------
#TASK 2: More functionalities for the Person class
#----------------------------------------------------

p1 = Person('Harry', 12, 'm')
p2 = Person('Jean', 12, 'f')
p1.greetingInformal()

p1.greetingFormal()
p2.greetingFormal()


#----------------------------------------------------
#TASK 4: Create a subsclass for the Person class
#----------------------------------------------------

class Wizard(Person):
    def geetingFormal(self):
        print('Welcome, Mr', self.name, end=' ')
        print('- you\'re a fine wizard!')
        
p1 = Wizard('Harry', 12, 'm')

