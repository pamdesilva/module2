# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:51:55 2018

@author: pamde
"""

###############################################

#CHAPTER 10 - DICTIONARIES

###############################################

#------------------------------------------------------------------------------
#TASK 1 & 2: Create a dictionary for which you can assign, retrieve and update values
#------------------------------------------------------------------------------
print('\nTask 1:')
x = {
     'bo': 5000, 
     'al': 20000, 
     7:('Joke', 'Chen', 'Bond')
     }

salary = {}

salary['al'] = 20000
salary['pam'] = 100000

print(salary)

salary['pam'] = 550000

print(salary)

salary['al'] += 1000

print(salary)


print('\nTask 2:')

phoneNumbers = {
        'dipsy' : 455,
        'lala': 323,
        'poe': 878

        }

print(phoneNumbers)

#--------------------------------------
#TASK 3: Look up and delete values
#--------------------------------------
print('\nTask 3:')

phoneNumbers['dipsy'] = 6455
phoneNumbers['lala'] = 7323
phoneNumbers['poe'] = 6878
phoneNumbers['tinky winky'] = 6352

print(phoneNumbers)

del phoneNumbers['poe']

print(phoneNumbers)

#This will return an error
#del phoneNumbers[1]

print(phoneNumbers)


#--------------------------------------------------------
#TASK 4: Retrieving keys and values from a dictionary
#--------------------------------------------------------
print('\nTask 4:')

print(phoneNumbers.keys())
print(phoneNumbers.values())

#--------------------------------------------------------
#TASK 5: Convert keys and value to a list data type
#-------------------------------------------------------- 

print('\nConvert key or value to list:')
print(list(phoneNumbers.keys())[0])

#--------------------------------------------------------
#TASK 6: Avoiding key errors
#-------------------------------------------------------- 

print('\nCheck if a key exists in a dictionary:')
k = 'eric'
if k in phoneNumbers:
    print(k, ':', phoneNumbers[k])
else:
    print(k, 'not found!')
    
#--------------------------------------------------------
#TASK 7 & 8: Sorting a dictionary
#-------------------------------------------------------- 
    
print('\nSorting a dictionary:')
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
labels.sort(key=lambda k:counts[k])
print(labels)


print('\nSorting exercise with sort():')
students = {'kate' : (3, 14), 'pam': (5, 7), 'amina' : (2, 4), 'leanne': (9, 26)}

studentsList = list(students.keys())

studentsList.sort(key = lambda m:students[m][0])
print('\nSort by month:')
print(studentsList)

studentsList.sort(key = lambda l:students[l][1])
print('\nSort by lucky number:')
print(studentsList)

print('\nSorting exercise with sorted():')

byMonth = sorted(studentsList, key = lambda m:students[m][0])
print('\nSort by month:')
print(byMonth)

byLuckyNumber = sorted(studentsList, key = lambda l:students[l][1])
print('\nSort by lucky number:')
print(byLuckyNumber)


byMonthPair = sorted(students.items(), key = lambda kv:kv[1][0])
print(byMonthPair)

byLuckyNumberPair = sorted(students.items(), key = lambda kv:kv[1][1])
print(byLuckyNumberPair)

print('\nDictionary application:')

densities = {'iron' : 7.8, 'gold': 19.3, 'zinc': 7.13, 'lead': 11.4}
metals = list(densities.keys())

metals.sort(reverse = True, key = lambda m:densities[m])
print('Metals sorted by descending names: ', metals)

sortKv = sorted(densities.items(), key = lambda kv:kv[0], reverse = True)
print('Sort metal names in kv pairs: ', sortKv)

densityKv = sorted(densities.items(), key = lambda kv:kv[1], reverse=True)
print('Sort metals in kv pairs by density:', densityKv)

print('\n')

products = {'iron' : (7.8, 0.93, 6000), 'gold': (19.3, 1.58, 26000), 'zinc': (7.13, 0.42, 15800), 'lead': (11.4, 0.75, 7300)}
metals = list(products.keys())

metals.sort(key = lambda m:products[m][1])
print('Sort metals by share price:', metals)

sortBySharePrice = sorted(products.items(), key = lambda kv:kv[1][1])
print('Sort metals in kv pairs by share price:', sortBySharePrice)

print('\n')

metals.sort(key = lambda m:products[m][2], reverse=True)
print('Sort metals by most shares available:', metals)

sortBySharesAvailable = sorted(products.items(), key = lambda kv:kv[1][2], reverse=True)
print('Sort metals in kv pairs by most shares available:', sortBySharesAvailable)

mostSharesAvailable = sorted(products.items(), key = lambda kv:kv[1][2], reverse=True)[0]
print('KV pair of most shares available:', mostSharesAvailable)