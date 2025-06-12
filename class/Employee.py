class Employee:

    def __init__(self, name, e_Id, dept, salary):
        self.name = name
        self.e_Id = e_Id
        self.dept = dept
        self.salary = salary


    def showEmployee(self):
        print("Hello my name is: ", self.name)
        print("My Employee Id is: ", self.e_Id)
        print("I belong to "+ self.dept+" department")

    def calculateBonus (self, bonusRate =0.1):
        return self.salary * bonusRate
    
    def updateSalary(self, newSalary):
        if(newSalary >0):
            self.salary = newSalary
            return True
        return False
    