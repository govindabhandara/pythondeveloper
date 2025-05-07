#for loop in list
''' 
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit) 
'''
#for loop in string
'''
for char in 'hello':
    print(char)'
'''
# for loop in range
'''
for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

for i in range(0,10,2):
    print(i) 

for i in range (0,10,3):
    print(i)'
'''
#looping with index and value
'''
fruits=["banana","cherry","apple"]
for index, fruit in enumerate(fruits):
    print(index,fruit)'

fruits=["apple","banana","cherry"]
for index, fruit in enumerate(fruits,start=1):
    print(f'*{index} fruit')
'''
#for loop with tuples
'''
points=[(1,2),(3,4),(5,6)]
for i,(x,y) in enumerate(points):
    print(f'point {i}:x={x},y={y}')
'''
#for loop with finding indices for  specific items
'''
fruits=["apple","banana","cherry"]
target='banana'
for i, fruit in enumerate(fruits):
    if fruit=='banana':
        print(f'found {target} at index {i}')'

ani=["cat","dog","rat"]
target='dog'
for i, an in enumerate(ani):
    if an=='dog':
        print(f" found {target} in index {i}")
'''
#for loop in dictionary

'''
person={"Name":"Govinda","Age":30,"City":"Banglore"}
for i in person:
    print(i,person[i])'

Dic={"animal":"Cat", "Qnty":40,"location":"banglore"}
for i in Dic:
    print(i,Dic[i])
'''
#for nested for loop
'''for i in range(3):
    for j in range(2):
        print(i,j)'
'''
#for using else with for loop
'''
for i in range(3):
    print(i)
else:
    print("loop complete")'
'''
#for loop in break and continue and pass
'''
for i in range(5):
    if i==2:
        continue
    if i==4:
        break
    print(i)'

for i in range(5):
    pass  # Does nothing 5 times
print(i)'

for num in [1, 2, 0, 4, 5]:
    if num == 0:
        pass  # Do nothing for zero
    else:
        print(10/num)
'''
# even number
'''
n=int(input("enter your number:"))
for n in range(1,n+1):
    if n%2==0:
        print("even number:",n)
'''
    #factorial
'''
num=int(input("enter number"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"{num} of factorial is {factorial}") 
'''
#sum
'''
n=int(input("enter number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("sum is:",sum)
'''
#largest number
'''
numbers=[23,54,12,87,90,34]
max_num=numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
print(f"largest num is:{max_num}")
'''
# count vowel in a string
'''
text="Programming is fun."
vowels='aeiouAEIOU'
count=0
for char in text:
    if char in vowels:  
        count+=1
print("no of vowels:",count)
'''
# Print Fibonacci sequence up to n terms
'''
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
'''
# Is_prime or not
'''
n=int(input("enter number"))
prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        prime=False
        break
print(f"{n} is prime {prime}")
'''
