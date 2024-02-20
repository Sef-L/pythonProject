import math
loop = 1
def x_den(side_value, angle, operation):
    answer = side_value / operation(math.radians(angle))
    return answer

def x_num(side_value, angle, operation):
    answer = side_value * operation(math.radians(angle))
    return answer
while loop == 1:
    angle_given = float(input("What angle do you have?: "))
    side_given_value = float(input("What is the length of the side you have?: "))
    side_given = int(input("What side do you have relative to the angle given?\n1 - Hypotenuse\n2 - Adjacent\n3 - Opposite\nChoose 1/2/3: "))
    looking_for = int(input("What side are you looking for relative to the angle given?\n1 - Hypotenuse\n2 - Adjacent\n3 - Opposite\nChoose 1/2/3: "))

    if side_given == 1 and looking_for == 3:
        # HAVE HYPOTENUSE, LOOKING FOR OPPOSITE, SINE.
        answer = x_num(side_given_value, angle_given, math.sin)
        print("\n\nThe missing side length is: ",answer,"\n\n")

    elif side_given == 3 and looking_for == 1:
        # HAVE OPPOSITE, LOOKING FOR HYPOTENUSE, SINE.
        answer = x_den(side_given_value, angle_given, math.sin)
        print("\n\nThe missing side length is: ",answer,"\n\n")

    elif side_given == 1 and looking_for == 2:
        # HAVE HYPOTENUSE, LOOKING FOR ADJACENT, COSINE.
        answer = x_num(side_given_value, angle_given, math.cos)
        print("\n\nThe missing side length is: ",answer,"\n\n")

    elif side_given == 2 and looking_for == 1:
        # HAVE ADJACENT, LOOKING FOR HYPOTENUSE, COSINE.
        answer = x_den(side_given_value, angle_given, math.cos)
        print("\n\nThe missing side length is: ", answer, "\n\n")

    elif side_given == 2 and looking_for == 3:
        # HAVE ADJACENT, LOOKING FOR OPPOSITE, TANGENT.
        answer = x_num(side_given_value, angle_given, math.tan)
        print("\n\nThe missing side length is: ",answer,"\n\n")

    elif side_given == 3 and looking_for == 2:
        # HAVE OPPOSITE, LOOKING FOR ADJACENT, TANGENT.
        answer = x_den(side_given_value, angle_given, math.tan)
        print("\n\nThe missing side length is: ", answer, "\n\n")

    loop = int(input("Do you want to continue?\n1 - Yes\n2 - No\nChoose 1/2: "))
    if loop == 1:
        continue
    else:
        break