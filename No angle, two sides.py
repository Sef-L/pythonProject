import math
loop = "1"
def calculation(side1, side2, operation):
    result = math.degrees(operation(side1/side2))
    return result

while loop == "1":
    side_value_1 = float(input("What is the length of the first side?: "))
    side_location_1 = (input("""Where is the length in question relative to the angle in question?
    1 - Opposite
    2 - Adjacent
    3 - Hypotenuse
    Choose 1/2/3: """))
    side_value_2 = float(input("What is the length of the second side?: "))
    side_location_2 = input("""Where is the length in question relative to the angle in question?
    1 - Opposite
    2 - Adjacent
    3 - Hypotenuse
    Choose 1/2/3: """)
    print("\n\n\n")
    if side_location_1 == "1" and side_location_2 == "2":
        answer = calculation(side_value_1, side_value_2,math.atan)
        print(answer)
    elif side_location_1 == "2" and side_location_2 == "1":
        answer = calculation(side_value_2, side_value_1,math.atan)
        print(answer)
    elif side_location_1 == "2" and side_location_2 == "3":
        answer = calculation(side_value_1, side_value_2,math.acos)
        print(answer)
    elif side_location_1 == "3" and side_location_2 == "2":
        answer = calculation(side_value_2, side_value_1,math.acos)
        print(answer)
    elif side_location_1 == "1" and side_location_2 == "3":
        answer = calculation(side_value_1, side_value_2,math.asin)
        print(answer)
    elif side_location_1 == "3" and side_location_2 == "1":
        answer = calculation(side_value_2, side_value_1,math.asin)
        print(answer)
    loop = input("\n\n\nWould you like to continue?\n1 - Yes\n2 - No\nChoose 1/2: ")
    if loop == "1":
        continue
    else:
        break