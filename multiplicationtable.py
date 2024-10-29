'''
Rishita
Date:29/10/24
Python program to get the multiplication table upto 12 of a user input number.
version 1.1
'''
number=int(input("Enter a number:"))
for i in range (1,13):
    operation=number*i
    print(number,"*", i,"\t=",operation)