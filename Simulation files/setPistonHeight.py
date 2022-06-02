import numpy as np
from pointsOnTriangle import pointsOfTriangle
from rotatingPanel import rotationalArray

rotationalVector = rotationalArray()        
# [[1.0,0.50,0.50],
#                            [0.50,1.0,0.50],
#                            [0.50,0.50,1.0]]
def pistonPlanePosition(xOfCentre,yOfCentre, panelHeight: float, baseToPanelRatio, testNumber):

    #calculating points of contact on ground
    xg,yg = pointsOfTriangle(xOfCentre, yOfCentre,5)
    zg = [0,0,0]

    #piston mount points onthe ground
    pistonGroundPointVector1 = np.array([[xg[0]],[yg[0]],[zg[0]]])
    pistonGroundPointVector2 = np.array([[xg[1]],[yg[1]],[zg[1]]])
    pistonGroundPointVector3 = np.array([[xg[2]],[yg[2]],[zg[2]]])

    #plane center point
    planeCentrePointVector = np.array([[xOfCentre],[yOfCentre],[panelHeight]])

    #plane points with respect to plane center point
    xp,yp = pointsOfTriangle(0,0,5*baseToPanelRatio)
    zp = 0,0,0
    pistonPlanePointVector1 = np.array([[xp[0]],[yp[0]],[zp[0]]])
    pistonPlanePointVector2 = np.array([[xp[1]],[yp[1]],[zp[1]]])
    pistonPlanePointVector3 = np.array([[xp[2]],[yp[2]],[zp[2]]])

    #calculating piston vector
    pistonVector1 = planeCentrePointVector + np.dot(rotationalVector[testNumber],pistonPlanePointVector1) - pistonGroundPointVector1
    pistonVector2 = planeCentrePointVector + np.dot(rotationalVector[testNumber],pistonPlanePointVector2) - pistonGroundPointVector2
    pistonVector3 = planeCentrePointVector + np.dot(rotationalVector[testNumber],pistonPlanePointVector3) - pistonGroundPointVector3
    # pistonVector1 = planeCentrePointVector + np.dot(rotationalVector,pistonPlanePointVector1) - pistonGroundPointVector1
    # pistonVector2 = planeCentrePointVector + np.dot(rotationalVector,pistonPlanePointVector2) - pistonGroundPointVector2
    # pistonVector3 = planeCentrePointVector + np.dot(rotationalVector,pistonPlanePointVector3) - pistonGroundPointVector3

    #calculating piston length
    pistonLength1 = np.sqrt(pistonVector1[0]**2 + pistonVector1[1]**2 + pistonVector1[2]**2)
    pistonLength2 = np.sqrt(pistonVector2[0]**2 + pistonVector2[1]**2 + pistonVector2[2]**2)
    pistonLength3 = np.sqrt(pistonVector3[0]**2 + pistonVector3[1]**2 + pistonVector3[2]**2)

    print('length of first piston: ', pistonLength1)
    print('length of second piston: ', pistonLength2)
    print('length of third piston: ', pistonLength3)

    #calculating coordinates of mounting points of piston on the plane
    xOfPistons = pistonGroundPointVector1[0][0] + pistonVector1[0][0], pistonGroundPointVector2[0][0] + pistonVector2[0][0], pistonGroundPointVector3[0][0] + pistonVector3[0][0]

    yOfPistons = pistonGroundPointVector1[1][0] + pistonVector1[1][0], pistonGroundPointVector2[1][0] + pistonVector2[1][0], pistonGroundPointVector3[1][0] + pistonVector3[1][0]

    zOfPistons = pistonGroundPointVector1[2][0] + pistonVector1[2][0], pistonGroundPointVector2[2][0] + pistonVector2[2][0], pistonGroundPointVector3[2][0] + pistonVector3[2][0]

    return xOfPistons, yOfPistons, zOfPistons
