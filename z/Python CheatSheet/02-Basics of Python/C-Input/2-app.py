name = input("What's your name? ")
age = input("What's your age? ")  # age is a string here

# Convert age to integer to use as a number
age = int(age)

print(f"Hi, my name is {name} and I am {age} years old.")


# :Notes:
"""
input() always returns a string.
To use numeric input for calculations, you must convert it (int() or float()).
"""