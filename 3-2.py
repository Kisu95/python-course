#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
from cs50 import get_float, get_string
from math import pi

def countField(field, x, y=0):
    if (field == "circle"):
        return 2*pi*x
    if (field == "rectangle"):
        return x*y
    if (field == "triangle" or field == "rhombus"):
        return (x*y)/2

figures = []
fields = []

for i in range(2):
    while True:
        try:
            fieldType = get_string(
                "Enter name of figure. Choose one of these: circle/rectangle/triangle/rhombus:  ")
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
        figures.append([fieldType, x, y])
        fields.append(countField(fieldType, x, y))
    else:
        figures.append([fieldType, x])
        fields.append(countField(fieldType, x))

#print(figures)

if (fields[0] > fields[1]):
    print("The first figure (" + figures[0][0] + ") has larger field.")
elif (fields[1] > fields[0]):
    print("The second figure (" + figures[1][0] + ") has larger field.")
else:
    print("Figures have the same fields.")
