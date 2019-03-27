#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
from cs50 import get_float
from decimal import *

x = get_float("x: ")
y = get_float("y: ")
if y == 0:
    y = get_float("y: ")
else:
    getcontext().prec = 50
    x = Decimal(x)
    y = Decimal(y)
    a = x/y
    print("x/y = ", "%.2f" % a)
    #print("x/y = " , "%.5f" %a)
    #print("x/y = ", "%.7f" % a)
    #print("{0:.2f}".format(x/y))
    #print("{0:.5f}".format(x/y))
    #print("{0:.7f}".format(x/y))

#print("{0:.2f}".format(x/y))

