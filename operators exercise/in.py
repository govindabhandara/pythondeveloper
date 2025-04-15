s1 = "hello"
s2 = "hello"
print(s1 is s2)  # What will this output?

s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # What will this output? Why?

def modify_list(lst):
    lst.append(4)
    return lst

original = [1, 2, 3]
modified = modify_list(original)
print(original is not modified)  # What will this output?