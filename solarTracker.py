import numpy as np
import matplotlib.pyplot as plt

# Function to find equation of plane.
def equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3):
     
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)
    if c != 0:
        z = (-a/c)*x-(b/c)*y-(d/c)
    else: z = 0
    return z
    

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)
eq = equation_plane(1,0,0,2,2,0,3,5,0)

fig = plt.figure()

ax = fig.gca(projection='3d')

ax.plot_surface(x, y, eq)

plt.show()