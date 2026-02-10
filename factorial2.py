def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}")