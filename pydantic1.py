from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True   # default value

# Valid input
user = User(id="1", name="Alice")
print(user)
# → id=1 name='Alice' is_active=True

# Invalid input
try:
    User(id="abc", name="Bob")
except Exception as e:
    print(e)
