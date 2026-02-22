# Program to predict population growth

# Formula: 
# Growth Formula: final population = initial population * (growth rate) * (total hours/growth period)
# initial population = starting organisms.
# growth rate = multiplication factor (example: 2 means doubling).
# growth period = hours required for one growth cycle.
# total hours = total time population grows

# Step 1: Input values from user

initial_population = int(input("Enter initial number of organisms: "))
growth_rate = float(input("Enter growth rate (greater than 0): "))
growth_period = float(input("Enter growth period (hours): "))
total_hours = float(input("Enter total growth time (hours): "))

# Step 2: Calculate number of growth cycles

growth_cycles = total_hours / growth_period

# Step 3: Calculate final population

final_population = initial_population * (growth_rate ** growth_cycles)

# Step 4: Display Result
print("--- Population Growth Prediction ---")
print("Initial Population: ", initial_population)
print("Final Population: ", final_population)