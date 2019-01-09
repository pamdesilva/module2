# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:02:18 2019

@author: pamde
"""

### Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.
import string

def printAlpha():
    alphabets = list(string.ascii_uppercase)
    
    for item in alphabets:
        print(item, '\n')
        
    
    print('\n')
        
### For every third letter, write it to the console in lowercase instead.
    thirdLetter = list(string.ascii_uppercase)
    thirdLetter[2::3] = map(str.lower, thirdLetter[2::3])    
    for item in thirdLetter:
        print(item, '\n')
    
    print('\n')
    
###For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4').
    fourthLetter = list(string.ascii_lowercase)
    fourthLetter[3::4] = [ord(x) for x in fourthLetter[3::4]]
    for item in fourthLetter:
        print(item, '\n')
    
    print('\n')
    
### If a letter satisfies both rules 2 and 3, write out its numeric position followed by the letter in lowercase (e.g. 'L' should be output as '12l').    
    
    
    
printAlpha()



