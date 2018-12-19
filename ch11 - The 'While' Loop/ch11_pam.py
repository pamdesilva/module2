# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:00:18 2018

@author: pamde
"""

###############################################

#CHAPTER 11 - THE 'WHILE' LOOP

###############################################

#-----------------------------
#TASK 1: Repeat division
#-----------------------------

x = 33
while x >= 1:
    print(x, ': ', end='')
    x = x / 2
print(x)

#-----------------------------
#TASK 2: Triangular numbers
#-----------------------------

def triangular(n):
    trinum = 0
    while n > 0:
        trinum = trinum + n
        n = n - 1
    return trinum

triangular(1)
triangular(3)
triangular(5)

#-----------------------------
#TASK 3: Students marks
#-----------------------------

mark = 1
while mark > 0:
    mark = input('Enter mark: ')
    mark = int(mark)
    print("Mark is", mark, end='')
    if mark >= 70:
        print(" - first class!")
    elif mark >= 40:
        print(" - that's a pass")
    else:
        print(" - that's a fail")
        
#----------------------------------------------------------
#TASK 4: Using the break statement in a while loop
#----------------------------------------------------------

while True:
    name = input('Enter name: ')
    if name.lower() == 'done':
        break
    print('Hello', name.title())


#-----------------------------
#TASK 5: Guessing number game
#-----------------------------

from random import randint

def guess(attempts, intrange):
    number = randint(1, intrange)
    print("Welcome! Can you guess my secret number? ")
    
    while attempts > 0:
        print("You have", attempts, "attempts left.")
        guess = int(input("Take a guess! "))
        
        if guess > number:
            print("No, too high!")
            attempts = attempts - 1
        elif guess < number:
            print("No, too low!")
            attempts = attempts - 1
        else:
            print("Well done. You got it right!")
            break
        
    print("Game over. Thanks for playing.")
        
guess(4, 10)    