🧠 DEFINITION 🧠

A variable is a name that stores a value in memory so you can reuse it later in your program.

In simple terms:

* It’s like a label on a box that tells you what’s inside.
* The value inside can change while the program is running.


✅ Example:

```python
# str (string) -> sequence of characters (text)
name = "User"

# int (integer) -> whole number (positive or negative, no decimals)
age = 25

# float (floating point) -> real number with decimals
temperature = 36.5

# bool (boolean) -> logical value: True or False
is_logged_in = True

# list -> ordered, mutable collection of values
fruits = ["apple", "banana", "cherry"]
mixed = [1, "yes", True]  # lists can mix types

# tuple -> ordered, immutable (non-modifiable) collection
coordinates = (4, 5)

# dict (dictionary) -> key/value pairs
person = {"name": "Alice", "age": 25}
print(person["name"])  # Access by key

# set -> unordered collection without duplicates
unique_numbers = {1, 2, 3, 3}  # duplicates are removed

# NoneType -> absence of a value
result = None

# Checking types
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(fruits))  # <class 'list'>
```


✅ Operations with variables:

```python
# String concatenation (str + str)
print("25" + "1")   # Result: "251"

# Number addition (int + int)
print(25 + 1)       # Result: 26

# Global variable
global name  # Variable accessible everywhere in the file
name = "User"

# String concatenation
print("Hello " + name + ", How are you?")  # Classic
print(f"Hello {name}")                     # f-string (recommended)
```


📌 Notes:

* Focus first on the most common types: **str, int, float, bool**.
* Use `type()` to check a variable’s type.
* F-strings (Python ≥ 3.6) are the cleanest way to mix text and variables.
* `global` allows a variable to be shared across functions, but should be used carefully.
