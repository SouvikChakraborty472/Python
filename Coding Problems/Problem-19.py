"""Write a Python program that checks whether a specified value is contained within a group of values."""

i = int(input())
num = input()
lst = [int(n) for n in num.split()]
if i in lst:
    print('True')