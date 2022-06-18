from inspect import indentsize


indentityMatrix = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
rotationArray = []
rotationArray.append(indentityMatrix)
# print(rotationArray)
finalArray = []
i = 0

def rotationalArray(pos):
    for i in range(0,3):
        finalArray = [[1,i,0],[i,1,i],[i,i,1]]
        rotationalArray.append(finalArray)
    return finalArray[pos]

array = rotationalArray(3)
print(array)
