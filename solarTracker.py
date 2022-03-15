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
    print('value of c is',c)
    d = (- a * x1 - b * y1 - c * z1)
    if c != 0:
        z = (-a/c)*x-(b/c)*y-(d/c)
    else: z = 0
    return z

#Function to find equation of a line.
#def length_line():


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(0, 20, 100)
y = np.linspace(0, 20, 100)

x, y = np.meshgrid(x, y)

#points on the plane.
xp1,yp1,zp1 = 3,5,35
xp2,yp2,zp2 = 13,5,35
xp3,yp3,zp3 = 8,8.5,35

#points on the ground.
xg1,yg1,zg1 = 3,5,0
xg2,yg2,zg2 = 13,5,0
xg3,yg3,zg3 = 8,8.5,0

xg = [xg1,xg2,xg3]
yg = [yg1,yg2,yg3]
zg = [zg3,zg3,zg3]

xl1 = [xp1,xg1]
yl1 = [yp1,yg1]
zl1 = [zp1,zg1]

xl2 = [xp2,xg2]
yl2 = [yp2,yg2]
zl2 = [zp2,zg2]

xl3 = [xp3,xg3]
yl3 = [yp3,yg3]
zl3 = [zp3,zg3]

eq = equation_plane(xp1,yp1,zp1,xp2,yp2,zp2,xp3,yp3,zp3)

fig = plt.figure()

ax = fig.gca(projection='3d')

#plot the plane
ax.plot_surface(x, y, eq)
#plot the points
ax.scatter(xg1,yg1,zg1,c='red',s=10)
ax.scatter(xp1,yp1,zp1,c='green',s=10)

#plot the lines
ax.plot(xl1,yl1,zl1,c='black')
ax.plot(xl2,yl2,zl2,c='black')
ax.plot(xl3,yl3,zl3,c='black')

plt.show()