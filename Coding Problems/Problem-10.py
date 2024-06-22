"""Write a Python program to calculate the difference between a given number and 17.
    If the number is greater than 17, return twice the absolute difference."""

n = int(input())
diff = 17-n
if n>17: print(2*abs(diff))
else: print(diff)