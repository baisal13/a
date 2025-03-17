from main import Calculator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
import sys

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.calculator = Calculator()  # Model instance
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        grid_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, button_text):
        if button_text == '=':
            result = self.calculator.calculate()
            self.input_field.setText(str(result))
        elif button_text == 'C':
            self.calculator.clear_expression()
            self.input_field.clear()
        else:
            self.calculator.add_to_expression(button_text)
            self.input_field.setText(self.calculator.get_expression())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())