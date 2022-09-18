# SolarTracker
a simulation of 3-RPS dual-axis solar tracker setup using python

21/04/2022:
the height of pistons can now be calculated using vector equations that wa found on robot kinematics tutorial videos
https://www.youtube.com/watch?v=wybp1_htA7k&list=PLT_0lwItn0sAfi3o4xwx-fNfcnbfMrXa7&index=10

the piston heights match the ones generated before when the z-coordinate of the plane was given. the additional feature I get is that now i can control the angle at which the plane slants with the help of a 3x3 rotaiontal matrix. for parallel operation it is set as a identity matrix.

the rotational matrix is found out be XY eulers angles

if theta_x is positive, it tilts to negative y-axis(y < 10) and vice-versa
if theta_y is positive, it tilts to positive x-axis(x > 10) and vice-versa

the input azimuth angles and the output titlting angle showed some variations. and upon further expolorations it shoed the variations where not linear. also couldn't fint the root cause. inverse trignonemtry above 90 degrees gets really confusing.

A graph was plotted between the input and output azimuth angle sand fount the grapph is only linear between 0 to 90 and then from 180 to 360



