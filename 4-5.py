# 5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic, test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p).

from scipy.optimize import basinhopping
from scipy import linspace, cos, exp, random, meshgrid, zeros, sin
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
import decimal
import time

start = time.time()


def f(x):
    return (sin(x[0])**2 + cos(x[1])**2)/(2+x[0]**2 + x[1]**2)


def neg_f(x):
    return -f(x)


# local optima
x0 = ((0, 2))
x_min = fmin(neg_f, x0)

#global optima
global_x = []
global_y = []
global_xy = []

for i in range(1000):
    ret = basinhopping(neg_f, x0)
    global_x.append(ret.x[0])
    global_y.append(ret.x[1])
    global_xy.append([ret.x[0], ret.x[1], f([ret.x[0], ret.x[1]])])
    end = time.time()
    time1 = end - start
    if time1 > 30:
        total = i
        break

# print(global_xy)
# print(ret)

ind_maximum = 0
for i in range(len(global_xy)):
    if global_xy[i][2] > global_xy[ind_maximum][2]:
        ind_maximum = i

#print(global_x, global_y, global_xy)
ret = basinhopping(neg_f, x0)
end = time.time()
time = end - start

# Nice print :D

print("Global optima is near: ", "{0:.2f}".format(
    ret.x[0]), "{0:.2f}".format(ret.x[1]))
print("Total time: ", "{0:.2f}".format(time))
fails = ret.minimization_failures
print('fails / total trials rate: ' + str(fails) + '/' + str(total))

delta = 4
x_knots = linspace(x_min[0] - delta, x_min[0] + delta, total)
y_knots = linspace(x_min[1] - delta, x_min[1] + delta, total)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g',
        marker='o', markersize=5, label='initial')
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k',
        marker='o', markersize=5, label='local maximum')
ax.plot([global_xy[ind_maximum][0]], [global_xy[ind_maximum][1]],
        [global_xy[ind_maximum][2]], '*', label='global maximum')
ax.legend()
show()
