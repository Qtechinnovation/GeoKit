def calculate_angles():
    num_sides = int(input("Enter the number of sides of the polygon: "))
    if num_sides < 3:
        print("Error: A polygon must have at least 3 sides.")
    else:
        exterior_angle = 360 / num_sides
        interior_angle = 180 - exterior_angle
        print("Exterior Angle:", exterior_angle)
        print("Interior Angle:", interior_angle)

calculate_angles()