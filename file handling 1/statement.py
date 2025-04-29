with open("xyz.txt",'r') as f:
    data=f.read()
    new_data=data.replace("which","this")
    print(new_data)