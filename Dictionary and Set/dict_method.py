student={
    "name":"govinda",
    "subject":{
        "chem":98,
        "math":87,
        "phy":97,
        "bio":96,
    }
}
print(student.keys()) #only outer layers come from nested dict it cannot come.
print(len(student))
print(len(list(student.keys()))) #myDict.keys() return all keys
print(student.values()) #return all the values
print(list(student.values()))
print(student.items()) #return all (key, val) pairs of tuples
print(list(student.items()))
print(student.get("name")) #returns the key according to the value
pairs=list(student.items())
print(pairs[0])

student.update({"city":"banglore"}) #insert the specific items to the dictionary
print(student) 
new_dict={"name":"romeo","city":"banglore"}
student.update(new_dict)
print(student)
