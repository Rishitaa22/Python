'''
Author: Rishita
Date: 22-10-2024
Python program that demonstrates the usage of arithmetic, comparison, and logical operators.
version 1.1
'''

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
sum=a+b
division=a/b
print("sum:",sum,end="")
print("divison:", division)
print("Is a greater than b?", end="")
print(a>b)
print("Are a and b equal?", end="")
print(a==b)
print("logical AND:", end="")
print((a>b) and (b>a))
print("logical OR:", end="")
print((a>=b) or (b<=a))