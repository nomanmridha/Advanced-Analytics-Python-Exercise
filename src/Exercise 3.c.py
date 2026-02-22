# Program to calculate sum and average of user-entered numbers.

total = 0
count = 0

print("Enter numbers one by one. Press Enter without typing anything to finish")

while True:
    user_input = input("Enter a number: ")

    # Stop if Enter key pressed without input
    if user_input == "":
        break

    number = float(user_input)
    total += number
    count += 1

# Calculate average

if count > 0:
    average = total / count
else:
    average = 0

# Display Results

print("--- Result ---")
print("Sum: ", total)
print("Average: ", average)
