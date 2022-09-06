import math

def cyltoEulerXY(azimuthAngle, altitudeAngle):
        azimuthAngle = math.radians(azimuthAngle)
        altitudeAngle = math.radians(90 - altitudeAngle)

        x = math.cos(azimuthAngle)
        y = math.sin(azimuthAngle)
        z = math.sqrt(x*x + y*y) * math.tan(altitudeAngle)

        k = math.sqrt(x*x + z*z)

        theta_x = math.degrees(math.atan(y/k))
        theta_y = math.degrees(math.atan(-x/z))

        return theta_x, theta_y

print(cyltoEulerXY(45,45))