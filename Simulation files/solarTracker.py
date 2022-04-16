import matplotlib.pyplot as plt
from lineDistance import distance
from pointsOnTriangle import pointsOfTriangle
from drawPlane import equationOfPlane
from plotPoint import plotPoint
from angleOfPlane import angleOfPlane

#configuration of matplotlib
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.gca(projection='3d')
#label the axises
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

#calculating points of contact on ground
xg,yg,zg = pointsOfTriangle(10,10,5,0)

#calculating pojints of contact of panel
xp,yp,zp = pointsOfTriangle(10,10,2.5,10)

#calculating angle of plane
angle = angleOfPlane(xp,yp,zp)
print("angle of plane wrt xy plane is", angle)

#defining starting and ending points of lines
xl1 = [xp[0],xg[0]]
yl1 = [yp[0],yg[0]]
zl1 = [zp[0],zg[0]]

xl2 = [xp[1],xg[1]]
yl2 = [yp[1],yg[1]]
zl2 = [zp[1],zg[1]]

xl3 = [xp[2],xg[2]]
yl3 = [yp[2],yg[2]]
zl3 = [zp[2],zg[2]]

#plot the points on ground
plotPoint(ax,xg[0],yg[0],zg[0],'Pg1','red')
plotPoint(ax,xg[1],yg[1],zg[1],'Pg2','red')
plotPoint(ax,xg[2],yg[2],zg[2],'Pg3','red')

#plot points on plane
plotPoint(ax,xp[0],yp[0],zp[0],'Pp1','black')
plotPoint(ax,xp[1],yp[1],zp[1],'Pp2','black')
plotPoint(ax,xp[2],yp[2],zp[2],'Pp3','black')

#plot the lines
ax.plot(xl1,yl1,zl1,c='black')
ax.plot(xl2,yl2,zl2,c='black')
ax.plot(xl3,yl3,zl3,c='black')

#calculate line length
tx1 = distance(xl1[0],yl1[0],zl1[0],xl1[1],yl1[1],zl1[1],'line 1')
tx1 = distance(xl2[0],yl2[0],zl2[0],xl2[1],yl2[1],zl2[1],'line 2')
tx1 = distance(xl3[0],yl3[0],zl3[0],xl3[1],yl3[1],zl3[1],'line 3')

#calculating the equation of plane
x,y,z = equationOfPlane(xp,yp,zp)

#plot the plane
ax.plot_surface(x, y, z)

#line of 20unit for reference in z axis
ax.plot((0,0),(0,0),(0,20),'white')

plt.show()