from contextlib import nullcontext
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

#Function to plot a point with cordinate 
def plotPoint(x:float,y:float,z:float,name:str = nullcontext,pointColor:str = 'black'):
    ax.scatter(x,y,z,c=pointColor,s=10)
    text = str(name) + str('(') + str(x) + ', ' + str(y) + ', ' + str(z) + str(')') 
    ax.text(x, y, z, text, zdir=(1, 1, 1))


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(0, 20, 100)
y = np.linspace(0, 20, 100)

x, y = np.meshgrid(x, y)

#points on the ground.
xg1,yg1,zg1 = 7.825,7.5,0
xg2,yg2,zg2 = 10,12.175,0
xg3,yg3,zg3 = 12.5,7.5,0

#points on the plane.
xp1,yp1,zp1 = 9.167,8.94,2
xp2,yp2,zp2 = 10,10.373,2
xp3,yp3,zp3 = 10.83,8.94,2

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

#plot the points on ground
plotPoint(xg1,yg1,zg1,'Pg1','red')
plotPoint(xg2,yg2,zg2,'Pg2','red')
plotPoint(xg3,yg3,zg3,'Pg3','red')

#show points on plane
plotPoint(xp1,yp1,zp1,'Pp1','black')
plotPoint(xp2,yp2,zp2,'Pp2','black')
plotPoint(xp3,yp3,zp3,'Pp3','black')

#plot the lines
ax.plot(xl1,yl1,zl1,c='black')
ax.plot(xl2,yl2,zl2,c='black')
ax.plot(xl3,yl3,zl3,c='black')

ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

plt.show()