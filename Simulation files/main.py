from pointsOnTriangle import pointsOfTriangle
import angleOfPlane
from setPistonHeight import pistonPlanePosition

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]

for testNumber in range(0,9):
        #calculating points of contact of panel
        xp,yp,zp = pistonPlanePosition(10,10,10,0.5,testNumber)

        #calculating angle of plane 
        angleXY = angleOfPlane.angleOfPlaneXY(xp,yp,zp)
        print("angle of plane wrt xy plane is", angleXY)

        # angleYZ = angleOfPlane.angleOfPlaneXY(xp,yp,zp)
        # print("angle of plane wrt yz plane is", angleYZ)

        # angleXZ = angleOfPlane.angleOfPlaneXY(xp,yp,zp)
        # print("angle of plane wrt xz plane is", angleXZ)

