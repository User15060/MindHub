🧠 DEFINITION 🧠

The `def` keyword is used to create a function, which is a reusable block of code designed to perform a specific task.

In simple terms:

* It’s like giving a name to a recipe.
* You can call (execute) it whenever you need that recipe.
* A function can take inputs (**parameters**) and send back a result using **return**.


✅ Example:

```python
def student_report(name, grades):  # Function with 2 parameters: name (str) and grades (list)

    # Check if the list is empty
    if not grades:
        return f"{name} has no grades to report."
    
    avg = sum(grades) / len(grades)  # Calculate average
    
    if avg >= 10:
        status = "Passed ✅"
    else:
        status = "Failed ❌"
    
    # Return the final report as a formatted string
    return f"Report for {name}:\n- Average: {avg:.2f}\n- Result: {status}\n"

# Function calls
print(student_report("Alice", [12, 15, 14, 9]))
print(student_report("Bob", [8, 7, 6]))
print(student_report("Charlie", []))
```


📌 Notes:

* A **parameter** is a variable defined in the function header that allows you to pass information into the function.
* The **return** statement sends a value back to the caller of the function.
