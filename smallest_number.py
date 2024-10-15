'''
Author: Rishita
Date: 15-10-2024
program to determine the smallest number of three numbers.
version 1.1
'''
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))
if num1<num2 and num1<num3:
    print(num1,"is the smallest number of all.")
elif num2<num1 and num2<num3:
    print(num2,"is the smallest number of all.")
else:
    print(num3,"is the smallest number of all.")