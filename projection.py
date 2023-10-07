import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np


#vectors data
x1 = int(input("Type coordinate for vector A(x, y):\n x: "))
y1 = int(input(" y: "))
x2 = int(input("Type coordinate for vector B(x, y):\n x: "))
y2 = int(input(" y: "))

#Create a figure and axes
fig, ax = plt.subplots(figsize = (10,5) )

#Vectors
vec1 = np.array([x1, y1])
vec2 = np.array([x2, y2])

#draw Vector 1
ax.quiver(0, 0, vec1[0], vec1[1], angles="xy", scale_units="xy", scale=1, color="red", label="Vector 1")

#draw Vector 2
ax.quiver(0, 0, vec2[0], vec2[1], angles="xy", color="green", scale_units="xy", scale=1, label="Vector 2")

vec1DotVec2 = np.dot(vec1, vec2)
vec2Norm = np.linalg.norm(vec2) **2
# vec2Norm = np.sqrt(vec2[0]**2 + vec2[1]**2)
vec1OntoVec2 = (vec1DotVec2 / vec2Norm) * vec2

#projected vector
ax.quiver(0, 0, vec1OntoVec2[0], vec1OntoVec2[1], angles="xy", scale_units="xy", scale=1, color="gray", label="Projected Vector")

# set limits for axes
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 8)


#set Title of axis
ax.set_title("Vector Projection")

# display grid as background
ax.grid(True)

ax.legend()

plt.show()