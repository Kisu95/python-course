#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)

from cs50 import get_float
from math import pi

def perimeter(r):
    x = 2*pi*r
    return "{0:.2f}".format(x)

def field(r):
    x = pi*r**2
    return "{0:.2f}".format(x)

while True:
    try:
        x = get_float("Enter first circle radius: ")
        y = get_float("Enter second circle radius: ")
        assert(x > 0 and y > 0)
        break
    except AssertionError:
        print("Both radius should be positive")

print("1st circle perimeter: " + (perimeter(x)))
print("1st circle field: " + field(x))

print("2nd circle perimeter: " + perimeter(y))
print("2nd circle field: " + field(y))
