# Program to find GCD using Euclid's Algorithm and display each step

# Step 1: Input two positive integers
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

# Step 2: Ensure a is the larger number
if b > a:
    a, b = b, a

print("\n--- Euclid's Algorithm Steps ---")

# Step 3: Apply Euclid's algorithm
step = 1
while b != 0:
    remainder = a % b
    print(f"Step {step}: {a} ÷ {b} = remainder {remainder}")
    
    # Replace numbers
    a, b = b, remainder
    step += 1

# Step 4: Final GCD
print("\nGCD is:", a)