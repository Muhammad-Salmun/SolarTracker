from pointsOnTriangle import pointsOfTriangle
import angleOfPlane
from setPistonHeight import pistonPlanePosition

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]

for testNumber in range(0,9):
        print()
        print('position: ',testNumber+1)
        try:
                #calculating points of contact of panel
                # pistonPlanePosition(xOfCentre, yOfCentre, panelHeight: float, baseToPanelRatio, maxPistonLength, testNumber):
                xp,yp,zp = pistonPlanePosition(10,10, 20, 0.5, 70, testNumber)
                # print('xp: ', xp)
                # print('yp: ', yp)
                # print('zp: ', zp)
        except:
                break
        #calculating angle of plane 
        angleXY = angleOfPlane.angleOfPlaneXY(xp,yp,zp)
        print("angle of plane wrt xy plane is", angleXY)

        angleYZ = angleOfPlane.angleOfPlaneYZ(xp,yp,zp)
        print("angle of plane wrt yz plane is", angleYZ)

        angleXZ = angleOfPlane.angleOfPlaneXZ(xp,yp,zp)
        print("angle of plane wrt xz plane is", angleXZ)


