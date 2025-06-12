from Employee import Employee

#Initializing all the employees in our org
employees= {
    42423: Employee('Raj', 42423,'AI', 25000000),
    42427: Employee('Shasahk', 42427,'AI', 15000000),
    42429: Employee('Vamsi', 42429,'AI', 13000000)
}


def totalPayroll(employees):
    totalSalary = 0
    for emp in employees.values():
        totalSalary += emp.salary
    print(totalSalary)


totalPayroll(employees)

print("\n")
#Displaying all the employees in our org
for emp_id, emp in employees.items():
    e = emp.showEmployee()
    print("\n")

#Bonues for all the employees in our org
for e_id, emp in employees.items():
    print(emp.name +"'s salary is: ",emp.salary)
    bonus = emp.calculateBonus(0.12)
    print(emp.name +"'s bonus is: ",bonus)

print("\n")


employees[42429].updateSalary(15000000)
print(employees[42429].name +"'s salary is: ",employees[42429].salary)
print("\n")



print("Bonus after salary incremental \n")
for e_id, emp in employees.items():
    print(emp.name +"'s salary is: ",emp.salary)
    bonus = emp.calculateBonus(0.12)
    print(emp.name +"'s bonus is: ",bonus)

print("\n")

totalPayroll(employees)

'''
emp = Employee('Raj', 42423,'AI', 25000000)

emp.showEmployee()

print(emp.name ," bonus is added & here is the updated CTC: ",emp.calculateBonus())
'''