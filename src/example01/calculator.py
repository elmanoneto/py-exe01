def sum(a, b):
    return float(a) + float(b)

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b