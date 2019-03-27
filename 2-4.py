#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
while y == 0:
    y = get_int("y: ")

print('X is divisible by Y') if (x % y == 0) else print('X is not divisible by Y')
