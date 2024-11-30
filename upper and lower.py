def upper_and_lower():
    str=input('Enter a string: ')
    lower_case=0
    upper_case=0
    numbers=0
    for i in str:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
        elif i.isnumeric():
            numbers+=1
    print("No. of upper case characters in string=",upper_case)
    print("NO. of lower case characters in string=",lower_case)
    print("No. of numeric characters in string=",numbers)
upper_and_lower()