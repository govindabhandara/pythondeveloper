from abc import ABC
class Bank(ABC):
    def cal_bal(self):
        print("cal_bal method")

h1=Bank()
print(id(h1))
           