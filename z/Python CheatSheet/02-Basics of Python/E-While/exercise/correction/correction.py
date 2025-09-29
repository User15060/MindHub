# Ask for user's name
name = input("What's your name? ")

while True:
    result = 0

    # Loop for the first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break  
        except ValueError:
            print("Invalid input. Please enter a numeric value for the first number.")

    # Loop for the second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break  
        except ValueError:
            print("Invalid input. Please enter a numeric value for the second number.")

    # Calculate the sum
    result = num1 + num2

    # Display the welcome message and the result
    # int(result) converts float to integer (removes decimals)
    print(f"\nWelcome {name}, here is the result of the sum: {int(result)}")

    # Ask if the user wants to continue
    continue_choice = input("\nDo you want to add more numbers? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print(f"Goodbye {name}!")
        break


# :Notes:
# \n -> newline character. Moves the cursor to the next line.
# strip() -> removes spaces from the beginning and end of the string.
# lower() -> converts the string to lowercase (useful for comparing 'YES', 'Yes', 'yes').
# break -> exits the nearest enclosing loop.
