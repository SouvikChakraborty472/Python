"""Write a python program to test whether a number is within
    100 of 1000 or 2000."""

def near_thousand(N):
    if N>1000-100 and N<1000+100:
        print("The number is within 100 of 1000")
    elif N>2000-100 and N<2000+100:
        print("The number is within 100 of 2000")
    else: print("The number is not with 100 of 1000 or 2000")

N = int(input())
near_thousand(N)