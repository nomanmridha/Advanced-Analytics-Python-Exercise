# List with positive and negative numbers
data = [-10, 20, -30, 40, -50]

# Loop to replace each number with its absolute value
for i in range(len(data)):
    data[i] = abs(data[i])

# Display result
print("Updated list with absolute values:", data)