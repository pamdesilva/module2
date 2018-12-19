# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:59:01 2018

@author: pamde

"""
###############################################

#CHAPTER 04 - CONDITIONALS

###############################################

#---------------------------------------
#TASK 3: IF statements
#---------------------------------------

number = input('Enter a number betwen 1 and 10:')
number = int(number)
if number > 10:
    print('Too high!')
if number <= 0:
    print('Too low!')
    
#---------------------------------------
#TASK 4: ELSE statements (cont' from above)
#---------------------------------------
#else:
    #print('Too low!')

#---------------------------------------
#TASK 4: ELIF statements 
#---------------------------------------

age = 20

if age < 13:
    print('child')
elif age < 18:
    print('teen')
elif age < 65:
    print('adult')
else:
    print('pensioner')


#---------------------------------------
#EXTRA: Dice game
#---------------------------------------

import random

def addition(a, b):
    return a + b

def checkVerdict(a, b):
    sum = addition(a, b)
    if sum >= 7:
        print("Both your dice rolls amount to " + str(sum) + ". Congrats! You win.")
    else:
        print("Both your dice rolls amount to " + str(sum) + ". Yikes! Better luck next time.")

def diceGame():
    print("Feeling lucky? Roll two dices and get 7 or more to win this game.")
    print('Roll your first dice by typing "roll" and hitting "enter"')
    input()
    numOne = random.randint(1, 6)
    diffOne = 7 - numOne
    if numOne <= 3:
        print("Uh-oh. " + "You got a " + str(numOne) + " .You're going to need at least " + str(diffOne) + " in the next roll to win."  )
    else:
        print("Nice! You got a " + str(numOne) + ". You only need " + str(diffOne) + " in the next roll to win.")
    print("Type 'roll' again and hit 'enter' to roll your second dice.")
    input()
    numTwo = random.randint(1, 6)
    print( "You got a " + str(numTwo) + ".")
    checkVerdict(numOne, numTwo)
    playAgain()  
    

def playAgain():
    print("Play again? y/n")
    playAgain = input()
    if(playAgain.lower() == 'y'):
        diceGame()
    else:
        print("Toodles, have a nice day!")
        
diceGame()
        
        
