# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:52:30 2018

@author: pamde
"""

def DataBundlePurchase(truePasscode, balance):
   if checkPassword(truePasscode):
       print('Welcome!')
       showOptions(balance)
   else:
       passwordRetry(truePasscode, balance)
   
def checkPassword(truePasscode):
    attempt = input('Please enter your password:')
    if attempt == truePasscode:
        return True
    else:
        return False


################ Lets user attempt to input correct password two more times ################
def passwordRetry(truePasscode, balance):
    print('Sorry, the password you entered is incorrect. Please try again - you have 2 tries left.')
    if checkPassword(truePasscode):
        print('Welcome!')
        showOptions(balance)
    else:
        print('Sorry, the password you entered is incorrect again. Please try again - you have 1 try left.')
        if checkPassword(truePasscode):
            print('Welcome!')
            showOptions(balance)
        else:
            print('Sorry! You\'ve used up your 3 tries. Your account has been temporarily locked. Please try again in an hour.')     


################ Displays transaction options based on user input ################          
def showOptions(balance):
    print('Type "1" to check your credit balance')
    print('OR')
    print('Type "2" to purchase more data')
    response = input()
    if response == '1':
        showBalance(balance)
    elif response == '2':
        if checkBalance(balance):
            print('Before you can purchase data, you\'ll need to validate your phone number.')
            checkNumber()
            purchaseData(balance)
        else:
            print('Sorry, this service is unavailable as you have insufficient credit.')
            showBalance(balance)
            print('You need at least $5 to purchase more data.')  
    else:
        print('Sorry, we don\'t recognise the option you\'ve entered. Please try again.')
        showOptions(balance)


################ Checks is user has a balance of more than $0 ################     
def checkBalance(balance):
    if balance >= 5:
        return True
    else:
        return False
    
    
################ Displays the user's credit balance ################         
def showBalance(balance):
    print('Your current balance is: $' + str(balance))
 
    
################ Validates user's phone number ################     
def checkNumber():
    numOne = input('Please enter your mobile number:')
    numTwo = input('Please enter your mobile number again:')
    
    if numOne == numTwo:
        return True
    else:
        print('The two mobile numbers you entered didn\'t match. Please enter them again.')
        checkNumber()


################ Runs conditionals for buying more data ################             
def purchaseData(balance):
    showBalance(balance)
    print('How much credit would you like to spend for more data?')
    amount = int(input())
    if amount < balance:
        if amount > 100:
            print('Sorry, you can only purchase $100 of data at a time.')
            purchaseAgain(balance)
        else:    
            if amount % 5 == 0:
                newBalance = round(balance - int(amount), 2)
                print('You\'ve successfully added $' + str(amount) + ' of data to your mobile plan. Your new balance is $' + str(newBalance))
            else:
                print('Sorry. You can only purchase data in increments of $5 (eg. $5, $10, $15, $20). Please enter a new amount.')
                purchaseData(balance)
    if amount > balance:
        print('Sorry, you do not have sufficient credit for that amount.')
        purchaseAgain(balance)           
 
    
################ Gives user the option to buy more data again if previous attempt was unsuccessful ################     
def purchaseAgain(balance):
    chooseLower = input('Would you like to purchase a lower amount? y/n')
    if chooseLower == 'y':
        purchaseData(balance)
    else:
        print('Thanks and have a nice day!')
        
    