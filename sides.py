def calculate_result():
    print("N-Sides Calculator")
    num = float(input("Enter angle measure: "))
    if num == 180:
        print("Error: Flat line.")
    elif num < 0:
        print("Error: Invalid angle measure.")
    else:
        result = (360 / (180 - num))
        if abs(int(result)) == 2:
            print("Error: The shape is not a polygon.")
        elif result % 1 != 0:
            print("Error: The shape is not a regular polygon.")
        else:
            print("Your polygon has", abs(int(result)), "sides:")


calculate_result()
