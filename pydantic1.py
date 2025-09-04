from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

# valid
p1 = Person(name="Alice", age=30)
print(p1)

# invalid
try:
    p2 = Person(name="Bob", age="thirty")  # string instead of int
except Exception as e:
    print(e)
