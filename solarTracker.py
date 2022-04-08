from contextlib import nullcontext
import numpy as np
import matplotlib.pyplot as plt
from lineDistance import distance
from mean import mean

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

#Function to plot a point with cordinate 
def plotPoint(x:float,y:float,z:float,name:str = nullcontext,pointColor:str = 'black'):
    ax.scatter(x,y,z,c=pointColor,s=10)
    text = str(name) + str('(') + str(x) + ', ' + str(y) + ', ' + str(z) + str(')') 
    ax.text(x, y, z, text, zdir=( 1, 1, 1))


#points on the ground.
xg1,yg1,zg1 = 7.825,7.5,0
xg2,yg2,zg2 = 10,12.175,0
xg3,yg3,zg3 = 12.5,7.5,0

#points on the plane.
xp1,yp1,zp1 = 9.167,8.94,10
xp2,yp2,zp2 = 10,10.373,10
xp3,yp3,zp3 = 10.83,8.94,10

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

#configuration
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(0, 20, 10)
y = np.linspace(0, 20, 10)

x, y = np.meshgrid(x, y)

eq = equation_plane(xp1,yp1,zp1,xp2,yp2,zp2,xp3,yp3,zp3)
print(eq)

fig = plt.figure()

ax = fig.gca(projection='3d')

#line for 20unit reference in z axis
ax.plot((0,0),(0,0),(0,20),'white')

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

#calculate line length
tx1 = distance(xl1[0],yl1[0],zl1[0],xl1[1],yl1[1],zl1[1],'line 1')
tx1 = distance(xl2[0],yl2[0],zl2[0],xl2[1],yl2[1],zl2[1],'line 2')
tx1 = distance(xl3[0],yl3[0],zl3[0],xl3[1],yl3[1],zl3[1],'line 3')

#plot the lines
ax.plot(xl1,yl1,zl1,c='black')
#ax.text(mean(xl1),mean(yl1),mean(zl1),tx1)
ax.plot(xl2,yl2,zl2,c='black')
ax.plot(xl3,yl3,zl3,c='black')

#label the axises
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

plt.show()