import math

# Get the radius from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume using the formula V = (4/3) * pi * r^3
volume = (4 / 3) * math.pi * radius**3

# Calculate the surface area using the formula A = 4 * pi * r^2
surface_area = 4 * math.pi * radius**2

# Print the calculated volume and surface area
print("Volume of the sphere:", volume)
print("Surface area of the sphere:", surface_area)