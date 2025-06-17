import numpy as np


y = np.array([25, 90,145,35,176, 110])

percentile = np.percentile(y, 90)

print("Percentile of Y is: ",percentile)