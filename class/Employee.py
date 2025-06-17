class Employee:

    #constructor
    def __init__(self, name, e_Id, dept, salary):
        self.name = name
        self.e_Id = e_Id
        self.dept = dept
        self.salary = salary

    def showEmployee(self):
        print("Hello my name is: ", self.name)
        print("My Employee Id is: ", self.e_Id)
        print("I belong to "+ self.dept+" department")
        
        return{
            "type": "Employee",
            "name": self.name,
            "e_Id": self.e_Id,
            "department": self.dept
        }
        

    def calculateBonus (self, bonusRate =0.1):
        return self.salary * bonusRate
    
    def updateSalary(self, newSalary):
        if(newSalary >0):
            self.salary = newSalary
            return True
        return False

class Manager (Employee):

    def __init__(self, name, e_Id, salary, dept="Management", team_size =0 ):
        super().__init__(name, e_Id, dept, salary)
        self.team_size = team_size

    def calculateBonus(self, bonusRate = 0.15):
        baseBonus = super().calculateBonus(bonusRate)
        team_bonus = self.team_size * 1000
        return baseBonus + team_bonus
    
    def showDetails(self):
        details = super().showEmployee()
        details["type"] = "Manager"
        details["team_size"] = self.team_size
        return details
    
    def addTeamMembers(self):
        self.team_size += 1
        return self.team_size
        
