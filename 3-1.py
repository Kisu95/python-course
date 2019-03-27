#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
from cs50 import get_float, get_string
from math import pi

def countField(field, x, y=0):
    if (field == "circle"):
        return 2*pi*x
    if (field == "rectangle"):
        return x*y
    if (field == "triangle" or field == "rhombus"):
        return (x*y)/2

while True:
    try:
        fieldType = get_string("Enter name of figure. Choose one of these: circle/rectangle/triangle/rhombus:  ")
        fieldType = fieldType.lower()
        assert(fieldType == "circle" or fieldType ==
               "rectangle" or fieldType == "triangle" or fieldType == "rhombus")
        break
    except AssertionError:
        print("Choose one of these figures: circle/rectangle/triangle/rhombus ")

while True:
    try:
        x = get_float("Enter x: ")
        assert(x > 0)
        break
    except AssertionError:
        print("Number should be greater than 0")
    
if (fieldType != "circle"):
    while True:
        try:
            y = get_float("Enter y: ")
            assert(y > 0)
            break
        except AssertionError:
            print("Number should be greater than 0")

if (fieldType != "circle"):
    print("Field of " + str(fieldType) + " = " + str("{0:.2f}".format(countField(fieldType, x, y))))
else: 
    print("Field of circle = " + str("{0:.2f}".format(countField(fieldType, x))))



