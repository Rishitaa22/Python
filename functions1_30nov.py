'''
Author: Rishita
Date: 30/11/2024
Python program to check whether the given number is a valid mobile number or not using functions.
Version 1.0
'''

def mobile():
    number = input('Enter a mobile number: ')
    length=len(number)
    if length==10:
        if number[0]=='7'or number[0]=='8' or number[0]=='9':
            print('The number is valid.')
        else:
            print("The number is invalid.")
    else:
        print('The number is invalid.')
mobile()
