import numpy as np
import math
indentityMatrix = [ [1.0,0.0,0.0],  [0.0,1.0,0.0],  [0.0,0.0,1.0]   ]
rotationalMatrix = []
# rotationArray.append(indentityMatrix)
# print(rotationArray)
finalArray = []

def rotationalArray(theta_x,theta_y):
    rotationalMatrix = [
        [
            round(np.cos(theta_y),3),
            0,
            round(np.sin(theta_y),3)
        ],
        [
            round(np.sin(theta_x) * np.sin(theta_y),3),
            round(np.cos(theta_x),3),
            round(-np.sin(theta_x) * np.cos(theta_y),3)
        ],
        [
            round(-np.cos(theta_x) * np.sin(theta_y),3), 
            round(np.sin(theta_x),3), 
            round(np.cos(theta_x) * np.cos(theta_y),3)
        ]
    ]    
    return rotationalMatrix


def RxRy_sim(theta_x, theta_y):
    rotationalMatrix = [
        [
            round(np.cos(theta_y),3),
            0,
            round(np.sin(theta_y),3)
        ],
        [
            round(np.sin(theta_x) * np.sin(theta_y),3),
            round(np.cos(theta_x),3),
            round(-np.sin(theta_x) * np.cos(theta_y),3)
        ],
        [
            round(-np.cos(theta_x) * np.sin(theta_y),3),
            round(np.sin(theta_x),3),
            round(np.cos(theta_x) * np.cos(theta_y),3)
        ]
    ]
    # print(finalArray)
    return rotationalMatrix
# print(array)

def RyRx_sim(theta_y, theta_x):
    rotationalMatrix = [
        [
            round(np.cos(theta_y),3), 
            round(np.sin(theta_x) * np.sin(theta_y),3),  
            round(np.cos(theta_x) * np.sin(theta_y),3)
        ],
        [
            0,
            round(np.cos(theta_x),3), 
            round(-np.sin(theta_x),3)
        ],
        [
            round(-np.sin(theta_y),3),
            round(np.sin(theta_x) * np.cos(theta_y),3),
            round(np.cos(theta_x) * np.cos(theta_y),3)
        ]
    ]
    return rotationalMatrix