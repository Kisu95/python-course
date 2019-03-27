#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
from cs50 import get_float
from decimal import *

x = get_float("x: ")
y = get_float("y: ")

while y == 0:
    y = get_float("y: ")

print("{0:.2f}".format(x/y))

