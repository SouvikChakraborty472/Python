"""Write a  Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20."""

a = int(input())
b = int(input())
c = int(input())
sum = a+b+c
if sum>15 and sum<20:
    print("sum = 20")
else: print("sum = ", sum)