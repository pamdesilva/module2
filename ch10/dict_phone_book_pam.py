# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:15:50 2018

@author: pamde
"""

def addClassmateToPhoneBook(phoneBook):
    name = input('What\'s the new classmate\'s name :' )
    lastThree = input('What\'s the last 3 digits of the new classmate\'s phone number :' )
    luckyNum = input('What\'s the new classmate\'s lucky number :' )
    postcode = input('What\'s the new classmate\'s postcode:' )
    town = input('What\'s the name of the new classmate\'s town:' )
    age = input('What\'s the new classmate\'s age:' )
    
    phoneBook[name.title()] = lastThree, int(luckyNum), postcode.upper(), town.title(), int(age)
    
    print('\nPhone book has ben updated with new classmate, ' + name.title(), ':\n', phoneBook, '\n')
    
    return phoneBook

def sortPhoneBookByName(phoneBook):
    sortByNamePair = sorted(phoneBook.items(), key = lambda kv:kv[0])
    print('\nPhone book sorted by names in alphabetical order:\n', sortByNamePair, '\n')

def sortPhoneBookByTown(phoneBook):
    sortByTown = sorted(phoneBook.items(), key = lambda kv:kv[1][3])
    print('\nPhone book sorted by towns in alphabetical order:\n', sortByTown, '\n')
    
def sortPhoneBookByLuckyNum(phoneBook):
    sortByLuckyNum = sorted(phoneBook.items(), key = lambda kv:kv[1][1])
    print('\nPhone book sorted by lucky numbers:\n', sortByLuckyNum, '\n')
    
def sortPhoneBookByAge(phoneBook):
    sortByAge = sorted(phoneBook.items(), key = lambda kv:kv[1][4])
    print('\nPhone book sorted by age:\n', sortByAge, '\n')

def runSortChoices(phoneBook):
    print('What would you like to sort the phone book by?')
    print('Type "n" to sort by name')
    print('Type "a" to sort by age')
    print('Type "t" to sort by town')
    print('Type "l" to sort by lucky number')
    response = input()
    if response == 'n':
        sortPhoneBookByName(phoneBook)
        runSortChoicesAgain(phoneBook)
    elif response == 't':
        sortPhoneBookByTown(phoneBook)
        runSortChoicesAgain(phoneBook)
    elif response == 'l':
        sortPhoneBookByLuckyNum(phoneBook)
        runSortChoicesAgain(phoneBook)
    elif response == 'a':
        sortPhoneBookByAge(phoneBook)
        runSortChoicesAgain(phoneBook)
    else:
        print('Sorry "' + response + '" is not an option. Let\'s try again.' )
        runSortChoices(phoneBook)
        
def runSortChoicesAgain(phoneBook):
    print('Would you like to sort the phone book again? (y/n)')
    response = input()
    if response == 'y':
        runSortChoices(phoneBook)
    else:
        returnToMainMenu()
        
def calculateQueensAgeDiff(phoneBook):
    print('Type a classmate to compare ages with the Queen:')
    namesList = list(sorted(phoneBook))
    print(namesList)
    classmate = input().title()
    diff = 92 - phoneBook[classmate][4]
    print('The difference between ' + classmate + '\'s age and the Queen\'s age is', diff, 'years.' )
    
def returnToMainMenu():
    print('Would you like to return to the main menu? (y/n)')
    response = input()
    if response == 'y':
        phoneBook()
    else:
        print('You have exited the phone book program. Good day to you.')
        
def printPhoneBookToFile(phoneBook):
    f = open('phoneBook.txt', 'w')
    f.write(str(phoneBook))
    f.close()
    
def phoneBook():
    phoneBook = phoneBook_dict
    print('Welcome to the phone book. What would you like to do today?')
    print('\nType "c" to add a classmate')
    print('Type "s" to sort the phone book')
    print('Type "q" to compare a classmate\'s age with the Queen\'s')
    print('Type "p" to print classmates details in an external file')
    print('Type "x" to exit the program')
    response = input()
    if response == 'c':
        addClassmateToPhoneBook(phoneBook)
        returnToMainMenu()
    elif response == 's':
        runSortChoices(phoneBook)
    elif response == 'q':
        calculateQueensAgeDiff(phoneBook)
        returnToMainMenu()
    elif response == 'p':
        printPhoneBookToFile(phoneBook)
        print('Your fle has been printed.')
        returnToMainMenu()
    elif response == 'x':
        print('You have exited the phone book program. Good day to you.')
    else:
        print('Sorry "' + response + '" is not an option. Let\'s try again.' )
        phoneBook()
        
phoneBook_dict = {'Pam': ('075', 7, 'BR5 7PL', 'Beckenham', 30),
                  'Kate': ('831', 2, 'BR8 3QV', 'Birmingham', 23),
                  'Muna': ('380', 5, 'LT5 2HP', 'Archway', 25),
                  }
    
phoneBook()  



