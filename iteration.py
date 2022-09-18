def factorial(n):
    """Outputs factorial of a number."""
    prod = 1
    for i in range(1, n + 1):
        prod *= i

    return prod


instance = factorial(5)
print(instance)
