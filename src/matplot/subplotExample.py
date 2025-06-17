import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1,2,3,4, 5])
y = np.array([25, 90,145,35,176, 110])

plt.subplot(2,3,1)
plt.plot(x,y)


x = np.array([0, 1,2,3,4, 5])
y = np.array([35, 60,45,25,76, 90])

plt.subplot(2,3,2)
plt.plot(x,y)

x = np.array([0, 1,2,3,4, 5])
y = np.array([35, 60,45,25,76, 90])

plt.subplot(2,3,3)
plt.plot(x,y)

x = np.array([0, 1,2,3,4, 5])
y = np.array([35, 60,45,25,76, 90])

plt.subplot(2,3,4)
plt.plot(x,y)

x = np.array([0, 1,2,3,4, 5])
y = np.array([35, 60,45,25,76, 90])

plt.subplot(2,3,5)
plt.plot(x,y)


plt.show()