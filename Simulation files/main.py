# import matplotlib.pyplot as plt
from pointsOnTriangle import pointsOfTriangle
from planeOrientation import planeOrientation
from setPistonHeight import pistonPlanePosition

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]

for testNumber in range(0,9):
        print()
        print('position: ',testNumber+1)
        try:
                #calculating points of contact of panel
                xp,yp,zp = pistonPlanePosition(10,10,20,0.5,70,testNumber*5,45)

                #calculating azimuth and altitude angles
                azimuthAngle, elevationAngle = planeOrientation(xp ,yp ,zp)
                print('azimuth: ',azimuthAngle,'altitude: ', elevationAngle)

        except:
                break
