#set is the collection of unordered items.
#each element in the set must be unique and immutable
#repeated element stored only once, so it resolved from set={1,2,2,2} to set={1,2}
#we cannot store list and dict in sets because they are mutable.
# boolean,int, str,float,tuple all we can store in set.
collection={1,2,3,4}
print(collection)
print(type(collection))
print(len(collection))

# set={}
# print(type(set)) #empty dictionary so we have to use following syntax

set=set()
print(type(set))
