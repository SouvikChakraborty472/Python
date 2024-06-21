"""Write a Python program that calculates the area of a circle based on the radius entered by the user.
    Sample Output :
    r = 1.1
    Area = 3.8013271108436504"""

# Type-1
r = float(input())
print("Area = ", float( 3.14*r**2))

# Type-2
r = float(input())
print("Area = ", pow(r, 2))