print("Start of loop")
n = 0
while n < 5:  # Condition is True as long as n < 5
    print(str(n))
    n = n + 1  # Increment n to avoid infinite loop
print("End of loop")


password = None
while not password == "password":
    password = input("Enter password: ")
print("Access granted!")


# :Notes:
"""
If the condition never becomes False, the loop will run forever (infinite loop).
Make sure to update the variables inside the loop!
"""