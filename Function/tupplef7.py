def num(n):
    if(n==0):
        return 0
    return num(n-1)+n
sum=num(5)
print(sum)