try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"You are {age} years old.")


# :Note:
"""
The try block contains code that may raise an error.
The except block runs only if an error occurs.
The else block runs only if no error happened.
"""