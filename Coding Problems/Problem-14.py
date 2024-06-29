"""Write a  Python program that returns a string that is n (non-negative integer) copies of a given string."""

n = int(input())
text = input()

if n>0:
    print(n*text)
else: print(text)