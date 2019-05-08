#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
#2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'
import numpy as np
import matplotlib.pyplot as plt
from cs50 import get_float

T = get_float("time range: ")
while T <= 0:
    T = get_float("time range: ")

a = get_float("a: ")
while a == 0:
    a = get_float("a: ")

def fig(T, a):
    initial_x = 1
    h = get_float("step: ")
    while h <= 0:
        h = get_float("step: ")
    t = np.arange(0, T, h)
    x = np.zeros(t.shape)
    x[0] = initial_x
    for i in range(t.size-1):
        x[i+1] = x[i] + h * (1 * x[i])
    return plt.plot(t, x, 'r', label = 'Not Ideal')

def per_fig(T, a):
    initial_x = 1
    h = get_float("step: ")
    while h <= 0:
        h = get_float("step: ")
    t = np.arange(0, T, h)
    x = np.zeros(t.shape)
    x[0] = initial_x
    for i in range(t.size-1):
        x[i+1] = x[i] + h * (1 * x[i])
    return plt.plot(t, x, 'g', label = 'Ideal')

fig(T, a)
per_fig(T, a)
plt.legend(loc='upper center')
plt.xlabel('t', fontsize=8)
plt.ylabel('x', fontsize=8)
plt.show()
