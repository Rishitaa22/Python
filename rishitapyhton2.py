'''

author: Rishita
date:08-10-2024
version 1.1
Create, concatenate, and print a string and access a sub-string from a given string.

'''

first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
full_name=first_name+" "+last_name
print("full name:",full_name,)
length= len(first_name)
print(length)
Extracted_first_name=full_name[length+1:]
print(Extracted_first_name)
