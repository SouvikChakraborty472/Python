"""Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years."""

pa = float(input())
roi = float(input())
noy = int(input())
print(pa*(1+(0.01*roi))**noy)