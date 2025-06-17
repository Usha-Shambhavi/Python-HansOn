import sqlite3

class SQLExample:
    def __init__(self, name, e_Id, salary):
        print("Connection to SQLite")
        connection = sqlite3.connect("EmployeeDB.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS employee (e_Id INTEGER PRIMARY KEY, empName TEXT, salary REAL)")
        connection.commit()

        cursor.execute("INSERT INTO employee (e_Id, empName, salary) VALUES (?,?,?)", (e_Id, name, salary))
        connection.commit()
        cursor.execute("SELECT * from employee")
        print(cursor.fetchall())
    
    '''def getEmployees(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * from employee")
        print(cursor.fetchall())'''
