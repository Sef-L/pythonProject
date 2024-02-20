# number_checker.py


def evenodd(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd")


def chkPstNgt(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("0")


def main():

    # TODO: Prompt the user to enter an integer and store it in the variable 'number'.
    number = int(input("Enter Number "))

    # TODO: Determine if the number is positive, negative, or zero and print the appropriate message.
    # Hint: Use comparison operators (>, <, ==) to check if the number is positive, negative, or zero.
    '''
    if number > 0 :
    print("positive")
    elif number < 0 :
    print("negative")
    else:
    print("0")
    '''
    chkPstNgt(number)

    # TODO: Check if the number is even or odd and print the message.
    # Hint: Use the modulo operator (%) to determine if a number is even or odd.
    '''
    if number % 2 == 0:
    print("even number")
    else:
    print("odd")
    '''
    evenodd(number)

    # TODO: Check if the number is divisible by 5 and print the message.
    # Hint: To check if a number is divisible by 5, the remainder when divided by 5 should be 0.
    division_number= float(input("enter a number to divide "))
    if number % division_number ==0:
        print(f"it's divisible by {division_number}")
    else:
        print(f"number not divisible by {division_number}")
    # Advanced Task: If the number is positive and even, check if it is also a multiple of 10.
# Hint: Combine conditions using 'and'. A number is a multiple of 10 if the remainder when divided by 10 is 0.


if __name__ == "__main__":
    main()