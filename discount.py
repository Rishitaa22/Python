'''
Author: Rishita
Date: 15-10-2024
Python program to determine colour based on a given code value.
version 1.1
'''
total_bill_amount=int(input("Enter bill amount:"))
if total_bill_amount>500:
    discount=total_bill_amount*.20
    final_bill=(total_bill_amount-discount)
    print(final_bill)
elif total_bill_amount>=200 and total_bill_amount<=500:
    discount=total_bill_amount*.10
    final_bill=(total_bill_amount-discount)
    print(final_bill)
else:
    discount=total_bill_amount*0
    final_bill=total_bill_amount
    print(final_bill)