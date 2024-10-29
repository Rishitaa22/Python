'''
Rishita
Date:29/10/24
Python program to get n prime number.
version 1.1
'''
limit=int(input("Enter the limit:"))
for number in range(2,limit+1):
    isPrime=True
    for i in range (2,(number//2)+1):
        if number%i==0:
            isPrime=False
    if isPrime:
        print(number)