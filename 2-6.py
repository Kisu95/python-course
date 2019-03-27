#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_int, get_float

while True:     
    try:
        i = get_float("i: ")
        assert(i > 0)
        break
    except AssertionError:
        print("Number should be greater than 0")

x_knots = np.linspace(-3*np.pi, 3*np.pi, 201)
y_knots = np.linspace(-3*np.pi, 3*np.pi, 201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2+i**2)
Z = np.cos(R*i)**2*np.exp(-0.1*R*i)
ax = Axes3D(plt.figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()
