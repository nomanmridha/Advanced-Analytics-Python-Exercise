# Function to calculate exponential using a loop

def exponential(base, exponent):
    result = 1

    # Loop to multiply base exponent times
    for i in range(exponent):
        result = result * base

    # return after completing all multiplications
    return result
    

# Test the function with base = 2 and exponent = 16
base = 2
exponent_value = 16

answer = exponential(base, exponent_value)

# Display Result

print(f"{base}^{exponent_value} = {answer}")