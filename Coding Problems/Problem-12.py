"""Write a Python program to calculate the sum of three given numbers. 
    If the values are equal, return three times their sum."""

a = int(input())
b = int(input())
c = int(input())

if a==b and b==c:
    print(3*(a+b+c))
else: print(a+b+c)