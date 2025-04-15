# print(10/0)

try:
    print(10/0)  #program creating error
    # raise ZeroDivisionError("Go to movie") #we are creating and throw
except ZeroDivisionError as err:
    print(err)
