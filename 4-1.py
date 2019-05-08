#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)

import numpy as np
import matplotlib.pyplot as plt
from cs50 import get_float

initial_x = 1

T = get_float("time range: ")
while T <= 0:
    T = get_float("time range: ")
    
h = get_float("step: ")
while h <= 0:
    h = get_float("step: ")

a = get_float("a: ")
while a == 0:
    a = get_float("a: ")

t = np.arange(0, T, h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (1 * x[i])

plt.plot(t,x)
plt.xlabel('t', fontsize=8)
plt.ylabel('x', fontsize=8)
plt.show()
