# Library Imports
# import * = import all (NOT RECOMMENDED)
from PyQt5.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #set window size and title
        self.setWindowTitle("My app 01")
        #
        self.setFixedSize(500, 500)

        # Create a layout and apply to window
        # a QGridLayout is similar to an excel Spreadsheet
        qGrid = QGridLayout()

        # Apply the layout to the window
        self.setLayout(qGrid)

        # Qlabels
        self.label01 = QLabel("Hello world")
        self.label02 = QLabel("Hello world 02")

        # Create QPushButtons
        button01 = QPushButton("Update")
        button02 = QPushButton("Original")

        # Place the label on the grid
        qGrid.addWidget(self.label01, 0, 0)
        qGrid.addWidget(self.label02, 0, 1)
        # Place the QPushBUtton on the grig
        qGrid.addWidget(button01, 1, 0)
        qGrid.addWidget(button02, 1, 1)

        # state the function to be called when the user
        # clicks the button named button01
        button01.clicked.connect(self.button01Clicked)

        # state the function to be called when the user
        # clicks the button named button02
        button02.clicked.connect(self.button02Clicked)

    def button01Clicked(self):
        print("You clicked Button 01")
        self.label01.setText("Button 01 clicked")
        self.label02.setText("Text Updated by Button01")

    def button02Clicked(self):
        print("You clicked Button 02")
        self.label01.setText("Hello World")
        self.label02.setText("Hello World")





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