#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
from math import pi

class Error(Exception):
   """Base class for other exceptions"""
   pass
class Zero(Error):
   pass
class Figures(Error):
   pass
class Sign(Error):
   pass

def Field(fig):
    try:
        figName = fig[0].lower()
        x = float(fig[1])
        if len(fig) > 2:
            y = float(fig[2])
        else:
            y = 1
        assert(x > 0 and y > 0)
    except AssertionError:
        print("X and Y should be greater than 0")
    fields = {"circle": 2 * pi * x,
            "rectangle": x * y,
            "triangle": 0.5 * x * y,
            "rhombus": x * y * 0.5}
    field = fields[figName]
    return field

def compareField(fields):
    stField = Field(fields[0])
    nnField = Field(fields[1])
    if stField > nnField:
        return print("The first figure (" + fields[0][0] + ") has larger field.")
    elif stField == nnField:
        return print("Figures have the same fields.")
    else:
        return print("The second figure (" + fields[1][0] + ") has larger field.")

try:
    inputs = [['rectangle', 2, 8], ['rectangle', 7, 2]]
    if len(inputs) != 2:
       raise Figures
    if ((inputs[0][0]).lower() == "circle" and len(inputs[0]) != 2) or ((inputs[0][0]).lower() != "circle" and len(inputs[0])):
       raise Sign
    if (inputs[1][0]).lower() == "circle" and len(inputs[1]) != 2 or (inputs[0][0]).lower() != "circle" and len(inputs[1]) != 3:
       raise Sign
    compareField(inputs)
except ValueError:
    print("Enter correct number.")
except Zero:
    print("Length can not be negative")
except KeyError:
    print("Choose one of these figures: circle/rectangle/triangle/rhombus ")
except Sign:
    print("Check your input")
except IndexError:
    print("wrong number of characters was entered")
except Figures:
    print("wrong amount of figures")
