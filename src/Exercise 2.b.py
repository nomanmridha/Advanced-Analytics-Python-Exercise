# Program to calculate sphere measurements. 

# Formula used: for a sphere with radius r: 
        # Diameter = 2r
        # Circumference = 2 * 3.14 * r
        # Surface Area = 4 * 3.14 * r ** 2
        # Volume = (4/3) * 3.14 * r ** 3

# Step 1: Input radius (floating-point number)

radius = float(input("Enter the radius of the sphere: "))

# Step 2: Calculate values

diameter = 2 * radius
circumference = 2 * 3.14 * radius
surface_area = 4 * 3.14 * radius ** 2
volume = (4/3) * 3.14 * radius ** 3

# Step 3: Display Results: 

print("--- Sphere Measurements---")
print("Radius: ", radius)
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface Area: ", surface_area)
print("Volume: ", volume)