### Number Guessing Game Overview:

This Python program is a fun and engaging **Number Guessing Game** where the user has five chances to guess a randomly generated number between 1 and 100. Here's a breakdown of how the game works and how the code operates:

---

### **How It Works**
1. **Welcome Message**  
   When the game starts, the user is greeted with a playful message:
   > *"Hello! This is Isaeus Guiang, and this is a number guessing game. You have 5 chances to guess the number, or... you will die :)."*

2. **Random Number Generation**  
   The program generates a random integer between 1 and 100 using `random.randint(1, 100)`. This number will be the target the user must guess.

3. **User Input & Validation**  
   - The user has five attempts to guess the number.
   - If the user enters anything other than a valid integer, they are prompted to enter a number again without losing an attempt.

4. **Feedback on Guesses**  
   After each guess, the program provides feedback:
   - If the guess is **too low**, the message is: *"Too low! Try again."*
   - If the guess is **too high**, the message is: *"Too high! Try again."*
   - If the guess is correct, the program congratulates the user and exits the game.

5. **Game Over**  
   - If the user runs out of attempts without guessing the number, the program reveals the correct number with the message:
     > *"Oops, sorry, the number was [number]. You are going to die :)."

---

### **Features of the Code**
1. **Random Number Generation**  
   The game uses `random.randint(1, 100)` to create an unpredictable number, ensuring a fair and exciting challenge for every playthrough.

2. **Input Validation**  
   The code prevents invalid inputs (like letters or symbols) from counting as attempts, using a `try-except` block to handle errors gracefully.

3. **Attempts Tracking**  
   The `guess_counter` variable keeps track of how many guesses the user has made, ensuring the user gets exactly five chances.

4. **Dynamic Feedback**  
   The game provides helpful hints after each incorrect guess, guiding the player toward the correct number.

5. **Humorous Twist**  
   The playful messaging adds a fun, lighthearted tone to the game, making it more entertaining.

---

### **Sample Gameplay**
1. **Start of the Game:**  
   ```
   Hello! This is Isaeus Guiang, and this is a number guessing game. 
   You have 5 chances to guess the number, or...
   you will die :).
   ```

2. **User Makes Guesses:**  
   ```
   Attempt 1/5 - Your Guess :) -> 50
   Too high! Try again.
   Attempt 2/5 - Your Guess :) -> 25
   Too low! Try again.
   Attempt 3/5 - Your Guess :) -> 37
   Too low! Try again.
   Attempt 4/5 - Your Guess :) -> 43
   Too high! Try again.
   Attempt 5/5 - Your Guess :) -> 40
   Oops, sorry, the number was 42. You are going to die :).
   ```

3. **Correct Guess (Before 5 Attempts):**  
   ```
   Attempt 3/5 - Your Guess :) -> 42
   The number is 42, and you guessed it right in 3 attempt(s)!
   ```

---

This program is a great way to practice basic Python concepts, including loops, conditionals, user input, and error handling, while also enjoying a fun guessing game!
