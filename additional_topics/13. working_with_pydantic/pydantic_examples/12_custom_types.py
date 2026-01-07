"""
12_custom_types.py
Shows how to use custom types in Pydantic models.
"""
from pydantic import BaseModel
from pydantic.types import PositiveInt

class Order(BaseModel):
    order_id: PositiveInt
    amount: float

order = Order(order_id=10, amount=99.99)
print(order)
