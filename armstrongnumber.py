'''
Author: Rishita
Date: 22-10-2024
Python program to determine the armstrong number.
version 1.1
'''

number=int(input("Enter a number:"))
armstrong=number
sum=0
while (number>0):
    r=number%10
    number=number//10
    sum=sum=r**3
if sum==armstrong:
    print("NUmber is armstrong.")
else:
    print(("Number is not armstrong."))