"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero."""

a = int(input())
b = int(input())
c = int(input())
if a==b or b==c or c==a:
    print("sum = 0")
else: print("sum = ", a+b+c)