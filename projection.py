import matplotlib.pyplot as plt
import numpy as np

#Create an figure and axes
fig, ax = plt.subplots(ncols=2)

# ax.plot([start_x, end_x], [start_y, end_y], "b")

#Vectors

vec1 = np.array([2, 2])
vec2 = np.array([6, 3.5])

#draw Vector 1
# ax[0].plot([0, vec1[0]], [0, vec1[1]], "b")
ax[0].quiver(0, 0, 2, 2, angles="xy", scale_units="xy", scale=1, color="black", label="Vector")
ax[0].quiver(0, 0, 6, 3.5, angles="xy", scale_units="xy", scale=1, color="red", label="Vector")

#draw Vector 2
# ax[0].plot([0, vec2[0]], [0, vec2[1]], "r")

vec1DotVec2 = np.dot(vec1, vec2)
# vec2Norm = np.linalg.norm(vec2)
vec2Norm = np.sqrt(vec2[0]**2 + vec2[1]**2)
vec1OntoVec2 = (vec1DotVec2 / vec2Norm**2) * vec2

# ax[0].plot([0, vec1OntoVec2[0]], [0, vec1OntoVec2[1] ], "g")
ax[0].quiver(0, 0, vec1OntoVec2[0], vec1OntoVec2[1], angles="xy", scale_units="xy", scale=1, color="green", label="Vector")
# set limits for axes
ax[0].set_xlim(-1, 8)
ax[0].set_ylim(-1, 10)

#set Title of axis
ax[0].set_title("Vector Projection")
ax[1].set_title("Plot 2")

# display grid as background
ax[0].grid(True)


plt.show()