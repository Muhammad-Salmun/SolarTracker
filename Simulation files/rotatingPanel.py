from inspect import indentsize


indentityMatrix = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
rotationArray = []
rotationArray.append(indentityMatrix)
# print(rotationArray)
finalArray = []
i = 0

def rotationalArray():
        for i in range(1,9):
                val = round(0.1 * i,3)
                finalArray = [[1.0,val,val],[val,1.0,val],[val,val,1.0]]
                # print(finalArray)
                rotationArray.append(finalArray)
        return rotationArray
# rotationalArray()
# print('rotation array :')
# for x in rotationArray:
#         print(*x)