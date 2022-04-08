import math as m
def pointsOfTriangle(xOfCentre :float,yOfCenter :float, sideLengthOfTriangle :float,heightOfPlane :float):
        # x cordinates
        xg1 = round(xOfCentre - sideLengthOfTriangle/2,4)
        xg2 = round(xOfCentre,4)
        xg3 = round(xOfCentre + sideLengthOfTriangle/2,4)
        # y cordinates
        yg1 = round(yOfCenter - (sideLengthOfTriangle*m.sqrt(3))/4,4)
        yg2 = round(yOfCenter + (sideLengthOfTriangle*m.sqrt(3))/4,4)
        yg3 = round(yOfCenter - (sideLengthOfTriangle*m.sqrt(3))/4,4)
        # z cordinates
        zg1 = round(heightOfPlane,4)
        zg2 = round(heightOfPlane,4)
        zg3 = round(heightOfPlane,4)

        xg = [xg1,xg2,xg3]
        yg = [yg1,yg2,yg3]
        zg = [zg1,zg2,zg3]


        return xg,yg,zg