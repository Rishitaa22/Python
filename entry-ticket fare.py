'''
Author: Rishita
Date: 15-10-2024
Python program to determine entry-ticket fare in a zoo based on age
version 1.1
'''
age=int(input('Enter your age:'))
print("age=",age)
if age<10:
    print("fare=7")
elif age>=10 and age<60:
    print("fare=10")
else:
    print("fare=5")