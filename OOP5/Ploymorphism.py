class Emp:
    def cal_tax(self):
        print("emp class -call Tax method")

class PE(Emp):
    def cal_tax(self):
        print("PE class - cal Tax method")

class CE(Emp):
    def cal_tax(self):
        print("CE class - cal Tax method")

def exec(obj):
    obj.cal_tax()

exec(Emp())
exec(PE())
exec(CE())
    