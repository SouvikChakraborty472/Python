"""Write a  Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
    Return n copies of the whole string if the length is less than 2."""

n = int(input())
text = input()
if len(text)<2:
    print(n*text)
else: print(n*text[:n])