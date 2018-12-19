# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:34:30 2018

@author: pamde
"""

###############################################

#CHAPTER 02 - OPERATIONS, STRINGS AND VARIABLES

###############################################

#---------------------------------------
#TASK 1: Simple operations
#---------------------------------------

print(5 - 6)
print(8 * 9)
print(6 / 2)
print(5 / 2)
print(5.0 / 2)
print(5 % 2)
print(2 * (10 + 3))
print(2**4)


#---------------------------------------
#TASK 2: Variable practise
#---------------------------------------

age = 5
age = "almost there"
age = 29.5
age = 'I really don\'t know!'
 
print(age)

#---------------------------------------
#TASK 3: Basic string manipulation
#---------------------------------------

print ('hello' + 'world')
print ("Joke \n" * 3)
print ("Chen" + str(3))
print ("hello".upper())
print ("GOODBYE".lower())
print ("\n \n")
print ("the lord of the rings".title())
print(type(10))

print("Bob \n" * 2 + "Bob")

S1 = 'hello ' + 'world '
S2 = "Joke " * 3
S3 = 5

print(S1 + S2 * 10)
print(S1 + S2 + str(S3))

s1 = '4'
s2 = '6'
s3 = 8

result = int(s1) + int(s2) + s3

print(result)

print("\n") 

#---------------------------------------
#EXTRA: Split strings
#---------------------------------------

str1 = 'a,b,c,d,e,happy'

print(str1)

splitStr = str1.split(',')

print(splitStr)

print("\n") 

#---------------------------------------
#TASK 4: Formatting
#---------------------------------------

age = 5
like = "painting"
color = "green"

age_description = "My age is {} and I like {}.".format(age, like)
print(age_description)

age_description2 = "My age is {0} and I like {2}.".format(age, like, color)
print(age_description2)

print("\n") 

test = """aaa
bbb ccc ddd eee
fff ggg hhh iii 
jjj kkk lll
"""

print(test)
