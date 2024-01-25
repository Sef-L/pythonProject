loop = 1
def ratio(x,y):
    return y/x

while loop == 1:

# Setting up Variables
# PAINFUL, VERY PAINFUL TO TRY TO THINK ABOUT IN ADVANCE! I LOWK REWROTE THIS SECTION 7 TIMES!
# Coding is hard.

    hypotenuse = int(input("What is the hypotenuse of the triangle?: "))
    adjacent = int(input("What is the length adjacent leg?: "))
    opposite = int(input("What is the length of the opposite leg?: "))
    operation = input("What are you looking for? \n1 - sin \n2 - cos \n3 - tan \nChoose 1/2/3: ")
    display_format = input("How would you like the answer displayed?\n1 - Equation\n2 - Answer\nChoose 1/2: ")

# Actual code
# This part was very easy, a lot of copy and paste...

    if operation == "1":
        # SINE
        if display_format == "1":
            print('\n\n',opposite,"/",hypotenuse,'\n\n')
        elif display_format == "2":
            print('\n\n',(ratio(opposite,hypotenuse)),'\n\n')
        else:
            print('\n\n'"You have made an error. Please try again.")
            continue
    elif operation == "2":
        # COSINE
        if display_format == "1":
            print('\n\n',adjacent,"/",hypotenuse,'\n\n')
        elif display_format == "2":
            print('\n\n',(ratio(adjacent, hypotenuse)),'\n\n')
        else:
            print('\n\n'"You have made an error. Please try again.")
            continue
    elif operation == "3":
        # TANGENT
        if display_format == "1":
            print('\n\n',opposite,"/",adjacent,'\n\n')
        elif display_format == "2":
            print('\n\n',(ratio(opposite, adjacent)),'\n\n')
        else:
            print('\n\n'"You have made an error. Please try again.")
            continue
    else:
        print('\n\n'"You have made an error. Please try again.")
        continue
    loop = int(input("Do you want to continue?\n1 - yes\n2 - no\nChoose 1/2: "))

# Syntax errors suck!