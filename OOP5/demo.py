from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass
        
class Account(Bank):
    min_bal=500  #static variable- only one copy create @class level
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def cal_bal(self):
        return self.acc_bal-self.min_bal
    
a1=Account(101,"Rahul",5000)
print(a1.__dict__)
print(a1.cal_bal())
    
        