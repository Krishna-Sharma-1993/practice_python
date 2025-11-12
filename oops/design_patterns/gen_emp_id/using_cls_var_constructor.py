print("Using class varaible + with constructor")
class Employeeee():
    emp_id: int=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        Employeeee.emp_id+=1
        self.emp_id=Employeeee.emp_id

    def get_details(self):
        print(f"name={self.name}\nage={self.age}\nemp_id={self.emp_id}")

print(f"{Employeeee.emp_id}")
e1=Employeeee("ABC", "25")
e1.get_details()
print(f"{Employeeee.emp_id}")
e2=Employeeee("DEF", "27")
e2.get_details()
print(f"{Employeeee.emp_id}")
e1.get_details()