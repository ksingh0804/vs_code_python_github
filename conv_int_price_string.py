# Day 1 — Sprint 0, pricing-engine
# Shared library. Shelf-tag printers and POS both import it. Overnight we print on the 
# order of millions of tags. Keep these functions tiny and allocation-light.
# Two tickets. Both are required. Do PRICE-101 first.

# PRICE-101 — Format shelf-tag price from integer cents
# Type: Story · Priority: P3 · Estimate: 2 points

# Service: pricing-engine
# Printers currently concatenate strings and we get "$1.9" instead of "$1.90". Cashiers then fight customers. Fix is a single function they will all call.


# This function converts an integer representing cents into a formatted price string 

def price_func(cents: int) -> str:
    # first check for integer
    if type(cents) is not int:
        #TypeError check
        raise TypeError('This is not integer, you provided ', type(cents).__name__)
    # if value is negative sign = '-' or else sign will be empty string
    sign = '-' if cents < 0 else ''
    # divmod returns tuple cents//100 and cents%100 
    # using absolute value for negative cents 
    dollar, remaining_cents = divmod(abs(cents), 100)
    # :02d will make sure we have 05 cents instead of 5 cents
    return f'{sign}${dollar}.{remaining_cents:02d}'

#Checking different values for the test 
print(price_func(1999))
print(price_func(0))
print(price_func(-101))







