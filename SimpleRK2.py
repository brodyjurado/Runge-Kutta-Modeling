#A program to ...

from numpy import * 
import matplotlib.pyplot as plt 

step = 0.0001

def f(x, y):
    return sin(x)*y

def recursion(x_previous, y_previous):
    k1 = f(x_previous, y_previous)
    k2 = f(x_previous + step/2, y_previous + step/2 * k1)
    k3 = f(x_previous + step/2, y_previous + step/2 * k2)
    k4 = f(x_previous + step, y_previous + step * k3)
    return y_previous + step/6*(k1 + 2 * k2 + 2 * k3 + k4)

x_initial = 0.0
y_initial = 1.0
x_final = 4.0*pi

x_values = [x_initial]
y_values = [y_initial]

while x_values[-1] < x_final:
    y_values.append(recursion(x_values[-1], y_values[-1]))
    x_values.append(x_values[-1] + step)
    
plt.figure()
plt.plot(x_values, y_values, 'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.show()