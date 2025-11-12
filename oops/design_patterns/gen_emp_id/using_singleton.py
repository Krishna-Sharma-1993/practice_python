# singleton 1
class GenEmpId:
    objEmpId = None
    
    class EmpId:
        emp_id : int = 0

    @classmethod
    def gen_emp_id(cls):
        if not cls.objEmpId:
            cls.objEmpId = cls.EmpId()
            cls.objEmpId.emp_id+=1
            return cls.objEmpId.emp_id
        else:
            cls.objEmpId.emp_id+=1
            return cls.objEmpId.emp_id

print(GenEmpId.gen_emp_id())
print(GenEmpId.gen_emp_id())
print(GenEmpId.gen_emp_id())
print(GenEmpId.gen_emp_id())
