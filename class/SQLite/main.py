import sqlite3

from sqlExample import SQLExample

connection = sqlite3.connect("EmployeeDB.db")
emp = SQLExample('Usha',678,178000)
emp = SQLExample('Ntihin',123,178000)
emp = SQLExample('Bharat',456,178000)
emp = SQLExample('Syed',890,178000)
#emp.getEmployees(connection)
 