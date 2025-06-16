import numpy as np

import matplotlib.pyplot as plt

print("Pi Value: ",np.pi)

print("Twice Pi Value: ",2 * np.pi)
x = np.linspace(0, 2 * np.pi, 500)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y, label="sin(x)", color="red")

plt.plot(x, cos_y, label="cos(x)", color="black")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Sine and Cosine Plot")

plt.show()