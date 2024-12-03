'''
Author: Rishita
Date: 03/12/24
version 1.1
Program to create a stick game.
'''
name1=input('enter first player name:')
name2=input("enter second player name:")
sticks=16
print()
while sticks!=0 :
     print(name1,",your turn:")
     user1=int(input("pick 1,2 or 3 sticks:"))
     if user1 <1 or user1>3:
         print(name2,"wins you entered invalid number.")
         break

     sticks-=user1
     print()
     print("sticks remaining:", sticks)

     if sticks==0:
         print(name2,"wins",name1,"loses")
         break
     if sticks<0:
         print(name2,"wins:you entered invalid number.")
         break

     print(name2,",your turn:")
     user2=int(input("pick 1,2 or 3 sticks:"))
     if user2<1 or user2>3:
         print(name1,"wins you entered invalid number.")
         break

     sticks-=user2
     print()
     print("sticks remaining:", sticks)

     if sticks==0:
         print(name1,"wins",name2,"loses")
         break
     if sticks<0:
         print(name1,"wins:you entered invalid number.")
         break