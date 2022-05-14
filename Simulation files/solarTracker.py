import matplotlib.pyplot as plt
from lineDistance import distance
from pointsOnTriangle import pointsOfTriangle
from drawPlane import equationOfPlane
from plotPoint import plotPoint
from angleOfPlane import angleOfPlaneXY
from setPistonHeight import pistonPlanePosition

#configuration of matplotlib
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
#plt.ion()
fig = plt.figure()
ax = fig.gca(projection='3d')

#label the axises
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

#set limit on z axis
ax.set_zlim3d(0, 20)

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]

#calculating points of contact of panel
xp,yp,zp = pistonPlanePosition(10,10,10,0.5)

#calculating angle of plane
angle = angleOfPlaneXY(xp,yp,zp)
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
plotPoint(ax,xp[0],yp[0],zp[0],'Pp1','red')
plotPoint(ax,xp[1],yp[1],zp[1],'Pp2','red')
plotPoint(ax,xp[2],yp[2],zp[2],'Pp3','red')

#plot the lines
ax.plot(xl1,yl1,zl1,c='black')
ax.plot(xl2,yl2,zl2,c='black')
ax.plot(xl3,yl3,zl3,c='black')

#calculate line length
distanceOfLine1 = distance(xl1[0],yl1[0],zl1[0],xl1[1],yl1[1],zl1[1],'line 1')
distanceOfLine2 = distance(xl2[0],yl2[0],zl2[0],xl2[1],yl2[1],zl2[1],'line 2')
distanceOfLine3 = distance(xl3[0],yl3[0],zl3[0],xl3[1],yl3[1],zl3[1],'line 3')


#calculating the equation of plane
x,y,z = equationOfPlane(xp,yp,zp)

#plot the plane
ax.plot_surface(x, y, z)

#plt.pause(1)

plt.show()

