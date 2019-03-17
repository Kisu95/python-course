#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)

from cs50 import get_int
from math import pi

def perimeter(r):
    x = 2*pi*r
    return "{0:.2f}".format(x)

def field(r):
    x = pi*r**2
    return "{0:.2f}".format(x)

x = get_int("Enter radius X: ")
y = get_int("Enter radius Y: ")

print("1st circle perimeter: " + (perimeter(x)))
print("1st circle field: " + field(x))

print("2nd circle perimeter: " + perimeter(y))
print("2nd circle field: " + field(y))
