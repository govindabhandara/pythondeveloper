#remove (x) vs discard(x)
#if element present in case both method id
#remove and discard method remove specified element
#if element not present -remove(x) method throw error 
# but discard(x) method throw doesnot error

s1={101,102,103,104}
# s1.remove(105) #key error
s1.discard(105)
print(s1)
