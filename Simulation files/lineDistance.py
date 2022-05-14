import math

#Function to find equation of a line.
def distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, name: str):
      
    d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)

    return d