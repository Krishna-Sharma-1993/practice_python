print("Using iterators")
class GenEmpId:
    emp_id: int =0
    def __next__(self):
        GenEmpId.emp_id+=1
        return  GenEmpId.emp_id

class Employeeeee():
    gen_emp_id=GenEmpId()
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.emp_id=next(self.gen_emp_id)

    def get_details(self):
        print(f"name={self.name}\nage={self.age}\nemp_id={self.emp_id}")

e1=Employeeeee("ABC", "25")
e1.get_details()
e2=Employeeeee("DEF", "27")
e2.get_details()
e3=Employeeeee("GHI", "29")
e3.get_details()
e1.get_details()