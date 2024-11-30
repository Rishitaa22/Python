'''
Author: Rishita
Date: 30/11/2024
Python program to whether or not the triangle is a right triangle.
Version 1.0
'''
def triangle():
    side_1=int(input('Enter first side: '))
    side_2=int(input('Enter second side: '))
    side_3=int(input('Enter third side: '))
    sides=[side_1,side_2,side_3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        print('The given triangle is a right triangle.')
    else:
        print('The given triangle is not a right triangle.')
triangle()