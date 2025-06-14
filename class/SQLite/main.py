import sqlite3

from sqlExample import SQLExample

connection = sqlite3.connect("EmployeeDB.db")
#emp = SQLExample('Bharat',678,178000)
#emp.getEmployees(connection)

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.show()