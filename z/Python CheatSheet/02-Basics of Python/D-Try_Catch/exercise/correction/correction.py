# Ask for user's name
name = input("What's your name? ")

# Ask for two numbers with error handling
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Calculate the sum
    result = num1 + num2

    # Display the welcome message and the result
    print(f"\nWelcome {name}, here is the result of the sum: {int(result)}")

except ValueError:
    print("\nInvalid input. Please enter numeric values.")
    

# :Notes:
# /n -> is called a newline character. It is used to move the cursor to the next line
