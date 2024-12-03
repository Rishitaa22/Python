'''
Author: Rishita
Date: 03/12/24
version 1.0
Program to create a stick game.
'''
def stick_game():
    print('Welcome to the stick game!')
    print(f'There will be a total of 16 sticks.\nEach player picks 1,2,or 3 sticks in one turn.\nThe player who picks the last stick loses.\nLet\'s begin!!')
    print()
    player1 = input("Enter the name of first player:")
    player2 = input("Enter the name of second player:")
    sticks = 16
    while sticks > 0:
        print(player1, ",Your Turn")
        print("Sticks remaining:", sticks)
        n=int(input("Pick 1,2 or 3 sticks:"))
        sticks-=n
        print()

        if sticks == 0:
            print(player2, "wins and", player1, "loses")
            break

        print(player2, ",Your Turn")
        print("Sticks remaining:", sticks)
        n = int(input("Pick 1,2 or 3 sticks:"))
        sticks -= n
        print()

        if sticks == 0:
            print(player1, "wins and", player2, "loses")
            break
stick_game()