#Find a differential equation which represents a process / model(your choice) 
# and implement it using odeint python function(1p)
#tłumiony oscylator sprężyna-masa.
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def F(x,t):
    dx = [0,0]
    dx[0] = x[1]
    dx[1] = -x[0] - 0.5*x[1]
    return dx

t_start = 0
t_stop = 20
n = 0.01
t = np.arange(t_start,t_stop,n)
x_init = (10,0)
X = odeint(F,x_init,t)

plt.plot(X)
plt.show()
