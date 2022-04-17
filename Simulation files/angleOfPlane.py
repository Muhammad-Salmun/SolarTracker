import imp
import numpy as np
import math

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angleBetween(v1, v2):
    """ Returns the angle in 'radians' between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def angleOfPlane(x, y, z):
        A = np.array([x[1]-x[0], y[1]-y[0], z[1]-z[0]])
        B = np.array([x[2]-x[0], y[2]-y[0], z[2]-z[0]])
        print("vector A is",A)
        print("vector B is",B)

        normal = np.cross(A,B)
        print("normal vector is ",normal)

        unitVecotrOfNormal = unit_vector(normal)
        
        unitVectorOnXYPlane = np.array([1,1,0])

        angleRadians = angleBetween(unitVecotrOfNormal,unitVectorOnXYPlane)

        angleDegree = math.degrees(angleRadians)

        return angleDegree


        

