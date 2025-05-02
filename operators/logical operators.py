#Logical Operators 
a=20
b=10
print(not True) #not operator use in single operans
print(not False)
print(not (a>b) )

val1=True
val2=True
print("and operator:",val1 and val2)

val1=True
val2=False
print("and operator:",val1 and val2)

val1=False
val2=False
print("and operator:",val1 and val2)
#and operator used in 2 operands
#normally In an and operator when both value will true then 
# it will true otherwise it will false.

val1=True
val2=False
print("or operator:",val1 or val2)

val1=True
val2=True
print("or operato:", val1 or val2)

val1=False
val2=False
print("or operator:", val1 or val2)

val1=True
val2=False
print("or operator:", (a==b) or (a>b))


