try:
    f=open("xyz.txt",'r')
    data=f.read()
    print(data)
finally:
        f.close()
        print("close sucessfully")