from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True  # default value

# ✅ valid data
p1 = Product(name="Laptop", price=49999.99)
print(p1)

# ❌ invalid data
try:
    p2 = Product(name="Mouse", price="cheap")  # "cheap" is not a float
except Exception as e:
    print(e)
