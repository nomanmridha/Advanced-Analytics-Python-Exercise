# Function to calculate summation from low to high (inclusive)
def summation(low, high):
    total = 0
    
    # Loop from low to high inclusive
    for number in range(low, high + 1):
        total += number
    
    return total

# Test the function

low = int(input("Enter the low value: "))
high = int(input("Enter the high value: "))

result = summation(low, high)

print(f"Summation from {low} to {high} is {result}")