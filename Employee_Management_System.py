'''
Author: Rishita
Date: 19/11/24
version 1.0
Python program to calculate employee with salary greater than a specified salary and total annual payroll expense of the company.
'''
employee_information=[
    ("Alex","cse",28000),
    ("Ben","ece",38000),
    ("Glenn","eee",25000),
    ("Jose","cse",40000)
]
threshold=int(input("Enter a salary threshold:"))
total_annual_expense=0
for employee in employee_information:
    employee_name,department,monthly_salary=employee
    if monthly_salary>threshold:
        print(employee)
    total_annual_expense+=monthly_salary*12
print("Total annual payroll expense of the company=",total_annual_expense)