#bitwise operator
#in bitwise operator are used to perform an operation individual by binay number
#there are six bitwise operators 1) & Bitwisw AND 2) | Bitwise OR 3) ~ Bitwise NOT 4) 
# ^ Bitwise XOR  5) << bitwise left shift 6) >> bitwise right shift 
#precedence from ~ (highest),<<>>,&,^,|(lowest)

a=0b1010
b=0b1100
c=a&b
print(bin(c)) 

c=a|b
print(bin(c))
c=~a
print(bin(c))

c=a^b
print(bin(c))

c=a>>b
print(bin(c))

c=a<<c
print(bin(c))

