# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number
number = 5

# Call the function and print the result
print(f"The factorial of {number} is: {factorial(number)}")
