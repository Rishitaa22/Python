''''
Author: Rishita
Date: 16-12-2024
Python program to find the factorial of a number using Recursion.
version 1.0
'''
def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence