# List of student ages (example data)
ages = [23, 19, 21, 18, 25, 20, 17, 22, 24, 20]

# Step 1: Asume the first age is the youngest.
youngest = ages[0]

# Step 2: Loop through the list to find the smallest age.
for age in ages:
    if age < youngest:
        youngest = age

# Step 3: Display the result
print("Ages List:", ages)
print("The youngest student's age is:", youngest)
