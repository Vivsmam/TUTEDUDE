import math

# Ask the user for a number
number = float(input("Enter a number: "))

# Calculations using math module
if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
else:
    square_root = "Undefined (cannot take square root of negative number)"
    natural_log = "Undefined (logarithm only for positive numbers)"

sine_value = math.sin(number)  # Sine works for any real number (in radians)

# Display the results
print("\n--- Calculated Results ---")
print(f"Square root: {square_root}")
print(f"Natural logarithm (log base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")
