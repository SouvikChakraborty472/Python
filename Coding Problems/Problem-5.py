"""Write a Python program that accepts a filename from the user and prints the extension of the file.
    Sample filename : abc.java
    Output : java"""

# Type-1
filename = input().split('.')
lst = list(filename)
print(filename[1])

# Type-2
filename = input()
f_extns = filename.split('.')
print(f_extns[-1])