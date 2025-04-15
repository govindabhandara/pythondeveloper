
from insufficienterror import InsufficentBalError

amount=int(input("enter number"))
acc_bal=15000
if acc_bal<amount:
    raise InsufficentBalError("low balance")
else:
    print("withdraw and enjoy")
    print("good morning")