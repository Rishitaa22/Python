'''

author: Rishita
date:08-10-2024
version 1.0
Create, concatenate, and print a string and access a sub-string from a given string.

'''

first_name="Rishita"
last_name="P"
full_name=first_name+" "+last_name
print("full name:",full_name,)
length= len(first_name)
print(length)
Extracted_first_name=full_name[length+1:]
print(Extracted_first_name)
