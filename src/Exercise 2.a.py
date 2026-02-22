# Program to calculate the surface area of a cube

# Surface area of a cube formula = 6 * (edge length)*2

# Step 1: Take edge length as integer input

edge = int(input("Enter the length of the cube's edge: "))

# Step 2: Calculate surface area

surface_area = 6 * edge ** 2

# Step 3: Display the result

print ("\n --- Cube Surface Area Result ---")
print ("Edge length: ", edge)
print ("Surface area of the cube: ", surface_area)