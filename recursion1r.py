#factorial
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
factorial(5)
print()
print()
#addition of two positive numbers.
n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
if n1>0 and n2>0:
    def add_numbers(n1,n2):
        if n2==0:
            print(n1)
        else:
            add_numbers(n1+1,n2-1)
    add_numbers(n1,n2)
else:
    print('The number is not a positive number.')
print()
print()
#multiplication of two numbers.
#n1 and n2 values are taken from user(in second function).
def mul_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mul_numbers(n1,n2-1)
print(mul_numbers(n1,n2))
#mul_numbers(3,4) will give 3*4
print()
print()
#gcd
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
print(gcd(516,188))
#gcd(n1,n2) will give gcd of two user input numbers of second function.