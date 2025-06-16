import sqlite3

from sqlExample import SQLExample

connection = sqlite3.connect("EmployeeDB.db")
#emp = SQLExample('Bharat',678,178000)
#emp.getEmployees(connection)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()

