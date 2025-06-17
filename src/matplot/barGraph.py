import numpy as np
import matplotlib.pyplot as plt


#data
colorCollection = ["red", "green", "yellow", "magenta", "brown", "purple"]
qty = np.array([25, 90,145,35,176, 110])

plt.bar(colorCollection,qty, color="blue", edgecolor="black")

plt.xlabel("Colors")
plt.ylabel("Quantity")

plt.title("Sales by week")

plt.show()