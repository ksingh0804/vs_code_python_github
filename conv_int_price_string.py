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







