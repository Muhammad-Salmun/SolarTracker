import numpy as np
rotationArray = np.identity(3,float)
finalArray = []
finalArray.append(rotationArray)
i = 0

def rotationalArray(pos):
    for i in range(0,3):
        finalArray = [[1,i,0],[i,1,i],[i,i,1]]
        rotationalArray.append(finalArray)
    return finalArray[pos]

array = rotationalArray(3)
print(array)