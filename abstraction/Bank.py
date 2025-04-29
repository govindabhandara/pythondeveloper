
from abc import abstractmethod,ABC
class Bank(ABC):
    @abstractmethod   #decorator
    def cal_bal(self):
        pass

