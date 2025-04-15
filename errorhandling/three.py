from insufficienterror import InsufficentBalError as LowBalError
acc_bal=15000
try:
    amount=int(input("enter number"))
    if acc_bal<amount:
        raise LowBalError("Buddy, Low balance please check it")
    else:
        print("please Withdraw and enjoy")
except LowBalError as err:
    print(err)
except:
    print("check the code! deafult Errors")
    
print("good morning")