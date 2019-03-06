import numpy as np
from matplotlib.pyplot import *

while True:
    try:
        length = float(input("Enter length of a chart: "))
        isinstance(length, float)
        assert(length > 0)
        break
    except ValueError:
        print("That was no valid number!")
    except AssertionError:
        print("Length should be greater then 0.")
        
x = np.linspace(0, length)
y = np.sin(x)
plot(x, y)
show()

