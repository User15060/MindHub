🧠 DEFINITION 🧠

A `while` loop repeats a block of code as long as a given condition is **True**.
It's useful when you don’t know in advance how many times you need to repeat.


✅ Example:

```python
print("Start of loop")
n = 0
while n < 5:  # Condition is True as long as n < 5
    print(str(n))
    n = n + 1  # Increment n to avoid infinite loop
print("End of loop")


password = None
while not password == "password":  # Keep asking until correct password
    password = input("Enter password: ")
print("Access granted!")
```


📌 Notes:

* If the condition never becomes **False**, the loop will run forever (infinite loop).
* Always make sure to update variables inside the loop!
