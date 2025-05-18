from dataclasses import dataclass
@dataclass
class person:
    name:str
    age:int
p=person("bob",30)
print(p.name)
print(p.age)