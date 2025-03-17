1)Calculator Class (Handles Calculations)
This class is responsible for storing and evaluating mathematical expressions.

Methods:
*__init__(self):
Initializes an empty string self.expression to store the mathematical expression.
*add_to_expression(self, char: str):
Adds a character (number or operator) to the expression.
*remove_last_character(self):
Removes the last character from the expression.
*clear_expression(self):
Clears the entire expression (sets it to an empty string).
*calculate(self):
Tries to evaluate the current expression using eval().
*Handles errors:
If division by zero occurs, it returns "Error: Division by zero".
If there's an invalid expression, it returns "Error: Invalid expression".
*get_expression(self):
Returns the current mathematical expression.

2)CalculatorWindow Class (GUI)
This class creates the graphical user interface (GUI) for the calculator using PyQt5.

Methods:
*__init__(self):
Calls super().__init__() to initialize the QWidget.
Creates an instance of Calculator (model) and calls initUI() to set up the UI.
*initUI(self):
Sets the window title and size.
Creates a text input field (QLineEdit) to display the expression.
Uses QGridLayout to arrange buttons in a 4x4 grid.
Connects button clicks to the on_button_click() method.
*on_button_click(self, button_text):
*Handles button clicks:
If = is pressed, calls calculate() and updates the input field with the result.
If C is pressed, clears the expression and the input field.
Otherwise, adds the button's text to the expression and updates the input field.

3)Main Execution (if __name__ == "__main__")
Initializes the PyQt5 application (QApplication).
Creates an instance of CalculatorWindow.
Runs the application (app.exec_()), keeping the window open.
