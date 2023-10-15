#!/usr/bin/python3
def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {num} is {factorial(num)}")

