# Function to calculate factorial using a loop

def factorial(n):
    result = 1

    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result

# Main Program: calculate factorial from 1 to 5
print("Factorials from 1 to 5:")

for number in range(1, 6):
    fact = factorial(number)
    print(f"{number}! = {fact}")