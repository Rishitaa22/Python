'''
Author: Rishita
Date: 19/11/24
version 1.0
Python program to calculate item with highest stock value in an inventory.
'''
inventory=[
    ("Laptop",10,30000.00),
    ("Mouse",12,150.00),
    ("Keyboard",22,250.00),
    ("Monitor",24,5000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f'Item name:{item_name}, the total stock value={stock_value}')
    highest_stock_value=stock_value
    item_with_highest_stock_value=item_name
print(f'Item with highest stock value is:{item_with_highest_stock_value}')
print(f'The highest stock value is:{highest_stock_value}')