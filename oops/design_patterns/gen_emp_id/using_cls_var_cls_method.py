print("Using class varaible + class method")
class Employeee():
    emp_id: int=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.emp_id=self.generate_emp_id()

    @classmethod
    def generate_emp_id(cls):
        cls.emp_id+=1
        return cls.emp_id

    def get_details(self):
        print(f"name={self.name}\nage={self.age}\nemp_id={self.emp_id}")

print(f"{Employeee.emp_id}")
e1=Employeee("ABC", "25")
e1.get_details()
print(f"{Employeee.emp_id}")
e2=Employeee("DEF", "27")
e2.get_details()
print(f"{Employeee.emp_id}")
e1.get_details()