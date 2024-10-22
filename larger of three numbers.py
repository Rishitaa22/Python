'''
Author: Rishita
Date: 22-10-2024
Python program to determine the larger number of three numbers.
version 1.1
'''

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if num1>num2 and num1>num3:
    print("The largest number is:",num1)
elif num2>num1 and num2>num3:
    print("THe largest number is:",num2)
else:
    print("The largest number is:",num3)
