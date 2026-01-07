

#  Tkinter Calculator Application

##  Overview

This is a **simple GUI-based calculator** built using **Python’s Tkinter library**.
It performs basic arithmetic operations such as **Addition, Subtraction, Multiplication, and Division** with a clean and colorful user interface.

---

##  Technologies Used

* Python 
* **Tkinter (GUI Library)**

---

##  Features

* Numeric buttons (0–9)
* Arithmetic operations:

  * ➕ Addition
  * ➖ Subtraction
  * ✖ Multiplication
  * ➗ Division
* Clear button to reset input
* Equals button to display result
* Styled buttons and entry field
* User-friendly interface with colors

---

##  GUI Description

* **Window size:** `350 x 500`
* **Background color:** Dark blue (`#2c3e50`)
* **Display box:** Center-aligned entry widget
* **Buttons:** Color-coded for better UX

  * Numbers → Light blue
  * Operators → Orange
  * Equals → Green
  * Clear → Red

---

##  How It Works

1. User clicks number buttons to enter values.
2. Clicking an operator (`+ - * /`) stores the first number.
3. User enters the second number.
4. Pressing `=` performs the selected operation.
5. Result is displayed in the entry box.
6. `Clear` resets the input field.

---

##  How to Run the Program

1. Make sure **Python 3** is installed.
2. Save the file as `calculator.py`
3. Run the file:

   ```bash
   python calculator.py
   ```

---

##  Code Structure

* `click(num)` → Handles number button clicks
* `add(), sub(), mul(), div()` → Store operation and first number
* `equal()` → Performs calculation
* `clear()` → Clears the display
* `Entry()` → Displays input and output
* `Button()` → Handles user interaction





