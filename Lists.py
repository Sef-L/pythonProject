# number_checker.py

def main():
    # TODO: Prompt the user to enter an integer and store it in the variable 'number'.
    number = int(input('Choose a number'))

    # TODO: Determine if the number is positive, negative, or zero and print the appropriate message.
    # Hint: Use comparison operators (>, <, ==) to check if the number is positive, negative, or zero.
    if number == 0:
        print('Number is 0')
    elif number > 0:
        print('The number is positive')
    else:
        print('The number is negative')

    # TODO: Check if the number is even or odd and print the message.
    # Hint: Use the modulo operator (%) to determine if a number is even or odd.
    # if (number % 2) == 0:
    #     print ("Even")
    # else:
    #     print ("Odd")

    # TODO: Check if the number is divisible by 5 and print the message.
    # Hint: To check if a number is divisible by 5, the remainder when divided by 5 should be 0.
    # if (number % 5) == 0:
    #    print ("Divisable by 5")
    # else:
    #    print ("Not divisable by 5")

    # Advanced Task: If the number is positive and even, check if it is also a multiple of 10.
    # Hint: Combine conditions using 'and'. A number is a multiple of 10 if the remainder when divided by 10 is 0.
    # if (number % 10) == 0:
    #     print ("Divisable by 10")
    # else:
    #     print ("Not divisable by 10")

    divisor = int(input('What number do you want to check?: '))

    if (number % divisor) == 0:
        print(f"Divisable by {divisor}")
    else:
        print(f"Not divisable by {divisor}")

    def search(search_grade, stu_grades):
        found = False
        i = 0
        while not found:
            user_choice = input('1 to search, \n2 to check\nChoose (1/2): ')



    if __name__ == "__main__":
        main()