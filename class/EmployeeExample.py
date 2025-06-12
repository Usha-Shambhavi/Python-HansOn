class Employee:

    def __init__(self, name, e_Id, dept):
        self.name = name
        self.e_Id = e_Id
        self.dept = dept

    def showEmployee(self):
        print("Hello my name is: ", self.name)
        print("My Employee Id is: ", self.e_Id)
        print("I belong to "+ self.dept+" department")



emp = Employee('Syed',42423, 'AI')
print(emp.name)
print(emp.e_Id)
print(emp.dept)

emp.showEmployee()