from lineDistance import distance
from pointsOnTriangle import pointsOfTriangle
import angleOfPlane
from setPistonHeight import pistonPlanePosition

#calculating points of contact on ground
xg,yg = pointsOfTriangle(10,10,5)
zg = [0,0,0]

#calculating points of contact of panel
xp,yp,zp = pistonPlanePosition(10,10,10,0.5)

#calculating angle of plane 
angleXY = angleOfPlane.angleOfPlaneXY(xp,yp,zp)
print("angle of plane wrt xy plane is", angleXY)

angleYZ = angleOfPlane.angleOfPlaneYZ(xp,yp,zp)
print("angle of plane wrt yz plane is", angleYZ)

angleXZ = angleOfPlane.angleOfPlaneXZ(xp,yp,zp)
print("angle of plane wrt xz plane is", angleXZ)