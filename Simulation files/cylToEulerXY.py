import math
import numpy as np

def cyltoEulerXY(azimuthAngle, altitudeAngle):
        azimuthAngle = math.radians(azimuthAngle)
        # so as to compute the angle from horizontal rather than the vertical i.e z-axis
        altitudeAngle = math.radians(90 - altitudeAngle) if altitudeAngle < 90 else math.radians(0.1)
        # altitudeAngle = math.radians(altitudeAngle)

        x = math.cos(azimuthAngle)
        y = math.sin(azimuthAngle)
        z = math.tan(altitudeAngle)

        k = math.sqrt(x*x + z*z)

        # theta_x = round(math.degrees(math.atan(y/k)))
        # theta_y = round(math.degrees(math.atan(-x/z)))

        theta_x = math.atan(y/k)
        theta_y = math.atan(-x/z)

        return theta_x, theta_y

# print(np.round(cyltoEulerXY(45,10)))