import math as m
def pointsOfTriangle(xOfCentre :float,yOfCenter :float, lengthOfTriangle :float,heightOfPlane :float):
        # x cordinates
        xg1 = xOfCentre - lengthOfTriangle/2
        xg2 = xOfCentre
        xg3 = xOfCentre + lengthOfTriangle/2
        # y cordinates
        yg1 = yOfCenter - (lengthOfTriangle*m.sqrt(3))/4
        yg2 = yOfCenter + (lengthOfTriangle*m.sqrt(3))/4
        yg3 = yOfCenter - (lengthOfTriangle*m.sqrt(3))/4
        # z cordinates
        zg1 = heightOfPlane
        zg2 = heightOfPlane
        zg3 = heightOfPlane