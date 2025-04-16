class Employee:
    org_name='TCS' #static variable

    def __init__(self,id,name,sal):
        pass
        # self.emp_id=id
        # self.emp_name=name
        # self.emp_sal=sal

e1=Employee(101,'rahul',45000.45)
e2=Employee(102,'soniya',55000.55)
e3=Employee(103,'priyanka',65000.5)
print(Employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
        