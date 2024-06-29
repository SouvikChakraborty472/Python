"""Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence."""

num = input()
lst = [int(n) for n in num.split()]
for element in lst:
    if element == 237:
        break
    elif element%2 == 0:
        print(element)
    else: continue