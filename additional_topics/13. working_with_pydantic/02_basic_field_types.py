from pydantic import BaseModel


class Product(BaseModel):
    id: int         # Product ID
    name: str       # Product name
    price: float    # Product price
    in_stock: bool  # Is the product in stock?


product = Product(id=1, name="Laptop", price=999.99, in_stock=True)
print(product)


product2 = Product(id="2", name="Mouse", price="19.99", in_stock="True")

print(product2)
print(product2.id, type(product2.id))
print(product2.name, type(product2.name))
print(product2.price, type(product2.price))
print(product2.in_stock, type(product2.in_stock))

# ---
# Summary:
# This program demonstrates how Pydantic models validate and convert basic field types.
# You can pass compatible types (like strings for numbers), and Pydantic will handle conversion.
