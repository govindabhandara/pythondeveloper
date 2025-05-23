original=[1,2,3,2,4,5,6,3,4]
unique=[]
for item in original:
    if item not in unique:
        unique.append(item)
print(unique)