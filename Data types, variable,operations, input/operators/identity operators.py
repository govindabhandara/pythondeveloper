#this operator is used to check whether two objects are same type or not.
#they share same memory or  not
#there are two identity operators : 'is' and 'is not'
#always return 'True or False ' as output 
a=10
b=5
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

a=10
b=10
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

a=10
b=9
print(a is not b )
print(id(a))
print(id(b))

a=10
b=5
c=a
print(c is b)
print(b is c)
print(id(a))
print(id(b))
print(id(c))

num1=None
num2=None
print(num1 is num2)