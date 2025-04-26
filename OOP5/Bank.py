'''class Bank():
    def cal_bal():
        pass
h1=Bank()
print(id(h1))'''

from abc import abstractmethod,ABC
class Bank(ABC):
    @abstractmethod   #decorator
    def cal_bal(self):
        pass
'''TypeError: Can't instantiate abstract class Bank without an implementation for abstract method 'cal_bal'''
