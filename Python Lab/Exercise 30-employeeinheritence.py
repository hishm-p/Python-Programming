class employee:
    def __init__(self, empid, name, salary, address):
        self.empid = empid
        self.name = name
        self.salary = salary
        self.address = address

    def show(self):
        print("\nENTERED INFO")
        print("-------------\n")
        print("Employee ID:",self.empid)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
        print("Employee Address:",self.address)

class teacher(employee):
    def __init__(self, department, subject):
        super().__init__(empid,name,salary,address)
        self.department = department
        self.subject = subject
        
    def show(self):
        super().show()
        print("Department:",self.department)
        print("Subject:",self.subject)
        
print("\nENTER YOUR INFO")
print("---------------\n")
empid = int(input("Enter Employee ID:"))
name = input("Enter Employee Name:")
salary = float(input("Enter Salary:"))
address = input("Enter your Address:")
department = input("Enter your Department:")
subject = input("Enter the subject taught by you:")

emp1 = employee(empid,name,salary,address)
t1 = teacher(department,subject)

t1.show()