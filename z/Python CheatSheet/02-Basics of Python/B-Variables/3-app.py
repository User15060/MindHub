# String concatenation (str + str)
age = "25" + "1"     # Result: "251" (string)

# Number addition (int + int or float + float)
age = 25 + 1        # Result: 26 (number)


global name # Global variable accessible everywhere in the file

name = "User"

# String concatenation
print("Hello " + name + ", How are you?")     # classic concatenation
print(f"Hello {name}")                        # f-string (recommended)
"""
(f"Hello {name}") is a formatted string introduced in Python 3.6, and it's the easiest way
to mix variables and text.
"""

