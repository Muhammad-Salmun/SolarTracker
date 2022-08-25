import numpy as np
import math
indentityMatrix = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
rotationArray = []
rotationArray.append(indentityMatrix)
# print(rotationArray)
finalArray = []
i = 0

def rotationalArray(theta_x,theta_y):
    finalArray = [
        [
            round(np.cos(math.radians(theta_y)),3), 
            0, 
            round(np.sin(math.radians(theta_y)),3)
        ],
        [
            round(np.sin(math.radians(theta_x)) * np.sin(math.radians(theta_y)),3),  
            round(np.cos(math.radians(theta_x)),3), 
            round(-np.sin(math.radians(theta_x)) * np.cos(math.radians(theta_y)),3)
        ],
        [
            round(-np.cos(math.radians(theta_x)) * np.sin(math.radians(theta_y)),3), 
            round(np.sin(math.radians(theta_x)),3), 
            round(np.cos(math.radians(theta_x)) * np.cos(math.radians(theta_y)),3)
        ]
    ]
                  
    # finalArray[0][0] = np.cos(math.radians(theta_y))
    # finalArray[0][1] = 0
    # finalArray[0][2] = np.sin(math.radians(theta_y))
    
    # finalArray[1][0] = np.sin(math.radians(theta_x)) * np.sin(math.radians(theta_y))
    # finalArray[1][1] = np.cos(math.radians(theta_x))
    # finalArray[1][2] = -np.sin(math.radians(theta_x)) * np.cos(math.radians(theta_y))
    
    # finalArray[2][0] = -np.cos(math.radians(theta_x)) * np.sin(math.radians(theta_y))
    # finalArray[2][1] = np.sin(math.radians(theta_x))
    # finalArray[2][2] = np.cos(math.radians(theta_x)) * np.cos(math.radians(theta_y))
    
    return finalArray


def rotationalArray_sim(theta_x, theta_y):
    finalArray = [
        [
            round(np.cos(math.radians(theta_y)),3), 
            0, 
            round(np.sin(math.radians(theta_y)),3)
        ],
        [
            round(np.sin(math.radians(theta_x)) * np.sin(math.radians(theta_y)),3),  
            round(np.cos(math.radians(theta_x)),3), 
            round(-np.sin(math.radians(theta_x)) * np.cos(math.radians(theta_y)),3)
        ],
        [
            round(-np.cos(math.radians(theta_x)) * np.sin(math.radians(theta_y)),3), 
            round(np.sin(math.radians(theta_x)),3), 
            round(np.cos(math.radians(theta_x)) * np.cos(math.radians(theta_y)),3)
        ]
    ]
    return finalArray
# array = rotationalArray(3)
# print(array)
