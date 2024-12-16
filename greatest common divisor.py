'''
Author: Rishita
date:16/12/24
Python program to find the greatest common divisor
'''

def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
g=gcd(50,40)
print(g)