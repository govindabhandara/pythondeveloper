#in sets, sets is mutable but element is immutable
#we can pass tuple under .add but not list and dict 
collection=set()
collection.add(1)   #we can add 
collection.add(2)
collection.add("govinda")
collection.add(1.2)
print(collection)

collection.remove("govinda") #we can remove
print(collection)

collection.clear() #we can clear all element on sets
print(collection)

collection={"i","am","govinda","bhandara"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())


