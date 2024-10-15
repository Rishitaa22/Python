'''
Author: Rishita
Date: 15-10-2024
Python program to calculate sum of digits of a number.
version 1.1
'''
num=int(input("Enter a number:"))
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=(sum+r)
print("sum of digits of the number=",sum)