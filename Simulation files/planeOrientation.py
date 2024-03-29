import numpy as np
import math

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def normalU(x,y,z):
    A = np.array([x[1]-x[0], y[1]-y[0], z[1]-z[0]])
    B = np.array([x[2]-x[0], y[2]-y[0], z[2]-z[0]])
    # print("vector A is",A)
    # print("vector B is",B)

    normal = np.cross(B,A)
    normal = unit_vector(normal)
    return normal

# caculates the angle wrt axis of variable provided first
def quadrantAngle(x, y):
    if y == 0:
        return 180 if x < 0 else 0
    
    if x == 0:
        return 90 if y > 0 else 270
    
    angleWithX = math.degrees(np.arctan(y/x))
    if x > 0:
        return angleWithX if angleWithX > 0 else 270 - angleWithX

    if x < 0:
        return angleWithX + 180

def planeAngle(normal):

    x,y,z = normal
    # print(x,y,z)
    
    # calculation of projection vector or Hypotenuse
    hypotnuseOfXandY = math.sqrt(x*x + y*y)
    
    #calculating azimuth angle
    azimuthAngle = round(quadrantAngle(x,y),2)

    #calculating altitude of panel
    altitude = round(90 - quadrantAngle(hypotnuseOfXandY,z),2)
    
    return azimuthAngle, altitude

def planeOrientation(x,y,z):
    
    planeNormal = normalU(x,y,z)

    orientationAngles = planeAngle(planeNormal)
    
    return orientationAngles
