🧠 DEFINITION 🧠

The `try/except` blocks are used to handle errors gracefully, preventing the program from crashing.
You put the code that might fail inside **try**, and handle errors inside **except**.

✅ Example:

```python
try:
    age = int(input("Enter your age: "))  # This may fail if input is not a number
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"You are {age} years old.")
```

📌 Notes:

* The **try** block contains code that may raise an error.
* The **except** block runs only if an error occurs.
* The **else** block runs only if no error happened.
