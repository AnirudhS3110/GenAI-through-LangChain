from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

p1 : Person = {
    'name':"ani",
    'age': 45
}

print(p1)