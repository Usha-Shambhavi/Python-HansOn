from Employee import Employee, Manager

#Initializing all the employees in our org
employees= {
    42423: Employee('Raj', 42423,'AI', 25000000),
    42427: Employee('Shasahk', 42427,'AI', 15000000),
    42429: Employee('Vamsi', 42429,'AI', 13000000),
    4765: Manager('Nitin', 4765, 180000000, "Management", 4)
}

#Display total payroll for our org
def totalPayroll(employees):
    totalSalary = 0
    for emp in employees.values():
        totalSalary += emp.salary
    print(totalSalary)

#Display Bonus and salary for all the employees in our org
def showBonusAndSalary():
    for e_id, emp in employees.items():
        print(emp.name +"'s salary is: ",emp.salary)
        bonus = emp.calculateBonus(0.12)
        print(emp.name +"'s bonus is: ",bonus)

#Finding employee from the collection
def findTheEmployee(empId):
    if (employees.get(empId)):
        return employees.get(empId)
    else:
        return []

#Display total payroll for our org
totalPayroll(employees)

print("\n")
#Displaying all the employees in our org
for emp_id, emp in employees.items():
    e = emp.showEmployee()
    print("\n")

#Bonues for all the employees in our org
showBonusAndSalary()

print("\n")

#Calibration for employee having less CTC
employees[42429].updateSalary(15000000)
print(employees[42429].name +"'s salary is: ",employees[42429].salary)
print("\n")

#Bonues for all the employees in our org
print("Bonus after salary incremental \n")
showBonusAndSalary()

print("\n")
#Display total payroll for our org
totalPayroll(employees)


eId = int(input("Input the employee id to find!"))
empL = findTheEmployee(eId)
if empL != []:
    empL.showEmployee()
else:
    print("Employee not found!")


'''
emp = Employee('Raj', 42423,'AI', 25000000)

emp.showEmployee()

print(emp.name ," bonus is added & here is the updated CTC: ",emp.calculateBonus())
'''