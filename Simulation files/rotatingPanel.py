from inspect import indentsize


indentityMatrix = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
rotationArray = []
rotationArray.append(indentityMatrix)
# print(rotationArray)
finalArray = []
i = 0

def rotationalArray(pos):
    # for i in range(0,pos):
    #     finalArray = [[1,i,0],[i,1,i],[i,i,1]]
    #     rotationArray.append(finalArray)
    pos = pos*-0.1
    finalArray = [[ 1,       0,    0],
                  [ 0,     1,      0],
                  [ pos,     pos,    1]]
    return finalArray

def rotationalArray_sim(pos):
    # for i in range(0,pos):
    #     finalArray = [[1,i,0],[i,1,i],[i,i,1]]
    #     rotationArray.append(finalArray)
    finalArray = [[ 1,       0,    0],
                  [ 0,     1,      0],
                  [ 0,     -pos,    1]]
    return finalArray
# array = rotationalArray(3)
# print(array)
