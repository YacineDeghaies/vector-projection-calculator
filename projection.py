import matplotlib.pyplot as plt
import numpy as np

#Create an figure and axes
fig, ax = plt.subplots()

#define vector coordinates
v = np.array([2, 4])
ax.plot([0, 0], [2, 2], "b")

plt.show()