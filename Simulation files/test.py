import math
import numpy as np
from setPistonHeight import pistonPlanePosition_sim
from rotatingPanel import RxRy_sim, RyRx_sim
import planeOrientation

# azimuthAngle = 25.55
# altitude = 67.72

# x = 1
# y = np.tan(math.radians(azimuthAngle))

# # calculation of projection vecotr or Hypotenuse
# hypotnuseOfXandY = math.sqrt(x*x + y*y)
# theta_y = 90 - azimuthAngle
# theta_x = math.degrees(np.arctan(altitude / hypotnuseOfXandY))

# print('theta_x: ',round(theta_x))
# print('theta_y: ',round(theta_y))

# xp,yp,zp = pistonPlanePosition_sim(10,10,10,0.5,-10.0,20.0)
# # print('x: ',xp,'y: ',yp,'z: ',zp)
# normal = planeOrientation.normalU(xp,yp,zp)
# print('normal: ', np.round(normal, decimals=3))

# inverseRotationalMatrix = RyRx_sim(theta_y,theta_x)
# normal = np.dot(normal,inverseRotationalMatrix)
# print('new normal: ',normal)
