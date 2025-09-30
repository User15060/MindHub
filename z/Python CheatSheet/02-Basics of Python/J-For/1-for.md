🧠 DEFINITION 🧠

A `for` loop is used to iterate (go through) a sequence such as a list, tuple, string, or a range of numbers.
It executes the block of code once for each element in the sequence.


✅ Example:

```python
# For loop that goes through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

# For loop with range()
for i in range(5):
    print("Iteration number:", i)
```


📌 Notes:

* `for` loops are useful when you know exactly how many times you want to repeat.
* `range(n)` generates numbers from 0 up to (but not including) `n`.
* The loop variable (like `fruit` or `i`) takes the value of each element in the sequence.
