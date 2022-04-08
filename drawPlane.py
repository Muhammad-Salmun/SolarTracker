import numpy as np

x = np.linspace(0, 20, 10)
y = np.linspace(0, 20, 10)
x, y = np.meshgrid(x, y)

# Function to find equation of plane
def equationOfPlane(xp, yp, zp):
     
    a1 = xp[1] - xp[0]
    b1 = yp[1] - yp[0]
    c1 = zp[1] - zp[0]
    a2 = xp[2] - xp[0]
    b2 = yp[2] - yp[0]
    c2 = zp[2] - zp[0]
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * xp[0] - b * yp[0] - c * zp[0])
    if c != 0:
        z = (-a/c)*x-(b/c)*y-(d/c)
    else: z = 0
    return x,y,z