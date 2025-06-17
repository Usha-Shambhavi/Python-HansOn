#Mean, Median and Mode
#Average, Mid Point, Common Value

import numpy as np
from scipy import stats

y = np.array([25, 90,145,35,176, 110])
print("Mean of Sales: ",np.mean(y))
print("Median of Sales: ",np.median(y))
print("Mode of Sales: ",stats.mode(y).mode)

#Standard Deviation
sd = np.std(y)
print("Standard Deviation for Sales: ",sd)

#Variance

print("Variance for Sales: ",sd * sd)

print("Variance for Sales: ",np.var(y))
