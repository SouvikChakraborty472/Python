"""Write a Python program that concatenates all elements in a list into a string and returns it."""

num = input()
lst = [int(n) for n in num.split()]
result = ""
for element in lst:
    result += str(element)
print(result)