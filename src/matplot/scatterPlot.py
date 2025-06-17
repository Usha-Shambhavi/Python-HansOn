import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10)
y = np.random.rand(10)

plt.scatter(x, y, color='orange')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Random Scatter Plot")

plt.show()