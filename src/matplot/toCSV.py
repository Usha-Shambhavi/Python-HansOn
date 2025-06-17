#Step 1: We have the hard coded values
#Step 2: frame the data
#Step 3: Convert this framed data to .csv file

import numpy as np
import pandas as pd

#data
data = {
    'Colors' : ["red", "green", "yellow", "magenta", "brown", "purple"],
    'Quantity' : [25, 90,145,35,176, 110]
}

df = pd.DataFrame(data)
df.to_csv('colors.csv', index=False)

# Read the US Sales data from csv and then plot a bar graph having Sales by month
