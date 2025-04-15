from random import randint,choices
lootery_num=[]
for x in range(10):
    lootery_num.append(randint(100000,999999))
    print(lootery_num)
print(choices(lootery_num))