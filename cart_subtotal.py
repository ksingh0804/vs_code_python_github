
# CART-102 — Cart subtotal in cents
# Type: Story · Priority: P3 · Estimate: 3 points

# Service: pricing-engine
# Self-checkout and the associate “price this cart” handheld share this.
# One-cent drift and the till is short at close.

from typing import TypedDict

class LineItem(TypedDict):
    sku: str
    name: str
    unit_price_cents: int
    quantity: int


def cart_subtotal_cents(items: list[LineItem]) -> int:
    # Creating a variable to store total amount
    total = 0
    # Loop
    for item in items:
        # items is list of dictionaries, item is one dictionary
        price = item["unit_price_cents"]   # KeyError if missing — that is OK
        qty = item["quantity"]
        # If negative value throw an error
        if price < 0 or qty < 0:
            raise ValueError('Price or quantity cannot be negative')
        # In every loop we will be adding values to the total 
        total += price * qty
    return total
