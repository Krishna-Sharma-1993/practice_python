print("Using class varaible + Normal function")
class Employee():
    emp_id: int=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.emp_id=self.generate_emp_id()

    def generate_emp_id(self):
        Employee.emp_id+=1
        return Employee.emp_id

    def get_details(self):
        print(f"name={self.name}\nage={self.age}\nemp_id={self.emp_id}")

print(f"{Employee.emp_id}")
e1=Employee("ABC", "25")
e1.get_details()
print(f"{Employee.emp_id}")
e2=Employee("DEF", "27")
e2.get_details()
print(f"{Employee.emp_id}")
e1.get_details()