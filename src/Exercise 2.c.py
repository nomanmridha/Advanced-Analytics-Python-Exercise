# Program to calculate total weekly pay including overtime. 

# Pay Formula: Total weekly pay = (hourly wage * regular hours) + (Overtime hours * 1.5 * hourly wage)

# Step 1: Input Values

hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

# Step 2: Calculate regular pay

regular_pay = hourly_wage * regular_hours

# Step 3: Calculate Overtime pay

overtime_pay = overtime_hours * 1.5 * hourly_wage

# Step 4: Calculate total weekly pay

total_pay = regular_pay + overtime_pay

# Step 5: Display Results

print("--- Weekly Pay Summary---")
print("Regular pay: ", regular_pay)
print("Overtime Pay: ", overtime_pay)
print("Total Weekly Pay: ", total_pay)