# calculator/calculator.py

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, or an error message if y is zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y
