while True:
    while True:
        operation = input("Do you want to add(1), subtract(2), multiply(3), divide(4)? Enter 0 to exit: ").strip()
        if operation in ["1", "2", "3", "4", "0"]:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 4.")

    if operation == "0":
        print("Exiting the calculator.")
        break

    # number1 input loop
    while True:
        try:
            number1 = int(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # number2 input loop
    while True:
        try:
            number2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # calculation
    if operation == "1":
        print(number1 + number2)
    elif operation == "2":
        print(number1 - number2)
    elif operation == "3":
        print(number1 * number2)
    elif operation == "4":
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(number1 / number2)
