#A built in data type that let us  create immutable sequence of values
tup=(3,4,3,1,4,5,6)
print(tup[0])
print(tup[1])
print(type(tup))

print(tup[1:4]) #slicing
print(tup.index(4)) #returns index of first occurance 
print(tup.count(4)) #counts total occurance 


