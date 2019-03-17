#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
while y == 0:
    if y == 0:
        y = get_int("y: ")

print("{0:.2f}".format(x/y))

