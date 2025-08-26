import math

def multiply_tuple_math(tup):
    """Calculate product using math.prod()"""
    return math.prod(tup)

# Example usage
numbers_tuple = (2, 3, 4, 5)
result = multiply_tuple_math(numbers_tuple)
print(f"Product of {numbers_tuple}: {result}")