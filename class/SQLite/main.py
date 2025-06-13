import sqlite3

from sqlExample import SQLExample

connection = sqlite3.connect("EmployeeDB.db")
emp = SQLExample('Nitin',124,178000)
#emp.getEmployees(connection)
