# Python Exercise

Write a Python program that creates a **Magic Number Game**:

1. The program chooses a random number between **1 and 10**
2. The user has **3 lives** to guess the number
3. After each wrong guess, the program reduces the number of lives and tells the user how many lives are left
4. If the user finds the magic number → print a winning message and stop the game
5. If the user loses all lives → print a losing message
6. At the end, the program asks if the user wants to **play again** or **quit**

---

## ✅ Example Output

```
Welcome to the Magic Number Game!
Guess the magic number between 1 and 10
You have 3 lives.

Enter your guess: 5
Wrong! You have 2 lives left.

Enter your guess: 7
Wrong! You have 1 life left.

Enter your guess: 2
Congratulations! You found the magic number!

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye!
```

or

```
Welcome to the Magic Number Game!
Guess the magic number between 1 and 10
You have 3 lives.

Enter your guess: 4
Wrong! You have 2 lives left.

Enter your guess: 9
Wrong! You have 1 life left.

Enter your guess: 6
Sorry, you lost! The magic number was 3.

Do you want to play again? (yes/no): yes
```
