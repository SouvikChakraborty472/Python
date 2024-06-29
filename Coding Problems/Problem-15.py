"""Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user."""

n = int(input())
if n%2 == 0:
    print("The number is even")
else: print("The number is odd")