def student_report(name, grades, passing_grade=10):  # Function with an optional parameter: passing_grade (default = 10).
    # Check if the list is empty
    if not grades:
        return f"{name} has no grades to report."
    
    avg = sum(grades) / len(grades)  # Calculate average
    
    if avg >= passing_grade:  # Use optional parameter instead of fixed 10
        status = "Passed ✅"
    else:
        status = "Failed ❌"
    
    # Return the final report as a formatted string
    return f"Report for {name}:\n- Average: {avg:.2f}\n- Result: {status}\n"


print(student_report("Alice", [12, 15, 14, 9]))           # Uses default passing_grade = 10
print(student_report("Bob", [8, 7, 6]))                   # Fails with default passing_grade = 10
print(student_report("Charlie", [12, 9, 11], 12))         # Custom passing_grade = 12
print(student_report("David", []))                        # No grades case


# :Notes:
"""
A parameter is a variable defined in the function header that allows you to pass information into the function.
The return statement sends a value back to the caller of the function.
An optional parameter (with a default value) makes the function more flexible.
"""