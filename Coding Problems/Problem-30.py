"""Write a Python program to sum the first n positive integers."""

n = int(input())
sum = 0
for num in range(n):
    sum += num
print(sum)