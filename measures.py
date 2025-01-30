def calculate_sum_of_interior_angles():
    num_sides = int(input("Enter the number of sides of the polygon: "))
    if num_sides < 3:
        print("Error: A polygon must have at least 3 sides.")
    elif num_sides % 1 != 0:
        print("Error: The number of sides must be an integer.")
    else:
        sum_of_interior_angles = (num_sides - 2) * 180
        print("The sum of the measures of the interior angles is:",
              sum_of_interior_angles)


calculate_sum_of_interior_angles()
