import matplotlib.pyplot as plt
import numpy as np

#Create an figure and axes
fig, ax = plt.subplots()

# ax.plot([start_x, end_x], [start_y, end_y], "b")

#Vectors

vec1 = np.array([2, 2])
vec2 = np.array([6, 3.5])

#draw Vector 1
ax.plot([0, vec1[0]], [0, vec1[1]], "b")

#draw Vector 2
ax.plot([0, vec2[0]], [0, vec2[1]], "r")

vec1DotVec2 = np.dot(vec1, vec2)
# vec2Norm = np.linalg.norm(vec2)
vec2Norm = np.sqrt(vec2[0]**2 + vec2[1]**2)
vec1OntoVec2 = (vec1DotVec2 / vec2Norm**2) * vec2

print(vec1OntoVec2)
ax.plot([0, vec1OntoVec2[0]], [0, vec1OntoVec2[1] ], "g")
# set limits for axes
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 10)

#set Title of axis
ax.set_title("Vector Projection")

# display grid as background
plt.grid(True)

plt.show()