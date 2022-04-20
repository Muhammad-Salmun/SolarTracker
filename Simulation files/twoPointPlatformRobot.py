import matplotlib.pyplot as plt
import numpy as np

#configuration of matplotlib
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.gca(projection='3d')
#label the axises
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

# desired inputs
p = np.array([[2.0],[4.0],[10.0]])
R = np.array([[1.0,0.0,0.0], [0.0,1.0,0.0], [0.0,0.0,1.0]])

# constant param
a1 = np.array([[7.5],  [7.8],  [0.0]])
a2 = np.array([[10.0], [12.1], [0.0]])
a3 = np.array([[12.5], [7.8],  [0.0]])

b1 = np.array([[8.7],  [8.9],  [5.0]])
b2 = np.array([[10],   [11],   [5.0]])
b3 = np.array([[11.2], [8.9],  [5.0]])

# piston vector as output
s1 = p + np.dot(R,b1) - a1
s2 = p + np.dot(R,b2) - a2
s3 = p + np.dot(R,b3) - a3

#calculating length of piston from vector
s1_length = np.sqrt(s1[0]**2 + s1[1]**2)
s2_length = np.sqrt(s2[0]**2 + s2[1]**2)
s3_length = np.sqrt(s3[0]**2 + s3[1]**2)

#ax.plot([a1[0], s1[0] + a1[0], p[0], s2[0] + a2[0], a2[0]], [a1[1],s1[1] + a1[1], p[1], s2[1] + a2[1], a2[1]], [a1[2],s1[2] + a1[2], p[2], s2[2] + a2[2], a2[2]])

ax.quiver(0,0,0,s1[0],s1[1],s1[2])

plt.show()
