from collections import namedtuple
person=namedtuple("person",["name","age"])
p=person("govinda","24")
print(p.name)
print(p.age)