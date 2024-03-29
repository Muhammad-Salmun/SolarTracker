from math import radians
import matplotlib.pyplot as plt
from pointsOnTriangle import pointsOfTriangle
from drawPlane import equationOfPlane
from plotPoint import plotPoint
from setPistonHeight import pistonPlanePosition_sim
from planeOrientation import planeOrientation
from cylToEulerXY import cyltoEulerXY

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

for testNumber in range(0,1):
        #calcuating Euler anlges from sensor data
        theta_x,theta_y = cyltoEulerXY(30+180,10)

        #calculating points of contact of panel
        xp,yp,zp = pistonPlanePosition_sim(10,10,10,0.5,theta_x, theta_y)

        #calculating azimuth and altitude angles
        azimuthAngle, elevationAngle = planeOrientation(xp ,yp ,zp)
        print('azimuth: ',azimuthAngle,'altitude: ', elevationAngle)

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

        #plot the lines - 3 arguments with starting and ending points of each coordinates of the line
        ax.plot(xl1,yl1,zl1,c='black')
        ax.plot(xl2,yl2,zl2,c='black')
        ax.plot(xl3,yl3,zl3,c='black')

        # y-axis
        ax.plot([10,10],[0,20],[0,0],c='yellow')
        ax.text(10,20,0, '+ve y-axis', zdir=( 1, 1, 1))
        
        # x-axis
        ax.plot([0,20],[10,10],[0,0],c='green')
        ax.text(20,10,0, '+ve x-axis', zdir=( 1, 1, 1))

        #plot nomral
        # plotPoint(ax,normalOfPlane[0]+10,normalOfPlane[1]+10,normalOfPlane[2]+10,'Pp3','yellow')
        # ax.plot([normalOfPlane[0],0],[normalOfPlane[1],0],[normalOfPlane[2],0],c='blue')

        #calculating the equation of plane
        x,y,z = equationOfPlane(xp,yp,zp)

        #plot the plane
        ax.plot_surface(x, y, z)

        #plt.pause(1)

        plt.show()

