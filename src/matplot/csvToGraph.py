import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df          =   pd.read_csv('colors.csv')
categories  =   df['Colors'].values
qty         =   np.array(df['Quantity'].values)

plt.bar(categories,qty, color="blue", edgecolor="black")

plt.xlabel("Colors")
plt.ylabel("Quantity")

plt.title("Qyantity of Colors")

plt.show()