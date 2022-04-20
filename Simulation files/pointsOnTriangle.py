import math as m
def pointsOfTriangle(xOfCentre :float,yOfCenter :float, sideLengthOfTriangle :float):
        
        # x cordinates
        xg1 = round(xOfCentre - sideLengthOfTriangle/2,4)
        xg2 = round(xOfCentre,4)
        xg3 = round(xOfCentre + sideLengthOfTriangle/2,4)
        # y cordinates
        yg1 = round(yOfCenter - (sideLengthOfTriangle*m.sqrt(3))/4,4)
        yg2 = round(yOfCenter + (sideLengthOfTriangle*m.sqrt(3))/4,4)
        yg3 = round(yOfCenter - (sideLengthOfTriangle*m.sqrt(3))/4,4)
        
        xg = [xg1,xg2,xg3]
        yg = [yg1,yg2,yg3]

        return xg,yg

