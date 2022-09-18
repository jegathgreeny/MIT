def factorial(n):
    """Outputs factorial of a number."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


instance = factorial(5)
print(instance)