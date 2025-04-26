from Bank import Bank
class Account(Bank):
    min_bal=500  #static variable- only one copy create @class level
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal-amount

    @classmethod
    def update_min_bal(cls,amount):
        Account.min_bal=amount
    
    @staticmethod
    def cal_roi():
        return 9
    
    def cal_bal(self):
        return self.acc_bal-self.min_bal
    
a1=Account(101,"Rahul",5000)
a1.deposit_amount(10)
Account.update_min_bal(600)
print(a1.__dict__)
print(a1.cal_bal())