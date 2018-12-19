# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:20:15 2018

@author: pamde
"""

import time

def apply_for_leave(person):
    print('Hi ' + person.firstName.title() + '! You have ' + str(person.vacationDays) + ' days of holiday remaining. Please type the number of days would you like to take?')
    leave_requested = input()
    
    if int(leave_requested) > 5 :
        print('Thanks for your request, ' + person.firstName.title() + '. Because it\'s more than 5 days, it will require further approval.' )
        reapply_leave(person)
    else:
        print('Yay, ' + person.firstName.title() + '. Your request has been approved. Happy holidays to you!' )
        person.vacationDays -= int(leave_requested)
        print('You now have ' + str(person.vacationDays) + ' days of holiday left this year.') 
        
def reapply_leave(person):
    print('Type "p" to proceed with your request | Type "y" to reapply for 5 days or less | Type "c" to cancel this leave application.')
    reapply = input().lower()
    
    if reapply == 'y':
        apply_for_leave(person)   
    elif reapply == 'p':
        print('Your request has been submitted. We will get back to you within 3 working days at ' + person.email)    
    else:
        print('Thanks and have a nice day!')
        

class Employee():
    def __init__(self, firstName, lastName, employeeId, vacationDays):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@company.com'
        self.employeeId = employeeId
        self.vacationDays = vacationDays
        
    def employee_info(self):
        print('First name: ' + self.firstName + '\n' + 'Last name: ' + self.lastName + '\n' + 'Email: ' + self.email + '\n' + 'Employee Id: ' + str(self.employeeId))
        
    def apply_for_leave_flow(self):
        apply_for_leave(self)

            
def printBalanceString(expense):
    print('You have £' + str(expense) + ' left in your client expenditure account this month.')  
        

class Employee_management(Employee):
    def __init__(self, firstName, lastName, employeeId, vacationDays, clientExpenses):
        Employee.__init__(self, firstName, lastName, employeeId, vacationDays)
        self.clientExpenses = clientExpenses
    
    def claim_client_expenses(self):
        print('Hi ' + self.firstName.title() + '! You have £' + str(self.clientExpenses) + ' left in your client expense account. Please type the amount you would like to claim. ')
        claim_amount = int(input())
        claim_limit = 0.9 * self.clientExpenses
        claim_limit_half = 0.5 * self.clientExpenses
        if claim_amount >= claim_limit and claim_amount < self.clientExpenses:
            time.sleep(1)
            print('Thanks, ' + self.firstName.title() + '. Your claims request is being processed.')
            time.sleep(1)
            print('You\'ve nearly reached your monthly client expenditure limit.')
            self.clientExpenses -= int(claim_amount)
            time.sleep(1)
            printBalanceString(self.clientExpenses)
        elif claim_amount > claim_limit_half and claim_amount < claim_limit:
            time.sleep(1)
            print('Thanks, ' + self.firstName.title() + '. Your claims request is being processed.')
            time.sleep(1)
            print('You have reached more than half of your monthly client expenditure.')
            self.clientExpenses -= int(claim_amount)
            time.sleep(1)
            printBalanceString(self.clientExpenses)
        elif claim_amount == self.clientExpenses:
            time.sleep(1)
            print('Thanks, ' + self.firstName.title() + '. Your claims request is being processed.')
            time.sleep(1)
            print('You have reached your limit for the month and will no longer be able to make any more claims till next month.')
        else:
            self.clientExpenses -= claim_amount
            printBalanceString(self.clientExpenses)

      
dwight = Employee('dwight', 'schrute', 3, 10)
michael = Employee_management('michael', 'scott', 1, 30, 1000) 

dwight.employee_info()
print('\n')
dwight.apply_for_leave_flow()
print('\n')
michael.claim_client_expenses()       
