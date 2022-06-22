# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # set window title and size
        self.setWindowTitle("Simple Calculator")
        # first is width, second height
        self.setFixedSize(200, 200)

        # create a QGrid layout and apply to window
        qGrid01 = QGridLayout()
        self.setLayout(qGrid01)

        # Create three labels called num1, num2 and result
        labelNum1 = QLabel("Num 1: ")
        labelNum2 = QLabel("Num 2: ")
        labelResult = QLabel("Result: ")
        self.labelDisplay = QLabel("0")

        #create an instance of a QPushButton
        buttonCalc = QPushButton("Add")
        buttonMul = QPushButton("Muliply")
        buttonDiv = QPushButton("Divide")
        buttonSub = QPushButton("Substract")


        # Create two instances of QLineEdits
        self.qLineEditNum1 = QLineEdit("0")
        self.qLineEditNum2 = QLineEdit("0")

        # Place the labels on the layout (first is row, second is collumm)
        qGrid01.addWidget(labelNum1, 0, 0)
        qGrid01.addWidget(self.qLineEditNum1, 0, 1)
        qGrid01.addWidget(labelNum2, 1, 0)
        qGrid01.addWidget(self.qLineEditNum2, 1, 1)
        qGrid01.addWidget(labelResult, 2, 0)
        qGrid01.addWidget(self.labelDisplay, 2, 1)
        qGrid01.addWidget(buttonCalc, 3, 0)
        qGrid01.addWidget(buttonMul, 3, 1)
        qGrid01.addWidget(buttonDiv, 4, 0)
        qGrid01.addWidget(buttonSub, 4, 1)

        # state the function to be called when the button is clicked
        buttonCalc.clicked.connect(self.Calculate)
        buttonMul.clicked.connect(self.Multiply)
        buttonDiv.clicked.connect(self.Divide)
        buttonSub.clicked.connect(self.Substract)

    # Define the Calculate function
    def Calculate(self):
        print("You pressed the calculate button")
        # Convert the input(String) into numbers (int, float, etc)
        num1 = float(self.qLineEditNum1.text())
        num2 = float(self.qLineEditNum2.text())
        result = num1+num2
        print(result)
        # Convert the number back to string to be displayed
        self.labelDisplay.setText(str(result))

    def Multiply(self):
        print("You pressed the Multiply button")
        # Convert the input(String) into numbers (int, float, etc)
        num1 = float(self.qLineEditNum1.text())
        num2 = float(self.qLineEditNum2.text())
        result = num1*num2
        print(result)
        # Convert the number back to string to be displayed
        self.labelDisplay.setText(str(result))

    def Divide(self):
        print("You pressed the Divide button")
        # Convert the input(String) into numbers (int, float, etc)
        num1 = float(self.qLineEditNum1.text())
        num2 = float(self.qLineEditNum2.text())
        result = num1/num2
        print(result)
        # Convert the number back to string to be displayed
        self.labelDisplay.setText(str(result))

    def Substract(self):
        print("You pressed the Substract button")
        # Convert the input(String) into numbers (int, float, etc)
        num1 = float(self.qLineEditNum1.text())
        num2 = float(self.qLineEditNum2.text())
        result = num1-num2
        print(result)
        # Convert the number back to string to be displayed
        self.labelDisplay.setText(str(result))



# Every GUI we create using Python and
# the PyQt5 framework will contain an instance
# of the QApplication class
app = QApplication(sys.argv)

# Create an instance of a Window
window = MainWindow()

# Display the window instance when the application runs
window.show()

# Create an event loop
app.exec_()