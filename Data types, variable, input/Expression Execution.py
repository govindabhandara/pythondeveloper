A,B=2,3
txt="@"
print(A*txt*B)
#it's for the string and numberic value operate together with *

A,B="2",3
txt="@"
print((A+txt)*B)
#it's string and string can operate with *

A,B,C=2,3,4
print(A*B+C)
#numberic value can operate with all arithmetic operators +,-,*,/,%,//,**

A,B = 2,5.5
print(A*B)
#Arithmetic expression with integer and float will result in float 
 
A,B=10,5
C=A/B
print(C)
#Result of division operator with two integer will be float

A,B=1.5,3
C=A//B
print(C,A/B)
#integer divisin with float and int will give int displayed as float

A,B=12,5
C=A//B
print(C)
A,B=-12,5
print(A//B)
A,B=12,-5
print(A//B)
#floor gives closest integer , which is lesser than or equal to the float value 
#result of (A//B) is same as floor A/B)

A,B=-5,2
C=A%B
print(C)
A,B=5,2
C=A%B
print(C)
A,B=5,-2
C=A%B
print(C)

#Remainder is negative when when denominator is negative Otherwise positive
