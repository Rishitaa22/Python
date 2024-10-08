'''
author: Rishita
date:08-10-2024
version 1.0
Simple desktop calculator using Python. Five basic arithmetic operators
'''


number1= int(input("enter first number:"))
number2= int(input("enter second number:"))
number3= int(input("enter third number:"))
A=number1+number2
print("The sum of num1 and num2 is:",A,)
B=number1-number2
print("The difference when number2 is subtracted rom number1 is:",B,)
C=number1*number2
print("The product of number1 and number2 is:",C,)
D=number1/number2
print("The quotient when number1 is divide by number2 is:",D,)
E=number1%number2
print("The reminder when number1 is divided by number2 is:",E,)
F=(number1+number2)*number3/2
print("The  result of (number1+number2)*number3/2 is:",F,)