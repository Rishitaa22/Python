'''
Author: Rishita
Date: 22-10-2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit.
version 1.1
'''

temperature=int(input("Enter temperature:"))
scale=input("Is this celsius or Fahrenheit?")
if scale=="C":
    f=(9/5*temperature)+32
    print(temperature,"Celsius is",f,"Fahrenheit")
else:
    c=5/9*(temperature-32)
    print(temperature, "Fahrenheit is",c,"Celsius")