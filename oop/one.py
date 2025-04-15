class Account: #define a new class nameed "Account"
    "created by ....."  #this is the doc string that describes the class(though its incomplete)
    pass  # this is the place holder where no any implementation is is needed yet.
          # It allows the class definition to exist without any methods or attributes.
          #to maintain dummy block-using pass keyword

#object creation
a1=Account()
a2=Account()
a3=Account()
#a1,a2,a3 are all distinct Account objects.

print(a1)
print(a2)
print(a3)
#print the string representation of each objects , which by default shows:
#1) The class name Account
#2) The memory address (in hexadecimal) where the object is stored.
print(id(a1))
print(id(a2))
print(id(a3))
#Returns the unique identifier (memory address in decimal ) for each object .
# this will show that all three objects have different IDs, proving they're seperate instances.
