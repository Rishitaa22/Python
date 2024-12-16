'''
Author: Rishita
date:16/12/24
Python program to add two numbers using recursion
'''

def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
         return add_numbers(n1+1,n2-1)
sum=add_numbers(24,30)
print(sum)