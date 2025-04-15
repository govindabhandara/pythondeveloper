"""Dictionary are used to store data values in key:value pairs
they are unordered ,mutable,(Changable)&don't allow duplicate 
"key":value to assign or add new dict["key"]="value" it works in pair form"""

dict = {
    "name":"pagal",
    "cgpa":9.6,
    "marks":[98,97,95],
}
print(dict)

info = {
    "key":"value",
    "name":"govinda",
    "learning":"python",
    "is_adult": True,
    12.99:32.899,
    "age":28,
    }
info["name"]="friend" #we can change name
info["surname"]="circle" #we can add key value pair
print(info)
print(info["key"])
print(info["name"])

null_dict={}    #we can create null dictionary
print(null_dict)
