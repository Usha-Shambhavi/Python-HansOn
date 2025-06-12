from Employee import Employee


employees= {
    401: Employee('Raj', 42423,'AI', 25000000),
    402: Employee('Shasahk', 42427,'AI', 15000000),
    403: Employee('Vamsi', 42429,'AI', 13000000)
}

for emp_id, emp in employees.items():
    e = emp.showEmployee()

for e_id, emp in employees.items():
    bonus = emp.calculateBonus(0.12)
    print(emp.name +"'s bonus is: ",bonus)






'''
emp = Employee('Raj', 42423,'AI', 25000000)

emp.showEmployee()

print(emp.name ," bonus is added & here is the updated CTC: ",emp.calculateBonus())
'''