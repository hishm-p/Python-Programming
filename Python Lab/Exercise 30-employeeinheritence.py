class employee:
    def __init__(self, empid, name, salary, address):
        self.empid = empid
        self.name = name
        self.salary = salary
        self.address = address

    def show(self):
        print("\nEMPLOYEE INFO OF",self.empid)
        print("-------------\n")
        print("Employee ID:",self.empid)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
        print("Employee Address:",self.address)

class teacher(employee):
    def __init__(self,empid,name,salary,address,department, subject):
        super().__init__(empid,name,salary,address)
        self.department = department
        self.subject = subject
        
    def show(self):
        super().show()
        print("Department:",self.department)
        print("Subject:",self.subject)
        


emp1 = employee(101,"Hisham P",12000,"Paravakkal")
t1 = teacher(102,"Hana",10000,"Paravakkal","Computer Applications","Maths")

t1.show()
emp1.show()