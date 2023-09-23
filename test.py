import matplotlib.pyplot as plt
import numpy as np

# Define grid coordinates
X, Y = np.meshgrid(np.arange(0, 10), np.arange(0, 10))

# Define vector components
U = np.cos(X)
V = np.sin(Y)

# Create a quiver plot
plt.quiver(X, Y, U, V, scale=5, color='blue')

# Customize plot properties
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quiver Plot Example')

# Show the plot
plt.show()