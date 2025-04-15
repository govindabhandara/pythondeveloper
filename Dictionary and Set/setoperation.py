#set opeartion union
s1={1,2,3,4}
s2={3,4,5,6}
uni_set=s1.union(s2)
print(uni_set)

#set operation intersection
s1={1,2,3,4}
s2={3,4,5,6}
inter_set=s1.intersection(s2)
print(inter_set)

#set opearion difference
s1={1,2,3,4}
s2={3,4,5,6}
diff=s1.difference(s2)
print(diff)

#set opeartin symmetric_difference// exclusive
s1={1,2,3,4}
s2={3,4,5,6}
sym_diff=s1.symmetric_difference(s2)
print(sym_diff)

s1={1,3,5,7}
s2={3,4,5,6}
print(s1|s2) #for union
print(s1&s2) #for intersection
print(s1-s2) #for difference
print(s1^s2) #for symmetric difference