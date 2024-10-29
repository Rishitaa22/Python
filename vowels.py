'''
Rishita
Date:29/10/24
Python program to check the number of vowels and consonants.
version 1.1
'''
string_input=input("enter a string:")
vowels="aeiouAEIOU"
consonants=0
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
        consonants+=1
print(f"The number of vowels in {string_input} = {vowels_count}")
print(f"The number of consonants in {string_input} = {consonants}")