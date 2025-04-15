a = 256
b = 256
print(a is b)  # True (due to Python's integer caching)

c = 257
d = 257
print(c is d)  # False (in most cases, unless optimized)

var=None
print(var is None)

a=256
b=256 
print( a is b)

C=257
d=257
print(c is d)