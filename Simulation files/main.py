import matplotlib.pyplot as plt
import numpy as np
from cylToEulerXY import cyltoEulerXY
from pointsOnTriangle import pointsOfTriangle
from planeOrientation import planeOrientation
from setPistonHeight import pistonPlanePosition_sim

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]
azimuth_input = np.arange(0,360,1)
# print(azimuth_input)
finalArray = []
for testNumber in range(0,360):        
        try:
                # print()
                # print('position: ',testNumber+1)
                # print(azimuth_input[testNumber])
                #calcuating Euler anlges from sensor data
                theta_x,theta_y = cyltoEulerXY(azimuth_input[testNumber],10)
                #calculating points of contact of panel
                xp,yp,zp = pistonPlanePosition_sim(10,10,20,0.5, theta_x, theta_y)

                #calculating azimuth and altitude angles
                azimuthAngle, elevationAngle = planeOrientation(xp ,yp ,zp)
                # print('azimuth: ',azimuthAngle,'altitude: ', elevationAngle)

                finalArray.append(azimuthAngle)

        except:
                break

# print(finalArray)

plt.plot(azimuth_input,finalArray)
plt.show()