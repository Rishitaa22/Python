'''
Author: Rishita
date:16/12/24
python program to multiplying two numbers using recursion
'''

def multi_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi_numbers(n1,n2-1)
m=multi_numbers(20,30)
print(m)
