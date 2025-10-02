age = 20

if age < 12: # This block runs if the age is less than 12
    print("You are a child.")
elif age < 18: # This block runs if the first condition is False AND the age is less than 18
    print("You are a teenager.")
else: # This block runs if none of the above conditions are True
    print("You are an adult.")


# :Notes:
"""
if checks the first condition.
elif (short for *else if*) checks additional conditions if the first one is False.
else runs if none of the previous conditions are True.
Only the first **True** block will execute.
"""