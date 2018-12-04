# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:59:01 2018

@author: pamde

"""

import random

  
def addition(a, b):
    return a + b

def randomNum():
    for x in range(10):
        return random.randint(1,6)

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
    numOne = randomNum()
    diffOne = 7 - numOne
    if numOne <= 3:
        print("Uh-oh. " + "You got a " + str(numOne) + " .You're going to need at least " + str(diffOne) + " in the next roll to win."  )
    else:
        print("Nice! You got a " + str(numOne) + ". You only need " + str(diffOne) + " in the next roll to win.")
    print("Type 'roll' again and hit 'enter' to roll your second dice.")
    input()
    numTwo = randomNum()
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
        
        
