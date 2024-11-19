'''
Author: Rishita
Date: 19/11/24
version 1.0
Python program to construct patterns of stars using a nested for loop.
'''
rows=int(input("Enter number of rows:"))
for i in range(rows):
    for j in range(i):
        print("*",end="")
    print()
print()
for i in range(rows-1,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print()
for i in range(1,rows+1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
print()
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
print()