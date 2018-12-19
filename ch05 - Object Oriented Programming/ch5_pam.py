# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:37:09 2018

@author: pamde
"""

###############################################

#CHAPTER 05 - OBJECT ORIENTED PROGRAMMING

###############################################

#---------------------------------------
#TASK 1: Using clases
#---------------------------------------

import sys

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's account.
    """
    
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        else:
            self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
         """Return the balance remaining after depositing *amount* dollars."""  
         self.balance += amount
         return self.balance
     

pam = Customer('Pam De Silva', 30000.00)

pam.withdraw(1000.00)

print(pam.balance)

#---------------------------------------
#TASK 2 & 3: Using inheritance
#---------------------------------------


class Animal():
    def eat(self):
        print('yum')
        
class Dog(Animal):
    def bark(self):
        print('Woof!')
        
class Cat(Animal):
    def meow(self):
        print('Meow!')
        
snoopy = Dog()
snoopy.bark()
felix = Cat()
felix.meow()


############### Robot superclass

class Robot():
    def move(self):
        print('..move move move..')
        
############### House chore robots
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class CookRobot(Robot):
    def cook(self):
        print('I make rice')
        
############### Cook robots        
        
class SoupRobot(CookRobot):
    def makeTomatoSoup(self):
        print('I make tomato soup' )
            
#swishbot = CleanRobot()
#swishbot.move()
#swishbot.clean()
#
#stirbot = CookRobot()
#stirbot.move()
#stirbot.cook()
#
#soupbot = SoupRobot()
#soupbot.makeTomatoSoup()


################################# Cat game 
 
class Animal():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def eat(self):
         print('yum yum')
         
class Cat(Animal):
    def __init__(self, name, age=0, meowNumber=0):
        Animal.__init__(self, name, age=0)
        self.meowNumber = meowNumber
        
    def meow(self):
        print(self.name + ' Meow! ')
                
class CatAgent(Cat):
    
    def detectMeow(self):
        if self.meowNumber <= 3:
            print(self.name + ' wants cuddles!!')
        elif self.meowNumber >= 4 and self.meowNumber <= 6:
            print(self.name + ' wants attention')
        else:
            print(self.name + ' is hungry, feed it, human!')
            
        
#name = input('what is your cat\'s name:').title()        
#age = int(input('what is your cat\'s age: '))
#meow = int(input('how many times you heard it meow: '))
#
#cat001 = CatAgent(name, age, meow) #always inheritant ancester's
#cat001.meow()
#cat001.detectMeow()

#---------------------------------------
#TASK 4: Using association
#---------------------------------------

class SuperRobot():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Cat(name, age)
        self.o3 = CleanRobot()
        
    def playGame(self):
        print('alphago game')
        
    def move(self):
        return self.o1.move()
    
    def meow(self):
        return self.o2.meow()
    
    def clean(self):
        return self.o3.clean()
        
name = sys.argv[1]
age = sys.argv[2]
    
machineCat = SuperRobot(name, age)
machineCat.move()
machineCat.meow()
print(name, age)