# str (string) -> Represents a sequence of characters (text)
name = "User"
# Can be enclosed in 'User' or "User"

# int (integer) -> Integer number (positive or negative, without decimals)
age = 25

# float (float) -> Real number with decimals (floating point)
temperature = 36.5

# bool (boolean) -> Logical value: True or False
is_logged_in = True

# list (list) -> Ordered, mutable collection of values
fruits = ["apple", "banana", "cherry"]
mixed = [1, "yes", True]
# Can contain mixed types

# tuple (tuple) -> Ordered, immutable (non-modifiable) collection
coordinates = (4, 5)
# Faster than lists

# dict (dictionary) -> Unordered collection of "key: value pairs"
person = {"name": "Alice", "age": 25}
# Access by key: person["name"]

# set (set) -> Unordered collection without duplicates
unique_numbers = {1, 2, 3, 3}
# Duplicates are automatically removed

#NoneType (NoneType) -> Represents the absence of a value (None)
result = None
# Often used to initialize a variable without a value


# Checking types with type()
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(fruits))   # <class 'list'>


# :Notes:
"""
Don’t worry if some things seem unclear to you. We will go over them in detail later, step by step.
For now, just remember the most important ones:
- str
- int
- float
- bool
"""